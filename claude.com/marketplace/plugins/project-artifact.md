<!-- source: https://claude.com/marketplace/plugins/project-artifact -->

Generate a polished, tabbed project status page and publish it as a shareable claude.ai artifact. Designed for migrations, launches, research efforts, and any initiative with multiple workstreams tracked over time. The artifact includes an overview with success criteria, a workstream sequence view, a persistent "next steps" strip, and optional tabs for background, plan, risks, and decisions — each included only when substantive.

Each artifact is backed by a per-project config stored on your machine. When you refresh, the plugin re-gathers live state, redeploys to the same URL, and reports only what changed since the last render. Your team always sees the latest status at a single stable link. Pages default to private and can be shared from the claude.ai viewer.

For PR-driven software projects, the plugin automatically sequences pull requests to show dependency order and pulls live PR status, CI check results, and unresolved review threads via the `gh` CLI. Status pills (`done`, `now`, `next`, `warn`) give an at-a-glance view of progress. The page supports light and dark mode, is fully responsive, and embeds all styles inline — no external dependencies.

**How to use:** Run `/project-artifact my-project` and point it at your project sources (repos, docs, trackers). The plugin gathers context, generates a self-contained HTML page, and publishes it as a private artifact. To update it later, just say "refresh the artifact" — it redeploys to the same URL with a delta summary of what changed. Requires the built-in Artifact tool (claude.ai login). The `gh` CLI is optional but recommended for GitHub-based projects.

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
