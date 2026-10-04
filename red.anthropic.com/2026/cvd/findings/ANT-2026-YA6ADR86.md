<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-YA6ADR86 -->

# ANT-2026-YA6ADR86 · libreoffice/core

## stack-buffer-overflow medium

[CVE-2026-63276](https://nvd.nist.gov/vuln/detail/CVE-2026-63276)

Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-YA6ADR86: CFF charstring to Type1 conversion stack buffer overflow

convert2Type1Ops() in vcl/source/fontsubset/cff.cxx writes converted Type1 charstring bytes through mpWritePtr into a fixed 81920-byte on-stack buffer (aCharString / aOps[MAX\_T1OPS\_SIZE]) with no end-pointer or bounds check in writeType1Val/writeTypeOp/writeCurveTo. Because mnHintSize accumulates and each HSTEM/VSTEM/HINTMASK re-emits the full hint list, and because subroutine recursion is unlimited, a single attacker-crafted glyph can inflate output well past 80KB (~1000:1 amplification). The converter is reached from document-embedded CFF/OTF fonts on File → Export As PDF, and the HarfBuzz subset pass preserves the attacker's charstrings. The result is an attacker-controlled unbounded stack write in the soffice process, yielding at minimum DoS/abort and potentially RCE.

**Project:** libreoffice/core
**Location:** `vcl/source/fontsubset/cff.cxx:2295`

writeType1Val/writeTypeOp/writeTypeEsc (cff.cxx:1041-1105) perform raw \*(mpWritePtr++) writes into the 81920-byte stack array declared at cff.cxx:714/2295, and there is no mpWriteEnd or length check anywhere in the write path. The HSTEM re-emit-all-hints loop (cff.cxx:1170-1174) combined with unlimited callType2Subr recursion (cff.cxx:1600-1624) lets a crafted Type2 charstring produce output far exceeding the buffer, overwriting adjacent stack frame data.

1. Craft an OTF with a CFF glyph whose Type2 charstring packs repeated hstem/vstem/hintmask groups and long rrcurveto/rlineto runs (and/or nested subroutine calls) to achieve >80KB converted output
2. Set the font's fsType flag so the embedded-font restriction gate (embeddedfontsmanager.cxx:393) passes and the font auto-activates
3. Embed the font in an ODT/ODP/DOCX and deliver it to the victim
4. Victim opens the document and selects File → Export As PDF
5. pdfwriter\_impl.cxx:2096 → PhysicalFontFace::CreateFontSubset → ConvertCFFfontToType1 invokes convert2Type1Ops(), which writes past the 80KB stack buffer

## Suggested Fix

Bound every write through mpWritePtr against the allocated output buffer size (track an end pointer) and abort the conversion with an error if the charstring output would exceed it.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-YA6ADR86.

---

**Reference:** ANT-2026-YA6ADR86

Triage and disclosure were performed by Ada Logics.

```
diff --git a/vcl/source/fontsubset/cff.cxx b/vcl/source/fontsubset/cff.cxx
index bbcb5176dbf8d..d1c332634b5fd 100644
--- a/vcl/source/fontsubset/cff.cxx
+++ b/vcl/source/fontsubset/cff.cxx
@@ -1337,7 +1337,8 @@ class CffContext : private CffGlobal
 private:
     bool convertCharStrings(std::vector<CharString>& rCharStrings, int nGlyphCount,
                             const sal_GlyphId* pGlyphIds = nullptr);
-    int convert2Type1Ops(CffLocal*, const U8* pType2Ops, int nType2Len, U8* pType1Ops);
+    int convert2Type1Ops(CffLocal*, const U8* pType2Ops, int nType2Len, U8* pType1Ops,
+                         size_t nType1Cap);
     bool convertOneTypeOp();
     bool convertOneTypeEsc();
     bool callType2Subr(bool bGlobal, int nSubrNumber);
@@ -1348,6 +1349,11 @@ class CffContext : private CffGlobal
     // != mpReadEnd post-check so flags as a parse failure.
     void abandonDictParse() { mpReadPtr = mpReadEnd + 1; }

+    // Abandon the charstring conversion when the output buffer is full.
+    // callType2Subr does not restore mpWritePtr, so this stays in effect when
+    // the buffer fills inside a subroutine.
+    void abandonConversion() { mpWritePtr = mpWriteEnd + 1; }
+
     const U8* mpBasePtr;
     const U8* mpBaseEnd;

@@ -1355,6 +1361,8 @@ class CffContext : private CffGlobal
     const U8* mpReadEnd;

     U8* mpWritePtr;
+    U8* mpWriteEnd;
+    int mnSubrDepth;
     bool mbNeedClose;
     bool mbIgnoreHints;
     sal_Int32 mnCntrMask;
@@ -1374,6 +1382,9 @@ class CffContext : private CffGlobal
     bool getBaseAccent(ValType aBase, ValType aAccent, int* nBase, int* nAccent);

     void read2push();
+    // True if nBytes more fit in the output buffer; otherwise abandon the
+    // conversion and return false so the caller skips the write.
+    bool hasWriteRoom(int nBytes);
     void writeType1Val(ValType);
     void writeTypeOp(int nTypeOp);
     void writeTypeEsc(int nTypeOp);
@@ -1420,6 +1431,8 @@ CffContext::CffContext(const U8* pBasePtr, int nBaseLen)
     , mpReadPtr(nullptr)
     , mpReadEnd(nullptr)
     , mpWritePtr(nullptr)
+    , mpWriteEnd(nullptr)
+    , mnSubrDepth(0)
     , mbNeedClose(false)
     , mbIgnoreHints(false)
     , mnCntrMask(0)
@@ -1755,8 +1768,21 @@ void CffContext::read2push()
     push(aVal);

+bool CffContext::hasWriteRoom(int nBytes)
+{
+    if (mpWritePtr + nBytes <= mpWriteEnd)
+        return true;
+    abandonConversion();
+    return false;
+}
+
 void CffContext::writeType1Val(ValType aVal)
+    // Five bytes for the number, plus five more and a two byte "div" escape
+    // when a fractional value is split.
+    if (!hasWriteRoom(12))
+        return;
+
     U8* pOut = mpWritePtr;

     // tdf#126242
@@ -1815,10 +1841,17 @@ void CffContext::writeType1Val(ValType aVal)

-inline void CffContext::writeTypeOp(int nTypeOp) { *(mpWritePtr++) = static_cast<U8>(nTypeOp); }
+inline void CffContext::writeTypeOp(int nTypeOp)
+{
+    if (!hasWriteRoom(1))
+        return;
+    *(mpWritePtr++) = static_cast<U8>(nTypeOp);
+}

 inline void CffContext::writeTypeEsc(int nTypeEsc)
+    if (!hasWriteRoom(2))
+        return;
     *(mpWritePtr++) = TYPE1OP::T1ESC;
     *(mpWritePtr++) = static_cast<U8>(nTypeEsc);
@@ -2370,28 +2403,40 @@ bool CffContext::callType2Subr(bool bGlobal, int nSubrNumber)
             return false;

-    while (mpReadPtr < mpReadEnd)
+    // The CFF specification limits subroutine call nesting to 10 levels;
+    // deeper nesting would let cyclic subroutines recurse without bound.
+    if (mnSubrDepth >= 10)
+        return false;
+    ++mnSubrDepth;
+
+    bool bRet = true;
+    while (mpReadPtr < mpReadEnd && mpWritePtr <= mpWriteEnd)
         if (!convertOneTypeOp())
-            return false;
+        {
+            bRet = false;
+            break;
+        }
+    --mnSubrDepth;

     mpReadPtr = pOldReadPtr;
     mpReadEnd = pOldReadEnd;
-    return true;
+    return bRet;

 int CffContext::convert2Type1Ops(CffLocal* pCffLocal, const U8* const pT2Ops, int nT2Len,
-                                 U8* const pT1Ops)
+                                 U8* const pT1Ops, size_t nT1Cap)
     mpCffLocal = pCffLocal;

     // prepare the charstring conversion
     mpWritePtr = pT1Ops;
-    U8 aType1Ops[MAX_T1OPS_SIZE];
-    if (!pT1Ops)
-        mpWritePtr = aType1Ops;
-    *const_cast<U8**>(&pT1Ops) = mpWritePtr;
+
+    // Remember where the output buffer ends so the write primitives can tell
+    // how much space is left. Start with no subroutine nesting.
+    mpWriteEnd = mpWritePtr + nT1Cap;
+    mnSubrDepth = 0;

     // prepend random seed for T1crypt
     *(mpWritePtr++) = 0x48;
@@ -2419,11 +2464,13 @@ int CffContext::convert2Type1Ops(CffLocal* pCffLocal, const U8* const pT2Ops, in
     mnHintSize = mnHorzHintSize = mnStackIdx = 0;
     maCharWidth = -1; //#######
     mnCntrMask = 0;
-    while (mpReadPtr < mpReadEnd)
+    while (mpReadPtr < mpReadEnd && mpWritePtr <= mpWriteEnd)
         if (!convertOneTypeOp())
             return -1;
+    if (mpWritePtr > mpWriteEnd)
+        return -1;
     if (maCharWidth != -1)
         // overwrite earlier charWidth value, which we only now have
@@ -3168,7 +3215,8 @@ bool CffContext::convertCharStrings(std::vector<CharString>& rCharStrings, int n
             return false;

         CharString aCharString;
-        const int nT1Len = convert2Type1Ops(mpCffLocal, mpReadPtr, nT2Len, aCharString.aOps);
+        const int nT1Len = convert2Type1Ops(mpCffLocal, mpReadPtr, nT2Len, aCharString.aOps,
+                                            std::size(aCharString.aOps));
         if (nT1Len < 0)
             return false;
         aCharString.nLen = nT1Len;
```

<https://github.com/LibreOffice/core/commit/49360f34f5caff4eee29489e339def8cf13053cc>

1. 2026-04-02
2. 2026-07-04
3. 2026-07-24
4. 2026-08-12
5. 2026-09-28

494557fa46d72a221c333ba25008c45576babe947f8e78b9bd4f593dea3fbeebc3c5c47719a2187f04b6674a97532dc748674543329568dd6af93b2827800c8e

Committed 2026-07-22 07:32 UTC

Revealed 2026-09-28 20:47 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-YA6ADR86%22%2C%22bug_class%22%3A%22Memory%20Safety%20/%20Stack%20Buffer%20Overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T01%3A54%3A46%2B00%3A00%22%2C%22description%22%3A%22convert2Type1Ops%28%29%20in%20vcl/source/fontsubset/cff.cxx%20writes%20converted%20Type1%20charstring%20bytes%20through%20mpWritePtr%20into%20a%20fixed%2081920-byte%20on-stack%20buffer%20%28aCharString%20/%20aOps%5BMAX_T1OPS_SIZE%5D%29%20with%20no%20end-pointer%20or%20bounds%20check%20in%20writeType1Val/writeTypeOp/writeCurveTo.%20Because%20mnHintSize%20accumulates%20and%20each%20HSTEM/VSTEM/HINTMASK%20re-emits%20the%20full%20hint%20list%2C%20and%20because%20subroutine%20recursion%20is%20unlimited%2C%20a%20single%20attacker-crafted%20glyph%20can%20inflate%20output%20well%20past%2080KB%20%28~1000%3A1%20amplification%29.%20The%20converter%20is%20reached%20from%20document-embedded%20CFF/OTF%20fonts%20on%20File%20%E2%86%92%20Export%20As%20PDF%2C%20and%20the%20HarfBuzz%20subset%20pass%20preserves%20the%20attacker%27s%20charstrings.%20The%20result%20is%20an%20attacker-controlled%20unbounded%20stack%20write%20in%20the%20soffice%20process%2C%20yielding%20at%20minimum%20DoS/abort%20and%20potentially%20RCE.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22vcl/source/fontsubset/cff.cxx%3A2295%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22LibreOffice/core%22%2C%22reproduction%22%3A%5B%221.%20Craft%20an%20OTF%20with%20a%20CFF%20glyph%20whose%20Type2%20charstring%20packs%20repeated%20hstem/vstem/hintmask%20groups%20and%20long%20rrcurveto/rlineto%20runs%20%28and/or%20nested%20subroutine%20calls%29%20to%20achieve%20%3E80KB%20converted%20output%22%2C%222.%20Set%20the%20font%27s%20fsType%20flag%20so%20the%20embedded-font%20restriction%20gate%20%28embeddedfontsmanager.cxx%3A393%29%20passes%20and%20the%20font%20auto-activates%22%2C%223.%20Embed%20the%20font%20in%20an%20ODT/ODP/DOCX%20and%20deliver%20it%20to%20the%20victim%22%2C%224.%20Victim%20opens%20the%20document%20and%20selects%20File%20%E2%86%92%20Export%20As%20PDF%22%2C%225.%20pdfwriter_impl.cxx%3A2096%20%E2%86%92%20PhysicalFontFace%3A%3ACreateFontSubset%20%E2%86%92%20ConvertCFFfontToType1%20invokes%20convert2Type1Ops%28%29%2C%20which%20writes%20past%20the%2080KB%20stack%20buffer%22%5D%2C%22technical_details%22%3A%22writeType1Val/writeTypeOp/writeTypeEsc%20%28cff.cxx%3A1041-1105%29%20perform%20raw%20%2A%28mpWritePtr%2B%2B%29%20writes%20into%20the%2081920-byte%20stack%20array%20declared%20at%20cff.cxx%3A714/2295%2C%20and%20there%20is%20no%20mpWriteEnd%20or%20length%20check%20anywhere%20in%20the%20write%20path.%20The%20HSTEM%20re-emit-all-hints%20loop%20%28cff.cxx%3A1170-1174%29%20combined%20with%20unlimited%20callType2Subr%20recursion%20%28cff.cxx%3A1600-1624%29%20lets%20a%20crafted%20Type2%20charstring%20produce%20output%20far%20exceeding%20the%20buffer%2C%20overwriting%20adjacent%20stack%20frame%20data.%22%2C%22title%22%3A%22CFF%20charstring%20to%20Type1%20conversion%20stack%20buffer%20overflow%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-YA6ADR86",
  "bug_class": "Memory Safety / Stack Buffer Overflow",
  "created_at": "2026-04-16T01:54:46+00:00",
  "description": "convert2Type1Ops() in vcl/source/fontsubset/cff.cxx writes converted Type1 charstring bytes through mpWritePtr into a fixed 81920-byte on-stack buffer (aCharString / aOps[MAX_T1OPS_SIZE]) with no end-pointer or bounds check in writeType1Val/writeTypeOp/writeCurveTo. Because mnHintSize accumulates and each HSTEM/VSTEM/HINTMASK re-emits the full hint list, and because subroutine recursion is unlimited, a single attacker-crafted glyph can inflate output well past 80KB (~1000:1 amplification). The converter is reached from document-embedded CFF/OTF fonts on File → Export As PDF, and the HarfBuzz subset pass preserves the attacker's charstrings. The result is an attacker-controlled unbounded stack write in the soffice process, yielding at minimum DoS/abort and potentially RCE.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "vcl/source/fontsubset/cff.cxx:2295",
  "project": "LibreOffice/core",
    "1. Craft an OTF with a CFF glyph whose Type2 charstring packs repeated hstem/vstem/hintmask groups and long rrcurveto/rlineto runs (and/or nested subroutine calls) to achieve >80KB converted output",
    "2. Set the font's fsType flag so the embedded-font restriction gate (embeddedfontsmanager.cxx:393) passes and the font auto-activates",
    "3. Embed the font in an ODT/ODP/DOCX and deliver it to the victim",
    "4. Victim opens the document and selects File → Export As PDF",
    "5. pdfwriter_impl.cxx:2096 → PhysicalFontFace::CreateFontSubset → ConvertCFFfontToType1 invokes convert2Type1Ops(), which writes past the 80KB stack buffer"
  "technical_details": "writeType1Val/writeTypeOp/writeTypeEsc (cff.cxx:1041-1105) perform raw *(mpWritePtr++) writes into the 81920-byte stack array declared at cff.cxx:714/2295, and there is no mpWriteEnd or length check anywhere in the write path. The HSTEM re-emit-all-hints loop (cff.cxx:1170-1174) combined with unlimited callType2Subr recursion (cff.cxx:1600-1624) lets a crafted Type2 charstring produce output far exceeding the buffer, overwriting adjacent stack frame data.",
  "title": "CFF charstring to Type1 conversion stack buffer overflow",
```
