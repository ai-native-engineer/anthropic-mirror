<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-8FZYKRTH -->

# ANT-2026-8FZYKRTH · libreoffice/core

## heap-buffer-overflow medium

[CVE-2026-6039](https://nvd.nist.gov/vuln/detail/CVE-2026-6039)

Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-8FZYKRTH: Heap buffer overflow in DXF LWPOLYLINE import via integer truncation from sal\_Int32 to sal\_uInt16

Integer truncation from sal\_Int32 to sal\_uInt16 during DXF LWPOLYLINE import causes a heap buffer overflow.

**Project:** libreoffice/core
**Location:** `vcl/source/filter/idxf/dxf2mtf.cxx:DXF2GDIMetaFile::DrawLWPolyLineEntity`

A 32-bit value (sal\_Int32) is truncated to 16 bits (sal\_uInt16) when handling an LWPOLYLINE entity in the DXF importer; the truncated value leads to an undersized buffer and a subsequent out-of-bounds heap write.

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-8FZYKRTH.

---

**Reference:** ANT-2026-8FZYKRTH

Triage and disclosure were performed by Ada Logics.

1. 2026-03-29
2. 2026-04-09
3. 2026-04-30
4. 2026-05-09
5. 2026-08-17

a287adfa390e0cfcb2b267c2e1ff26b4a8e73b07532dafeed696cb0231a0d164d594559df99d67b8a195d5cd0549220922038fc2f119d3c5596945ae93fa5b44

Committed 2026-04-09 18:50 UTC

Revealed 2026-08-17 21:12 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-8FZYKRTH%22%2C%22bug_class%22%3A%22Heap%20Buffer%20Overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A43%3A11%2B00%3A00%22%2C%22description%22%3A%22Integer%20truncation%20from%20sal_Int32%20to%20sal_uInt16%20during%20DXF%20LWPOLYLINE%20import%20causes%20a%20heap%20buffer%20overflow.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22LibreOffice%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3A%22A%2032-bit%20value%20%28sal_Int32%29%20is%20truncated%20to%2016%20bits%20%28sal_uInt16%29%20when%20handling%20an%20LWPOLYLINE%20entity%20in%20the%20DXF%20importer%3B%20the%20truncated%20value%20leads%20to%20an%20undersized%20buffer%20and%20a%20subsequent%20out-of-bounds%20heap%20write.%22%2C%22title%22%3A%22Heap%20buffer%20overflow%20in%20DXF%20LWPOLYLINE%20import%20via%20integer%20truncation%20from%20sal_Int32%20to%20sal_uInt16%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-8FZYKRTH",
  "bug_class": "Heap Buffer Overflow",
  "created_at": "2026-03-29T20:43:11+00:00",
  "description": "Integer truncation from sal_Int32 to sal_uInt16 during DXF LWPOLYLINE import causes a heap buffer overflow.",
  "project": "LibreOffice",
  "technical_details": "A 32-bit value (sal_Int32) is truncated to 16 bits (sal_uInt16) when handling an LWPOLYLINE entity in the DXF importer; the truncated value leads to an undersized buffer and a subsequent out-of-bounds heap write.",
  "title": "Heap buffer overflow in DXF LWPOLYLINE import via integer truncation from sal_Int32 to sal_uInt16",
```
