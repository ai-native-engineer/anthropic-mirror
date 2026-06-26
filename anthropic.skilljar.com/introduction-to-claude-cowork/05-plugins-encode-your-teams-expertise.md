<!-- https://anthropic.skilljar.com/introduction-to-claude-cowork/444168 -->

**Estimated time:** 12 minutes

### Learning objectives

By the end of this lesson you'll be able to:

* Define a plugin and what it bundles together
* Recognize the two shapes plugins take
* Install or customize a plugin against a real piece of your work

---

### Watch what a plugin unlocks

The video shows what changes when a team's workflow stops being one person's playbook and becomes a shared toolkit anyone can install.

#### Key takeaways

* **A plugin is a packaged set of skills built around a job.** Where a skill is one playbook, a plugin is several — skills, plus the connectors and subagents they depend on. (A subagent is a purpose-built helper a skill can spin up to handle one part of the work in its own context — e.g., a research subagent for a research step, a drafting subagent for a drafting step.)
* **Plugins teach Claude your team's way of working.** Install a finance plugin and Claude knows the way your team analyzes equities. Install a legal plugin and it knows your contract playbook. The expertise travels with the install, not the person.
* **Anthropic publishes plugins for common roles** — finance, legal, sales, marketing, customer support, product management, and more. You can install one off the shelf, customize it, or build your own.

### Two kinds of plugins

Plugins come in two flavors — both useful, both common.

**Shape 1: An end-to-end process bundled together.** When the work has many sequential steps, you can package the skills for each step into a plugin so the whole process runs as one. For example, a monthly-close plugin might include separate skills for pulling the actuals, building the variance table, and drafting the board memo — each one a step in the larger workflow. Anyone on the team installs the plugin and gets the entire process the way you do it.

**Shape 2: A team's most-used skills bundled together.** This is great for a set of recurring jobs the team does. You can bundle the most important ones into a single plugin. For example, a finance plugin might include separate skills for variance analysis, financial modeling, investment-memo drafting, and quarterly reports. They aren't dependent on each other — they're just the skills the team reaches for most. Bundling them means new teammates install one thing and have the team's whole toolkit.

Explore the interactive below to see the different shapes of plugins.

Two plugins, two shapes

Legal
function's toolkit

Experiment Readout
end-to-end pipeline

## Experiment Readout

Customize

…

Source

Uploaded from file

Version

1.0.0

Last updated

3 days ago

Description

Run an A/B test from raw results to shipped readout.

Skills
Click any skill to see what it does.

Pull experiment exposures and metrics from the warehouse.

/pull-results

Joins exposures to event tables, dedupes by user, returns one row per user per metric for the experiment window.



Break results down by the cuts that matter (platform, plan, geo).

/segment-cuts

Computes lift per segment, flags any segment where the effect reverses sign or loses significance.



Validate traffic balance, sample ratio, and metric definitions.

/sanity-check

Runs a chi-square SRM test, checks pre-period parity, confirms metric definitions match the spec.



Build the lift charts and confidence-interval plots.

/visualize

Generates the team's standard chart pack: lift over time, CI bars, segment heatmap.



Draft the decision memo in the team's readout format.

/write-readout

Headline metric → segment cuts → risks → recommendation. Same shape every readout.



Draft the TL;DR for the experiments channel.

/ship-summary

Drafts a Slack-ready two-line summary with a link to the full readout — you post it.

Connectors
BigQuery
Slack
Hex

## Legal

Customize

…

Source

Marketplace (Anthropic & Partners)

Version

1.2.0

Author

Anthropic

Last updated

9 hours ago

Description

The contract and review work a legal team does most.

Skills
Click any skill to see what it does.

Redline an NDA against the house playbook.

/nda-review

Compares incoming language to the house position; flags deltas; produces a redline + a short rationale per change.



Pull key terms, dates, and obligations from any contract.

/contract-summary

One-page summary: parties, term, fees, termination triggers, indemnity, key dates calendar.



Find pre-approved fallback language for a given clause.

/clause-library

Searches the team's clause bank by topic; returns the approved alternatives in priority order.



Flag jurisdiction-specific issues in a draft.

/regulatory-check

Checks the draft against the jurisdiction's known requirements; flags missing notices or non-compliant clauses.



Pull public filings and prior deal history.

/counterparty-research

Public filings, prior contracts on file, recent press. One-page brief on who you're negotiating with.

Connectors
Box
Egnyte
Slack
M365
Atlassian

*Stay in the loop.* A plugin enables Claude to run your workflows, but the output is still yours to review.

The shape that matters in either case: a plugin is a package built around *workflows*. "Renewal prep for our customer success team" is a plugin. "Equity research for our fund" is a plugin. "The monthly board cycle for the CFO's office" is a plugin.

### Install a plugin from the Anthropic marketplace

Anthropic publishes plugins for the most common roles in knowledge work, each one built and maintained as a starting point you can use as-is or shape to your team. Find them in **Customize → Plugins** in Cowork. Browse for the plugin that matches your work, click **Install**, and approve the connectors the plugin uses. The plugin's skills become available immediately.

### Customize a plugin to fit your team

A plugin from the marketplace is a strong default, not a final answer. The skills and connectors inside use a generic version of the workflow; your team has its own templates, definitions, and steps. You can shape any installed plugin to match.

After you've installed the plugin, go back to **Customize → Plugins → [Plugin name]** and click **Customize**. This opens a new Cowork task where you and Claude work together to tailor the plugin. You can add a starter prompt by directing it to specific assets, sharing context, or uploading the examples you want it to use as a base. Claude will then update the plugin to be true to your team's context.

For example, you could say something like:

> *"Here are our last three red-lined NDAs. Update the /nda-triage skill in this plugin so the format and tone match these."*

Claude adapts the plugin in place. The more you shape it to your team's actual work, the more leverage it produces.

### Build your own plugin

If your team has a workflow that doesn't fit any existing plugin, you can build one by working with Cowork. It will bundle the skills the workflow needs, include any connectors it depends on, and package it for easy installation into your instance of Cowork.

Most teams start small. One skill for the most repetitive task. Then another. By the time it has three or four skills and the connectors that matter, it's a plugin worth sharing — and you'll learn how to share it with your team in Lesson 13.

Your admin may have already published plugins for your organization — check the Directory (Customize → Plugins) before you build anything yourself.

### Try it now

Let's find the plugins that fit your work. In a new Cowork conversation, type:

> /setup-cowork

The skill starts a short interview. Claude asks about the type of work you do, then suggests a plugin that would work best for your needs. You can easily add the plugin right from chat and test it out in the conversation. Once installed, customize it for your team.

### What’s next

You've now made Cowork yours for one piece of your work. The next module is about extending Cowork beyond the desktop — into your browser, and into the M365 apps where a lot of the work lands.

#### Feedback

As you progress through the course, we'd love to hear how you're using concepts from it in your work, plus any feedback you may have. Share your feedback [here](https://docs.google.com/forms/d/e/1FAIpQLScol7ZPi1cxhXy40g0AQieFbhTNQoVNm1Bvvs2gD1giMzOXHQ/viewform).

#### Acknowledgments and license

*Copyright 2026 Anthropic. All rights reserved.*
