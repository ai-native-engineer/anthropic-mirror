<!-- source: https://academy.claude.com/use-cases/variance-exec-slides -->

Loading

## Set up

### Try a plugin

The Finance plugin ships with `/financial-statements` and seven other close-week skills as a starting point, it already knows how to read a variance table and frame it for an exec audience. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.



FinanceStreamline finance and accounting workflows, from journal entries and reconciliation to financial statements and variance analysis. Speed up audit prep, month-end close, and keeping your books clean.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=finance)

`/financial-statements`Generate financial statements (income statement, balance sheet, cash flow) with period-over-period comparison and variance analysis.

[Run](claude://cowork/new?q=%2Ffinancial-statements)

`/variance-analysis`Decompose financial variances into drivers with narrative explanations and waterfall analysis.

[Run](claude://cowork/new?q=%2Fvariance-analysis)

Show all 7 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23F25022'%20d='M1%201h10.5v10.5H1z'/%3e%3cpath%20fill='%237FBA00'%20d='M12.5%201H23v10.5H12.5z'/%3e%3cpath%20fill='%2300A4EF'%20d='M1%2012.5h10.5V23H1z'/%3e%3cpath%20fill='%23FFB900'%20d='M12.5%2012.5H23V23H12.5z'/%3e%3c/svg%3e)

Microsoft 365

Read the variance workbook and write a real .pptx with editable charts and your master layout.

[Connect](https://claude.ai/desktop/directory/microsoft-365)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google Drive

Pull last quarter's deck and the brand template from the shared FP&A folder.

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)



NetSuiteOptional

Pull the actuals straight from the GL when there's no workbook yet.

[Connect](https://claude.ai/desktop/directory/netsuite)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)



**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (the variance workbook, last quarter's deck, the list of known one-timers) into one folder and point Cowork at it. Cowork reads from it and writes the .pptx back to it. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from your board-prep folder so the materiality threshold, the slide template, and the CFO's preferred phrasing stay attached.

FY26-Close / Board-prep / March

variance-mar-2026.xlsxApr 4, 202696 KB

Q4-board-finance.pptxJan 14, 20262.1 MB

known-one-timers.mdApr 3, 20262 KB

In Cowork’s chat bar:FY26-Close / Board-prep / March

## The prompt

### Copy this into Claude Cowork

Build the three exec slides from the March variance workbook: a headline page with result vs plan, a drivers page with top movers above our materiality threshold and the known one-timers called out, and an outlook page with what carries into Q2. Match last quarter's deck layout and write the .pptx to the close folder.



FY26-Close / Board-prep / MarchOpen in Cowork

### Why this works

Prompt

**Name each part of the output.** Headline / drivers / outlook is the structure the CFO expects; saying it out loud means no fourth slide of filler.

Prompt

**Anticipate the audience's first question.** Separating non-recurring items on the drivers page is the question leadership always asks first.

Prompt

**Point to last quarter's deck as the example.** The template is the example, not a description of one.

Source

**Store recurring values in project instructions.** Materiality lives in the project instructions, so "above our threshold" means your number, every month.

### Get a better draft

Practice

**Specify the chart type.** "Use a waterfall on the drivers page" gets you the chart type that survived last board review.

Practice

**Ask for the speaker notes.** Add "put the supporting detail in the notes pane, not on the slide" so the page stays clean and the backup is one click away.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /financial-statements skill with my feedback.



FY26-Close / Board-prepOpen in Cowork



**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it on a schedule

Board prep is due the same week every quarter. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill builds the three pages from whatever variance workbook is newest.

**/schedule** Every Monday at 9am, if a new variance workbook is in FY26-Close/Board-prep, build the three exec slides from it and write the .pptx to that folder.



FY26-Close / Board-prepOpen in Cowork

Scheduled taskActive

Exec variance slides

Builds the headline / drivers / outlook .pptx from the newest variance workbook and writes it to the board-prep folder.

Every **Monday at 9:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized skill now carries your three-slide structure, your materiality line, and your CFO's preferred framing. Share it so every business unit's pages arrive looking like one deck, not five.



Share the skill

In Cowork, open **Skills** → your saved skill → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your instructions baked in, they don't repeat Steps 1-3.

## What changes for board prep

The exec slides are generated from your variance workbook in your own template, with the numbers charted and the commentary written — ready to review instead of build.

You did this for one variance period. The same approach covers the cash bridge, the forecast update, and the monthly operating review — each one becomes a skill your team runs the same way.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/powerpoint-icon.svg)

Claude in PowerPoint

Polish the three pages in place

Install](https://claude.com/claude-for-powerpoint)[![](https://academy.claude.com/surfaces/excel-icon.svg)

Claude in Excel

Edit the underlying workbook

Install](https://claude.com/claude-for-excel)

[Next: Explain a variance](https://academy.claude.com/use-cases/explain-a-variance)
