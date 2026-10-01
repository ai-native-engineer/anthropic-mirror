<!-- source: https://claude.com/marketplace/plugins/sap-hana-cli -->

Integrates 150+ SAP HANA database tools directly into Claude Code via the Model Context Protocol (MCP). Covers schema exploration, data import/export, performance monitoring, security auditing, backup management, and developer tooling — for both SAP HANA Cloud and on-premise databases. The plugin wraps the open-source **hana-cli** project, giving your AI assistant full access to database administration and development commands without leaving the conversation.

Key capabilities span eight categories: **schema exploration** (list tables, views, procedures, functions, schemas), **object inspection** (examine columns, view definitions, procedure parameters), **data tools** (CSV/Excel/JSON import and export, data quality profiling, validation), **performance monitoring** (expensive statements, memory usage, blocking sessions, deadlocks), **security** (user and role management, privilege analysis, audit logs), **backup & recovery**, **system administration** (health checks, diagnostics, INI configuration), and **developer tools** (CDS generation, code templates, test data, HDI container management).

**How to use:** After installing, configure your SAP HANA connection credentials (the plugin checks `default-env.json`, `.env`, and other standard sources, or run `npx hana-cli connect` to set up interactively). Then ask Claude naturally:

`What tables exist in my HANA database?` · `Show me the most expensive SQL statements` · `Export the PRODUCTS table to CSV` · `Profile data quality for the ORDERS table` · `Compare schemas between DEV and PROD` · `List all user privileges and run a security audit` · `Check system health and memory usage` · `Generate a CDS entity definition for my table`

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
