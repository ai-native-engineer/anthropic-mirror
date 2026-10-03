<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-QQ2P9M9V -->

# ANT-2026-QQ2P9M9V · openexr

## heap-buffer-overflow high

[CVE-2026-45696](https://nvd.nist.gov/vuln/detail/CVE-2026-45696)

Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-QQ2P9M9V: Heap-buffer-overflow in internal\_ht.cpp:305

While decoding a crafted OpenEXR file that uses HTJ2K (High-Throughput JPEG 2000) compression, ht\_undo\_impl() in OpenEXRCore reads 4 bytes past the end of a buffer allocated by the bundled OpenJPH codestream allocator. The overflow is reached through the normal file-decoding path (exr\_uncompress\_chunk → internal\_exr\_undo\_ht → ht\_undo\_impl), so any application that opens untrusted EXR files can hit it. The attacker controls the EXR/HTJ2K codestream contents that determine the buffer size and the read offset. The result is an out-of-bounds read that could cause a crash (DoS) or leak adjacent heap memory.

**Project:** openexr
**Location:** `internal_ht.cpp:305`

ASAN: "READ of size 4 at 0x7aed229e5428 ... heap-buffer-overflow ... internal\_ht.cpp:305:45 in ht\_undo\_impl". The read lands immediately after a 21033-byte region allocated via ojph::local::codestream::finalize\_alloc(), indicating ht\_undo\_impl pulls a 32-bit value from the OpenJPH-decoded line/component buffer without validating that the decoded codestream dimensions match the EXR channel/scanline dimensions it is iterating over.

**Crash trace (truncated — full trace in attached crash.log):**

```
INFO: Running with entropic power schedule (0xFF, 100).
INFO: Seed: 2979886539
INFO: Loaded 1 modules   (45624 inline 8-bit counters): 45624 [0x58074f7c1bf0, 0x58074f7cce28),
INFO: Loaded 1 PC tables (45624 PCs): 45624 [0x58074f7cce28,0x58074f87f1a8),
/out/openexr_exrcorecheck_fuzzer: Running 1 inputs 1 time(s) each.
Running: /tmp/poc
EXIT_CODE:1

=== ASAN Report ===
=================================================================
==26==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x7aed229e5428 at pc 0x58074f458a4a bp 0x7ffe094f96f0 sp 0x7ffe094f96e8
READ of size 4 at 0x7aed229e5428 thread T0
    #0 0x58074f458a49 in ht_undo_impl /src/openexr/src/lib/OpenEXRCore/internal_ht.cpp:305:45
    #1 0x58074f458a49 in internal_exr_undo_ht /src/openexr/src/lib/OpenEXRCore/internal_ht.cpp:338:16
    #2 0x58074f3f5d07 in exr_uncompress_chunk /src/openexr/src/lib/OpenEXRCore/compression.c:542:14
    #3 0x58074f4211b2 in exr_decoding_run /src/openexr/src/lib/OpenEXRCore/decoding.c:580:14
    #4 0x58074f1a7be6 in readCoreScanlinePart /src/openexr/src/lib/OpenEXRUtil/ImfCheckFile.cpp:1447:18
    #5 0x58074f1a7be6 in Imf_4_0::(anonymous namespace)::checkCoreFile(_priv_exr_context_t*, bool, bool) /src/openexr/src/lib/OpenEXRUtil/ImfCheckFile.cpp:1675:17
    #6 0x58074f1a53da in runCoreChecks /src/openexr/src/lib/OpenEXRUtil/ImfCheckFile.cpp:1817:15
    #7 0x58074f1a53da in Imf_4_0::checkOpenEXRFile(char const*, unsigned long, bool, bool, bool) /src/openexr/src/lib/OpenEXRUtil/ImfCheckFile.cpp:1849:16
    [... 25 more frames — full trace in crash.log]
```

1. Craft an EXR file with a scanline part whose chunk uses HTJ2K compression and whose embedded JPEG 2000 codestream declares dimensions/components smaller than the EXR channel layout expects
2. Deliver the file to the victim (download, email attachment, asset pipeline, thumbnailer)
3. Victim application calls exr\_decoding\_run / exr\_uncompress\_chunk on the part
4. ht\_undo\_impl reads a 32-bit sample past the end of the OpenJPH-allocated line buffer

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-QQ2P9M9V.

---

**Reference:** ANT-2026-QQ2P9M9V

Triage and disclosure were performed by Ada Logics.

1. 2026-03-24
2. 2026-05-13
3. 2026-05-13
4. 2026-05-28
5. 2026-07-21

7a7e55e50f61c3afc2409fdfb1614d90c34fba559bb37c9a31661778cd36575196c68f44622667cc78c4e05d378670762f40034923f73a18f0f0f3528098a378

Committed 2026-05-13 17:56 UTC

Revealed 2026-07-21 05:04 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-QQ2P9M9V%22%2C%22bug_class%22%3A%22Heap-buffer-overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-24T18%3A27%3A21%2B00%3A00%22%2C%22description%22%3A%22While%20decoding%20a%20crafted%20OpenEXR%20file%20that%20uses%20HTJ2K%20%28High-Throughput%20JPEG%202000%29%20compression%2C%20ht_undo_impl%28%29%20in%20OpenEXRCore%20reads%204%20bytes%20past%20the%20end%20of%20a%20buffer%20allocated%20by%20the%20bundled%20OpenJPH%20codestream%20allocator.%20The%20overflow%20is%20reached%20through%20the%20normal%20file-decoding%20path%20%28exr_uncompress_chunk%20%E2%86%92%20internal_exr_undo_ht%20%E2%86%92%20ht_undo_impl%29%2C%20so%20any%20application%20that%20opens%20untrusted%20EXR%20files%20can%20hit%20it.%20The%20attacker%20controls%20the%20EXR/HTJ2K%20codestream%20contents%20that%20determine%20the%20buffer%20size%20and%20the%20read%20offset.%20The%20result%20is%20an%20out-of-bounds%20read%20that%20could%20cause%20a%20crash%20%28DoS%29%20or%20leak%20adjacent%20heap%20memory.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22internal_ht.cpp%3A305%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22openexr%22%2C%22reproduction%22%3A%5B%221.%20Craft%20an%20EXR%20file%20with%20a%20scanline%20part%20whose%20chunk%20uses%20HTJ2K%20compression%20and%20whose%20embedded%20JPEG%202000%20codestream%20declares%20dimensions/components%20smaller%20than%20the%20EXR%20channel%20layout%20expects%22%2C%222.%20Deliver%20the%20file%20to%20the%20victim%20%28download%2C%20email%20attachment%2C%20asset%20pipeline%2C%20thumbnailer%29%22%2C%223.%20Victim%20application%20calls%20exr_decoding_run%20/%20exr_uncompress_chunk%20on%20the%20part%22%2C%224.%20ht_undo_impl%20reads%20a%2032-bit%20sample%20past%20the%20end%20of%20the%20OpenJPH-allocated%20line%20buffer%22%5D%2C%22technical_details%22%3A%22ASAN%3A%20%5C%22READ%20of%20size%204%20at%200x7aed229e5428%20...%20heap-buffer-overflow%20...%20internal_ht.cpp%3A305%3A45%20in%20ht_undo_impl%5C%22.%20The%20read%20lands%20immediately%20after%20a%2021033-byte%20region%20allocated%20via%20ojph%3A%3Alocal%3A%3Acodestream%3A%3Afinalize_alloc%28%29%2C%20indicating%20ht_undo_impl%20pulls%20a%2032-bit%20value%20from%20the%20OpenJPH-decoded%20line/component%20buffer%20without%20validating%20that%20the%20decoded%20codestream%20dimensions%20match%20the%20EXR%20channel/scanline%20dimensions%20it%20is%20iterating%20over.%22%2C%22title%22%3A%22Heap-buffer-overflow%20in%20internal_ht.cpp%3A305%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-QQ2P9M9V",
  "bug_class": "Heap-buffer-overflow",
  "created_at": "2026-03-24T18:27:21+00:00",
  "description": "While decoding a crafted OpenEXR file that uses HTJ2K (High-Throughput JPEG 2000) compression, ht_undo_impl() in OpenEXRCore reads 4 bytes past the end of a buffer allocated by the bundled OpenJPH codestream allocator. The overflow is reached through the normal file-decoding path (exr_uncompress_chunk → internal_exr_undo_ht → ht_undo_impl), so any application that opens untrusted EXR files can hit it. The attacker controls the EXR/HTJ2K codestream contents that determine the buffer size and the read offset. The result is an out-of-bounds read that could cause a crash (DoS) or leak adjacent heap memory.",
  "location": "internal_ht.cpp:305",
  "project": "openexr",
    "1. Craft an EXR file with a scanline part whose chunk uses HTJ2K compression and whose embedded JPEG 2000 codestream declares dimensions/components smaller than the EXR channel layout expects",
    "2. Deliver the file to the victim (download, email attachment, asset pipeline, thumbnailer)",
    "3. Victim application calls exr_decoding_run / exr_uncompress_chunk on the part",
    "4. ht_undo_impl reads a 32-bit sample past the end of the OpenJPH-allocated line buffer"
  "technical_details": "ASAN: \"READ of size 4 at 0x7aed229e5428 ... heap-buffer-overflow ... internal_ht.cpp:305:45 in ht_undo_impl\". The read lands immediately after a 21033-byte region allocated via ojph::local::codestream::finalize_alloc(), indicating ht_undo_impl pulls a 32-bit value from the OpenJPH-decoded line/component buffer without validating that the decoded codestream dimensions match the EXR channel/scanline dimensions it is iterating over.",
  "title": "Heap-buffer-overflow in internal_ht.cpp:305",
```
