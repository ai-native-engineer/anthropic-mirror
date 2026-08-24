<!-- source: https://academy.claude.com/tutorials/how-to-build-a-plugin-from-scratch-in-cowork -->

A Cowork plugin is a group of files that can teach Claude how to do a specific job — encoding your methodology, your workflows, your tool connections.

Anthropic publishes [pre-built plugins(opens in new tab)](https://claude.com/plugins) for common roles like [Sales(opens in new tab)](https://claude.com/plugins/sales), [Finance(opens in new tab)](https://claude.com/plugins/finance), and [Legal(opens in new tab)](https://claude.com/plugins/legal). Customizing those with your company's context can help tailor the plugin to your needs. Building from scratch is for when your team has workflows, processes, or institutional knowledge that existing plugins don't cover.

*To learn more about installing and using plugins in Cowork,* [*visit here*(opens in new tab)](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)*.*

## Why build from scratch

* **Your workflow doesn't map to an existing plugin.** Your workflow has specifics that an existing plugin doesn't cover, and customizing one doesn't close the gap.
* **You want to encode institutional knowledge for your team.** The way your team actually does things — your standards, your judgment calls, your process docs — packaged so everyone works from the same playbook.
* **You need Claude to coordinate across your tools.** Your workflow pulls from a particular combination of data sources, applies particular criteria, and produces a particular deliverable.

## What's inside a plugin

A plugin can include a few types of components. Claude builds the right combination based on what you describe.

#### **Skills —** the knowledge and workflows that shape how Claude works.

A skill might be a few lines describing a formatting preference, a detailed methodology covering your full review framework, or a structured workflow you trigger by typing `/` in your prompt. Claude reads each skill's description and draws on it when it matches what you're working on — or you invoke it directly from the slash menu.

Skills can carry supporting reference documents — playbooks, compliance frameworks, pricing matrices — that Claude loads when relevant. They can accept inputs, so `/close-package North America` and `/close-package Europe` run the same process with different scope. Recurring skills can run as [scheduled tasks(opens in new tab)](https://support.claude.com/en/articles/13345190-get-started-with-cowork#h_260d21b5b3) with your criteria applied each time, and skills can chain to each other, where the output of one feeds the next.

#### **Connectors** — link Claude to your tools.

A plugin works without connectors — you can upload data manually or describe the situation — but connected tools let Claude pull what it needs mid-workflow and write results back.

You can direct Claude to search broadly across a connected tool or look in a specific place, depending on what the workflow needs.

#### **Sub-agents** — specialized helpers for complex tasks.

One agent might research a company while another pulls data from your CRM and a third scans Slack for context. They can run in parallel or in sequence, each with its own focus and fresh context window.

## How to create a plugin

Understanding the components within a plugin can give you a framework for what to share while building one: your **knowledge, judgment calls, and repeatable tasks** become skills, your **data sources** become connectors. If you have existing documents or examples of deliverables you've been happy with, share them — Claude maps it to the relevant parts of the plugin.

In Cowork, describe the plugin you want to build — even a sentence is enough to start.

![The Cowork home screen with a prompt describing a plugin to build for a procurement team](https://academy.claude.com/assets/media/d922d57dc690563b0bf76462529ab967ff2a9b677984f3f052c6dcbc0a4382ba.png)

A simpler start works too — Claude will follow up with questions about your workflow, your tools, your standards, and how you handle edge cases.

I need a plugin for our customer success team



Open in Cowork

## What changes with a plugin

With detailed instructions, Claude can handle many of these workflows. A plugin packages them into skills anyone on the team can run.

### [Finance(opens in new tab)](https://claude.com/plugins/finance)

Here's our P&L. Materiality threshold is $25K. Decompose by price, volume, and mix. Check these GL accounts against the subledger. Format the JE with debits on top.



Open in Cowork

###### **Without a plugin:** Claude can handle it, but restating your full close methodology every session is overhead that compounds, and the output might vary depending on who's giving Claude the instructions.

`/monthly-close` North America



Open in Cowork

###### **With your plugin:** Skills load your chart of accounts, materiality thresholds, close calendar, and narrative standards. Connectors pull from your data warehouse. The skill runs the full process — a new analyst runs it and gets consistent rigor.

### [Sales(opens in new tab)](https://claude.com/plugins/sales)

Pull usage data for Meridian Health from our analytics dashboard. Check for support escalations in the last 90 days. Compare their current contract against our pricing tiers. Score the renewal risk and flag expansion opportunities.



Open in Cowork

###### **Without a plugin:** You're directing Claude to each source, restating your scoring criteria, and specifying the output format every time.

`/renewal-score` Meridian Health



Open in Cowork

###### **With your plugin:** Skills hold your scoring criteria and competitive positioning. Connectors pull from your CRM and analytics dashboard. Claude scores the account and flags expansion opportunities — consistent quality whether a senior rep or a new hire runs it.

### [Legal(opens in new tab)](https://claude.com/plugins/legal)

Review this vendor agreement. Our standard on indemnification is capped at 2x contract value. Flag auto-renewals over 12 months. Use GREEN/YELLOW/RED.



Open in Cowork

###### **Without a plugin:** This prompt covers a few checks on one contract. A full review applies dozens of standard positions across every clause type, and you'd need to restate all of them for each new agreement.

`/due-diligence`



Open in Cowork

###### **With your plugin:** Skills hold your standard positions across every clause type and your severity classifications. A connector accesses the data room. Claude reviews every document against your playbook and produces a risk-rated summary.

## Refining your plugin

* **Use it on real work and refine as you go.** If you run a skill and something's off — a step is missing, the criteria need adjusting, the output format isn't right — tell Claude and it can update the plugin files directly. Looking through the files after Claude builds them can also help spot gaps early.
* **Show Claude the deliverable.** Upload an example or point Claude to one in a connected drive. Claude picks up the structure, emphasis, and formatting directly.
* **Keep skills focused.** Claude composes multiple skills when a task spans several areas, and focused skills with specific descriptions tend to activate more reliably than broad ones. If a skill isn't loading when you expect, its description is likely too vague — structure it as *what it does, when to use it, what it covers.*
* **Consider subagents for multi-source or long-running tasks.** If a workflow pulls from several tools at once, or if a task regularly hits context limits from processing too much in one pass, subagents let Claude split the work across separate context windows.

## Things to know

* **Plugins work in Cowork, Code, and Chat.** Your plugin's skills are active in whichever surface you're using.
* **Plugins you add yourself live on that machine.** A plugin you build or install manually is stored locally, so it typically doesn't follow your account to your other devices — including into remote sessions (in beta), where Claude works on Anthropic's servers. Plugins your organization distributes work differently: they usually come from a private marketplace your admin manages, and an admin can make a plugin available for people to install or have it installed by default.
* **Sharing with teammates isn't automatic, but you have options.** You can share a plugin as a compressed file, host it on GitHub for automatic updates, or have an admin provision it across your org. [*Learn more about sharing plugins.*(opens in new tab)](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)
* **Skills and connectors can also live outside plugins.** If you have personal context that applies across everything you do in Cowork — not tied to one plugin — you can add standalone skills and connectors in settings.

*Cowork with plugins is generally available for all paid Claude plans (Pro, Max, Team, Enterprise) on macOS and Windows. Browse* [*available plugins*(opens in new tab)](https://claude.com/plugins)*.*

## Learn more

* [Getting started with Cowork(opens in new tab)](https://support.claude.com/en/articles/13345190-getting-started-with-cowork)
* [Using plugins in Cowork(opens in new tab)](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)
* [Browse plugins(opens in new tab)](https://claude.com/plugins)
