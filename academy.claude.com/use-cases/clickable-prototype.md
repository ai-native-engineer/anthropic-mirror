<!-- source: https://academy.claude.com/use-cases/clickable-prototype -->

Loading

## Set up

### Try a plugin

The Design plugin ships with `/design-handoff` already structured to read a flow description and a component library and emit a wired, clickable HTML build. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.



DesignAccelerate design workflows — critique, design system management, UX writing, accessibility audits, research synthesis, and dev handoff. From exploration to pixel-perfect specs.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=design)

`/design-handoff`Generate developer handoff specs from a design.

[Run](claude://cowork/new?q=%2Fdesign-handoff)

`/ux-copy`Write or review UX copy — microcopy, error messages, empty states, CTAs.

[Run](claude://cowork/new?q=%2Fux-copy)

Show all 7 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%230ACF83'%20d='M8%2024a4%204%200%200%200%204-4v-4H8a4%204%200%200%200%200%208Z'/%3e%3cpath%20fill='%23A259FF'%20d='M4%2012a4%204%200%200%201%204-4h4v8H8a4%204%200%200%201-4-4Z'/%3e%3cpath%20fill='%23F24E1E'%20d='M4%204a4%204%200%200%201%204-4h4v8H8a4%204%200%200%201-4-4Z'/%3e%3cpath%20fill='%23FF7262'%20d='M12%200h4a4%204%200%200%201%200%208h-4V0Z'/%3e%3cpath%20fill='%231ABCFE'%20d='M20%2012a4%204%200%201%201-8%200%204%204%200%200%201%208%200Z'/%3e%3c/svg%3e)

Figma

Read the published components and variables so the prototype uses the real library.

[Connect](https://claude.ai/desktop/directory/figma)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23181717'%20d='M12%20.3a12%2012%200%200%200-3.8%2023.39c.6.11.82-.26.82-.58v-2.03c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.33-1.76-1.33-1.76-1.09-.74.08-.73.08-.73%201.2.09%201.84%201.24%201.84%201.24%201.07%201.83%202.81%201.3%203.49%201%20.11-.78.42-1.31.76-1.61-2.67-.3-5.47-1.33-5.47-5.93%200-1.31.47-2.38%201.24-3.22-.13-.3-.54-1.52.11-3.18%200%200%201.01-.32%203.3%201.23a11.5%2011.5%200%200%201%206%200c2.29-1.55%203.3-1.23%203.3-1.23.65%201.66.24%202.88.12%203.18.77.84%201.23%201.91%201.23%203.22%200%204.61-2.8%205.63-5.48%205.92.43.37.81%201.1.81%202.22v3.29c0%20.32.22.7.82.58A12%2012%200%200%200%2012%20.3'/%3e%3c/svg%3e)

GitHub

Pull the design-system package so generated markup matches what engineering ships.

[Connect](https://claude.ai/desktop/directory/github)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google DriveOptional

Read the flow description and write the prototype link back to the project doc.

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)



**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (the flow description or spec, the component library export, your tokens, sample content) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the prototype HTML back into a subfolder. If you prototype regularly, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your library and conventions stay attached.

Prototypes / Invite-Flow

invite-flow-spec.docxApr 26, 202631 KB

tokens.jsonApr 20, 202618 KB

design-system.cssApr 20, 2026142 KB

In Cowork’s chat bar:Prototypes / Invite-Flow

## The prompt

### Copy this into Claude Cowork

Build a clickable HTML prototype of the flow in this folder using only components from our design system library. Wire up the navigation, use realistic placeholder data, and write it to prototype/index.html so I can click through in a browser.



Prototypes / Invite-FlowOpen in Cowork

### Why this works

Prompt

**Limit it to your own materials.** No invented UI; everything maps to the real library.

Prompt

**Describe what each interaction should do.** Clicking actually moves; users test a flow, not pictures.

Prompt

**Ask for realistic sample content.** No lorem ipsum; the screens read like the product.

Source

**Give it the source files directly.** Tokens and CSS ship into the prototype unchanged.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

The plugin's `/design-handoff` is a generic starting point. Once Step 2 produces a build you'd actually put in front of a participant, tell Cowork to write your version of the skill. Layer in your component naming, your data fixtures, your interaction conventions, and the wrapper page your prototypes always sit in. A few minutes of conversation and the skill runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /design-handoff skill with my feedback.



PrototypesOpen in Cowork

## Make it repeatable

### Make it a live artifact

A prototype you have to email around gets stale. Ask Cowork to publish it as a live artifact and every reviewer and test participant has one link that stays current — re-run the skill (or schedule it) to refresh.

Publish that prototype as a live artifact. Add a small "v2, v3" version stamp in the corner.



Prototypes / Invite-FlowOpen in Cowork

### Rebuild it on every spec change

The spec moves, the prototype should follow without a request. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and set the customized skill to rebuild each morning from whatever is in the folder.

**/schedule** Weekdays at 7am, check Prototypes/Invite-Flow for changes and re-run /design-handoff, rebuilding prototype/index.html and bumping the version stamp.



PrototypesOpen in Cowork

Scheduled taskActive

Daily prototype rebuild

Each weekday at 7am, checks the project folder for spec or library changes, re-runs `/design-handoff`, and rebuilds the clickable HTML with a bumped version stamp.

Every **weekday at 7 am · checks Prototypes/Invite-Flow for changes**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/design-handoff` now carries your component map, your data fixtures, and your wrapper page. Share it so any designer on the team can go from spec to clickable build the same way, and concept testing stops waiting on someone who knows how to wire frames by hand.



Share the skill

In Cowork, open **Skills** → `/design-handoff` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your library and conventions baked in, so they don't repeat Steps 1-3.

## What changes for early concept testing

A clickable prototype built from your real component library, with working navigation and realistic content — ready to test with users and gather feedback on the flow.

You did this for one flow. The same approach covers onboarding, checkout, and side-by-side variant comparisons — each one becomes a skill your team runs the same way.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/design-icon.svg)

Claude Design

Bring the prototype into Figma as on-brand frames

Open](https://claude.ai/design)

[Next: Competitive teardown and heuristic audit](https://academy.claude.com/use-cases/design-heuristic-audit)
