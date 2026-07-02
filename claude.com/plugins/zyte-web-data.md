<!-- source: https://claude.com/plugins/zyte-web-data -->

# Zyte Web Data

Web scraping skills for Claude Code powered by the Zyte API — scrape sites, generate and run Scrapy spiders, define e...

  [Zyte](https://www.zyte.com)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Turn plain-English prompts into production-ready Scrapy spiders. This plugin provides an end-to-end web scraping workflow powered by the Zyte API — from schema definition and site exploration to code generation, testing, and deployment. It automatically discovers extractable fields from target websites, generates web-poet page objects with pytest test suites, and wires everything into standard Scrapy projects you can run independently.

The plugin handles the full scraping lifecycle: it analyzes target pages (supporting both static HTML and JavaScript-rendered content via Zyte API), builds typed extraction schemas through an interactive approval loop, generates maintainable page objects and navigation spiders, and validates everything with automated test crawls. Projects are scaffolded with all necessary dependencies including scrapy-poet, scrapy-zyte-api, and web-poet.

**How to use:** Run `/scrape` followed by a URL and a description of what you want to extract — for example, `/scrape https://books.toscrape.com extract book titles, prices, and ratings`. The plugin walks you through five stages: defining the extraction schema, analyzing the website structure, creating a Scrapy project, generating page object code, and assembling the spider. You can also deploy finished spiders to Scrapy Cloud for scheduled, monitored crawls with `/scrape-deploy`. Individual stages are available as standalone skills: `/scrape-define` to build a schema, `/scrape-spec` to explore and validate a site, and `/scrape-codegen` to generate extraction code.
