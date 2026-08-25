<!-- source: https://claude.com/blog/bringing-mcp-2026-07-28-to-claude -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229b7f170bab528846d_0df729ce74e4c9dd62c3342c9549ce6c7cef1202-1000x1000.svg)

# Bringing MCP 2026-07-28 to Claude

* Category

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude apps

  [Claude Platform](https://claude.com/platform/api)
* Date

  July 28, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/bringing-mcp-2026-07-28-to-claude

The fifth spec release of the Model Context Protocol, [**MCP 2026-07-28**](https://modelcontextprotocol.io/specification/2026-07-28)**,** is live today. The latest spec moves MCP to a stateless core, while hardening authorization and graduating official extensions. Support is being rolled out across Claude products.

## **What's new in MCP**‍

MCP recently surpassed 400M monthly SDK downloads, a 4x increase this year, and has become the industry standard for connecting AI agents to applications. MCP 2026-07-28 is one of the most significant spec releases to date: **Stateless core.** MCP moves from a bidirectional stateful protocol to a request/response model. Servers can now deploy on serverless and edge infrastructure. This simplifies the experience of building MCP servers for Claude and scaling their usage as they grow in adoption.

**Standardized extensions.** [MCP Apps](https://modelcontextprotocol.io/extensions/apps/overview) and [Tasks](https://modelcontextprotocol.io/extensions/tasks/overview) now ship under a versioned extensions framework, giving developers a formal path to add capabilities like interactive UIs and long-running work without changing the core protocol.

**Auth hardening.** Authorization now aligns with production OAuth 2.0 and OIDC deployments, so MCP servers connect to enterprise identity systems like Entra or Okta without workarounds.

Companies across the ecosystem have been building on the new spec alongside the MCP community since beta:

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d1ee4cb7c69d15a44ec7d6_Figma%20Dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d1ee481c19e67f332ef755_Figma%20Light.svg)

“More builders are using our MCP server to bring generated outputs into Figma's canvas, where they can explore, riff and refine them with their team into products that stand out. As that usage grows, our stateless architecture can scale with it, and with MCP Apps, Tasks, and Enterprise-Managed Auth, we can do even more to keep design and code together in one, connected flow.”

Josh Clemm, VP of Engineering

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a689e68f0c0711f4b55978e_intuit-blue.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a689e68f0c0711f4b55978e_intuit-blue.svg)

"MCP is the industry standard for connecting AI agents to tools and data, and Intuit is proud to support the new MCP 2026-07-28 spec. The stateless protocol core and extensions framework, including MCP Apps and Tasks, let our technologists and customers build and connect agentic experiences at enterprise scale, and allow Intuit to continue delivering trusted financial intelligence experiences to its 100 million consumers and businesses, wherever they choose to work."

Chris Kasten, Chief Architect and SVP of Engineering, Platform and Development Xceleration Group

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bf6b97730efbbe48c60cf7_Netlify_Logo_0%201%20(1).svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bf70fe8bd1d6d413430b7f_Netlify_Logo_0%202%20(1).svg)

"The stateless core in the 2026-07-28 spec makes MCP a first-class HTTP workload with no session management to work around. Our customers wanted MCPs on Netlify to be as simple as the rest of the platform and this new spec unlocks this at its core. Building MCP Apps into the new extensions framework is a huge step forward for scalability, accessibility, and capability across the whole ecosystem."

Sean Roberts, VP of Applied AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a68a0572ec430ef25573811_posthog-logo.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a68a05e4db3770d9eccece8_posthog-logo-white.svg)

"Moving MCP to a stateless protocol makes it easier to scale our own service and makes it easier for us to add analytics for our customers' MCP servers. This helps us show people how their MCP tools are being used and what tools are missing that their users would want to use. It's great to see this protocol growing in this direction."

Paul D'Ambra, Product Engineer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a689fd3ac5b9fc22a54b573_Xero%20Wordmark__Blue.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a689fec4db3770d9ecc9a00_Xero%20Wordmark_White.png)

