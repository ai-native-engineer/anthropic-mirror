<!-- source: https://academy.claude.com/use-cases/engagement-survey-themes -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Engagement survey to action plan

Top themes, supporting quotes, and a 30-day action plan.

10 minHRClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-h6intrnq.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-ijzy6x76.png)

## Set up

### Try a plugin

The Human Resources plugin ships with `/org-planning` and other org-health skills as a starting point, already structured to cluster open text, weight by frequency, and draft an action plan. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Human ResourcesStreamline people operations — recruiting, onboarding, performance reviews, compensation analysis, and policy guidance. Maintain compliance and keep your team running smoothly.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=human-resources)

`/org-planning`Headcount planning, org design, and team structure optimization.

[Run](claude://cowork/new?q=%2Forg-planning)

`/people-report`Generate headcount, attrition, diversity, or org health reports.

[Run](claude://cowork/new?q=%2Fpeople-report)

Show all 9 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.951%209.85a1.47%201.47%200%201%201-2.94%200%201.47%201.47%200%200%201%201.47-1.471h1.47V9.85Zm.735%200a1.47%201.47%200%201%201%202.94%200v3.679a1.47%201.47%200%201%201-2.94%200V9.85Z'%20fill='%23E01E5A'/%3e%3cpath%20d='M6.157%203.943a1.47%201.47%200%201%201%200-2.943%201.47%201.47%200%200%201%201.47%201.471v1.472h-1.47Zm0%20.746a1.47%201.47%200%201%201%200%202.943H2.47a1.47%201.47%200%201%201%200-2.943h3.687Z'%20fill='%2336C5F0'/%3e%3cpath%20d='M12.049%206.16a1.47%201.47%200%201%201%202.94%200%201.47%201.47%200%200%201-1.47%201.472h-1.47V6.16Zm-.736%200a1.47%201.47%200%201%201-2.94%200V2.471a1.47%201.47%200%201%201%202.94%200V6.16Z'%20fill='%232EB67D'/%3e%3cpath%20d='M9.843%2012.057a1.47%201.47%200%201%201%200%202.943%201.47%201.47%200%200%201-1.47-1.471v-1.472h1.47Zm0-.735a1.47%201.47%200%201%201%200-2.943h3.687a1.47%201.47%200%201%201%200%202.943H9.843Z'%20fill='%23ECB22E'/%3e%3c/svg%3e)

SlackOptional

Read the open-ended responses dropped in the survey channel so nothing handwritten gets missed.

[Connect](https://claude.ai/desktop/directory/slack)

Gusto

Pull headcount and team structure so themes break down by org, tenure, and manager.

[Connect](https://claude.ai/desktop/directory/gusto)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google Drive

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (the raw survey CSV, the org roster for segmentation, last cycle's brief) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the People brief and action plan back to it. If you run engagement each quarter, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from the parent engagement folder so prior cycles and your anonymization rules stay attached.

People / engagement-Q2

engagement-q2-export.csvApr 20, 2026612 KB

org-roster-apr.csvApr 1, 202634 KB

q1-people-brief.docxJan 28, 202652 KB

In Cowork’s chat bar:People / engagement-Q2

## The prompt

### Copy this into Claude Cowork

Theme the open-text survey responses, segment by team and tenure where the data allows, and separate loud-minority comments from broad signal. Output a one-page People brief: the top three themes, two or three supporting quotes per theme, and a draft 30-day action plan for each. Never attribute a quote to an individual.

People / engagement-Q2Open in Cowork

### Why this works

Prompt

**State the privacy rule explicitly.** "Never attribute a quote to an individual" is a standing instruction in the skill; Cowork strips names, roles, and small-team identifiers so the brief is safe to share with leadership.

Prompt

**Say how to weight the responses.** "Loud-minority from broad signal" tells Cowork to weight a theme by how many distinct respondents raised it, not how forcefully a few wrote about it.

Prompt

**Ask for an action per theme.** Asking for "a draft 30-day action plan for each" turns the readout into something a leader can commit to in the meeting, not a finding to file.

Source

**Let the working folder supply context.** The raw export and the org roster sit in the working folder, so team and tenure cuts come from your real structure and the brief is saved next to the source data.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /org-planning skill with my feedback.

People / engagement-Q2Open in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it every survey cycle

Surveys close on the same cadence each quarter. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill runs against the newest export and writes the brief and action plan to that quarter's folder.

**/schedule** Every Monday at 9am, if a new export is in People/engagement-<quarter>, run /org-planning against it and write the People brief and action plan to that folder.

PeopleOpen in Cowork

Scheduled taskActive

Quarterly engagement brief

Runs `/org-planning` on the newest export in People/engagement and writes the one-page brief and 30-day action plans to that quarter's folder.

Every **Monday at 9:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/org-planning` now carries your anonymization rules, your segment thresholds, and your action-plan format. Share it so HRBPs across the org produce the same shape of brief, and leaders see consistent readouts whether the survey ran in Lattice, CultureAmp, or a Google Form.

Share the skill

In Cowork, open **Skills** → `/org-planning` → **Share** and pick your People partners (or your whole workspace, if your admin allows). They get the skill with your privacy rules and format baked in, so they don't repeat Steps 1-3.

## Going forward

### Now in your Cowork

Your processes

Human Resources plugin

Your tools

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)Google Drive

Your workspace

People / engagement

Open-text survey responses are themed, segmented, and anonymized into a one-page brief with a draft action plan for each theme — ready to act on instead of compile.

You did this for one engagement survey. The same approach works for exit-interview notes, onboarding feedback, and pulse-survey comments — each one becomes a skill your team runs the same way.

[Next: Performance review administrator](https://academy.claude.com/use-cases/performance-review-admin)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
