<!-- source: https://academy.claude.com/use-cases/support-incident-postmortem -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Support incident postmortem

The customer-facing postmortem, drafted from the war room before anyone forgets.

10 minOperationsClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-ekdkz1b1.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-dwsje4gy.png)

## Set up[](#set-up)

### Try a plugin[](#try-a-plugin)

The Operations plugin ships with `/runbook` and `/status-report` as a starting point, already structured to walk a war room and frame the customer impact. In Step 3 you'll save your own version as `/incident-review`. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

OperationsOptimize business operations — vendor management, process documentation, change management, capacity planning, and compliance tracking. Keep your organization running efficiently.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=operations)

`/runbook`Create or update an operational runbook for a recurring task or procedure.

[Run](claude://cowork/new?q=%2Frunbook)

`/status-report`Generate a status report with KPIs, risks, and action items.

[Run](claude://cowork/new?q=%2Fstatus-report)

Show all 9 skills

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/b6bf6491858dcff4.svg)

Slack

Read the war-room channel end to end and pull every status update, decision, and timestamp.

[Connect](https://claude.ai/desktop/directory/slack)

![](images/fce598a81466f954.svg)

Zendesk

Pull every ticket opened during the impact window, with the customer's own words.

Custom connector

![](images/92b68e492ad6094d.svg)

GitHubOptional

List the deploys and merged changes in the 24 hours before the incident started.

[Connect](https://claude.ai/desktop/directory/github)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

Drag the files you'll use (your customer-postmortem template, an export of the war room, the ticket CSV) into one folder and point Cowork at it. Cowork reads the template from there and writes the draft, the impacted-customer list, and the remediation tracker back to it. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from your incident-reviews folder so the template, tone guide, and SLA definitions stay attached.

Support / Incidents / INC-4417

customer-postmortem-template.mdFeb 3, 20263 KB

tickets-2026-04-24.csvApr 25, 202662 KB

war-room-export.txtApr 25, 2026340 KB

In Cowork’s chat bar:Support / Incidents / INC-4417

## The prompt[](#the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Draft the customer-facing incident review for INC-4417. Pull the war-room thread, tickets from the impact window, deploys from the prior 24 hours, and direct customer quotes. Reconstruct the timeline, quantify how many customers were impacted and for how long, and write the first cut in our template with recommended remediation owners.

Support / Incidents / INC-4417Open in Cowork

### Why this works[](#why-this-works)

Prompt

**Name the audience up front.** The register changes; this is the doc your CSMs forward, not the engineering retro.

Prompt

**Quantify the impact.** "How many, for how long" forces a number you can put in the SLA-credit conversation.

Prompt

**Ask for direct quotes.** The affected-customer voice is the part leadership pays attention to; ask for it explicitly.

Prompt

**Set a time range.** Tickets and deploys are bounded by the incident timestamps, so the suspect list is short and relevant.

### Get a better draft[](#get-a-better-draft)

Practice

**Separate internal from external.** Add "write an internal appendix with the suspect deploys; keep the customer doc to impact and remediation" so one run produces both.

Practice

**Add an example to match.** Drop a past review you were proud of in the folder and Cowork matches the structure and the apology tone your brand uses.

## Make Cowork work for you[](#make-cowork-work-for-you)

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /incident-review skill with my feedback.

Support / IncidentsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable[](#make-it-repeatable)

### Run it when the war room closes[](#run-it-when-the-war-room-closes)

The customer doc should exist before the first CSM asks for it. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill watches for closed war rooms and writes the first cut.

**/schedule** Every weekday at 9am, check for any #inc- channel marked resolved in the last 24 hours, run /incident-review on it, and write the draft to Support/Incidents/<incident-id>/customer-review.md.

Support / IncidentsOpen in Cowork

Scheduled taskActive

Customer incident-review draft

Daily at 9am, finds war rooms resolved in the last 24h, runs `/incident-review` on each, and writes the customer-facing draft to the incident folder.

Every **weekdays at 9:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates[](#share-with-your-teammates)

Your customized `/incident-review` now carries your template, your tone guide, and your SLA-credit language. Share it so every incident gets the same customer doc, whichever support lead was on shift.

Share the skill

In Cowork, open **Skills** → `/incident-review` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your instructions baked in, they don't repeat Steps 1-3.

## What changes after an incident[](#what-changes-after-an-incident)

The customer-facing incident review is drafted from the source record with impact quantified and remediation assigned — ready to edit and send rather than write from scratch.

You did this for one incident. The same approach covers internal retros, status-page updates, and SLA-credit summaries — each one becomes a skill your team runs the same way.

[Next: Turn the thread into a decision doc(opens in new tab)](https://academy.claude.com/use-cases/thread-to-decision)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes after an incident](#what-changes-after-an-incident)
