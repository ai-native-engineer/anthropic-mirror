<!-- source: https://claude.com/marketplace/plugins/product-tracking-skills -->

A complete AI-powered workflow for product analytics instrumentation. This plugin adds seven slash-command skills and a background watchdog agent that take you from zero to fully instrumented — scanning your codebase, building a tracking plan, and generating production-ready SDK wrapper code for 25+ analytics platforms including Segment, Amplitude, Mixpanel, PostHog, and more.

The skills follow a structured lifecycle: start with `/product-tracking-business-case` to generate a stakeholder-ready justification, then `/product-tracking-model-product` to scan your codebase and map your product's entities and value flows. Run `/product-tracking-audit-current-tracking` to inventory what's already instrumented, `/product-tracking-design-tracking-plan` to produce an opinionated tracking plan with explicit deltas, and `/product-tracking-generate-implementation-guide` for SDK-specific patterns. Finally, `/product-tracking-implement-tracking` generates typed wrapper functions, identity management, and integration code ready for your codebase.

As your product evolves, use `/product-tracking-instrument-new-feature` to update your tracking plan when features ship or change. A background tracking watchdog agent monitors your commits and flags gaps in telemetry coverage automatically, keeping your analytics in sync with your product.

**How to use:** Try prompts like "model this product for tracking", "audit our current analytics", "design a tracking plan for our app", "generate Segment implementation code from our tracking plan", or "what tracking does this new feature need?" All artifacts are stored in a `.telemetry/` directory for version control alongside your code.

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
