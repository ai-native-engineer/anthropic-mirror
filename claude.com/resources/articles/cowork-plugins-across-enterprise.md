<!-- source: https://claude.com/resources/articles/cowork-plugins-across-enterprise -->

Today, we're introducing updates to Cowork and plugins that help enterprises customize Claude to how you work. Plugins turn Claude into specialized agents for every role and department. Now, you can build private marketplaces to distribute them across your organization.

This release also makes plugins easier to build and customize, gives admins more control over marketplaces and connectors, and adds new plugins and connectors across a wider range of job functions. Claude can also now orchestrate across Excel and PowerPoint, working end-to-end and passing context between apps.

#### ‍

#### *Silvern Capital is a fictional company. Most teams in the demo are working in Cowork, with the legal team working in Thomson Reuters CoCounsel Legal — a purpose-built legal agent, reimagined from the ground up using the Claude Agent SDK.*

## Upgrading the plugin experience

Today we're launching a suite of updates that make it easier to create, use, and manage plugins across your organization.

Admins can now set up plugins from starter templates or build them from scratch, with Claude guiding you through setup by asking questions to tailor skills, commands, and connectors (MCPs) to your company. All of this lives in a new unified menu called 'Customize,' which consolidates plugins, skills, and connectors so admins can see and manage everything in one place.

