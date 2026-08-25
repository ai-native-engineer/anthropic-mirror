<!-- source: https://academy.claude.com/use-cases/clickable-prototype -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Clickable prototype from real components

A clickable HTML prototype built from your real library.

15 minDesignClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-e6bs284y.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-m8ta2480.png)

## Set up

### Try a plugin

The Design plugin ships with `/design-handoff` already structured to read a flow description and a component library and emit a wired, clickable HTML build. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

DesignAccelerate design workflows — critique, design system management, UX writing, accessibility audits, research synthesis, and dev handoff. From exploration to pixel-perfect specs.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=design)

`/design-handoff`Generate developer handoff specs from a design.

[Run](claude://cowork/new?q=%2Fdesign-handoff)

`/ux-copy`Write or review UX copy — microcopy, error messages, empty states, CTAs.

[Run](claude://cowork/new?q=%2Fux-copy)

Show all 7 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/d0c4c5893ba4311d.svg)

Figma

Read the published components and variables so the prototype uses the real library.

[Connect](https://claude.ai/desktop/directory/figma)

![](images/92b68e492ad6094d.svg)

GitHub

Pull the design-system package so generated markup matches what engineering ships.

[Connect](https://claude.ai/desktop/directory/github)

![](images/a3bfc5814bd6a3e2.svg)

Google DriveOptional

Read the flow description and write the prototype link back to the project doc.

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (the flow description or spec, the component library export, your tokens, sample content) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the prototype HTML back into a subfolder. If you prototype regularly, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your library and conventions stay attached.

Prototypes / Invite-Flow

invite-flow-spec.docxApr 26, 202631 KB

tokens.jsonApr 20, 202618 KB

design-system.cssApr 20, 2026142 KB

In Cowork’s chat bar:Prototypes / Invite-Flow

## The prompt

### Copy this into Claude Cowork

Build a clickable HTML prototype of the flow in this folder using only components from our design system library. Wire up the navigation, use realistic placeholder data, and write it to prototype/index.html so I can click through in a browser.

Prototypes / Invite-FlowOpen in Cowork

### Why this works

Prompt

**Limit it to your own materials.** No invented UI; everything maps to the real library.

Prompt

**Describe what each interaction should do.** Clicking actually moves; users test a flow, not pictures.

Prompt

**Ask for realistic sample content.** No lorem ipsum; the screens read like the product.

Source

**Give it the source files directly.** Tokens and CSS ship into the prototype unchanged.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

The plugin's `/design-handoff` is a generic starting point. Once Step 2 produces a build you'd actually put in front of a participant, tell Cowork to write your version of the skill. Layer in your component naming, your data fixtures, your interaction conventions, and the wrapper page your prototypes always sit in. A few minutes of conversation and the skill runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /design-handoff skill with my feedback.

PrototypesOpen in Cowork

## Make it repeatable

### Make it a live artifact

A prototype you have to email around gets stale. Ask Cowork to publish it as a live artifact and every reviewer and test participant has one link that stays current — re-run the skill (or schedule it) to refresh.

Publish that prototype as a live artifact. Add a small "v2, v3" version stamp in the corner.

Prototypes / Invite-FlowOpen in Cowork

### Rebuild it on every spec change

The spec moves, the prototype should follow without a request. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and set the customized skill to rebuild each morning from whatever is in the folder.

**/schedule** Weekdays at 7am, check Prototypes/Invite-Flow for changes and re-run /design-handoff, rebuilding prototype/index.html and bumping the version stamp.

PrototypesOpen in Cowork

Scheduled taskActive

Daily prototype rebuild

Each weekday at 7am, checks the project folder for spec or library changes, re-runs `/design-handoff`, and rebuilds the clickable HTML with a bumped version stamp.

Every **weekday at 7 am · checks Prototypes/Invite-Flow for changes**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/design-handoff` now carries your component map, your data fixtures, and your wrapper page. Share it so any designer on the team can go from spec to clickable build the same way, and concept testing stops waiting on someone who knows how to wire frames by hand.

Share the skill

In Cowork, open **Skills** → `/design-handoff` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your library and conventions baked in, so they don't repeat Steps 1-3.

## What changes for early concept testing

A clickable prototype built from your real component library, with working navigation and realistic content — ready to test with users and gather feedback on the flow.

You did this for one flow. The same approach covers onboarding, checkout, and side-by-side variant comparisons — each one becomes a skill your team runs the same way.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/design-icon.svg)

Claude Design

Bring the prototype into Figma as on-brand frames

Open](https://claude.ai/design)

[Next: Competitive teardown and heuristic audit](https://academy.claude.com/use-cases/design-heuristic-audit)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for early concept testing](#what-changes-for-early-concept-testing)
