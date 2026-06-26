<!-- source: https://claude.com/plugins/astronomer-data-agents -->

# Astronomer Data Agents

Apache Airflow/Astronomer: author DAGs, debug failures, trace lineage, profile tables, migrate 2→3, manage deployments

* Install in

  [Claude Code](#)

  [Astronomer](https://astronomer.io)
* Installs

  1939

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

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
