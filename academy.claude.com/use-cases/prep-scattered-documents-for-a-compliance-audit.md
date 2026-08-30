<!-- source: https://academy.claude.com/use-cases/prep-scattered-documents-for-a-compliance-audit -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Prep scattered documents for a compliance audit

Turn a folder of scattered policy documents, contracts, and records into an organized, clearly named collection ready for regulatory review.

15 minLegalClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-lqm2wx2c.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-k7xxgqjb.png)

## 1. Describe the task[](#1-describe-the-task)

In Cowork, Claude processes an entire folder of audit documents at once: policies, procedures, contracts, evidence, scans. It reads each file to understand what it is, so there's no renaming or sorting beforehand.

Your prompt just needs the audit framework and scope. Claude categorizes everything, renames files to match, and flags gaps in your documentation while you move on to something else.

I have 100+ documents for our upcoming SOC 2 audit in this folder. Right now they're scattered with names like "policy\_v2\_final.docx" and "scan0042.pdf". I need to organize them before the auditors arrive:

* Rename files with clear titles showing document type, effective date, and which control area they cover
* Group by control category (Access Control, Change Management, Incident Response, etc.)
* Flag any control areas where we seem to have gaps in documentation

Our audit scope covers security, availability, and confidentiality. The audit period is January through December 2024.

Open in Cowork

## 2. Give Claude context[](#2-give-claude-context)

In [Claude Desktop(opens in new tab)](https://claude.com/download), [Cowork(opens in new tab)](https://academy.claude.com/tutorials/choosing-between-claude-cowork-or-chat) is a workspace that works directly with your local files. Point it at your audit folder and it reads everything inside, including PDFs, Word docs, spreadsheets, and scans.

**What to expect:** After your initial prompt in Cowork, Claude may ask you questions about your audit scope and requirements, then build a plan you can review in the sidebar. This helps it work more independently and produce results closer to finished.

### Required context[](#required-context)

To get started:

* Download [Claude Desktop(opens in new tab)](https://claude.com/download) and start a Cowork session
* Select ***Work in a folder*** in the chat bar and choose the folder containing your audit documents, or use the ***+*** button to add individual files
* Include your audit scope or control framework so Cowork can categorize documents against it

## 3. What Claude creates[](#3-what-claude-creates)

Cowork reviews the entire document folder, produces a rename mapping organized by control area, identifies coverage, and flags potential gaps.

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

## 4. Follow up prompts[](#4-follow-up-prompts)

Continue the conversation with Claude to refine, expand, or explore further.

### Create the control matrix as a spreadsheet[](#create-the-control-matrix-as-a-spreadsheet)

Cowork writes files directly to your folder. Instead of copying output from chat, have it create the matrix as an Excel file you can share with auditors.

*"Create a spreadsheet in this folder mapping each SOC 2 control to the documents that support it. Include columns for control ID, description, evidence documents, and coverage status."*

Open in Cowork

### Pull evidence from your ticketing system[](#pull-evidence-from-your-ticketing-system)

Use Claude in Chrome for web-based tools. If your change management or incident response evidence lives in Jira, ServiceNow, or another web tool, Cowork can read it directly from the browser.

*"I have Jira open with our change management tickets. Pull the last 6 months of change requests and create a summary document showing we follow our change management procedure."*

Open in Cowork

### Generate policy summaries for the walkthrough[](#generate-policy-summaries-for-the-walkthrough)

Create a reference doc for your audit conversations. Cowork reads each policy and writes a cheat sheet you can use when auditors ask questions.

*"Read our policies folder and create a one-page reference doc. For each policy: what it covers, last updated date, and the 2-3 key requirements I should be able to explain."*

Open in Cowork

## 5. Tricks, tips, and troubleshooting[](#5-tricks-tips-and-troubleshooting)

### For sensitive policies, contracts, and evidence files, run your session locally[](#for-sensitive-policies-contracts-and-evidence-files-run-your-session-locally)

Those documents stay stored in your own folders and Claude's work on them runs on your machine — what Claude reads is processed by Anthropic's servers to generate responses, as in any Claude conversation.

### Point Cowork at the mess, not just the polished files[](#point-cowork-at-the-mess-not-just-the-polished-files)

If you have a "to be organized" folder with random scans and downloads, that's exactly where to start. Cowork can make sense of poorly named files from their content.

### Use your existing framework as a guide[](#use-your-existing-framework-as-a-guide)

If you have a control matrix, audit checklist, or framework mapping, include it in the folder. Cowork uses it to categorize documents more accurately.

## 6. Ready to try for yourself?[](#6-ready-to-try-for-yourself)

Give Cowork folder access and get organized documentation, identified gaps, and a clear picture of your audit readiness.

I have 100+ documents for our upcoming SOC 2 audit in this folder. Right now they're scattered with names like "policy\_v2\_final.docx" and "scan0042.pdf". I need to organize them before the auditors arrive:

• Rename files with clear titles showing document type, effective date, and which control area they cover
• Group by control category (Access Control, Change Management, Incident Response, etc.)
• Flag any control areas where we seem to have gaps in documentation

Our audit scope covers security, availability, and confidentiality. The audit period is January through December 2024.

Try in Cowork

* [1. Describe the task](#1-describe-the-task)
* [2. Give Claude context](#2-give-claude-context)
* [3. What Claude creates](#3-what-claude-creates)
* [4. Follow up prompts](#4-follow-up-prompts)
* [5. Tricks, tips, and troubleshooting](#5-tricks-tips-and-troubleshooting)
* [6. Ready to try for yourself?](#6-ready-to-try-for-yourself)
