<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-RVPC18B1 -->

# ANT-2026-RVPC18B1 · libgit2/libgit2

## heap-buffer-overflow medium

[GHSA-wfx7-g85r-q6vw](https://github.com/libgit2/libgit2/security/advisories/GHSA-wfx7-g85r-q6vw)

Claude medium
Security research firm medium
Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-RVPC18B1: Heap buffer overflow in bundled PCRE regex compilation via pre-compile/compile phase mismatch in atomic wrapping

A size mismatch between PCRE's pre-compile and compile phases when applying atomic-group wrapping leads to a heap buffer overflow during regex compilation.

**Project:** libgit2/libgit2

This finding was identified by static analysis and has not yet been dynamically reproduced. A trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-RVPC18B1.

---

**Reference:** ANT-2026-RVPC18B1

Triage and disclosure were performed by Trail of Bits.

:   medium

1. 2026-03-29
2. 2026-04-09
3. 2026-05-09
4. 2026-06-01
5. 2026-08-17

ff61b166630b666ba65794e93dc603c73b94d689cb24e5e278ccc9aaec77357155e8ed59e4a584226659042238d5105aba3cf083f1409261b11d5495faed05b2

Committed 2026-04-09 18:49 UTC

Revealed 2026-08-17 17:47 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-RVPC18B1%22%2C%22bug_class%22%3A%22Heap%20Buffer%20Overflow%22%2C%22claude_severity%22%3A%22medium%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A43%3A06%2B00%3A00%22%2C%22description%22%3A%22A%20size%20mismatch%20between%20PCRE%27s%20pre-compile%20and%20compile%20phases%20when%20applying%20atomic-group%20wrapping%20leads%20to%20a%20heap%20buffer%20overflow%20during%20regex%20compilation.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22libgit2%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22Heap%20buffer%20overflow%20in%20bundled%20PCRE%20regex%20compilation%20via%20pre-compile/compile%20phase%20mismatch%20in%20atomic%20wrapping%22%2C%22vendor_severity%22%3A%22medium%22%7D)

```
  "ant_id": "ANT-2026-RVPC18B1",
  "bug_class": "Heap Buffer Overflow",
  "claude_severity": "medium",
  "created_at": "2026-03-29T20:43:06+00:00",
  "description": "A size mismatch between PCRE's pre-compile and compile phases when applying atomic-group wrapping leads to a heap buffer overflow during regex compilation.",
  "project": "libgit2",
  "technical_details": null,
  "title": "Heap buffer overflow in bundled PCRE regex compilation via pre-compile/compile phase mismatch in atomic wrapping",
  "vendor_severity": "medium"
```
