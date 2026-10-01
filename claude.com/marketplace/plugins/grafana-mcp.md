<!-- source: https://claude.com/marketplace/plugins/grafana-mcp -->

Connects Claude Code to a live Grafana instance via the official Grafana MCP server, adding 40+ tools for AI-assisted observability workflows. Manage dashboards, datasources, alerting rules, incidents, and on-call schedules directly from your editor. Query Prometheus metrics and Loki logs, create and patch dashboards, manage contact points, and deep-link to specific panels — all through natural language.

The plugin runs the official `grafana/mcp-grafana` Docker image and covers nine major tool categories: Dashboards (search, summarize, patch), Datasources (list, retrieve), Prometheus (query execution, metric exploration), Loki (log and metric analysis), Alerting (rule and contact point management), Incidents (creation and activity tracking), OnCall (schedule and shift visibility), Navigation (deep linking), and Annotations (CRUD and tag management).

Requires Docker and a Grafana service account token. Viewer role provides read access; Editor role enables write operations. Works with both self-hosted Grafana and Grafana Cloud instances.

**How to use:** After installing and configuring your Grafana URL and service account token, try prompts like: `"Show me all dashboards related to API latency"`, `"Query Prometheus for the p99 request duration over the last hour"`, `"Create an alert rule for when error rate exceeds 5%"`, `"Search Loki logs for errors in the auth service"`, or `"List all active incidents and their current status"`.

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
