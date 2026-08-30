<!-- source: https://academy.claude.com/use-cases/oncall-handoff-brief -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# On-call handoff brief

Everything that happened on your shift, written before you log off.

10 minEngineeringClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-ggtsvh5v.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-ckm3olk1.png)

## Set up[](#set-up)

### Try a plugin[](#try-a-plugin)

The Engineering plugin ships with `/standup` and other incident-and-ops skills as a starting point, already structured to summarize a shift from the alert stream. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

EngineeringStreamline engineering workflows — standups, code review, architecture decisions, incident response, and technical documentation. Works with your existing tools or standalone.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=engineering)

`/standup`Generate a standup update from recent activity.

[Run](claude://cowork/new?q=%2Fstandup)

`/incident-response`Run an incident response workflow — triage, communicate, and write postmortem.

[Run](claude://cowork/new?q=%2Fincident-response)

Show all 10 skills

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/f1af6a4ad6ba0248.svg)

PagerDuty

Pull every page from your shift with ack time, resolution, and the alert that fired.

[Connect](https://claude.ai/desktop/directory/pagerduty)

![](images/b6bf6491858dcff4.svg)

Slack

Read the incident channels and #support-escalations for what CS raised during the week.

[Connect](https://claude.ai/desktop/directory/slack)

![](images/92b68e492ad6094d.svg)

GitHubOptional

List every production deploy that shipped during your shift, with the change summary.

[Connect](https://claude.ai/desktop/directory/github)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

Drag the files you'll use (your handoff template, last week's brief, the runbook index) into one folder and point Cowork at it. Cowork reads the template from there and writes the brief and the watch-list back to it. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from your on-call folder so the template, channel list, and severity definitions stay attached every rotation.

Platform / Oncall / 2026-W17

handoff-template.mdJan 12, 20262 KB

handoff-2026-W16.mdApr 20, 20266 KB

runbook-index.mdMar 30, 202611 KB

In Cowork’s chat bar:Platform / Oncall / 2026-W17

## The prompt[](#the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Write the on-call handoff for my shift. Cover pages and incident channels from the last 7 days, CS escalations from #support-escalations, and production deploys. For each, note status (resolved, monitoring, still open), the one-line cause if known, and what the next on-call should watch. Write it to the on-call folder and post it to #oncall.

Platform / Oncall / 2026-W17Open in Cowork

### Why this works[](#why-this-works)

Prompt

**Name every source you need.** Pages, CS escalations, and deploys are the three things that wake the next person up; naming all three means nothing falls between systems.

Prompt

**Specify the fields for each item.** That triplet is exactly what the next shift needs to triage at 2am; the brief comes back already shaped that way.

Prompt

**Say where the output should go.** The doc is saved to the folder for the record and in #oncall so the next engineer actually sees it.

Source

**Include the previous version for context.** Anything you marked "monitoring" last rotation carries forward instead of getting dropped.

### Get a better draft[](#get-a-better-draft)

Practice

**Ask for the noisy alerts.** Add "list any alert that fired more than 3 times so we can tune it" and the handoff doubles as the alert-hygiene backlog.

Practice

**Ask it to link runbooks.** Add "for anything still open, link the relevant runbook" so the next on-call has the fix one click away.

## Make Cowork work for you[](#make-cowork-work-for-you)

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /standup skill with my feedback.

Platform / OncallOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable[](#make-it-repeatable)

### Run it at rotation change[](#run-it-at-rotation-change)

Handoff happens the same hour every week. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill writes the brief at the end of every rotation, whether you remembered or not.

**/schedule** Every Monday at 9am, run /standup over the prior 7 days of pages, #support-escalations, and prod deploys, write the handoff to Platform/Oncall/<week>.md, and post it to #oncall.

Platform / OncallOpen in Cowork

Scheduled taskActive

Weekly on-call handoff

Runs `/standup` over the week's pages, CS escalations, and deploys, writes the brief to the on-call folder, and posts it to #oncall.

Every **Mondays at 9:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates[](#share-with-your-teammates)

Your customized `/standup` now carries your channel list, your status labels, and your team's handoff template. Share it so every engineer in the rotation produces the same brief, and nobody starts a shift blind because the last person was too tired to write it up.

Share the skill

In Cowork, open **Skills** → `/standup` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your instructions baked in, they don't repeat Steps 1-3.

## What changes for the rotation[](#what-changes-for-the-rotation)

The handoff is written and posted with each item's status, cause, and what to watch — the next engineer starts informed instead of searching channels for context.

You did this for one rotation. The same approach covers incident postmortems, release summaries, and the weekly ops review — each one a skill in your team's plugin, run the same way every time.

[Next: Draft the incident postmortem](https://academy.claude.com/use-cases/incident-postmortem)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for the rotation](#what-changes-for-the-rotation)
