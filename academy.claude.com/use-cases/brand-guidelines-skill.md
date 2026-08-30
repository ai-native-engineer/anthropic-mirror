<!-- source: https://academy.claude.com/use-cases/brand-guidelines-skill -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Encode the brand as a skill

Every Claude output across the org stays on-brand.

15 minDesignClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-ffjdr70o.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-bm06b1oh.png)

## Set up[](#set-up)

### Try a plugin[](#try-a-plugin)

The Design plugin ships with `/ux-copy` and `/design-system` as starting points for brand-aware output; you'll build your own `/on-brand` on top. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

DesignAccelerate design workflows — critique, design system management, UX writing, accessibility audits, research synthesis, and dev handoff. From exploration to pixel-perfect specs.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=design)

`/ux-copy`Write or review UX copy — microcopy, error messages, empty states, CTAs.

[Run](claude://cowork/new?q=%2Fux-copy)

`/design-system`Audit, document, or extend your design system.

[Run](claude://cowork/new?q=%2Fdesign-system)

Show all 7 skills

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/d0c4c5893ba4311d.svg)

Figma

Read published variables, type styles, and components straight from the library file.

[Connect](https://claude.ai/desktop/directory/figma)

![](images/ea7c24639ab8053c.svg)

Notion

Pull the brand guidelines and voice doc from where the team already maintains them.

[Connect](https://claude.ai/desktop/directory/notion)

![](images/92b68e492ad6094d.svg)

GitHubOptional

Read the design-tokens package so the skill stays in sync with what ships.

[Connect](https://claude.ai/desktop/directory/github)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

Drag the files you'll use (the brand guidelines PDF, the voice and tone doc, the exported component docs, the tokens JSON) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the skill definition back to it. If you maintain the brand system, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so updates to the guidelines flow through.

Brand / System-Source

brand-guidelines-2026.pdfFeb 3, 20263.4 MB

voice-and-tone.docxFeb 3, 202652 KB

tokens.jsonApr 20, 202618 KB

In Cowork’s chat bar:Brand / System-Source

## The prompt[](#the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Turn the brand docs in this folder into a shared skill called /on-brand. The skill should enforce our color tokens, typography, spacing, and voice rules on any content or UI it generates, and refuse off-brand patterns with a short reason.

Brand / System-SourceOpen in Cowork

### Why this works[](#why-this-works)

Source

**Point at your docs.** The folder chip plus "in this folder" tells Claude your guidelines are the authority, not what it knows about branding in general.

Prompt

**Name the output.** Asking for "a shared skill called /on-brand" instead of "brand guidelines" is the difference between a reusable command and a one-time answer.

Prompt

**List what it covers.** "Color tokens, typography, spacing, and voice" — naming the parts means Claude reads those sections of your docs first instead of guessing what counts as brand.

Prompt

**Define the failure case.** "Refuse off-brand patterns with a short reason" is what makes the skill enforce rather than suggest, and the reason teaches whoever gets refused.

### Get a better draft[](#get-a-better-draft)

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you[](#make-cowork-work-for-you)

The plugin's `/on-brand` is a generic scaffold. Once Step 2 produces output that passes your own brand review, tell Cowork to harden it. Layer in your exception list, your sub-brand variations, your accessibility minimums, and the phrasing you never want to see. A few minutes of conversation and the skill enforces your system from then on.

Make what we've done in this task so far into a skill, or edit the /on-brand skill with my feedback.

BrandOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable[](#make-it-repeatable)

### Make it a live artifact[](#make-it-a-live-artifact)

Guidelines change; the skill should too. Ask Cowork to publish a brand-compliance summary as a live artifact so anyone can see exactly what `/on-brand` enforces today. Re-run the skill (or schedule it) and the page reflects the latest guidelines.

Publish a one-page summary of what /on-brand enforces as a live artifact for the whole company.

Brand / System-SourceOpen in Cowork

### Re-sync it with every guideline change[](#re-sync-it-with-every-guideline-change)

The brand evolves; the skill should follow without a ticket. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and set the customized skill to rebuild itself weekly from the source folder and library.

**/schedule** Mondays at 9am, re-read Brand/System-Source and the Figma library and rebuild /on-brand, posting a short changelog of what the skill now enforces differently.

BrandOpen in Cowork

Scheduled taskActive

Brand skill re-sync

Each Monday at 9am, re-reads the guidelines folder and Figma library, rebuilds `/on-brand`, and posts a short changelog of what now enforces differently.

Every **Monday at 9:00 AM**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates[](#share-with-your-teammates)

Your customized `/on-brand` now carries your tokens, your type scale, your voice rules, and your refusal list. Share it workspace-wide so marketing, product, sales, and support all generate from the same system, and the design team stops being the brand police after the fact.

Share the skill

In Cowork, open **Skills** → `/on-brand` → **Share** and pick your whole workspace (if your admin allows). Every team gets the skill with your guidelines baked in, so they don't repeat Steps 1-3.

## What changes for the design system team[](#what-changes-for-the-design-system-team)

Everything Claude generates across the workspace follows your brand rules by default. Review is for judgment calls, not for correcting colors, type, and voice on every draft.

You did this for the core brand. The same approach covers sub-brands, event identities, and accessibility minimums — each one becomes a skill in the design plugin your team maintains.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/design-icon.svg)

Claude Design

Generate the on-brand asset from your encoded system

Open](https://claude.ai/design)

[Next: Design system drift review](https://academy.claude.com/use-cases/design-police)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for the design system team](#what-changes-for-the-design-system-team)
