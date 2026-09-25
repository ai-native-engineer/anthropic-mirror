<!-- source: https://claude.com/marketplace/plugins/cockroachdb -->

Connect Claude Code directly to your CockroachDB clusters for hands-on database work. This plugin provides three core MCP tools — execute SQL, list schemas, and list tables — letting you explore database structure, run queries, and manage data without leaving your coding session. It includes a specialized DBA agent with deep knowledge of CockroachDB distributed SQL internals for diagnosing performance issues, reviewing schema designs, analyzing query plans, and planning multi-region deployments.

The plugin ships with 22+ structured skills across 9 operational domains: onboarding and migrations (MOLT fetch, replicator, and verify), observability and diagnostics (range distribution analysis, statement and transaction fingerprint profiling, live SQL activity triage), operations and lifecycle (cluster provisioning, maintenance, upgrades, health reviews), and security and governance (audit logging, TLS certificates, SSO/SCIM, CMEK encryption, compliance documentation). Built-in safety hooks validate SQL before execution and check SQL files after edits to prevent destructive operations and catch anti-patterns.

**How to use:** Install with `claude plugin install cockroachdb`, then set your connection environment variables (COCKROACHDB\_HOST, COCKROACHDB\_PORT, COCKROACHDB\_USER, COCKROACHDB\_PASSWORD, COCKROACHDB\_DATABASE). Try prompts like: "List all tables in my database and describe their schemas", "Write an optimized query to find the top 10 customers by order volume", "Analyze the EXPLAIN plan for this slow query and suggest indexes", "Review my schema for write hotspot risks", or "Help me plan a multi-region deployment for this cluster". Use the DBA agent for autonomous deep-dive diagnostics with prompts like "Diagnose why this query is slow" or "Check my cluster health and recommend improvements".

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
