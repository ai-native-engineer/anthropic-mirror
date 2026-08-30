<!-- source: https://academy.claude.com/use-cases/ad-performance-recap -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Recap your ad performance

A performance summary, recommendation on what to improve, and a deck shared in Slack.

10 minMarketingClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-em4laj46.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-lnkhp3d2.png)

## Set up[](#set-up)

### Try a plugin[](#try-a-plugin)

The Marketing plugin ships with `/performance-report` and other performance-reporting skills as a starting point, already structured to compare spend, reach, and conversion across platforms and write the readout. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

MarketingCreate content, plan campaigns, and analyze performance across marketing channels. Maintain brand voice consistency, track competitors, and report on what's working.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=marketing)

`/performance-report`Build a marketing performance report with key metrics, trend analysis, wins and misses, and prioritized recommendations.

[Run](claude://cowork/new?q=%2Fperformance-report)

`/campaign-plan`Generate a full campaign brief with objectives, audience, messaging, channel strategy, content calendar, and success metrics.

[Run](claude://cowork/new?q=%2Fcampaign-plan)

Show all 7 skills

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

HubSpot

Pull campaign performance and attribution so the recap ties spend to pipeline.

[Connect](https://claude.ai/desktop/directory/hubspot)

BigQueryOptional

Query ad-platform and GA4 data from your warehouse instead of pulling exports.

[Connect](https://claude.ai/desktop/directory/bigquery)

![](images/b6bf6491858dcff4.svg)

Slack

[Connect](https://claude.ai/desktop/directory/slack)

![](images/a3bfc5814bd6a3e2.svg)

Google Drive

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

Drag the files you'll use (the platform exports, the campaign brief, last period's recap deck) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the analysis, recap deck, and live artifact link back to it. If you'll report on this campaign every week, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so the data sources, instructions, and scheduled runs stay attached.

Campaigns / Spring-Launch / performance

google-ads-export.csvApr 26, 2026412 KB

meta-ads-export.csvApr 26, 2026288 KB

ga4-conversions.csvApr 26, 202696 KB

recap-deck-wk16.pptxApr 19, 20261.4 MB

In Cowork’s chat bar:Campaigns / Spring-Launch / performance

## The prompt[](#the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Analyze this campaign's ad performance and build the recap deck: what worked, what didn't, and what we change next time. Post a digest to the team Slack with the top three movers, and create a live shared artifact that stays updated from the underlying data.

Campaigns / Spring-Launch / performanceOpen in Cowork

### Why this works[](#why-this-works)

Prompt

**Ask for what to do next, with the data behind it.** "What worked, what didn't, and what we change" means the analysis ends in a recommendation, not a table.

Prompt

**Set a length limit.** "Top three movers" keeps the Slack post short enough that the team actually reads it.

Prompt

**Ask for an output that stays current.** A live shared artifact gives stakeholders one link with current numbers — no re-sending decks when data updates.

Source

**Put the sources in one place.** Google, Meta, and GA4 exports sit in one working folder, so the analysis joins spend to conversion across platforms without you stitching CSVs.

### Get a better draft[](#get-a-better-draft)

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask for options.** Add "draft three versions with different angles" and pick the one that works best.

## Make Cowork work for you[](#make-cowork-work-for-you)

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /performance-report skill with my feedback.

Campaigns / Spring-Launch / performanceOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable[](#make-it-repeatable)

### Run it on a schedule[](#run-it-on-a-schedule)

The performance recap is due the same morning every week. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill pulls fresh data, refreshes the live artifact, rebuilds the deck, and posts the digest automatically.

**/schedule** Every Monday at 8am, run /performance-report against the connected ad platforms for this campaign, refresh the live artifact, write the recap deck to the performance folder, and post the top-three digest to #paid-media.

Campaigns / Spring-Launch / performanceOpen in Cowork

Scheduled taskActive

Weekly ad performance recap

Runs `/performance-report` against the connected ad platforms, refreshes the live artifact, writes the recap deck to the performance folder, and posts the top-three digest to #paid-media.

Every **Monday at 8am, weekly**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates[](#share-with-your-teammates)

Your customized `/performance-report` now carries your KPI definitions, your deck template, and your live-artifact layout. Share it so every campaign owner reports the same way, and leadership reads one consistent recap no matter which program it came from.

Share the skill

In Cowork, open **Skills** → `/performance-report` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your KPIs and templates baked in, so they don't repeat Steps 1-3.

## Going forward[](#going-forward)

### Now in your Cowork

Your processes

Marketing plugin

Your tools

HubSpotGoogle Cloud BigQuery![](images/b6bf6491858dcff4.svg)Slack![](images/a3bfc5814bd6a3e2.svg)Google Drive

Your workspace

Campaigns / performance

`/performance-report` gives you a consistent recap each period: ad performance across platforms, measured against your KPI definitions, with what worked and what to change ready to share.

You did this for one campaign. The same approach covers email performance, organic social, and landing-page conversion — each one becomes a skill your team runs the same way.

[Next: Build a campaign brief](https://academy.claude.com/use-cases/campaign-brief)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
