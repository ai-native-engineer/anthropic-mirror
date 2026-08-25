<!-- source: https://academy.claude.com/use-cases/explain-a-variance -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Explain a variance

The variance narrative, written from the actuals.

10 minFinanceClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-ejn575jr.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-m0b89rp1.png)

## Set up

### Try a plugin

The Finance plugin ships with `/variance-analysis` and seven other close-week skills as a starting point, it already knows how to compare periods and structure commentary. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

FinanceStreamline finance and accounting workflows, from journal entries and reconciliation to financial statements and variance analysis. Speed up audit prep, month-end close, and keeping your books clean.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=finance)

`/variance-analysis`Decompose financial variances into drivers with narrative explanations and waterfall analysis.

[Run](claude://cowork/new?q=%2Fvariance-analysis)

`/financial-statements`Generate financial statements (income statement, balance sheet, cash flow) with period-over-period comparison and variance analysis.

[Run](claude://cowork/new?q=%2Ffinancial-statements)

`/close-management`Manage the month-end close process with task sequencing, dependencies, and status tracking.

[Run](claude://cowork/new?q=%2Fclose-management)

Show all 7 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

NetSuite

Pull GL detail, AP aging, and trial balances directly from the system of record.

[Connect](https://claude.ai/desktop/directory/netsuite)

![](images/a3bfc5814bd6a3e2.svg)

Google Drive

Read and write Sheets, generate Slides, and pull supporting docs from Drive.

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

![](images/3cb5db332ced9f49.svg)

Microsoft 365

Build and edit Excel models with working formulas, and draft Word memos and PowerPoint decks.

[Connect](https://claude.ai/desktop/directory/microsoft-365)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (actuals, prior period, budget, chart of accounts) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the narrative back to it. If you'll run this every close, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so instructions, memory, and scheduled runs stay attached to it.

FY26-Close / March

actuals-mar-2026.xlsxApr 2, 202684 KB

actuals-feb-2026.xlsxMar 3, 202681 KB

budget-FY26.xlsxJan 8, 202642 KB

chart-of-accounts.pdfDec 12, 2025118 KB

In Cowork’s chat bar:FY26-Close / March

## The prompt

### Copy this into Claude Cowork

Draft this month's variance commentary for the monthly review. Compare actuals to last month and to budget, and for every line that moved more than 10% or $50K explain what moved and why, in plain English for a leadership audience. Write it to the close folder.

FY26-Close / MarchOpen in Cowork

### Why this works

Prompt

**Set the threshold.** "10% or $50K" is your materiality line, so the narrative covers what matters and skips the rest.

Prompt

**Name the audience.** "For leadership" tells Claude who's reading. so the same numbers are written with less line-level detail and more interpretation than the audit version would.

Source

**Say where the output goes.** Name a specific file and Cowork edits it; otherwise it creates the draft in your working folder for you to audit.

### Get a better draft

Practice

**Add an example to match.** Drop last quarter's commentary in the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag any line where the driver isn't clear from the data" so you know exactly where to dig before the review.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /variance-analysis skill with my feedback.

FY26-CloseOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Make it a live artifact

A document is a snapshot. Ask Cowork to publish the same view as a live artifact and it becomes a link the CFO can open any time. Re-run the skill (or schedule it) and the link reflects the latest.

Publish that variance table as a live artifact for leadership.

FY26-Close / MarchOpen in Cowork

### Run it on a schedule

Variance commentary is due the same day every close. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill runs against the latest actuals automatically.

**/schedule** Every Monday at 9am, if a new actuals file is in FY26-Close, run /variance-analysis against it and write the draft to that folder.

FY26-CloseOpen in Cowork

Scheduled taskActive

Monthly variance narrative

Runs `/variance-analysis` against the latest actuals in FY26-Close and writes the draft commentary to the same folder.

Every **Monday at 9:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/variance-analysis` now carries your team's standards. Share it so everyone on the close runs the same version, same threshold, same format, same voice.

Share the skill

In Cowork, open **Skills** → `/variance-analysis` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your instructions baked in, they don't repeat Steps 1-3.

## What changes for close week

Variance commentary is drafted from your actuals with every material line explained and consistently formatted — ready to review instead of write.

You did this for variance commentary. The same approach covers account reconciliations, accruals review, and cash flow commentary — each one becomes a skill your team runs the same way.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/excel-icon.svg)

Claude in Excel

Edit the model in place

Install](https://claude.com/claude-for-excel)[![](https://academy.claude.com/surfaces/powerpoint-icon.svg)

Claude in PowerPoint

Polish the board pages

Install](https://claude.com/claude-for-powerpoint)

[Next: Forecast and scenario modeling](https://academy.claude.com/use-cases/forecast-scenarios)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for close week](#what-changes-for-close-week)
