<!-- source: https://academy.claude.com/use-cases/renewal-risk-audit -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Renewal risk audit

Every account renewing this quarter, scored on usage, sentiment, and open commitments.

15 minSalesClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-om42hzcu.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-mj4bkeih.png)

## 1. Set up

### Try a plugin

The Sales plugin ships with `/pipeline-review` and other account-health skills as a starting point, already structured to score a book of business and flag what's at risk. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

SalesProspect, craft outreach, and build deal strategy faster. Prep for calls, manage your pipeline, and write personalized messaging that moves deals forward.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=sales)

`/pipeline-review`Analyze pipeline health — prioritize deals, flag risks, get a weekly action plan.

[Run](claude://cowork/new?q=%2Fpipeline-review)

`/call-prep`Prepare for a sales call with account context, attendee research, and suggested agenda.

[Run](claude://cowork/new?q=%2Fcall-prep)

Show all 9 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/764fa5af07f936df.svg)

Salesforce

Pull the renewal book, ARR, owner, and any logged exec commitments straight from CRM.

Custom connector

Gong

Read the last QBR and recent call sentiment for each account.

Custom connector

![](images/fce598a81466f954.svg)

ZendeskOptional

Factor open and recently escalated support tickets into the risk score.

Custom connector

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (a CRM export of the renewal book, a product-usage CSV, last quarter's QBR notes) into one folder and point Cowork at it. Cowork reads from it and writes the risk audit and the artifact link back to it. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from your renewal folder so your scoring rubric and the exec-commitment tracker stay attached.

Renewals / FY26-Q3

q3-renewal-book.csvApr 27, 202648 KB

usage-90d-by-account.csvApr 27, 2026112 KB

exec-commitments-open.mdApr 20, 20264 KB

In Cowork’s chat bar:Renewals / FY26-Q3

## 2. The prompt

### Copy this into Claude Cowork

Audit my Q3 renewal book. For every account renewing in the next 90 days,
score renewal risk red/yellow/green based on product-usage
trend, recent sentiment, and open exec commitments. Explain
the signal that drove each score, and publish it as a
live artifact I can share with leadership.

Renewals / FY26-Q3Open in Cowork

### Why this works

Prompt

**Name the inputs to weigh.** Usage trend, last sentiment, open commitments
are the inputs that actually predict churn; saying so keeps the score
explainable.

Prompt

**Ask for the reason behind each score.** Asking for the reason behind each
score so each red includes why it's at risk — something you can act on.

Prompt

**Say how you'll share the output.** A live artifact means leadership opens
one link and it's current, not last Tuesday's spreadsheet.

Source

**Pull from the authoritative source.** The renewal date, ARR, and owner come
from Salesforce, so the audit and the forecast agree.

### Get a better draft

Practice

**Add your scoring rubric.** Drop your team's red/yellow/green definitions in
the project and the scores match how your forecast call already talks.

Practice

**Ask for next actions.** Add "for every red, suggest the next action and who
runs it" so the audit is also the save plan.

## 3. Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the
/pipeline-review skill with my feedback.

RenewalsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## 4. Make it repeatable

### Make it a live artifact

A spreadsheet is a snapshot. Ask Cowork to publish the audit as a live artifact and leadership opens one link that refreshes from CRM, with filters for segment, owner, and risk.

Publish that renewal-risk table as a live artifact for sales leadership,
filterable by segment and owner, and refresh it nightly from Salesforce.

Renewals / FY26-Q3Open in Cowork

### Run it on a schedule

Risk moves week to week. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill rescores the book and refreshes the artifact before your Monday forecast call.

**/schedule** Every Monday at 7am, rerun the renewal risk audit on the
current 90-day book, refresh the live artifact, and DM me any account that
moved to red since last week.

RenewalsOpen in Cowork

Scheduled taskActive

Weekly renewal risk audit

Rescores the 90-day renewal book on usage, sentiment, and open commitments,
refreshes the live artifact, and DMs new reds.

Every **Mondays at 7:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## 5. Share with your teammates

Your customized skill now carries your scoring rubric, your usage thresholds, and your save-play library. Share it so every CSM and AE in the segment runs the same audit and the forecast call argues about action, not definitions.

Share the skill

In Cowork, open **Skills** → your saved skill → **Share** and pick your
teammates (or your whole workspace, if your admin allows). They get the skill
with your instructions baked in, they don't repeat Steps 1-3.

## What changes for the renewal motion

Every account in your renewal window has a risk score, the signal behind it, and an owner, in one shared view that stays current. You work the at-risk list instead of building it.

You did this for one renewal cycle. The same approach covers expansion reviews, forecast risk, and QBR prep — each one a skill in your team's plugin, run the same way every time.

[Next: Account tracking and health](https://academy.claude.com/use-cases/account-tracking)

* [1. Set up](#1-set-up)
* [2. The prompt](#2-the-prompt)
* [3. Make Cowork work for you](#3-make-cowork-work-for-you)
* [4. Make it repeatable](#4-make-it-repeatable)
* [5. Share with your teammates](#5-share-with-your-teammates)
* [What changes for the renewal motion](#what-changes-for-the-renewal-motion)
