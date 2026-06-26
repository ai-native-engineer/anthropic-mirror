<!-- source: https://claude.com/blog/cowork-for-enterprise -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

# Making Claude Cowork ready for enterprise

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude Enterprise
* Date

  April 9, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/cowork-for-enterprise

Claude Cowork is now generally available on all paid plans. Within companies, Claude Cowork has become a key part of how teams operate: handling tasks, drafting project deliverables, and keeping teams up to date.

Today, we’re introducing organization controls to help teams deploy Claude Cowork company-wide:  role-based access controls for Enterprise, group spend limits, expanded OpenTelemetry observability, and usage analytics for admins to see Claude Cowork adoption.

## Early signals

Claude Code helped developers transition from handing Claude questions to whole tasks, and we’re seeing the same pattern across the entire organization with Claude Cowork: the vast majority of Claude Cowork usage comes from outside engineering teams. Importantly, functions like operations, marketing, finance, and legal are not handing Claude their core work, but rather the work that surrounds their most critical tasks—project updates, collaboration decks, research sprints, etc.

As early enterprise adopters of Claude Cowork have seen this pattern emerge in one team, they’ve often wanted to roll it out more broadly, opening questions like who gets access, spend management, and how to see what’s happening across teams.

## Controls for organization-wide deployment

Deploying agents with Claude Cowork’s capabilities across an organization requires governance and visibility for admin teams. Today, we’re adding more of the controls organizations need:

**Role-based access controls.** Admins on Claude Enterprise can now organize users into groups — manually or via SCIM from your identity provider — and assign each a custom role defining which Claude capabilities its members can use. Turn Claude Cowork on for specific teams and adjust as adoption grows.

**Group spend limits.** Set per-team budgets from the admin console. Predictable costs, adjustable as you learn what each team needs.

**Usage analytics.** Claude Cowork activity now appears in the admin dashboard and the Analytics API. From the dashboard, admins can track Claude Cowork sessions and active users across various date ranges. The Analytics API goes deeper: per-user Claude Cowork activity, skill and connector invocations, and DAU/WAU/MAU alongside existing Chat and Claude Code figures. See which teams are adopting, which workflows are landing, and where to invest next.

**Expanded OpenTelemetry support.** Claude Cowork now emits events for tool and connector calls, files read or modified, skills used, and whether each AI-initiated action was approved manually or automatically. Events are compatible with standard SIEM pipelines like Splunk and Cribl, and a shared user account identifier lets you correlate OTEL events with Compliance API records. OpenTelemetry is available on Team and Enterprise plans.

**Zoom MCP connector.** Claude Cowork integrates with the tools your teams already use. Today, Zoom is launching a connector that brings meeting intelligence directly into the Cowork experience. The Zoom connector delivers AI Companion meeting summaries and action items alongside transcripts and smart recordings — helping teams use their conversations on Zoom to create agentic workflows in Cowork. Add Zoom from the connector directory in Claude's settings.

**Per tool connector controls.** Admins can now restrict which actions are available within each MCP connector across the organization — allowing read access but disabling write operations, for example. Permissions apply org-wide and are configured from the admin console.

## How organizations use Claude Cowork

[Zapier](https://claude.com/customers/zapier-cowork-qa) connected Cowork to their org database, Slack, and Jira to surface engineering bottlenecks—getting back a dashboard, team-by-team analyses, and a prioritized roadmap that Product and Design Ops then copied for themselves. [Jamf](https://claude.com/customers/jamf) turned a seven-facet performance review into a 45-minute guided self-evaluation, then built similar workflows for vendor reviews and incident response. [Airtree](https://claude.com/customers/airtree), a venture firm, built a board prep workflow that pulls from a portfolio company's Drive, Slack updates, and competitor news, cross-referenced against the previous prep.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aedd1d4ccaa7aaecee72_zapier_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aed89af0a9a659d820f0_zapier_dark.svg)

“The barrier between "having an idea" and "shipping something" has collapsed. The skill that matters now isn't knowing how to do every step. It's knowing clearly what you're trying to accomplish and being able to direct toward that outcome. Execution is still real work, but the ceiling on what one person can ship has moved dramatically. I genuinely cannot remember doing my job without it.”

Larisa Cavallaro, AI Automation Engineer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b45499ebd143bd2c52765a_logo_jamf-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b454a6ceaa3ebddb228495_logo_jamf-dark.svg)

“People across the org are using Cowork for data blending, analysis, and dashboard building. Bespoke dashboarding has been huge. Tasks that previously required a BI tool or an engineer's help, people are now doing themselves in minutes.”

Nick Benyo, Software Engineer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69c4c1998c3401934f20e29f_logo_airtree-light-mode.png)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69c4c19b37fe50b8853f38b3_logo_airtree-dark-mode.png)

“Using Claude Cowork across teams multiplied its value. Skills built by one person could be used by everyone. Claude Cowork became shared firm infrastructure rather than just an individual productivity tool.”

Jackie Vullinghs, Partner

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba1577e91d8296653388ca_Group%202055245285.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a186e574d077d020536326e_thomson_reuters_logo_white.svg)

“Claude Cowork helps teams do work at a scale that was hard to justify before. The human role becomes validation, refinement, and decision-making. Not repetitive rework.”

Joel Hron, CTO

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## Getting started

Claude Cowork and Claude Code on Desktop are generally available today on all paid plans on macOS and Windows. Download the Claude desktop app at[claude.com/download](http://claude.com/download).

For admins deploying Claude across your organization: [configure role-based access controls](https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans), group spend limits and [OpenTelemetry](https://claude.com/docs/cowork/monitoring) from the [admin console](https://claude.com/settings/admin). Claude Cowork usage data is available in the admin dashboard, and the Analytics API is documented [here](https://support.claude.com/en/articles/13694757-access-engagement-and-adoption-data-with-the-analytics-api).

For a deployment walkthrough, join our April 16th [webinar](https://www.anthropic.com/webinars/deploying-cowork-across-the-enterprise-with-paypal) with PayPal.

FAQ

No items found.

More about Cowork

[More about Cowork](https://claude.com/product/cowork)More about Cowork

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Jun 17, 2026

### Secure access to the Claude Platform with Workload Identity Federation

Product announcements

[Secure access to the Claude Platform with Workload Identity Federation](#)Secure access to the Claude Platform with Workload Identity Federation

[Secure access to the Claude Platform with Workload Identity Federation](/blog/workload-identity-federation)Secure access to the Claude Platform with Workload Identity Federation

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229a7aa26ac1b6e96c2_a62b6eb169818f14c35b7a192af269e283f8fa93-1000x1000.svg)

May 7, 2026

### Collaborate with Claude across Excel, PowerPoint, Word and Outlook

Product announcements

[Collaborate with Claude across Excel, PowerPoint, Word and Outlook](#) Collaborate with Claude across Excel, PowerPoint, Word and Outlook

[Collaborate with Claude across Excel, PowerPoint, Word and Outlook](/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook) Collaborate with Claude across Excel, PowerPoint, Word and Outlook

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d224ef32980bc807847d_a683fdcfe3e2c7c6532342a0fa4ff789c3fd4852-1000x1000.svg)

May 19, 2026

### New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

Product announcements

[New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](#)New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

[New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](/blog/new-in-claude-managed-agents)New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Apr 30, 2026

### Claude Security is now in public beta

Product announcements

[Claude Security is now in public beta](#)Claude Security is now in public beta

[Claude Security is now in public beta](/blog/claude-security-public-beta)Claude Security is now in public beta

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

Business

Productivity

Work
