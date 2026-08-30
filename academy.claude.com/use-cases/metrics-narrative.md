<!-- source: https://academy.claude.com/use-cases/metrics-narrative -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Metrics deep-dive to narrative

What moved, why, and which ship caused it.

10 minProductClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-gl4mvsbr.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-f2aunmbb.png)

## Set up[](#set-up)

### Try a plugin[](#try-a-plugin)

The Product Management plugin ships with `/metrics-review` and other analysis skills as a starting point, already structured to find the anomaly, segment to the driver, and write the story. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Product ManagementWrite feature specs, plan roadmaps, and synthesize user research faster. Keep stakeholders updated and stay ahead of the competitive landscape.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=product-management)

`/metrics-review`Review and analyze product metrics with trend analysis and actionable insights.

[Run](claude://cowork/new?q=%2Fmetrics-review)

`/stakeholder-update`Generate a stakeholder update tailored to audience and cadence.

[Run](claude://cowork/new?q=%2Fstakeholder-update)

Show all 8 skills

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

Amplitude

[Connect](https://claude.ai/desktop/directory/amplitude)

Databricks

Query the metrics tables directly so the narrative cites the same numbers as the dashboards.

[Connect](https://claude.ai/desktop/directory/databricks)

![](images/d9bcb0bb9b2b1fff.svg)

Linear

[Connect](https://claude.ai/desktop/directory/linear)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

Drag the files you'll use (the Amplitude or Mixpanel CSV export, last week's narrative for comparison, the changelog if it's a flat file) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the narrative and chart images back to it. If you write this every week, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your metric definitions, instructions, and memory stay attached.

Product / metrics / wk17

amplitude-activation-funnel-wk17.csvApr 24, 20262.4 MB

looker-retention-by-plan.csvApr 24, 2026880 KB

changelog-apr.mdApr 23, 20269 KB

narrative-wk16.mdOptionalApr 17, 20266 KB

In Cowork’s chat bar:Product / metrics / wk17

## The prompt[](#the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Find the anomaly in this week's activation funnel. Segment by plan, platform, and signup source until you've isolated the driver, check it against what shipped in the same window, and write the "what happened and why" narrative with the two charts that prove it.

Product / metrics / wk17Open in Cowork

### Why this works[](#why-this-works)

Prompt

**Ask for the evidence behind each claim.** Starting with "find the anomaly" lets Cowork scan the whole funnel for the step that actually moved instead of anchoring on the metric you happened to notice first.

Prompt

**Name the segments to try.** "Plan, platform, and signup source" gives the isolation a search order, so the narrative points to the one segment that explains most of the move rather than a grid of every cut.

Source

**Check it against what changed.** Checking the changelog and Linear over the same window turns correlation into a causal hypothesis the team can act on, not just a chart that went down.

Prompt

**Set a chart limit.** "Two charts that prove it" keeps the output to the before/after and the segment split that carry the argument, instead of a dashboard dump.

### Get a better draft[](#get-a-better-draft)

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you[](#make-cowork-work-for-you)

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /metrics-review skill with my feedback.

Product / metricsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable[](#make-it-repeatable)

### Run it every Monday morning[](#run-it-every-monday-morning)

The "why did the number move" question comes every week whether or not you've had time to dig. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill writes the narrative before standup.

**/schedule** Every Monday at 7am, run /metrics-review for the prior week, write the narrative and charts to Product/metrics/<week>, and flag anything that moved more than 10% week over week.

Product / metricsOpen in Cowork

Scheduled taskActive

Weekly metrics narrative

Runs `/metrics-review` against the prior week's data, isolates the driver, and writes the what-happened-and-why with charts to the week's folder.

Every **Monday at 7:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates[](#share-with-your-teammates)

Your customized `/metrics-review` now carries your metric definitions, your segment order, and your narrative format. Share it so any PM can answer "why did this move" in your structure, and the weekly readout stays consistent no matter whose number it is.

Share the skill

In Cowork, open **Skills** → `/metrics-review` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your definitions and format baked in, so they don't repeat Steps 1-3.

## Going forward[](#going-forward)

### Now in your Cowork

Your processes

Product Management plugin

Your tools

AmplitudeDatabricks![](images/d9bcb0bb9b2b1fff.svg)Linear

Your workspace

Product / metrics

The metric move is explained in writing with its driver and likely cause identified, plus the charts that support it — ready to act on rather than investigate.

[Next: Launch readiness sweep](https://academy.claude.com/use-cases/launch-readiness)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
