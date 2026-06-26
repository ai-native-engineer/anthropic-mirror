<!-- source: https://claude.com/plugins/data-engineering -->

# Data Engineering

Data engineering plugin - warehouse exploration, pipeline authoring, Airflow integration

* Install in

  [Claude Code](#)

  [Astronomer](https://www.astronomer.io)
* Installs

  13336

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

A comprehensive data engineering plugin that brings warehouse exploration, pipeline authoring, and Apache Airflow management directly into your coding workflow. It provides over 30 specialized skills spanning DAG development, data analysis, dbt integration, data lineage tracing, and Airflow deployment — plus an MCP server for full Airflow REST API access. An integrated `af` CLI tool lets you interact with Airflow instances from your terminal to list DAGs, trigger runs, diagnose failures, and manage connections.

Query your data warehouse to answer business questions using natural language, profile tables, check data freshness, and trace upstream or downstream lineage across your pipelines. The plugin caches discovered patterns and table-to-concept mappings so repeated analysis gets faster over time.

Author new Airflow DAGs through a guided Discover → Plan → Implement → Validate → Test → Iterate workflow, with built-in validation commands that catch errors before you deploy. Integrate dbt projects into Airflow using Astronomer Cosmos, with support for multiple execution modes and parsing strategies. Migrate pipelines from Airflow 2.x to 3.x with dedicated upgrade assistance.

**How to use:** Ask questions and give commands like: "Create a new DAG that ingests data from S3 into Snowflake every hour", "Why did my ETL pipeline fail last night?", "Trace the upstream lineage of the orders table", "How many active users signed up last month?", "Profile the customers table and check freshness", "Help me migrate this DAG from Airflow 2 to 3", or "Set up a dbt project with Cosmos in my Airflow environment".

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
