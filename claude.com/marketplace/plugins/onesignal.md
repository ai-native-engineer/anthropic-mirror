<!-- source: https://claude.com/marketplace/plugins/onesignal -->

The OneSignal plugin onboards your own app onto OneSignal from Claude Code. Point Claude at your project and it detects your platform, installs and initializes the OneSignal SDK, sets up your push credentials, and then proves the integration works by sending a real test notification to your device. It supports web, iOS, Android, React Native, Expo, Flutter, Cordova, Ionic, Capacitor and Unity projects.

Three skills run in order. Setup installs the SDK and adds a debug-only verification helper. Credentials walks you through the console steps for Apple APNs keys, Firebase Cloud Messaging, web push, email DNS records and SMS senders, then uploads the keys it can for you. Verify confirms on OneSignal’s side that a message was actually delivered. Every file change is shown as a diff for your approval first, secrets stay in environment variables, and the bundled OneSignal MCP server lets Claude look up users, check delivery stats and send test messages directly.

**How to use:**
Install the plugin, then describe what you want and Claude picks the right skill. Try “Set up OneSignal in this app”, “Add push notifications to my Expo app”, “Upload my APNs .p8 key to OneSignal”, “Why isn’t my Android push delivering?”, or “Send me a test notification and confirm it arrived”. You’ll need a free OneSignal account, your App ID, a REST API key set as an environment variable, and Python 3.7 or newer. The first time Claude uses the OneSignal MCP server, you sign in once through your browser.

## Other plugins

### [Frontend Design](https://claude.com/marketplace/plugins/frontend-design)

Frontend design skill for UI/UX implementation

### [Superpowers](https://claude.com/marketplace/plugins/superpowers)

Core skills library for Claude Code: TDD, debugging, collaboration patterns, and proven techniques

### [Code Review](https://claude.com/marketplace/plugins/code-review)

Automated code review for pull requests using multiple specialized agents with confidence-based scoring

### [Context7](https://claude.com/marketplace/plugins/context7)

Upstash Context7 MCP server for up-to-date documentation lookup. Connects to Context7's hosted remote MCP server (https://mcp.context7.com/mcp) — no local Node.js or npx required — to pull version-specific documentation and code examples directly from source repositories into your LLM context. Authenticate with Context7 when prompted.

### [Code Simplifier](https://claude.com/marketplace/plugins/code-simplifier)

Agent that simplifies and refines code for clarity, consistency, and maintainability while preserving functionality

### [Playwright](https://claude.com/marketplace/plugins/playwright)

Browser automation and end-to-end testing MCP server by Microsoft. Enables Claude to interact with web pages, take screenshots, fill forms, click elements, and perform automated browser testing workflows.
