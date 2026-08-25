<!-- source: https://claude.com/blog/claude-enterprise-inference-hooks -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22753311132c8c37b39_d3dd09ad16c68461dc3fb01df5e84cf7ccafda6c-1000x1000.svg)

# Inference hooks: inline data loss prevention for Claude Enterprise

* Category

  [Enterprise AI](https://claude.com/blog/category/enterprise-ai)

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  [Claude Enterprise](https://claude.com/solutions/enterprise)

  Claude apps

  [Claude Cowork](https://claude.com/product/cowork)

  [Claude Code](https://claude.com/product/claude-code)
* Date

  August 5, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/claude-enterprise-inference-hooks

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a737642f52b1b4fc4aaec1a_260805-PromptHooks-Blog-960x540-ZT-v008.gif)

Inference hooks lets your compliance team inspect and enforce policy on every prompt and tool call response before they reach Claude — across Claude Enterprise surfaces including chat, Claude Code, Claude Cowork, and more. Your DLP server makes the call to block or allow, and Claude enforces that decision in real time, blocking unapproved content before it reaches Claude.

Security teams require every channel where employees can move sensitive data to pass through an inspection point their team controls. Until today, native inline enforcement was limited to Claude Code's client-side hooks. Inference hooks closes the gap with a single enforcement layer that covers every Claude Enterprise surface without separate integration work or agent per product.

## How inference hooks works

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7362314ccf1158f2bffe5f_Claude-blog-prompt-hooks-DLP%20(1).png)

When an organization turns on inference hooks, every inference request routes through a signed WebSocket connection to a security server. Before the model starts generating, Claude sends the prompt and its surrounding context to your server. Your server returns a verdict — allow or deny — and Claude only proceeds once it has one. The same check runs on tool calls: when Claude calls a tool — including tools connected through MCP, skills, and plugins — the tool's response is checked before it's sent back to the model.

Teams are already putting that real-time check to work. "Inference hooks add a checkpoint to inspect what's flowing to Claude in real time, before the model ever sees it," said Andrew Grimmett, Vice President of Information Security at Bandwidth. "This lets us safely move faster on AI without giving up control."

## Ways to use inference hooks

Extend your existing DLP program to Claude. Inference hooks uses an open, webhook-based protocol with a published schema. That makes deployment easy — just point it at the same server your other tools already report to including Netskope, Palo Alto Networks, Proofpoint, Zscaler or an AI security server you built in-house.

Cover chat, Claude Code, Cowork, and additional Claude Enterprise products with one configuration. Turn on inference hooks once at the organization level and it applies to Claude Enterprise surfaces, including tool calls made through MCP connectors, skills, and plugins.

Simplify rollout with shadow mode (always allow), role-based exclusions, and percentage-based rollouts. Customize failure-policy tolerance, timeouts, and other settings to match your organization's risk tolerance.

## Getting started

Inference hooks is available today in beta for Claude Enterprise customers. Read the [documentation](https://platform.claude.com/docs/en/manage-claude/inference-hooks) to configure your organization's DLP server and start enforcing policy across Claude Enterprise surfaces.

For security vendors, inference hooks is built on a webhook-based protocol with a documented schema, so you can build an integration, and Claude Enterprise customers can point their organization at your platform.

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d222061abf091318fb82_423062049d4676b41d52b16068cbb5e21603190e-1000x1000.svg)

Aug 21, 2026

### The AI-Native SDLC playbook

Enterprise AI

[The AI-Native SDLC playbook](#)The AI-Native SDLC playbook

[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook)The AI-Native SDLC playbook

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

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude Enterprise

Claude apps

Claude Cowork

Claude Code
