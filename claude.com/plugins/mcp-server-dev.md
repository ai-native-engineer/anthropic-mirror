<!-- source: https://claude.com/plugins/mcp-server-dev -->

# MCP Server Dev

Design and build MCP servers for Claude. Learn deployment (HTTP, MCPB, local), tools, auth, and interactive apps.

* Anthropic Verified
* Install in

  [Claude Code](#)

  [Anthropic](https://anthropic.com)
* Installs

  24571

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

A comprehensive guide for designing and building MCP (Model Context Protocol) servers that work seamlessly with Claude. This plugin provides three composable skills that walk you through the entire process — from choosing the right deployment model and tool design patterns to scaffolding code, adding authentication, and packaging for distribution. It covers remote streamable-HTTP servers, interactive MCP apps with embedded UI widgets, and MCPB bundles for local machine access.

The core **build-mcp-server** skill follows a structured five-phase workflow: it interrogates your use case, recommends a deployment model (remote HTTP, elicitation, MCP app, MCPB, or local stdio), selects a tool-design pattern (one-tool-per-action vs. search+execute for large APIs), picks a framework (TypeScript SDK or FastMCP for Python), and scaffolds your project. The **build-mcp-app** skill adds interactive UI capabilities — form widgets, searchable pickers, confirmation dialogs, charts, and live-updating status displays — rendered directly in chat via sandboxed iframes. The **build-mcpb** skill handles packaging local stdio servers with their runtime into installable bundles that require no Node.js or Python on the user's machine.

**How to use:** Invoke the entry skill with `/mcp-server-dev:build-mcp-server` or simply ask "help me build an MCP server" to start the guided workflow. Use `/mcp-server-dev:build-mcp-app` when you need to add interactive widgets like contact pickers or confirmation dialogs to your server. Use `/mcp-server-dev:build-mcpb` to package a local server into a distributable MCPB bundle. Each skill includes reference files covering auth flows, widget templates, iframe sandbox constraints, manifest schemas, and security hardening guidelines.

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
