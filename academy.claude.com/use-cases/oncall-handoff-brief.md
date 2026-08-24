<!-- source: https://academy.claude.com/use-cases/oncall-handoff-brief -->

Loading

## Set up

### Try a plugin

The Engineering plugin ships with `/standup` and other incident-and-ops skills as a starting point, already structured to summarize a shift from the alert stream. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.



EngineeringStreamline engineering workflows — standups, code review, architecture decisions, incident response, and technical documentation. Works with your existing tools or standalone.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=engineering)

`/standup`Generate a standup update from recent activity.

[Run](claude://cowork/new?q=%2Fstandup)

`/incident-response`Run an incident response workflow — triage, communicate, and write postmortem.

[Run](claude://cowork/new?q=%2Fincident-response)

Show all 10 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%2306AC38'%20d='M4.05%2017.71h4.6V24h-4.6zM16.59.32C14.75.01%2013.45%200%2011.13%200H4.05v14.19h7.24c2.05%200%203.59-.13%204.95-.96%201.5-.9%202.71-2.77%202.71-5.55%200-2.98-1.39-5.01-2.36-5.85C15.89.93%2016.59.32%2016.59.32zm-4.66%2010.39H8.65V3.55h2.87c2.96%200%204.45%201.12%204.45%203.53%200%202.59-1.62%203.63-4.04%203.63z'/%3e%3c/svg%3e)

PagerDuty

Pull every page from your shift with ack time, resolution, and the alert that fired.

[Connect](https://claude.ai/desktop/directory/pagerduty)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.951%209.85a1.47%201.47%200%201%201-2.94%200%201.47%201.47%200%200%201%201.47-1.471h1.47V9.85Zm.735%200a1.47%201.47%200%201%201%202.94%200v3.679a1.47%201.47%200%201%201-2.94%200V9.85Z'%20fill='%23E01E5A'/%3e%3cpath%20d='M6.157%203.943a1.47%201.47%200%201%201%200-2.943%201.47%201.47%200%200%201%201.47%201.471v1.472h-1.47Zm0%20.746a1.47%201.47%200%201%201%200%202.943H2.47a1.47%201.47%200%201%201%200-2.943h3.687Z'%20fill='%2336C5F0'/%3e%3cpath%20d='M12.049%206.16a1.47%201.47%200%201%201%202.94%200%201.47%201.47%200%200%201-1.47%201.472h-1.47V6.16Zm-.736%200a1.47%201.47%200%201%201-2.94%200V2.471a1.47%201.47%200%201%201%202.94%200V6.16Z'%20fill='%232EB67D'/%3e%3cpath%20d='M9.843%2012.057a1.47%201.47%200%201%201%200%202.943%201.47%201.47%200%200%201-1.47-1.471v-1.472h1.47Zm0-.735a1.47%201.47%200%201%201%200-2.943h3.687a1.47%201.47%200%201%201%200%202.943H9.843Z'%20fill='%23ECB22E'/%3e%3c/svg%3e)

Slack

Read the incident channels and #support-escalations for what CS raised during the week.

[Connect](https://claude.ai/desktop/directory/slack)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23181717'%20d='M12%20.3a12%2012%200%200%200-3.8%2023.39c.6.11.82-.26.82-.58v-2.03c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.33-1.76-1.33-1.76-1.09-.74.08-.73.08-.73%201.2.09%201.84%201.24%201.84%201.24%201.07%201.83%202.81%201.3%203.49%201%20.11-.78.42-1.31.76-1.61-2.67-.3-5.47-1.33-5.47-5.93%200-1.31.47-2.38%201.24-3.22-.13-.3-.54-1.52.11-3.18%200%200%201.01-.32%203.3%201.23a11.5%2011.5%200%200%201%206%200c2.29-1.55%203.3-1.23%203.3-1.23.65%201.66.24%202.88.12%203.18.77.84%201.23%201.91%201.23%203.22%200%204.61-2.8%205.63-5.48%205.92.43.37.81%201.1.81%202.22v3.29c0%20.32.22.7.82.58A12%2012%200%200%200%2012%20.3'/%3e%3c/svg%3e)

GitHubOptional

List every production deploy that shipped during your shift, with the change summary.

[Connect](https://claude.ai/desktop/directory/github)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)



**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (your handoff template, last week's brief, the runbook index) into one folder and point Cowork at it. Cowork reads the template from there and writes the brief and the watch-list back to it. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from your on-call folder so the template, channel list, and severity definitions stay attached every rotation.

Platform / Oncall / 2026-W17

handoff-template.mdJan 12, 20262 KB

handoff-2026-W16.mdApr 20, 20266 KB

runbook-index.mdMar 30, 202611 KB

In Cowork’s chat bar:Platform / Oncall / 2026-W17

## The prompt

### Copy this into Claude Cowork

Write the on-call handoff for my shift. Cover pages and incident channels from the last 7 days, CS escalations from #support-escalations, and production deploys. For each, note status (resolved, monitoring, still open), the one-line cause if known, and what the next on-call should watch. Write it to the on-call folder and post it to #oncall.



Platform / Oncall / 2026-W17Open in Cowork

### Why this works

Prompt

**Name every source you need.** Pages, CS escalations, and deploys are the three things that wake the next person up; naming all three means nothing falls between systems.

Prompt

**Specify the fields for each item.** That triplet is exactly what the next shift needs to triage at 2am; the brief comes back already shaped that way.

Prompt

**Say where the output should go.** The doc is saved to the folder for the record and in #oncall so the next engineer actually sees it.

Source

**Include the previous version for context.** Anything you marked "monitoring" last rotation carries forward instead of getting dropped.

### Get a better draft

Practice

**Ask for the noisy alerts.** Add "list any alert that fired more than 3 times so we can tune it" and the handoff doubles as the alert-hygiene backlog.

Practice

**Ask it to link runbooks.** Add "for anything still open, link the relevant runbook" so the next on-call has the fix one click away.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /standup skill with my feedback.



Platform / OncallOpen in Cowork



**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it at rotation change

Handoff happens the same hour every week. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill writes the brief at the end of every rotation, whether you remembered or not.

**/schedule** Every Monday at 9am, run /standup over the prior 7 days of pages, #support-escalations, and prod deploys, write the handoff to Platform/Oncall/<week>.md, and post it to #oncall.



Platform / OncallOpen in Cowork

Scheduled taskActive

Weekly on-call handoff

Runs `/standup` over the week's pages, CS escalations, and deploys, writes the brief to the on-call folder, and posts it to #oncall.

Every **Mondays at 9:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/standup` now carries your channel list, your status labels, and your team's handoff template. Share it so every engineer in the rotation produces the same brief, and nobody starts a shift blind because the last person was too tired to write it up.



Share the skill

In Cowork, open **Skills** → `/standup` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your instructions baked in, they don't repeat Steps 1-3.

## What changes for the rotation

The handoff is written and posted with each item's status, cause, and what to watch — the next engineer starts informed instead of searching channels for context.

You did this for one rotation. The same approach covers incident postmortems, release summaries, and the weekly ops review — each one a skill in your team's plugin, run the same way every time.

[Next: Draft the incident postmortem](https://academy.claude.com/use-cases/incident-postmortem)