"Anthropic pairs frontier models with a developer experience that keeps raising the bar. The stateless core in the open MCP 2026-07-28 spec reduces the complexity we manage, so we can ship more features to our customers, faster and at scale."

Andrew Goodman, VP of AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68c1e924b89aa4ed22b0d827_cs-logo-zoom-light-theme.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68c1e9282f4c49a5abab41de_cs-logo-zoom-dark-theme.svg)

"At Zoom, we believe organizational context is what enables AI to deliver meaningful work, which is why we've built MCP servers that securely bring Zoom meeting intelligence into AI platforms like Claude. The new MCP spec makes it far easier to deploy and scale MCP servers on standard HTTP infrastructure — so users get Zoom's meeting intelligence faster and more reliably, right inside the AI workflows they depend on every day."

Ross Mayfield, Head of Product for AI Platform

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

See the [MCP 2026-07-28 release announcement](https://blog.modelcontextprotocol.io/posts/2026-07-28/) for full details on the new spec.

## ‍**Advancing MCP in Claude**‍

Claude now lists over 950 MCP servers in the [connectors directory](https://claude.ai/directory/connectors), used by millions of people every day. This year we shipped support for new protocol extensions alongside features that make MCP easier to build on and deploy:

[MCP Apps](https://claude.com/blog/interactive-tools-in-claude) let servers render interactive UI directly in the conversation. Users can see what a connector is doing and work with it inline, without switching tabs.

[Enterprise-managed auth](https://claude.com/blog/enterprise-managed-auth) lets admins provision MCP connectors for their whole organization through their identity provider. Admins authorize a connector once, users inherit access through their existing IdP groups, and it's connected on first login: zero-touch setup for the end user.

[Observability for developers building connectors](https://claude.com/blog/observability-for-developers-building-connectors) gives published connectors in our directory a dashboard showing how they perform across Claude product surfaces. Developers can use it to track adoption, diagnose errors and latency, and break down usage by product.

[MCP tunnels (research preview)](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview) connect Claude to MCP servers inside a private network without exposing them to the public internet. Teams can bring internal tools to Claude with no inbound firewall rules, no public endpoints, and no IP allowlisting on the origin.

The stateless core, standardized extensions, and hardened auth in 2026-07-28 will help developers bring more applications to Claude, with a lower-friction, more consistent end-user experience. We'll continue investing in MCP as an open standard alongside the community, and in the Claude features that make MCP more accessible and effective in production.

## ‍**Getting started**

**‍**Explore the [spec](https://modelcontextprotocol.io/specification/2026-07-28/) and [SDKs](https://modelcontextprotocol.io/docs/sdk) to get started. Support is rolling out across Claude products soon. If you’re planning to submit your MCP server to Claude’s [connectors directory](https://claude.ai/directory/connectors), you can learn more [here](https://claude.com/docs/connectors/building/submission).

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d23008bbc20c0ffaeb6f_43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg)

Jun 18, 2026

### Centrally manage authorization for MCP connectors

Enterprise AI

[Centrally manage authorization for MCP connectors](#) Centrally manage authorization for MCP connectors

[Centrally manage authorization for MCP connectors](https://claude.com/blog/enterprise-managed-auth) Centrally manage authorization for MCP connectors

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Aug 21, 2026

### Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders

Product announcements

[Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders](#)Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders

[Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders)Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

Aug 13, 2026

### Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions

Agents

[Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions](#)Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions

[Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions](https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions)Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229061abf091318fc81_6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg)

Aug 20, 2026

### Build production agents with computer use, the Skills API, and the Files API

Product announcements

[Build production agents with computer use, the Skills API, and the Files API](#)Build production agents with computer use, the Skills API, and the Files API

[Build production agents with computer use, the Skills API, and the Files API](https://claude.com/blog/computer-use-skills-api-files-api)Build production agents with computer use, the Skills API, and the Files API

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude apps

Claude Platform

Agents
