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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d228c83775fcc75f4e6d_74409af25137110ac04cc39e4d5ea0a2fbcea421-1000x1000.svg)

Sep 2, 2026

### Building commerce agents with Claude

Product announcements

[Building commerce agents with Claude](#)Building commerce agents with Claude

[Building commerce agents with Claude](https://claude.com/blog/claude-for-commerce-agents)Building commerce agents with Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f783c784823d48ad84175_Object-CodeChatText.svg)

Aug 28, 2026

### How Anthropic employees use Claude Tag

Enterprise AI

[How Anthropic employees use Claude Tag](#)How Anthropic employees use Claude Tag

[How Anthropic employees use Claude Tag](https://claude.com/blog/how-anthropic-employees-use-claude-tag)How Anthropic employees use Claude Tag

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a90479f5433ec75978f1e8a_Object-Apple.svg)

Aug 28, 2026

### Claude for Teachers, now available for U.S. K-12 schools and districts

Product announcements

[Claude for Teachers, now available for U.S. K-12 schools and districts](#)Claude for Teachers, now available for U.S. K-12 schools and districts

[Claude for Teachers, now available for U.S. K-12 schools and districts](https://claude.com/blog/claude-for-teachers-now-available-for-schools-and-districts)Claude for Teachers, now available for U.S. K-12 schools and districts

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22b8840b2f6f9a40fe0_8925ac952fa2cb8eb5e845b2e44f3e71b33fd695-1000x1000.svg)

Aug 26, 2026

### Claude gets its own browser in Cowork

Product announcements

[Claude gets its own browser in Cowork](#)Claude gets its own browser in Cowork

[Claude gets its own browser in Cowork](https://claude.com/blog/cowork-built-in-browser)Claude gets its own browser in Cowork

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
