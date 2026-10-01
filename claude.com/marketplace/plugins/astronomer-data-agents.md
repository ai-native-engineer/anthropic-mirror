<!-- source: https://claude.com/marketplace/plugins/astronomer-data-agents -->

A comprehensive data engineering toolkit for Apache Airflow and Astronomer. This plugin equips Claude with 22+ specialized skills spanning the full data pipeline lifecycle — from authoring DAGs with best practices, to debugging pipeline failures, tracing data lineage, profiling warehouse tables, and managing local and cloud deployments. It includes an Airflow MCP server providing full REST API integration for DAG management, triggering, task logs, and system health monitoring.

Key capabilities include a structured DAG authoring workflow with validation checkpoints, deep failure diagnosis with root cause analysis, upstream and downstream data lineage tracing (including column-level lineage), table profiling with data quality scoring, and a guided Airflow 2-to-3 migration path powered by automated Ruff linting rules. The plugin also integrates with dbt via Cosmos for analytics engineering workflows, and supports 25+ warehouse backends including Snowflake, BigQuery, and PostgreSQL.

The plugin provides an `af` CLI tool for terminal-based Airflow interaction, enabling commands like listing DAGs, triggering runs, inspecting task logs, and checking environment health — all without leaving your coding session.

**How to use:** Skills are invoked automatically based on your prompts, or you can trigger them directly. Try prompts like:

* "Write a DAG that loads CSV files from S3 into Snowflake on a daily schedule"
* "Debug why my etl\_pipeline DAG failed last night"
* "Trace where the orders\_fact table gets its data from"
* "Profile the customers table and check data quality"
* "Migrate my Airflow 2 DAGs to Airflow 3"
* "Set up a new Astro project and deploy it locally"

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
