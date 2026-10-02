<!-- source: https://claude.com/blog/compliance-api-cowork-and-claude-code -->

Explore here

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

# Compliance API coverage extends to Claude Cowork and Claude Code

* Category

  [Enterprise AI](https://claude.com/blog/category/enterprise-ai)

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  [Claude Enterprise](https://claude.com/solutions/enterprise)

  Claude apps

  [Claude Code](https://claude.com/product/claude-code)

  [Claude Cowork](https://claude.com/product/cowork)
* Date

  August 11, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/compliance-api-cowork-and-claude-code

***Update: Compliance API: Cowork (desktop, web, and mobile) and Claude Code (CLI and desktop) coverage are now generally available; Microsoft 365 add-ins (Excel, Word, PowerPoint, and Outlook) and Claude Science coverage are in beta (August 26, 2026)***

Claude's Compliance API now covers Cowork across the desktop app, web, and mobile, as well as Claude Code in the CLI and desktop app. Coverage is in beta for Claude Enterprise customers. Compliance and security teams can pull session content and metadata from both products through the same Compliance API interface they already use for Claude chats.

The new endpoints are additive: nothing changes about the data you already pull from the Compliance API today.

Security and compliance teams rely on the Compliance API to see how Claude is used across their organization — for audits and eDiscovery — without deploying separate logging infrastructure for each surface. Extending coverage to Cowork and Claude Code closes a gap: those sessions now show up alongside Claude chats.

## How it works

The new session endpoints return a consolidated, server-hosted transcript for each Cowork and Claude Code session, so prompts, responses, and tool activity come back together in a single session record.

Each session record carries two kinds of data:

* **Session content:** prompts and responses, tool calls content (web and MCP), and skills and artifacts content captured as transcript text.
* **Session metadata:** verified user ID and email address, organization ID, session and per-message IDs, and timestamps.

This beta doesn't include Claude Code on the web, Claude Code accessed through the Claude Platform, or sessions run on Amazon Bedrock, Google Cloud's Vertex AI, or Microsoft Foundry.

Organizations already exporting OpenTelemetry data can keep it running: the Compliance API can work alongside it with no infrastructure required on your side.

## Getting started

Coverage for Cowork and Claude Code is available today and included with the Compliance API using your existing Compliance Access Key – there’s no separate integration to build. If it's already enabled for your organization, query the new session endpoints directly. If not, review the Compliance API [documentation](https://platform.claude.com/docs/en/manage-claude/compliance-api) to enable it.

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0112e18cdd7f0b92d19e40_Hand-BuildingBricks.svg)

Oct 1, 2026

### Customize Claude Code with mods

Product announcements

[Customize Claude Code with mods](#)Customize Claude Code with mods

[Customize Claude Code with mods](https://claude.com/blog/claude-code-mods)Customize Claude Code with mods

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f7912d5b05a5c7ed8ae86_Object-CodeChatCode.svg)

Jul 20, 2026

### Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5

Enterprise AI

[Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5](#)Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5

[Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5](https://claude.com/blog/working-at-the-frontier-rakuten)Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e6fa9211768bbce0b_6e00dbffcddc82df5e471c43453abfc74ca94e8d-1000x1000.svg)

Sep 30, 2026

### Claude for Government is now generally available

Product announcements

[Claude for Government is now generally available](#)Claude for Government is now generally available

[Claude for Government is now generally available](https://claude.com/blog/claude-for-government-is-now-generally-available)Claude for Government is now generally available

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2279047e82efc257633_6c7219042e95bfef1a126ad5ee8b2c7def8b8b0a-1000x1000.svg)

Sep 30, 2026

### How Anthropic's sales team rebuilt inbound with Claude Managed Agents

Enterprise AI

[How Anthropic's sales team rebuilt inbound with Claude Managed Agents](#)How Anthropic's sales team rebuilt inbound with Claude Managed Agents

[How Anthropic's sales team rebuilt inbound with Claude Managed Agents](https://claude.com/blog/how-anthropics-sales-team-rebuilt-inbound-with-claude-managed-agents)How Anthropic's sales team rebuilt inbound with Claude Managed Agents

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

Claude Code

Claude Cowork

Business
