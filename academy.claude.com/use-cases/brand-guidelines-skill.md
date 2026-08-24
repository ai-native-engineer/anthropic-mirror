<!-- source: https://academy.claude.com/use-cases/brand-guidelines-skill -->

Loading

## Set up

### Try a plugin

The Design plugin ships with `/ux-copy` and `/design-system` as starting points for brand-aware output; you'll build your own `/on-brand` on top. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.



DesignAccelerate design workflows — critique, design system management, UX writing, accessibility audits, research synthesis, and dev handoff. From exploration to pixel-perfect specs.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=design)

`/ux-copy`Write or review UX copy — microcopy, error messages, empty states, CTAs.

[Run](claude://cowork/new?q=%2Fux-copy)

`/design-system`Audit, document, or extend your design system.

[Run](claude://cowork/new?q=%2Fdesign-system)

Show all 7 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%230ACF83'%20d='M8%2024a4%204%200%200%200%204-4v-4H8a4%204%200%200%200%200%208Z'/%3e%3cpath%20fill='%23A259FF'%20d='M4%2012a4%204%200%200%201%204-4h4v8H8a4%204%200%200%201-4-4Z'/%3e%3cpath%20fill='%23F24E1E'%20d='M4%204a4%204%200%200%201%204-4h4v8H8a4%204%200%200%201-4-4Z'/%3e%3cpath%20fill='%23FF7262'%20d='M12%200h4a4%204%200%200%201%200%208h-4V0Z'/%3e%3cpath%20fill='%231ABCFE'%20d='M20%2012a4%204%200%201%201-8%200%204%204%200%200%201%208%200Z'/%3e%3c/svg%3e)

Figma

Read published variables, type styles, and components straight from the library file.

[Connect](https://claude.ai/desktop/directory/figma)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23000'%20d='M4.46%204.44c.74.6%201.02.56%202.42.46l13.18-.79c.28%200%20.05-.28-.05-.32l-2.19-1.58c-.42-.33-.98-.7-2.05-.6L2.99%202.53c-.46.05-.56.28-.37.46l1.84%201.45Zm.8%203.1v13.87c0%20.74.37%201.02%201.21.98l14.49-.84c.84-.05.93-.56.93-1.16V6.6c0-.6-.23-.93-.74-.88l-15.14.88c-.56.05-.75.33-.75.93Zm14.3.74c.1.42%200%20.84-.42.89l-.7.14v10.24c-.6.33-1.16.51-1.63.51-.74%200-.93-.23-1.49-.93l-4.56-7.16v6.93l1.44.33s0%20.84-1.16.84l-3.21.18c-.1-.18%200-.65.33-.74l.84-.23V9.98l-1.16-.1c-.1-.42.14-1.02.79-1.07l3.44-.23%204.75%207.25V9.42l-1.21-.14c-.1-.51.28-.88.74-.93l3.21-.18Z'/%3e%3c/svg%3e)

Notion

Pull the brand guidelines and voice doc from where the team already maintains them.

[Connect](https://claude.ai/desktop/directory/notion)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23181717'%20d='M12%20.3a12%2012%200%200%200-3.8%2023.39c.6.11.82-.26.82-.58v-2.03c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.33-1.76-1.33-1.76-1.09-.74.08-.73.08-.73%201.2.09%201.84%201.24%201.84%201.24%201.07%201.83%202.81%201.3%203.49%201%20.11-.78.42-1.31.76-1.61-2.67-.3-5.47-1.33-5.47-5.93%200-1.31.47-2.38%201.24-3.22-.13-.3-.54-1.52.11-3.18%200%200%201.01-.32%203.3%201.23a11.5%2011.5%200%200%201%206%200c2.29-1.55%203.3-1.23%203.3-1.23.65%201.66.24%202.88.12%203.18.77.84%201.23%201.91%201.23%203.22%200%204.61-2.8%205.63-5.48%205.92.43.37.81%201.1.81%202.22v3.29c0%20.32.22.7.82.58A12%2012%200%200%200%2012%20.3'/%3e%3c/svg%3e)

GitHubOptional

Read the design-tokens package so the skill stays in sync with what ships.

[Connect](https://claude.ai/desktop/directory/github)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)



**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (the brand guidelines PDF, the voice and tone doc, the exported component docs, the tokens JSON) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the skill definition back to it. If you maintain the brand system, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so updates to the guidelines flow through.

Brand / System-Source

brand-guidelines-2026.pdfFeb 3, 20263.4 MB

voice-and-tone.docxFeb 3, 202652 KB

tokens.jsonApr 20, 202618 KB

In Cowork’s chat bar:Brand / System-Source

## The prompt

### Copy this into Claude Cowork

Turn the brand docs in this folder into a shared skill called /on-brand. The skill should enforce our color tokens, typography, spacing, and voice rules on any content or UI it generates, and refuse off-brand patterns with a short reason.



Brand / System-SourceOpen in Cowork

### Why this works

Source

**Point at your docs.** The folder chip plus "in this folder" tells Claude your guidelines are the authority, not what it knows about branding in general.

Prompt

**Name the output.** Asking for "a shared skill called /on-brand" instead of "brand guidelines" is the difference between a reusable command and a one-time answer.

Prompt

**List what it covers.** "Color tokens, typography, spacing, and voice" — naming the parts means Claude reads those sections of your docs first instead of guessing what counts as brand.

Prompt

**Define the failure case.** "Refuse off-brand patterns with a short reason" is what makes the skill enforce rather than suggest, and the reason teaches whoever gets refused.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

The plugin's `/on-brand` is a generic scaffold. Once Step 2 produces output that passes your own brand review, tell Cowork to harden it. Layer in your exception list, your sub-brand variations, your accessibility minimums, and the phrasing you never want to see. A few minutes of conversation and the skill enforces your system from then on.

Make what we've done in this task so far into a skill, or edit the /on-brand skill with my feedback.



BrandOpen in Cowork



**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Make it a live artifact

Guidelines change; the skill should too. Ask Cowork to publish a brand-compliance summary as a live artifact so anyone can see exactly what `/on-brand` enforces today. Re-run the skill (or schedule it) and the page reflects the latest guidelines.

Publish a one-page summary of what /on-brand enforces as a live artifact for the whole company.



Brand / System-SourceOpen in Cowork

### Re-sync it with every guideline change

The brand evolves; the skill should follow without a ticket. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and set the customized skill to rebuild itself weekly from the source folder and library.

**/schedule** Mondays at 9am, re-read Brand/System-Source and the Figma library and rebuild /on-brand, posting a short changelog of what the skill now enforces differently.



BrandOpen in Cowork

Scheduled taskActive

Brand skill re-sync

Each Monday at 9am, re-reads the guidelines folder and Figma library, rebuilds `/on-brand`, and posts a short changelog of what now enforces differently.

Every **Monday at 9:00 AM**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/on-brand` now carries your tokens, your type scale, your voice rules, and your refusal list. Share it workspace-wide so marketing, product, sales, and support all generate from the same system, and the design team stops being the brand police after the fact.



Share the skill

In Cowork, open **Skills** → `/on-brand` → **Share** and pick your whole workspace (if your admin allows). Every team gets the skill with your guidelines baked in, so they don't repeat Steps 1-3.

## What changes for the design system team

Everything Claude generates across the workspace follows your brand rules by default. Review is for judgment calls, not for correcting colors, type, and voice on every draft.

You did this for the core brand. The same approach covers sub-brands, event identities, and accessibility minimums — each one becomes a skill in the design plugin your team maintains.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/design-icon.svg)

Claude Design

Generate the on-brand asset from your encoded system

Open](https://claude.ai/design)

[Next: Design system drift review](https://academy.claude.com/use-cases/design-police)
