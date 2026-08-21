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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229061abf091318fc81_6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg)

Aug 20, 2026

### Build production agents with computer use, the Skills API, and the Files API

Product announcements

[Build production agents with computer use, the Skills API, and the Files API](#)Build production agents with computer use, the Skills API, and the Files API

[Build production agents with computer use, the Skills API, and the Files API](https://claude.com/blog/computer-use-skills-api-files-api)Build production agents with computer use, the Skills API, and the Files API

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

Aug 20, 2026

### Anthropic’s approach to teaching and learning AI

Product announcements

[Anthropic’s approach to teaching and learning AI](#)Anthropic’s approach to teaching and learning AI

[Anthropic’s approach to teaching and learning AI](https://claude.com/blog/anthropics-approach-to-teaching-and-learning-ai)Anthropic’s approach to teaching and learning AI

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a7bb714a55b503cd7_cad034e66b44f7f017c0cb931c403a97d1763758-1000x1000.svg)

Aug 18, 2026

### Claude on call: How Claude Tag serves as Anthropic’s first responder for CI/CD failures

Enterprise AI

[Claude on call: How Claude Tag serves as Anthropic’s first responder for CI/CD failures](#)Claude on call: How Claude Tag serves as Anthropic’s first responder for CI/CD failures

[Claude on call: How Claude Tag serves as Anthropic’s first responder for CI/CD failures](https://claude.com/blog/ai-ci-cd-on-call)Claude on call: How Claude Tag serves as Anthropic’s first responder for CI/CD failures

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225588ad176f7c4aafd_abc884c723daea810d2e986455358281a2f94102-1000x1000.svg)

Aug 7, 2026

### How Anthropic's business development team uses Claude to run inbound and outbound at scale

Enterprise AI

[How Anthropic's business development team uses Claude to run inbound and outbound at scale](#)How Anthropic's business development team uses Claude to run inbound and outbound at scale

[How Anthropic's business development team uses Claude to run inbound and outbound at scale](https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale)How Anthropic's business development team uses Claude to run inbound and outbound at scale

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
