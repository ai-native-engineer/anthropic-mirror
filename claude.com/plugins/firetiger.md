<!-- source: https://claude.com/plugins/firetiger -->

# Firetiger

Claude Code plugin for Firetiger observability workflows and MCP-powered investigations.

* Install in

  [Claude Code](#)

  [Firetiger](https://firetiger.com)
* Installs

  1024

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Firetiger brings autonomous observability workflows directly into Claude Code. Connect to Firetiger's MCP-powered platform to monitor your applications, investigate production issues, and query telemetry data — all without leaving your editor. The plugin provides six slash commands covering the full observability lifecycle from setup and instrumentation to active monitoring and incident investigation.

Get started quickly with `/firetiger:setup`, which auto-detects your stack (Vercel, AWS, GCP, Cloudflare), connects integrations, instruments your code with OpenTelemetry, and creates a monitoring agent — all in one guided flow. Use `/firetiger:instrument` to add OpenTelemetry instrumentation to Node.js, Python, Go, or Rust projects with framework-specific templates and automatic credential management.

Create autonomous monitoring agents with `/firetiger:create-agent` using plain English goals like "monitor API routes for errors and slow responses" or "watch for authentication failures." Track deployments by commenting `@firetiger` on PRs with `/firetiger:monitor-deploy` — the agent monitors health from 10 minutes to 72 hours post-deploy and reports issues directly on the PR.

**How to use:** Run `/firetiger:setup` to onboard your project. Query your traces, logs, and metrics with SQL using `/firetiger:query` (e.g., "show me the slowest API calls in the last hour"). Start a structured diagnosis session with `/firetiger:investigate` to systematically track down error spikes, latency regressions, or missing data. Use `/firetiger:create-agent` to spin up always-on monitoring for any part of your system.

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
