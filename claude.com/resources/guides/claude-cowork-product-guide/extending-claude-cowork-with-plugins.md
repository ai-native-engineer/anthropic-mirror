<!-- source: https://claude.com/resources/guides/claude-cowork-product-guide/extending-claude-cowork-with-plugins -->

Chapter 044 min read

# Extending Claude Cowork with plugins

4 min read

19 min remaining

Out of the box, Claude Cowork can read your files, run code in a sandbox, browse the web, and connect to a growing list of apps through MCP connectors. Plugins go further: they bundle [skills (opens in new tab)](https://agentskills.io/home), [sub-agents (opens in new tab)](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork), and [connectors (opens in new tab)](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities) into a single installable package built around a specific job.

A plugin is a pre-built toolkit for a role or workflow. Instead of wiring up connectors one at a time and re-explaining how your team works every session, you install a plugin and Claude knows the vocabulary, the steps, and the outputs your workflow expects.

## What's inside a plugin

A plugin can include any combination of:

* [Skills (opens in new tab)](https://agentskills.io/home): step-by-step playbooks Claude loads automatically when a task matches. A "contract review" skill might tell Claude which clauses to flag, what your standard fallback positions are, and how to format the redline.
* [Subagents (opens in new tab)](https://code.claude.com/docs/en/sub-agents): purpose-built assistants for specific kinds of work. Each runs in its own context window with a custom system prompt, specific tool access, and independent permissions.
* [Connectors (opens in new tab)](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities): the MCP integrations the plugin depends on (Salesforce, Asana, Slack, internal tools), bundled so you don't have to hunt for them.

## When to reach for a plugin

Plugins earn their keep when your request depends on your org's specific context — your pipeline, your playbooks, your templates, your customers. Good signals:

* You keep re-explaining the same workflow to Claude every session.
* The task touches several tools in sequence (pull from CRM, draft in Docs, send via Slack).
* There's a "right way" your team does this thing, and you want Claude to follow it consistently.

For one-off questions or general knowledge ("what's MEDDIC?", "draft a cold email"), skip the plugin and just ask.

## Installing a plugin

Browse available plugins from the [Claude Cowork plugin marketplace (opens in new tab)](https://github.com/anthropics/knowledge-work-plugins/tree/main), or wait for Claude to suggest one when it notices your request would benefit. Installation is a single click: approve the plugin and from there, you can use individual skills or chained skills in a workflow. You can disable or remove a plugin at any time from settings.

## Building your own plugins

If your team has a workflow that doesn't exist as a plugin yet, you can build one. A plugin is a folder that can include skill files (Markdown with instructions), slash commands, subagents for specialized tasks that need their own context and tool permissions, and a manifest listing any MCP servers it depends on. Most teams start with a single skill for their most repetitive task and grow from there—adding a subagent when a job is big enough to warrant its own isolated context. Plugins can stay private to your org or be published to a marketplace for others to install.

## A quick example

Say you run customer success and every renewal call follows the same prep ritual: pull the account from Salesforce, check recent Zendesk tickets, skim the last three Gong calls, and drop a briefing in a Google Doc.

Without a plugin, you explain that sequence to Claude every time. With a "Renewal prep" plugin installed, you type `/prep-renewal Acme Corp` and Claude runs the whole chain — connectors already wired up, format already defined, briefing landed in the right folder.
