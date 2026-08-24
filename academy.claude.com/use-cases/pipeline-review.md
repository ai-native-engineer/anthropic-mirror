<!-- source: https://academy.claude.com/use-cases/pipeline-review -->

Loading

## 1. Set up

### Try a plugin

The Sales plugin ships with `/pipeline-review` and other forecast-hygiene skills as a starting point, already structured to score opps and call out risk. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.



SalesProspect, craft outreach, and build deal strategy faster. Prep for calls, manage your pipeline, and write personalized messaging that moves deals forward.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=sales)

`/pipeline-review`Analyze pipeline health — prioritize deals, flag risks, get a weekly action plan.

[Run](claude://cowork/new?q=%2Fpipeline-review)

`/call-prep`Prepare for a sales call with account context, attendee research, and suggested agenda.

[Run](claude://cowork/new?q=%2Fcall-prep)

Show all 9 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%2300A1E0'%20d='M10.01%205.56a4.18%204.18%200%200%201%203.02-1.3c1.58%200%202.96.88%203.7%202.19a5.12%205.12%200%200%201%202.1-.45%205.18%205.18%200%200%201%200%2010.36c-.37%200-.73-.04-1.07-.11a3.77%203.77%200%200%201-4.94%201.55%204.3%204.3%200%200%201-7.99-.2%203.98%203.98%200%200%201-.82.09%203.97%203.97%200%200%201-1.96-7.43%204.57%204.57%200%200%201%207.96-4.7'/%3e%3c/svg%3e)

Salesforce

Custom connector

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google Drive

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)



**Want to try this task before setting anything up?** Add your files to a
working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (this week's pipeline export, last week's review doc, your stage definitions) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the scored sheet and review doc back to it. If you run pipeline weekly, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your stage criteria, instructions, and memory stay attached.

Pipeline / 2026-W17

pipeline-export-W17.xlsxApr 26, 202688 KB

review-doc-W16.docxApr 20, 202631 KB

stage-exit-criteria.pdfJan 6, 202652 KB

In Cowork’s chat bar:Pipeline / 2026-W17

## 2. The prompt

### Copy this into Claude Cowork

Score each open opp in this week's pipeline on stage hygiene, whether there's a real next step, and how long it's sat in stage. Flag the at-risk deals and say why in one line each, then write the manager-ready review doc for our Monday pipeline meeting.



Pipeline / 2026-W17Open in Cowork

### Why this works

Prompt

**Spell out your scoring criteria.** "Hygiene, real next step, age in
stage" gives Cowork the rubric your manager uses, so the score means
something in the meeting instead of being a generic health number.

Prompt

**Set a length limit per item.** "Say why in one line each" keeps the
at-risk section scannable, so the meeting time goes to the deals that need
it rather than reading paragraphs.

Prompt

**Ask for the write-up alongside the data.** "Manager-ready review doc"
tells Cowork to write the narrative around the scores, the part you'd
otherwise type up Sunday night.

Source

**Put your reference docs in the folder.** Your stage exit criteria and last
week's review doc sit in the working folder, so hygiene is scored against
your definitions and the doc follows the format your manager already expects.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and
Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about"
so you know where to look first when you review the draft.

## 3. Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the
/pipeline-review skill with my feedback.



PipelineOpen in Cowork



**Tip:** tell Claude to edit the skill for you.

## 4. Make it repeatable

### Run it before the Monday meeting

The review should be waiting before the meeting, not built during it. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill scores the pipeline and writes the doc every Monday morning.

**/schedule** Every Monday at 8am, run /pipeline-review against the current
Salesforce pipeline and write the scored sheet and review doc to a new folder
under Pipeline named for the week.



PipelineOpen in Cowork

Scheduled taskActive

Monday pipeline review

Runs `/pipeline-review` against the current Salesforce pipeline and writes
the scored sheet and review doc to a weekly folder.

Every **Monday at 8:00 AM**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## 5. Share with your teammates

Your customized `/pipeline-review` now carries your stage criteria, your at-risk thresholds, and your review doc format. Share it so every rep scores their own pipeline the same way, and the team meeting reads from one consistent doc per rep.



Share the skill

In Cowork, open **Skills** → `/pipeline-review` → **Share** and pick your
teammates (or your whole workspace, if your admin allows). They get the skill
with your criteria and format baked in, so they don't repeat Steps 1-3.

## Going forward

### Now in your Cowork

Your processes

Sales plugin

Your tools

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%2300A1E0'%20d='M10.01%205.56a4.18%204.18%200%200%201%203.02-1.3c1.58%200%202.96.88%203.7%202.19a5.12%205.12%200%200%201%202.1-.45%205.18%205.18%200%200%201%200%2010.36c-.37%200-.73-.04-1.07-.11a3.77%203.77%200%200%201-4.94%201.55%204.3%204.3%200%200%201-7.99-.2%203.98%203.98%200%200%201-.82.09%203.97%203.97%200%200%201-1.96-7.43%204.57%204.57%200%200%201%207.96-4.7'/%3e%3c/svg%3e)Salesforce![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)Google Sheets

Your workspace

Pipeline

Every deal is scored against your own criteria with the at-risk ones explained, so review time goes to decisions instead of preparation.

You did this for pipeline review. The same approach covers forecast roll-ups, renewal-risk checks, and account health — each one becomes a skill your team runs the same way.

[Next: Account tracking](https://academy.claude.com/use-cases/account-tracking)
