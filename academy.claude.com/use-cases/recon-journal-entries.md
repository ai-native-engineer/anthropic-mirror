<!-- source: https://academy.claude.com/use-cases/recon-journal-entries -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Reconcile and draft the journal entries

Intercompany breaks sorted, JEs drafted with memo and support.

10 minFinanceClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-nhxr907i.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-ci4exa6p.png)

## Set up

### Try a plugin

The Finance plugin ships with `/journal-entry` and seven other close-week skills as a starting point, it already knows how to match across ledgers and structure a JE. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

FinanceStreamline finance and accounting workflows, from journal entries and reconciliation to financial statements and variance analysis. Speed up audit prep, month-end close, and keeping your books clean.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=finance)

`/journal-entry`Prepare journal entries with proper debits, credits, and supporting documentation for month-end close.

[Run](claude://cowork/new?q=%2Fjournal-entry)

`/variance-analysis`Decompose financial variances into drivers with narrative explanations and waterfall analysis.

[Run](claude://cowork/new?q=%2Fvariance-analysis)

Show all 7 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

NetSuite

Pull GL detail and intercompany subledgers directly from the system of record.

[Connect](https://claude.ai/desktop/directory/netsuite)

![](images/3cb5db332ced9f49.svg)

Microsoft 365

Build the recon workbook in Excel with working formulas, tie-outs, and a JE upload tab.

[Connect](https://claude.ai/desktop/directory/microsoft-365)

![](images/a3bfc5814bd6a3e2.svg)

Google DriveOptional

Read the FX rate sheet and prior-period recon from the shared close folder.

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (both entity exports, the FX rate sheet, your JE template, last month's recon) into one folder and point Cowork at it. Cowork reads from it and writes the matched workbook and JE draft back to it. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from your intercompany folder so the FX policy, materiality threshold, and JE template stay attached every close.

FY26-Close / Intercompany / March

subledger-US-mar.xlsxApr 2, 2026312 KB

subledger-EMEA-mar.xlsxApr 2, 2026288 KB

fx-rates-mar-2026.xlsxMar 31, 20269 KB

JE-template.xlsxJan 8, 202614 KB

In Cowork’s chat bar:FY26-Close / Intercompany / March

## The prompt

### Copy this into Claude Cowork

Reconcile the March intercompany balances across both subledgers. Normalize FX to USD at the month-end rate, fuzzy-match by amount and reference, and sort the differences into timing, rounding, and true breaks. For every true break, draft the journal entry with Dr/Cr, memo, and support reference, and write the recon workbook to this folder.

FY26-Close / Intercompany / MarchOpen in Cowork

### Why this works

Prompt

**Give it your own categories.** "Timing, rounding, true breaks" is your classification, stated once, so the workbook comes back already sorted your way.

Prompt

**Specify the matching method.** References never line up perfectly across entities; asking for fuzzy match catches the near-misses a VLOOKUP drops.

Prompt

**Name every part of the output.** Dr/Cr, memo, and support reference means the output is one review away from posting.

Source

**Supply the reference data yourself.** Cowork reads the month-end rate from the file you trust, not a number it looked up.

### Get a better draft

Practice

**Add last month's recon.** Drop the prior workbook in the folder and Cowork matches your tab structure, column names, and tie-out cells.

Practice

**Set the rounding threshold.** Add "treat anything under $25 as rounding" so you're not clearing pennies by hand.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /journal-entry skill with my feedback.

FY26-Close / IntercompanyOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it on a schedule

Intercompany is due the same day every close. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill runs against the newest exports automatically.

**/schedule** Every Monday at 9am, if new subledger exports are in FY26-Close/Intercompany, run /journal-entry against them and write the recon workbook and JE draft to that folder.

FY26-Close / IntercompanyOpen in Cowork

Scheduled taskActive

Intercompany recon and JE draft

Runs `/journal-entry` against the newest subledger exports, sorts breaks, and writes the JE draft to the close folder.

Every **Monday at 9:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/journal-entry` now carries your match logic, your FX policy, and your JE template. Share it so every entity controller runs the same recon, same buckets, same memo format.

Share the skill

In Cowork, open **Skills** → `/journal-entry` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your instructions baked in, they don't repeat Steps 1-3.

## What changes for close week

Intercompany reconciles across both ledgers with each difference classified and its journal entry drafted — ready to review and post instead of match line by line.

You did this for intercompany. The same approach covers bank reconciliations, accrual entries, and prepaid schedules — each one a skill your team runs the same way every close.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/excel-icon.svg)

Claude in Excel

Review the breaks and reconcile in the workbook

Install](https://claude.com/claude-for-excel)

[Next: Explain a variance](https://academy.claude.com/use-cases/explain-a-variance)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for close week](#what-changes-for-close-week)
