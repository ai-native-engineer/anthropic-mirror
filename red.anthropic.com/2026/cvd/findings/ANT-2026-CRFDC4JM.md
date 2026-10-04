<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-CRFDC4JM -->

# ANT-2026-CRFDC4JM · libreoffice/core

## heap-buffer-overflow medium

[CVE-2026-63272](https://nvd.nist.gov/vuln/detail/CVE-2026-63272)

Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-CRFDC4JM: WMF Unicode-escape text DX-array heap overflow

In the WMF W\_META\_ESCAPE PRIVATE\_ESCAPE\_UNICODE path (wmfreader.cxx:1271-1311), nStringLen and nDXCount are read independently from the file with no check that nDXCount >= nStringLen. The KernArray (std::vector) is resized to nDXCount and passed to MtfTools::DrawText, which loops i=0..rText.getLength()-1 and does unchecked (\*pDXArry)[i] reads and writes. An attacker sets nStringLen large (e.g. 8000) and nDXCount=1, causing ~64 KB (up to ~256 KB) of doubles to be written past an 8-byte heap allocation. WMF is parsed whenever opened standalone or embedded in ODT/DOCX/RTF/PPTX, so a malicious document triggers heap corruption and likely RCE on open.

**Project:** libreoffice/core
**Location:** `emfio/source/reader/mtftools.cxx:1717`

Root cause is a missing invariant check: the reader never enforces nDXCount >= nStringLen (the writer side at wmfwr.cxx:516 shows the intended invariant). DrawText then uses unchecked std::vector::operator[] in a loop bounded by the string length rather than the array size, yielding both OOB read (mtftools.cxx:1715) and OOB write (mtftools.cxx:1720). \_GLIBCXX\_ASSERTIONS is off in default TDF builds, so operator[] performs no bounds check.

1. Craft a WMF with W\_META\_CREATEFONTINDIRECT for a ubiquitous font (e.g. Arial/Liberation Sans) followed by SELECTOBJECT to pass the IsFontAvailable gate.
2. Add a W\_META\_ESCAPE record carrying the LibreOffice PRIVATE\_ESCAPE\_UNICODE signature (magic 0x2c2a4f4f / 0x0a) and a correct CRC32 over the payload.
3. In the escape payload, set nStringLen large (e.g. 8000) with a matching string, and nDXCount=1 with a single DX entry.
4. Embed the WMF in an ODT/DOCX/RTF/PPTX (or deliver standalone) and send to the victim.
5. On open, DrawText loops over 8000 chars and writes ~7999 doubles past the 1-element KernArray heap allocation.

## Suggested Fix

Before per-character indexing, ensure the DX-advance array has at least rText.getLength() elements (reject the record or resize/pad the array) so pDXArry is never indexed beyond its size.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-CRFDC4JM.

---

**Reference:** ANT-2026-CRFDC4JM

Triage and disclosure were performed by Ada Logics.

```
diff --git a/emfio/source/reader/wmfreader.cxx b/emfio/source/reader/wmfreader.cxx
index a645411267b53..390f7271acf38 100644
--- a/emfio/source/reader/wmfreader.cxx
+++ b/emfio/source/reader/wmfreader.cxx
@@ -1349,7 +1349,7 @@ namespace emfio
                                                     GetFont().GetFamilyName()))
                                                 Point aPt;
-                                                sal_uInt32 nStringLen, nDXCount;
+                                                sal_uInt32 nStringLen(0), nDXCount(0);
                                                 KernArray aDXAry;
                                                 SvMemoryStream aMemoryStream(nEscLen);
                                                 aMemoryStream.WriteBytes(pData.get(), nEscLen);
@@ -1368,6 +1368,8 @@ namespace emfio
                                                     OUString aString = read_uInt16s_ToOUString(
                                                         aMemoryStream, nStringLen);
                                                     aMemoryStream.ReadUInt32(nDXCount);
+                                                    if (nDXCount < o3tl::make_unsigned(aString.getLength()))
+                                                        nDXCount = 0;
                                                     if ((static_cast<sal_uInt64>(nDXCount)
                                                         * sizeof(sal_Int32))
                                                         >= (nEscLen - aMemoryStream.Tell()))
@@ -1376,7 +1378,7 @@ namespace emfio
                                                         aDXAry.resize(nDXCount);
                                                     for (sal_uInt32 i = 0; i < nDXCount; i++)
-                                                        sal_Int32 val;
+                                                        sal_Int32 val(0);
                                                         aMemoryStream.ReadInt32(val);
                                                         aDXAry[i] = val;
```

<https://github.com/LibreOffice/core/commit/4406da79b0>

1. 2026-04-02
2. 2026-07-03
3. 2026-07-06
4. 2026-07-24
5. 2026-09-28

0cc2bd420b5659200db58805519d367e0f76e3baa0e39bdb85cfbe5ae2687a623a7c42edd42b0b875e954d9a14f8dd9a8fa8d63e23c38f0c84e44f843f7e823a

Committed 2026-07-22 07:32 UTC

Revealed 2026-09-28 21:05 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-CRFDC4JM%22%2C%22bug_class%22%3A%22Heap%20buffer%20overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T01%3A54%3A40%2B00%3A00%22%2C%22description%22%3A%22In%20the%20WMF%20W_META_ESCAPE%20PRIVATE_ESCAPE_UNICODE%20path%20%28wmfreader.cxx%3A1271-1311%29%2C%20nStringLen%20and%20nDXCount%20are%20read%20independently%20from%20the%20file%20with%20no%20check%20that%20nDXCount%20%3E%3D%20nStringLen.%20The%20KernArray%20%28std%3A%3Avector%3Cdouble%3E%29%20is%20resized%20to%20nDXCount%20and%20passed%20to%20MtfTools%3A%3ADrawText%2C%20which%20loops%20i%3D0..rText.getLength%28%29-1%20and%20does%20unchecked%20%28%2ApDXArry%29%5Bi%5D%20reads%20and%20writes.%20An%20attacker%20sets%20nStringLen%20large%20%28e.g.%208000%29%20and%20nDXCount%3D1%2C%20causing%20~64%20KB%20%28up%20to%20~256%20KB%29%20of%20doubles%20to%20be%20written%20past%20an%208-byte%20heap%20allocation.%20WMF%20is%20parsed%20whenever%20opened%20standalone%20or%20embedded%20in%20ODT/DOCX/RTF/PPTX%2C%20so%20a%20malicious%20document%20triggers%20heap%20corruption%20and%20likely%20RCE%20on%20open.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22emfio/source/reader/mtftools.cxx%3A1717%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22LibreOffice/core%22%2C%22reproduction%22%3A%5B%221.%20Craft%20a%20WMF%20with%20W_META_CREATEFONTINDIRECT%20for%20a%20ubiquitous%20font%20%28e.g.%20Arial/Liberation%20Sans%29%20followed%20by%20SELECTOBJECT%20to%20pass%20the%20IsFontAvailable%20gate.%22%2C%222.%20Add%20a%20W_META_ESCAPE%20record%20carrying%20the%20LibreOffice%20PRIVATE_ESCAPE_UNICODE%20signature%20%28magic%200x2c2a4f4f%20/%200x0a%29%20and%20a%20correct%20CRC32%20over%20the%20payload.%22%2C%223.%20In%20the%20escape%20payload%2C%20set%20nStringLen%20large%20%28e.g.%208000%29%20with%20a%20matching%20string%2C%20and%20nDXCount%3D1%20with%20a%20single%20DX%20entry.%22%2C%224.%20Embed%20the%20WMF%20in%20an%20ODT/DOCX/RTF/PPTX%20%28or%20deliver%20standalone%29%20and%20send%20to%20the%20victim.%22%2C%225.%20On%20open%2C%20DrawText%20loops%20over%208000%20chars%20and%20writes%20~7999%20doubles%20past%20the%201-element%20KernArray%20heap%20allocation.%22%5D%2C%22technical_details%22%3A%22Root%20cause%20is%20a%20missing%20invariant%20check%3A%20the%20reader%20never%20enforces%20nDXCount%20%3E%3D%20nStringLen%20%28the%20writer%20side%20at%20wmfwr.cxx%3A516%20shows%20the%20intended%20invariant%29.%20DrawText%20then%20uses%20unchecked%20std%3A%3Avector%3Cdouble%3E%3A%3Aoperator%5B%5D%20in%20a%20loop%20bounded%20by%20the%20string%20length%20rather%20than%20the%20array%20size%2C%20yielding%20both%20OOB%20read%20%28mtftools.cxx%3A1715%29%20and%20OOB%20write%20%28mtftools.cxx%3A1720%29.%20_GLIBCXX_ASSERTIONS%20is%20off%20in%20default%20TDF%20builds%2C%20so%20operator%5B%5D%20performs%20no%20bounds%20check.%22%2C%22title%22%3A%22WMF%20Unicode-escape%20text%20DX-array%20heap%20overflow%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-CRFDC4JM",
  "bug_class": "Heap buffer overflow",
  "created_at": "2026-04-16T01:54:40+00:00",
  "description": "In the WMF W_META_ESCAPE PRIVATE_ESCAPE_UNICODE path (wmfreader.cxx:1271-1311), nStringLen and nDXCount are read independently from the file with no check that nDXCount >= nStringLen. The KernArray (std::vector<double>) is resized to nDXCount and passed to MtfTools::DrawText, which loops i=0..rText.getLength()-1 and does unchecked (*pDXArry)[i] reads and writes. An attacker sets nStringLen large (e.g. 8000) and nDXCount=1, causing ~64 KB (up to ~256 KB) of doubles to be written past an 8-byte heap allocation. WMF is parsed whenever opened standalone or embedded in ODT/DOCX/RTF/PPTX, so a malicious document triggers heap corruption and likely RCE on open.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "emfio/source/reader/mtftools.cxx:1717",
  "project": "LibreOffice/core",
    "1. Craft a WMF with W_META_CREATEFONTINDIRECT for a ubiquitous font (e.g. Arial/Liberation Sans) followed by SELECTOBJECT to pass the IsFontAvailable gate.",
    "2. Add a W_META_ESCAPE record carrying the LibreOffice PRIVATE_ESCAPE_UNICODE signature (magic 0x2c2a4f4f / 0x0a) and a correct CRC32 over the payload.",
    "3. In the escape payload, set nStringLen large (e.g. 8000) with a matching string, and nDXCount=1 with a single DX entry.",
    "4. Embed the WMF in an ODT/DOCX/RTF/PPTX (or deliver standalone) and send to the victim.",
    "5. On open, DrawText loops over 8000 chars and writes ~7999 doubles past the 1-element KernArray heap allocation."
  "technical_details": "Root cause is a missing invariant check: the reader never enforces nDXCount >= nStringLen (the writer side at wmfwr.cxx:516 shows the intended invariant). DrawText then uses unchecked std::vector<double>::operator[] in a loop bounded by the string length rather than the array size, yielding both OOB read (mtftools.cxx:1715) and OOB write (mtftools.cxx:1720). _GLIBCXX_ASSERTIONS is off in default TDF builds, so operator[] performs no bounds check.",
  "title": "WMF Unicode-escape text DX-array heap overflow",
```
