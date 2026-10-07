<!-- source: https://claude.com/resources/guides/claude-for-the-legal-industry/product-overview -->

Chapter 0210 min read

# Product overview

10 min read

28 min remaining

Claude shows up to work for lawyers in a few forms: Claude chat, Claude Cowork, Claude for Microsoft 365, Claude Platform, and Claude Managed Agents.

### Claude Chat

The Claude web and desktop app, at [Claude.ai (opens in new tab)](https://claude.ai), is a chat interface for research and drafting. An associate might use it to summarize a deposition transcript or pressure-test an argument before pulling it into a brief. Use Chat when the work fits inside a single conversation: a question to the model, a research summary, an inline draft. Each conversation is its own session, so Chat is suited to one-off tasks rather than ongoing matters. It is often the first place a new user starts.

### Claude Cowork

[Claude Cowork (opens in new tab)](https://www.anthropic.com/product/claude-cowork) is a desktop application where Claude works across local files and connected apps to complete multi-step matters. It can read and write local documents, call connected services like iManage, NetDocuments, Box, and Microsoft 365, and coordinate work across files and apps. Use Cowork when the work spans multiple files, multiple apps, or multiple steps — reviewing every contract in a data room, comparing third-party paper against the firm's playbook, or drafting a PIA from a folder of prior assessments. Cowork can run for minutes or hours on a single task, with the lawyer reviewing the output once it is done.

Claude Chat or Claude Cowork?

The simplest distinction: Chat is for asking questions and working with Claude in the moment. Cowork is for delegating a project to Claude and reviewing the result. Most lawyers use both — Chat for quick questions through the day, and Cowork for the matter-level work that would otherwise eat an afternoon.

### Claude for Microsoft 365

Legal teams can use Claude inside Microsoft 365 in two ways. Add-ins from the Microsoft Marketplace put [Claude inside Word, Outlook, Excel, and PowerPoint (opens in new tab)](https://claude.com/claude-for-microsoft-365), so a lawyer can redline a contract with tracked changes and turn the analysis into a memo without leaving the app. The [Microsoft 365 connector (opens in new tab)](https://support.claude.com/en/articles/12542951-enable-and-use-the-microsoft-365-connector) lets Claude search and analyze content in Outlook, Teams, SharePoint, and OneDrive. Context carries across the suite, so a redline drafted in Word can be turned into a client update without rebuilding anything.

### Claude Platform

[The Claude Platform (opens in new tab)](https://platform.claude.com/) is Anthropic's API for organizations building their own applications on Claude. Legal engineering teams and legal tech companies use it to embed Claude into contract lifecycle, e-discovery, matter management systems, and other internal software.

### Claude Managed Agents

[Claude Managed Agents (opens in new tab)](https://claude.com/resources/articles/claude-managed-agents) allows teams to take any agent it builds on the Claude Platform and have Anthropic run it as a hosted service, with the long-running sessions, scoped permissions, and audit trail handled for them. For example, a Contract Review agent might handle NDA triage across thousands of incoming agreements.

## Claude product matrix: when to use what

Claude products compared by use case, users, where they run, and example tasks

| Surface | Best for | Primary users | Where it runs | Example task |
| --- | --- | --- | --- | --- |
| Claude.ai | Conversational drafting, research, and analysis in a chat interface | All legal staff | Browser, desktop, mobile | "Summarize this deposition transcript and flag inconsistencies." |
| Claude Cowork | Cross-app matter work that touches files and multiple tools | All legal staff | Claude desktop app | "Review the data room contracts in Box, flag material issues, and produce a diligence summary." |
| Claude for Microsoft 365 | In-place drafting, redlining, and comparison across the Microsoft 365 suite; context carries across apps | All legal staff | Word, Outlook, Excel, PowerPoint (add-ins); Teams, SharePoint, OneDrive (via M365 connector) | "Redline this MSA against our playbook and produce a deviation summary." |
| Claude Platform (API) | Building custom legal applications; embedding Claude into CLM, e-discovery, or matter management | Legal engineering, platform teams, legal tech vendors | Anthropic API, Amazon Bedrock, Google Vertex AI, Microsoft Foundry | "Integrate Claude into our CLM to triage incoming third-party paper" |
| Claude Managed Agents | Running custom legal agents as hosted cloud services with Anthropic handling the runtime | Platform and legal engineering teams | Claude Platform | "Deploy our NDA triage agent as a managed service with scoped permissions and audit tracing." |

## Customizing Claude: connectors, skills, and plugins

Claude becomes specific to a legal organization through three building blocks. **Connectors** give it access to the firm's matter data. [Skills (opens in new tab)](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) teach it how to complete specific legal tasks in a repeatable way. [Plugins (opens in new tab)](https://github.com/anthropics/knowledge-work-plugins/tree/main/legal) bundle skills, subagents, and connectors into installable packages for a specific practice area.

### MCP Connectors

MCP Connectors give Claude access to a specific data source over the [Model Context Protocol (MCP) (opens in new tab)](https://modelcontextprotocol.io/docs/getting-started/intro), an open standard that lets Claude query the provider's system directly rather than working off an uploaded copy. This matters in legal work, where confidentiality and privilege must be preserved end to end.

### Skills

[Skills (opens in new tab)](https://agentskills.io/home) are reusable, encoded workflows that teach Claude how to complete specific legal tasks in a repeatable way. They are valuable in legal work, where consistency, oversight and accuracy are not optional.

Skills are best used for work that follows a standard format. An NDA review skill captures the firm's playbook and fallback positions, while a citation skill enforces Bluebook or local format.

Anthropic has pre-built skills for [PDF (opens in new tab)](https://github.com/anthropics/skills/blob/main/skills/pdf/SKILL.md), [Word (opens in new tab)](https://github.com/anthropics/skills/blob/main/skills/docx/SKILL.md), [Excel (opens in new tab)](https://github.com/anthropics/skills/blob/main/skills/xlsx/SKILL.md), and [PowerPoint (opens in new tab)](https://github.com/anthropics/skills/tree/main/skills/pptx) creation. Firms can also [build their own skills (opens in new tab)](https://github.com/anthropics/skills/tree/main/skills/skill-creator). Simple skills are written in Markdown with no code; more advanced ones can include executable scripts. Either way, skills are uploaded in Claude.ai settings, Claude Code, or the API.

#### The connectors most relevant to legal organizations

* **Contract lifecycle & drafting:** Docusign, Ironclad, Definely
* **Document management:** iManage, NetDocuments
* **Legal research & case law:** Trellis, Midpage
* **Deal rooms and transaction documents:** Box, Datasite
* **E-discovery and review:** Everlaw, Relativity, Consilio
* **Legal AI assistants, skills, and expert network:** Harvey, Legora, LawVu, SolveAI
* **Productivity and collaboration:** Asana, Google Workspace, Microsoft 365, SharePoint, Slack
* **Public Service:** Free Law Project, Courtroom5, Descrybe, Boardwise

### Subagents

**Subagents** are narrowly-scoped helper agents that Claude can delegate to mid-task. Where a skill tells Claude how to do something, a [subagent (opens in new tab)](https://code.claude.com/docs/en/sub-agents) is an agent that runs in its own context window with its own system prompt and tool access, completes one bounded job (check a citation, extract a clause, audit defined terms) and reports back. They keep long matters from overloading a single context window and let firms put tighter tool restrictions on the parts of a workflow that touch sensitive systems.

Plugins can package subagents alongside skills and connectors so a practice area ships with the right helpers built in.

### Plugins

Plugins bundle skills, subagents, and connectors into a single installable package for a practice area.

[Anthropic-built plugins are open source (opens in new tab)](https://github.com/anthropics/legal-plugins), so firms can install them as shipped or fork them to swap in their own playbooks and add approval workflows. Partner plugins bring specialized data and provider-built skills into Claude.

Lawyers have different areas of expertise and focus. These plugins expand beyond [our initial legal plugin (opens in new tab)](https://github.com/anthropics/knowledge-work-plugins/tree/main/legal) launched in early 2026, aligned to more specific practice areas. Here is a list of plugins designed for legal professionals:

* **Commercial Legal.** Reviews vendor agreements, NDAs, and SaaS subscriptions against the playbook you taught it, with separate positions for sales-side and purchasing-side work. Tracks renewals, routes escalations, and translates findings for business stakeholders.
* **Corporate Legal.** M&A diligence at scale: extracts issues from a data room, builds disclosure schedules, drafts board consents, tracks the closing checklist, and runs tabular review across hundreds of agreements. Modular setup for deals, board work, public company governance, and entity compliance.
* **Employment Legal.** Jurisdiction-aware. Reviews hires and terminations, classifies workers, tracks leave deadlines, runs investigations, and drafts policies with state supplements.
* **Privacy Legal.** Reviews DPAs against your playbook, triages PIAs and DPIAs, drafts DSAR responses with the right statutory timeline, and watches for drift between what your policy promises and what your practice does.
* **Product Legal.** The connective tissue between a Product Review Doc and a launch. Reviews launches against your framework, checks marketing claims for substantiation, triages "can we do this?" questions, and learns what actually blocks a launch at your company.
* **Regulatory Legal.** Watches regulatory feeds, filters by your materiality threshold, diffs new rules against your policy library, tracks gaps and comment deadlines, and drafts proposed policy updates for review.
* **AI Governance Legal.** Triages AI use cases against your governance tiers, runs impact assessments, reviews vendor AI terms, and checks whether your AI policy has kept pace with your practice. Ships with a policy-starter skill that drafts a firm AI policy from published model policies.
* **IP Legal.** Trademark clearance, FTO triage, cease-and-desist drafting and response, DMCA takedowns, OSS compliance, IP clause review, invention intake screening, and portfolio tracking. Loud guardrails on anything that needs a specialist.
* **Litigation Legal.** Matter intake, portfolio tracking, legal holds, demand letters, subpoena triage, chronologies, depo prep, privilege logs, claim charts, and brief drafting. Adapts to in-house, firm associate, or solo practice.
* **Law Student.** Socratic drilling that won't give you the answer, because the point is learning. Case briefing, outlining, IRAC grading, bar prep with jurisdiction distinctions.
* **Legal Clinic.** Client intake, deadline tracking, case memos, and supervisor review queues. Supervisors set a pedagogy dial per practice area that controls how much the plugin does versus how much the student does. Built within ABA Formal Op. 512.
* **Legal Builder Hub.** Finds, reviews, installs, and updates community-built legal skills from registries like Lawvable, with a security review, license gate, and freshness check on every install. The trust layer for the open legal skills ecosystem.

Each role can run as a plugin in Cowork and the Microsoft 365 add-ins for desktop use with a human in the loop. Lawyers stay in the workflow, reviewing and approving the agent's outputs before anything moves downstream.