![](https://assets.claude.com/b8a7594584b08cf688085642b32ac3d7508b00f2.png)

The connector experience has been overhauled too, with an improved directory, streamlined admin controls, and easier management of which connectors are bundled into plugins. Admins also get more control over what plugins their teams can access, including org-specific marketplaces, private GitHub repositories as plugin sources (in private beta), per-user provisioning, and auto-install.

On the user side, slash commands now launch with structured forms, so running a workflow like 'generate report' or 'dashboard' feels as intuitive as filling out a brief. And Cowork now features company branding throughout, including a redesigned home experience tailored to your organization.

![](https://assets.claude.com/e97245debbb07158f4ff862168f295ff3e6ec7f5.png)

Additionally, we're adding [OpenTelemetry](https://claude.com/docs/cowork/monitoring#monitoring) support, letting admins track usage, costs, and tool activity across their teams.

## New connectors and plugins

Cowork handles complex tasks best when connected to the tools you already use. Connectors bring Claude closer to where your work lives—helping you move faster across tools, not replace the expertise or software you rely on.

New connectors from popular enterprise software providers are now available, including Google Workspace ([Calendar](https://claude.com/connectors/google-calendar), [Drive](https://claude.com/connectors/google-drive), [Gmail](https://claude.com/connectors/gmail)), [Docusign](https://claude.com/connectors/docusign), [Apollo](https://claude.com/connectors/apollo), [Clay](https://claude.com/connectors/clay), [Outreach](https://claude.com/connectors/outreach), [Similarweb](https://claude.com/connectors/similarweb), [MSCI](https://claude.com/connectors/msci), [LegalZoom](https://claude.com/connectors/legalzoom), [FactSet](https://claude.com/connectors/factset), [WordPress](https://claude.com/connectors/wordpress-com), and [Harvey](https://claude.com/connectors/harvey). And companies like [Slack by Salesforce](https://claude.com/plugins/slack), [LSEG](https://claude.com/plugins/lseg), [S&P Global](https://claude.com/plugins/sp-global), [Apollo](https://claude.com/plugins/apollo), [Common Room](https://claude.com/plugins/common-room), and Tribe AI (see below) have also built plugins for joint customers to explore.

We're also expanding the library of pre-built plugin templates so more knowledge workers can find value in Cowork. Each was designed with practitioners in the relevant field, so workflows, terminology, and outputs reflect how that work actually gets done. New plugins include:

* [**HR**](https://claude.com/plugins/human-resources): Support people operations across the employee lifecycle, from drafting offer letters and building onboarding plans to writing performance reviews and running compensation analyses.
* [**Design**](https://claude.com/plugins/design): Accelerate design workflows by generating critique frameworks, drafting UX copy, running accessibility audits, and structuring user research plans.
* [**Engineering**](https://claude.com/plugins/engineering): Streamline day-to-day engineering workflows like writing standup summaries, coordinating incident response, building deploy checklists, and drafting postmortems.
* [**Operations**](https://claude.com/plugins/operations): Manage core business operations including process documentation, vendor evaluations, change request tracking, and runbook creation.
* **[Brand voice](https://claude.com/plugins/brand-voice) (by Tribe AI)**: Analyze your existing documents, marketing materials, and conversations to distill your brand's voice into clear, enforceable guidelines.
* [**Financial analysis**](https://claude.com/plugins/financial-analysis): Support the baseline workflows every finance analyst needs, from market and competitive research to financial modeling and PowerPoint template creation and quality checking.
* [**Investment banking**](https://claude.com/plugins/investment-banking): Accelerate deal workflows including reviewing transaction documents, building comparable company analyses, and preparing pitch materials.
* [**Equity research**](https://claude.com/plugins/equity-research): Streamline research workflows like parsing earnings transcripts, updating financial models with new guidance, and drafting research notes.
* [**Private equity**](https://claude.com/plugins/private-equity): Support deal sourcing and diligence by reviewing large document sets, extracting standardized financial data, modeling scenarios, and scoring opportunities against investment criteria.
* [**Wealth management**](https://claude.com/plugins/wealth-management): Help advisors analyze portfolios, identify drift and tax exposure, and generate rebalancing recommendations at scale.

Plugins are simple, portable file systems that you own. They work across Cowork and anything built on the Claude Agent SDK, making it easy to create private plugin marketplaces across teams and with industry experts.

> ““Three waves have reshaped professional work: productivity tools, cloud and search, and now agentic AI. PwC is partnering with Anthropic to bring enterprise-grade agents into the office of the CFO — making finance teams an even more strategic and valuable function by giving every team member the tools to do more ambitious work, make better decisions, and grow the business in ways that weren't possible before.” - Sanjay Subramanian, Anthropic Alliance Leader, PWC”

> ““For two years, the market has been hyping us up about AI agents like they would be digital employees that work around the clock on a specific, discrete workflow. What Anthropic built is so much better.” - Mark Hines, COO, Blank Metal”

## Working across apps

Claude can now also handle multi-step tasks end-to-end across Excel and PowerPoint. Claude can use and pass context from one Office add-in to the other, which makes it possible to assign Claude larger projects, like running an analysis in Excel and turning it into a presentation in PowerPoint. It's an early research preview that points toward Claude working across apps just like we do.

## Getting started

All user experience updates for plugins are available to all Cowork users. Team and Enterprise admins can access company branding, provisioning, and MCP controls.

Claude working across Excel and PowerPoint is now available in research preview for all paid plans on Mac and Windows. Download the add-in for [Claude in Excel](https://claude.com/claude-in-excel) and [Claude in PowerPoint](https://claude.com/claude-in-powerpoint) to get started.

To learn more about Cowork and plugins for financial services, see our [companion blog post](https://claude.com/resources/articles/cowork-plugins-finance).

[ArticleSep 29, 2026

### Agents you can coach: how Asana builds human-agent teams with Claude

Arnab Bose, Chief Product Officer at Asana, on how Asana runs AI agents as teammates with scoped roles, shared memory, and work that everyone can see.
‍

Claude Platform](https://claude.com/resources/articles/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude)[ArticleSep 28, 2026

### Giving companies more control over their AI agents, with NVIDIA

Claude Platform](https://claude.com/resources/articles/giving-companies-more-control-over-their-ai-agents-with-nvidia)[ArticleSep 8, 2026

### Reducing cost and improving performance with Claude Platform

Tuning prompt caching, instructions, and effort can reduce Claude's cost without sacrificing application performance.

Claude Platform](https://claude.com/resources/articles/reducing-cost-and-improving-performance-with-claude-platform)[ArticleSep 2, 2026

### A guide to the anatomy of effective commerce agents

The architecture, latency & cost techniques, and eval practices for agents that make it easier to buy and sell online.

Claude Platform](https://claude.com/resources/articles/the-anatomy-of-effective-commerce-agents)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
