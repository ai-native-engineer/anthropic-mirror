<!-- source: https://academy.claude.com/use-cases/incident-postmortem -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Draft the incident postmortem

Timeline, root cause, and action items from the incident channel.

10 minEngineeringClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-fnbe9wym.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-nsjpa7is.png)

## Set up

### Try a plugin

The Engineering plugin ships with `/incident-response` and other incident-and-ops skills as a starting point, already structured to walk an incident channel and reconstruct a timeline. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

EngineeringStreamline engineering workflows — standups, code review, architecture decisions, incident response, and technical documentation. Works with your existing tools or standalone.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=engineering)

`/incident-response`Run an incident response workflow — triage, communicate, and write postmortem.

[Run](claude://cowork/new?q=%2Fincident-response)

`/standup`Generate a standup update from recent activity.

[Run](claude://cowork/new?q=%2Fstandup)

Show all 10 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.951%209.85a1.47%201.47%200%201%201-2.94%200%201.47%201.47%200%200%201%201.47-1.471h1.47V9.85Zm.735%200a1.47%201.47%200%201%201%202.94%200v3.679a1.47%201.47%200%201%201-2.94%200V9.85Z'%20fill='%23E01E5A'/%3e%3cpath%20d='M6.157%203.943a1.47%201.47%200%201%201%200-2.943%201.47%201.47%200%200%201%201.47%201.471v1.472h-1.47Zm0%20.746a1.47%201.47%200%201%201%200%202.943H2.47a1.47%201.47%200%201%201%200-2.943h3.687Z'%20fill='%2336C5F0'/%3e%3cpath%20d='M12.049%206.16a1.47%201.47%200%201%201%202.94%200%201.47%201.47%200%200%201-1.47%201.472h-1.47V6.16Zm-.736%200a1.47%201.47%200%201%201-2.94%200V2.471a1.47%201.47%200%201%201%202.94%200V6.16Z'%20fill='%232EB67D'/%3e%3cpath%20d='M9.843%2012.057a1.47%201.47%200%201%201%200%202.943%201.47%201.47%200%200%201-1.47-1.471v-1.472h1.47Zm0-.735a1.47%201.47%200%201%201%200-2.943h3.687a1.47%201.47%200%201%201%200%202.943H9.843Z'%20fill='%23ECB22E'/%3e%3c/svg%3e)

Slack

Read the incident channel end to end and pull every timestamp, decision, and status update.

[Connect](https://claude.ai/desktop/directory/slack)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%2306AC38'%20d='M4.05%2017.71h4.6V24h-4.6zM16.59.32C14.75.01%2013.45%200%2011.13%200H4.05v14.19h7.24c2.05%200%203.59-.13%204.95-.96%201.5-.9%202.71-2.77%202.71-5.55%200-2.98-1.39-5.01-2.36-5.85C15.89.93%2016.59.32%2016.59.32zm-4.66%2010.39H8.65V3.55h2.87c2.96%200%204.45%201.12%204.45%203.53%200%202.59-1.62%203.63-4.04%203.63z'/%3e%3c/svg%3e)

PagerDuty

Pull the alert timeline, who was paged, and when the incident was acknowledged and resolved.

[Connect](https://claude.ai/desktop/directory/pagerduty)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23632CA6'%20d='m20.43%2017.56-1.86-1.24-1.6%202.63-1.85-.53-1.73%202.7.07.71%208.92-1.63-.52-6.45zm-6.33-3.64c.46-.06.86-.13%201.35-.42.08-.32.1-.83-.04-1.43-.21-.87-.5-1.4-1.1-1.31-.6.1-.63.84-.42%201.71.12.5.33.98.54%201.28zm-2.54.4c.45-.08.96-.43%201.12-.64-.12-.18-.33-.54-.42-1.04-.32-.05-.6-.01-.92.19-.43.26-.77.86-.67%201.28.24.24.53.28.89.21zm-1.87.92c.18-.32.13-.86-.14-1.28-.19.02-.38.07-.57.18-.42.24-.86.77-.73%201.24.35.19.98.2%201.44-.14zm12.63%206.24-1.06-13.1L1.68.13.07%2019.05l8.6%201.24%201.55-2.42c-.85-.56-1.38-1.4-1.62-2.06-.42-1.14-.07-2.45.86-3.13.24-.18.5-.3.77-.37-.07-.43-.01-.93.24-1.37.42-.73%201.2-1.12%202-1.06.06-.58.36-1.13.9-1.46.86-.53%201.98-.33%202.63.44.35-.06.73-.02%201.12.14%201.21.5%201.6%201.88%201.39%202.96.5.36.86.86%201.02%201.45.33%201.21-.24%202.5-1.32%203.07l-1.37%202.25%201.84.53%201.58-2.6%202.44%201.63.63-.07zm-14.2-9.95c.14-.65.86-1.02%201.14-1.18-.33-.56-.5-1.28-.42-1.84.14-.93.93-1.5%201.63-1.43-.14-.5-.14-1.07.06-1.6.36-.93%201.32-1.36%202.14-1%20.03-.5.24-1%20.65-1.36.77-.7%201.93-.6%202.6.2.38-.2.84-.24%201.28-.07.86.33%201.28%201.32.93%202.2.43.2.77.6.93%201.1.3.93-.2%201.93-1.1%202.27.1.45.04.93-.2%201.35-.18.32-.43.55-.71.7.28.59.37%201.27.2%201.93l.5.35c.31-.55.85-.93%201.5-.98a8.53%208.53%200%200%201-.06-2.24c.2-1.84%201.36-2.56%202.35-2.45.43.05.77.24%201.02.5l.23-2.85L3.07%201.7%201.73%2017.56l5.77.83c-.12-.5-.12-1.02.04-1.5-.86-.42-1.5-1.32-1.5-2.4a2.6%202.6%200%200%201%201.28-2.24c-.24-.43-.33-.93-.2-1.43z'/%3e%3c/svg%3e)

DatadogOptional

Attach the error-rate and latency graphs for the impact window.

[Connect](https://claude.ai/desktop/directory/datadog)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (your postmortem template, the runbook, any log exports or graph screenshots) into one folder and point Cowork at it. Cowork reads the template from there and writes the draft, the timeline, and the action-item tracker back to it. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from your incidents folder so your template, severity definitions, and blameless-language guide stay attached.

Incidents / 2026-04-22-checkout-5xx

postmortem-template.mdJan 9, 20263 KB

checkout-service-logs.txtApr 22, 20261.4 MB

error-rate-graph.pngApr 22, 202688 KB

In Cowork’s chat bar:Incidents / 2026-04-22-checkout-5xx

## The prompt

### Copy this into Claude Cowork

From #inc-2026-04-22-checkout-5xx, reconstruct the sequence of events with timestamps, write the customer impact summary, identify the root cause and contributing factors, and draft the postmortem in our template with owners on every action item. Be blameless: describe what the system did, not who made a mistake.

Incidents / 2026-04-22-checkout-5xxOpen in Cowork

### Why this works

Prompt

**Reconstruct, don't summarize.** Asking for the timestamped sequence means the timeline is built from evidence, not memory.

Prompt

**Separate root cause from contributing factors.** Forces a real causal chain instead of a single scapegoat line.

Prompt

**State the tone you want.** Language stays on system behavior; the doc survives review.

Source

**Provide your template as context.** Output drops straight into your sections, your severity scale, your action-item format.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /incident-response skill with my feedback.

IncidentsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it when the incident closes

The draft should exist before the review meeting is scheduled. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill watches for resolved incidents and writes the first draft into the matching folder.

**/schedule** Every weekday at 6pm, check PagerDuty for incidents resolved in the last 24 hours, run /incident-response on each one, and write the draft to Incidents/<incident-id>/incident-response-draft.md.

IncidentsOpen in Cowork

Scheduled taskActive

Postmortem first draft

Daily at 6pm, finds incidents resolved in the last 24h, runs `/incident-response` against the channel and timeline, and writes the draft to the incident folder.

Every **weekdays at 6:00pm**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/incident-response` now carries your template, your severity definitions, and your blameless-language rules. Share it so every on-call engineer writes the doc the same way, and the review meeting starts at "is this right" instead of "who's writing this up."

Share the skill

In Cowork, open **Skills** → `/incident-response` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your template and tone baked in, so they don't repeat Steps 1-3.

## What changes for incident review

You have a postmortem drafted from the incident record, with an owner on every action item — ready to review instead of write.

You did this for one incident. The same approach covers on-call handoffs, runbook updates, and sprint retros — each one a skill your team runs the same way.

[Next: Sprint retro and on-call handoff](https://academy.claude.com/use-cases/sprint-retro-handoff)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for incident review](#what-changes-for-incident-review)
