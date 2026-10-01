<!-- source: https://claude.com/marketplace/plugins/tavily -->

Tavily brings real-time web intelligence into Claude Code through a suite of search, extraction, crawling, and research skills powered by the Tavily CLI. Search the web with LLM-optimized results, extract clean content from URLs (including JavaScript-rendered pages), crawl entire websites into local markdown files, discover all URLs on a site with the map skill, and run comprehensive AI-powered research that synthesizes multiple sources into cited reports.

Key features include domain and time-range filtering, multiple search depths (ultra-fast to advanced), topic-specialized queries (general, news, finance), semantic content filtering for crawls, and research reports with configurable citation formats (numbered, MLA, APA, Chicago). Results are structured as JSON for easy downstream processing.

**How to use:** Ask Claude to search the web and it will use Tavily automatically — try prompts like "search for the latest developments in quantum computing", "extract the content from this URL", "crawl the docs at docs.example.com and save them locally", "map all the URLs on example.com", or "research the competitive landscape for AI code editors and cite your sources". You can also use the skills directly: `/tavily-search`, `/tavily-extract`, `/tavily-crawl`, `/tavily-map`, and `/tavily-research`.

Requires a Tavily API key from tavily.com. After installing, authenticate with the Tavily CLI to get started.

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
