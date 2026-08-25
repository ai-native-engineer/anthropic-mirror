<!-- source: https://academy.claude.com/use-cases/pattern-consistency-audit -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Pattern consistency audit

Every existing surface that already solves this, before you design a new one.

10 minDesignClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-pa0satz7.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-ewc5ye4g.png)

## Set up

### Try a plugin

The Design plugin ships with `/design-handoff` and other design-system skills as a starting point, already structured to inventory components and cross-reference where they live. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

DesignAccelerate design workflows — critique, design system management, UX writing, accessibility audits, research synthesis, and dev handoff. From exploration to pixel-perfect specs.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=design)

`/design-handoff`Generate developer handoff specs from a design.

[Run](claude://cowork/new?q=%2Fdesign-handoff)

`/research-synthesis`Synthesize user research into themes, insights, and recommendations.

[Run](claude://cowork/new?q=%2Fresearch-synthesis)

Show all 7 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/d0c4c5893ba4311d.svg)

Figma

Search your component libraries and shipped files for every instance of the pattern.

[Connect](https://claude.ai/desktop/directory/figma)

![](images/92b68e492ad6094d.svg)

GitHub

Find where the pattern is implemented in the product and who owns that surface.

[Connect](https://claude.ai/desktop/directory/github)

AmplitudeOptional

Pull engagement and conversion for each surface so the recommendation is grounded in data.

[Connect](https://claude.ai/desktop/directory/amplitude)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (a Figma export of the design system, screenshots of the surfaces you already know about, the product sitemap) into one folder and point Cowork at it. Cowork reads from it and writes the audit back to it. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from your design-system folder so the component inventory and ownership map stay attached for every audit.

Design-system / Audits / inline-filter

component-inventory.mdMar 18, 202642 KB

search-results-current.pngApr 26, 2026410 KB

surface-ownership.csvFeb 9, 20268 KB

In Cowork’s chat bar:Design-system / Audits / inline-filter

## The prompt

### Copy this into Claude Cowork

Before I propose a new inline-filter pattern for the search results page, find every surface in our product using something similar (chips, segmented controls, dropdown filters, faceted sidebars). For each, show a screenshot or Figma link, note which team owns it and how it performed (engagement or conversion if we have it). Tell me which pattern to reuse and why.

Design-system / Audits / inline-filterOpen in Cowork

### Why this works

Prompt

**Name the variants to search for.** Chips, segmented controls, dropdowns, facets are how the same intent shows up under different names; naming them widens the search.

Prompt

**Ask for the owner.** You'll need to talk to that team either way; the audit doubles as your stakeholder list.

Prompt

**Back the recommendation with data.** "How that surface performed" turns the recommendation from taste into evidence for the design crit.

Source

**Put your reference list in the folder.** Cowork starts from your component list, then checks the live product for what's drifted.

### Get a better draft

Practice

**Ask for the consolidation plan.** Add "if I should reuse one, list which other surfaces should migrate to it too" and the audit becomes a design-system roadmap item.

Practice

**Add a screenshot of the destination.** Drop a screenshot of where the pattern is going and Cowork weighs fit, not just precedent.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /design-handoff skill with my feedback.

Design-system / AuditsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Make it the default first step

This audit should run before any new pattern enters review. Save it as a skill the whole design org can call with one line, swapping the pattern name each time, so "did we check what already exists" stops being a crit-week surprise.

Save this as /pattern-audit. It should take a pattern name, search Figma, the codebase, and Amplitude for existing instances, and write the side-by-side with a reuse recommendation to Design-system/Audits/<pattern>.md.

Design-system / AuditsOpen in Cowork

## Share with your teammates

Your customized `/pattern-audit` now carries your component inventory, your ownership map, and your performance lookups. Share it so every designer runs the same check before crit, and the design system stops growing five ways to do one thing.

Share the skill

In Cowork, open **Skills** → `/pattern-audit` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your instructions baked in, they don't repeat Steps 1-3.

## What changes for design crit

You have every existing instance of the pattern inventoried with its owner and performance data, plus a recommendation on which to reuse. The decision is backed by evidence rather than preference.

You did this for one filter pattern. The same approach covers navigation, empty states, and form patterns — each one becomes a skill your team runs before proposing something new.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/design-icon.svg)

Claude Design

Mock the reuse option directly in your design file

Open](https://claude.ai/design)

[Next: Heuristic audit a flow](https://academy.claude.com/use-cases/design-heuristic-audit)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for design crit](#what-changes-for-design-crit)
