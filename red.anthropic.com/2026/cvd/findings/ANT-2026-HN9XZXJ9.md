<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-HN9XZXJ9 -->

# ANT-2026-HN9XZXJ9 · freerdp/freerdp

## heap-buffer-overflow critical

[CVE-2026-45700](https://nvd.nist.gov/vuln/detail/CVE-2026-45700)
[GHSA-mpxh-8fq3-x8mh](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-mpxh-8fq3-x8mh)
[GHSA-mvpx-xj7r-3p3r](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-mvpx-xj7r-3p3r)
[GHSA-p6r2-4hgm-m6ff](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-p6r2-4hgm-m6ff)

Claude critical
Security research firm critical (revised; sealed as medium)
Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-HN9XZXJ9: heap-buffer-overflow write (attacker-controlled offset, partially-controlled data via rle delta values; up to ~15kb overwrite past ptempdata with these parameters, further with larger nxdst) in planar.c:472

In FreeRDP's planar bitmap codec (libfreerdp/codec/planar.c), the X-axis bounds check at line 968 validates nXDst against the caller's destination stride (nDstStep) rather than the internal temp buffer stride (nTempStep) when the temp-buffer path is active. A malicious RDP server can send RDPGFX planar data with a large nXDst (e.g. 6000) that passes the check (24016 <= 28032) but causes planar\_decompress\_plane\_rle to write up to offset ~40131 into a 24576-byte pTempData allocation. The attacker controls the destination offset and RLE-decoded byte content, yielding an out-of-bounds heap write in the connecting FreeRDP client.

**Project:** freerdp/freerdp
**Location:** `planar.c:472`

ASAN: heap-buffer-overflow WRITE of size 1 at 0x52b0000062e2, 170 bytes past the end of a 24632-byte heap region. The bounds check at planar.c:968 compares against nDstStep (28032) instead of nTempStep (256), so when the temp-buffer code path is used the check does not actually constrain writes to pTempData. Large attacker-supplied nXDst values therefore pass validation and drive OOB writes during RLE plane decompression.

**Crash trace (truncated — full trace in attached crash.log):**

```
The PoC is a C harness (`planar_poc_gfx.c`, 6225 bytes) that demonstrates a heap-buffer-overflow WRITE vulnerability in FreeRDP's planar codec (`libfreerdp/codec/planar.c`).

**Root Cause**: The X-axis bounds check at `planar.c:968` compares against `nDstStep` (the caller's destination stride of 28032) instead of `nTempStep` (the internal temp buffer stride of 256) when the temp buffer code path is active. This allows writing far past the end of `pTempData` (24576 bytes) when `nXDst` is large.

**Reproduction**: The harness simulates a malicious RDPGFX server scenario:
1. Creates a planar context sized 64x64 (pTempData = 24576 bytes, nTempStep = 256)
2. Calls `freerdp_bitmap_decompress_planar()` with nXDst=6000, which passes the buggy bounds check (24016 <= 28032) but results in writes up to offset 40131 in the 24576-byte temp buffer

**All 3 runs in a fresh container produced identical results**:
- ERROR: AddressSanitizer: heap-buffer-overflow on address 0x52b0000062e2
- WRITE of size 1 at `planar_decompress_plane_rle` (planar.c:472)
- Called from `freerdp_bitmap_decompress_planar` (planar.c:977)
- 170 bytes past end of 24632-byte heap allocation
- Exit code: 1

The vulnerability is exploitable in a realistic attack scenario where a malicious RDP server sends crafted RDPGFX planar data to a FreeRDP client.
```

1. Server negotiates RDPGFX and sends planar-encoded bitmap data
2. Planar context is initialized small (e.g. 64x64), allocating a ~24KB pTempData buffer with nTempStep=256
3. Server supplies a large nXDst (e.g. 6000) alongside a large caller nDstStep (e.g. 28032)
4. Bounds check at planar.c:968 compares 4\*nXDst+16 against nDstStep instead of nTempStep and passes
5. planar\_decompress\_plane\_rle writes RLE-decoded bytes into pTempData at offsets up to ~40131, overflowing the 24576-byte buffer

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-HN9XZXJ9.

---

**Reference:** ANT-2026-HN9XZXJ9

Triage and disclosure were performed by Trail of Bits. The severity shown is the firm's current assessment; the report was sealed with the firm's earlier assessment of medium.

:   critical (revised; sealed as medium)

1. 2026-03-24
2. 2026-04-30
3. 2026-04-30
4. 2026-05-13
5. 2026-05-20

29af186542c112b5343a65f02c7172778fb1557257c7f93bae53f138452377c80bff2e5179a0fdc789f462a28ae262e222512a5257acc425172a7f894d2c5468

Committed 2026-04-30 07:03 UTC

Revealed 2026-05-20 07:40 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-HN9XZXJ9%22%2C%22bug_class%22%3A%22heap%22%2C%22claude_severity%22%3A%22critical%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-24T20%3A43%3A50%2B00%3A00%22%2C%22description%22%3A%22In%20FreeRDP%27s%20planar%20bitmap%20codec%20%28libfreerdp/codec/planar.c%29%2C%20the%20X-axis%20bounds%20check%20at%20line%20968%20validates%20nXDst%20against%20the%20caller%27s%20destination%20stride%20%28nDstStep%29%20rather%20than%20the%20internal%20temp%20buffer%20stride%20%28nTempStep%29%20when%20the%20temp-buffer%20path%20is%20active.%20A%20malicious%20RDP%20server%20can%20send%20RDPGFX%20planar%20data%20with%20a%20large%20nXDst%20%28e.g.%206000%29%20that%20passes%20the%20check%20%2824016%20%3C%3D%2028032%29%20but%20causes%20planar_decompress_plane_rle%20to%20write%20up%20to%20offset%20~40131%20into%20a%2024576-byte%20pTempData%20allocation.%20The%20attacker%20controls%20the%20destination%20offset%20and%20RLE-decoded%20byte%20content%2C%20yielding%20an%20out-of-bounds%20heap%20write%20in%20the%20connecting%20FreeRDP%20client.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22planar.c%3A472%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22freerdp%22%2C%22reproduction%22%3A%5B%221.%20Server%20negotiates%20RDPGFX%20and%20sends%20planar-encoded%20bitmap%20data%22%2C%222.%20Planar%20context%20is%20initialized%20small%20%28e.g.%2064x64%29%2C%20allocating%20a%20~24KB%20pTempData%20buffer%20with%20nTempStep%3D256%22%2C%223.%20Server%20supplies%20a%20large%20nXDst%20%28e.g.%206000%29%20alongside%20a%20large%20caller%20nDstStep%20%28e.g.%2028032%29%22%2C%224.%20Bounds%20check%20at%20planar.c%3A968%20compares%204%2AnXDst%2B16%20against%20nDstStep%20instead%20of%20nTempStep%20and%20passes%22%2C%225.%20planar_decompress_plane_rle%20writes%20RLE-decoded%20bytes%20into%20pTempData%20at%20offsets%20up%20to%20~40131%2C%20overflowing%20the%2024576-byte%20buffer%22%5D%2C%22technical_details%22%3A%22ASAN%3A%20heap-buffer-overflow%20WRITE%20of%20size%201%20at%200x52b0000062e2%2C%20170%20bytes%20past%20the%20end%20of%20a%2024632-byte%20heap%20region.%20The%20bounds%20check%20at%20planar.c%3A968%20compares%20against%20nDstStep%20%2828032%29%20instead%20of%20nTempStep%20%28256%29%2C%20so%20when%20the%20temp-buffer%20code%20path%20is%20used%20the%20check%20does%20not%20actually%20constrain%20writes%20to%20pTempData.%20Large%20attacker-supplied%20nXDst%20values%20therefore%20pass%20validation%20and%20drive%20OOB%20writes%20during%20RLE%20plane%20decompression.%22%2C%22title%22%3A%22heap-buffer-overflow%20write%20%28attacker-controlled%20offset%2C%20partially-controlled%20data%20via%20rle%20delta%20values%3B%20up%20to%20~15kb%20overwrite%20past%20ptempdata%20with%20these%20parameters%2C%20further%20with%20larger%20nxdst%29%20in%20planar.c%3A472%22%2C%22vendor_severity%22%3A%22medium%22%7D)

