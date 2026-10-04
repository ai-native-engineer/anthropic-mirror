<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-RNHRV8B9 -->

# ANT-2026-RNHRV8B9 · libreoffice/core

## stack-buffer-overflow medium

[CVE-2026-63275](https://nvd.nist.gov/vuln/detail/CVE-2026-63275)

Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-RNHRV8B9: CFF hint-stack bound compared against double the array size

In LibreOffice's CFF font subsetter (vcl/source/fontsubset/cff.cxx), addHints() guards the hint stack with `(mnHintSize + mnStackIdx) > 2*NMAXHINTS` but mnHintStack has only NMAXHINTS (192) slots, so the guard permits twice the actual capacity. A glyph charstring that issues repeated hstemhm/vstemhm operators accumulates mnHintSize past 192 and writes up to ~192 attacker-controlled doubles (~1.5KB) past the array. CffContext is a stack automatic in ConvertCFFfontToType1(), so the overflow clobbers maCharWidth, mbDoSeac, the std::vector maExtraGlyphIds (whose corrupted internal pointers give a write/free primitive), and the calling stack frame. The path is reached during routine PDF export of any document embedding a CFF/OTF font (pdfwriter\_impl.cxx → PhysicalFontFace::CreateFontSubset → ConvertCFFfontToType1), including headless `soffice --convert-to pdf` pipelines, and hb\_subset preserves the hint operators.

**Project:** libreoffice/core
**Location:** `vcl/source/fontsubset/cff.cxx:867`

NMAXHINTS is defined as 2*96 = 192 and mnHintStack is declared with NMAXHINTS elements, but the guard at line 867 checks against 2*NMAXHINTS (384) — the author double-counted the hint-pair factor already baked into the constant. Because mnHintSize persists across every hstem/vstem/hintmask operator within a glyph, five hstemhm ops with 48 operands each drive mnHintSize to 240, under the erroneous 384 guard but past the 192-slot array, and the loop `mnHintStack[mnHintSize++] = nHintOfs` writes attacker-chosen ValType doubles off the end of the stack object.

1. Craft an OTF/CFF font with a glyph charstring containing repeated hstemhm/vstemhm operators accumulating >192 (up to 384) hint values
2. Embed the font in a document (ODT/DOCX/etc.) and deliver it to the victim or upload to a headless conversion service
3. Trigger PDF export; pdfwriter\_impl.cxx calls PhysicalFontFace::CreateFontSubset → ConvertCFFfontToType1 on the embedded font
4. convert2Type1Ops processes the glyph, addHints() passes the faulty 2\*NMAXHINTS guard and writes attacker doubles past mnHintStack[192]
5. Overwritten std::vector internal pointers are dereferenced on push\_back/destruction, yielding a write/free primitive before any stack canary check

## Suggested Fix

Change the capacity check in addHints() to compare against the actual array size (NMAXHINTS, not 2\*NMAXHINTS) so the total number of stored hint values can never exceed the mnHintStack allocation.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-RNHRV8B9.

---

**Reference:** ANT-2026-RNHRV8B9

Triage and disclosure were performed by Ada Logics.

```
diff --git a/vcl/source/fontsubset/cff.cxx b/vcl/source/fontsubset/cff.cxx
index 0aa33be342593..fb1409fcacacd 100644
--- a/vcl/source/fontsubset/cff.cxx
+++ b/vcl/source/fontsubset/cff.cxx
@@ -1472,7 +1472,7 @@ bool CffContext::addHints(bool bVerticalHints)
     if (mnStackIdx & 1)
         --mnStackIdx; //#######

-    if ((mnHintSize + mnStackIdx) > 2 * NMAXHINTS)
+    if (o3tl::make_unsigned(mnHintSize + mnStackIdx) > std::size(mnHintStack))
         return false;

     ValType nHintOfs = 0;
```

<https://github.com/LibreOffice/core/commit/1db305f340787ab7e59d089e51ac9d6fc07c2715>

1. 2026-04-02
2. 2026-07-04
3. 2026-07-24
4. 2026-08-12
5. 2026-09-28

2f4789bd452bfa96bea6d71f747bcaffcfe45f9cc4d83ece8f4cb87f0ce7f68e1186083314d35ad9a564b230684ba9fead02f1f1fcb2b6d2a0f62a5df090bcd7

Committed 2026-07-22 07:32 UTC

Revealed 2026-09-28 21:06 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-RNHRV8B9%22%2C%22bug_class%22%3A%22Stack%20Buffer%20Overflow%20/%20Off-by-N%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T01%3A54%3A45%2B00%3A00%22%2C%22description%22%3A%22In%20LibreOffice%27s%20CFF%20font%20subsetter%20%28vcl/source/fontsubset/cff.cxx%29%2C%20addHints%28%29%20guards%20the%20hint%20stack%20with%20%60%28mnHintSize%20%2B%20mnStackIdx%29%20%3E%202%2ANMAXHINTS%60%20but%20mnHintStack%20has%20only%20NMAXHINTS%20%28192%29%20slots%2C%20so%20the%20guard%20permits%20twice%20the%20actual%20capacity.%20A%20glyph%20charstring%20that%20issues%20repeated%20hstemhm/vstemhm%20operators%20accumulates%20mnHintSize%20past%20192%20and%20writes%20up%20to%20~192%20attacker-controlled%20doubles%20%28~1.5KB%29%20past%20the%20array.%20CffContext%20is%20a%20stack%20automatic%20in%20ConvertCFFfontToType1%28%29%2C%20so%20the%20overflow%20clobbers%20maCharWidth%2C%20mbDoSeac%2C%20the%20std%3A%3Avector%20maExtraGlyphIds%20%28whose%20corrupted%20internal%20pointers%20give%20a%20write/free%20primitive%29%2C%20and%20the%20calling%20stack%20frame.%20The%20path%20is%20reached%20during%20routine%20PDF%20export%20of%20any%20document%20embedding%20a%20CFF/OTF%20font%20%28pdfwriter_impl.cxx%20%E2%86%92%20PhysicalFontFace%3A%3ACreateFontSubset%20%E2%86%92%20ConvertCFFfontToType1%29%2C%20including%20headless%20%60soffice%20--convert-to%20pdf%60%20pipelines%2C%20and%20hb_subset%20preserves%20the%20hint%20operators.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22vcl/source/fontsubset/cff.cxx%3A867%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22LibreOffice/core%22%2C%22reproduction%22%3A%5B%221.%20Craft%20an%20OTF/CFF%20font%20with%20a%20glyph%20charstring%20containing%20repeated%20hstemhm/vstemhm%20operators%20accumulating%20%3E192%20%28up%20to%20384%29%20hint%20values%22%2C%222.%20Embed%20the%20font%20in%20a%20document%20%28ODT/DOCX/etc.%29%20and%20deliver%20it%20to%20the%20victim%20or%20upload%20to%20a%20headless%20conversion%20service%22%2C%223.%20Trigger%20PDF%20export%3B%20pdfwriter_impl.cxx%20calls%20PhysicalFontFace%3A%3ACreateFontSubset%20%E2%86%92%20ConvertCFFfontToType1%20on%20the%20embedded%20font%22%2C%224.%20convert2Type1Ops%20processes%20the%20glyph%2C%20addHints%28%29%20passes%20the%20faulty%202%2ANMAXHINTS%20guard%20and%20writes%20attacker%20doubles%20past%20mnHintStack%5B192%5D%22%2C%225.%20Overwritten%20std%3A%3Avector%3Csal_GlyphId%3E%20internal%20pointers%20are%20dereferenced%20on%20push_back/destruction%2C%20yielding%20a%20write/free%20primitive%20before%20any%20stack%20canary%20check%22%5D%2C%22technical_details%22%3A%22NMAXHINTS%20is%20defined%20as%202%2A96%20%3D%20192%20and%20mnHintStack%20is%20declared%20with%20NMAXHINTS%20elements%2C%20but%20the%20guard%20at%20line%20867%20checks%20against%202%2ANMAXHINTS%20%28384%29%20%E2%80%94%20the%20author%20double-counted%20the%20hint-pair%20factor%20already%20baked%20into%20the%20constant.%20Because%20mnHintSize%20persists%20across%20every%20hstem/vstem/hintmask%20operator%20within%20a%20glyph%2C%20five%20hstemhm%20ops%20with%2048%20operands%20each%20drive%20mnHintSize%20to%20240%2C%20under%20the%20erroneous%20384%20guard%20but%20past%20the%20192-slot%20array%2C%20and%20the%20loop%20%60mnHintStack%5BmnHintSize%2B%2B%5D%20%3D%20nHintOfs%60%20writes%20attacker-chosen%20ValType%20doubles%20off%20the%20end%20of%20the%20stack%20object.%22%2C%22title%22%3A%22CFF%20hint-stack%20bound%20compared%20against%20double%20the%20array%20size%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-RNHRV8B9",
  "bug_class": "Stack Buffer Overflow / Off-by-N",
  "created_at": "2026-04-16T01:54:45+00:00",
  "description": "In LibreOffice's CFF font subsetter (vcl/source/fontsubset/cff.cxx), addHints() guards the hint stack with `(mnHintSize + mnStackIdx) > 2*NMAXHINTS` but mnHintStack has only NMAXHINTS (192) slots, so the guard permits twice the actual capacity. A glyph charstring that issues repeated hstemhm/vstemhm operators accumulates mnHintSize past 192 and writes up to ~192 attacker-controlled doubles (~1.5KB) past the array. CffContext is a stack automatic in ConvertCFFfontToType1(), so the overflow clobbers maCharWidth, mbDoSeac, the std::vector maExtraGlyphIds (whose corrupted internal pointers give a write/free primitive), and the calling stack frame. The path is reached during routine PDF export of any document embedding a CFF/OTF font (pdfwriter_impl.cxx → PhysicalFontFace::CreateFontSubset → ConvertCFFfontToType1), including headless `soffice --convert-to pdf` pipelines, and hb_subset preserves the hint operators.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "vcl/source/fontsubset/cff.cxx:867",
  "project": "LibreOffice/core",
    "1. Craft an OTF/CFF font with a glyph charstring containing repeated hstemhm/vstemhm operators accumulating >192 (up to 384) hint values",
    "2. Embed the font in a document (ODT/DOCX/etc.) and deliver it to the victim or upload to a headless conversion service",
    "3. Trigger PDF export; pdfwriter_impl.cxx calls PhysicalFontFace::CreateFontSubset → ConvertCFFfontToType1 on the embedded font",
    "4. convert2Type1Ops processes the glyph, addHints() passes the faulty 2*NMAXHINTS guard and writes attacker doubles past mnHintStack[192]",
    "5. Overwritten std::vector<sal_GlyphId> internal pointers are dereferenced on push_back/destruction, yielding a write/free primitive before any stack canary check"
  "technical_details": "NMAXHINTS is defined as 2*96 = 192 and mnHintStack is declared with NMAXHINTS elements, but the guard at line 867 checks against 2*NMAXHINTS (384) — the author double-counted the hint-pair factor already baked into the constant. Because mnHintSize persists across every hstem/vstem/hintmask operator within a glyph, five hstemhm ops with 48 operands each drive mnHintSize to 240, under the erroneous 384 guard but past the 192-slot array, and the loop `mnHintStack[mnHintSize++] = nHintOfs` writes attacker-chosen ValType doubles off the end of the stack object.",
  "title": "CFF hint-stack bound compared against double the array size",
```
