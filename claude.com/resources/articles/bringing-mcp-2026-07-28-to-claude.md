<!-- source: https://claude.com/resources/articles/bringing-mcp-2026-07-28-to-claude -->

The fifth spec release of the Model Context Protocol, **[MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28),** is live today. The latest spec moves MCP to a stateless core, while hardening authorization and graduating official extensions. Support is being rolled out across Claude products.

## **What's new in MCP**‍

MCP recently surpassed 400M monthly SDK downloads, a 4x increase this year, and has become the industry standard for connecting AI agents to applications. MCP 2026-07-28 is one of the most significant spec releases to date:

**Stateless core.** MCP moves from a bidirectional stateful protocol to a request/response model. Servers can now deploy on serverless and edge infrastructure. This simplifies the experience of building MCP servers for Claude and scaling their usage as they grow in adoption.

**Standardized extensions.** [MCP Apps](https://modelcontextprotocol.io/extensions/apps/overview) and [Tasks](https://modelcontextprotocol.io/extensions/tasks/overview) now ship under a versioned extensions framework, giving developers a formal path to add capabilities like interactive UIs and long-running work without changing the core protocol.

**Auth hardening.** Authorization now aligns with production OAuth 2.0 and OIDC deployments, so MCP servers connect to enterprise identity systems like Entra or Okta without workarounds.

Companies across the ecosystem have been building on the new spec alongside the MCP community since beta:

![Posthog](https://assets.claude.com/cf764d6e5c00baee08c58260767945f4b3cd823c.svg)

> “Moving MCP to a stateless protocol makes it easier to scale our own service and makes it easier for us to add analytics for our customers' MCP servers. This helps us show people how their MCP tools are being used and what tools are missing that their users would want to use. It's great to see this protocol growing in this direction.”

Paul D'Ambra, Product Engineer

![Xero](https://assets.claude.com/77549e68eceff2d4b0caa7d5624d47bf6447f3b6.svg)

> “Anthropic pairs frontier models with a developer experience that keeps raising the bar. The stateless core in the open MCP 2026-07-28 spec reduces the complexity we manage, so we can ship more features to our customers, faster and at scale.”

Andrew Goodman, VP of AI

![Zoom](https://assets.claude.com/6a7f21b4cf5f286e7bd8ffd3ae9ca839f6f0d681.svg)

> “At Zoom, we believe organizational context is what enables AI to deliver meaningful work, which is why we've built MCP servers that securely bring Zoom meeting intelligence into AI platforms like Claude. The new MCP spec makes it far easier to deploy and scale MCP servers on standard HTTP infrastructure — so users get Zoom's meeting intelligence faster and more reliably, right inside the AI workflows they depend on every day.”

Ross Mayfield, Head of Product for AI Platform

![Figma](https://assets.claude.com/30df15cbd261edbc52262a1fa2d1339f3a1a372b.svg)

> “More builders are using our MCP server to bring generated outputs into Figma's canvas, where they can explore, riff and refine them with their team into products that stand out. As that usage grows, our stateless architecture can scale with it, and with MCP Apps, Tasks, and Enterprise-Managed Auth, we can do even more to keep design and code together in one, connected flow.”

Josh Clemm, VP of Engineering

![Intuit](https://assets.claude.com/b730fa6588d08aef3d1c1e12fbe768211c465c24.svg)

> “MCP is the industry standard for connecting AI agents to tools and data, and Intuit is proud to support the new MCP 2026-07-28 spec. The stateless protocol core and extensions framework, including MCP Apps and Tasks, let our technologists and customers build and connect agentic experiences at enterprise scale, and allow Intuit to continue delivering trusted financial intelligence experiences to its 100 million consumers and businesses, wherever they choose to work.”

Chris Kasten, Chief Architect and SVP of Engineering, Platform and Development Xceleration Group

![Netlify](https://assets.claude.com/0058f4c2736de86844ed9ac368b924d4a86e2bfb.svg)

> “The stateless core in the 2026-07-28 spec makes MCP a first-class HTTP workload with no session management to work around. Our customers wanted MCPs on Netlify to be as simple as the rest of the platform and this new spec unlocks this at its core. Building MCP Apps into the new extensions framework is a huge step forward for scalability, accessibility, and capability across the whole ecosystem.”

Sean Roberts, VP of Applied AI

![Posthog](https://assets.claude.com/cf764d6e5c00baee08c58260767945f4b3cd823c.svg)

> “Moving MCP to a stateless protocol makes it easier to scale our own service and makes it easier for us to add analytics for our customers' MCP servers. This helps us show people how their MCP tools are being used and what tools are missing that their users would want to use. It's great to see this protocol growing in this direction.”

Paul D'Ambra, Product Engineer

![Xero](https://assets.claude.com/77549e68eceff2d4b0caa7d5624d47bf6447f3b6.svg)

> “Anthropic pairs frontier models with a developer experience that keeps raising the bar. The stateless core in the open MCP 2026-07-28 spec reduces the complexity we manage, so we can ship more features to our customers, faster and at scale.”

Andrew Goodman, VP of AI

![Zoom](https://assets.claude.com/6a7f21b4cf5f286e7bd8ffd3ae9ca839f6f0d681.svg)

> “At Zoom, we believe organizational context is what enables AI to deliver meaningful work, which is why we've built MCP servers that securely bring Zoom meeting intelligence into AI platforms like Claude. The new MCP spec makes it far easier to deploy and scale MCP servers on standard HTTP infrastructure — so users get Zoom's meeting intelligence faster and more reliably, right inside the AI workflows they depend on every day.”

Ross Mayfield, Head of Product for AI Platform

![Figma](https://assets.claude.com/30df15cbd261edbc52262a1fa2d1339f3a1a372b.svg)

> “More builders are using our MCP server to bring generated outputs into Figma's canvas, where they can explore, riff and refine them with their team into products that stand out. As that usage grows, our stateless architecture can scale with it, and with MCP Apps, Tasks, and Enterprise-Managed Auth, we can do even more to keep design and code together in one, connected flow.”

Josh Clemm, VP of Engineering

![Intuit](https://assets.claude.com/b730fa6588d08aef3d1c1e12fbe768211c465c24.svg)

> “MCP is the industry standard for connecting AI agents to tools and data, and Intuit is proud to support the new MCP 2026-07-28 spec. The stateless protocol core and extensions framework, including MCP Apps and Tasks, let our technologists and customers build and connect agentic experiences at enterprise scale, and allow Intuit to continue delivering trusted financial intelligence experiences to its 100 million consumers and businesses, wherever they choose to work.”

Chris Kasten, Chief Architect and SVP of Engineering, Platform and Development Xceleration Group

![Netlify](https://assets.claude.com/0058f4c2736de86844ed9ac368b924d4a86e2bfb.svg)

> “The stateless core in the 2026-07-28 spec makes MCP a first-class HTTP workload with no session management to work around. Our customers wanted MCPs on Netlify to be as simple as the rest of the platform and this new spec unlocks this at its core. Building MCP Apps into the new extensions framework is a huge step forward for scalability, accessibility, and capability across the whole ecosystem.”

Sean Roberts, VP of Applied AI

1/6

See the [MCP 2026-07-28 release announcement](https://blog.modelcontextprotocol.io/posts/2026-07-28/) for full details on the new spec.

## ‍**Advancing MCP in Claude**‍

Claude now lists over 950 MCP servers in the [connectors directory](https://claude.ai/directory/connectors), used by millions of people every day. This year we shipped support for new protocol extensions alongside features that make MCP easier to build on and deploy:

[MCP Apps](https://claude.com/resources/articles/interactive-tools-in-claude) let servers render interactive UI directly in the conversation. Users can see what a connector is doing and work with it inline, without switching tabs.

[Enterprise-managed auth](https://claude.com/resources/articles/enterprise-managed-auth) lets admins provision MCP connectors for their whole organization through their identity provider. Admins authorize a connector once, users inherit access through their existing IdP groups, and it's connected on first login: zero-touch setup for the end user.

[Observability for developers building connectors](https://claude.com/resources/articles/observability-for-developers-building-connectors) gives published connectors in our directory a dashboard showing how they perform across Claude product surfaces. Developers can use it to track adoption, diagnose errors and latency, and break down usage by product.

[MCP tunnels (research preview)](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview) connect Claude to MCP servers inside a private network without exposing them to the public internet. Teams can bring internal tools to Claude with no inbound firewall rules, no public endpoints, and no IP allowlisting on the origin.

The stateless core, standardized extensions, and hardened auth in 2026-07-28 will help developers bring more applications to Claude, with a lower-friction, more consistent end-user experience. We'll continue investing in MCP as an open standard alongside the community, and in the Claude features that make MCP more accessible and effective in production.

## ‍**Getting started**

**‍**Explore the [spec](https://modelcontextprotocol.io/specification/2026-07-28/) and [SDKs](https://modelcontextprotocol.io/docs/sdk) to get started. Support is rolling out across Claude products soon. If you’re planning to submit your MCP server to Claude’s [connectors directory](https://claude.ai/directory/connectors), you can learn more [here](https://claude.com/docs/connectors/building/submission).

[ArticleOct 1, 2026

### Customize Claude Code with mods

Change how Claude Code behaves and looks with a few lines of TypeScript.

Claude Code](https://claude.com/resources/articles/claude-code-mods)[ArticleSep 30, 2026

### Claude for Government is now generally available

Claude Code CLI and Claude for Microsoft 365 also now available in early access.](https://claude.com/resources/articles/claude-for-government-is-now-generally-available)[ArticleSep 25, 2026

### Build plugins for Claude

You can now submit plugins to the Claude directory through a new developer portal, track them through review, and see usage analytics once they’re live.

Claude apps](https://claude.com/resources/articles/build-plugins-for-claude)[ArticleSep 24, 2026

### Claude Tag now supports personal connectors in channels

Claude Tag can now use your connectors for requests you make in a channel. Nobody else can use them, and you're in control of how to present the output.

Claude Tag](https://claude.com/resources/articles/claude-tag-now-supports-personal-connectors-in-channels)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
