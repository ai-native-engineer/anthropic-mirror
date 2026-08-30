<!-- source: https://academy.claude.com/use-cases/incident-postmortem -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Draft the incident postmortem

Timeline, root cause, and action items from the incident channel.

10 minEngineeringClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-fnbe9wym.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-nsjpa7is.png)

## Set up[](#set-up)

### Try a plugin[](#try-a-plugin)

The Engineering plugin ships with `/incident-response` and other incident-and-ops skills as a starting point, already structured to walk an incident channel and reconstruct a timeline. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

EngineeringStreamline engineering workflows — standups, code review, architecture decisions, incident response, and technical documentation. Works with your existing tools or standalone.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=engineering)

`/incident-response`Run an incident response workflow — triage, communicate, and write postmortem.

[Run](claude://cowork/new?q=%2Fincident-response)

`/standup`Generate a standup update from recent activity.

[Run](claude://cowork/new?q=%2Fstandup)

Show all 10 skills

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/b6bf6491858dcff4.svg)

Slack

Read the incident channel end to end and pull every timestamp, decision, and status update.

[Connect](https://claude.ai/desktop/directory/slack)

![](images/f1af6a4ad6ba0248.svg)

PagerDuty

Pull the alert timeline, who was paged, and when the incident was acknowledged and resolved.

[Connect](https://claude.ai/desktop/directory/pagerduty)

![](images/51045b184cff6ff6.svg)

DatadogOptional

Attach the error-rate and latency graphs for the impact window.

[Connect](https://claude.ai/desktop/directory/datadog)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

Drag the files you'll use (your postmortem template, the runbook, any log exports or graph screenshots) into one folder and point Cowork at it. Cowork reads the template from there and writes the draft, the timeline, and the action-item tracker back to it. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from your incidents folder so your template, severity definitions, and blameless-language guide stay attached.

Incidents / 2026-04-22-checkout-5xx

postmortem-template.mdJan 9, 20263 KB

checkout-service-logs.txtApr 22, 20261.4 MB

error-rate-graph.pngApr 22, 202688 KB

In Cowork’s chat bar:Incidents / 2026-04-22-checkout-5xx

## The prompt[](#the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

From #inc-2026-04-22-checkout-5xx, reconstruct the sequence of events with timestamps, write the customer impact summary, identify the root cause and contributing factors, and draft the postmortem in our template with owners on every action item. Be blameless: describe what the system did, not who made a mistake.

Incidents / 2026-04-22-checkout-5xxOpen in Cowork

### Why this works[](#why-this-works)

Prompt

**Reconstruct, don't summarize.** Asking for the timestamped sequence means the timeline is built from evidence, not memory.

Prompt

**Separate root cause from contributing factors.** Forces a real causal chain instead of a single scapegoat line.

Prompt

**State the tone you want.** Language stays on system behavior; the doc survives review.

Source

**Provide your template as context.** Output drops straight into your sections, your severity scale, your action-item format.

### Get a better draft[](#get-a-better-draft)

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you[](#make-cowork-work-for-you)

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /incident-response skill with my feedback.

IncidentsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable[](#make-it-repeatable)

### Run it when the incident closes[](#run-it-when-the-incident-closes)

The draft should exist before the review meeting is scheduled. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill watches for resolved incidents and writes the first draft into the matching folder.

**/schedule** Every weekday at 6pm, check PagerDuty for incidents resolved in the last 24 hours, run /incident-response on each one, and write the draft to Incidents/<incident-id>/incident-response-draft.md.

IncidentsOpen in Cowork

Scheduled taskActive

Postmortem first draft

Daily at 6pm, finds incidents resolved in the last 24h, runs `/incident-response` against the channel and timeline, and writes the draft to the incident folder.

Every **weekdays at 6:00pm**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates[](#share-with-your-teammates)

Your customized `/incident-response` now carries your template, your severity definitions, and your blameless-language rules. Share it so every on-call engineer writes the doc the same way, and the review meeting starts at "is this right" instead of "who's writing this up."

Share the skill

In Cowork, open **Skills** → `/incident-response` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your template and tone baked in, so they don't repeat Steps 1-3.

## What changes for incident review[](#what-changes-for-incident-review)

You have a postmortem drafted from the incident record, with an owner on every action item — ready to review instead of write.

You did this for one incident. The same approach covers on-call handoffs, runbook updates, and sprint retros — each one a skill your team runs the same way.

[Next: Sprint retro and on-call handoff](https://academy.claude.com/use-cases/sprint-retro-handoff)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for incident review](#what-changes-for-incident-review)
