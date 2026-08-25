<!-- source: https://academy.claude.com/use-cases/competitor-comparison -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Build the competitive comparison doc

Cowork reads competitor materials against your positioning, writes the win/lose/draw, and outputs a sales deck and Excel matrix.

10 minMarketingClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-lfte5epc.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-ljg8b3c8.png)

## Set up

### Try a plugin

The Marketing plugin ships with `/competitor-compare` as a starting point, already structured to read a competitor's public materials against your positioning and write the win/lose/draw breakdown. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Marketing8 skills to draft content, plan campaigns, hold brand voice, and report on performance

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=marketing)

`/competitive-brief`Read competitor materials against your positioning and write the win/lose/draw deck

[Run](claude://cowork/new?q=%2Fcompetitive-brief)

`/campaign-plan`Draft the campaign brief from a goal and last quarter's results

[Run](claude://cowork/new?q=%2Fcampaign-plan)

Show all 7 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/a3bfc5814bd6a3e2.svg)

Google Drive

Your positioning doc, messaging framework, and the last comparison deck so the new one matches.

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

![](images/b6bf6491858dcff4.svg)

Slack

The #competitive channel where the question came in — and where the answer goes back.

[Connect](https://claude.ai/desktop/directory/slack)

HubSpotOptional

Win/loss notes and deal context so the comparison reflects what actually closes.

[Connect](https://claude.ai/desktop/directory/hubspot)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Paste the competitor's URL and drag your positioning doc into the chat, then start with the prompt.

### Set your working folder

Drag the files you'll use (the competitor's pricing page PDF, their datasheet, your positioning doc, last quarter's comparison deck) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the deck and the Excel matrix back to it. If you track this competitor every quarter, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so the sources and instructions stay attached.

Competitive / Acme

acme-pricing-page.pdfApr 28, 2026312 KB

acme-datasheet.pdfApr 28, 20261.1 MB

our-positioning.docxApr 12, 202688 KB

comparison-q1.pptxJan 30, 20262.3 MB

In Cowork’s chat bar:Competitive / Acme

## The prompt

### Copy this into Claude Cowork

Here's the competitor's site, pricing page, and recent announcements, plus our positioning doc. Build a structured comparison: where we win, where they win, and where it's a draw. Output a PowerPoint deck for sales and an Excel workbook with the feature-by-feature matrix.

Competitive / AcmeOpen in Cowork

### Why this works

Prompt

**Ask for a verdict, not a list.** "Where we win, where they win, where it's a draw" forces a position on every row instead of a neutral feature dump.

Prompt

**Name both output formats.** The deck is what sales presents. The Excel matrix is what they filter when a prospect asks about one specific feature.

Source

**Anchor to your positioning.** Including your own positioning doc means the "where we win" rows use your language, not the competitor's framing.

Source

**Use their public materials.** Pricing pages and datasheets are what prospects see — comparing against those keeps the deck defensible in front of a customer.

### Get a better draft

Practice

**Add the audience.** Say "for an enterprise security buyer" or "for a mid-market ops lead" and the win/lose framing shifts to what that buyer cares about.

Practice

**Add your last deck as the template.** Drop last quarter's comparison into the folder and Cowork matches the slide structure and tone.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /competitor-compare skill with my feedback.

Competitive / AcmeOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it on a schedule

Competitors ship and reprice without telling you. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill re-reads their public pages, refreshes the matrix, and flags what changed since last time.

**/schedule** First Monday of each month, run /competitor-compare against the sources in this folder, refresh the Excel matrix, and post a summary of what changed to #competitive.

Competitive / AcmeOpen in Cowork

Scheduled taskActive

Monthly competitor refresh

Runs `/competitor-compare` against the sources in this folder, refreshes the Excel matrix, and posts a summary of what changed to #competitive.

Every **first Monday of the month**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/competitor-compare` now carries your positioning, your deck template, and your matrix columns. Share it so PMM, sales enablement, and the field answer the same competitor question the same way.

Share the skill

In Cowork, open **Skills** → `/competitor-compare` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your positioning and templates baked in, so they don't repeat Steps 1-3.

## Going forward

### Now in your Cowork

Your processes

Marketing plugin

Your tools

![](images/a3bfc5814bd6a3e2.svg)Google Drive![](images/b6bf6491858dcff4.svg)SlackHubSpot

Your workspace

Competitive / Acme

`/competitor-compare` turns the next "how do we stack up against X" into a deck and a matrix in one pass — grounded in your positioning, not theirs.

You did this for one competitor. The same approach covers your whole competitive set — one folder per name, one scheduled refresh, one consistent answer for the field.

[Next: Build a campaign brief](https://academy.claude.com/use-cases/campaign-brief)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
