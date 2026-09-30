<!-- source: https://red.anthropic.com/2026/cvd/ -->

# Anthropic's coordinated vulnerability disclosure dashboard

Last updated 2026-08-26 11:55 PT.

In February 2026, Anthropic began using an early snapshot of Claude Mythos Preview to find security vulnerabilities in open-source software. We then partnered with external security research firms to triage findings, validate them, and report human-reviewed critical- or high-severity vulnerabilities to the software's maintainers under our [Coordinated Vulnerability Disclosure policy](https://www.anthropic.com/coordinated-vulnerability-disclosure). This page tracks the findings that we've disclosed, and, in line with our policy, publishes details of the ones whose disclosure window has now closed.

As of August 26, 2026, we've disclosed 2,300 vulnerabilities across 392 open source projects. To our knowledge, 421 of these have been patched. Across all findings in the ledger, 462 identifiers have been issued: 177 CVE records and 285 GitHub Security Advisories (a single finding may carry both). In other cases, maintainers have shipped a fix without publishing an advisory. The number of vulnerabilities we've disclosed is a subset of the total number of vulnerabilities that Mythos Preview (and other Claude models) has found, since the process of independent human triage and review is the rate limiting step.

This page covers a headline count of the vulnerabilities we've disclosed, and a breakdown of these by class. For those vulnerabilities we've disclosed and where the disclosure window has now closed, it also includes identifier records (CVE & GHSA) and finding details, further below.

Finally, it includes a disclosure ledger, which lists a hash commitment for every finding we've disclosed that is still inside the disclosure window, so that the finding's existence and commitment date can be proved without revealing its content.

Assessed by

Claude-assessed
Firm-assessed
Maintainer-assessed

critical
high
medium
low

Discovered

to

Clear

Showing all assessment sources and severities for findings discovered between November 1, 2025 and August 26, 2026.

The date range filters by discovery date and combines with the severity selection. The flowchart, the disclosure ledger, the identifier records, and the severity-agreement heatmap reflect findings discovered in the selected window.

