<!-- source: https://claude.com/blog/claude-platform-compliance-api -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690937bee860a953417a8eee_Object-CodeBrowserGlobe.svg)

# Audit Claude Platform activity with the Compliance API

The Compliance API gives admins programmatic access to audit logs across their Claude Platform organization.

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

* Date

  March 30, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/claude-platform-compliance-api

## Audit Claude Platform activity with the Compliance API

The Compliance API is now available on the Claude Platform, giving admins programmatic access to audit logs across their organization. Security and compliance teams can track user activity, monitor configuration changes, and integrate Claude usage data into their existing compliance infrastructure.

## Audit logging for your organization

Organizations in regulated industries—like financial services, healthcare, legal—need detailed records of who accessed what, when, and what changed. Without programmatic access to this data, compliance teams need to rely on manual exports and periodic reviews, which don't scale.

The Compliance API provides an activity feed that logs security-relevant events across your organization. Admins can fetch activity logs filtered by time range, specific users, or API keys.

The API currently tracks two categories of activity:

* **Admin and system activities:** Actions that modify access or configuration of resources, like adding a member to a workspace, creating an API key, updating account settings, or modifying entity access.
* **Resource activities:** User-driven actions that create or modify resource data, such as creating a file, downloading a file, or deleting a skill. These cover actions that may affect data or allow resources to access sensitive information, excluding direct interactions with the model.

Together, these cover user login and logout events, account setting updates, workspace changes, and other organizational audit events. The API does not log inference activities, such as user interactions with the model or model activities.

## Getting started

Contact your account team to enable the Compliance API for your organization. Once enabled, create an admin API key and use it to query the activity feed endpoint. Note that logging begins once the API is enabled—historical activities prior to that point aren't available.

Organizations that already use the Compliance API for Claude Enterprise can add their Claude API organization to the same parent organization and filter activity across both from a single feed.

Read the documentation on the [Anthropic Trust Center](https://trust.anthropic.com/resources?s=tob70gqyan60x3dwb7nkap&name=anthropic-compliance-api) to learn more.

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229b7f170bab528846d_0df729ce74e4c9dd62c3342c9549ce6c7cef1202-1000x1000.svg)

Jul 28, 2026

### Bringing MCP 2026-07-28 to Claude

Product announcements

[Bringing MCP 2026-07-28 to Claude](#)Bringing MCP 2026-07-28 to Claude

[Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude)Bringing MCP 2026-07-28 to Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d231b45c2193efbb0f02_1869137c9d7f2a38b50e804d707e10e85de05ddb-1000x1000.svg)

Jul 23, 2026

### Think through hard problems in voice mode

Product announcements

[Think through hard problems in voice mode](#)Think through hard problems in voice mode

[Think through hard problems in voice mode](https://claude.com/blog/think-through-hard-problems-in-voice-mode)Think through hard problems in voice mode

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a025cf25f0694905405e054_Object-Scale.svg)

May 12, 2026

### Claude for the legal industry

Product announcements

[Claude for the legal industry](#)Claude for the legal industry

[Claude for the legal industry](https://claude.com/blog/claude-for-the-legal-industry)Claude for the legal industry

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3f14a08cb97bf1b16d40ef_ObjectClouds.svg)

Jul 7, 2026

### Claude Cowork is coming to mobile and web

Product announcements

[Claude Cowork is coming to mobile and web](#)Claude Cowork is coming to mobile and web

[Claude Cowork is coming to mobile and web](https://claude.com/blog/cowork-web-mobile)Claude Cowork is coming to mobile and web

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.
