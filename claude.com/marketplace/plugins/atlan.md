<!-- source: https://claude.com/marketplace/plugins/atlan -->

Connect Claude Code to your Atlan data catalog and interact with your entire data estate through natural language. This plugin provides 15 MCP tools (12 enabled by default, 3 via feature flags) for discovering, exploring, governing, and managing data assets — all powered by the Atlan MCP server with secure OAuth 2.1 authentication requiring no API keys.

Core capabilities include semantic search across your data catalog, upstream and downstream lineage traversal, asset metadata updates, glossary management (glossaries, terms, and categories), data mesh operations (domains and data products), and data quality rule creation, scheduling, and management. Three additional tools for structured asset search, DSL-based querying, and SQL execution are available via tenant feature flags.

**How to use:** After installing, authenticate by running `/mcp` in Claude Code — this opens a browser-based login flow. Then interact with your catalog using natural language prompts like:

* "Search for all tables related to customer revenue"
* "Show me the upstream lineage for the orders\_fact table"
* "Create a glossary term called 'Monthly Active Users' with a definition"
* "Set the certification status of the payments table to VERIFIED"
* "Create a data quality rule to check for null values in the email column"
* "List all data products in the Finance domain"

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
