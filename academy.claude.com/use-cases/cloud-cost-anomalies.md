<!-- source: https://academy.claude.com/use-cases/cloud-cost-anomalies -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Find the cloud cost anomaly

Where the bill jumped, why, and who owns the fix.

10 minEngineeringClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-nuxe06ft.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-lz8vk1yx.png)

## Set up

### Try a plugin

The Engineering plugin ships with `/debug` already wired to read a Cost Explorer or BigQuery billing export, baseline it, and group the deltas by tag. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Engineering9 skills for postmortems, design docs, on-call handoffs, and cost reviews

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=engineering)

`/debug`Find over-trend cloud spend and trace each spike to a cause

[Run](claude://cowork/new?q=%2Fdebug)

`/documentation`Write up the cost finding as a runbook entry the team can act on

[Run](claude://cowork/new?q=%2Fdocumentation)

Show all 10 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

Snowflake

Query the cost-and-usage tables in the warehouse so the anomaly report runs against the same data Finance sees.

[Connect](https://claude.ai/desktop/directory/snowflake)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23632CA6'%20d='m20.43%2017.56-1.86-1.24-1.6%202.63-1.85-.53-1.73%202.7.07.71%208.92-1.63-.52-6.45zm-6.33-3.64c.46-.06.86-.13%201.35-.42.08-.32.1-.83-.04-1.43-.21-.87-.5-1.4-1.1-1.31-.6.1-.63.84-.42%201.71.12.5.33.98.54%201.28zm-2.54.4c.45-.08.96-.43%201.12-.64-.12-.18-.33-.54-.42-1.04-.32-.05-.6-.01-.92.19-.43.26-.77.86-.67%201.28.24.24.53.28.89.21zm-1.87.92c.18-.32.13-.86-.14-1.28-.19.02-.38.07-.57.18-.42.24-.86.77-.73%201.24.35.19.98.2%201.44-.14zm12.63%206.24-1.06-13.1L1.68.13.07%2019.05l8.6%201.24%201.55-2.42c-.85-.56-1.38-1.4-1.62-2.06-.42-1.14-.07-2.45.86-3.13.24-.18.5-.3.77-.37-.07-.43-.01-.93.24-1.37.42-.73%201.2-1.12%202-1.06.06-.58.36-1.13.9-1.46.86-.53%201.98-.33%202.63.44.35-.06.73-.02%201.12.14%201.21.5%201.6%201.88%201.39%202.96.5.36.86.86%201.02%201.45.33%201.21-.24%202.5-1.32%203.07l-1.37%202.25%201.84.53%201.58-2.6%202.44%201.63.63-.07zm-14.2-9.95c.14-.65.86-1.02%201.14-1.18-.33-.56-.5-1.28-.42-1.84.14-.93.93-1.5%201.63-1.43-.14-.5-.14-1.07.06-1.6.36-.93%201.32-1.36%202.14-1%20.03-.5.24-1%20.65-1.36.77-.7%201.93-.6%202.6.2.38-.2.84-.24%201.28-.07.86.33%201.28%201.32.93%202.2.43.2.77.6.93%201.1.3.93-.2%201.93-1.1%202.27.1.45.04.93-.2%201.35-.18.32-.43.55-.71.7.28.59.37%201.27.2%201.93l.5.35c.31-.55.85-.93%201.5-.98a8.53%208.53%200%200%201-.06-2.24c.2-1.84%201.36-2.56%202.35-2.45.43.05.77.24%201.02.5l.23-2.85L3.07%201.7%201.73%2017.56l5.77.83c-.12-.5-.12-1.02.04-1.5-.86-.42-1.5-1.32-1.5-2.4a2.6%202.6%200%200%201%201.28-2.24c-.24-.43-.33-.93-.2-1.43z'/%3e%3c/svg%3e)

Datadog

Correlate a cost spike with the traffic, deploy, or job that ran in the same window.

[Connect](https://claude.ai/desktop/directory/datadog)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23181717'%20d='M12%20.3a12%2012%200%200%200-3.8%2023.39c.6.11.82-.26.82-.58v-2.03c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.33-1.76-1.33-1.76-1.09-.74.08-.73.08-.73%201.2.09%201.84%201.24%201.84%201.24%201.07%201.83%202.81%201.3%203.49%201%20.11-.78.42-1.31.76-1.61-2.67-.3-5.47-1.33-5.47-5.93%200-1.31.47-2.38%201.24-3.22-.13-.3-.54-1.52.11-3.18%200%200%201.01-.32%203.3%201.23a11.5%2011.5%200%200%201%206%200c2.29-1.55%203.3-1.23%203.3-1.23.65%201.66.24%202.88.12%203.18.77.84%201.23%201.91%201.23%203.22%200%204.61-2.8%205.63-5.48%205.92.43.37.81%201.1.81%202.22v3.29c0%20.32.22.7.82.58A12%2012%200%200%200%2012%20.3'/%3e%3c/svg%3e)

GitHubOptional

Check what merged into the owning service around the date the spend changed.

[Connect](https://claude.ai/desktop/directory/github)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drop the billing CSV (or point at the export bucket), your tag-to-team mapping, and last quarter's report into one folder so Cowork has the baseline and the ownership map. The anomaly report and the per-team breakouts get written back here. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from the folder so your thresholds and known-okay exceptions persist month to month.

Infra / cloud-cost / 2026-04

aws-cur-2026-04.csvApr 28, 202622 MB

tag-team-map.csvFeb 3, 20264 KB

2026-03-anomaly-report.mdMar 31, 20269 KB

In Cowork’s chat bar:Infra / cloud-cost / 2026-04

## The prompt

### Copy this into Claude Cowork

Compare this month's AWS costs to the trailing three-month average by service and tag:team. Flag any line more than 20% over trend, trace each to the workload or change behind it, and write the cost-anomaly report with an owner and recommended action for every item. Put a one-line summary for the infra channel at the top.

Infra / cloud-cost / 2026-04Open in Cowork

### Why this works

Prompt

**Set the comparison baseline.** One month is noise; three months is a baseline.

Prompt

**Set the threshold.** "More than 20% over" turns a wall of numbers into a short list worth reading.

Prompt

**Ask for what caused each anomaly.** "Likely cause and owning team" is what makes a finding useful — so each anomaly includes where it came from and who to talk to about it.

Source

**Include who owns what.** Every anomaly has an owner, so the report is a to-do list, not an FYI.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/excel-icon.svg)

Claude in Excel

Compare savings against the budget

Install](https://claude.com/claude-for-excel)

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /debug skill with my feedback.

Infra / cloud-costOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it when the bill closes

The report should be waiting before anyone opens the console. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill runs against the new export as soon as the month closes.

**/schedule** Every Monday at 7am, if a new month's billing export is in Infra/cloud-cost, run /debug against it, write the anomaly report to that month's folder, and post the one-line summary to #infra-cost.

Infra / cloud-costOpen in Cowork

Scheduled taskActive

Monthly cloud-cost anomaly report

Runs `/debug` on the closed month, writes the ranked anomaly report to the dated folder, and posts the headline to the infra channel.

Every **Monday at 7:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/debug` now knows your tag scheme, your threshold, and the spikes you've already accepted. Share it so any infra engineer can run the same analysis mid-month when something looks off.

Share the skill

In Cowork, open **Skills** → `/debug` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your thresholds and exceptions baked in, so they don't repeat Steps 1-3.

## What changes for the bill review

Cloud spend is checked against trend with each anomaly traced to a cause, costed, and assigned an owner — ready to act on instead of investigate.

You did this for one cloud account. The same approach covers other providers, SaaS tool spend, and per-team budget checks — each one becomes a skill your team runs the same way.

[Next: Build an "Ask the Company" agent](https://academy.claude.com/use-cases/ask-the-company)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for the bill review](#what-changes-for-the-bill-review)
