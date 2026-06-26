<!-- source: https://claude.com/plugins/project-artifact -->

# Project Artifact

Build a live, shareable project status page that auto-refreshes and shows state deltas.

* Anthropic Verified
* Install in

  [Claude Code](#)

  [Anthropic](https://anthropic.com)
* Installs

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Generate a polished, tabbed project status page and publish it as a shareable claude.ai artifact. Designed for migrations, launches, research efforts, and any initiative with multiple workstreams tracked over time. The artifact includes an overview with success criteria, a workstream sequence view, a persistent "next steps" strip, and optional tabs for background, plan, risks, and decisions — each included only when substantive.

Each artifact is backed by a per-project config stored on your machine. When you refresh, the plugin re-gathers live state, redeploys to the same URL, and reports only what changed since the last render. Your team always sees the latest status at a single stable link. Pages default to private and can be shared from the claude.ai viewer.

For PR-driven software projects, the plugin automatically sequences pull requests to show dependency order and pulls live PR status, CI check results, and unresolved review threads via the `gh` CLI. Status pills (`done`, `now`, `next`, `warn`) give an at-a-glance view of progress. The page supports light and dark mode, is fully responsive, and embeds all styles inline — no external dependencies.

**How to use:** Run `/project-artifact my-project` and point it at your project sources (repos, docs, trackers). The plugin gathers context, generates a self-contained HTML page, and publishes it as a private artifact. To update it later, just say "refresh the artifact" — it redeploys to the same URL with a delta summary of what changed. Requires the built-in Artifact tool (claude.ai login). The `gh` CLI is optional but recommended for GitHub-based projects.

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
