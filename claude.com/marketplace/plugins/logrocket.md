<!-- source: https://claude.com/marketplace/plugins/logrocket -->

Connect Claude Code to LogRocket to query session replays, metrics, issues, and user behavior using natural language. Investigate user-reported bugs by searching and watching session replays, analyze feature usage patterns, identify regressions after deployments, and surface high-impact issues — all without leaving your terminal.

The plugin provides six tools: `list_organizations` and `list_projects` for discovering your LogRocket resources, `use_logrocket` for broad natural language queries, `find_sessions` to filter sessions by user, URL, timeframe, or events, `watch_sessions` to examine specific session details and user behavior, and `build_metric` to query analytics data directly.

**How to use:** Ask Claude naturally about your LogRocket data. Try prompts like:

* "Find sessions where users hit errors on the checkout page in the last 24 hours"
* "What are the top issues affecting users this week?"
* "Watch the session for user jane@example.com and tell me what went wrong"
* "Build a metric showing page load times for /dashboard over the past month"
* "Show me sessions with rage clicks on the signup form"

For open-ended investigation, use natural language and the plugin will route to the right tool. For targeted debugging, be specific about URLs, user identifiers, time ranges, and custom events to get more precise results. You can also combine LogRocket data with your backend observability tools for comprehensive end-to-end debugging.

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
