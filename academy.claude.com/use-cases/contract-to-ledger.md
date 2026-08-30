<!-- source: https://academy.claude.com/use-cases/contract-to-ledger -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Contract to ledger extraction

ASC 606 fields pulled from the contract, exceptions flagged before they hit the GL.

10 minFinanceClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-h97eje0w.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-b4zgvlm6.png)

## Set up[](#set-up)

### Try a plugin[](#try-a-plugin)

The Finance plugin ships with `/journal-entry` and seven other close-week skills as a starting point, already structured to read source documents and produce a structured accounting record. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

FinanceStreamline finance and accounting workflows, from journal entries and reconciliation to financial statements and variance analysis. Speed up audit prep, month-end close, and keeping your books clean.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=finance)

`/journal-entry`Prepare journal entries with proper debits, credits, and supporting documentation for month-end close.

[Run](claude://cowork/new?q=%2Fjournal-entry)

`/close-management`Manage the month-end close process with task sequencing, dependencies, and status tracking.

[Run](claude://cowork/new?q=%2Fclose-management)

Show all 7 skills

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

Ironclad

Read executed contracts straight from the CLM, including amendments and order forms.

[Connect](https://claude.ai/desktop/directory/ironclad)

NetSuite

Populate the rev-rec schedule and check what's already been booked for the customer.

[Connect](https://claude.ai/desktop/directory/netsuite)

![](images/764fa5af07f936df.svg)

SalesforceOptional

Cross-check deal terms against what the opportunity record says was sold.

Custom connector

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

Drag the files you'll use (the executed PDFs, your rev-rec intake template, your accounting policy memo) into one folder and point Cowork at it. Cowork reads each contract and writes the populated intake sheet and the exception list back to it. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from your rev-rec folder so the policy, the field list, and the standard-deal patterns stay attached.

Revenue / Intake / 2026-W17

Northwind-MSA-executed.pdfApr 24, 20261.1 MB

Helio-order-form-3.pdfApr 25, 2026340 KB

revrec-intake-template.xlsxJan 6, 202622 KB

asc606-policy.mdNov 4, 202518 KB

In Cowork’s chat bar:Revenue / Intake / 2026-W17

## The prompt[](#the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Extract the ASC 606 fields (performance obligations, standalone selling price, contract term, billing schedule, variable consideration) from every executed contract into the rev-rec intake sheet, and flag any that don't match a standard pattern for my review before booking.

Revenue / Intake / 2026-W17Open in Cowork

### Why this works[](#why-this-works)

Prompt

**List the exact fields you need.** Listing the exact ASC 606 inputs means the intake sheet comes back with the columns your policy uses, not generic contract metadata.

Prompt

**Ask it to flag the exceptions.** Asking for exceptions keeps the accounting judgment with you; standard deals flow, the weird ones stop at your desk.

Prompt

**Process the whole batch at once.** Cowork works the whole batch in one pass, so the intake sheet covers the week, not one PDF at a time.

Source

**Put your definitions in the folder.** "Standard pattern" means whatever your asc606-policy memo says it means.

### Get a better draft[](#get-a-better-draft)

Practice

**Ask for the clause reference.** Add "cite the section number for each extracted field" so the audit trail is one click from the value.

Practice

**Add a filled example sheet.** Drop a filled example in the folder and Cowork matches your column order, naming, and dropdown values exactly.

## Make Cowork work for you[](#make-cowork-work-for-you)

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /journal-entry skill with my feedback.

Revenue / IntakeOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable[](#make-it-repeatable)

### Run it when contracts close[](#run-it-when-contracts-close)

Signed contracts come in all week. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill watches the executed-contracts folder and processes new arrivals into intake.

**/schedule** Every weekday at 5pm, run the contract-to-ledger skill on any executed contract added to Revenue/Intake since the last run, append to the intake sheet, and post the exception list to #revenue-ops.

Revenue / IntakeOpen in Cowork

Scheduled taskActive

Contract intake to rev-rec

Daily at 5pm, extracts ASC 606 fields from any new executed contracts, appends to the intake sheet, and posts exceptions to #revenue-ops.

Every **Weekdays at 5:00pm**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates[](#share-with-your-teammates)

Your customized skill now carries your field list, your policy memo, and your definition of a standard deal. Share it so every revenue accountant runs the same extraction and the exception queue is one list, not five inboxes.

Share the skill

In Cowork, open **Skills** → your saved skill → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your instructions baked in, they don't repeat Steps 1-3.

## What changes for revenue accounting[](#what-changes-for-revenue-accounting)

Every contract's revenue-recognition fields are extracted into the intake sheet with non-standard terms flagged for review — you spend time on accounting judgment, not on reading and re-keying.

You did this for revenue recognition. The same approach covers lease abstraction, fixed-asset additions, and invoice coding — each one becomes a skill your team runs the same way.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/excel-icon.svg)

Claude in Excel

Review and adjust the intake sheet in place

Install](https://claude.com/claude-for-excel)

[Next: SOX controls documentation](https://academy.claude.com/use-cases/sox-controls-doc)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for revenue accounting](#what-changes-for-revenue-accounting)
