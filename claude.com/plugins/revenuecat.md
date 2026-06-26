<!-- source: https://claude.com/plugins/revenuecat -->

# RevenueCat

Configure RevenueCat projects, apps, products, entitlements, and offerings directly from Claude Code.

* Install in

  [Claude Code](#)

  [RevenueCat](https://github.com/RevenueCat)
* Installs

  2691

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Manage your RevenueCat in-app purchase backend directly from Claude Code. This plugin connects to the RevenueCat MCP server via OAuth, giving you full control over projects, apps, products, entitlements, offerings, and webhooks without leaving your development workflow. It supports iOS, Android, and Web platforms.

The plugin includes four slash commands: `/rc:status` gives a quick overview of your project configuration with counts and health indicators for apps, products, entitlements, and offerings; `/rc:create-app` walks you through setting up an iOS or Android app with store credentials and SDK code snippets; `/rc:create-product` guides you through creating subscriptions, consumables, or one-time purchases; and `/rc:apikey` retrieves your public SDK keys with ready-to-use Swift, Kotlin, or JavaScript code.

Three specialized agents handle more involved tasks. The Project Bootstrap agent automates full project setup from scratch — tell it your platforms and monetization model, and it creates apps, products, entitlements, and offerings in the correct dependency order. The Troubleshooting agent systematically diagnoses subscription and purchase issues, checking product configuration, entitlement wiring, webhook setup, and platform-specific gotchas like iOS 18.x StoreKit bugs. The Paywall Builder agent creates styled paywalls integrated with your app's design system.

**How to use:** Try prompts like `/rc:status` to see your project overview, `/rc:create-app ios com.myapp.bundle` to set up an iOS app, `/rc:create-product subscription monthly` to create a monthly subscription, or ask "help me set up RevenueCat from scratch" to launch the bootstrap agent. For debugging, say "my users can't restore purchases on Android" to engage the troubleshooting agent.

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
