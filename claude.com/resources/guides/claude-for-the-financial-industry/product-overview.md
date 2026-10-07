<!-- source: https://claude.com/resources/guides/claude-for-the-financial-industry/product-overview -->

Chapter 028 min read

# Product overview

8 min read

21 min remaining

### Pillar 01: Chat

#### Every knowledge worker

The on-ramp. Conversational access for drafting, research, analysis, and Q&A — in the browser and embedded in Microsoft 365.

* Policy and memo drafting
* Research synthesis
* Email and client comms

### Pillar 02: Cowork

#### Business operators and analysts

Multi-step work done for you. Claude operates across the tools your people already use — inbox, files, CRM, internal systems — with humans in the loop.

* Deal room prep
* KYC and onboarding
* Portfolio and ops reviews

### Pillar 03: Code

#### Engineers and quants

The on-ramp. Conversational access for drafting, research, analysis, and Q&A — in the browser and embedded in Microsoft 365.

* Legacy COBOL and Java migration
* Quant notebooks and models
* Test and review automation

Claude shows up to work in two forms: **products** your teams use directly such as Claude Chat, Claude Cowork, Claude Code, and the Microsoft 365 add-ins, as well as the **Claude Platform**, for firms building and running their own applications and agents.

### Claude Chat

The Claude web and desktop app, at [Claude.ai (opens in new tab)](https://claude.ai), is a chat interface for research and drafting. An analyst might use it, for example, to summarize an earnings transcript or pressure-test a thesis before a memo goes to the committee. It is often the first place a new user starts.

### Claude Cowork

[Claude Cowork (opens in new tab)](https://www.anthropic.com/product/claude-cowork) is a desktop application where Claude works across local files and connected apps to complete multi-step projects. It can read and write local documents, call connected services such as Google Drive, Gmail, Box, and Asana, and coordinate multi-step work across files and apps. Examples of the kind of project this is suited to include building a pitch book, reconciling a month-end close, or preparing a board packet.

### Claude Code

[Claude Code (opens in new tab)](https://claude.com/product/claude-code) is a command-line interface for technical teams: quantitative researchers, data engineers, and platform teams building internal tools. Finance firms use Claude Code to write and audit quantitative code, including trading logic and data pipelines under version control.

### Claude for Microsoft 365

Teams can use Claude within the Microsoft 365 suite in two ways. Add-ins from the Microsoft Marketplace put Claude inside Outlook, [Excel (opens in new tab)](https://claude.com/claude-for-excel), [PowerPoint (opens in new tab)](https://claude.com/claude-for-powerpoint), and [Word (opens in new tab)](https://claude.com/claude-for-word), so an analyst can [update a financial model (opens in new tab)](https://claude.com/resources/use-cases/update-your-financial-model-after-earnings) built in Excel, explain it with cell-level citations, and turn it into a slide [without leaving the app (opens in new tab)](https://www.youtube.com/watch?v=cIctgHKEeMA). The [Microsoft 365 connector (opens in new tab)](https://support.claude.com/en/articles/12542951-enable-and-use-the-microsoft-365-connector) lets Claude search and analyze content in Outlook, Teams, SharePoint, and OneDrive from chat, Cowork, or the add-ins. Context carries across the suite, so a model built in Excel can be turned into a slide or a client email without the analyst rebuilding anything.

<!-- yt-inline:cIctgHKEeMA -->
[![YouTube cIctgHKEeMA](https://img.youtube.com/vi/cIctgHKEeMA/hqdefault.jpg)](https://www.youtube.com/watch?v=cIctgHKEeMA)

<details>
<summary>자막: YouTube cIctgHKEeMA</summary>

_(자막 없음)_

</details>


### Claude Platform

[The Claude Platform (opens in new tab)](https://platform.claude.com/) is Anthropic's API for firms building their own applications on Claude. Quantitative teams, platform engineers, and internal tools teams use it to embed Claude directly into trading platforms, risk systems, KYC and underwriting applications, and other production workflows.

### Claude Managed Agents

[Claude Managed Agents (opens in new tab)](https://claude.com/resources/articles/claude-managed-agents) is Anthropic's suite of composable APIs for building and deploying cloud-hosted agents on the Claude Platform. A firm builds an agent on the platform and Anthropic runs it as a cloud service, with the production scaffolding Managed Agents provides (long running sessions, scoped permissions, managed credential vaults, and full execution tracing built in). Financial services firms use Managed Agents to run agents programmatically, for example, a Valuation Reviewer agent handling month-end reconciliation across a multi-hour close.

## Claude product matrix: when to use what

Claude products compared by use case, users, where they run, and example tasks

| Surface | Best for | Primary users | Where it runs | Example task |
| --- | --- | --- | --- | --- |
| Claude Chat | Conversational drafting, research, and analysis in a chat interface | Anyone | Browser, desktop, mobile | "Summarize this report and draft a response." |
| Claude Code | Agentic coding inside a repo — building, refactoring, testing | Developers | Terminal, IDE | "Refactor this module and run the tests." |
| Claude Cowork | Cross-app knowledge work that touches files and multiple tools | Knowledge workers (analysts, PMs, operators, researchers) | Claude desktop app | "Read the five vendor PDFs in my Downloads folder, compare them on price and SLAs, and put the result in a spreadsheet." |
| Claude for Microsoft 365 | In-place drafting, modeling, and editing across the Microsoft 365 suite; context carries across apps | Knowledge workers (analysts, PMs, operators, researchers) | Outlook, Excel, PowerPoint, Word (add-ins); Teams, SharePoint, OneDrive (via M365 connector) | "Update this DCF with the new guidance and turn it into a three-slide deck." |
| Claude Platform (API) | Building custom applications on Claude; embedding Claude into internal systems and production workflows | Developers, quantitative teams, platform and engineering teams | Anthropic API, Amazon Bedrock, Google Vertex AI, Microsoft Foundry | "Add Claude to our advisor platform to draft personalized portfolio commentary at scale, with a human in the loop." |
| Claude Managed Agents | Running custom agents as hosted cloud services with Anthropic handling the runtime | Platform and engineering teams | Claude Platform (hosted by Anthropic) | "Deploy our Valuation Reviewer agent as a managed service with scoped permissions and audit tracing." |

## Customizing Claude: connectors, skills, and plugins

Claude becomes specific to a financial services firm through three building blocks: **connectors** that give it access to the firm's data, **skills** that teach it how to complete specific tasks in a repeatable way, and **plugins** that bundle skills, subagents, and connectors into installable packages for a specific job.

### MCP Connectors

MCP Connectors give Claude access to a specific data source over the [Model Context Protocol (MCP) (opens in new tab)](https://modelcontextprotocol.io/docs/getting-started/intro), an open standard that lets Claude query the provider's system directly rather than working off an uploaded copy. This is important for firms with strict data-residency or entitlement requirements.

### Skills

Skills are reusable, encoded workflows—instructions, templates, and optionally scripts—that teach Claude how to complete specific tasks in a repeatable way. They are especially valuable in heavily regulated industries like financial services and insurance, where consistency matters.

Skills are best used for work that follows a standard format. For example, a credit memo skill captures the firm's template, required disclosures, and formatting, and a KYC skill captures the onboarding checks the compliance team runs on every new client.

Anthropic has pre-built skills for [PDF (opens in new tab)](https://github.com/anthropics/skills/tree/main/skills/pdf), [Word (opens in new tab)](https://github.com/anthropics/skills/tree/main/skills/docx), [Excel (opens in new tab)](https://github.com/anthropics/skills/tree/main/skills/xlsx), and [PowerPoint (opens in new tab)](https://github.com/anthropics/skills/tree/main/skills/pptx) creation. Firms can also build their own skills. Simple skills are written in Markdown with no code; more advanced ones can include executable scripts. Either way, skills are then uploaded in Claude.ai settings (via the customize tab in both web and desktop), Claude Code, or the API.

#### MCP connectors relevant to financial services firms

* **Credit and risk data:** Dun & Bradstreet, Moody's, Verisk
* **Market and company data:** Daloopa, FactSet, Fiscal.ai, LSEG, MSCI, Morningstar, PitchBook, S&P Capital IQ, FMP
* **Industry research and expert networks:** GLG, Guidepoint, IBISWorld, Third Bridge
* **News and real-time feeds:** Aiera, MT Newswires
* **Diligence and data rooms:** Chronograph, Egnyte, SS&C Intralinks
* **Productivity and collaboration:** Asana, Box, Google Workspace, Microsoft 365, SharePoint, Slack

## Pre-built finance agent reference architectures

Anthropic has shipped ten pre-built agent reference architectures for financial services work that packages up the skills, tools, and data connections a specific workflow needs into a template. Firms can then customize those templates to their modeling standards, data sources, and review steps.

Examples include:

#### Research and client coverage

* **Pitch builder** creates target lists, runs comparables, and drafts pitchbooks for client meetings;
* **Meeting preparer** assembles client and counterparty briefs ahead of calls;
* **Earnings reviewer** reads transcripts and filings, updates models, and flags thesis-relevant changes;
* **Model builder** builds and maintains financial models from filings, data feeds, and analyst inputs.
* **Market researcher:** tracks sector and issuer developments, synthesizes news, filings, and broker research, and flags items for credit and risk review.

#### Finance and operations

* **General ledger reconciler** reconciles general ledger accounts and runs net asset value calculations against the books of record;
* **KYC screener** assembles entity files, reviews source documents, and packages escalations for compliance review;
* **Month-end closer** runs the close checklist, prepares journal entries, and produces close reports;
* **Statement auditor** reviews financial statements for consistency, completeness, and audit-readiness;
* **Valuation reviewer** checks valuations against comparables, methodology, and the firm's review standards;

Each role can run as a plugin in Cowork and the Microsoft 365 add-ins for desktop use with a human in the loop, or via Claude Managed Agents in the Claude Platform. Either way, analysts stay in the loop, reviewing, iterating on, and approving the agent's outputs before anything moves downstream.
