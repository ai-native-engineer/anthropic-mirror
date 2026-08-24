<!-- source: https://academy.claude.com/use-cases/design-heuristic-audit -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Competitive teardown and heuristic audit

Heuristic-scored teardown of competitor flows with evidence.

10 minDesignClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-drc4nbll.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-kor1z3r3.png)

## Set up

### Try a plugin

The Design plugin ships with `/design-critique` already structured to walk screens against a rubric and compare across competitors. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

DesignAccelerate design workflows — critique, design system management, UX writing, accessibility audits, research synthesis, and dev handoff. From exploration to pixel-perfect specs.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=design)

`/design-critique`Get structured design feedback on usability, hierarchy, and consistency.

[Run](claude://cowork/new?q=%2Fdesign-critique)

`/design-system`Audit, document, or extend your design system.

[Run](claude://cowork/new?q=%2Fdesign-system)

Show all 7 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%230ACF83'%20d='M8%2024a4%204%200%200%200%204-4v-4H8a4%204%200%200%200%200%208Z'/%3e%3cpath%20fill='%23A259FF'%20d='M4%2012a4%204%200%200%201%204-4h4v8H8a4%204%200%200%201-4-4Z'/%3e%3cpath%20fill='%23F24E1E'%20d='M4%204a4%204%200%200%201%204-4h4v8H8a4%204%200%200%201-4-4Z'/%3e%3cpath%20fill='%23FF7262'%20d='M12%200h4a4%204%200%200%201%200%208h-4V0Z'/%3e%3cpath%20fill='%231ABCFE'%20d='M20%2012a4%204%200%201%201-8%200%204%204%200%200%201%208%200Z'/%3e%3c/svg%3e)

Figma

Compare competitor screens against your own current frames side by side.

[Connect](https://claude.ai/desktop/directory/figma)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3crect%20width='24'%20height='24'%20rx='5'%20fill='%23FFD02F'/%3e%3cpath%20fill='%23050038'%20d='M16.59%203.52h-2.65l2.2%203.87-4.85-3.87H8.64l2.43%204.84-5.08-4.84H3.34l2.7%206.16-2.7%2010.8h2.65l5.08-11.77-2.43%2011.77h2.65l4.85-12.74-2.2%2012.74h2.65l4.87-14.19z'/%3e%3c/svg%3e)

Miro

Drop the scored teardown onto a board for the competitive workshop.

[Connect](https://claude.ai/desktop/directory/miro)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google DriveOptional

Read the competitor docs folder and write the teardown back as a shareable Doc.

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (competitor flow screenshots, their help-center PDFs, your own current screens, your heuristic rubric) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the scored teardown back to it. If you do teardowns regularly, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your rubric and memory stay attached.

Competitive / Teardown-Q2

competitor-a-onboarding.pngApr 23, 20262.4 MB

competitor-b-checkout.pngApr 23, 20261.9 MB

heuristic-rubric.pdfJan 12, 202664 KB

In Cowork’s chat bar:Competitive / Teardown-Q2

## The prompt

### Copy this into Claude Cowork

Run a heuristic audit of these competitors. Score each screen against Nielsen's ten heuristics plus our three custom ones, note where each competitor is stronger or weaker than us, and end with the three patterns worth stealing and the three to avoid.

Competitive / Teardown-Q2Open in Cowork

### Why this works

Prompt

**Score against a named rubric.** Ten plus three: comparable scores, not vibes.

Prompt

**Compare against your own baseline.** Every finding is measured against your current product.

Prompt

**Ask for a clear recommendation.** The teardown becomes a decision, not a report.

Source

**Your source files are the evidence.** Every score points at a frame in the folder.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /design-critique skill with my feedback.

CompetitiveOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Make it a live artifact

Competitors ship weekly; a static teardown ages fast. Ask Cowork to publish the scorecard as a live artifact and product leadership has one link that stays current — re-run the skill or schedule it to refresh.

Publish that teardown scorecard as a live artifact. Keep a "what changed since last quarter" note at the top.

Competitive / Teardown-Q2Open in Cowork

### Run it after every competitor release

A rival ships, the teardown should already be updating. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and set the customized skill to run every Monday, picking up any new screenshots dropped in the folder.

**/schedule** Mondays at 10am, check Competitive/Teardown-Q2 for new screenshots and re-run /design-critique, updating the scorecard and flagging any heuristic where a competitor overtook us.

CompetitiveOpen in Cowork

Scheduled taskActive

Weekly competitive re-score

Each Monday at 10am, checks the teardown folder for new screenshots, re-runs `/design-critique`, and flags any heuristic where a competitor overtook us.

Every **Monday at 10 am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/design-critique` now carries your rubric, your severity scale, and your steal/avoid framing. Share it so every designer and PM scores competitors the same way, and the quarterly review compares like with like.

Share the skill

In Cowork, open **Skills** → `/design-critique` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your rubric baked in, so they don't repeat Steps 1-3.

## What changes for competitive review

Every competitor flow is scored against the same rubric, with evidence for each finding and a short list of what to adopt or avoid — consistent enough to compare and specific enough to act on.

You did this for one set of competitor flows. The same approach works for accessibility audits, design-system drift checks, and heuristic reviews of your own product — each one a skill your team runs the same way.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/design-icon.svg)

Claude Design

Turn the teardown into the on-brand competitive deck

Open](https://claude.ai/design)

[Next: Synthesize user interviews into findings](https://academy.claude.com/use-cases/uxr-synthesis)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for competitive review](#what-changes-for-competitive-review)
