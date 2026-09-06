<!-- source: https://claude.com/blog/claude-platform-compliance-api -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690937bee860a953417a8eee_Object-CodeBrowserGlobe.svg)

# Audit Claude Platform activity with the Compliance API

The Compliance API gives admins programmatic access to audit logs across their Claude Platform organization.

* Category

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  [Claude Platform](https://claude.com/platform/api)
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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d228c83775fcc75f4e6d_74409af25137110ac04cc39e4d5ea0a2fbcea421-1000x1000.svg)

Sep 2, 2026

### Building commerce agents with Claude

Product announcements

[Building commerce agents with Claude](#)Building commerce agents with Claude

[Building commerce agents with Claude](https://claude.com/blog/claude-for-commerce-agents)Building commerce agents with Claude

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d0099a66d72e05699_33ddc751e21fb4b116b3f57dd553f0bc55ea09d1-1000x1000.svg)

Aug 26, 2026

### Claude in Chrome is generally available

Product announcements

[Claude in Chrome is generally available](#) Claude in Chrome is generally available

[Claude in Chrome is generally available](https://claude.com/blog/claude-in-chrome-generally-available) Claude in Chrome is generally available

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude Platform
