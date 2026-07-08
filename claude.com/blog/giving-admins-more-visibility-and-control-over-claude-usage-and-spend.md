<!-- source: https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22349f86cd1968deab7_f06ca06f9d08ca4a85f26357eb896c3730274507-1000x1000.svg)

# Giving admins more visibility and control over Claude spend

New analytics and cost controls are available for Claude Enterprise.

  [Product announcements](https://claude.com/blog/category/announcements)

  Claude Enterprise

  July 2, 2026

  https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend

We’re introducing richer admin analytics, model-level entitlements, and spend alerts for Claude Enterprise. As Claude takes on increasingly difficult and complex agentic work across the organization, usage and cost patterns look different from a standard chat tool. These controls give admins the visibility to understand how Claude is being used and the tools to manage costs.

Today's additions build on controls Anthropic already provides: spend caps at every level, access and model routing, a usage analytics dashboard with exports and an Analytics API, and effort controls. Richer analytics and more granular cost controls are the newest additions to a control surface we've been building on for months.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a45ed484e5998965a180707_Cost-controls-admin-viz-thumbnail.png)

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

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## Getting started

For admins managing Claude across their organization: explore usage and cost breakdowns in the admin console, set model defaults and spend limits by group, and configure spend-threshold alerts to stay ahead of overages. Usage data is available in the admin dashboard, and the Analytics API lets finance and IT pull the same metrics into existing reporting systems, learn more [here](https://support.claude.com/en/articles/13694757-get-started-with-the-claude-enterprise-analytics-api).

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e6fa9211768bbce0b_6e00dbffcddc82df5e471c43453abfc74ca94e8d-1000x1000.svg)

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3f14a08cb97bf1b16d40ef_ObjectClouds.svg)

### Claude Cowork is coming to mobile and web

[Claude Cowork is coming to mobile and web](#)Claude Cowork is coming to mobile and web

[Claude Cowork is coming to mobile and web](/blog/cowork-web-mobile)Claude Cowork is coming to mobile and web

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a42c9bc20d2072552ef256a_Node-EnterpriseAgents.svg)

Jun 29, 2026

### Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud

[Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud](#)Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud

[Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud](/blog/introducing-the-claude-apps-gateway)Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3f14a08cb97bf1b16d40ef_ObjectClouds.svg)

Jun 29, 2026

### Claude in Microsoft Foundry is now generally available

[Claude in Microsoft Foundry is now generally available](#)Claude in Microsoft Foundry is now generally available

[Claude in Microsoft Foundry is now generally available](/blog/claude-in-microsoft-foundry)Claude in Microsoft Foundry is now generally available

    

    

    

    

    

    

    

    

    

    

Claude Enterprise
