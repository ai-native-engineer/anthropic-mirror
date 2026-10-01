<!-- https://anthropic.skilljar.com/introduction-to-claude-cowork/444168 -->

### ⁠

## What you'll learn

*Estimated time: 15 minutes*

By the end of this lesson you'll be able to:

* Define a plugin and what it bundles together
* Recognize the two shapes plugins take
* Install or customize a plugin against a real piece of your work

## Watch what a plugin unlocks

The video shows what changes when a team's workflow stops being one
person's playbook and becomes a shared toolkit anyone can install.

## Key takeaways

* **A plugin is a packaged set of skills built around a job.** Where a skill is one playbook, a plugin is several — skills, plus the connectors and subagents they depend on. (A subagent is a purpose-built helper a skill can spin up to handle one part of the work in its own context — e.g., a research subagent for a research step, a drafting subagent for a drafting step.)
* **Plugins teach Claude your team's way of working.** Install a finance plugin and Claude knows the way your team analyzes equities. Install a legal plugin and it knows your contract playbook. The expertise travels with the install, not the person.
* **Anthropic publishes plugins for common roles** — finance, legal, sales, marketing, customer support, product management, and more. You can install one off the shelf, customize it, or build your own.

## Two kinds of plugins

Plugins come in two flavors — both useful, both common.

**Shape 1: An end-to-end process bundled together.** When the work has many sequential steps, you can package the skills for each step into a plugin so the whole process runs as one. For example, a monthly-close plugin might include separate skills for pulling the actuals, building the variance table, and drafting the board memo — each one a step in the larger workflow. Anyone on the team installs the plugin and gets the entire process the way you do it.

**Shape 2: A team's most-used skills bundled together.** This is great for a set of recurring jobs the team does. You can bundle the most important ones into a single plugin. For example, a finance plugin might include separate skills for variance analysis, financial modeling, investment-memo drafting, and quarterly reports. They aren't dependent on each other — they're just the skills the team reaches for most. Bundling them means new teammates install one thing and have the team's whole toolkit.

Explore the interactive below to see the different shapes of plugins.

The shape that matters in either case: a plugin is a package built around *workflows*. "Renewal prep for our customer success team" is a plugin. "Equity research for our fund" is a plugin. "The monthly board cycle for the CFO's office" is a plugin.

## Install a plugin from the Anthropic marketplace

Anthropic publishes plugins for the most common roles in knowledge work, each one built and maintained as a starting point you can use as-is or shape to your team. Find them in **Customize → Plugins** in Cowork. Browse for the plugin that matches your work, click **Install**, and approve the connectors the plugin uses. The plugin's skills become available immediately.

## Customize a plugin to fit your team

A plugin from the marketplace is a strong default, not a final answer. The skills and connectors inside use a generic version of the workflow; your team has its own templates, definitions, and steps. You can shape any installed plugin to match.

After you've installed the plugin, go back to **Customize → Plugins → [Plugin name]** and click **Customize**. This opens a new Cowork task where you and Claude work together to tailor the plugin. You can add a starter prompt by directing it to specific assets, sharing context, or uploading the examples you want it to use as a base. Claude will then update the plugin to be true to your team's context.

For example, you could say something like:

Here are our last three red-lined NDAs. Update the /nda-triage skill in this plugin so the format and tone match these.

[Open in Cowork](claude://cowork/new?q=Here%20are%20our%20last%20three%20red-lined%20NDAs.%20Update%20the%20%2Fnda-triage%20skill%20in%20this%20plugin%20so%20the%20format%20and%20tone%20match%20these.)

Claude adapts the plugin in place. The more you shape it to your team's actual work, the more leverage it produces.

## Build your own plugin

If your team has a workflow that doesn't fit any existing plugin, you can build one by working with Cowork. It will bundle the skills the workflow needs, include any connectors it depends on, and package it for easy installation into your instance of Cowork.

Most teams start small. One skill for the most repetitive task. Then another. By the time it has three or four skills and the connectors that matter, it's a plugin worth sharing — and you'll learn how to share it with your team in Lesson 13.

Your admin may have already published plugins for your organization — check the Directory (Customize → Plugins) before you build anything yourself.

## Try it now

Let's find the plugins that fit your work. In a new Cowork conversation, type:

/setup-claude

[Open in Cowork](claude://cowork/new?q=%2Fsetup-claude)

The skill starts a short interview. Claude asks about the type of work you do, then suggests a plugin that would work best for your needs. You can easily add the plugin right from chat and test it out in the conversation. Once installed, customize it for your team.

## What’s next

You've now made Cowork yours for one piece of your work. The next module is about extending Cowork beyond the desktop — into your browser, and into the M365 apps where a lot of the work lands.

<!-- embed: https://academy.claude.com/embed/courses/introduction-to-claude-cowork/PluginShapesExplorer -->

Explorer: a mock plugin detail page lets the learner switch between two sample plugins, one a function's toolkit and one an end-to-end pipeline, clicking metadata, toggle, description, skills, and connectors to reveal explanations of each part.

Two plugins, two shapes

### Legal

…

SkillsClick any skill to see what it does.

*Stay in the loop.* A plugin enables Claude to run your workflows, but the output is still yours to review.
<!-- yt-pending: v5IOHK5xFlc -->

_(영상 자막 없음 또는 추출 실패)_
