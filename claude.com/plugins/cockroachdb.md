<!-- source: https://claude.com/plugins/cockroachdb -->

# CockroachDB

CockroachDB plugin for Claude Code — explore schemas, write SQL, debug queries, manage clusters

* Install in

  [Claude Code](#)

  [Cockroach Labs](https://www.cockroachlabs.com)
* Installs

  1796

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Connect Claude Code directly to your CockroachDB clusters for hands-on database work. This plugin provides three core MCP tools — execute SQL, list schemas, and list tables — letting you explore database structure, run queries, and manage data without leaving your coding session. It includes a specialized DBA agent with deep knowledge of CockroachDB distributed SQL internals for diagnosing performance issues, reviewing schema designs, analyzing query plans, and planning multi-region deployments.

The plugin ships with 22+ structured skills across 9 operational domains: onboarding and migrations (MOLT fetch, replicator, and verify), observability and diagnostics (range distribution analysis, statement and transaction fingerprint profiling, live SQL activity triage), operations and lifecycle (cluster provisioning, maintenance, upgrades, health reviews), and security and governance (audit logging, TLS certificates, SSO/SCIM, CMEK encryption, compliance documentation). Built-in safety hooks validate SQL before execution and check SQL files after edits to prevent destructive operations and catch anti-patterns.

**How to use:** Install with `claude plugin install cockroachdb`, then set your connection environment variables (COCKROACHDB\_HOST, COCKROACHDB\_PORT, COCKROACHDB\_USER, COCKROACHDB\_PASSWORD, COCKROACHDB\_DATABASE). Try prompts like: "List all tables in my database and describe their schemas", "Write an optimized query to find the top 10 customers by order volume", "Analyze the EXPLAIN plan for this slow query and suggest indexes", "Review my schema for write hotspot risks", or "Help me plan a multi-region deployment for this cluster". Use the DBA agent for autonomous deep-dive diagnostics with prompts like "Diagnose why this query is slow" or "Check my cluster health and recommend improvements".

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
