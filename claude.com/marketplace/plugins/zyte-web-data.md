<!-- source: https://claude.com/marketplace/plugins/zyte-web-data -->

Turn plain-English prompts into production-ready Scrapy spiders. This plugin provides an end-to-end web scraping workflow powered by the Zyte API — from schema definition and site exploration to code generation, testing, and deployment. It automatically discovers extractable fields from target websites, generates web-poet page objects with pytest test suites, and wires everything into standard Scrapy projects you can run independently.

The plugin handles the full scraping lifecycle: it analyzes target pages (supporting both static HTML and JavaScript-rendered content via Zyte API), builds typed extraction schemas through an interactive approval loop, generates maintainable page objects and navigation spiders, and validates everything with automated test crawls. Projects are scaffolded with all necessary dependencies including scrapy-poet, scrapy-zyte-api, and web-poet.

**How to use:** Run `/scrape` followed by a URL and a description of what you want to extract — for example, `/scrape https://books.toscrape.com extract book titles, prices, and ratings`. The plugin walks you through five stages: defining the extraction schema, analyzing the website structure, creating a Scrapy project, generating page object code, and assembling the spider. You can also deploy finished spiders to Scrapy Cloud for scheduled, monitored crawls with `/scrape-deploy`. Individual stages are available as standalone skills: `/scrape-define` to build a schema, `/scrape-spec` to explore and validate a site, and `/scrape-codegen` to generate extraction code.

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
