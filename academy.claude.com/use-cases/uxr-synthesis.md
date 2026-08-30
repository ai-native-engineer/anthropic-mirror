<!-- source: https://academy.claude.com/use-cases/uxr-synthesis -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Synthesize user interviews into findings

Themed findings and quotes from raw transcripts.

10 minDesignClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-e7bnk7fu.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-gpzn7vel.png)

## Set up[](#set-up)

### Try a plugin[](#try-a-plugin)

The Design plugin ships with `/research-synthesis` and other research and spec skills as a starting point, already structured to cluster observations and pull supporting quotes. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Design8 skills for research synthesis, spec drafting, brand enforcement, and prototype generation

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=design)

`/research-synthesis`Cluster interview transcripts into themed findings with supporting quotes

[Run](claude://cowork/new?q=%2Fresearch-synthesis)

`/design-handoff`Turn scattered threads and notes into a structured design spec

[Run](claude://cowork/new?q=%2Fdesign-handoff)

Show all 7 skills

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/7a4f4c146b11d7dc.svg)

Airtable

Read the research tracker so findings, participants, and tags stay linked to the source sessions.

[Connect](https://claude.ai/desktop/directory/airtable)

![](images/a3bfc5814bd6a3e2.svg)

Google Drive

Read transcript docs from the study folder and write the findings doc back.

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

![](images/f64a01189517b3e7.svg)

MiroOptional

Drop the themes onto a board as sticky clusters for the workshop debrief.

[Connect](https://claude.ai/desktop/directory/miro)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

Drag the files you'll use (the raw transcripts, your discussion guide, the participant roster) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the themed findings doc back to it. If you run studies regularly, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your guide, taxonomy, and memory stay attached.

Research / Onboarding-Study-Q2

P01-transcript.txtApr 21, 202638 KB

P02-transcript.txtApr 21, 202641 KB

discussion-guide.pdfApr 14, 202688 KB

In Cowork’s chat bar:Research / Onboarding-Study-Q2

## The prompt[](#the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Synthesize the interview transcripts into a research findings doc. Cluster the observations into 5-7 themes, name each plainly, support each with 2-3 verbatim quotes attributed to participant ID, and end with the open questions the team still needs to answer.

Research / Onboarding-Study-Q2Open in Cowork

### Why this works[](#why-this-works)

Prompt

**Give a number range.** Five to seven forces real clustering, not a laundry list.

Prompt

**Ask for attributed evidence.** Evidence stays in the participant's words, attributed by ID.

Prompt

**End on open questions.** The doc tells the team what to study next.

Source

**Let the folder supply the context.** Every transcript is read; nothing depends on memory.

### Get a better draft[](#get-a-better-draft)

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you[](#make-cowork-work-for-you)

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /research-synthesis skill with my feedback.

ResearchOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable[](#make-it-repeatable)

### Make it a live artifact[](#make-it-a-live-artifact)

A findings doc goes stale once the next round of interviews comes in. Ask Cowork to publish the themes as a live artifact and the product team has one link that stays current — re-run the skill or schedule it to refresh.

Publish those themes as a live artifact for the product team. Keep a "what shifted since last round" note at the top.

Research / Onboarding-Study-Q2Open in Cowork

### Run it after every interview day[](#run-it-after-every-interview-day)

Sessions wrap, the synthesis should already be cooking. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and set the customized skill to run each evening, picking up any new transcripts in the study folder.

**/schedule** Weekdays at 6pm, check Research/Onboarding-Study-Q2 for new transcripts and re-run /research-synthesis, updating the findings doc and noting which themes moved.

ResearchOpen in Cowork

Scheduled taskActive

Rolling research synthesis

Each weekday at 6pm, checks the study folder for new transcripts, re-runs `/research-synthesis`, and updates the findings doc with a note on which themes moved.

Every **weekday at 6 pm · checks Research/Onboarding-Study-Q2 for new transcripts**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates[](#share-with-your-teammates)

Your customized `/research-synthesis` now carries your taxonomy, your quote format, and your readout structure. Share it so every researcher on the team clusters the same way, and PMs see a consistent findings doc no matter who ran the study.

Share the skill

In Cowork, open **Skills** → `/research-synthesis` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your taxonomy and format baked in, so they don't repeat Steps 1-3.

## What changes for the research team[](#what-changes-for-the-research-team)

Your interview transcripts are synthesized into a findings document with each theme named, evidenced, and attributed to participants — work you review and share instead of produce from scratch.

You did this for one interview study. The same approach covers usability sessions, diary studies, and survey open-ends — each one becomes a skill your team runs the same way.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/design-icon.svg)

Claude Design

Turn the findings into the on-brand readout deck

Open](https://claude.ai/design)

[Next: Design spec from scattered threads](https://academy.claude.com/use-cases/design-spec-from-threads)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for the research team](#what-changes-for-the-research-team)
