<!-- source: https://claude.com/plugins/rill -->

# Rill

Skills for developing and querying projects in the Rill business intelligence platform

* Install in

  [Claude Code](#)

  [Rill Data](https://github.com/rilldata)
* Installs

  15

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Provides skills for developing and querying projects in the **Rill** business intelligence platform. Rill is a code-first BI tool where projects are built from YAML and SQL resources organized as a declarative DAG. This plugin gives your agent deep knowledge of Rill's resource types — models, metrics views, canvas dashboards, explore dashboards, connectors, and themes — so it can build and iterate on Rill projects from scratch or modify existing ones.

The plugin includes eight specialized skills covering the full Rill development workflow: project structure and development patterns (`rill-development`), data models with incremental and partitioned loading (`rill-model`), semantic-layer metrics views with dimensions, measures, and security policies (`rill-metrics-view`), interactive explore dashboards (`rill-explore`), free-form canvas dashboards with charts, KPIs, and custom Vega-Lite visualizations (`rill-canvas`), connector configuration (`rill-connector`), project-level settings (`rill-rillyaml`), and theming (`rill-theme`). It also connects to a local Rill Developer server via MCP for live project status, SQL queries, and data profiling.

**How to use:** Skills load automatically when you work on Rill project files. You can also invoke them directly — try prompts like *"Create a metrics view for my orders table with revenue and customer count measures"*, *"Build a canvas dashboard summarizing sales by region"*, *"Add an incremental model that ingests data from S3"*, or *"Profile the columns in my events model and suggest dimensions"*. The MCP integration requires a running Rill Developer server on localhost:9009.

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
