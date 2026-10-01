<!-- source: https://claude.com/marketplace/plugins/lovable -->

Build, iterate on, deploy, and manage full-stack Lovable apps without leaving Claude Code. This plugin bundles the official Lovable MCP server (remote, OAuth 2.1 — no API keys to configure) and adds focused commands for the most common workflows: creating new apps, sending change requests, managing Cloud Postgres databases, and publishing to live URLs.

The plugin connects to Lovable's AI-powered app builder through three streamlined commands. `/lovable:build` creates a new project from a description, monitors the build, and optionally deploys it to a public URL. `/lovable:iterate` sends change requests to an existing project, shows unified diffs for review, and lets you continue refining or publish. `/lovable:db` manages your project's Cloud Postgres database — check status, provision new databases, run SQL queries, and retrieve connection info.

Safety prompts are built in: you'll be asked to confirm before spending build credits, before publishing to a public URL, and before executing any write or schema-altering SQL. Beyond the three main commands, the plugin gives access to the full Lovable MCP toolset including project inspection, edit history, analytics, file uploads, and external integrations with Linear, Notion, and Slack.

**How to use:** Run `/lovable:build` to create a new app (e.g., "build me a project tracker with a Kanban board"). Use `/lovable:iterate` to request changes to an existing project (e.g., "add dark mode to my project"). Use `/lovable:db` to manage your project's database (e.g., "show me all users in my app's database"). You can also ask naturally — "deploy my Lovable project" or "check the database status for my app" — and the plugin's tools will handle it.

## Other plugins

### [Frontend Design](https://claude.com/marketplace/plugins/frontend-design)

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

### [Superpowers](https://claude.com/marketplace/plugins/superpowers)

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

### [Code Review](https://claude.com/marketplace/plugins/code-review)

AI code review with specialized agents and confidence-based filtering for pull requests

### [Context7](https://claude.com/marketplace/plugins/context7)

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

### [Code Simplifier](https://claude.com/marketplace/plugins/code-simplifier)

Code clarity agent: simplifies and refines recently modified code while preserving functionality and consistency.

### [Playwright](https://claude.com/marketplace/plugins/playwright)

Browser automation and end-to-end testing MCP server by Microsoft. Enables Claude to interact with web pages, take screenshots, fill forms, and automate testing workflows.
