<!-- source: https://academy.claude.com/use-cases/eng-performance-reviews -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Draft your reports' performance reviews

A grounded review draft with linked evidence, per report.

10 minEngineeringClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-llbosc4e.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-jig8shre.png)

## Set up

### Try a plugin

The Engineering plugin ships with `/code-review` as a starting point, already structured to gather a report's shipped work and frame it against a career ladder. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Engineering9 skills for postmortems, design docs, on-call handoffs, and cost reviews

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=engineering)

`/code-review`Gather a report's shipped work and draft the review against your career framework

[Run](claude://cowork/new?q=%2Fcode-review)

`/standup`Compile a report's PRs, reviews, and incidents into an evidence packet

[Run](claude://cowork/new?q=%2Fstandup)

Show all 10 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/92b68e492ad6094d.svg)

GitHub

Pull each report's merged PRs, reviews given, and incidents responded to over the period.

[Connect](https://claude.ai/desktop/directory/github)

![](images/b6bf6491858dcff4.svg)

Slack

Surface the threads where they led, unblocked a teammate, or drove a decision.

[Connect](https://claude.ai/desktop/directory/slack)

![](images/d9bcb0bb9b2b1fff.svg)

LinearOptional

List the projects and epics they shipped and the cycle outcomes they owned.

[Connect](https://claude.ai/desktop/directory/linear)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (your career framework, the review template, last cycle's reviews, your team roster) into one folder and point Cowork at it. Cowork reads the framework from there and writes one draft per report back to it. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your framework and your writing voice stay attached.

Reviews / 2026-Q1

eng-career-framework.pdfJan 12, 2026220 KB

review-template.mdJan 12, 20262 KB

team-roster.mdApr 1, 20261 KB

In Cowork’s chat bar:Reviews / 2026-Q1

## The prompt

### Copy this into Claude Cowork

I'm writing quarterly reviews for my reports. For each engineer in my team list, draft the review in our framework with evidence linked for every claim, drawing on their work this quarter and their last review's growth areas. Flag where I need to add my own judgment; do not write the rating.

Reviews / 2026-Q1Open in Cowork

### Why this works

Prompt

**Require evidence for every claim.** The draft is defensible in calibration; nothing rests on vibes.

Prompt

**Include prior context to show progress.** The review tracks progress, not just a snapshot of this quarter.

Prompt

**Keep judgment calls yours.** Saying the rating is yours to make tells Claude where its job ends. The draft gathers and organizes the evidence, then stops.

Source

**Give it your review framework.** Every draft maps to your levels and your competencies, not a generic ladder.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /code-review skill with my feedback.

ReviewsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it at the start of every cycle

The evidence packet should be ready before review season opens. Type `/schedule` or open **Scheduled** in the Cowork sidebar, and the customized skill builds the drafts as soon as the quarter folder appears.

**/schedule** Every Monday at 9am, if a new quarter folder exists under Reviews, run /code-review for everyone in team-roster.md and write each draft to Reviews/<quarter>/<name>.md.

ReviewsOpen in Cowork

Scheduled taskActive

Quarterly review drafts

When a new quarter folder appears, runs `/code-review` for each report against GitHub, Linear, and Slack and writes evidence-linked drafts to the cycle folder.

Every **Monday at 9:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/code-review` now carries your career framework, your evidence sources, and your tone. Share it so every manager in the org drafts against the same ladder, and calibration compares apples to apples.

Share the skill

In Cowork, open **Skills** → `/code-review` → **Share** and pick your peer managers (or your whole workspace, if your admin allows). They get the skill with your framework baked in, so they don't repeat Steps 1-3.

## What changes for review season

Each report has a review draft with evidence linked for every claim and the places that need your judgment clearly marked. Your time goes to the assessment and the conversation, not to gathering what they shipped.

You did this for one review cycle. The same approach covers promotion packets, calibration prep, and peer-feedback summaries — each one becomes a skill your team runs the same way.

[Next: Draft the incident postmortem](https://academy.claude.com/use-cases/incident-postmortem)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for review season](#what-changes-for-review-season)
