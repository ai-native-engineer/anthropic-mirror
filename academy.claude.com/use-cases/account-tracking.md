<!-- source: https://academy.claude.com/use-cases/account-tracking -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Account tracking

Account health in green/yellow/red with this week's two moves.

10 minSalesClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-kb8jxxpj.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-lt8ltc3p.png)

## 1. Set up

### Try a plugin

The Sales plugin ships with `/pipeline-review` and other customer success skills as a starting point, already structured to weigh usage, tickets, and sentiment into one call. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Sales8 skills for account research, call prep, pipeline review, and account health

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=sales)

`/pipeline-review`Score account health from usage, tickets, NPS, and the success plan

[Run](claude://cowork/new?q=%2Fpipeline-review)

`/call-summary`Cluster a folder of call transcripts into themes with counts and quotes

[Run](claude://cowork/new?q=%2Fcall-summary)

Show all 9 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/764fa5af07f936df.svg)

Salesforce

Custom connector

![](images/2ba03d1b12a8d596.svg)

Intercom

Read open conversations and recent tickets so the health call reflects what support is actually seeing.

[Connect](https://claude.ai/desktop/directory/intercom)

![](images/a3bfc5814bd6a3e2.svg)

Google Drive

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a
working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (the usage export, the success plan, the latest NPS responses) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the health summary back to it. If you track this account ongoing, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your health criteria, instructions, and memory stay attached.

Accounts / Northwind / health

usage-export-apr.csvApr 25, 202664 KB

success-plan.docxFeb 3, 202638 KB

nps-responses-q1.csvApr 2, 202612 KB

In Cowork’s chat bar:Accounts / Northwind / health

## 2. The prompt

### Copy this into Claude Cowork

From the usage data, open Zendesk tickets, NPS responses, and success plan for Northwind, write the account health summary to the account folder: call it red, yellow, or green with the reason in one or two sentences, then the two actions to take this week.

Accounts / Northwind / healthOpen in Cowork

### Why this works

Prompt

**Give a fixed set of answers.** "Red, yellow, or green" makes Cowork commit
to one status instead of hedging, and "with the reason" means the call is
defensible when leadership asks.

Prompt

**Say how many items you want.** "Two actions I should take this week" keeps
the output to what you'll actually do before Friday, not a backlog of
everything that could help.

Source

**Name the sources to weigh together.** Naming usage, tickets, NPS, and the
success plan together means health is weighed across product, support,
sentiment, and goals, not just whichever dashboard you checked last.

Source

**Include the goals to measure against.** The success plan and usage export
sit in the working folder, so the health call is measured against the goals
you actually agreed with the customer.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and
Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about"
so you know where to look first when you review the draft.

## 3. Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the
/pipeline-review skill with my feedback.

AccountsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## 4. Make it repeatable

### Run it across your book every week

Health should be tracked, not checked when something breaks. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill writes a fresh summary for every account in your book each week.

**/schedule** Every Monday at 7am, run /pipeline-review for each account in my
book and write the summary to the matching health folder under Accounts. Roll
up anything red into one digest at the top.

AccountsOpen in Cowork

Scheduled taskActive

Weekly account health

Runs `/pipeline-review` for every account in your book and writes the summary
to its health folder, with red accounts rolled up into one digest.

Every **Monday at 7:00 AM**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## 5. Share with your teammates

Your customized `/pipeline-review` now carries your usage thresholds, your risk rules, and your summary format. Share it so every CSM scores health the same way, and the red/yellow/green means the same thing across the whole book.

Share the skill

In Cowork, open **Skills** → `/pipeline-review` → **Share** and pick your
teammates (or your whole workspace, if your admin allows). They get the skill
with your thresholds and format baked in, so they don't repeat Steps 1-3.

## Going forward

### Now in your Cowork

Your processes

Sales plugin

Your tools

![](images/764fa5af07f936df.svg)Salesforce![](images/fce598a81466f954.svg)Zendesk![](images/a3bfc5814bd6a3e2.svg)Google Drive

Your workspace

Accounts

Every account in your book has a current health summary — scored the same way, written to its folder, with the next actions already named.

[Next: Transcript theme extractor](https://academy.claude.com/use-cases/transcript-themes)

* [1. Set up](#1-set-up)
* [2. The prompt](#2-the-prompt)
* [3. Make Cowork work for you](#3-make-cowork-work-for-you)
* [4. Make it repeatable](#4-make-it-repeatable)
* [5. Share with your teammates](#5-share-with-your-teammates)
* [Going forward](#going-forward)
