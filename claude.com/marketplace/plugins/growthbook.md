<!-- source: https://claude.com/marketplace/plugins/growthbook -->

Manage the full GrowthBook feature flag and experimentation lifecycle without leaving your editor. This plugin provides a comprehensive suite of skills that connect directly to the GrowthBook REST API, covering flag creation, targeting, rollouts, experiment design, dependency auditing, and stale flag cleanup — all through natural-language commands.

The flag management skills handle the complete lifecycle: create flags with collision-safe key validation, toggle environments on or off, configure targeting rules and progressive rollouts with metric guardrails, manage draft revisions and approvals, and safely archive or delete stale flags with automated code-reference inlining. A dependency graph skill traces prerequisites, reverse dependencies, and linked experiments to assess blast radius before changes.

For experimentation, dedicated skills walk you through designing statistically rigorous A/B tests — from hypothesis framing and metric selection to sample-size estimation — then hand off a launchable spec. Discovery skills let you search, filter, and audit your flag inventory, surfacing cleanup candidates based on staleness criteria.

**How to use:** Start with `/growthbook:gb-setup` to configure your GrowthBook API credentials. Then try commands like `/growthbook:flag-create` to create a new feature flag, `/growthbook:flag-search` to find and audit existing flags, `/growthbook:experiment-design` to plan an A/B test, `/growthbook:flag-graph` to visualize flag dependencies, or `/growthbook:flag-cleanup` to safely remove stale flags.

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
