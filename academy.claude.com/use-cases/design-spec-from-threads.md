<!-- source: https://academy.claude.com/use-cases/design-spec-from-threads -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Design spec from scattered threads

One review-ready spec from threads, notes, and screenshots.

10 minDesignClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-g1uo6xw3.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-hq8pagpq.png)

## Set up

### Try a plugin

The Design plugin ships with `/design-handoff` and other research and structuring skills as a starting point, already shaped to the section order most design reviews expect. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

DesignAccelerate design workflows — critique, design system management, UX writing, accessibility audits, research synthesis, and dev handoff. From exploration to pixel-perfect specs.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=design)

`/design-handoff`Generate developer handoff specs from a design.

[Run](claude://cowork/new?q=%2Fdesign-handoff)

`/research-synthesis`Synthesize user research into themes, insights, and recommendations.

[Run](claude://cowork/new?q=%2Fresearch-synthesis)

Show all 7 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/b6bf6491858dcff4.svg)

Slack

Read the project channel and DM threads where the real decisions were made.

[Connect](https://claude.ai/desktop/directory/slack)

![](images/ea7c24639ab8053c.svg)

Notion

Pull the meeting notes and PRD draft and write the finished spec back to the project page.

[Connect](https://claude.ai/desktop/directory/notion)

![](images/d0c4c5893ba4311d.svg)

FigmaOptional

Reference the exploration frames and pull the screenshot annotations into the spec.

[Connect](https://claude.ai/desktop/directory/figma)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (exported Slack threads, meeting notes, the screenshots people kept pasting) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the assembled spec back to it. If you write specs regularly, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your spec template, instructions, and memory stay attached.

Design / Checkout-Redesign

slack-export-checkout.txtApr 25, 202662 KB

kickoff-notes.docxApr 18, 202624 KB

current-flow-screens.pngApr 18, 20261.1 MB

In Cowork’s chat bar:Design / Checkout-Redesign

## The prompt

### Copy this into Claude Cowork

Assemble everything in this folder into a single design spec. Structure it as problem, goals, constraints, proposed solution, open questions, and out of scope. Quote the source for any decision already made and flag anything contradictory.

Design / Checkout-RedesignOpen in Cowork

### Why this works

Prompt

**Name the section order.** The output matches the review template, no reshuffling.

Prompt

**Ask it to cite its sources.** Nobody re-litigates what was already settled in Slack.

Prompt

**Flag contradictions explicitly.** Conflicts surface before the review, not during it.

Source

**Put all the context in one place.** Threads, notes, and screenshots all carry equal weight.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /design-handoff skill with my feedback.

DesignOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Make it a live artifact

A spec is out of date the moment someone replies in the channel. Ask Cowork to publish it as a live artifact and the cross-functional team has one link that stays current — re-run the skill or schedule it to refresh.

Publish that spec as a live artifact for the squad. Keep a "decisions changed since last version" section at the top.

Design / Checkout-RedesignOpen in Cowork

### Run it the morning before every review

Review is on the calendar, the spec should already reflect last night's thread. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and set the customized skill to run each morning, re-reading the channel and folder.

**/schedule** Weekdays at 8am, re-read #checkout-redesign and Design/Checkout-Redesign and re-run /design-handoff, updating the spec file and listing any decisions that changed overnight.

DesignOpen in Cowork

Scheduled taskActive

Spec freshness pass

Each weekday at 8am, re-reads the project channel and folder, re-runs `/design-handoff`, and updates the spec with a list of decisions that changed overnight.

Every **weekday at 8 am · re-reads #checkout-redesign and the project folder**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/design-handoff` now carries your section order, your decision-log format, and your contradiction flags. Share it so every designer on the team writes specs the same way, and reviewers know exactly where to look no matter who owns the project.

Share the skill

In Cowork, open **Skills** → `/design-handoff` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your template and format baked in, so they don't repeat Steps 1-3.

## What changes for design review

You have one review-ready spec with each decision cited to its source and each contradiction flagged — assembled from the actual discussion instead of reconstructed by hand.

You did this for one project. The same approach covers research readouts, kickoff briefs, and engineering handoffs — each one becomes a skill your team runs the same way.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/design-icon.svg)

Claude Design

Lay the spec out as an on-brand one-pager

Open](https://claude.ai/design)

[Next: Clickable prototype from real components](https://academy.claude.com/use-cases/clickable-prototype)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for design review](#what-changes-for-design-review)
