<!-- source: https://claude.com/marketplace/plugins/firetiger -->

Firetiger brings autonomous observability workflows directly into Claude Code. Connect to Firetiger's MCP-powered platform to monitor your applications, investigate production issues, and query telemetry data — all without leaving your editor. The plugin provides six slash commands covering the full observability lifecycle from setup and instrumentation to active monitoring and incident investigation.

Get started quickly with `/firetiger:setup`, which auto-detects your stack (Vercel, AWS, GCP, Cloudflare), connects integrations, instruments your code with OpenTelemetry, and creates a monitoring agent — all in one guided flow. Use `/firetiger:instrument` to add OpenTelemetry instrumentation to Node.js, Python, Go, or Rust projects with framework-specific templates and automatic credential management.

Create autonomous monitoring agents with `/firetiger:create-agent` using plain English goals like "monitor API routes for errors and slow responses" or "watch for authentication failures." Track deployments by commenting `@firetiger` on PRs with `/firetiger:monitor-deploy` — the agent monitors health from 10 minutes to 72 hours post-deploy and reports issues directly on the PR.

**How to use:** Run `/firetiger:setup` to onboard your project. Query your traces, logs, and metrics with SQL using `/firetiger:query` (e.g., "show me the slowest API calls in the last hour"). Start a structured diagnosis session with `/firetiger:investigate` to systematically track down error spikes, latency regressions, or missing data. Use `/firetiger:create-agent` to spin up always-on monitoring for any part of your system.

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
