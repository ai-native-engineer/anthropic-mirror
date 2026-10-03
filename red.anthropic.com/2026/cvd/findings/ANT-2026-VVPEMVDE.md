<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-VVPEMVDE -->

# ANT-2026-VVPEMVDE · cisco-talos/clamav

## integer-overflow high

[CVE-2026-20213](https://nvd.nist.gov/vuln/detail/CVE-2026-20213)
[GHSA-rjvx-x4g3-vr6w](https://github.com/advisories/GHSA-rjvx-x4g3-vr6w)

Maintainer high

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-VVPEMVDE: Integer overflow in PE rebuild section size summation in Aspack unpacker

An integer overflow occurs when summing section sizes during PE rebuild in the Aspack unpacker.

**Project:** cisco-talos/clamav
**Location:** `libclamav/rebuildpe.c:cli_rebuildpe_align (lines ~140-144)`

This finding was identified by static analysis and has not yet been dynamically reproduced. A trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-VVPEMVDE.

---

**Reference:** ANT-2026-VVPEMVDE

Triage and disclosure were performed by Trail of Bits.

ADVISORY

<https://github.com/Cisco-Talos/clamav/commit/ca39e3843b47f298c3315996df30cf937c20c4ee>

1. 2026-03-29
2. 2026-04-09
3. 2026-05-07
4. 2026-05-07
5. 2026-07-21

89125e041730615a2fff06ae6e0eff4b40b6408d111f17abde7f218c7f212abf26dd07500ce51127eac4875d6d9bbc7c8a90e37310611e2c394c3aea90d93723

Committed 2026-04-09 18:49 UTC

Revealed 2026-07-21 05:25 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-VVPEMVDE%22%2C%22bug_class%22%3A%22Integer%20Overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A42%3A41%2B00%3A00%22%2C%22description%22%3A%22An%20integer%20overflow%20occurs%20when%20summing%20section%20sizes%20during%20PE%20rebuild%20in%20the%20Aspack%20unpacker.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22ClamAV%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22Integer%20overflow%20in%20PE%20rebuild%20section%20size%20summation%20in%20Aspack%20unpacker%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-VVPEMVDE",
  "bug_class": "Integer Overflow",
  "created_at": "2026-03-29T20:42:41+00:00",
  "description": "An integer overflow occurs when summing section sizes during PE rebuild in the Aspack unpacker.",
  "project": "ClamAV",
  "technical_details": null,
  "title": "Integer overflow in PE rebuild section size summation in Aspack unpacker",
```
