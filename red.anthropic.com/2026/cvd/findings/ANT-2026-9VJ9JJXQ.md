<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-9VJ9JJXQ -->

# ANT-2026-9VJ9JJXQ · junrar

## path-traversal medium

[GHSA-j273-m5qq-6825](https://github.com/advisories/GHSA-j273-m5qq-6825)

Security research firm -
Maintainer medium

Anthropic's analysis of this finding, sealed at approval.

# ANT-2026-9VJ9JJXQ: Arbitrary file write due to backslash path traversal

Arbitrary file write due to backslash path traversal.

**Project:** junrar

Path sanitization fails to account for backslash (`\`) as a directory separator, allowing traversal sequences to bypass checks and write files to arbitrary locations.

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-9VJ9JJXQ.

---

**Reference:** ANT-2026-9VJ9JJXQ

ADVISORY

<https://github.com/junrar/junrar/security/advisories/GHSA-j273-m5qq-6825>

1. 2026-02-25
2. 2026-02-26
3. 2026-03-29
4. 2026-05-08
5. 2026-05-20

13bbdaec20acded7c4956102a40ff8d229d80f0392e67a98291fdb9596eb048217b4402ddd65a0d4ac1ca6f95eea4854a0fba28e33811baddae7e5857dcbdb1f

Committed 2026-05-08 09:37 PT

Revealed 2026-05-20 00:40 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-9VJ9JJXQ%22%2C%22bug_class%22%3A%22Path%20Traversal%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A45%3A57%2B00%3A00%22%2C%22description%22%3A%22Arbitrary%20file%20write%20due%20to%20backslash%20path%20traversal.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22junrar%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3A%22Path%20sanitization%20fails%20to%20account%20for%20backslash%20%28%60%5C%5C%60%29%20as%20a%20directory%20separator%2C%20allowing%20traversal%20sequences%20to%20bypass%20checks%20and%20write%20files%20to%20arbitrary%20locations.%22%2C%22title%22%3A%22Arbitrary%20file%20write%20due%20to%20backslash%20path%20traversal%22%2C%22vendor_severity%22%3Anull%7D)

```
  "ant_id": "ANT-2026-9VJ9JJXQ",
  "bug_class": "Path Traversal",
  "created_at": "2026-03-29T20:45:57+00:00",
  "description": "Arbitrary file write due to backslash path traversal.",
  "project": "junrar",
  "technical_details": "Path sanitization fails to account for backslash (`\\`) as a directory separator, allowing traversal sequences to bypass checks and write files to arbitrary locations.",
  "title": "Arbitrary file write due to backslash path traversal",
  "vendor_severity": null
```
