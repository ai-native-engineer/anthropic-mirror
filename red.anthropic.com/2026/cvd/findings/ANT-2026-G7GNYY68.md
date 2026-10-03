<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-G7GNYY68 -->

# ANT-2026-G7GNYY68 · libreoffice/core

## heap-buffer-overflow medium

[CVE-2026-6045](https://nvd.nist.gov/vuln/detail/CVE-2026-6045)

Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-G7GNYY68: Heap Buffer Overflow via Integer Overflow in EMF+ Brush Blend Point Parsing

An integer overflow during parsing of EMF+ brush blend points leads to a heap buffer overflow.

**Project:** libreoffice/core
**Location:** `drawinglayer/source/tools/emfpbrush.cxx:EMFPBrush::Read`

This finding was identified by static analysis and has not yet been dynamically reproduced. A trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-G7GNYY68.

---

**Reference:** ANT-2026-G7GNYY68

Triage and disclosure were performed by Ada Logics.

1. 2026-03-29
2. 2026-04-09
3. 2026-04-30
4. 2026-05-09
5. 2026-08-17

d3fd15b9dba2859842eca0b54091853a125bd20ca023ce3b82e5a4d1cccd8c92384c803858f19b22b61c66823161cb21ee42fe234e93b24e86b1efb9faab8469

Committed 2026-04-09 18:50 UTC

Revealed 2026-08-17 21:12 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-G7GNYY68%22%2C%22bug_class%22%3A%22Heap%20Buffer%20Overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A43%3A12%2B00%3A00%22%2C%22description%22%3A%22An%20integer%20overflow%20during%20parsing%20of%20EMF%2B%20brush%20blend%20points%20leads%20to%20a%20heap%20buffer%20overflow.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22LibreOffice%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22Heap%20Buffer%20Overflow%20via%20Integer%20Overflow%20in%20EMF%2B%20Brush%20Blend%20Point%20Parsing%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-G7GNYY68",
  "bug_class": "Heap Buffer Overflow",
  "created_at": "2026-03-29T20:43:12+00:00",
  "description": "An integer overflow during parsing of EMF+ brush blend points leads to a heap buffer overflow.",
  "project": "LibreOffice",
  "technical_details": null,
  "title": "Heap Buffer Overflow via Integer Overflow in EMF+ Brush Blend Point Parsing",
```
