<!-- source: https://claude.com/plugins/sap-hana-cli -->

# SAP HANA CLI

150+ SAP HANA database tools for AI: query, import/export, profile, compare, backup, monitor. Cloud/on-premise.

  [SAP SE](https://www.sap.com)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Integrates 150+ SAP HANA database tools directly into Claude Code via the Model Context Protocol (MCP). Covers schema exploration, data import/export, performance monitoring, security auditing, backup management, and developer tooling — for both SAP HANA Cloud and on-premise databases. The plugin wraps the open-source **hana-cli** project, giving your AI assistant full access to database administration and development commands without leaving the conversation.

Key capabilities span eight categories: **schema exploration** (list tables, views, procedures, functions, schemas), **object inspection** (examine columns, view definitions, procedure parameters), **data tools** (CSV/Excel/JSON import and export, data quality profiling, validation), **performance monitoring** (expensive statements, memory usage, blocking sessions, deadlocks), **security** (user and role management, privilege analysis, audit logs), **backup & recovery**, **system administration** (health checks, diagnostics, INI configuration), and **developer tools** (CDS generation, code templates, test data, HDI container management).

**How to use:** After installing, configure your SAP HANA connection credentials (the plugin checks `default-env.json`, `.env`, and other standard sources, or run `npx hana-cli connect` to set up interactively). Then ask Claude naturally:

`What tables exist in my HANA database?` · `Show me the most expensive SQL statements` · `Export the PRODUCTS table to CSV` · `Profile data quality for the ORDERS table` · `Compare schemas between DEV and PROD` · `List all user privileges and run a security audit` · `Check system health and memory usage` · `Generate a CDS entity definition for my table`
