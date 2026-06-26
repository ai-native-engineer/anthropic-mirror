<!-- source: https://claude.com/plugins/stripe -->

# Stripe

Stripe development plugin for Claude

* Install in

  [Claude Code](#)

  [Stripe](https://stripe.com)
* Installs

  43526

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

The Stripe plugin connects Claude to Stripe's MCP server, enabling AI-assisted payment integration development. It provides best practices guidance for implementing checkout flows, subscriptions, webhooks, and Connect platforms while helping you avoid deprecated APIs and follow Stripe's recommended patterns.

Key features include error explanation with code examples in your programming language, test card references organized by scenario, and guidance on modern Stripe APIs like CheckoutSessions, PaymentIntents, and Billing APIs. The plugin steers you toward Stripe-hosted checkout and Payment Element while warning against legacy patterns like the Charges API.

**How to use:**

Use `/explain-error` followed by a Stripe error code or message to get plain English explanations, common causes, and remediation code. Use `/test-cards` to quickly access test card numbers for different scenarios like declined payments, 3D Secure, or fraud testing. Ask Claude about Stripe best practices when implementing payment flows, and it will guide you using Stripe's recommended CheckoutSessions API and modern payment methods.

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
