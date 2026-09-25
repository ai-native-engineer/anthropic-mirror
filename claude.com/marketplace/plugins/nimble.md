<!-- source: https://claude.com/marketplace/plugins/nimble -->

Nimble gives Claude the ability to fetch, search, scrape, and crawl the live web. It provides two complementary skills: a **Web Expert** for immediate data retrieval and a reusable **Agent Builder** for creating structured extraction workflows that run at scale. The toolkit connects to Nimble's cloud infrastructure via MCP and the Nimble CLI, with pre-built agents covering 50+ popular websites for structured data extraction out of the box.

The Web Expert skill handles one-off fetches, real-time lookups, and live research. It can extract content from any URL, run web searches across eight focus modes (general, coding, news, academic, shopping, social, geo, and location), discover URLs with site mapping, and bulk-crawl entire website sections. Results are returned as structured data tables with automatic render-tier escalation for difficult pages.

The Agent Builder skill lets you create, refine, and publish reusable extraction agents for recurring data needs. It searches existing agents first, supports interactive testing with schema previews, and can generate batch scripts for large-scale runs (50+ items). Built agents automatically become available to the Web Expert, forming a feedback loop between ad-hoc extraction and repeatable pipelines.

**How to use:** Ask Claude to fetch or scrape a webpage (e.g., "scrape the product listings from this URL"), search the web ("search for recent funding rounds in AI startups"), discover URLs on a site ("map all blog post URLs on example.com"), or build a reusable extractor ("build an agent to extract job listings from LinkedIn"). You can also use the `/search` command for quick web lookups (e.g., `/search latest Python release notes`).

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
