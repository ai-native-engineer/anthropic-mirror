<!-- source: https://academy.claude.com/use-cases/forecast-scenarios -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Forecast & scenario modeling

Three scenarios with the assumptions memo.

10 minFinanceClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-d27lxpfj.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-ia2n89lp.png)

## Set up

### Try a plugin

The Finance plugin ships with `/financial-statements` and other planning skills as a starting point, already structured to roll a driver model forward and lay out scenarios. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

FinanceStreamline finance and accounting workflows, from journal entries and reconciliation to financial statements and variance analysis. Speed up audit prep, month-end close, and keeping your books clean.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=finance)

`/financial-statements`Generate financial statements (income statement, balance sheet, cash flow) with period-over-period comparison and variance analysis.

[Run](claude://cowork/new?q=%2Ffinancial-statements)

`/variance-analysis`Decompose financial variances into drivers with narrative explanations and waterfall analysis.

[Run](claude://cowork/new?q=%2Fvariance-analysis)

Show all 7 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

NetSuite

[Connect](https://claude.ai/desktop/directory/netsuite)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google Drive

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23F25022'%20d='M1%201h10.5v10.5H1z'/%3e%3cpath%20fill='%237FBA00'%20d='M12.5%201H23v10.5H12.5z'/%3e%3cpath%20fill='%2300A4EF'%20d='M1%2012.5h10.5V23H1z'/%3e%3cpath%20fill='%23FFB900'%20d='M12.5%2012.5H23V23H12.5z'/%3e%3c/svg%3e)

Microsoft 365

[Connect](https://claude.ai/desktop/directory/microsoft-365)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (the driver model, last quarter's assumptions memo, the headcount plan) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the extended model, scenario tabs, and memo back to it. If you'll re-forecast every month, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so the model, memory, and scheduled runs stay attached.

Planning / FY-forecast

driver-model-FY26.xlsxApr 3, 2026214 KB

headcount-plan.xlsxMar 28, 202646 KB

assumptions-Q1.docxJan 14, 202628 KB

In Cowork’s chat bar:Planning / FY-forecast

## The prompt

### Copy this into Claude Cowork

Pull the latest actuals into the driver model, extend it through the next four quarters, and run base, upside, and downside scenarios. For each scenario list the assumptions you changed and by how much, then write a one-page memo explaining what drives the difference between them in plain English for the leadership review.

Planning / FY-forecastOpen in Cowork

### Why this works

Prompt

**Start from the source data.** "Pull the latest actuals into the driver model" rebases the forecast on what just closed, so every scenario starts from the same true-up and the planning cycle isn't waiting on a manual roll-forward.

Prompt

**Name the scenarios.** Calling for base, upside, and downside in one run keeps the three cases on the same driver tree, so the only thing that differs is the assumptions you can defend.

Prompt

**Ask it to list its assumptions.** "List the assumptions you changed and by how much" produces the audit trail leadership asks for first; the memo explains the why, the log shows the what.

Source

**Keep source files in the working folder.** The driver model and prior memo sit in the working folder (or Sheets, if connected), so the new periods and scenario tabs write back as working formulas next to the original.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /financial-statements skill with my feedback.

Planning / FY-forecastOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it on a schedule

The re-forecast is due the same day every month. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill rebases on the latest actuals and refreshes all three scenarios automatically.

**/schedule** Every Monday at 9am, if newly closed actuals are in Planning/FY-forecast, run /financial-statements against them, write the updated model and scenarios there, and save the assumptions memo alongside.

Planning / FY-forecastOpen in Cowork

Scheduled taskActive

Monthly re-forecast

Runs `/financial-statements` against the latest closed actuals and writes the refreshed model, three scenarios, and assumptions memo to Planning/FY-forecast.

Every **Monday at 9:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/financial-statements` now carries your driver tree, your scenario sensitivities, and your memo format. Share it so every FP&A partner runs the same model the same way, and leadership sees one consistent set of scenarios no matter who owns the number.

Share the skill

In Cowork, open **Skills** → `/financial-statements` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your drivers and assumptions baked in, so they don't repeat Steps 1-3.

## Going forward

### Now in your Cowork

Your processes

Finance plugin

Your tools

NetSuite![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)Google Drive![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23F25022'%20d='M1%201h10.5v10.5H1z'/%3e%3cpath%20fill='%237FBA00'%20d='M12.5%201H23v10.5H12.5z'/%3e%3cpath%20fill='%2300A4EF'%20d='M1%2012.5h10.5V23H1z'/%3e%3cpath%20fill='%23FFB900'%20d='M12.5%2012.5H23V23H12.5z'/%3e%3c/svg%3e)Microsoft 365

Your workspace

Planning / FY-forecast

Running `/financial-statements` each period gives you a forecast that's current with closed actuals, with scenarios and their assumptions documented together — ready to review instead of rebuild.

You did this for one forecast. The same approach covers cash-flow projections, department budgets, and the long-range plan — each one becomes a skill your team runs the same way.

[Next: Explain a variance](https://academy.claude.com/use-cases/explain-a-variance)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
