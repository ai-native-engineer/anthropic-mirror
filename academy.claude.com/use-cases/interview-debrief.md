<!-- source: https://academy.claude.com/use-cases/interview-debrief -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Interview debrief synthesis

Where the panel agreed, where they split, what to resolve.

10 minHRClaude Cowork

![](https://academy.claude.com/assets/v1/thumbnail.light-off27hqc.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-esddo3nx.png)

## 1. Set up

### Try a plugin

The Human Resources plugin ships with `/recruiting-pipeline` and other recruiting skills as a starting point, already structured to compare scorecards against a rubric and surface agreement and splits. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Human ResourcesStreamline people operations — recruiting, onboarding, performance reviews, compensation analysis, and policy guidance. Maintain compliance and keep your team running smoothly.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=human-resources)

`/recruiting-pipeline`Track and manage recruiting pipeline stages.

Show all 9 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/a3bfc5814bd6a3e2.svg)

Google Drive

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

![](images/b6bf6491858dcff4.svg)

Slack

[Connect](https://claude.ai/desktop/directory/slack)

![](images/3cb5db332ced9f49.svg)

Microsoft 365

[Connect](https://claude.ai/desktop/directory/microsoft-365)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a
working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (the scorecard export or pasted feedback, the role's competency rubric, the interview plan) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the debrief brief back to it. If you run debriefs every week, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from the role folder so the rubric and instructions stay attached.

Hiring / Senior-PM-Growth / debrief

scorecards-export-ARivera.csvApr 21, 202628 KB

competency-rubric.pdfFeb 10, 2026142 KB

interview-plan.docxFeb 10, 202636 KB

In Cowork’s chat bar:Hiring / Senior-PM-Growth / debrief

## 2. The prompt

### Copy this into Claude Cowork

Synthesize the interviewer scorecards into the debrief brief: where the panel converged, where they split, which signals are strong versus anecdotal, which competencies weren't covered, and the three questions to resolve in the debrief. Do not recommend hire or no-hire; that decision belongs to the panel.

Hiring / Senior-PM-Growth / debriefOpen in Cowork

### Why this works

Prompt

**State what not to do.** "Do not recommend hire or no-hire" is in the
prompt because Claude does not make hiring decisions; the brief organizes
the evidence so the people in the room can.

Prompt

**Ask it to weigh the evidence.** Asking which signals are "strong versus
anecdotal" forces the brief to weight a pattern across four scorecards
differently from one interviewer's aside.

Prompt

**Ask for what's missing.** "Which competencies weren't covered" checks the
scorecards against the rubric in the folder so the panel knows where it's
deciding without evidence.

Source

**Include your criteria with the data.** The scorecards, the competency
rubric, and the interview plan sit in the working folder, so convergence and
gaps are measured against the bar you set for this role.

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
/recruiting-pipeline skill with my feedback.

HiringOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## 4. Make it repeatable

### Run it when the last scorecard is in

The brief should be waiting before the debrief starts. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill runs every weekday morning. Cowork checks the hiring folder for candidates with all scorecards submitted and runs /recruiting-pipeline on each.

**/schedule** Weekdays at 9am. Check the hiring folder for candidates with all
scorecards in, run /recruiting-pipeline on each, and write the brief to
Hiring/<role>/debrief.

HiringOpen in Cowork

Scheduled taskActive

Debrief brief on scorecard complete

Runs `/recruiting-pipeline` each weekday morning on any candidate with all
scorecards in the hiring folder and writes the brief to that role's debrief
folder.

Every **Weekdays at 9am · checks the hiring folder for complete scorecard sets**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## 5. Share with your teammates

Your customized `/recruiting-pipeline` now carries your rubric, your convergence threshold, and the rule that the decision stays with humans. Share it so every hiring manager and recruiter walks into debrief with the same brief, and the panel spends its time on the open questions instead of re-reading scorecards.

Share the skill

In Cowork, open **Skills** → `/recruiting-pipeline` → **Share** and pick your
hiring managers and recruiters (or your whole workspace, if your admin
allows). They get the skill with your rubric and guardrails baked in, so they
don't repeat Steps 1-3.

## Going forward

### Now in your Cowork

Your processes

Human Resources plugin

Your tools

![](images/a3bfc5814bd6a3e2.svg)Google Drive

Your workspace

Hiring / debrief

Interviewer feedback is organized into one brief before the meeting, so the
panel starts from the same summary and uses the time to decide instead of
re-reading scorecards.

[Next: Offer process](https://academy.claude.com/use-cases/offer-process)

* [1. Set up](#1-set-up)
* [2. The prompt](#2-the-prompt)
* [3. Make Cowork work for you](#3-make-cowork-work-for-you)
* [4. Make it repeatable](#4-make-it-repeatable)
* [5. Share with your teammates](#5-share-with-your-teammates)
* [Going forward](#going-forward)
