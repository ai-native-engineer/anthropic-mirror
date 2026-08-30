<!-- source: https://academy.claude.com/use-cases/design-doc -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Write the design doc or RFC

A structured proposal with prior art and trade-offs filled in.

10 minEngineeringClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-pbyyssck.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-oj6tpm7w.png)

## Set up[](#set-up)

### Try a plugin[](#try-a-plugin)

The Engineering plugin ships with `/system-design` as a starting point, already structured to fill an RFC template and look up prior art across your wiki. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

EngineeringStreamline engineering workflows — standups, code review, architecture decisions, incident response, and technical documentation. Works with your existing tools or standalone.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=engineering)

`/system-design`Design systems, services, and architectures.

[Run](claude://cowork/new?q=%2Fsystem-design)

`/architecture`Create or evaluate an architecture decision record (ADR).

[Run](claude://cowork/new?q=%2Farchitecture)

Show all 10 skills

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/9d4cebe262b9da95.svg)'%20d='M.87%2018.26c-.25.4-.52.87-.75%201.23a.75.75%200%200%200%20.25%201.02l4.96%203.05a.75.75%200%200%200%201.04-.25c.2-.33.45-.76.73-1.21%201.95-3.22%203.91-2.83%207.45-1.14l4.92%202.34a.75.75%200%200%200%201-.36l2.36-5.34a.75.75%200%200%200-.38-.98c-1.04-.49-3.1-1.46-4.96-2.36-6.68-3.24-12.36-3.03-16.62%204Z'/%3e%3cpath%20fill='url(%23cfB)'%20d='M23.13%205.74c.25-.4.52-.87.75-1.23a.75.75%200%200%200-.25-1.02L18.67.44a.75.75%200%200%200-1.04.25c-.2.33-.45.76-.73%201.21-1.95%203.22-3.91%202.83-7.45%201.14L4.53.7a.75.75%200%200%200-1%20.36L1.17%206.4a.75.75%200%200%200%20.38.98c1.04.49%203.1%201.46%204.96%202.36%206.68%203.24%2012.36%203.03%2016.62-4Z'/%3e%3c/svg%3e)

Confluence

Look up prior RFCs and architecture pages and write the new doc straight into your engineering space. Confluence access comes through the Atlassian Rovo connector (Jira and Confluence).

[Connect](https://claude.ai/desktop/directory/atlassian)

![](images/92b68e492ad6094d.svg)

GitHub

Read the relevant code and past ADRs so the proposal references the system as it actually is.

[Connect](https://claude.ai/desktop/directory/github)

![](images/ea7c24639ab8053c.svg)

NotionOptional

Pull the RFC template and publish the draft into your design-review database.

[Connect](https://claude.ai/desktop/directory/notion)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

Drag the files you'll use (your RFC template, the one-pager or notes you've already written, related past RFCs, the service's architecture diagram) into one folder and point Cowork at it. Cowork reads from there and writes the draft, the alternatives table, and the diagram back to it. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from your RFCs folder so your template, your review checklist, and your team's writing conventions stay attached.

RFCs / 0087-streaming-events

rfc-template.mdJan 4, 20262 KB

notes-streaming-migration.mdApr 24, 20265 KB

current-pipeline-diagram.pngMar 11, 2026142 KB

In Cowork’s chat bar:RFCs / 0087-streaming-events

## The prompt[](#the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Write a design doc for moving our event pipeline from batch to streaming. Look up prior art and architecture constraints, then draft the proposal in our RFC template: problem, goals and non-goals, two or three approaches with trade-offs, the recommendation, and open questions. I'll fill in the parts only I know.

RFCs / 0087-streaming-eventsOpen in Cowork

### Why this works[](#why-this-works)

Prompt

**Ask for prior art explicitly.** Cowork searches your wiki and past RFCs so the doc cites what's been tried before.

Prompt

**Force two or three approaches.** You get a real trade-off table, not a sales pitch for the first idea.

Prompt

**Say which parts you'll fill in.** Cowork handles structure and lookup; you spend time on the actual judgment call.

Source

**Give it your template to follow.** Output follows your sections and headings, so reviewers see the structure they expect.

### Get a better draft[](#get-a-better-draft)

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you[](#make-cowork-work-for-you)

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /system-design skill with my feedback.

RFCsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable[](#make-it-repeatable)

### Run it from any one-pager[](#run-it-from-any-one-pager)

Design docs start as a paragraph in a Slack thread or a notes file. Type `/schedule` or open **Scheduled** in the Cowork sidebar, and the customized skill watches your RFCs/inbox folder and turns any new one-pager into a structured first draft.

**/schedule** Weekdays at 9am, check RFCs/inbox for new one-pagers, run /system-design on each one, and write the structured draft to a numbered folder under RFCs/.

RFCsOpen in Cowork

Scheduled taskActive

RFC inbox to draft

Weekdays at 9am, picks up new one-pagers from RFCs/inbox, runs `/system-design` with prior-art lookup, and writes a structured draft to a numbered RFC folder.

Every **weekday at 9:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates[](#share-with-your-teammates)

Your customized `/system-design` now carries your template, your prior-art sources, and your reviewers' standing questions. Share it so every tech lead's RFC arrives in the same shape, and architecture review spends time on the decision instead of the formatting.

Share the skill

In Cowork, open **Skills** → `/system-design` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your template and review checklist baked in, so they don't repeat Steps 1-3.

## What changes for design review[](#what-changes-for-design-review)

You have a complete RFC draft in your template, with prior art and trade-offs filled in from your own sources — ready to edit and review instead of write from a blank page.

You did this for one proposal. The same approach covers API changes, schema migrations, and architecture decisions — each one becomes a skill your team runs the same way.

[Next: Build an "Ask the Company" agent](https://academy.claude.com/use-cases/ask-the-company)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for design review](#what-changes-for-design-review)
