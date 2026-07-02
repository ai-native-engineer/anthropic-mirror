<!-- source: https://claude.com/plugins/grafana-mcp -->

# Grafana MCP

MCP server for AI-assisted Grafana dashboard, datasource, alerting, and incident management.

  [Grafana Labs](https://grafana.com)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Connects Claude Code to a live Grafana instance via the official Grafana MCP server, adding 40+ tools for AI-assisted observability workflows. Manage dashboards, datasources, alerting rules, incidents, and on-call schedules directly from your editor. Query Prometheus metrics and Loki logs, create and patch dashboards, manage contact points, and deep-link to specific panels — all through natural language.

The plugin runs the official `grafana/mcp-grafana` Docker image and covers nine major tool categories: Dashboards (search, summarize, patch), Datasources (list, retrieve), Prometheus (query execution, metric exploration), Loki (log and metric analysis), Alerting (rule and contact point management), Incidents (creation and activity tracking), OnCall (schedule and shift visibility), Navigation (deep linking), and Annotations (CRUD and tag management).

Requires Docker and a Grafana service account token. Viewer role provides read access; Editor role enables write operations. Works with both self-hosted Grafana and Grafana Cloud instances.

**How to use:** After installing and configuring your Grafana URL and service account token, try prompts like: `"Show me all dashboards related to API latency"`, `"Query Prometheus for the p99 request duration over the last hour"`, `"Create an alert rule for when error rate exceeds 5%"`, `"Search Loki logs for errors in the auth service"`, or `"List all active incidents and their current status"`.
