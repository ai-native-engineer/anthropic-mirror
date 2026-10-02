<!-- source: https://claude.com/marketplace/plugins/onesignal -->

The OneSignal plugin onboards your own app onto OneSignal from Claude Code. Point Claude at your project and it detects your platform, installs and initializes the OneSignal SDK, sets up your push credentials, and then proves the integration works by sending a real test notification to your device. It supports web, iOS, Android, React Native, Expo, Flutter, Cordova, Ionic, Capacitor and Unity projects.

Three skills run in order. Setup installs the SDK and adds a debug-only verification helper. Credentials walks you through the console steps for Apple APNs keys, Firebase Cloud Messaging, web push, email DNS records and SMS senders, then uploads the keys it can for you. Verify confirms on OneSignal’s side that a message was actually delivered. Every file change is shown as a diff for your approval first, secrets stay in environment variables, and the bundled OneSignal MCP server lets Claude look up users, check delivery stats and send test messages directly.

**How to use:**
Install the plugin, then describe what you want and Claude picks the right skill. Try “Set up OneSignal in this app”, “Add push notifications to my Expo app”, “Upload my APNs .p8 key to OneSignal”, “Why isn’t my Android push delivering?”, or “Send me a test notification and confirm it arrived”. You’ll need a free OneSignal account, your App ID, a REST API key set as an environment variable, and Python 3.7 or newer. The first time Claude uses the OneSignal MCP server, you sign in once through your browser.

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
