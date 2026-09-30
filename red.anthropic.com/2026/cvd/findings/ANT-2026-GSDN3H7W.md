<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-GSDN3H7W -->

# ANT-2026-GSDN3H7W · opensc

## stack-buffer-overflow low

[CVE-2026-40528](https://nvd.nist.gov/vuln/detail/CVE-2026-40528)

Claude low
Security research firm low
Maintainer low

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-GSDN3H7W: Stack buffer overflow in do\_key\_value profile parsing via unbounded memcpy into 32-byte buffer

An unbounded memcpy in do\_key\_value copies profile data into a fixed 32-byte stack buffer, overflowing it.

**Project:** opensc
**Location:** `do_key_value()`

This finding was identified by static analysis and has not yet been dynamically reproduced. A trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-GSDN3H7W.

---

**Reference:** ANT-2026-GSDN3H7W

Triage and disclosure were performed by Trail of Bits.

:   low

1. 2026-03-03
2. 2026-03-29
3. 2026-03-29
4. 2026-05-09

ce928e32f2d40c5afc3911f86cbf75774a72defba7331a4233ba68f846447e71482974fd708e1b7137ccf7edcae245f89826cfeb3b038c4fa962703b3640efdb

Committed 2026-04-09 11:50 PT

Revealed 2026-08-17 10:47 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-GSDN3H7W%22%2C%22bug_class%22%3A%22Stack%20Buffer%20Overflow%22%2C%22claude_severity%22%3A%22low%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A43%3A23%2B00%3A00%22%2C%22description%22%3A%22An%20unbounded%20memcpy%20in%20do_key_value%20copies%20profile%20data%20into%20a%20fixed%2032-byte%20stack%20buffer%2C%20overflowing%20it.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22do_key_value%28%29%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22OpenSC%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22Stack%20buffer%20overflow%20in%20do_key_value%20profile%20parsing%20via%20unbounded%20memcpy%20into%2032-byte%20buffer%22%2C%22vendor_severity%22%3A%22low%22%7D)

```
  "ant_id": "ANT-2026-GSDN3H7W",
  "bug_class": "Stack Buffer Overflow",
  "claude_severity": "low",
  "created_at": "2026-03-29T20:43:23+00:00",
  "description": "An unbounded memcpy in do_key_value copies profile data into a fixed 32-byte stack buffer, overflowing it.",
  "location": "do_key_value()",
  "project": "OpenSC",
  "technical_details": null,
  "title": "Stack buffer overflow in do_key_value profile parsing via unbounded memcpy into 32-byte buffer",
  "vendor_severity": "low"
```
