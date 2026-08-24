<!-- source: https://academy.claude.com/use-cases/design-police -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Design system drift review

Shipped screens and PRs flagged for design-system drift.

15 minDesignClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-mliphhy1.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-hvy17a2s.png)

## Set up

### Try a plugin

The Design plugin ships with `/design-system` already structured to diff a screen or PR against a token file and component inventory. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

DesignAccelerate design workflows — critique, design system management, UX writing, accessibility audits, research synthesis, and dev handoff. From exploration to pixel-perfect specs.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=design)

`/design-system`Audit, document, or extend your design system.

[Run](claude://cowork/new?q=%2Fdesign-system)

`/ux-copy`Write or review UX copy — microcopy, error messages, empty states, CTAs.

[Run](claude://cowork/new?q=%2Fux-copy)

Show all 7 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23181717'%20d='M12%20.3a12%2012%200%200%200-3.8%2023.39c.6.11.82-.26.82-.58v-2.03c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.33-1.76-1.33-1.76-1.09-.74.08-.73.08-.73%201.2.09%201.84%201.24%201.84%201.24%201.07%201.83%202.81%201.3%203.49%201%20.11-.78.42-1.31.76-1.61-2.67-.3-5.47-1.33-5.47-5.93%200-1.31.47-2.38%201.24-3.22-.13-.3-.54-1.52.11-3.18%200%200%201.01-.32%203.3%201.23a11.5%2011.5%200%200%201%206%200c2.29-1.55%203.3-1.23%203.3-1.23.65%201.66.24%202.88.12%203.18.77.84%201.23%201.91%201.23%203.22%200%204.61-2.8%205.63-5.48%205.92.43.37.81%201.1.81%202.22v3.29c0%20.32.22.7.82.58A12%2012%200%200%200%2012%20.3'/%3e%3c/svg%3e)

GitHub

Read open PRs that touch UI and post the drift report as a review comment.

[Connect](https://claude.ai/desktop/directory/github)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%230ACF83'%20d='M8%2024a4%204%200%200%200%204-4v-4H8a4%204%200%200%200%200%208Z'/%3e%3cpath%20fill='%23A259FF'%20d='M4%2012a4%204%200%200%201%204-4h4v8H8a4%204%200%200%201-4-4Z'/%3e%3cpath%20fill='%23F24E1E'%20d='M4%204a4%204%200%200%201%204-4h4v8H8a4%204%200%200%201-4-4Z'/%3e%3cpath%20fill='%23FF7262'%20d='M12%200h4a4%204%200%200%201%200%208h-4V0Z'/%3e%3cpath%20fill='%231ABCFE'%20d='M20%2012a4%204%200%201%201-8%200%204%204%200%200%201%208%200Z'/%3e%3c/svg%3e)

Figma

Use the published library as the source of truth for tokens and components.

[Connect](https://claude.ai/desktop/directory/figma)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.951%209.85a1.47%201.47%200%201%201-2.94%200%201.47%201.47%200%200%201%201.47-1.471h1.47V9.85Zm.735%200a1.47%201.47%200%201%201%202.94%200v3.679a1.47%201.47%200%201%201-2.94%200V9.85Z'%20fill='%23E01E5A'/%3e%3cpath%20d='M6.157%203.943a1.47%201.47%200%201%201%200-2.943%201.47%201.47%200%200%201%201.47%201.471v1.472h-1.47Zm0%20.746a1.47%201.47%200%201%201%200%202.943H2.47a1.47%201.47%200%201%201%200-2.943h3.687Z'%20fill='%2336C5F0'/%3e%3cpath%20d='M12.049%206.16a1.47%201.47%200%201%201%202.94%200%201.47%201.47%200%200%201-1.47%201.472h-1.47V6.16Zm-.736%200a1.47%201.47%200%201%201-2.94%200V2.471a1.47%201.47%200%201%201%202.94%200V6.16Z'%20fill='%232EB67D'/%3e%3cpath%20d='M9.843%2012.057a1.47%201.47%200%201%201%200%202.943%201.47%201.47%200%200%201-1.47-1.471v-1.472h1.47Zm0-.735a1.47%201.47%200%201%201%200-2.943h3.687a1.47%201.47%200%201%201%200%202.943H9.843Z'%20fill='%23ECB22E'/%3e%3c/svg%3e)

SlackOptional

Post the daily drift summary to the design-system channel for triage.

[Connect](https://claude.ai/desktop/directory/slack)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (production screenshots, the PR diffs you're reviewing, your tokens file, the component inventory) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the drift report back to it. If you run design QA regularly, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your system source stays attached.

Design-QA / Sprint-42

prod-settings-screen.pngApr 27, 2026820 KB

pr-4821-billing-panel.diffApr 27, 202614 KB

tokens.jsonApr 20, 202618 KB

In Cowork’s chat bar:Design-QA / Sprint-42

## The prompt

### Copy this into Claude Cowork

Review the shipped screens and open PRs in this folder against our design system. For each one, list every place it drifts from our tokens, components, spacing, or interaction patterns, rate the severity, and suggest the system-compliant fix. Skip anything that already matches.

Design-QA / Sprint-42Open in Cowork

### Why this works

Prompt

**Spell out what to check for.** Tokens, components, spacing, interaction: the checklist is explicit.

Prompt

**Ask for a severity on each finding.** Triage knows what to fix this sprint.

Prompt

**Say what to leave out.** The report is only the work, never the noise.

Source

**Put the reference files in the folder.** Tokens and inventory are read, not remembered.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

The plugin's `/design-system` is a generic starting point. Once Step 2 produces a drift report you'd actually post on a PR, tell Cowork to write your version of the skill. Layer in your severity thresholds, your allowed exceptions, your component-to-code mapping, and the comment tone your engineers respond to. A few minutes of conversation and the skill runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /design-system skill with my feedback.

Design-QAOpen in Cowork

## Make it repeatable

### Make it a live artifact

Drift compounds quietly between sprints. Ask Cowork to publish the report as a live artifact and the design-system team has one link that stays current — re-run the skill or schedule it to refresh.

Publish that drift report as a live artifact for the design-system channel. Keep a running tally of high-severity items still open.

Design-QA / Sprint-42Open in Cowork

### Run it on every PR that touches UI

Drift is cheapest to catch before merge. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and set the customized skill to run twice a day, checking open PRs and the latest production screenshots.

**/schedule** Weekdays at 10am and 4pm, check open PRs labeled "ui" and Design-QA/Sprint-42 for new screens, run /design-system on each, and post the drift report as a comment or to #design-system.

Design-QAOpen in Cowork

Scheduled taskActive

Twice-daily drift check

At 10am and 4pm, checks open UI PRs and the QA folder, runs `/design-system`, and posts the drift report as a PR comment or to #design-system.

Every **weekday at 10 am & 4 pm · checks open UI PRs and Design-QA/Sprint-42**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/design-system` now carries your tokens, your component map, your severity scale, and your exception list. Share it so every squad gets the same review on every PR, and the system team stops being the bottleneck for "is this on-system."

Share the skill

In Cowork, open **Skills** → `/design-system` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your system rules baked in, so they don't repeat Steps 1-3.

## What changes for design QA

Screens and PRs are checked against your design system, with each deviation rated, explained, and paired with the compliant fix — ready to correct instead of spot-check.

You did this for one set of screens. The same approach covers your marketing pages, mobile app, and internal tools — each one becomes a skill your team runs the same way.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/design-icon.svg)

Claude Design

Redraw the flagged screens with on-system components

Open](https://claude.ai/design)

[Next: Encode the brand as a skill](https://academy.claude.com/use-cases/brand-guidelines-skill)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for design QA](#what-changes-for-design-qa)
