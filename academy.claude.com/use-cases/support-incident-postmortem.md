<!-- source: https://academy.claude.com/use-cases/support-incident-postmortem -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Support incident postmortem

The customer-facing postmortem, drafted from the war room before anyone forgets.

10 minOperationsClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-ekdkz1b1.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-dwsje4gy.png)

## Set up

### Try a plugin

The Operations plugin ships with `/runbook` and `/status-report` as a starting point, already structured to walk a war room and frame the customer impact. In Step 3 you'll save your own version as `/incident-review`. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

OperationsOptimize business operations — vendor management, process documentation, change management, capacity planning, and compliance tracking. Keep your organization running efficiently.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=operations)

`/runbook`Create or update an operational runbook for a recurring task or procedure.

[Run](claude://cowork/new?q=%2Frunbook)

`/status-report`Generate a status report with KPIs, risks, and action items.

[Run](claude://cowork/new?q=%2Fstatus-report)

Show all 9 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.951%209.85a1.47%201.47%200%201%201-2.94%200%201.47%201.47%200%200%201%201.47-1.471h1.47V9.85Zm.735%200a1.47%201.47%200%201%201%202.94%200v3.679a1.47%201.47%200%201%201-2.94%200V9.85Z'%20fill='%23E01E5A'/%3e%3cpath%20d='M6.157%203.943a1.47%201.47%200%201%201%200-2.943%201.47%201.47%200%200%201%201.47%201.471v1.472h-1.47Zm0%20.746a1.47%201.47%200%201%201%200%202.943H2.47a1.47%201.47%200%201%201%200-2.943h3.687Z'%20fill='%2336C5F0'/%3e%3cpath%20d='M12.049%206.16a1.47%201.47%200%201%201%202.94%200%201.47%201.47%200%200%201-1.47%201.472h-1.47V6.16Zm-.736%200a1.47%201.47%200%201%201-2.94%200V2.471a1.47%201.47%200%201%201%202.94%200V6.16Z'%20fill='%232EB67D'/%3e%3cpath%20d='M9.843%2012.057a1.47%201.47%200%201%201%200%202.943%201.47%201.47%200%200%201-1.47-1.471v-1.472h1.47Zm0-.735a1.47%201.47%200%201%201%200-2.943h3.687a1.47%201.47%200%201%201%200%202.943H9.843Z'%20fill='%23ECB22E'/%3e%3c/svg%3e)

Slack

Read the war-room channel end to end and pull every status update, decision, and timestamp.

[Connect](https://claude.ai/desktop/directory/slack)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cg%20fill='%2303363D'%3e%3cpath%20d='M11%207.7v13.1H.2L11%207.7Z'/%3e%3cpath%20d='M11%203.2a5.4%205.4%200%200%201-10.8%200H11Z'/%3e%3cpath%20d='M13%2016.3V3.2h10.8L13%2016.3Z'/%3e%3cpath%20d='M13%2020.8a5.4%205.4%200%200%201%2010.8%200H13Z'/%3e%3c/g%3e%3c/svg%3e)

Zendesk

Pull every ticket opened during the impact window, with the customer's own words.

Custom connector

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23181717'%20d='M12%20.3a12%2012%200%200%200-3.8%2023.39c.6.11.82-.26.82-.58v-2.03c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.33-1.76-1.33-1.76-1.09-.74.08-.73.08-.73%201.2.09%201.84%201.24%201.84%201.24%201.07%201.83%202.81%201.3%203.49%201%20.11-.78.42-1.31.76-1.61-2.67-.3-5.47-1.33-5.47-5.93%200-1.31.47-2.38%201.24-3.22-.13-.3-.54-1.52.11-3.18%200%200%201.01-.32%203.3%201.23a11.5%2011.5%200%200%201%206%200c2.29-1.55%203.3-1.23%203.3-1.23.65%201.66.24%202.88.12%203.18.77.84%201.23%201.91%201.23%203.22%200%204.61-2.8%205.63-5.48%205.92.43.37.81%201.1.81%202.22v3.29c0%20.32.22.7.82.58A12%2012%200%200%200%2012%20.3'/%3e%3c/svg%3e)

GitHubOptional

List the deploys and merged changes in the 24 hours before the incident started.

[Connect](https://claude.ai/desktop/directory/github)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (your customer-postmortem template, an export of the war room, the ticket CSV) into one folder and point Cowork at it. Cowork reads the template from there and writes the draft, the impacted-customer list, and the remediation tracker back to it. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from your incident-reviews folder so the template, tone guide, and SLA definitions stay attached.

Support / Incidents / INC-4417

customer-postmortem-template.mdFeb 3, 20263 KB

tickets-2026-04-24.csvApr 25, 202662 KB

war-room-export.txtApr 25, 2026340 KB

In Cowork’s chat bar:Support / Incidents / INC-4417

## The prompt

### Copy this into Claude Cowork

Draft the customer-facing incident review for INC-4417. Pull the war-room thread, tickets from the impact window, deploys from the prior 24 hours, and direct customer quotes. Reconstruct the timeline, quantify how many customers were impacted and for how long, and write the first cut in our template with recommended remediation owners.

Support / Incidents / INC-4417Open in Cowork

### Why this works

Prompt

**Name the audience up front.** The register changes; this is the doc your CSMs forward, not the engineering retro.

Prompt

**Quantify the impact.** "How many, for how long" forces a number you can put in the SLA-credit conversation.

Prompt

**Ask for direct quotes.** The affected-customer voice is the part leadership pays attention to; ask for it explicitly.

Prompt

**Set a time range.** Tickets and deploys are bounded by the incident timestamps, so the suspect list is short and relevant.

### Get a better draft

Practice

**Separate internal from external.** Add "write an internal appendix with the suspect deploys; keep the customer doc to impact and remediation" so one run produces both.

Practice

**Add an example to match.** Drop a past review you were proud of in the folder and Cowork matches the structure and the apology tone your brand uses.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /incident-review skill with my feedback.

Support / IncidentsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it when the war room closes

The customer doc should exist before the first CSM asks for it. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill watches for closed war rooms and writes the first cut.

**/schedule** Every weekday at 9am, check for any #inc- channel marked resolved in the last 24 hours, run /incident-review on it, and write the draft to Support/Incidents/<incident-id>/customer-review.md.

Support / IncidentsOpen in Cowork

Scheduled taskActive

Customer incident-review draft

Daily at 9am, finds war rooms resolved in the last 24h, runs `/incident-review` on each, and writes the customer-facing draft to the incident folder.

Every **weekdays at 9:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/incident-review` now carries your template, your tone guide, and your SLA-credit language. Share it so every incident gets the same customer doc, whichever support lead was on shift.

Share the skill

In Cowork, open **Skills** → `/incident-review` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your instructions baked in, they don't repeat Steps 1-3.

## What changes after an incident

The customer-facing incident review is drafted from the source record with impact quantified and remediation assigned — ready to edit and send rather than write from scratch.

You did this for one incident. The same approach covers internal retros, status-page updates, and SLA-credit summaries — each one becomes a skill your team runs the same way.

[Next: Turn the thread into a decision doc(opens in new tab)](https://academy.claude.com/use-cases/thread-to-decision)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes after an incident](#what-changes-after-an-incident)
