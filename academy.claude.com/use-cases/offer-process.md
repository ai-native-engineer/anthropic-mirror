<!-- source: https://academy.claude.com/use-cases/offer-process -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Offer process

Candidate email, offer fields, and a screenshare-ready deck.

10 minHRClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-jslgxynt.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-fx1l2f4o.png)

## 1. Set up[](#1-set-up)

### Try a plugin[](#try-a-plugin)

The Human Resources plugin ships with `/draft-offer` and other recruiting skills as a starting point, already structured to fill an offer template, draft the email, and lay out the call deck. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Human Resources9 skills for recruiting, onboarding, performance reviews, comp analysis, and org health reporting

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=human-resources)

`/draft-offer`Assemble the offer email, filled offer fields, and screenshare deck for a finalist

[Run](claude://cowork/new?q=%2Fdraft-offer)

`/comp-analysis`Benchmark a proposed offer against your comp bands and recent closes

[Run](claude://cowork/new?q=%2Fcomp-analysis)

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

![](images/0b7839904dd03a68.svg)

DocuSignOptional

[Connect](https://claude.ai/desktop/directory/docusign)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

Drag the files you'll use (the candidate summary, your offer letter template, the comp approval, the benefits one-pager) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the filled offer, the email draft, and the HTML deck back to it. If you run offers regularly, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from the role's offers folder so your templates and tone stay attached.

Hiring / Senior-PM-Growth / offers

offer-letter-template.docxJan 12, 202654 KB

candidate-summary-ARivera.pdfApr 22, 202688 KB

comp-approval.xlsxApr 23, 202622 KB

benefits-overview-2026.pdfFeb 3, 2026410 KB

In Cowork’s chat bar:Hiring / Senior-PM-Growth / offers

## 2. The prompt[](#2-the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Put together the offer package for our finalist. Fill out the offer fields for my review, draft a warm email to the candidate that sets up the call, and build a short HTML presentation I can screenshare on the offer call covering the role, the numbers, and why we're excited about them.

Hiring / Senior-PM-Growth / offersOpen in Cowork

### Why this works[](#why-this-works)

Prompt

**Ask for related outputs together.** Naming the email, the filled offer, and the deck in one prompt means the three artifacts agree on title, numbers, and start date because they were written together.

Prompt

**Say the output is for review.** "Fill out the offer fields for my review" makes the output a draft you approve, so nothing goes to the candidate or to signature until a person has checked the numbers.

Prompt

**Ask for personalized content.** "Why we're excited about them" pulls specifics from the candidate summary into the screenshare, so the call opens on what they bring rather than a generic pitch.

Source

**Put your source files in the folder.** The offer template, the approved numbers, and the benefits one-pager sit in the working folder, so the filled offer and the deck quote your real terms and land back next to them.

### Get a better draft[](#get-a-better-draft)

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## 3. Make Cowork work for you[](#3-make-cowork-work-for-you)

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /draft-offer skill with my feedback.

HiringOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## 4. Make it repeatable[](#4-make-it-repeatable)

### Run it on a schedule[](#run-it-on-a-schedule)

Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill runs every weekday morning. It checks the hiring folder for candidates who moved to Offer overnight so the package is ready before the recruiter opens it.

**/schedule** Weekdays at 9am. Check the hiring folder for candidates who moved to Offer overnight, run /draft-offer for each, and write the email draft, filled offer, and HTML deck to Hiring/<role>/offers.

HiringOpen in Cowork

Scheduled taskActive

Offer package on stage change

Runs `/draft-offer` each weekday morning for any candidate who moved to Offer overnight and writes the email, filled offer, and deck to the role's offers folder.

Every **Weekdays at 9am · checks the hiring folder for new Offer-stage candidates**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## 5. Share with your teammates[](#5-share-with-your-teammates)

Your customized `/draft-offer` now carries your offer template, your email tone, and your branded deck layout. Share it so every recruiter and hiring manager produces the same quality of offer artifact, and candidates get a consistent experience no matter which team is closing them.

Share the skill

In Cowork, open **Skills** → `/draft-offer` → **Share** and pick your recruiting team (or your whole workspace, if your admin allows). They get the skill with your templates and guardrails baked in, so they don't repeat Steps 1-3.

## Going forward[](#going-forward)

### Now in your Cowork

Your processes

Human Resources plugin

Your tools

![](images/a3bfc5814bd6a3e2.svg)Google Drive![](images/0b7839904dd03a68.svg)DocuSign

Your workspace

Hiring / offers

You have a complete, consistent offer package for each finalist — drafted from your approved terms and templates, ready for your review before anything goes to the candidate.

[Next: Onboarding plan](https://academy.claude.com/use-cases/open-new-role)

* [1. Set up](#1-set-up)
* [2. The prompt](#2-the-prompt)
* [3. Make Cowork work for you](#3-make-cowork-work-for-you)
* [4. Make it repeatable](#4-make-it-repeatable)
* [5. Share with your teammates](#5-share-with-your-teammates)
* [Going forward](#going-forward)
