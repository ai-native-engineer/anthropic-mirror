<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-EBDTPNVH -->

# ANT-2026-EBDTPNVH · jqlang/jq

## heap-buffer-overflow medium

[CVE-2026-32316](https://nvd.nist.gov/vuln/detail/CVE-2026-32316)
[GHSA-q3h9-m34w-h76f](https://github.com/jqlang/jq/security/advisories/GHSA-q3h9-m34w-h76f)

Claude medium
Security research firm medium
Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-EBDTPNVH: Integer overflow in string concatenation leading to 1 GB memcpy heap buffer overflow

An integer overflow during string concatenation leads to a 1 GB memcpy heap buffer overflow.

**Project:** jqlang/jq

The root cause is an integer overflow in the string-concatenation size calculation; the resulting undersized buffer is then overflowed by a ~1 GB memcpy.

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-EBDTPNVH.

---

**Reference:** ANT-2026-EBDTPNVH

Triage and disclosure were performed by Trail of Bits.

:   medium

1. 2026-03-29
2. 2026-05-07
3. 2026-05-07
4. 2026-05-07
5. 2026-05-20

e58a8b9eeba1e34b6155b568522e0ed14fbaab99b1699e170f1bb129f78dd3b8ad1baf7997acbfbd05c8a10c16ffad6f5cda3bd7b6798efd06569cd55df3c1a9

Committed 2026-05-07 07:00 UTC

Revealed 2026-05-20 07:40 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-EBDTPNVH%22%2C%22bug_class%22%3A%22Heap%20Buffer%20Overflow%22%2C%22claude_severity%22%3A%22medium%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A43%3A01%2B00%3A00%22%2C%22description%22%3A%22An%20integer%20overflow%20during%20string%20concatenation%20leads%20to%20a%201%20GB%20memcpy%20heap%20buffer%20overflow.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22jq%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3A%22The%20root%20cause%20is%20an%20integer%20overflow%20in%20the%20string-concatenation%20size%20calculation%3B%20the%20resulting%20undersized%20buffer%20is%20then%20overflowed%20by%20a%20~1%20GB%20memcpy.%22%2C%22title%22%3A%22Integer%20overflow%20in%20string%20concatenation%20leading%20to%201%20GB%20memcpy%20heap%20buffer%20overflow%22%2C%22vendor_severity%22%3A%22medium%22%7D)

```
  "ant_id": "ANT-2026-EBDTPNVH",
  "bug_class": "Heap Buffer Overflow",
  "claude_severity": "medium",
  "created_at": "2026-03-29T20:43:01+00:00",
  "description": "An integer overflow during string concatenation leads to a 1 GB memcpy heap buffer overflow.",
  "project": "jq",
  "technical_details": "The root cause is an integer overflow in the string-concatenation size calculation; the resulting undersized buffer is then overflowed by a ~1 GB memcpy.",
  "title": "Integer overflow in string concatenation leading to 1 GB memcpy heap buffer overflow",
  "vendor_severity": "medium"
```
