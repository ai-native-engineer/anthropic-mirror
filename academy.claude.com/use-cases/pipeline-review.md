<!-- source: https://academy.claude.com/use-cases/pipeline-review -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Pipeline reviews

At-risk deals flagged, with the why.

10 minSalesClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-jwybpfo3.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-gah6gl3f.png)

## 1. Set up[](#1-set-up)

### Try a plugin[](#try-a-plugin)

The Sales plugin ships with `/pipeline-review` and other forecast-hygiene skills as a starting point, already structured to score opps and call out risk. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

SalesProspect, craft outreach, and build deal strategy faster. Prep for calls, manage your pipeline, and write personalized messaging that moves deals forward.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=sales)

`/pipeline-review`Analyze pipeline health — prioritize deals, flag risks, get a weekly action plan.

[Run](claude://cowork/new?q=%2Fpipeline-review)

`/call-prep`Prepare for a sales call with account context, attendee research, and suggested agenda.

[Run](claude://cowork/new?q=%2Fcall-prep)

Show all 9 skills

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/764fa5af07f936df.svg)

Salesforce

Custom connector

![](images/a3bfc5814bd6a3e2.svg)

Google Drive

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a
working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

Drag the files you'll use (this week's pipeline export, last week's review doc, your stage definitions) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the scored sheet and review doc back to it. If you run pipeline weekly, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your stage criteria, instructions, and memory stay attached.

Pipeline / 2026-W17

pipeline-export-W17.xlsxApr 26, 202688 KB

review-doc-W16.docxApr 20, 202631 KB

stage-exit-criteria.pdfJan 6, 202652 KB

In Cowork’s chat bar:Pipeline / 2026-W17

## 2. The prompt[](#2-the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Score each open opp in this week's pipeline on stage hygiene, whether there's a real next step, and how long it's sat in stage. Flag the at-risk deals and say why in one line each, then write the manager-ready review doc for our Monday pipeline meeting.

Pipeline / 2026-W17Open in Cowork

### Why this works[](#why-this-works)

Prompt

**Spell out your scoring criteria.** "Hygiene, real next step, age in
stage" gives Cowork the rubric your manager uses, so the score means
something in the meeting instead of being a generic health number.

Prompt

**Set a length limit per item.** "Say why in one line each" keeps the
at-risk section scannable, so the meeting time goes to the deals that need
it rather than reading paragraphs.

Prompt

**Ask for the write-up alongside the data.** "Manager-ready review doc"
tells Cowork to write the narrative around the scores, the part you'd
otherwise type up Sunday night.

Source

**Put your reference docs in the folder.** Your stage exit criteria and last
week's review doc sit in the working folder, so hygiene is scored against
your definitions and the doc follows the format your manager already expects.

### Get a better draft[](#get-a-better-draft)

Practice

**Add an example to match.** Drop an example you like into the folder and
Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about"
so you know where to look first when you review the draft.

## 3. Make Cowork work for you[](#3-make-cowork-work-for-you)

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the
/pipeline-review skill with my feedback.

PipelineOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## 4. Make it repeatable[](#4-make-it-repeatable)

### Run it before the Monday meeting[](#run-it-before-the-monday-meeting)

The review should be waiting before the meeting, not built during it. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill scores the pipeline and writes the doc every Monday morning.

**/schedule** Every Monday at 8am, run /pipeline-review against the current
Salesforce pipeline and write the scored sheet and review doc to a new folder
under Pipeline named for the week.

PipelineOpen in Cowork

Scheduled taskActive

Monday pipeline review

Runs `/pipeline-review` against the current Salesforce pipeline and writes
the scored sheet and review doc to a weekly folder.

Every **Monday at 8:00 AM**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## 5. Share with your teammates[](#5-share-with-your-teammates)

Your customized `/pipeline-review` now carries your stage criteria, your at-risk thresholds, and your review doc format. Share it so every rep scores their own pipeline the same way, and the team meeting reads from one consistent doc per rep.

Share the skill

In Cowork, open **Skills** → `/pipeline-review` → **Share** and pick your
teammates (or your whole workspace, if your admin allows). They get the skill
with your criteria and format baked in, so they don't repeat Steps 1-3.

## Going forward[](#going-forward)

### Now in your Cowork

Your processes

Sales plugin

Your tools

![](images/764fa5af07f936df.svg)Salesforce![](images/a3bfc5814bd6a3e2.svg)Google Sheets

Your workspace

Pipeline

Every deal is scored against your own criteria with the at-risk ones explained, so review time goes to decisions instead of preparation.

You did this for pipeline review. The same approach covers forecast roll-ups, renewal-risk checks, and account health — each one becomes a skill your team runs the same way.

[Next: Account tracking](https://academy.claude.com/use-cases/account-tracking)

* [1. Set up](#1-set-up)
* [2. The prompt](#2-the-prompt)
* [3. Make Cowork work for you](#3-make-cowork-work-for-you)
* [4. Make it repeatable](#4-make-it-repeatable)
* [5. Share with your teammates](#5-share-with-your-teammates)
* [Going forward](#going-forward)