```
  "ant_id": "ANT-2026-HN9XZXJ9",
  "bug_class": "heap",
  "claude_severity": "critical",
  "created_at": "2026-03-24T20:43:50+00:00",
  "description": "In FreeRDP's planar bitmap codec (libfreerdp/codec/planar.c), the X-axis bounds check at line 968 validates nXDst against the caller's destination stride (nDstStep) rather than the internal temp buffer stride (nTempStep) when the temp-buffer path is active. A malicious RDP server can send RDPGFX planar data with a large nXDst (e.g. 6000) that passes the check (24016 <= 28032) but causes planar_decompress_plane_rle to write up to offset ~40131 into a 24576-byte pTempData allocation. The attacker controls the destination offset and RLE-decoded byte content, yielding an out-of-bounds heap write in the connecting FreeRDP client.",
  "location": "planar.c:472",
  "project": "freerdp",
    "1. Server negotiates RDPGFX and sends planar-encoded bitmap data",
    "2. Planar context is initialized small (e.g. 64x64), allocating a ~24KB pTempData buffer with nTempStep=256",
    "3. Server supplies a large nXDst (e.g. 6000) alongside a large caller nDstStep (e.g. 28032)",
    "4. Bounds check at planar.c:968 compares 4*nXDst+16 against nDstStep instead of nTempStep and passes",
    "5. planar_decompress_plane_rle writes RLE-decoded bytes into pTempData at offsets up to ~40131, overflowing the 24576-byte buffer"
  "technical_details": "ASAN: heap-buffer-overflow WRITE of size 1 at 0x52b0000062e2, 170 bytes past the end of a 24632-byte heap region. The bounds check at planar.c:968 compares against nDstStep (28032) instead of nTempStep (256), so when the temp-buffer code path is used the check does not actually constrain writes to pTempData. Large attacker-supplied nXDst values therefore pass validation and drive OOB writes during RLE plane decompression.",
  "title": "heap-buffer-overflow write (attacker-controlled offset, partially-controlled data via rle delta values; up to ~15kb overwrite past ptempdata with these parameters, further with larger nxdst) in planar.c:472",
  "vendor_severity": "medium"
```
