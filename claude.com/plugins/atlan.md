<!-- source: https://claude.com/plugins/atlan -->

# Atlan

Atlan data catalog for Claude Code. Search, explore, govern, and manage data assets through natural language.

* Install in

  [Claude Code](#)

  [Atlan](https://atlan.com)
* Installs

  1681

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Connect Claude Code to your Atlan data catalog and interact with your entire data estate through natural language. This plugin provides 15 MCP tools (12 enabled by default, 3 via feature flags) for discovering, exploring, governing, and managing data assets — all powered by the Atlan MCP server with secure OAuth 2.1 authentication requiring no API keys.

Core capabilities include semantic search across your data catalog, upstream and downstream lineage traversal, asset metadata updates, glossary management (glossaries, terms, and categories), data mesh operations (domains and data products), and data quality rule creation, scheduling, and management. Three additional tools for structured asset search, DSL-based querying, and SQL execution are available via tenant feature flags.

**How to use:** After installing, authenticate by running `/mcp` in Claude Code — this opens a browser-based login flow. Then interact with your catalog using natural language prompts like:

* "Search for all tables related to customer revenue"
* "Show me the upstream lineage for the orders\_fact table"
* "Create a glossary term called 'Monthly Active Users' with a definition"
* "Set the certification status of the payments table to VERIFIED"
* "Create a data quality rule to check for null values in the email column"
* "List all data products in the Finance domain"

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
