<!-- source: https://academy.claude.com/use-cases/feedback-synthesis -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Feedback synthesis to prioritized themes

The five themes that matter, quantified and quoted.

10 minProductClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-calyi96r.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-iv2hjqlx.png)

## Set up

### Try a plugin

The Product Management plugin ships with `/synthesize-research` and other discovery skills as a starting point, already structured to cluster raw signal into themes and rank them. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Product ManagementWrite feature specs, plan roadmaps, and synthesize user research faster. Keep stakeholders updated and stay ahead of the competitive landscape.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=product-management)

`/synthesize-research`Synthesize user research from interviews, surveys, and feedback into structured insights.

[Run](claude://cowork/new?q=%2Fsynthesize-research)

`/roadmap-update`Update, create, or reprioritize your product roadmap.

[Run](claude://cowork/new?q=%2Froadmap-update)

Show all 8 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/b6bf6491858dcff4.svg)

Slack

[Connect](https://claude.ai/desktop/directory/slack)

![](images/d9bcb0bb9b2b1fff.svg)

Linear

[Connect](https://claude.ai/desktop/directory/linear)

![](images/2ba03d1b12a8d596.svg)

Intercom

Read support conversations and tags so product hears what customers are actually saying, verbatim.

[Connect](https://claude.ai/desktop/directory/intercom)

![](images/a3bfc5814bd6a3e2.svg)

Google DriveOptional

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (the NPS verbatim export, the support ticket CSV, the sales call snippets, the six interview transcripts) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the Voice of Customer brief back to it. If you run this every quarter, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your sources, instructions, and memory stay attached.

Product / voc-q2

nps-verbatims-q2.csvApr 22, 2026412 KB

zendesk-export-feedback.csvApr 22, 20261.1 MB

sales-call-snippets.mdApr 20, 202638 KB

interview-01-ops-lead.docxApr 9, 202652 KB

interview-02 through 06.docxOptionalApr 20265 files

In Cowork’s chat bar:Product / voc-q2

## The prompt

### Copy this into Claude Cowork

Read this folder plus the #product-feedback Slack channel and the open Zendesk tickets tagged feedback. Cluster everything into 5 to 7 themes, count how often each shows up and how severe it is, pull the best verbatim for each, flag which map to a Linear roadmap item versus net-new, and write a one-page Voice of Customer brief for roadmap review.

Product / voc-q2Open in Cowork

### Why this works

Prompt

**Give a number range.** "5 to 7 themes" forces real clustering instead of a forty-row tag list, so the brief fits on one page and the roadmap conversation stays on the top signals.

Prompt

**Ask for frequency and severity.** Naming both gives Claude your ranking criteria, so the themes come back ordered by what matters to planning rather than just by how often they came up.

Prompt

**Ask for the single best example.** The single best quote does more in roadmap review than a wall of evidence; Cowork picks the strongest line and links the rest underneath.

Source

**Compare against your existing plan.** "Map to a Linear roadmap item versus net-new" means the brief arrives already split into validate-what-we-planned and here-is-what-we-missed.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /synthesize-research skill with my feedback.

ProductOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it ahead of every roadmap review

Feedback piles up between planning cycles whether or not anyone is reading it. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill produces a fresh brief the Friday before each roadmap review.

**/schedule** Every Friday at 4pm, run /synthesize-research against Product/voc-<current-quarter> plus the live Slack and Zendesk sources, and write the brief to that folder as voc-brief-<date>.md.

ProductOpen in Cowork

Scheduled taskActive

Monthly Voice of Customer brief

Runs `/synthesize-research` against the quarter's VoC folder plus live Slack and Zendesk and writes the one-page brief back to the folder.

Every **Friday at 4:00pm**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/synthesize-research` now carries your severity scale, your standing sources, and your brief format. Share it so every PM on the team clusters feedback the same way, and roadmap review reads one consistent VoC page no matter whose area it covers.

Share the skill

In Cowork, open **Skills** → `/synthesize-research` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your sources and severity scale baked in, so they don't repeat Steps 1-3.

## Going forward

### Now in your Cowork

Your processes

Product Management plugin

Your tools

![](images/b6bf6491858dcff4.svg)Slack![](images/d9bcb0bb9b2b1fff.svg)Linear![](images/fce598a81466f954.svg)Zendesk![](images/a3bfc5814bd6a3e2.svg)Google Drive

Your workspace

Product / voc

Feedback from all your sources is organized into a ranked one-page brief, each theme counted, quoted, and checked against the roadmap — ready to act on instead of sort through.

[Next: Metrics deep-dive to narrative](https://academy.claude.com/use-cases/metrics-narrative)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
