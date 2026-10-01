<!-- source: https://red.anthropic.com/2026/cvd/about/ -->

# About this dashboard

Anthropic uses Claude to discover security vulnerabilities in widely used open-source software. When a finding is validated, the affected project's maintainers are notified privately and given time to issue a fix before details are made public consistent with the timelines provided in our [Coordinated Vulnerability Disclosure](https://www.anthropic.com/coordinated-vulnerability-disclosure) policy. This site summarizes the program's progress as of August 26, 2026.

EXTERNAL SECURITY RESEARCH FIRM PARTNERS

The following are the external security research firms that work with us to triage Claude's vulnerability findings and notify project maintainers. Additional detail on their analysis will follow in subsequent dashboard updates.

* [Ada Logics](https://adalogics.com/)
* [Anvil](https://www.anvilsecure.com/)
* [Calif.io](https://calif.io)
* [Doyensec](https://www.doyensec.com/)
* [Ophion Security](https://www.ophionsecurity.com/)
* [Trail of Bits](https://trailofbits.com/)

GLOSSARY

| Term | Definition |
| --- | --- |
| Candidates | Every distinct crash or vulnerability hypothesis that Claude produced across the program, before any triage. |
| True positive rate | The share of firm-reviewed findings confirmed as real, including duplicates and "won't fix" findings. |
| Total reported to maintainers | A finding whose report has been sent to the project maintainer. |
| Acknowledged by maintainer | The maintainer has responded to the report. The count of these findings reflects the fact the OSS maintainers are experiencing a higher volume of inbound security findings. Our teams reach out to maintainers based on the severity of the findings and existing maintainer volume. |
| Patched upstream | A patch has landed after the report was sent. |
| CVEs and GHSAs assigned | A CVE or GHSA identifier assigned to a finding. Identifiers themselves are listed once the finding's disclosure window has closed. |
| Disclosure window | See [Anthropic's Coordinated Vulnerability Disclosure policy](https://www.anthropic.com/coordinated-vulnerability-disclosure). |
| Commitment hash | A SHA-3-512 hash of the finding, published when the disclosure clock starts. |
| Ledger | The record of commitment hashes and their reveal state. Hashes are never removed, and the identifier, project, bug class, advisories, severities and dates revealed on a prior snapshot are never removed; a finding may later be marked withdrawn or merged, with the date and, where recorded, the reason. An advisory identifier published in error stays visible as a struck-through correction rather than being removed. A finding withdrawn while it remains revealed keeps its full card; only when a finding's reveal is cleared after publication are its report text and preimage withheld. |
| Withdrawn | A commitment whose finding was retracted. Before the finding is revealed it shows only the hash and commitment date; after it has been revealed it keeps its identifier and advisories and is marked withdrawn with the date and reason. |
| Merged | A commitment whose finding was consolidated into another finding; the entry keeps its identifier and links to the surviving finding. |
| Severity | The assessor's rating of impact (critical, high, medium, low). |
| Claude-assessed severity | The severity Claude assigned when it first analyzed the finding, recorded on the canonical report before any external review. |
| Firm-assessed severity | The severity assigned by an external security research firm during triage. It exists only for findings a firm has reviewed. |
| Maintainer-assessed severity | The severity assigned by the project maintainer, typically through a published security advisory. It exists only when the maintainer has provided one. |
| Bug class | The vulnerability category. |

VERIFYING A COMMITMENT

The commitment hash is the SHA-3-512 digest of a canonical JSON document. The document has sorted keys, no whitespace between tokens, and is encoded as UTF-8. It contains the finding identifier, project, creation time, title, bug class, target commit, location, discovery time, Claude's and the security research firm's severity assessments, the description, technical details, reproduction steps, and the SHA-256 of the proof-of-concept artifact. Fields not known at approval time are recorded as `null`. The preimage records each assessment as of approval; if the external security research firm later revises its severity, the card shows the current value marked as revised alongside the sealed one. To verify, download the preimage JSON from the finding card and confirm that its SHA-3-512 digest matches the commitment hash published on the ledger.

Each ledger entry shows more detail as it progresses through disclosure: before the maintainer has been notified, only the commitment hash and the commitment date are published; once the report has been sent, the status and the severity assessments are shown and the discovery date is published (it drives the date filter); and the identifier, project, and bug class are revealed only when the disclosure window closes. A commitment that is withdrawn at any stage keeps its hash and commitment date and is marked withdrawn in the status column; a commitment withdrawn before the finding was revealed is also struck through in the table.

FINDING CARDS

Once a finding's disclosure window closes, its identifier in the ledger links to a finding card. A card shows the project, bug class, and severity. When the report body carries substantive content, the card also shows Anthropic's analysis of the finding. Every card links to any assigned advisory and shows the commitment hash. A card for a finding that remains published also shows the preimage JSON, so that the published card can be verified against the ledger entry that committed to it. A finding withdrawn while it remains revealed keeps its full card, report text and preimage included, marked as withdrawn after publication. Only a finding whose reveal was cleared after publication has its card replaced by a page that keeps the hash and identifiers but withholds the report text and the preimage, because the preimage is the withdrawn report.
