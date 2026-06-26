<!-- source: https://claude.com/resources/use-cases/prep-scattered-documents-for-a-compliance-audit -->

Legal

Cowork

Cowork

# Prep scattered documents for a compliance audit

Turn a folder of scattered policy documents, contracts, and records into an organized, clearly named collection ready for regulatory review.

Try in Claude

[Try in Claude](https://claude.com/download)Try in Claude

* Author

  Anthropic

  Legal
* Model

  Sonnet 4.5
* Features

  Cowork
* Share

  [Copy link](#)

  https://claude.com/resources/use-case/prep-scattered-documents-for-a-compliance-audit

1

## Describe the task

In Cowork, Claude processes an entire folder of audit documents at once: policies, procedures, contracts, evidence, scans. It reads each file to understand what it is, so there's no renaming or sorting beforehand.

Your prompt just needs the audit framework and scope. Claude categorizes everything, renames files to match, and flags gaps in your documentation while you move on to something else.

I have 100+ documents for our upcoming SOC 2 audit in this folder. Right now they're scattered with names like "policy\_v2\_final.docx" and "scan0042.pdf". I need to organize them before the auditors arrive:

* Rename files with clear titles showing document type, effective date, and which control area they cover
* Group by control category (Access Control, Change Management, Incident Response, etc.)
* Flag any control areas where we seem to have gaps in documentation

Our audit scope covers security, availability, and confidentiality. The audit period is January through December 2024.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

2

## Give Claude context

[Cowork](https://claude.com/resources/tutorials/claude-cowork-a-research-preview) is a workspace in [Claude Desktop](https://claude.com/download) that works directly with your local files. Point it at your audit folder and it reads everything inside, including PDFs, Word docs, spreadsheets, and scans.

**What to expect:** After your initial prompt in Cowork, Claude may ask you questions about your audit scope and requirements, then build a plan you can review in the sidebar. This helps it work more independently and produce results closer to finished.

## Required context

To get started:

* Download [Claude Desktop](https://claude.com/download) and start a Cowork session
* Select ***Work in a folder*** in the chat bar and choose the folder containing your audit documents, or use the ***+*** button to add individual files
* Include your audit scope or control framework so Cowork can categorize documents against it

No items found.

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

## Optional context

* Control matrix or checklist
* Naming convention preference
* [Claude in Chrome](https://claude.com/chrome) — for pulling evidence from web-based tools

No items found.

3

## What Claude creates

Cowork reviews the entire document folder, produces a rename mapping organized by control area, identifies coverage, and flags potential gaps.

From Claude

I've reviewed all 156 documents in your audit folder. Here's what I found:

#### Document Inventory

* Policies: 24 documents
* Procedures: 31 documents
* Contracts and agreements: 18 documents
* Evidence and logs: 67 documents
* Training records: 16 documents

#### Coverage by Control Area

**Well covered:** Access Control (28), Change Management (22), Vendor Management (18)

**May need attention:** Incident Response (8), Data Backup & Recovery (6)

#### Gaps Identified

* Incident Response: No evidence of testing or tabletop exercises
* Backup & Recovery: No restoration test evidence
* Business Continuity: Not in inventory

Want me to proceed with the reorganization?

4

## Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Create the control matrix as a spreadsheet

Cowork writes files directly to your folder. Instead of copying output from chat, have it create the matrix as an Excel file you can share with auditors.

*"Create a spreadsheet in this folder mapping each SOC 2 control to the documents that support it. Include columns for control ID, description, evidence documents, and coverage status."*

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Pull evidence from your ticketing system

Use Claude in Chrome for web-based tools. If your change management or incident response evidence lives in Jira, ServiceNow, or another web tool, Cowork can read it directly from the browser.

*"I have Jira open with our change management tickets. Pull the last 6 months of change requests and create a summary document showing we follow our change management procedure."*

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Generate policy summaries for the walkthrough

Create a reference doc for your audit conversations. Cowork reads each policy and writes a cheat sheet you can use when auditors ask questions.

*"Read our policies folder and create a one-page reference doc. For each policy: what it covers, last updated date, and the 2-3 key requirements I should be able to explain."*

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

5

## Tricks, tips, and troubleshooting

### Your documents stay on your machine

Cowork runs locally. Sensitive policies, contracts, and evidence files never leave your computer.

### Point Cowork at the mess, not just the polished files

If you have a "to be organized" folder with random scans and downloads, that's exactly where to start. Cowork can make sense of poorly named files from their content.

### Use your existing framework as a guide

If you have a control matrix, audit checklist, or framework mapping, include it in the folder. Cowork uses it to categorize documents more accurately.

## Ready to try for yourself?

Give Cowork folder access and get organized documentation, identified gaps, and a clear picture of your audit readiness.

Try in Claude

[Try in Claude](/download)Try in Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6984dd48d2c1f32acf967bbe_Screenshot%202026-02-05%20at%2010.02.45%E2%80%AFAM.png)

Open artifact in new window

[Open artifact in new window](#)Open artifact in new window

## Related use cases

[Organize your legal workflows using Projects](/resources/use-cases/organize-your-legal-workflows-using-projects)Organize your legal workflows using Projects

Organize your legal workflows using Projects

Use case

[Use case](/resources/use-cases/organize-your-legal-workflows-using-projects)Use case

[Track discovery timelines and analyze patterns](/resources/use-cases/track-discovery-timelines-and-analyze-patterns)Track discovery timelines and analyze patterns

Track discovery timelines and analyze patterns

Use case

[Use case](/resources/use-cases/track-discovery-timelines-and-analyze-patterns)Use case

[Contract redlining and negotiation](/resources/use-cases/contract-redlining-and-negotiation)Contract redlining and negotiation

Contract redlining and negotiation

Use case

[Use case](/resources/use-cases/contract-redlining-and-negotiation)Use case
