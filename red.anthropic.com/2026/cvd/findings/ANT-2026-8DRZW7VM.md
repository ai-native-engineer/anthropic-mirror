<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-8DRZW7VM -->

# ANT-2026-8DRZW7VM · cisco-talos/clamav

## integer-overflow high

[CVE-2026-20215](https://nvd.nist.gov/vuln/detail/CVE-2026-20215)
[GHSA-6gff-7f37-2v35](https://github.com/advisories/GHSA-6gff-7f37-2v35)

Maintainer high

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-8DRZW7VM: Integer overflow in 7z SubStreams count leading to heap buffer overflow

An integer overflow when computing the SubStreams count in the 7z archive parser results in an undersized allocation and subsequent heap buffer overflow.

**Project:** cisco-talos/clamav
**Location:** `libclamav/7z/7zIn.c:SzReadSubStreamsInfo (7zIn.c:771)`

This finding was identified by static analysis and has not yet been dynamically reproduced. A trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-8DRZW7VM.

---

**Reference:** ANT-2026-8DRZW7VM

Triage and disclosure were performed by Trail of Bits.

ADVISORY

<https://github.com/Cisco-Talos/clamav/commit/a0b1531c6368347a79c15fb69d508171c55cc8cf>

1. 2026-03-29
2. 2026-04-09
3. 2026-05-07
4. 2026-05-07
5. 2026-07-21

67ced60afd5a1e4a42149c7ab50f3c46bf4db111cb82f29c246c6a1e74f7644512439a18d8fa6b6a3bd1d3f13b5f4282d8195e21a3a4a5b4e57029947237f85f

Committed 2026-04-09 18:49 UTC

Revealed 2026-07-21 05:20 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-8DRZW7VM%22%2C%22bug_class%22%3A%22Integer%20Overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A42%3A42%2B00%3A00%22%2C%22description%22%3A%22An%20integer%20overflow%20when%20computing%20the%20SubStreams%20count%20in%20the%207z%20archive%20parser%20results%20in%20an%20undersized%20allocation%20and%20subsequent%20heap%20buffer%20overflow.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22ClamAV%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22Integer%20overflow%20in%207z%20SubStreams%20count%20leading%20to%20heap%20buffer%20overflow%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-8DRZW7VM",
  "bug_class": "Integer Overflow",
  "created_at": "2026-03-29T20:42:42+00:00",
  "description": "An integer overflow when computing the SubStreams count in the 7z archive parser results in an undersized allocation and subsequent heap buffer overflow.",
  "location": null,
  "project": "ClamAV",
  "technical_details": null,
  "title": "Integer overflow in 7z SubStreams count leading to heap buffer overflow",
```
