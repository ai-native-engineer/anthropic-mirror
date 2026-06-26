<!-- source: https://claude.com/plugins/lovable -->

# Lovable

Build, iterate on, deploy, and manage Lovable apps from Claude Code. Bundles the official Lovable MCP server (remote,...

* Install in

  [Claude Code](#)

  [Lovable](https://lovable.dev)
* Installs

  32

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Build, iterate on, deploy, and manage full-stack Lovable apps without leaving Claude Code. This plugin bundles the official Lovable MCP server (remote, OAuth 2.1 — no API keys to configure) and adds focused commands for the most common workflows: creating new apps, sending change requests, managing Cloud Postgres databases, and publishing to live URLs.

The plugin connects to Lovable's AI-powered app builder through three streamlined commands. `/lovable:build` creates a new project from a description, monitors the build, and optionally deploys it to a public URL. `/lovable:iterate` sends change requests to an existing project, shows unified diffs for review, and lets you continue refining or publish. `/lovable:db` manages your project's Cloud Postgres database — check status, provision new databases, run SQL queries, and retrieve connection info.

Safety prompts are built in: you'll be asked to confirm before spending build credits, before publishing to a public URL, and before executing any write or schema-altering SQL. Beyond the three main commands, the plugin gives access to the full Lovable MCP toolset including project inspection, edit history, analytics, file uploads, and external integrations with Linear, Notion, and Slack.

**How to use:** Run `/lovable:build` to create a new app (e.g., "build me a project tracker with a Kanban board"). Use `/lovable:iterate` to request changes to an existing project (e.g., "add dark mode to my project"). Use `/lovable:db` to manage your project's database (e.g., "show me all users in my app's database"). You can also ask naturally — "deploy my Lovable project" or "check the database status for my app" — and the plugin's tools will handle it.

## Related plugins

[### Frontend Design

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

Anthropic verified

948012

installs](/plugins/frontend-design)

[### Superpowers

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

855112

installs](/plugins/superpowers)

[### Code Review

AI code review with specialized agents and confidence-based filtering for pull requests

Anthropic verified

383892

installs](/plugins/code-review)

[### Context7

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

377529

installs](/plugins/context7)
