<!-- source: https://academy.claude.com/use-cases/cloud-cost-anomalies -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Find the cloud cost anomaly

Where the bill jumped, why, and who owns the fix.

10 minEngineeringClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-nuxe06ft.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-lz8vk1yx.png)

## Set up[](#set-up)

### Try a plugin[](#try-a-plugin)

The Engineering plugin ships with `/debug` already wired to read a Cost Explorer or BigQuery billing export, baseline it, and group the deltas by tag. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Engineering9 skills for postmortems, design docs, on-call handoffs, and cost reviews

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=engineering)

`/debug`Find over-trend cloud spend and trace each spike to a cause

[Run](claude://cowork/new?q=%2Fdebug)

`/documentation`Write up the cost finding as a runbook entry the team can act on

[Run](claude://cowork/new?q=%2Fdocumentation)

Show all 10 skills

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](https://academy.claude.com/assets/v1/snowflake-f7euzg40.svg)

Snowflake

Query the cost-and-usage tables in the warehouse so the anomaly report runs against the same data Finance sees.

[Connect](https://claude.ai/desktop/directory/snowflake)

![](images/51045b184cff6ff6.svg)

Datadog

Correlate a cost spike with the traffic, deploy, or job that ran in the same window.

[Connect](https://claude.ai/desktop/directory/datadog)

![](images/92b68e492ad6094d.svg)

GitHubOptional

Check what merged into the owning service around the date the spend changed.

[Connect](https://claude.ai/desktop/directory/github)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

Drop the billing CSV (or point at the export bucket), your tag-to-team mapping, and last quarter's report into one folder so Cowork has the baseline and the ownership map. The anomaly report and the per-team breakouts get written back here. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from the folder so your thresholds and known-okay exceptions persist month to month.

Infra / cloud-cost / 2026-04

aws-cur-2026-04.csvApr 28, 202622 MB

tag-team-map.csvFeb 3, 20264 KB

2026-03-anomaly-report.mdMar 31, 20269 KB

In Cowork’s chat bar:Infra / cloud-cost / 2026-04

## The prompt[](#the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Compare this month's AWS costs to the trailing three-month average by service and tag:team. Flag any line more than 20% over trend, trace each to the workload or change behind it, and write the cost-anomaly report with an owner and recommended action for every item. Put a one-line summary for the infra channel at the top.

Infra / cloud-cost / 2026-04Open in Cowork

### Why this works[](#why-this-works)

Prompt

**Set the comparison baseline.** One month is noise; three months is a baseline.

Prompt

**Set the threshold.** "More than 20% over" turns a wall of numbers into a short list worth reading.

Prompt

**Ask for what caused each anomaly.** "Likely cause and owning team" is what makes a finding useful — so each anomaly includes where it came from and who to talk to about it.

Source

**Include who owns what.** Every anomaly has an owner, so the report is a to-do list, not an FYI.

### Get a better draft[](#get-a-better-draft)

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

### Finish it where the file lives[](#finish-it-where-the-file-lives)

[![](https://academy.claude.com/surfaces/excel-icon.svg)

Claude in Excel

Compare savings against the budget

Install](https://claude.com/claude-for-excel)

## Make Cowork work for you[](#make-cowork-work-for-you)

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /debug skill with my feedback.

Infra / cloud-costOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable[](#make-it-repeatable)

### Run it when the bill closes[](#run-it-when-the-bill-closes)

The report should be waiting before anyone opens the console. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill runs against the new export as soon as the month closes.

**/schedule** Every Monday at 7am, if a new month's billing export is in Infra/cloud-cost, run /debug against it, write the anomaly report to that month's folder, and post the one-line summary to #infra-cost.

Infra / cloud-costOpen in Cowork

Scheduled taskActive

Monthly cloud-cost anomaly report

Runs `/debug` on the closed month, writes the ranked anomaly report to the dated folder, and posts the headline to the infra channel.

Every **Monday at 7:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates[](#share-with-your-teammates)

Your customized `/debug` now knows your tag scheme, your threshold, and the spikes you've already accepted. Share it so any infra engineer can run the same analysis mid-month when something looks off.

Share the skill

In Cowork, open **Skills** → `/debug` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your thresholds and exceptions baked in, so they don't repeat Steps 1-3.

## What changes for the bill review[](#what-changes-for-the-bill-review)

Cloud spend is checked against trend with each anomaly traced to a cause, costed, and assigned an owner — ready to act on instead of investigate.

You did this for one cloud account. The same approach covers other providers, SaaS tool spend, and per-team budget checks — each one becomes a skill your team runs the same way.

[Next: Build an "Ask the Company" agent](https://academy.claude.com/use-cases/ask-the-company)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for the bill review](#what-changes-for-the-bill-review)
