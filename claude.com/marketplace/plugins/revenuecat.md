<!-- source: https://claude.com/marketplace/plugins/revenuecat -->

Manage your RevenueCat in-app purchase backend directly from Claude Code. This plugin connects to the RevenueCat MCP server via OAuth, giving you full control over projects, apps, products, entitlements, offerings, and webhooks without leaving your development workflow. It supports iOS, Android, and Web platforms.

The plugin includes four slash commands: `/rc:status` gives a quick overview of your project configuration with counts and health indicators for apps, products, entitlements, and offerings; `/rc:create-app` walks you through setting up an iOS or Android app with store credentials and SDK code snippets; `/rc:create-product` guides you through creating subscriptions, consumables, or one-time purchases; and `/rc:apikey` retrieves your public SDK keys with ready-to-use Swift, Kotlin, or JavaScript code.

Three specialized agents handle more involved tasks. The Project Bootstrap agent automates full project setup from scratch — tell it your platforms and monetization model, and it creates apps, products, entitlements, and offerings in the correct dependency order. The Troubleshooting agent systematically diagnoses subscription and purchase issues, checking product configuration, entitlement wiring, webhook setup, and platform-specific gotchas like iOS 18.x StoreKit bugs. The Paywall Builder agent creates styled paywalls integrated with your app's design system.

**How to use:** Try prompts like `/rc:status` to see your project overview, `/rc:create-app ios com.myapp.bundle` to set up an iOS app, `/rc:create-product subscription monthly` to create a monthly subscription, or ask "help me set up RevenueCat from scratch" to launch the bootstrap agent. For debugging, say "my users can't restore purchases on Android" to engage the troubleshooting agent.

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
