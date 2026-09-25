<!-- source: https://claude.com/marketplace/plugins/stagehand -->

Stagehand brings browser automation to Claude Code, letting you control a web browser through natural language. Powered by Browserbase, it supports both local Chrome and remote sessions with anti-bot stealth, automatic CAPTCHA solving, and residential proxies across 201 countries. Navigate pages, fill forms, click buttons, extract data, and take screenshots — all from your conversation with Claude.

The plugin uses a CLI-based `browse` command under the hood with a structured snapshot workflow: open a URL, capture the accessibility tree to get element references, interact with those elements, and verify results. It automatically handles pagination, tab management, and session cleanup. Remote mode via Browserbase is available for sites with bot detection, rate limiting, or geo-restrictions.

**How to use:** Ask Claude to perform web tasks in plain language. Example prompts:

* "Go to https://news.ycombinator.com and summarize the top 5 stories"
* "Open my app at localhost:3000 and test the login flow"
* "Extract all product prices from this e-commerce page"
* "Fill out the contact form on example.com with my details"
* "Take a screenshot of the homepage and check if the hero banner is visible"

For sites with bot protection, Claude can automatically switch to Browserbase remote mode for stealth browsing. Set `BROWSERBASE_API_KEY` and `BROWSERBASE_PROJECT_ID` environment variables to enable remote sessions.

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
