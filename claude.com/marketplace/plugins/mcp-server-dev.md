<!-- source: https://claude.com/marketplace/plugins/mcp-server-dev -->

A comprehensive guide for designing and building MCP (Model Context Protocol) servers that work seamlessly with Claude. This plugin provides three composable skills that walk you through the entire process — from choosing the right deployment model and tool design patterns to scaffolding code, adding authentication, and packaging for distribution. It covers remote streamable-HTTP servers, interactive MCP apps with embedded UI widgets, and MCPB bundles for local machine access.

The core **build-mcp-server** skill follows a structured five-phase workflow: it interrogates your use case, recommends a deployment model (remote HTTP, elicitation, MCP app, MCPB, or local stdio), selects a tool-design pattern (one-tool-per-action vs. search+execute for large APIs), picks a framework (TypeScript SDK or FastMCP for Python), and scaffolds your project. The **build-mcp-app** skill adds interactive UI capabilities — form widgets, searchable pickers, confirmation dialogs, charts, and live-updating status displays — rendered directly in chat via sandboxed iframes. The **build-mcpb** skill handles packaging local stdio servers with their runtime into installable bundles that require no Node.js or Python on the user's machine.

**How to use:** Invoke the entry skill with `/mcp-server-dev:build-mcp-server` or simply ask "help me build an MCP server" to start the guided workflow. Use `/mcp-server-dev:build-mcp-app` when you need to add interactive widgets like contact pickers or confirmation dialogs to your server. Use `/mcp-server-dev:build-mcpb` to package a local server into a distributable MCPB bundle. Each skill includes reference files covering auth flows, widget templates, iframe sandbox constraints, manifest schemas, and security hardening guidelines.

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
