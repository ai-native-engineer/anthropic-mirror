<!-- source: https://claude.com/marketplace/plugins/firecrawl -->

Turn any website into clean, LLM-ready markdown or structured data. Firecrawl integrates powerful web scraping, crawling, and search capabilities directly into Claude Code. Scrape single pages, crawl entire sites, map site structures, and search the web — all with automatic JavaScript rendering, anti-bot handling, and proxy rotation built in.

The plugin includes an AI agent for autonomous multi-source data gathering. Just describe the data you need in plain language and the agent finds, navigates, and extracts it across multiple websites — no URLs required. Results can be returned as markdown, HTML, screenshots, links, or structured data matching a custom schema.

**How to use:** After installing, run `/firecrawl:setup` to configure your API key. Then use these commands to get started:

`/firecrawl:scrape` — Extract a single webpage as clean markdown.
`/firecrawl:crawl` — Crawl and extract content from an entire website.
`/firecrawl:search` — Search the web and get scraped results.
`/firecrawl:map` — Discover all URLs on a site.
`/firecrawl:agent` — Describe what data you need and let the AI agent autonomously find and extract it.

You can also use Firecrawl's tools directly in conversation: ask Claude to scrape a URL, search the web for information, or gather competitive research across multiple sites. Supports self-hosted Firecrawl instances via custom API endpoint configuration.

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
