<!-- source: https://academy.claude.com/use-cases/headcount-reconciliation -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Reconcile headcount

HRIS, the budget, and the GL agreeing on who's on the books.

10 minFinanceClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-csmvr9ol.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-egkt2awn.png)

## Set up

### Try a plugin

The Finance plugin ships with `/close-management` and seven other close-week skills as a starting point, already structured to compare records across sources and categorize the gaps. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

FinanceStreamline finance and accounting workflows, from journal entries and reconciliation to financial statements and variance analysis. Speed up audit prep, month-end close, and keeping your books clean.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=finance)

`/close-management`Manage the month-end close process with task sequencing, dependencies, and status tracking.

[Run](claude://cowork/new?q=%2Fclose-management)

`/variance-analysis`Decompose financial variances into drivers with narrative explanations and waterfall analysis.

[Run](claude://cowork/new?q=%2Fvariance-analysis)

Show all 7 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

Gusto

Pull the active roster by cost center, employment type, and start date.

[Connect](https://claude.ai/desktop/directory/gusto)

NetSuite

Read payroll postings to the GL by cost center for the period.

[Connect](https://claude.ai/desktop/directory/netsuite)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google DriveOptional

Read the approved headcount plan from the FP&A planning folder.

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (the Workday export, the headcount plan, the payroll register) into one folder and point Cowork at it. Cowork reads from it and writes the reconciliation back to it. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from your headcount folder so the cost-center map and FTE-vs-contractor rules stay attached every month.

FY26-Close / Headcount / March

workday-roster-2026-03-31.xlsxApr 1, 2026410 KB

FY26-headcount-plan-v4.xlsxFeb 11, 202688 KB

payroll-register-mar.xlsxApr 2, 2026620 KB

cost-center-map.csvJan 5, 20266 KB

In Cowork’s chat bar:FY26-Close / Headcount / March

## The prompt

### Copy this into Claude Cowork

Reconcile March headcount across the Workday roster, the FY26 plan, and payroll in the GL. Match by cost center and employee ID, list every difference (unplanned hires, budgeted heads still open, roster entries with no payroll, contractors miscoded as FTE), and write the reconciliation by cost center to the close folder.

FY26-Close / Headcount / MarchOpen in Cowork

### Why this works

Prompt

**Say how to match the records.** Naming HRIS, plan, and GL with "by cost center and employee ID" tells Cowork exactly how the three tables join.

Prompt

**List the categories you want.** Hired-not-planned, open reqs, ghost roster, miscoded contractors are the four answers your business partners need; the recon comes back already tagged.

Prompt

**Organize output for the reader.** The output rolls up the way budget owners are accountable, so it's ready to forward.

Source

**Put reference files in the folder.** Your cost-center crosswalk handles the cases where HRIS and the GL use different codes.

### Get a better draft

Practice

**Ask for cost impact.** "Show the loaded-cost impact of each break" turns a count into a number leadership reacts to.

Practice

**Ask what changed.** Add "compare to last month's recon and highlight new breaks" so you're chasing only what moved.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /close-management skill with my feedback.

FY26-Close / HeadcountOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it on a schedule

Headcount ties on the same day every close. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill runs against the newest roster and payroll automatically.

**/schedule** Every Monday at 9am, if a new Workday export is in FY26-Close/Headcount, reconcile headcount across that export, the FY26 plan, and the payroll register, and write the by-cost-center recon there.

FY26-Close / HeadcountOpen in Cowork

Scheduled taskActive

Monthly headcount reconciliation

Ties Workday roster, the FY26 plan, and the payroll register by cost center and writes the categorized break list to the close folder.

Every **Monday at 9:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized skill now carries your cost-center map, your break categories, and your loaded-cost assumptions. Share it so HR, FP&A, and Accounting all reconcile from the same definition of a head.

Share the skill

In Cowork, open **Skills** → your saved skill → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your instructions baked in, they don't repeat Steps 1-3.

## What changes for the headcount review

Headcount reconciles across systems with each difference categorized, costed, and assigned an owner — ready to resolve instead of investigate.

You did this for one period. The same approach covers payroll-to-GL, contractor counts, and the budget-vs-actual headcount view — each one becomes a skill your team runs the same way.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/excel-icon.svg)

Claude in Excel

Pivot the differences by department in place

Install](https://claude.com/claude-for-excel)

[Next: Forecast and scenario modeling](https://academy.claude.com/use-cases/forecast-scenarios)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for the headcount review](#what-changes-for-the-headcount-review)
