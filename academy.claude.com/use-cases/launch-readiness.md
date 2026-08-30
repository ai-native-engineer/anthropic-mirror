<!-- source: https://academy.claude.com/use-cases/launch-readiness -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Launch readiness sweep

Red/yellow/green with the blockers named.

10 minProductClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-cfvv79hl.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-fa1zco5y.png)

## Set up[](#set-up)

### Try a plugin[](#try-a-plugin)

The Product Management plugin ships with `/stakeholder-update` and other release skills as a starting point, already structured to build a checklist, assign status, and make the go/no-go call. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Product Management7 skills to write specs, synthesize research, run competitive analysis, and keep the roadmap honest

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=product-management)

`/stakeholder-update`Sweep launch readiness across PRD, epic, Slack, and GTM brief and make the go/no-go call

[Run](claude://cowork/new?q=%2Fstakeholder-update)

`/metrics-review`Explain a metric move with segment isolation and ship correlation

[Run](claude://cowork/new?q=%2Fmetrics-review)

Show all 8 skills

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/d9bcb0bb9b2b1fff.svg)

Linear

[Connect](https://claude.ai/desktop/directory/linear)

![](images/b6bf6491858dcff4.svg)

Slack

[Connect](https://claude.ai/desktop/directory/slack)

![](images/a3bfc5814bd6a3e2.svg)

Google Drive

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

![](images/ea7c24639ab8053c.svg)

NotionOptional

[Connect](https://claude.ai/desktop/directory/notion)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

Drag the files you'll use (the PRD, the GTM brief, the launch checklist template, the retro from your last two launches) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the readiness checklist back to it. If you run launches regularly, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your checklist template, prior retros, and memory stay attached.

Launches / saved-views

PRD-saved-views.docxApr 8, 202662 KB

gtm-brief-saved-views.docxApr 20, 202628 KB

launch-checklist-template.mdFeb 2, 20268 KB

retro-bulk-export-launch.mdOptionalMar 30, 202611 KB

In Cowork’s chat bar:Launches / saved-views

## The prompt[](#the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Sweep launch readiness for the saved-views launch. Produce the launch checklist with status and owner per item, give a red/yellow/green readiness call overall, name the blockers, and note anything that matches what went well or wrong in our last two launches.

Launches / saved-viewsOpen in Cowork

### Why this works[](#why-this-works)

Source

**Give it every source at once.** PRD, epic, Slack, and GTM brief each hold a different slice of the truth; sweeping them at once is what catches the item that's "done" in Linear but still being argued in the channel.

Prompt

**Ask for an owner on every line.** A checklist with a name on every line is actionable in launch standup; a checklist without owners is a wish list.

Prompt

**Ask for a verdict with reasons.** Asking for an overall red/yellow/green forces a judgment, and "name the specific blockers" means yellow comes with the two things that have to clear, not a vibe.

Source

**Compare against your own history.** Pointing Claude at your past retros lets it check this launch against what's gone wrong before. Otherwise it's evaluating in isolation.

### Get a better draft[](#get-a-better-draft)

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you[](#make-cowork-work-for-you)

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /stakeholder-update skill with my feedback.

LaunchesOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable[](#make-it-repeatable)

### Run it daily during launch week[](#run-it-daily-during-launch-week)

Readiness changes by the hour in the final stretch. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill posts a fresh checklist every morning of launch week so standup opens with the current picture.

**/schedule** Every weekday at 8am from May 4 through May 8, run /stakeholder-update for the saved-views launch and write the checklist to Launches/saved-views as readiness-<date>.md, with a one-line color change vs yesterday.

LaunchesOpen in Cowork

Scheduled taskActive

Daily launch readiness sweep

Runs `/stakeholder-update` against the PRD, Linear epic, Slack channel, and GTM brief and writes the dated checklist with the overall color to the launch folder.

Every **day at 8:00am, May 4 to May 8**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates[](#share-with-your-teammates)

Your customized `/stakeholder-update` now carries your checklist template, your owners, and your color criteria. Share it so every launch lead runs the same sweep, and the go/no-go meeting reads one consistent format no matter which feature is shipping.

Share the skill

In Cowork, open **Skills** → `/stakeholder-update` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your checklist and criteria baked in, so they don't repeat Steps 1-3.

## Going forward[](#going-forward)

### Now in your Cowork

Your processes

Product Management plugin

Your tools

![](images/d9bcb0bb9b2b1fff.svg)Linear![](images/b6bf6491858dcff4.svg)Slack![](images/a3bfc5814bd6a3e2.svg)Google Docs![](images/ea7c24639ab8053c.svg)Notion

Your workspace

Launches

Launch readiness is one current checklist with each item owned, blockers named, and a go/no-go call — ready to review instead of compile across systems.

[Next: PRD from a problem statement](https://academy.claude.com/use-cases/prd-from-a-one-pager)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
