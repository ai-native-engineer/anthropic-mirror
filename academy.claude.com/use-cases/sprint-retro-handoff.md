<!-- source: https://academy.claude.com/use-cases/sprint-retro-handoff -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Write the sprint retro and on-call handoff

What shipped, what slipped, and what the next on-call needs to know.

10 minEngineeringClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-ko3ehgyx.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-lth7yta3.png)

## Set up

### Try a plugin

The Engineering plugin ships with `/tech-debt` and `/standup` already structured to read a closed cycle and a channel window and split the output into discussion themes versus operational watch-fors. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Engineering9 skills for postmortems, design docs, on-call handoffs, and cost reviews

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=engineering)

`/tech-debt`Draft the sprint retro from the closed cycle and team channel

[Run](claude://cowork/new?q=%2Ftech-debt)

`/standup`Write the on-call handoff from the week's alerts and pages

[Run](claude://cowork/new?q=%2Fstandup)

Show all 10 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%20100%20100'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%235E6AD2'%20d='M1.225%2061.523c-.222-.949.908-1.546%201.597-.857l36.512%2036.512c.689.689.092%201.819-.857%201.597a50.06%2050.06%200%200%201-37.252-37.252Zm-1.22-13.59a.98.98%200%200%200%20.283.724l50.055%2050.055a.98.98%200%200%200%20.724.283%2049.9%2049.9%200%200%200%208.636-1.518.976.976%200%200%200%20.462-1.647L2.17%2038.835a.976.976%200%200%200-1.647.462%2049.9%2049.9%200%200%200-1.518%208.636Zm4.194-17.443a.988.988%200%200%200%20.184%201.152l63.975%2063.975a.988.988%200%200%200%201.152.184%2050.4%2050.4%200%200%200%206.08-3.495.993.993%200%200%200%20.161-1.53L9.224%2024.249a.993.993%200%200%200-1.53.161%2050.4%2050.4%200%200%200-3.495%206.08Zm9.723-13.067a.99.99%200%200%201-.026-1.377C23.068%206.08%2036.765-.002%2051.888-.002c27.59%200%2049.957%2022.367%2049.957%2049.957%200%2015.123-6.082%2028.82-16.048%2038.013a.99.99%200%200%201-1.377-.026z'/%3e%3c/svg%3e)

Linear

Read the closed cycle: what was planned, what shipped, what carried over and why.

[Connect](https://claude.ai/desktop/directory/linear)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.951%209.85a1.47%201.47%200%201%201-2.94%200%201.47%201.47%200%200%201%201.47-1.471h1.47V9.85Zm.735%200a1.47%201.47%200%201%201%202.94%200v3.679a1.47%201.47%200%201%201-2.94%200V9.85Z'%20fill='%23E01E5A'/%3e%3cpath%20d='M6.157%203.943a1.47%201.47%200%201%201%200-2.943%201.47%201.47%200%200%201%201.47%201.471v1.472h-1.47Zm0%20.746a1.47%201.47%200%201%201%200%202.943H2.47a1.47%201.47%200%201%201%200-2.943h3.687Z'%20fill='%2336C5F0'/%3e%3cpath%20d='M12.049%206.16a1.47%201.47%200%201%201%202.94%200%201.47%201.47%200%200%201-1.47%201.472h-1.47V6.16Zm-.736%200a1.47%201.47%200%201%201-2.94%200V2.471a1.47%201.47%200%201%201%202.94%200V6.16Z'%20fill='%232EB67D'/%3e%3cpath%20d='M9.843%2012.057a1.47%201.47%200%201%201%200%202.943%201.47%201.47%200%200%201-1.47-1.471v-1.472h1.47Zm0-.735a1.47%201.47%200%201%201%200-2.943h3.687a1.47%201.47%200%201%201%200%202.943H9.843Z'%20fill='%23ECB22E'/%3e%3c/svg%3e)

Slack

Pull the team and on-call channels for the context the tickets don't capture: the why-it-slipped and the 2am page.

[Connect](https://claude.ai/desktop/directory/slack)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%2306AC38'%20d='M4.05%2017.71h4.6V24h-4.6zM16.59.32C14.75.01%2013.45%200%2011.13%200H4.05v14.19h7.24c2.05%200%203.59-.13%204.95-.96%201.5-.9%202.71-2.77%202.71-5.55%200-2.98-1.39-5.01-2.36-5.85C15.89.93%2016.59.32%2016.59.32zm-4.66%2010.39H8.65V3.55h2.87c2.96%200%204.45%201.12%204.45%203.53%200%202.59-1.62%203.63-4.04%203.63z'/%3e%3c/svg%3e)

PagerDutyOptional

List every page in the rotation so toil is counted, not estimated.

[Connect](https://claude.ai/desktop/directory/pagerduty)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Keep your retro template, the running action-items list, and last sprint's retro in one folder. Cowork reads the format from there and writes both docs back so the retro and the handoff live next to their predecessors. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from the folder so your team's definition of "shipped" and the discussion-prompt style carry over every cycle.

Platform / retros / 2026-sprint-08

retro-template.mdJan 6, 20262 KB

sprint-07-retro.mdApr 13, 20266 KB

retro-action-items.mdApr 13, 20263 KB

In Cowork’s chat bar:Platform / retros / 2026-sprint-08

## The prompt

### Copy this into Claude Cowork

Read the just-closed Linear cycle and two weeks of #team-platform and #oncall-platform. Write the sprint retro (shipped, slipped with reasons, themes worth discussing) and a separate on-call handoff (open alerts, toil, what the next rotation should watch). Pull quotes where they help. Keep each section to what's discussable in a 30-minute meeting.

Platform / retros / 2026-sprint-08Open in Cowork

### Why this works

Prompt

**Ask for the reason behind each item.** The retro is about why, not the list. Asking forces the synthesis.

Prompt

**Split outputs that serve different purposes.** One is a conversation, one is operational. Mixing them buries both.

Prompt

**Set a length limit.** A length budget kills the exhaustive list and surfaces what's worth talking about.

Source

**Combine complementary sources.** Tickets say what moved; Slack says why. The pair is the whole story.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /tech-debt skill with my feedback.

Platform / retrosOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it when the cycle closes

Retro prep shouldn't be the TPM's Friday afternoon. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill drafts both docs the moment the cycle ends.

**/schedule** Every Friday at 3pm, run /tech-debt on the cycle that just closed and /standup on the last two weeks, write both to Platform/retros/<sprint>/, and post the handoff to #oncall-platform.

Platform / retrosOpen in Cowork

Scheduled taskActive

Sprint retro + on-call handoff

At cycle close, runs `/tech-debt` and `/standup`, writes both to the dated retro folder, and posts the handoff to the on-call channel.

Every **Friday at 3:00pm**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/tech-debt` now knows your tracker, your channels, your template, and what counts as a theme versus a status update. Share it so every squad runs the same retro prep and on-call handoffs read the same way org-wide.

Share the skill

In Cowork, open **Skills** → `/tech-debt` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your template and channel defaults baked in, so they don't repeat Steps 1-3.

## What changes for retro day

The sprint retro and on-call handoff are drafted from the closed cycle and channel history — ready to review and edit instead of write from scratch.

You did this for one sprint. The same approach covers incident postmortems, release notes, and the weekly status summary — each one becomes a skill your team runs the same way.

[Next: Draft the incident postmortem](https://academy.claude.com/use-cases/incident-postmortem)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for retro day](#what-changes-for-retro-day)
