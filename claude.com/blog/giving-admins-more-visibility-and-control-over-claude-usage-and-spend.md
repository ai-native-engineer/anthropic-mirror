<!-- source: https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22349f86cd1968deab7_f06ca06f9d08ca4a85f26357eb896c3730274507-1000x1000.svg)

# Giving admins more visibility and control over Claude spend

New analytics and cost controls are available for Claude Enterprise.

* Category

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  [Claude Enterprise](https://claude.com/solutions/enterprise)
* Date

  July 2, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend

We’re introducing richer admin analytics, model-level entitlements, and spend alerts for [Claude Enterprise](https://claude.com/solutions/enterprise). As Claude takes on increasingly difficult and complex agentic work across the organization, usage and cost patterns look different from a standard chat tool. These controls give admins the visibility to understand how Claude is being used and the tools to manage costs.

Today's additions build on controls Anthropic already provides: spend caps at every level, access and model routing, a usage analytics dashboard with exports and an Analytics API, and effort controls. Richer analytics and more granular cost controls are the newest additions to a control surface we've been building on for months.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a45ed484e5998965a180707_Cost-controls-admin-viz-thumbnail.png)

## Track adoption and cost

The [analytics dashboard for admins](https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans) now shows usage and cost by group and by user, with output like artifacts created, files edited, skills and connectors used displayed directly next to their cost. Admins can filter by the SCIM groups their IT team already manages, so the breakdown follows their existing org chart.

Claude Code gets richer insights with two new tabs focused on value and usage inside the admin console. Usage shows active developers, session counts, and top commands across the org, and is updated daily. The value tab summarizes usage and cost data to help admins understand value of Claude Code at a glance, estimating productivity lift, cost per commit, and annual value. Every formula is visible in the tab, and the inputs are adjustable.

[Analytics chat](https://support.claude.com/en/articles/14729354-use-analytics-chat-to-ask-claude-about-usage) can now answer a much broader set of questions and produce richer artifacts that you can dive deeper into. Admins can ask questions in plain language — "Which teams doubled their Claude usage this month?" or "Where are we getting the most value per seat?" — and Claude returns charts that can be exported and shared with stakeholders.

Usage and cost data is available programmatically through the [Analytics API](https://platform.claude.com/docs/en/manage-claude/analytics-api), so finance and IT can bring Claude usage and cost data into the tools they already run — like Datadog Cloud Cost Management and CloudZero — and see it alongside the rest of their cloud and AI spend. Results can be filtered by date range, team, product, or model. Skills report their own usage and cost, and new endpoints track plugin adoption and artifact creation.

Admins can extend usage visibility to individual users — cost, product and model breakdowns, and progress against spend limits — so no one hits a surprise cutoff. Users can also see their own usage trends over time, including which products, models, and skills they rely on most, and how that activity adds up in spend.

## Controls for managing spend

[Model defaults and entitlements](https://support.claude.com/en/articles/15694740-manage-model-access-for-your-organization) let admins set which Claude model new conversations start with across chat, Cowork, and Claude Code so routine work doesn't necessarily default to the most expensive option. Admins control which models are available to specific roles or across the entire organization.

Spend-threshold alerts notify admins at 75% and 90% of an org-level spend limit, giving them time to raise the cap before anyone gets blocked mid-task. Users receive in-app notifications at 75% and 95% thresholds and can request a limit increase directly from their admin without leaving Claude.

For organizations managing limits across many groups, the [Admin API](https://platform.claude.com/docs/en/manage-claude/spend-limits-api#example-workflows) moves cost-control workflows into scripts so controls scale with the org. Automate increase-request reviews, identify members close to their spend limit, and flag rapidly changing usage all at scale.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68c4898064ee45d6186056ab_Frame.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68c4897e0ac296b8c65e5713_Frame-1.svg)

"Cost visibility isn't a once-a-month exercise. Granular spend data and alerts give teams regular nudges to reassess how they're using Claude, instead of a surprise at the end of the billing cycle. With the Analytics API, we can bring that data into the tools we already use every day."

Kyra Abbu, Product Manager

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a451ef104342d131f95adb1_Workato_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a451ef3b97d50cc14b9f880_Workato_dark.svg)

“I'm not going to slow down the people driving our best quarter, and my CFO isn't asking me to. He's asking for ROI. We've tied Claude, connected to our enterprise MCP servers, to a 4% revenue lift, and seeing cost next to business impact by team is how I make that case stick.”

Carter Busse, CIO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a4691bbbc84cd40c4662c8c_nubank-color.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a4691b8d4901403602b533c_nubank-white.svg)

"Token usage alone doesn't tell you much. What I actually want to see is which skills get run again and again across the org — that's the real signal of value."

Ciro Yamada, Product Director

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## Getting started

For admins managing Claude across their organization: explore usage and cost breakdowns in the admin console, set model defaults and spend limits by group, and configure spend-threshold alerts to stay ahead of overages. Usage data is available in the admin dashboard, and the Analytics API lets finance and IT pull the same metrics into existing reporting systems, learn more [here](https://support.claude.com/en/articles/13694757-get-started-with-the-claude-enterprise-analytics-api).

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

Aug 20, 2026

### Anthropic’s approach to teaching and learning AI

Product announcements

[Anthropic’s approach to teaching and learning AI](#)Anthropic’s approach to teaching and learning AI

[Anthropic’s approach to teaching and learning AI](https://claude.com/blog/anthropics-approach-to-teaching-and-learning-ai)Anthropic’s approach to teaching and learning AI

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
