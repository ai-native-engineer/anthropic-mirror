<!-- source: https://academy.claude.com/use-cases/sprint-retro-handoff -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Write the sprint retro and on-call handoff

What shipped, what slipped, and what the next on-call needs to know.

10 minEngineeringClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-ko3ehgyx.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-lth7yta3.png)

## Set up[](#set-up)

### Try a plugin[](#try-a-plugin)

The Engineering plugin ships with `/tech-debt` and `/standup` already structured to read a closed cycle and a channel window and split the output into discussion themes versus operational watch-fors. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Engineering9 skills for postmortems, design docs, on-call handoffs, and cost reviews

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=engineering)

`/tech-debt`Draft the sprint retro from the closed cycle and team channel

[Run](claude://cowork/new?q=%2Ftech-debt)

`/standup`Write the on-call handoff from the week's alerts and pages

[Run](claude://cowork/new?q=%2Fstandup)

Show all 10 skills

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/d9bcb0bb9b2b1fff.svg)

Linear

Read the closed cycle: what was planned, what shipped, what carried over and why.

[Connect](https://claude.ai/desktop/directory/linear)

![](images/b6bf6491858dcff4.svg)

Slack

Pull the team and on-call channels for the context the tickets don't capture: the why-it-slipped and the 2am page.

[Connect](https://claude.ai/desktop/directory/slack)

![](images/f1af6a4ad6ba0248.svg)

PagerDutyOptional

List every page in the rotation so toil is counted, not estimated.

[Connect](https://claude.ai/desktop/directory/pagerduty)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

Keep your retro template, the running action-items list, and last sprint's retro in one folder. Cowork reads the format from there and writes both docs back so the retro and the handoff live next to their predecessors. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from the folder so your team's definition of "shipped" and the discussion-prompt style carry over every cycle.

Platform / retros / 2026-sprint-08

retro-template.mdJan 6, 20262 KB

sprint-07-retro.mdApr 13, 20266 KB

retro-action-items.mdApr 13, 20263 KB

In Cowork’s chat bar:Platform / retros / 2026-sprint-08

## The prompt[](#the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Read the just-closed Linear cycle and two weeks of #team-platform and #oncall-platform. Write the sprint retro (shipped, slipped with reasons, themes worth discussing) and a separate on-call handoff (open alerts, toil, what the next rotation should watch). Pull quotes where they help. Keep each section to what's discussable in a 30-minute meeting.

Platform / retros / 2026-sprint-08Open in Cowork

### Why this works[](#why-this-works)

Prompt

**Ask for the reason behind each item.** The retro is about why, not the list. Asking forces the synthesis.

Prompt

**Split outputs that serve different purposes.** One is a conversation, one is operational. Mixing them buries both.

Prompt

**Set a length limit.** A length budget kills the exhaustive list and surfaces what's worth talking about.

Source

**Combine complementary sources.** Tickets say what moved; Slack says why. The pair is the whole story.

### Get a better draft[](#get-a-better-draft)

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you[](#make-cowork-work-for-you)

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /tech-debt skill with my feedback.

Platform / retrosOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable[](#make-it-repeatable)

### Run it when the cycle closes[](#run-it-when-the-cycle-closes)

Retro prep shouldn't be the TPM's Friday afternoon. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill drafts both docs the moment the cycle ends.

**/schedule** Every Friday at 3pm, run /tech-debt on the cycle that just closed and /standup on the last two weeks, write both to Platform/retros/<sprint>/, and post the handoff to #oncall-platform.

Platform / retrosOpen in Cowork

Scheduled taskActive

Sprint retro + on-call handoff

At cycle close, runs `/tech-debt` and `/standup`, writes both to the dated retro folder, and posts the handoff to the on-call channel.

Every **Friday at 3:00pm**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates[](#share-with-your-teammates)

Your customized `/tech-debt` now knows your tracker, your channels, your template, and what counts as a theme versus a status update. Share it so every squad runs the same retro prep and on-call handoffs read the same way org-wide.

Share the skill

In Cowork, open **Skills** → `/tech-debt` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your template and channel defaults baked in, so they don't repeat Steps 1-3.

## What changes for retro day[](#what-changes-for-retro-day)

The sprint retro and on-call handoff are drafted from the closed cycle and channel history — ready to review and edit instead of write from scratch.

You did this for one sprint. The same approach covers incident postmortems, release notes, and the weekly status summary — each one becomes a skill your team runs the same way.

[Next: Draft the incident postmortem](https://academy.claude.com/use-cases/incident-postmortem)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for retro day](#what-changes-for-retro-day)
