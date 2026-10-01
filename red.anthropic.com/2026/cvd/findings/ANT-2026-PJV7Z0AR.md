<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-PJV7Z0AR -->

# ANT-2026-PJV7Z0AR · open62541

## integer-overflow high

[CVE-2026-63559](https://nvd.nist.gov/vuln/detail/CVE-2026-63559)
[CVE-2026-65423](https://nvd.nist.gov/vuln/detail/CVE-2026-65423)

Maintainer high

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-PJV7Z0AR: Integer overflow in variant dimension validation allowing wild-address write via arrayDimensions product overflow

The product of arrayDimensions overflows during variant dimension validation, leading to a wild-address write.

**Project:** open62541

This finding was identified by static analysis and has not yet been dynamically reproduced. A trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-PJV7Z0AR.

---

**Reference:** ANT-2026-PJV7Z0AR

Triage and disclosure were performed by Trail of Bits.

1. 2026-03-29
2. 2026-04-09
3. 2026-05-09
4. 2026-07-22

03bf968a7d024ab0ac6f945f14f827bdfa8fba50c910ca06cf6b2af74116597317a198657ed216efa65014c755f20e9ed5a8e2c162b139e74b5c054f55f3e198

Committed 2026-04-09 11:50 PT

Revealed 2026-08-17 10:47 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-PJV7Z0AR%22%2C%22bug_class%22%3A%22Integer%20Overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A43%3A19%2B00%3A00%22%2C%22description%22%3A%22The%20product%20of%20arrayDimensions%20overflows%20during%20variant%20dimension%20validation%2C%20leading%20to%20a%20wild-address%20write.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22open62541%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22Integer%20overflow%20in%20variant%20dimension%20validation%20allowing%20wild-address%20write%20via%20arrayDimensions%20product%20overflow%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-PJV7Z0AR",
  "bug_class": "Integer Overflow",
  "created_at": "2026-03-29T20:43:19+00:00",
  "description": "The product of arrayDimensions overflows during variant dimension validation, leading to a wild-address write.",
  "project": "open62541",
  "technical_details": null,
  "title": "Integer overflow in variant dimension validation allowing wild-address write via arrayDimensions product overflow",
```
