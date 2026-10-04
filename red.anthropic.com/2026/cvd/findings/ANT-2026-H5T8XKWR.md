<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-H5T8XKWR -->

# ANT-2026-H5T8XKWR · tryghost/ghost

## sql-injection

[GHSA-w52v-v783-gw97](https://github.com/advisories/GHSA-w52v-v783-gw97)

MERGED

This finding was consolidated into
[ANT-2026-69D8H6RP](https://red.anthropic.com/2026/cvd/findings/ANT-2026-69D8H6RP.html)
after publication. Both entries described the same underlying
vulnerability; the surviving finding carries the full report and the
disclosure record. The original commitment below remains in the
ledger.

Advisories assigned to this finding before it was consolidated. The fix record is carried on the surviving finding.

<https://github.com/advisories/GHSA-w52v-v783-gw97>

6479c89ca89975bde1a83168dcdaf7c0efffd8b9c3938659365bc7a4974131645c651422ea7bf38a531543cbeecea4d68d0743fa17e25e35e030028719e4c652

Committed 2026-05-08 16:37 UTC

Revealed 2026-05-20 07:40 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-H5T8XKWR%22%2C%22bug_class%22%3A%22sql-injection%22%2C%22claude_severity%22%3A%22critical%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A43%3A35%2B00%3A00%22%2C%22description%22%3A%22The%20Ghost%20Content%20API%2C%20which%20is%20publicly%20accessible%20by%20design%2C%20fails%20to%20properly%20sanitize%20the%20slug%20filter%20parameter%20in%20query%20strings.%20An%20unauthenticated%20attacker%20can%20inject%20SQL%20via%20a%20crafted%20%60slug%3A%5B...%5D%60%20filter%20value.%20This%20allows%20reading%20arbitrary%20data%20from%20the%20Ghost%20database%2C%20including%20staff%20API%20keys%20and%20other%20sensitive%20records.%20Because%20the%20Content%20API%20key%20is%20intentionally%20public%2C%20no%20authentication%20barrier%20exists.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22TryGhost/Ghost%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3A%22User-supplied%20input%20in%20the%20Content%20API%20%60filter%60%20query-string%20parameter%20%28specifically%20%60slug%3A%5B...%5D%60%20expressions%29%20is%20incorporated%20into%20a%20SQL%20query%20without%20sufficient%20sanitization%2C%20permitting%20injection%20of%20arbitrary%20SQL%20and%20exfiltration%20of%20any%20row%20in%20the%20database.%22%2C%22title%22%3A%22SQL%20injection%20in%20Content%20API%22%2C%22vendor_severity%22%3Anull%7D)

```
  "ant_id": "ANT-2026-H5T8XKWR",
  "bug_class": "sql-injection",
  "claude_severity": "critical",
  "created_at": "2026-03-29T20:43:35+00:00",
  "description": "The Ghost Content API, which is publicly accessible by design, fails to properly sanitize the slug filter parameter in query strings. An unauthenticated attacker can inject SQL via a crafted `slug:[...]` filter value. This allows reading arbitrary data from the Ghost database, including staff API keys and other sensitive records. Because the Content API key is intentionally public, no authentication barrier exists.",
  "location": null,
  "project": "TryGhost/Ghost",
  "technical_details": "User-supplied input in the Content API `filter` query-string parameter (specifically `slug:[...]` expressions) is incorporated into a SQL query without sufficient sanitization, permitting injection of arbitrary SQL and exfiltration of any row in the database.",
  "title": "SQL injection in Content API",
  "vendor_severity": null
```
