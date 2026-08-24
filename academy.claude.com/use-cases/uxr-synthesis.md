<!-- source: https://academy.claude.com/use-cases/uxr-synthesis -->

Loading

## Set up

### Try a plugin

The Design plugin ships with `/research-synthesis` and other research and spec skills as a starting point, already structured to cluster observations and pull supporting quotes. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.



Design8 skills for research synthesis, spec drafting, brand enforcement, and prototype generation

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=design)

`/research-synthesis`Cluster interview transcripts into themed findings with supporting quotes

[Run](claude://cowork/new?q=%2Fresearch-synthesis)

`/design-handoff`Turn scattered threads and notes into a structured design spec

[Run](claude://cowork/new?q=%2Fdesign-handoff)

Show all 7 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23FCB400'%20d='M11.99%202.07%202.36%206.05c-.54.22-.53.98.01%201.19l9.67%203.83c.83.33%201.75.33%202.58%200l9.67-3.83c.54-.21.55-.97.01-1.19l-9.63-3.98a3.5%203.5%200%200%200-2.68%200Z'/%3e%3cpath%20fill='%2318BFFF'%20d='M12.92%2013.07v9.57c0%20.46.46.77.88.6l10.77-4.18a.64.64%200%200%200%20.41-.6V8.89c0-.46-.46-.77-.88-.6l-10.77%204.18a.64.64%200%200%200-.41.6Z'/%3e%3cpath%20fill='%23F82B60'%20d='M10.4%2013.56.98%2018.11c-.42.2-.98-.1-.98-.58V8.96c0-.17.09-.33.22-.44.14-.12.3-.19.48-.21.15-.02.3%200%20.44.06l9.24%203.66c.51.2.53.93.02%201.53Z'/%3e%3cpath%20fill='%23BA1E45'%20d='m10.4%2013.56-2.8%201.35L.22%208.52c.14-.12.3-.19.48-.21.15-.02.3%200%20.44.06l9.24%203.66c.51.2.53.93.02%201.53Z'/%3e%3c/svg%3e)

Airtable

Read the research tracker so findings, participants, and tags stay linked to the source sessions.

[Connect](https://claude.ai/desktop/directory/airtable)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google Drive

Read transcript docs from the study folder and write the findings doc back.

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3crect%20width='24'%20height='24'%20rx='5'%20fill='%23FFD02F'/%3e%3cpath%20fill='%23050038'%20d='M16.59%203.52h-2.65l2.2%203.87-4.85-3.87H8.64l2.43%204.84-5.08-4.84H3.34l2.7%206.16-2.7%2010.8h2.65l5.08-11.77-2.43%2011.77h2.65l4.85-12.74-2.2%2012.74h2.65l4.87-14.19z'/%3e%3c/svg%3e)

MiroOptional

Drop the themes onto a board as sticky clusters for the workshop debrief.

[Connect](https://claude.ai/desktop/directory/miro)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)



**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (the raw transcripts, your discussion guide, the participant roster) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the themed findings doc back to it. If you run studies regularly, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your guide, taxonomy, and memory stay attached.

Research / Onboarding-Study-Q2

P01-transcript.txtApr 21, 202638 KB

P02-transcript.txtApr 21, 202641 KB

discussion-guide.pdfApr 14, 202688 KB

In Cowork’s chat bar:Research / Onboarding-Study-Q2

## The prompt

### Copy this into Claude Cowork

Synthesize the interview transcripts into a research findings doc. Cluster the observations into 5-7 themes, name each plainly, support each with 2-3 verbatim quotes attributed to participant ID, and end with the open questions the team still needs to answer.



Research / Onboarding-Study-Q2Open in Cowork

### Why this works

Prompt

**Give a number range.** Five to seven forces real clustering, not a laundry list.

Prompt

**Ask for attributed evidence.** Evidence stays in the participant's words, attributed by ID.

Prompt

**End on open questions.** The doc tells the team what to study next.

Source

**Let the folder supply the context.** Every transcript is read; nothing depends on memory.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /research-synthesis skill with my feedback.



ResearchOpen in Cowork



**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Make it a live artifact

A findings doc goes stale once the next round of interviews comes in. Ask Cowork to publish the themes as a live artifact and the product team has one link that stays current — re-run the skill or schedule it to refresh.

Publish those themes as a live artifact for the product team. Keep a "what shifted since last round" note at the top.



Research / Onboarding-Study-Q2Open in Cowork

### Run it after every interview day

Sessions wrap, the synthesis should already be cooking. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and set the customized skill to run each evening, picking up any new transcripts in the study folder.

**/schedule** Weekdays at 6pm, check Research/Onboarding-Study-Q2 for new transcripts and re-run /research-synthesis, updating the findings doc and noting which themes moved.



ResearchOpen in Cowork

Scheduled taskActive

Rolling research synthesis

Each weekday at 6pm, checks the study folder for new transcripts, re-runs `/research-synthesis`, and updates the findings doc with a note on which themes moved.

Every **weekday at 6 pm · checks Research/Onboarding-Study-Q2 for new transcripts**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/research-synthesis` now carries your taxonomy, your quote format, and your readout structure. Share it so every researcher on the team clusters the same way, and PMs see a consistent findings doc no matter who ran the study.



Share the skill

In Cowork, open **Skills** → `/research-synthesis` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your taxonomy and format baked in, so they don't repeat Steps 1-3.

## What changes for the research team

Your interview transcripts are synthesized into a findings document with each theme named, evidenced, and attributed to participants — work you review and share instead of produce from scratch.

You did this for one interview study. The same approach covers usability sessions, diary studies, and survey open-ends — each one becomes a skill your team runs the same way.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/design-icon.svg)

Claude Design

Turn the findings into the on-brand readout deck

Open](https://claude.ai/design)

[Next: Design spec from scattered threads](https://academy.claude.com/use-cases/design-spec-from-threads)
