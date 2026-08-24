<!-- source: https://academy.claude.com/use-cases/performance-review-admin -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Performance review administrator

Your perf framework published as a skill every manager runs.

10 minHRClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-n3rpgf21.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-jww7pt0u.png)

## Set up

### Try a plugin

The Human Resources plugin ships with `/performance-review` and other people-ops skills as a starting point, already structured to gather input, score against competencies, and draft a review. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Human ResourcesStreamline people operations — recruiting, onboarding, performance reviews, compensation analysis, and policy guidance. Maintain compliance and keep your team running smoothly.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=human-resources)

`/performance-review`Structure a performance review with self-assessment, manager template, and calibration prep.

[Run](claude://cowork/new?q=%2Fperformance-review)

`/org-planning`Headcount planning, org design, and team structure optimization.

[Run](claude://cowork/new?q=%2Forg-planning)

Show all 9 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

Gusto

Pull the roster, reporting lines, and review-cycle dates so the packet is built for the right people.

[Connect](https://claude.ai/desktop/directory/gusto)

AsanaOptional

Read the review-cycle tasks and deadlines so nothing slips between self-review and calibration.

[Connect](https://claude.ai/desktop/directory/asana)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google Drive

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (your performance framework, the rating definitions, the review template, the cycle instructions you send managers) into one folder on your machine, then point Cowork at it. Cowork reads from it to build the skill and writes the skill file back to it. If you administer the cycle each half, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so the framework, instructions, and memory stay attached.

People / perf-cycle

performance-framework-2026.pdfJan 5, 2026512 KB

rating-definitions.docxJan 5, 202638 KB

review-template.docxJan 5, 202644 KB

manager-cycle-instructions.pdfMar 30, 2026126 KB

In Cowork’s chat bar:People / perf-cycle

## The prompt

### Copy this into Claude Cowork

Help me build the /performance-review skill for our managers. The skill should walk a manager through gathering input, scoring against our competencies, and drafting the review in our template. It should quote our rating definitions verbatim and never invent criteria that aren't in the framework.

People / perf-cycleOpen in Cowork

### Why this works

Prompt

**Ask for a reusable process.** "Help me build the /performance-review skill" makes the output the reusable process, so you author it once and every manager inherits the same steps.

Prompt

**Say what it must not make up.** "Quote our rating definitions verbatim and never invent criteria" keeps the skill anchored to the document in the folder, so calibration is comparing like with like.

Prompt

**List the steps in order.** Listing gather input, score, then draft tells Cowork the order your cycle instructions expect, so the skill matches the process you already trained managers on.

Source

**Let the working folder supply context.** The framework, rating definitions, and template sit in the working folder, so the skill is built from your current cycle documents and updates when you replace them.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /performance-review skill with my feedback.

People / perf-cycleOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it when the cycle opens

The cycle opens on the same date each half. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and Cowork reminds every manager to run `/performance-review` and refreshes the skill from the latest framework in the folder.

**/schedule** Every Monday at 9am, if a new cycle folder is in People/perf-cycle, refresh /performance-review from those files and post the kickoff note with instructions to the managers channel.

People / perf-cycleOpen in Cowork

Scheduled taskActive

Perf cycle kickoff

Refreshes `/performance-review` from People/perf-cycle and posts the manager kickoff note when each review cycle opens.

Every **Monday at 9:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/performance-review` now carries your framework, your rating language, and your template. Share it so every people manager runs the same process, and calibration compares reviews that were written against the same bar.

Share the skill

In Cowork, open **Skills** → `/performance-review` → **Share** and pick all people managers (or your whole workspace, if your admin allows). They get the skill with your framework and instructions baked in, so they don't repeat Steps 1-3.

## Going forward

### Now in your Cowork

Your processes

Human Resources plugin

Your tools

Gusto![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)Google Drive

Your workspace

People / perf-cycle

Every manager writes reviews against your framework, in your template, through one shared `/performance-review` skill — so the drafts that go to calibration are comparable.

You did this for performance reviews. The same approach works for promotion cases, onboarding plans, and improvement plans — each one becomes a skill in your team's plugin that managers run the same way.

[Next: Engagement survey to action plan](https://academy.claude.com/use-cases/engagement-survey-themes)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
