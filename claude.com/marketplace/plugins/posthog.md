<!-- source: https://claude.com/marketplace/plugins/posthog -->

Connect Claude Code directly to your PostHog analytics platform. This plugin gives you access to 27+ PostHog tools for querying insights, managing feature flags, running A/B experiments, tracking errors, and analyzing LLM costs—all through natural language. Ask questions like "What are my top errors this week?" or "Create a feature flag for 50% of users" and Claude handles the API calls for you.

The plugin includes 12 slash commands for streamlined workflows: `/posthog:flags` for feature flag management, `/posthog:insights` for analytics queries, `/posthog:experiments` for A/B testing, `/posthog:errors` for debugging, `/posthog:dashboards` for dashboard administration, `/posthog:surveys` for user surveys, `/posthog:llm-analytics` for AI usage tracking, and more.

**How to use:** Install with `claude plugin install posthog`, then authenticate via OAuth using the `/mcp` command. Try prompts like "Show me my feature flags", "Create an experiment to test the new checkout flow", "What errors happened in the last 24 hours?", or "Query page views by country". EU Cloud users can append `?region=eu` to the MCP URL, and self-hosted instances are supported via the `POSTHOG_BASE_URL` environment variable.

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
