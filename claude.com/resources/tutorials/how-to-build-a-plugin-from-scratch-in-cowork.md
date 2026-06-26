<!-- source: https://claude.com/resources/tutorials/how-to-build-a-plugin-from-scratch-in-cowork -->

# How to build a plugin from scratch in Claude Cowork

Build a Claude Cowork plugin from scratch to encode your team's workflows, institutional knowledge, and tool connections into a repeatable, shareable process.

  Professional
* Product

  Claude Cowork
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/how-to-build-a-plugin-from-scratch-in-cowork

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69a5bbbe653abc69c4ee2f9a_Screenshot%202026-03-02%20at%208.32.55%E2%80%AFAM.png)

A Cowork plugin is a group of files that can teach Claude how to do a specific job — encoding your methodology, your workflows, your tool connections.   
  
Anthropic publishes [pre-built plugins](https://claude.com/plugins) for common roles like [Sales](https://claude.com/plugins/sales), [Finance](https://claude.com/plugins/finance), and [Legal](https://claude.com/plugins/legal). Customizing those with your company's context can help tailor the plugin to your needs. Building from scratch is for when your team has workflows, processes, or institutional knowledge that existing plugins don't cover.

*To learn more about installing and using plugins in Cowork,* [*visit here*](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)*.*

## Why build from scratch

* **Your workflow doesn't map to an existing plugin.** Your workflow has specifics that an existing plugin doesn't cover, and customizing one doesn't close the gap.
* **You want to encode institutional knowledge for your team.** The way your team actually does things — your standards, your judgment calls, your process docs — packaged so everyone works from the same playbook.
* **You need Claude to coordinate across your tools.** Your workflow pulls from a particular combination of data sources, applies particular criteria, and produces a particular deliverable.

## What's inside a plugin

A plugin can include a few types of components. Claude builds the right combination based on what you describe.

#### **Skills —** the knowledge and workflows that shape how Claude works.

A skill might be a few lines describing a formatting preference, a detailed methodology covering your full review framework, or a structured workflow you trigger by typing `/` in your prompt. Claude reads each skill's description and draws on it when it matches what you're working on — or you invoke it directly from the slash menu.

Skills can carry supporting reference documents — playbooks, compliance frameworks, pricing matrices — that Claude loads when relevant. They can accept inputs, so `/close-package North America` and `/close-package Europe` run the same process with different scope. Recurring skills can run as [scheduled tasks](https://support.claude.com/en/articles/13345190-get-started-with-cowork#h_260d21b5b3) with your criteria applied each time, and skills can chain to each other, where the output of one feeds the next.

#### **Connectors** — link Claude to your tools.

A plugin works without connectors — you can upload data manually or describe the situation — but connected tools let Claude pull what it needs mid-workflow and write results back.

You can direct Claude to search broadly across a connected tool or look in a specific place, depending on what the workflow needs.

#### **Sub-agents** — specialized helpers for complex tasks.

One agent might research a company while another pulls data from your CRM and a third scans Slack for context. They can run in parallel or in sequence, each with its own focus and fresh context window.

## How to create a plugin

Understanding the components within a plugin can give you a framework for what to share while building one: your **knowledge, judgment calls, and repeatable tasks** become skills, your **data sources** become connectors. If you have existing documents or examples of deliverables you've been happy with, share them — Claude maps it to the relevant parts of the plugin.

In Cowork, describe the plugin you want to build — even a sentence is enough to start.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b8460843a447d8ca18de65_699fb4b80c990fef020d939d_699fadff328117154b6b0dd6_Screenshot%2525202026-02-25%252520at%2525206.20.40%2525E2%252580%2525AFPM.png)

A simpler start works too — Claude will follow up with questions about your workflow, your tools, your standards, and how you handle edge cases.

> *"I need a plugin for our customer success team"*

## What changes with a plugin

With detailed instructions, Claude can handle many of these workflows. A plugin packages them into skills anyone on the team can run.

‍

### [Finance](https://claude.com/plugins/finance)

> *"Here's our P&L. Materiality threshold is $25K. Decompose by price, volume, and mix. Check these GL accounts against the subledger. Format the JE with debits on top."*

###### **Without a plugin:**Claude can handle it, but restating your full close methodology every session is overhead that compounds, and the output might vary depending on who's giving Claude the instructions.

> `/monthly-close` North America

###### **With your plugin:** Skills load your chart of accounts, materiality thresholds, close calendar, and narrative standards. Connectors pull from your data warehouse. The skill runs the full process — a new analyst runs it and gets consistent rigor.

### [Sales](https://claude.com/plugins/sales)

> *"Pull usage data for Meridian Health from our analytics dashboard. Check for support escalations in the last 90 days. Compare their current contract against our pricing tiers. Score the renewal risk and flag expansion opportunities."*

###### **Without a plugin:** You're directing Claude to each source, restating your scoring criteria, and specifying the output format every time.

> `/renewal-score` Meridian Health

###### **With your plugin:** Skills hold your scoring criteria and competitive positioning. Connectors pull from your CRM and analytics dashboard. Claude scores the account and flags expansion opportunities — consistent quality whether a senior rep or a new hire runs it.

### [Legal](https://claude.com/plugins/legal)

> *"Review this vendor agreement. Our standard on indemnification is capped at 2x contract value. Flag auto-renewals over 12 months. Use GREEN/YELLOW/RED."*

###### **Without a plugin:** This prompt covers a few checks on one contract. A full review applies dozens of standard positions across every clause type, and you'd need to restate all of them for each new agreement.

> `/due-diligence`

###### **With your plugin:** Skills hold your standard positions across every clause type and your severity classifications. A connector accesses the data room. Claude reviews every document against your playbook and produces a risk-rated summary.

## Refining your plugin

* **Use it on real work and refine as you go.** If you run a skill and something's off — a step is missing, the criteria need adjusting, the output format isn't right — tell Claude and it can update the plugin files directly. Looking through the files after Claude builds them can also help spot gaps early.
* **Show Claude the deliverable.** Upload an example or point Claude to one in a connected drive. Claude picks up the structure, emphasis, and formatting directly.
* **Keep skills focused.** Claude composes multiple skills when a task spans several areas, and focused skills with specific descriptions tend to activate more reliably than broad ones. If a skill isn't loading when you expect, its description is likely too vague — structure it as *what it does, when to use it, what it covers.*
* **Consider sub-agents for multi-source or long-running tasks.** If a workflow pulls from several tools at once, or if a task regularly hits context limits from processing too much in one pass, sub-agents let Claude split the work across separate context windows.

## Things to know

* **Plugins work in Cowork, not Chat.** Your plugin's skills are active in the Cowork tab.
* **Plugins live on your machine.** They don't sync across devices or to teammates automatically. You can share them as a compressed file, host them on GitHub for automatic updates, or have an admin provision them across your org. [*Learn more about sharing plugins.*](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)
* **Skills and connectors can also live outside plugins.** If you have personal context that applies across everything you do in Cowork — not tied to one plugin — you can add standalone skills and connectors in settings.

*Cowork with plugins is available as a research preview for all paid Claude plans (Pro, Max, Team, Enterprise) on macOS and Windows. Browse* [*available plugins*](https://claude.com/plugins)*.*

## Learn more

* ‍[Getting started with Cowork](https://support.claude.com/en/articles/13345190-getting-started-with-cowork)
* [Using plugins in Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)
* [‍](https://code.claude.com/docs/en/plugins)[Browse plugins](https://claude.com/plugins)

## Related tutorials

[Tasks to try with @Claude in your workspace](/resources/tutorials/tasks-to-try-with-claude-tag-in-your-workspace)Tasks to try with @Claude in your workspace

Tasks to try with @Claude in your workspace

Tutorial

[Tutorial](/resources/tutorials/tasks-to-try-with-claude-tag-in-your-workspace)Tutorial

[Best practices for using @Claude](/resources/tutorials/best-practices-using-claude-tag)Best practices for using @Claude

Best practices for using @Claude

Tutorial

[Tutorial](/resources/tutorials/best-practices-using-claude-tag)Tutorial

[Using Claude Cowork for legal: answer fast questions on past decisions](/resources/tutorials/using-claude-cowork-for-legal-question-briefing)Using Claude Cowork for legal: answer fast questions on past decisions

Using Claude Cowork for legal: answer fast questions on past decisions

Tutorial

[Tutorial](/resources/tutorials/using-claude-cowork-for-legal-question-briefing)Tutorial

[Using Claude Cowork for marketing ops: run a weekly review that preps itself](/resources/tutorials/using-claude-cowork-for-marketing-ops-review)Using Claude Cowork for marketing ops: run a weekly review that preps itself

Using Claude Cowork for marketing ops: run a weekly review that preps itself

Tutorial

[Tutorial](/resources/tutorials/using-claude-cowork-for-marketing-ops-review)Tutorial
