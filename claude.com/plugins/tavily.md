<!-- source: https://claude.com/plugins/tavily -->

# Tavily

Build AI applications with real-time web data using Tavily's search, extract, crawl, and research APIs.

  [Tavily](https://www.tavily.com/)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Tavily brings real-time web intelligence into Claude Code through a suite of search, extraction, crawling, and research skills powered by the Tavily CLI. Search the web with LLM-optimized results, extract clean content from URLs (including JavaScript-rendered pages), crawl entire websites into local markdown files, discover all URLs on a site with the map skill, and run comprehensive AI-powered research that synthesizes multiple sources into cited reports.

Key features include domain and time-range filtering, multiple search depths (ultra-fast to advanced), topic-specialized queries (general, news, finance), semantic content filtering for crawls, and research reports with configurable citation formats (numbered, MLA, APA, Chicago). Results are structured as JSON for easy downstream processing.

**How to use:** Ask Claude to search the web and it will use Tavily automatically — try prompts like "search for the latest developments in quantum computing", "extract the content from this URL", "crawl the docs at docs.example.com and save them locally", "map all the URLs on example.com", or "research the competitive landscape for AI code editors and cite your sources". You can also use the skills directly: `/tavily-search`, `/tavily-extract`, `/tavily-crawl`, `/tavily-map`, and `/tavily-research`.

Requires a Tavily API key from tavily.com. After installing, authenticate with the Tavily CLI to get started.
