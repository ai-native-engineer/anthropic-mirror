<!-- source: https://academy.claude.com/use-cases/open-new-role -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Open a new role

A consistent role spec without the kickoff meeting.

10 minHRClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-lbgzsezl.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-crjbtqxa.png)

## 1. Set up[](#1-set-up)

### Try a plugin[](#try-a-plugin)

The Human Resources plugin ships with `/recruiting-pipeline` and other recruiting skills as a starting point, already structured to ask the intake questions in order and write to a spec template. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Human Resources9 skills for recruiting, onboarding, performance reviews, comp analysis, and org health reporting

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=human-resources)

`/recruiting-pipeline`Run the hiring-manager intake and produce a complete role specification

[Run](claude://cowork/new?q=%2Frecruiting-pipeline)

`/interview-prep`Draft the external job description from an approved role spec

[Run](claude://cowork/new?q=%2Finterview-prep)

Show all 9 skills

### Connect your tools[](#connect-your-tools)

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

### Set your working folder[](#set-your-working-folder)

Drag the files you'll use (your role spec template, the leveling guide, the team charter) into one folder on your machine, then point Cowork at it. Cowork reads from it during the intake and writes the finished spec back to it. If you open roles regularly, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from the parent Hiring folder so your templates and instructions stay attached.

Hiring / Senior-PM-Growth

role-spec-template.docxJan 9, 202642 KB

leveling-guide-2026.pdfFeb 2, 2026318 KB

growth-team-charter.docxMar 18, 202661 KB

In Cowork’s chat bar:Hiring / Senior-PM-Growth

## 2. The prompt[](#2-the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

I'm opening a new role on my team. Walk me through the intake: what this person will own, the must-have versus nice-to-have skills, the level and reporting line, and what good looks like at 90 days. Push back where I'm vague. Then write the role spec in our standard format and list what's still open for the recruiter.

Hiring / Senior-PM-GrowthOpen in Cowork

### Why this works[](#why-this-works)

Prompt

**Ask to be interviewed before it drafts.** "Walk me through the intake"
makes the conversation the deliverable, so the spec is built from your
answers rather than guessed from a job title.

Prompt

**Give permission to push back.** "Push back where I'm vague" gives Cowork
permission to do what a good recruiter does: notice when "strong
communicator" needs to become a testable signal.

Prompt

**List open questions separately.** Asking for "what's still open for the
recruiter" keeps undecided comp bands or location flex out of the spec and
on a short list for the live sync.

Source

**Put your templates in the working folder.** Your spec template and
leveling guide sit in the working folder, so "our standard format" and the
level definition mean the same thing for every manager who runs this.

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
/recruiting-pipeline skill with my feedback.

HiringOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## 4. Make it repeatable[](#4-make-it-repeatable)

### Run it whenever a headcount is approved[](#run-it-whenever-a-headcount-is-approved)

A new req gets approved, the intake should be waiting for the hiring manager. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill starts the conversation whenever a new role folder appears under Hiring.

**/schedule** Weekdays at 9am, check Hiring for any new subfolder, run
/recruiting-pipeline in each one, and save the intake transcript and finished
role spec there.

HiringOpen in Cowork

Scheduled taskActive

New role intake

Runs `/recruiting-pipeline` in every new subfolder under Hiring and writes the
intake transcript and finished spec to that role's folder.

Every **Weekdays at 9am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## 5. Share with your teammates[](#5-share-with-your-teammates)

Your customized `/recruiting-pipeline` now carries your intake questions, your leveling guide, and your spec template. Share it so every hiring manager runs the same intake, and recruiting receives a complete spec before the first call instead of after it.

Share the skill

In Cowork, open **Skills** → `/recruiting-pipeline` → **Share** and pick your
hiring managers (or your whole workspace, if your admin allows). They get the
skill with your intake and templates baked in, so they don't repeat Steps 1-3.

## Going forward[](#going-forward)

### Now in your Cowork

Your processes

Human Resources plugin

Your tools

![](images/a3bfc5814bd6a3e2.svg)Google Drive

Your workspace

Hiring

Every role you open gets the same structured intake and a complete spec in your standard format, with open questions listed for the recruiter — ready before the first call.

[Next: Interview debrief synthesis](https://academy.claude.com/use-cases/interview-debrief)

* [1. Set up](#1-set-up)
* [2. The prompt](#2-the-prompt)
* [3. Make Cowork work for you](#3-make-cowork-work-for-you)
* [4. Make it repeatable](#4-make-it-repeatable)
* [5. Share with your teammates](#5-share-with-your-teammates)
* [Going forward](#going-forward)
