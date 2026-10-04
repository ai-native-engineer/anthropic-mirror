<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-DJBBBBPE -->

# ANT-2026-DJBBBBPE · temporalio/temporal

## broken-access-control low

[CVE-2026-5199](https://nvd.nist.gov/vuln/detail/CVE-2026-5199)

Claude critical
Security research firm -
Maintainer low

Anthropic's analysis of this finding, sealed at approval.

# ANT-2026-DJBBBBPE: Cross-namespace manipulation (including deletion) of workflows on the same cluster

Workflows can be manipulated or deleted across namespace boundaries within the same cluster.

**Project:** temporalio/temporal

checkNamespaceID() at activities.go:283 only compares batchParams.NamespaceId to a.namespaceID; the redundant batchParams.Request.Namespace field is never checked and is then used verbatim in frontendClient.SignalWorkflowExecution / DeleteWorkflowExecution / etc. Because frontendClient dials internal-frontend, whose noopClaimMapper.GetClaims returns &Claims{System: RoleAdmin} unconditionally, the server-side component acts as a confused deputy executing privileged operations against an attacker-chosen namespace.

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-DJBBBBPE.

---

**Reference:** ANT-2026-DJBBBBPE

1. 2026-03-22
2. 2026-03-29
3. 2026-04-01
4. 2026-05-08
5. 2026-05-20

6f20094036e4b8c066b9a2f033c4e59b99f883e623acbb0256d7ce0310528a13c03d24f7d1f5a1817de5b29e350a97a62ead6a93eb9a92e6881fb17052a7d2e4

Committed 2026-05-08 16:37 UTC

Revealed 2026-05-20 07:40 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-DJBBBBPE%22%2C%22bug_class%22%3A%22Broken%20Access%20Control%22%2C%22claude_severity%22%3A%22critical%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A43%3A54%2B00%3A00%22%2C%22description%22%3A%22Workflows%20can%20be%20manipulated%20or%20deleted%20across%20namespace%20boundaries%20within%20the%20same%20cluster.%22%2C%22discovered_at%22%3A%222026-03-22T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22temporalio/temporal%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3A%22checkNamespaceID%28%29%20at%20activities.go%3A283%20only%20compares%20batchParams.NamespaceId%20to%20a.namespaceID%3B%20the%20redundant%20batchParams.Request.Namespace%20field%20is%20never%20checked%20and%20is%20then%20used%20verbatim%20in%20frontendClient.SignalWorkflowExecution%20/%20DeleteWorkflowExecution%20/%20etc.%20Because%20frontendClient%20dials%20internal-frontend%2C%20whose%20noopClaimMapper.GetClaims%20returns%20%26Claims%7BSystem%3A%20RoleAdmin%7D%20unconditionally%2C%20the%20server-side%20component%20acts%20as%20a%20confused%20deputy%20executing%20privileged%20operations%20against%20an%20attacker-chosen%20namespace.%22%2C%22title%22%3A%22Cross-namespace%20manipulation%20%28including%20deletion%29%20of%20workflows%20on%20the%20same%20cluster%22%2C%22vendor_severity%22%3Anull%7D)

```
  "ant_id": "ANT-2026-DJBBBBPE",
  "bug_class": "Broken Access Control",
  "claude_severity": "critical",
  "created_at": "2026-03-29T20:43:54+00:00",
  "description": "Workflows can be manipulated or deleted across namespace boundaries within the same cluster.",
  "discovered_at": "2026-03-22T00:00:00+00:00",
  "location": null,
  "project": "temporalio/temporal",
  "technical_details": "checkNamespaceID() at activities.go:283 only compares batchParams.NamespaceId to a.namespaceID; the redundant batchParams.Request.Namespace field is never checked and is then used verbatim in frontendClient.SignalWorkflowExecution / DeleteWorkflowExecution / etc. Because frontendClient dials internal-frontend, whose noopClaimMapper.GetClaims returns &Claims{System: RoleAdmin} unconditionally, the server-side component acts as a confused deputy executing privileged operations against an attacker-chosen namespace.",
  "title": "Cross-namespace manipulation (including deletion) of workflows on the same cluster",
  "vendor_severity": null
```
