<!-- source: https://claude.com/plugins/posthog -->

# PostHog

Connect Claude Code to PostHog. Query analytics, manage flags, run A/B tests, track errors, analyze LLM costs via natural language. 10+ commands, OAuth, EU/US/self-hosted.

* Install in

  [Claude Code](#)

  [PostHog](https://posthog.com)
* Installs

  11820

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Connect Claude Code directly to your PostHog analytics platform. This plugin gives you access to 27+ PostHog tools for querying insights, managing feature flags, running A/B experiments, tracking errors, and analyzing LLM costs—all through natural language. Ask questions like "What are my top errors this week?" or "Create a feature flag for 50% of users" and Claude handles the API calls for you.

The plugin includes 12 slash commands for streamlined workflows: `/posthog:flags` for feature flag management, `/posthog:insights` for analytics queries, `/posthog:experiments` for A/B testing, `/posthog:errors` for debugging, `/posthog:dashboards` for dashboard administration, `/posthog:surveys` for user surveys, `/posthog:llm-analytics` for AI usage tracking, and more.

**How to use:** Install with `claude plugin install posthog`, then authenticate via OAuth using the `/mcp` command. Try prompts like "Show me my feature flags", "Create an experiment to test the new checkout flow", "What errors happened in the last 24 hours?", or "Query page views by country". EU Cloud users can append `?region=eu` to the MCP URL, and self-hosted instances are supported via the `POSTHOG_BASE_URL` environment variable.

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
