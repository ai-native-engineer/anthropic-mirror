<!-- source: https://claude.com/blog/cowork-plugins-across-enterprise -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d226da492fb9f7f815ba_1c3d1af62032009538b8bf5864139ca124b06741-1000x1000.svg)

# Cowork and plugins for teams across the enterprise

Admins can now create private plugin marketplaces, with better control over plugins, connectors, and skills. We've also added new plugins and connectors across more departments.

* Category

  [Agents](https://claude.com/blog/category/agents)

  [Enterprise AI](https://claude.com/blog/category/enterprise-ai)
* Product

  [Claude Enterprise](https://claude.com/solutions/enterprise)
* Date

  February 24, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/cowork-plugins-across-enterprise

Today, we're introducing updates to Cowork and pluginsthat help enterprises customize Claude to how you work. Plugins turn Claude into specialized agents for every role and department. Now, you can build private marketplaces to distribute them across your organization.

This release also makes plugins easier to build and customize, gives admins more control over marketplaces and connectors, and adds new plugins and connectors across a wider range of job functions. Claude can also now orchestrate across Excel and PowerPoint, working end-to-end and passing context between apps.

###### ‍

###### *Silvern Capital is a fictional company. Most teams in the demo are working in Cowork, with the legal team working in Thomson Reuters CoCounsel Legal — a purpose-built legal agent, reimagined from the ground up using the Claude Agent SDK.*

## Upgrading the plugin experience

Today we're launching a suite of updates that make it easier to create, use, and manage plugins across your organization.

Admins can now set up plugins from starter templates or build them from scratch, with Claude guiding you through setup by asking questions to tailor skills, commands, and connectors (MCPs) to your company. All of this lives in a new unified menu called 'Customize,' which consolidates plugins, skills, and connectors so admins can see and manage everything in one place.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/699cdb3778de7aaeb213b113_Customize%20(1).png)

The connector experience has been overhauled too, with an improved directory, streamlined admin controls, and easier management of which connectors are bundled into plugins. Admins also get more control over what plugins their teams can access, including org-specific marketplaces, private GitHub repositories as plugin sources (in private beta), per-user provisioning, and auto-install.

On the user side, slash commands now launch with structured forms, so running a workflow like 'generate report' or 'dashboard' feels as intuitive as filling out a brief. And Cowork now features company branding throughout, including a redesigned home experience tailored to your organization.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/699cdb4f81e69eef7fe2ee35_Elicitation%20(1).png)

Additionally, we're adding [OpenTelemetry](https://claude.com/docs/cowork/monitoring#monitoring) support, letting admins track usage, costs, and tool activity across their teams.

## New connectors and plugins

Cowork handles complex tasks best when connected to the tools you already use. Connectors bring Claude closer to where your work lives—helping you move faster across tools, not replace the expertise or software you rely on.

New connectors from popular enterprise software providers are now available, including Google Workspace ([Calendar](https://claude.com/connectors/google-calendar), [Drive](https://claude.com/connectors/google-drive), [Gmail](https://claude.com/connectors/gmail)), [Docusign](https://claude.com/connectors/docusign), [Apollo](https://claude.com/connectors/apollo), [Clay](https://claude.com/connectors/clay), [Outreach](https://claude.com/connectors/outreach), [Similarweb](https://claude.com/connectors/similarweb), [MSCI](https://claude.com/connectors/msci), [LegalZoom](https://claude.com/connectors/legalzoom), [FactSet](https://claude.com/connectors/factset), [WordPress](https://claude.com/connectors/wordpress-com), and [Harvey](https://claude.com/connectors/harvey). And companies like [Slack by Salesforce](https://claude.com/plugins/slack), [LSEG](https://claude.com/plugins/lseg), [S&P Global](https://claude.com/plugins/sp-global), [Apollo](https://claude.com/plugins/apollo), [Common Room](https://claude.com/plugins/common-room), and Tribe AI (see below) have also built plugins for joint customers to explore.

We're also expanding the library of pre-built plugin templates so more knowledge workers can find value in Cowork. Each was designed with practitioners in the relevant field, so workflows, terminology, and outputs reflect how that work actually gets done. New plugins include:

* [**HR**](https://claude.com/plugins/human-resources): Support people operations across the employee lifecycle, from drafting offer letters and building onboarding plans to writing performance reviews and running compensation analyses.
* [**Design**](https://claude.com/plugins/design): Accelerate design workflows by generating critique frameworks, drafting UX copy, running accessibility audits, and structuring user research plans.
* [**Engineering**](https://claude.com/plugins/engineering): Streamline day-to-day engineering workflows like writing standup summaries, coordinating incident response, building deploy checklists, and drafting postmortems.
* [**Operations**](https://claude.com/plugins/operations): Manage core business operations including process documentation, vendor evaluations, change request tracking, and runbook creation.
* [**Brand voice**](https://claude.com/plugins/brand-voice) **(by Tribe AI)**: Analyze your existing documents, marketing materials, and conversations to distill your brand's voice into clear, enforceable guidelines.
* [**Financial analysis**](https://claude.com/plugins/financial-analysis): Support the baseline workflows every finance analyst needs, from market and competitive research to financial modeling and PowerPoint template creation and quality checking.
* [**Investment banking**](https://claude.com/plugins/investment-banking): Accelerate deal workflows including reviewing transaction documents, building comparable company analyses, and preparing pitch materials.
* [**Equity research**](https://claude.com/plugins/equity-research): Streamline research workflows like parsing earnings transcripts, updating financial models with new guidance, and drafting research notes.
* [**Private equity**](https://claude.com/plugins/private-equity): Support deal sourcing and diligence by reviewing large document sets, extracting standardized financial data, modeling scenarios, and scoring opportunities against investment criteria.
* [**Wealth management**](https://claude.com/plugins/wealth-management): Help advisors analyze portfolios, identify drift and tax exposure, and generate rebalancing recommendations at scale.

Plugins are simple, portable file systems that you own. They work across Cowork and anything built on the Claude Agent SDK, making it easy to create private plugin marketplaces across teams and with industry experts.

> “Three waves have reshaped professional work: productivity tools, cloud and search, and now agentic AI. PwC is partnering with Anthropic to bring enterprise-grade agents into the office of the CFO — making finance teams an even more strategic and valuable function by giving every team member the tools to do more ambitious work, make better decisions, and grow the business in ways that weren't possible before.” - Sanjay Subramanian, Anthropic Alliance Leader, PWC

> “For two years, the market has been hyping us up about AI agents like they would be digital employees that work around the clock on a specific, discrete workflow. What Anthropic built is so much better.” - Mark Hines, COO, Blank Metal

## Working across apps

Claude can now also handle multi-step tasks end-to-end across Excel and PowerPoint. Claude can use and pass context from one Office add-in to the other, which makes it possible to assign Claude larger projects, like running an analysis in Excel and turning it into a presentation in PowerPoint. It's an early research preview that points toward Claude working across apps just like we do.

## Getting started

All user experience updates for plugins are available to all Cowork users. Team and Enterprise admins can access company branding, provisioning, and MCP controls.

Claude working across Excel and PowerPoint is now available in research preview for all paid plans on Mac and Windows. Download the add-in for [Claude in Excel](https://claude.com/claude-in-excel) and [Claude in PowerPoint](https://claude.com/claude-in-powerpoint) to get started.

To learn more about Cowork and plugins for financial services, see our [companion blog post](https://claude.com/blog/cowork-plugins-finance).

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f783c784823d48ad84175_Object-CodeChatText.svg)

Aug 28, 2026

### How Anthropic employees use Claude Tag

Enterprise AI

[How Anthropic employees use Claude Tag](#)How Anthropic employees use Claude Tag

[How Anthropic employees use Claude Tag](https://claude.com/blog/how-anthropic-employees-use-claude-tag)How Anthropic employees use Claude Tag

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225485fe31f1ed2d9a1_db28a79c9f4492b8471009d4c20e900f234ece48-1000x1000.svg)

Aug 26, 2026

### How Warp builds self-improving agents on Claude

Agents

[How Warp builds self-improving agents on Claude](#)How Warp builds self-improving agents on Claude

[How Warp builds self-improving agents on Claude](https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude)How Warp builds self-improving agents on Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d222061abf091318fb82_423062049d4676b41d52b16068cbb5e21603190e-1000x1000.svg)

Aug 21, 2026

### The AI-Native SDLC playbook

Enterprise AI

[The AI-Native SDLC playbook](#)The AI-Native SDLC playbook

[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook)The AI-Native SDLC playbook

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Aug 11, 2026

### Compliance API coverage extends to Claude Cowork and Claude Code

Enterprise AI

[Compliance API coverage extends to Claude Cowork and Claude Code](#)Compliance API coverage extends to Claude Cowork and Claude Code

[Compliance API coverage extends to Claude Cowork and Claude Code](https://claude.com/blog/compliance-api-cowork-and-claude-code)Compliance API coverage extends to Claude Cowork and Claude Code

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

Agents

Financial services

Legal

Business

Productivity
