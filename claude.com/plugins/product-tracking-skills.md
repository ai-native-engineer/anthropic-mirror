<!-- source: https://claude.com/plugins/product-tracking-skills -->

# Product Tracking Skills

AI agents making SaaS products data-ready—scan codebase, build tracking plan, generate code

* Install in

  [Claude Code](#)

  [Accoil](https://accoil.com)
* Installs

  5423

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

A complete AI-powered workflow for product analytics instrumentation. This plugin adds seven slash-command skills and a background watchdog agent that take you from zero to fully instrumented — scanning your codebase, building a tracking plan, and generating production-ready SDK wrapper code for 25+ analytics platforms including Segment, Amplitude, Mixpanel, PostHog, and more.

The skills follow a structured lifecycle: start with `/product-tracking-business-case` to generate a stakeholder-ready justification, then `/product-tracking-model-product` to scan your codebase and map your product's entities and value flows. Run `/product-tracking-audit-current-tracking` to inventory what's already instrumented, `/product-tracking-design-tracking-plan` to produce an opinionated tracking plan with explicit deltas, and `/product-tracking-generate-implementation-guide` for SDK-specific patterns. Finally, `/product-tracking-implement-tracking` generates typed wrapper functions, identity management, and integration code ready for your codebase.

As your product evolves, use `/product-tracking-instrument-new-feature` to update your tracking plan when features ship or change. A background tracking watchdog agent monitors your commits and flags gaps in telemetry coverage automatically, keeping your analytics in sync with your product.

**How to use:** Try prompts like "model this product for tracking", "audit our current analytics", "design a tracking plan for our app", "generate Segment implementation code from our tracking plan", or "what tracking does this new feature need?" All artifacts are stored in a `.telemetry/` directory for version control alongside your code.

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