Discovered
Triaged
[26,153 findings
Candidates](#ledger)

[5,008 findings
Reviewed by external security firms](#ledger)

[4,576 findings
Confirmed valid
91.4% true positives of 5,008](#ledger)

[1,022 findings
Reported to maintainers](#ledger)
[1,278 findings
Reported direct to maintainers by Anthropic, at their request
May contain false positives](#ledger)
Disclosed
Remediated
[2,300 findings
Total reported to maintainers](#ledger)

[1,815 findings
Acknowledged by maintainer](#ledger)

[421 findings
Patched upstream](#ledger)

[462 advisories
CVEs and GHSAs assigned](#ledger)
Counts as of August 26, 2026 [Showing all assessment sources and severities for findings discovered between November 1, 2025 and August 26, 2026.](#filters "Showing all assessment sources and severities for findings discovered between November 1, 2025 and August 26, 2026.")

The statistics above reflect all bugs found by Claude Mythos Preview and other Claude models. They can also be filtered by severity under at least one of three assessment sources: Claude's own assessment, the assessment of the external security research firm that triaged the finding, or the project maintainer's assessment. Each source is defined in the glossary on the [About](https://red.anthropic.com/2026/cvd/about/index.html) page, and the filtered view states how many findings the selected sources have not assessed. These figures are designed to reflect our coordinated vulnerability disclosure process, which works approximately as follows. A glossary of the terms is available on the [About](https://red.anthropic.com/2026/cvd/about/index.html) page.

First, our models find candidate vulnerabilities, which we add to a list for human triage. This is the figure at the top. (The previous update included Mythos Preview; this one includes candidates from Mythos Preview, other Mythos-class models, and other Claude models.)

Then, in order to disclose a vulnerability to a maintainer, we take one of two steps.

**Triage:** In most cases, we pass them to one of six external security research firms that we have engaged for this endeavor, or we triage them ourselves. We or the security research firms reproduce each issue, assess whether it is a real bug (and if so, assess how severe it is), and then write a report for confirmed bugs that will go to the project's maintainer. Importantly, there are many additional bugs that we or our security partners have investigated and confirmed are real but that we have not yet reported to maintainers, due to capacity limitations.

In our triage process, the "true positive rate" (the number of findings confirmed as valid, as a share of the number of findings manually reviewed) reflects how often the external security research firms determined that a finding Mythos Preview (and other Claude models) produced was a real vulnerability. This includes real bugs that we later discover have already been reported, and "won't fix" findings (the bug is real, but the maintainer is unlikely to address it—e.g. because it falls outside the project's threat model, or affects code that isn't typically reachable). We include these in the true positive rate because we're reliant on our security research partners (rather than maintainers) to tell us how many bugs they've confirmed, and it's only *after* the maintainers have received the report and assessed the vulnerability that we'll learn whether a vulnerability is one they plan to fix. For this reason, it's also possible that a vendor has marked a vulnerability as a true positive (or a false positive) in error. Given this, the number of "true positives" in the dashboard above should only be taken as one proxy for impact. Another, more reliable one is the number of patches created, though this is only a lagging indicator of progress, since patches take a long time to create.

**Direct disclosure:** Some vulnerabilities are disclosed to maintainers directly by Anthropic staff, and don't go through the same independent check. This happens when maintainers specifically request that we provide them un-triaged findings.

Once bugs have either been triaged or directly disclosed, "Acknowledged by maintainer" counts all bugs whose reports maintainers have responded to. "Patched upstream" reflects the number of those vulnerabilities that maintainers have since created and released fixes for, though this does not guarantee that those patches have been widely installed. Finally, "CVEs and GHSAs assigned" counts the CVE records and GitHub Security Advisories issued across all findings in the ledger, whether or not a patch has shipped (a finding may carry both). Some advisories are now public, and we list them out further down on this page. We leave whether to create a security advisory up to the discretion of maintainers.

See [About](https://red.anthropic.com/2026/cvd/about/index.html) for more information.

DISCLOSURE LEDGER [Showing all assessment sources and severities for findings discovered between November 1, 2025 and August 26, 2026.](#filters "Showing all assessment sources and severities for findings discovered between November 1, 2025 and August 26, 2026.")

Once a finding has been validated by one of our external security research firms, a SHA-3-512 hash of the sealed report is published immediately as proof of possession. Each ledger entry shows more detail as it progresses through disclosure: before the maintainer has been notified, only the commitment hash and the commitment date are published; once the report has been sent, the status and the severity assessments are shown and the discovery date is published (it drives the date filter); and the identifier, project, and bug class are revealed only when the disclosure window closes. A commitment that is withdrawn at any stage keeps its hash and commitment date and is marked withdrawn in the status column; a commitment withdrawn before the finding was revealed is also struck through in the table.

2,736 / 2,736  · [View full ledger →](https://red.anthropic.com/2026/cvd/ledger/index.html)

Search

 Revealed only
Clear

Project
All projects

Bug class
All classes

Status
All statuses

Assessed by

Page filters
Any source Claude-assessed
Firm-assessed
Maintainer-assessed

Page filters
Any severity Critical
High
Medium
Low

Discovered

to

Local filters are overriding the page filters for this table. Use page filters

| Date committed | Hash / identifier | Project | Bug class | Severity assessments | Status |
| --- | --- | --- | --- | --- | --- |
| 2026-08-26 | 07eaeaba04c0… | — | — | Claude: highFirm: medium | disclosed |
| 2026-08-26 | b9d73e0d02d5… | — | — | Claude: highFirm: high | disclosed |
| 2026-08-25 | f077c53dcce5… | — | — | Claude: highFirm: high | disclosed |
| 2026-08-25 | d2994b50747e… | — | — | Claude: highFirm: high | disclosed |
| 2026-08-25 | 4c50b368332d… | — | — | Claude: highFirm: high | disclosed |
| 2026-08-25 | c59c619f86af… | — | — | Claude: highFirm: high | disclosed |
| 2026-08-25 | f1770083897e… | — | — | Claude: highFirm: high | disclosed |
| 2026-08-25 | febeaf46a9ce… | — | — | Claude: highFirm: high | disclosed |
| 2026-08-25 | 4c49aa66ad57… | — | — | Claude: criticalFirm: highMaintainer: high | disclosed |
| 2026-08-25 | a722bcfe171a… | — | — | Claude: criticalFirm: critical | disclosed |

‹ Prev
Next ›

[View all 2,736 entries →](https://red.anthropic.com/2026/cvd/ledger/index.html)

CVEs [Showing all assessment sources and severities for findings discovered between November 1, 2025 and August 26, 2026.](#filters "Showing all assessment sources and severities for findings discovered between November 1, 2025 and August 26, 2026.")

Common Vulnerabilities and Exposures records assigned to findings disclosed through this program. The records below are publicly available. The remainder are reserved, pending publication by the assigning authority.

[CVE-2026-12340](https://nvd.nist.gov/vuln/detail/CVE-2026-12340)
wolfssl/wolfssl · heap-buffer-overflow · low · [ANT-2026-87DJGDRB](https://red.anthropic.com/2026/cvd/findings/ANT-2026-87DJGDRB.html)
Heap-buffer-overflow in sha.c:733

[CVE-2026-13002](https://nvd.nist.gov/vuln/detail/CVE-2026-13002)
dnsmasq · denial-of-service · medium · [ANT-2026-QRYCJNAP](https://red.anthropic.com/2026/cvd/findings/ANT-2026-QRYCJNAP.html)
DNSSEC NSEC typemap infinite loop hangs daemon

[CVE-2026-13595](https://nvd.nist.gov/vuln/detail/CVE-2026-13595)
util-linux/util-linux · use-after-free · medium · [ANT-2026-ZRDQDR79](https://red.anthropic.com/2026/cvd/findings/ANT-2026-ZRDQDR79.html)
heap-use-after-free in util-linux

[CVE-2026-20213](https://nvd.nist.gov/vuln/detail/CVE-2026-20213)
cisco-talos/clamav · integer-overflow · high · [ANT-2026-VVPEMVDE](https://red.anthropic.com/2026/cvd/findings/ANT-2026-VVPEMVDE.html)
Integer overflow in PE rebuild section size summation in Aspack unpacker

[CVE-2026-20214](https://nvd.nist.gov/vuln/detail/CVE-2026-20214)
cisco-talos/clamav · integer-underflow · high · [ANT-2026-Z477W54M](https://red.anthropic.com/2026/cvd/findings/ANT-2026-Z477W54M.html)
Unsigned integer underflow in FSG unpacker section loop

[CVE-2026-20215](https://nvd.nist.gov/vuln/detail/CVE-2026-20215)
cisco-talos/clamav · integer-overflow · high · [ANT-2026-8DRZW7VM](https://red.anthropic.com/2026/cvd/findings/ANT-2026-8DRZW7VM.html)
Integer overflow in 7z SubStreams count leading to heap buffer overflow

[CVE-2026-26980](https://nvd.nist.gov/vuln/detail/CVE-2026-26980)
tryghost/ghost · sql-injection · critical · [ANT-2026-69D8H6RP](https://red.anthropic.com/2026/cvd/findings/ANT-2026-69D8H6RP.html)
Critical Vulnerability (CVSS 9.1) : SQLi from unauthenticated user; arbitrary DB reads

[CVE-2026-27654](https://nvd.nist.gov/vuln/detail/CVE-2026-27654)
nginx/nginx · heap-buffer-overflow · high · [ANT-2026-HY56VRSB](https://red.anthropic.com/2026/cvd/findings/ANT-2026-HY56VRSB.html)
Heap buffer overflow in DAV COPY/MOVE with alias directive. Destination URI shorter than alias length causes size\_t underflow in ngx\_http\_map\_uri\_to\_path buffer calculation, then ngx\_copy overflows th

[CVE-2026-29198](https://nvd.nist.gov/vuln/detail/CVE-2026-29198)
rocketchat/rocket.chat · sql-injection · critical · [ANT-2026-GEM3N3N3](https://red.anthropic.com/2026/cvd/findings/ANT-2026-GEM3N3N3.html)
Critical vulnerability (cvss 9.8): complete authentication bypass to admin permissions

[CVE-2026-31554](https://nvd.nist.gov/vuln/detail/CVE-2026-31554)
torvalds/linux · use-after-free · high · [ANT-2026-1BCAFJCC](https://red.anthropic.com/2026/cvd/findings/ANT-2026-1BCAFJCC.html)
futex: UAF in private-hash teardown via cross-process sys\_futex\_requeue leading giving LPE

[CVE-2026-32316](https://nvd.nist.gov/vuln/detail/CVE-2026-32316)
jqlang/jq · heap-buffer-overflow · medium · [ANT-2026-EBDTPNVH](https://red.anthropic.com/2026/cvd/findings/ANT-2026-EBDTPNVH.html)
Integer overflow in string concatenation leading to 1 GB memcpy heap buffer overflow

[CVE-2026-33721](https://nvd.nist.gov/vuln/detail/CVE-2026-33721)
mapserver · heap-buffer-overflow · medium · [ANT-2026-9SZMPW41](https://red.anthropic.com/2026/cvd/findings/ANT-2026-9SZMPW41.html)
Heap buffer overflow in SLD categorize threshold parsing due to wrong counter variable in reallocation guard

[CVE-2026-33901](https://nvd.nist.gov/vuln/detail/CVE-2026-33901)
imagemagick/imagemagick · heap-buffer-overflow · high · [ANT-2026-T44WA684](https://red.anthropic.com/2026/cvd/findings/ANT-2026-T44WA684.html)
Heap buffer overflow in MVG pattern rendering via CopyMagickString without bounds check

[CVE-2026-34580](https://nvd.nist.gov/vuln/detail/CVE-2026-34580)
randombit/botan · improper-cert-validation · high · [ANT-2026-2FETJP49](https://red.anthropic.com/2026/cvd/findings/ANT-2026-2FETJP49.html)
[security] certificate\_known(): Complete x509 bypass

[CVE-2026-35590](https://nvd.nist.gov/vuln/detail/CVE-2026-35590)
libvips/libvips · oob-write · low · [ANT-2026-JBKARRJ7](https://red.anthropic.com/2026/cvd/findings/ANT-2026-JBKARRJ7.html)
Out-of-bounds IFD array access in EXIF metadata processing leading to write through corrupted pointer

[CVE-2026-40033](https://nvd.nist.gov/vuln/detail/CVE-2026-40033)
freerdp/freerdp · heap-buffer-overflow · critical · [ANT-2026-RXYVE4DZ](https://red.anthropic.com/2026/cvd/findings/ANT-2026-RXYVE4DZ.html)
Heap-buffer-overflow in sanitizer\_common\_interceptors.inc:827

[CVE-2026-40383](https://nvd.nist.gov/vuln/detail/CVE-2026-40383)
joomla/joomla-cms · path-traversal · high · [ANT-2026-HHD77M82](https://red.anthropic.com/2026/cvd/findings/ANT-2026-HHD77M82.html)
Path Traversal in `layout` Parameter Leads to Arbitrary PHP File Inclusion (LFI → RCE)

[CVE-2026-40384](https://nvd.nist.gov/vuln/detail/CVE-2026-40384)
joomla/joomla-cms · path-traversal · medium · [ANT-2026-GSV3GS1G](https://red.anthropic.com/2026/cvd/findings/ANT-2026-GSV3GS1G.html)
Path Traversal via Glob Injection in com\_media Search

[CVE-2026-40528](https://nvd.nist.gov/vuln/detail/CVE-2026-40528)
opensc · stack-buffer-overflow · low · [ANT-2026-GSDN3H7W](https://red.anthropic.com/2026/cvd/findings/ANT-2026-GSDN3H7W.html)
Stack buffer overflow in do\_key\_value profile parsing via unbounded memcpy into 32-byte buffer

[CVE-2026-40685](https://nvd.nist.gov/vuln/detail/CVE-2026-40685)
exim/exim · off-by-one · medium · [ANT-2026-B615AQ9E](https://red.anthropic.com/2026/cvd/findings/ANT-2026-B615AQ9E.html)
Exim dewrap() Off-By-One OOB Read → Code Execution

[CVE-2026-41401](https://nvd.nist.gov/vuln/detail/CVE-2026-41401)
cesnet/libyang · use-after-free · medium · [ANT-2026-TZQ1KH7E](https://red.anthropic.com/2026/cvd/findings/ANT-2026-TZQ1KH7E.html)
Heap use-after-free write in metadata list management during XML data parsing due to incorrect list head pointer update

[CVE-2026-41579](https://nvd.nist.gov/vuln/detail/CVE-2026-41579)
opencontainers/runc · symlink-following · medium · [ANT-2026-N6TD9MF6](https://red.anthropic.com/2026/cvd/findings/ANT-2026-N6TD9MF6.html)
Host filesystem write via /dev symlink in container image

[CVE-2026-41990](https://nvd.nist.gov/vuln/detail/CVE-2026-41990)
gpg/libgcrypt · stack-buffer-overflow · medium · [ANT-2026-GSPVGEYA](https://red.anthropic.com/2026/cvd/findings/ANT-2026-GSPVGEYA.html)
ML-DSA context string stack buffer overflow

[CVE-2026-43074](https://nvd.nist.gov/vuln/detail/CVE-2026-43074)
torvalds/linux · use-after-free · high · [ANT-2026-CM0TCREP](https://red.anthropic.com/2026/cvd/findings/ANT-2026-CM0TCREP.html)
UAF in ep\_get\_upwards\_depth\_proc() giving unprivileged LPE

[CVE-2026-44420](https://nvd.nist.gov/vuln/detail/CVE-2026-44420)
freerdp/freerdp · heap-buffer-overflow · critical · [ANT-2026-H97FY6C8](https://red.anthropic.com/2026/cvd/findings/ANT-2026-H97FY6C8.html)
Heap-buffer-overflow in cliprdr\_main.c:547

[CVE-2026-44421](https://nvd.nist.gov/vuln/detail/CVE-2026-44421)
freerdp/freerdp · heap-buffer-overflow · critical · [ANT-2026-RXYVE4DZ](https://red.anthropic.com/2026/cvd/findings/ANT-2026-RXYVE4DZ.html)
Heap-buffer-overflow in sanitizer\_common\_interceptors.inc:827

[CVE-2026-45447](https://nvd.nist.gov/vuln/detail/CVE-2026-45447)
openssl/openssl · use-after-free · critical · [ANT-2026-AYWQW7P2](https://red.anthropic.com/2026/cvd/findings/ANT-2026-AYWQW7P2.html)
PKCS7\_verify frees caller-owned `indata` BIO when `digestAlgorithms` SET is empty

[CVE-2026-45696](https://nvd.nist.gov/vuln/detail/CVE-2026-45696)
openexr · heap-buffer-overflow · high · [ANT-2026-QQ2P9M9V](https://red.anthropic.com/2026/cvd/findings/ANT-2026-QQ2P9M9V.html)
Heap-buffer-overflow in internal\_ht.cpp:305

[CVE-2026-45700](https://nvd.nist.gov/vuln/detail/CVE-2026-45700)
freerdp/freerdp · heap-buffer-overflow · critical · [ANT-2026-HN9XZXJ9](https://red.anthropic.com/2026/cvd/findings/ANT-2026-HN9XZXJ9.html)
heap-buffer-overflow write (attacker-controlled offset, partially-controlled data via rle delta values; up to ~15kb overwrite past ptempdata with these parameters, further with larger nxdst) in planar.c:472

[CVE-2026-46348](https://nvd.nist.gov/vuln/detail/CVE-2026-46348)
mastodon/mastodon · ssrf · high · [ANT-2026-6DSMTXZ8](https://red.anthropic.com/2026/cvd/findings/ANT-2026-6DSMTXZ8.html)
SSRF Bypass via IPv6 Unspecified Address (`::`) in Mastodon

[CVE-2026-46349](https://nvd.nist.gov/vuln/detail/CVE-2026-46349)
mastodon/mastodon · signature-bypass · high · [ANT-2026-P2DWB2SK](https://red.anthropic.com/2026/cvd/findings/ANT-2026-P2DWB2SK.html)
LD-Signature bypass via JSON-LD named-graph restructuring

[CVE-2026-46633](https://nvd.nist.gov/vuln/detail/CVE-2026-46633)
twigphp/twig · code-injection · critical · [ANT-2026-J3EVXWDY](https://red.anthropic.com/2026/cvd/findings/ANT-2026-J3EVXWDY.html)
PHP code injection via single quote in {% use %} template name

[CVE-2026-46639](https://nvd.nist.gov/vuln/detail/CVE-2026-46639)
twigphp/twig · auth-bypass · high · [ANT-2026-203E7E95](https://red.anthropic.com/2026/cvd/findings/ANT-2026-203E7E95.html)
Sandbox bypass via object-destructuring assignment

[CVE-2026-47345](https://nvd.nist.gov/vuln/detail/CVE-2026-47345)
typo3 · xss · medium · [ANT-2026-MHJX7J31](https://red.anthropic.com/2026/cvd/findings/ANT-2026-MHJX7J31.html)
Stored XSS in TYPO3 HTML Sanitizer via `xmlns` Namespace URI Injection

[CVE-2026-4747](https://nvd.nist.gov/vuln/detail/CVE-2026-4747)
freebsd/freebsd-src · stack-buffer-overflow · high · [ANT-2026-MVVACQKN](https://red.anthropic.com/2026/cvd/findings/ANT-2026-MVVACQKN.html)
Unauthenticated remote code execution via svc\_rpc\_gss\_validate stack overflow

[CVE-2026-4890](https://nvd.nist.gov/vuln/detail/CVE-2026-4890)
dnsmasq · denial-of-service · medium · [ANT-2026-QRYCJNAP](https://red.anthropic.com/2026/cvd/findings/ANT-2026-QRYCJNAP.html)
DNSSEC NSEC typemap infinite loop hangs daemon

[CVE-2026-4892](https://nvd.nist.gov/vuln/detail/CVE-2026-4892)
dnsmasq · heap-buffer-overflow · high · [ANT-2026-PCBAKVPB](https://red.anthropic.com/2026/cvd/findings/ANT-2026-PCBAKVPB.html)
Heap overflow in privileged helper via oversized DHCPv6 client identifier

[CVE-2026-48929](https://nvd.nist.gov/vuln/detail/CVE-2026-48929)
rocketchat/rocket.chat · auth-bypass · high · [ANT-2026-QXNF2N9K](https://red.anthropic.com/2026/cvd/findings/ANT-2026-QXNF2N9K.html)
Unauthenticated Arbitrary File Deletion via `deleteFileMessage` Meteor Method

[CVE-2026-5194](https://nvd.nist.gov/vuln/detail/CVE-2026-5194)
wolfssl/wolfssl · other · critical · [ANT-2026-7DG11TPA](https://red.anthropic.com/2026/cvd/findings/ANT-2026-7DG11TPA.html)
[SECURITY: critical] Universal ECDSA certificate forgery for arbitrary hosts

[CVE-2026-5199](https://nvd.nist.gov/vuln/detail/CVE-2026-5199)
temporalio/temporal · broken-access-control · low · [ANT-2026-DJBBBBPE](https://red.anthropic.com/2026/cvd/findings/ANT-2026-DJBBBBPE.html)
Cross-namespace manipulation (including deletion) of workflows on the same cluster

[CVE-2026-5295](https://nvd.nist.gov/vuln/detail/CVE-2026-5295)
wolfssl/wolfssl · buffer-overflow · medium · [ANT-2026-JS5D1Z2X](https://red.anthropic.com/2026/cvd/findings/ANT-2026-JS5D1Z2X.html)
Stack buffer overflow in PKCS#7 OtherRecipientInfo OID copy

[CVE-2026-5398](https://nvd.nist.gov/vuln/detail/CVE-2026-5398)
freebsd/freebsd-src · use-after-free · high · [ANT-2026-5DFBSQR9](https://red.anthropic.com/2026/cvd/findings/ANT-2026-5DFBSQR9.html)
Local privilege escalation via tty\_drop\_ctty t\_session UAF + pmap\_pkru\_update\_range PDPE walk

[CVE-2026-5446](https://nvd.nist.gov/vuln/detail/CVE-2026-5446)
wolfssl/wolfssl · crypto-failure · medium · [ANT-2026-SB4PHA43](https://red.anthropic.com/2026/cvd/findings/ANT-2026-SB4PHA43.html)
ARIA-GCM Nonce Reuse in TLS 1.2 Record Encryption in wolfSSL

[CVE-2026-5447](https://nvd.nist.gov/vuln/detail/CVE-2026-5447)
wolfssl/wolfssl · heap-buffer-overflow · medium · [ANT-2026-VV0PRKKV](https://red.anthropic.com/2026/cvd/findings/ANT-2026-VV0PRKKV.html)
wolfSSL: heap buffer overflow in CertFromX509() from AuthorityKeyIdentifier size mismatch

[CVE-2026-5448](https://nvd.nist.gov/vuln/detail/CVE-2026-5448)
wolfssl/wolfssl · heap-buffer-overflow · low · [ANT-2026-6615Y595](https://red.anthropic.com/2026/cvd/findings/ANT-2026-6615Y595.html)
Final Assessment: 2-Byte Heap Overflow in wolfSSL\_X509\_notAfter / wolfSSL\_X509\_notBefore

[CVE-2026-5466](https://nvd.nist.gov/vuln/detail/CVE-2026-5466)
wolfssl/wolfssl · signature-bypass · high · [ANT-2026-KNXJMVYC](https://red.anthropic.com/2026/cvd/findings/ANT-2026-KNXJMVYC.html)
eccsi universal signature forgery via r 0 s 0 missing s

[CVE-2026-5477](https://nvd.nist.gov/vuln/detail/CVE-2026-5477)
wolfssl/wolfssl · integer-overflow · high · [ANT-2026-ZZY4987K](https://red.anthropic.com/2026/cvd/findings/ANT-2026-ZZY4987K.html)
cmac 32 bit totalsz wraparound prefix substitution forg

[CVE-2026-5479](https://nvd.nist.gov/vuln/detail/CVE-2026-5479)
wolfssl/wolfssl · crypto-failure · high · [ANT-2026-RSSMAMA7](https://red.anthropic.com/2026/cvd/findings/ANT-2026-RSSMAMA7.html)
wolfssl evp chacha20 poly1305 poly1305 tag never verifi

[CVE-2026-5500](https://nvd.nist.gov/vuln/detail/CVE-2026-5500)
wolfssl/wolfssl · crypto-failure · high · [ANT-2026-P23DVQM2](https://red.anthropic.com/2026/cvd/findings/ANT-2026-P23DVQM2.html)
cms authenvelopeddata aead forgery via gcm tag truncati

[CVE-2026-5501](https://nvd.nist.gov/vuln/detail/CVE-2026-5501)
wolfssl/wolfssl · improper-cert-validation · high · [ANT-2026-K8YY7WWS](https://red.anthropic.com/2026/cvd/findings/ANT-2026-K8YY7WWS.html)
wolfssl x509 verify cert leaf signature verification by

[CVE-2026-5503](https://nvd.nist.gov/vuln/detail/CVE-2026-5503)
wolfssl/wolfssl · heap-buffer-overflow · medium · [ANT-2026-0JRYQPCF](https://red.anthropic.com/2026/cvd/findings/ANT-2026-0JRYQPCF.html)
wolfssl ech heap buffer overflow via publicname sni pol

[CVE-2026-55084](https://nvd.nist.gov/vuln/detail/CVE-2026-55084)
dhis2/dhis2-core · sql-injection · high · [ANT-2026-FW0V6SAJ](https://red.anthropic.com/2026/cvd/findings/ANT-2026-FW0V6SAJ.html)
SQL Injection via Unquoted Column Name in SqlView Filter Parameter

[CVE-2026-56132](https://nvd.nist.gov/vuln/detail/CVE-2026-56132)
libexpat/libexpat · heap-buffer-overflow · medium · [ANT-2026-X3EB6DN3](https://red.anthropic.com/2026/cvd/findings/ANT-2026-X3EB6DN3.html)
This is a genuine heap-buffer-overflow WRITE vulnerability in expat's core XML DTD parser (`doProlog` function in `xmlparse.c`).

[CVE-2026-5747](https://nvd.nist.gov/vuln/detail/CVE-2026-5747)
firecracker-microvm/firecracker · oob-read · high · [ANT-2026-PQ3CNCCK](https://red.anthropic.com/2026/cvd/findings/ANT-2026-PQ3CNCCK.html)
Virtio-PCI queue size writable after activation enables host OOB

[CVE-2026-58435](https://nvd.nist.gov/vuln/detail/CVE-2026-58435)
go-gitea/gitea · idor · medium · [ANT-2026-VN61PHA0](https://red.anthropic.com/2026/cvd/findings/ANT-2026-VN61PHA0.html)
Gitea LFS Deploy-Key Privilege Escalation — Cross-Repository Data Exfiltration

[CVE-2026-6039](https://nvd.nist.gov/vuln/detail/CVE-2026-6039)
libreoffice · heap-buffer-overflow · medium · [ANT-2026-8FZYKRTH](https://red.anthropic.com/2026/cvd/findings/ANT-2026-8FZYKRTH.html)
Heap buffer overflow in DXF LWPOLYLINE import via integer truncation from sal\_Int32 to sal\_uInt16

[CVE-2026-6040](https://nvd.nist.gov/vuln/detail/CVE-2026-6040)
libreoffice · use-after-free · medium · [ANT-2026-6X60WXT0](https://red.anthropic.com/2026/cvd/findings/ANT-2026-6X60WXT0.html)
Heap use-after-free write in number format blank-width parsing via out-of-bounds remove() on freed buffer

[CVE-2026-6045](https://nvd.nist.gov/vuln/detail/CVE-2026-6045)
libreoffice · heap-buffer-overflow · medium · [ANT-2026-G7GNYY68](https://red.anthropic.com/2026/cvd/findings/ANT-2026-G7GNYY68.html)
Heap Buffer Overflow via Integer Overflow in EMF+ Brush Blend Point Parsing

[CVE-2026-6047](https://nvd.nist.gov/vuln/detail/CVE-2026-6047)
libreoffice · heap-buffer-overflow · medium · [ANT-2026-0HC68EK6](https://red.anthropic.com/2026/cvd/findings/ANT-2026-0HC68EK6.html)
Heap Buffer Overflow via Unsafe static\_cast in OOXML VML Textbox Replay

[CVE-2026-63559](https://nvd.nist.gov/vuln/detail/CVE-2026-63559)
open62541 · integer-overflow · high · [ANT-2026-PJV7Z0AR](https://red.anthropic.com/2026/cvd/findings/ANT-2026-PJV7Z0AR.html)
Integer overflow in variant dimension validation allowing wild-address write via arrayDimensions product overflow

[CVE-2026-6386](https://nvd.nist.gov/vuln/detail/CVE-2026-6386)
freebsd/freebsd-src · use-after-free · high · [ANT-2026-5DFBSQR9](https://red.anthropic.com/2026/cvd/findings/ANT-2026-5DFBSQR9.html)
Local privilege escalation via tty\_drop\_ctty t\_session UAF + pmap\_pkru\_update\_range PDPE walk

[CVE-2026-6479](https://nvd.nist.gov/vuln/detail/CVE-2026-6479)
postgres/postgres · denial-of-service · high · [ANT-2026-CJQWKW82](https://red.anthropic.com/2026/cvd/findings/ANT-2026-CJQWKW82.html)
Pre-auth unbounded recursion in ProcessStartupPacket: alternating SSL/GSS negotiation requests cause infinite recursion when both are rejected. ssl\_done/gss\_done flags oscillate (true,false)->(false,true) endlessly. No check\_stack\_depth. Pre-authentication.

[CVE-2026-65423](https://nvd.nist.gov/vuln/detail/CVE-2026-65423)
open62541 · integer-overflow · high · [ANT-2026-PJV7Z0AR](https://red.anthropic.com/2026/cvd/findings/ANT-2026-PJV7Z0AR.html)
Integer overflow in variant dimension validation allowing wild-address write via arrayDimensions product overflow

[CVE-2026-66032](https://nvd.nist.gov/vuln/detail/CVE-2026-66032)
libssh2/libssh2 · double-free · high · [ANT-2026-Q5A1RHS0](https://red.anthropic.com/2026/cvd/findings/ANT-2026-Q5A1RHS0.html)
SFTP double-free via server-controlled FXP\_STATUS packet length

[CVE-2026-6678](https://nvd.nist.gov/vuln/detail/CVE-2026-6678)
wolfssl/wolfssl · buffer-overflow · medium · [ANT-2026-JS5D1Z2X](https://red.anthropic.com/2026/cvd/findings/ANT-2026-JS5D1Z2X.html)
Stack buffer overflow in PKCS#7 OtherRecipientInfo OID copy

[CVE-2026-6772](https://nvd.nist.gov/vuln/detail/CVE-2026-6772)
nss · heap-buffer-overflow · high · [ANT-2026-1ZNMP148](https://red.anthropic.com/2026/cvd/findings/ANT-2026-1ZNMP148.html)
Off-by-one heap buffer overflow in TLS extension negotiation due to SSL\_MAX\_EXTENSIONS (22) being too small for 23 extensions

[CVE-2026-8356](https://nvd.nist.gov/vuln/detail/CVE-2026-8356)
libreoffice · stack-buffer-overflow · medium · [ANT-2026-TNXYTAEH](https://red.anthropic.com/2026/cvd/findings/ANT-2026-TNXYTAEH.html)
Stack-buffer-overflow in libreoffice

[CVE-2026-8357](https://nvd.nist.gov/vuln/detail/CVE-2026-8357)
libreoffice · heap-buffer-overflow · medium · [ANT-2026-XV1EVAMH](https://red.anthropic.com/2026/cvd/findings/ANT-2026-XV1EVAMH.html)
Heap-buffer-overflow in libreoffice

[CVE-2026-8358](https://nvd.nist.gov/vuln/detail/CVE-2026-8358)
libreoffice · heap-buffer-overflow · medium · [ANT-2026-YN5QG0SH](https://red.anthropic.com/2026/cvd/findings/ANT-2026-YN5QG0SH.html)
Heap-buffer-overflow in libreoffice

No published records fall inside the default discovery window.

‹  ›

GHSAs [Showing all assessment sources and severities for findings discovered between November 1, 2025 and August 26, 2026.](#filters "Showing all assessment sources and severities for findings discovered between November 1, 2025 and August 26, 2026.")

GitHub Security Advisory records assigned to findings disclosed through this program. The records below are publicly available. The remainder are reserved, pending publication by the assigning authority.

[GHSA-425r-vwq2-26qv](https://github.com/advisories/GHSA-425r-vwq2-26qv)
libexpat/libexpat · heap-buffer-overflow · medium · [ANT-2026-X3EB6DN3](https://red.anthropic.com/2026/cvd/findings/ANT-2026-X3EB6DN3.html)
This is a genuine heap-buffer-overflow WRITE vulnerability in expat's core XML DTD parser (`doProlog` function in `xmlparse.c`).

[GHSA-47qf-hp3h-rwmm](https://github.com/advisories/GHSA-47qf-hp3h-rwmm)
wolfssl/wolfssl · signature-bypass · high · [ANT-2026-KNXJMVYC](https://red.anthropic.com/2026/cvd/findings/ANT-2026-KNXJMVYC.html)
eccsi universal signature forgery via r 0 s 0 missing s

[GHSA-589g-qgf8-m6mx](https://github.com/advisories/GHSA-589g-qgf8-m6mx)
asterisk/asterisk · stack-buffer-overflow · critical · [ANT-2026-HFGGE6HR](https://red.anthropic.com/2026/cvd/findings/ANT-2026-HFGGE6HR.html)
Stack buffer overflow in parse\_simple\_message\_summary via unbounded sscanf %s (SIP MWI NOTIFY)

[GHSA-59q6-j4w8-8pjx](https://github.com/advisories/GHSA-59q6-j4w8-8pjx)
oisf/suricata · use-after-free · high · [ANT-2026-WCSVRYAX](https://red.anthropic.com/2026/cvd/findings/ANT-2026-WCSVRYAX.html)
heap-use-after-free in suricata

[GHSA-5jqq-xpcr-q3r7](https://github.com/advisories/GHSA-5jqq-xpcr-q3r7)
wolfssl/wolfssl · heap-buffer-overflow · low · [ANT-2026-6615Y595](https://red.anthropic.com/2026/cvd/findings/ANT-2026-6615Y595.html)
Final Assessment: 2-Byte Heap Overflow in wolfSSL\_X509\_notAfter / wolfSSL\_X509\_notBefore

[GHSA-65xm-pfx9-g5p3](https://github.com/advisories/GHSA-65xm-pfx9-g5p3)
wolfssl/wolfssl · heap-buffer-overflow · medium · [ANT-2026-0JRYQPCF](https://red.anthropic.com/2026/cvd/findings/ANT-2026-0JRYQPCF.html)
wolfssl ech heap buffer overflow via publicname sni pol

[GHSA-6gff-7f37-2v35](https://github.com/advisories/GHSA-6gff-7f37-2v35)
cisco-talos/clamav · integer-overflow · high · [ANT-2026-8DRZW7VM](https://red.anthropic.com/2026/cvd/findings/ANT-2026-8DRZW7VM.html)
Integer overflow in 7z SubStreams count leading to heap buffer overflow

[GHSA-776c-mpj7-jm3r](https://github.com/advisories/GHSA-776c-mpj7-jm3r)
firecracker-microvm/firecracker · oob-read · high · [ANT-2026-PQ3CNCCK](https://red.anthropic.com/2026/cvd/findings/ANT-2026-PQ3CNCCK.html)
Virtio-PCI queue size writable after activation enables host OOB

[GHSA-78pv-qq8x-94px](https://github.com/advisories/GHSA-78pv-qq8x-94px)
gpg/libgcrypt · stack-buffer-overflow · medium · [ANT-2026-GSPVGEYA](https://red.anthropic.com/2026/cvd/findings/ANT-2026-GSPVGEYA.html)
ML-DSA context string stack buffer overflow

[GHSA-7p85-w9px-jpjp](https://github.com/advisories/GHSA-7p85-w9px-jpjp)
twigphp/twig · code-injection · critical · [ANT-2026-J3EVXWDY](https://red.anthropic.com/2026/cvd/findings/ANT-2026-J3EVXWDY.html)
PHP code injection via single quote in {% use %} template name

[GHSA-86w7-h9x4-hpxv](https://github.com/advisories/GHSA-86w7-h9x4-hpxv)
cisco-talos/clamav · integer-underflow · high · [ANT-2026-Z477W54M](https://red.anthropic.com/2026/cvd/findings/ANT-2026-Z477W54M.html)
Unsigned integer underflow in FSG unpacker section loop

[GHSA-9f49-8x56-jmjc](https://github.com/advisories/GHSA-9f49-8x56-jmjc)
cesnet/libyang · use-after-free · medium · [ANT-2026-TZQ1KH7E](https://red.anthropic.com/2026/cvd/findings/ANT-2026-TZQ1KH7E.html)
Heap use-after-free write in metadata list management during XML data parsing due to incorrect list head pointer update

[GHSA-c2q7-642g-3vwr](https://github.com/advisories/GHSA-c2q7-642g-3vwr)
nss · heap-buffer-overflow · high · [ANT-2026-1ZNMP148](https://red.anthropic.com/2026/cvd/findings/ANT-2026-1ZNMP148.html)
Off-by-one heap buffer overflow in TLS extension negotiation due to SSL\_MAX\_EXTENSIONS (22) being too small for 23 extensions

[GHSA-cc7p-2j3x-x7xf](https://github.com/advisories/GHSA-cc7p-2j3x-x7xf)
craftcms/cms · privilege-escalation · high · [ANT-2026-ZQ8AY22X](https://red.anthropic.com/2026/cvd/findings/ANT-2026-ZQ8AY22X.html)
Privilege Escalation/Bypass through UsersController->actionImpersonateWithToken()

[GHSA-chgx-jx3p-rf73](https://github.com/advisories/GHSA-chgx-jx3p-rf73)
mastodon/mastodon · signature-bypass · high · [ANT-2026-P2DWB2SK](https://red.anthropic.com/2026/cvd/findings/ANT-2026-P2DWB2SK.html)
LD-Signature bypass via JSON-LD named-graph restructuring

[GHSA-crr4-7rm4-8gpw](https://github.com/advisories/GHSA-crr4-7rm4-8gpw)
mastodon/mastodon · ssrf · high · [ANT-2026-6DSMTXZ8](https://red.anthropic.com/2026/cvd/findings/ANT-2026-6DSMTXZ8.html)
SSRF Bypass via IPv6 Unspecified Address (`::`) in Mastodon

[GHSA-f26g-jm89-4g65](https://github.com/advisories/GHSA-f26g-jm89-4g65)
gitoxidelabs/gitoxide · rce · high · [ANT-2026-6SNS6KMP](https://red.anthropic.com/2026/cvd/findings/ANT-2026-6SNS6KMP.html)
RCE when updating a Git submodule of a malicious repository

[GHSA-f684-cpcq-j565](https://github.com/advisories/GHSA-f684-cpcq-j565)
openssl/openssl · use-after-free · critical · [ANT-2026-AYWQW7P2](https://red.anthropic.com/2026/cvd/findings/ANT-2026-AYWQW7P2.html)
PKCS7\_verify frees caller-owned `indata` BIO when `digestAlgorithms` SET is empty

[GHSA-grqc-3vmg-p68x](https://github.com/advisories/GHSA-grqc-3vmg-p68x)
wolfssl/wolfssl · integer-overflow · high · [ANT-2026-ZZY4987K](https://red.anthropic.com/2026/cvd/findings/ANT-2026-ZZY4987K.html)
cmac 32 bit totalsz wraparound prefix substitution forg

[GHSA-hg75-4cmp-f367](https://github.com/advisories/GHSA-hg75-4cmp-f367)
wolfssl/wolfssl · improper-cert-validation · high · [ANT-2026-K8YY7WWS](https://red.anthropic.com/2026/cvd/findings/ANT-2026-K8YY7WWS.html)
wolfssl x509 verify cert leaf signature verification by

[GHSA-hr66-rv65-f5r4](https://github.com/advisories/GHSA-hr66-rv65-f5r4)
joomla/joomla-cms · path-traversal · medium · [ANT-2026-GSV3GS1G](https://red.anthropic.com/2026/cvd/findings/ANT-2026-GSV3GS1G.html)
Path Traversal via Glob Injection in com\_media Search

[GHSA-hwfh-mh4f-m67f](https://github.com/advisories/GHSA-hwfh-mh4f-m67f)
postgres/postgres · denial-of-service · high · [ANT-2026-CJQWKW82](https://red.anthropic.com/2026/cvd/findings/ANT-2026-CJQWKW82.html)
Pre-auth unbounded recursion in ProcessStartupPacket: alternating SSL/GSS negotiation requests cause infinite recursion when both are rejected. ssl\_done/gss\_done flags oscillate (true,false)->(false,true) endlessly. No check\_stack\_depth. Pre-authentication.

[GHSA-j273-m5qq-6825](https://github.com/advisories/GHSA-j273-m5qq-6825)
junrar · path-traversal · medium · [ANT-2026-9VJ9JJXQ](https://red.anthropic.com/2026/cvd/findings/ANT-2026-9VJ9JJXQ.html)
Arbitrary file write due to backslash path traversal

[GHSA-jmwm-wc68-mhwm](https://github.com/advisories/GHSA-jmwm-wc68-mhwm)
libvips/libvips · oob-write · low · [ANT-2026-JBKARRJ7](https://red.anthropic.com/2026/cvd/findings/ANT-2026-JBKARRJ7.html)
Out-of-bounds IFD array access in EXIF metadata processing leading to write through corrupted pointer

[GHSA-m62j-63mf-xr95](https://github.com/advisories/GHSA-m62j-63mf-xr95)
dnsmasq · heap-buffer-overflow · high · [ANT-2026-PCBAKVPB](https://red.anthropic.com/2026/cvd/findings/ANT-2026-PCBAKVPB.html)
Heap overflow in privileged helper via oversized DHCPv6 client identifier

[GHSA-m77r-vqw2-hffx](https://github.com/advisories/GHSA-m77r-vqw2-hffx)
wolfssl/wolfssl · crypto-failure · high · [ANT-2026-P23DVQM2](https://red.anthropic.com/2026/cvd/findings/ANT-2026-P23DVQM2.html)
cms authenvelopeddata aead forgery via gcm tag truncati

[GHSA-mm6w-gr99-p3jj](https://github.com/advisories/GHSA-mm6w-gr99-p3jj)
twigphp/twig · auth-bypass · high · [ANT-2026-203E7E95](https://red.anthropic.com/2026/cvd/findings/ANT-2026-203E7E95.html)
Sandbox bypass via object-destructuring assignment

[GHSA-mpxh-8fq3-x8mh](https://github.com/advisories/GHSA-mpxh-8fq3-x8mh)
freerdp/freerdp · heap-buffer-overflow · critical · [ANT-2026-H97FY6C8](https://red.anthropic.com/2026/cvd/findings/ANT-2026-H97FY6C8.html)
Heap-buffer-overflow in cliprdr\_main.c:547 freerdp/freerdp · heap-buffer-overflow · critical · [ANT-2026-HN9XZXJ9](https://red.anthropic.com/2026/cvd/findings/ANT-2026-HN9XZXJ9.html)
heap-buffer-overflow write (attacker-controlled offset, partially-controlled data via rle delta values; up to ~15kb overwrite past ptempdata with these parameters, further with larger nxdst) in planar.c:472 freerdp/freerdp · heap-buffer-overflow · critical · [ANT-2026-RXYVE4DZ](https://red.anthropic.com/2026/cvd/findings/ANT-2026-RXYVE4DZ.html)
Heap-buffer-overflow in sanitizer\_common\_interceptors.inc:827

[GHSA-mvpx-xj7r-3p3r](https://github.com/advisories/GHSA-mvpx-xj7r-3p3r)
freerdp/freerdp · heap-buffer-overflow · critical · [ANT-2026-H97FY6C8](https://red.anthropic.com/2026/cvd/findings/ANT-2026-H97FY6C8.html)
Heap-buffer-overflow in cliprdr\_main.c:547 freerdp/freerdp · heap-buffer-overflow · critical · [ANT-2026-HN9XZXJ9](https://red.anthropic.com/2026/cvd/findings/ANT-2026-HN9XZXJ9.html)
heap-buffer-overflow write (attacker-controlled offset, partially-controlled data via rle delta values; up to ~15kb overwrite past ptempdata with these parameters, further with larger nxdst) in planar.c:472 freerdp/freerdp · heap-buffer-overflow · critical · [ANT-2026-RXYVE4DZ](https://red.anthropic.com/2026/cvd/findings/ANT-2026-RXYVE4DZ.html)
Heap-buffer-overflow in sanitizer\_common\_interceptors.inc:827

[GHSA-mx4j-fjqx-f8qj](https://github.com/advisories/GHSA-mx4j-fjqx-f8qj)
wolfssl/wolfssl · heap-buffer-overflow · medium · [ANT-2026-VV0PRKKV](https://red.anthropic.com/2026/cvd/findings/ANT-2026-VV0PRKKV.html)
wolfSSL: heap buffer overflow in CertFromX509() from AuthorityKeyIdentifier size mismatch

[GHSA-p5j5-4j3q-8mq8](https://github.com/advisories/GHSA-p5j5-4j3q-8mq8)
typo3 · xss · medium · [ANT-2026-MHJX7J31](https://red.anthropic.com/2026/cvd/findings/ANT-2026-MHJX7J31.html)
Stored XSS in TYPO3 HTML Sanitizer via `xmlns` Namespace URI Injection

[GHSA-p6r2-4hgm-m6ff](https://github.com/advisories/GHSA-p6r2-4hgm-m6ff)
freerdp/freerdp · heap-buffer-overflow · critical · [ANT-2026-H97FY6C8](https://red.anthropic.com/2026/cvd/findings/ANT-2026-H97FY6C8.html)
Heap-buffer-overflow in cliprdr\_main.c:547 freerdp/freerdp · heap-buffer-overflow · critical · [ANT-2026-HN9XZXJ9](https://red.anthropic.com/2026/cvd/findings/ANT-2026-HN9XZXJ9.html)
heap-buffer-overflow write (attacker-controlled offset, partially-controlled data via rle delta values; up to ~15kb overwrite past ptempdata with these parameters, further with larger nxdst) in planar.c:472 freerdp/freerdp · heap-buffer-overflow · critical · [ANT-2026-RXYVE4DZ](https://red.anthropic.com/2026/cvd/findings/ANT-2026-RXYVE4DZ.html)
Heap-buffer-overflow in sanitizer\_common\_interceptors.inc:827

[GHSA-pjjp-65r7-ppgm](https://github.com/advisories/GHSA-pjjp-65r7-ppgm)
libass/libass · heap-buffer-overflow · high · [ANT-2026-9WB9SMM6](https://red.anthropic.com/2026/cvd/findings/ANT-2026-9WB9SMM6.html)
heap-buffer-overflow in libass

[GHSA-q349-x427-xg3w](https://github.com/advisories/GHSA-q349-x427-xg3w)
wolfssl/wolfssl · heap-buffer-overflow · low · [ANT-2026-87DJGDRB](https://red.anthropic.com/2026/cvd/findings/ANT-2026-87DJGDRB.html)
Heap-buffer-overflow in sha.c:733

[GHSA-q3h9-m34w-h76f](https://github.com/advisories/GHSA-q3h9-m34w-h76f)
jqlang/jq · heap-buffer-overflow · medium · [ANT-2026-EBDTPNVH](https://red.anthropic.com/2026/cvd/findings/ANT-2026-EBDTPNVH.html)
Integer overflow in string concatenation leading to 1 GB memcpy heap buffer overflow

[GHSA-qmc9-vqq2-8mv3](https://github.com/advisories/GHSA-qmc9-vqq2-8mv3)
oisf/suricata · use-after-free · high · [ANT-2026-61Y3NTY3](https://red.anthropic.com/2026/cvd/findings/ANT-2026-61Y3NTY3.html)
Use-after-free in mod.rs:547

[GHSA-qpmf-9p9c-455w](https://github.com/advisories/GHSA-qpmf-9p9c-455w)
util-linux/util-linux · use-after-free · medium · [ANT-2026-ZRDQDR79](https://red.anthropic.com/2026/cvd/findings/ANT-2026-ZRDQDR79.html)
heap-use-after-free in util-linux

[GHSA-rh79-75qm-gwjr](https://github.com/advisories/GHSA-rh79-75qm-gwjr)
go-gitea/gitea · idor · medium · [ANT-2026-VN61PHA0](https://red.anthropic.com/2026/cvd/findings/ANT-2026-VN61PHA0.html)
Gitea LFS Deploy-Key Privilege Escalation — Cross-Repository Data Exfiltration

[GHSA-rjvx-x4g3-vr6w](https://github.com/advisories/GHSA-rjvx-x4g3-vr6w)
cisco-talos/clamav · integer-overflow · high · [ANT-2026-VVPEMVDE](https://red.anthropic.com/2026/cvd/findings/ANT-2026-VVPEMVDE.html)
Integer overflow in PE rebuild section size summation in Aspack unpacker

[GHSA-v782-6fq4-q827](https://github.com/advisories/GHSA-v782-6fq4-q827)
randombit/botan · improper-cert-validation · high · [ANT-2026-2FETJP49](https://red.anthropic.com/2026/cvd/findings/ANT-2026-2FETJP49.html)
[security] certificate\_known(): Complete x509 bypass

[GHSA-v7jp-vmx6-5429](https://github.com/advisories/GHSA-v7jp-vmx6-5429)
cesnet/libyang · use-after-free · medium · [ANT-2026-TZQ1KH7E](https://red.anthropic.com/2026/cvd/findings/ANT-2026-TZQ1KH7E.html)
Heap use-after-free write in metadata list management during XML data parsing due to incorrect list head pointer update

[GHSA-v8h9-9g8j-w7h4](https://github.com/advisories/GHSA-v8h9-9g8j-w7h4)
joomla/joomla-cms · path-traversal · high · [ANT-2026-HHD77M82](https://red.anthropic.com/2026/cvd/findings/ANT-2026-HHD77M82.html)
Path Traversal in `layout` Parameter Leads to Arbitrary PHP File Inclusion (LFI → RCE)

[GHSA-vgv9-mv66-mpc7](https://github.com/advisories/GHSA-vgv9-mv66-mpc7)
wolfssl/wolfssl · crypto-failure · medium · [ANT-2026-SB4PHA43](https://red.anthropic.com/2026/cvd/findings/ANT-2026-SB4PHA43.html)
ARIA-GCM Nonce Reuse in TLS 1.2 Record Encryption in wolfSSL

[GHSA-w52v-v783-gw97](https://github.com/advisories/GHSA-w52v-v783-gw97)
tryghost/ghost · sql-injection · critical · [ANT-2026-69D8H6RP](https://red.anthropic.com/2026/cvd/findings/ANT-2026-69D8H6RP.html)
Critical Vulnerability (CVSS 9.1) : SQLi from unauthenticated user; arbitrary DB reads

[GHSA-wc3v-3457-c8cm](https://github.com/advisories/GHSA-wc3v-3457-c8cm)
openmeterio/openmeter · sql-injection · medium · [ANT-2026-KC1Y51NF](https://red.anthropic.com/2026/cvd/findings/ANT-2026-KC1Y51NF.html)
SQL injection in ClickHouse JSONPath validation

[GHSA-wfx7-g85r-q6vw](https://github.com/advisories/GHSA-wfx7-g85r-q6vw)
libgit2/libgit2 · heap-buffer-overflow · medium · [ANT-2026-RVPC18B1](https://red.anthropic.com/2026/cvd/findings/ANT-2026-RVPC18B1.html)
Heap buffer overflow in bundled PCRE regex compilation via pre-compile/compile phase mismatch in atomic wrapping

[GHSA-wj3p-xhqm-pffc](https://github.com/advisories/GHSA-wj3p-xhqm-pffc)
bytecodealliance/wasm-micro-runtime · heap-buffer-overflow · critical · [ANT-2026-P7DSVPH6](https://red.anthropic.com/2026/cvd/findings/ANT-2026-P7DSVPH6.html)
Heap-buffer-overflow in posix.c:2253

[GHSA-x9h5-r9v2-vcww](https://github.com/advisories/GHSA-x9h5-r9v2-vcww)
imagemagick/imagemagick · heap-buffer-overflow · high · [ANT-2026-T44WA684](https://red.anthropic.com/2026/cvd/findings/ANT-2026-T44WA684.html)
Heap buffer overflow in MVG pattern rendering via CopyMagickString without bounds check

[GHSA-xjvp-4fhw-gc47](https://github.com/advisories/GHSA-xjvp-4fhw-gc47)
opencontainers/runc · symlink-following · medium · [ANT-2026-N6TD9MF6](https://red.anthropic.com/2026/cvd/findings/ANT-2026-N6TD9MF6.html)
Host filesystem write via /dev symlink in container image

No published records fall inside the default discovery window.

‹  ›

SEVERITY AGREEMENT [Showing all assessment sources and severities for findings discovered between November 1, 2025 and August 26, 2026.](#filters "Showing all assessment sources and severities for findings discovered between November 1, 2025 and August 26, 2026.")

This graph compares Claude's initial severity assessments against the external security research firms' assessments, for those findings that have completed triage. Cells on the diagonal indicate agreement. The number assessed here represents the subset of vulnerabilities included on our disclosure ledger that were reviewed by our security partners, rather than disclosed by us directly.

Claude-assessed (rows) against external security research firm-assessed (columns), n = 1017.
85.2% exact agreement, 97.1% within one band.

Anthropic's severity assessments are produced before any maintainer input. Project maintainers often apply project-specific severity rules that Claude does not have access to at run time, so what one maintainer rates as critical another may rate as low. The external security research firms incorporate that context, which is why their assessments tend to be lower.

This snapshot was generated on 2026-08-26 11:55 PT. The manifest hash below is the SHA-3-512 hash of the structured payload and is republished with every dated snapshot so any figure on this page can be verified against the [machine-readable record](https://red.anthropic.com/2026/cvd/data/payload.json).

Revision 32 · checksum f89b26dc49393d86613a9687a7b6e152d60e1b8de4066640707ded608fd51f5bd354b29ac790490fc0fc6ee3b01dcf7ae11617318a95129c9cbc0ae353b6d281

---

## Subscribe
