<!-- source: https://claude.com/resources/guides/claude-for-the-legal-industry/claude-for-legal-adoption-roadmap -->

Chapter 0412 min read

# Claude for legal adoption roadmap

12 min read

14 min remaining

Most successful Claude rollouts in legal organizations follow this sequence: the team lays the foundation for a pilot program, runs a pilot with a focused practice group, and scales out to the rest of the legal department or firm. [Anthropic's recommended Claude Cowork adoption playbook (opens in new tab)](https://claude.com/resources/tutorials/scaling-workflows-with-claude-cowork-at-your-organization) maps out these three phases.

## Phase 1: Lay the foundation

Before launching a Claude pilot program, the responsible team needs to put access and connectors in place. For most legal organizations, this means standing up Claude on the first-party API, Amazon Bedrock, Google Vertex AI, or Microsoft Foundry — whichever keeps Claude inside the firm's existing cloud perimeter. Enterprise controls for SSO, SCIM, audit logs, and custom data retention need to be configured at this stage. Scope governance in parallel: legal hold, privilege protection, and data-privacy review should run alongside access setup.

The connector set usually starts with the Microsoft 365 connector for Outlook, Teams, SharePoint, and OneDrive access, plus one or two systems the pilot team relies on most. Common starting points are iManage or NetDocuments for matter files, Thomson Reuters for research, and Ironclad or DocuSign for contracts. Firms can install these a la carte as MCP connectors, or access them inside one of Anthropic's legal plugins.

Next, use Claude to analyze your legal ticket requests to solve the cold start problem. Point Claude at your inbox, your ticket queues, and other work to figure out what Claude might be able to assist your department with.

Pick work that is document-heavy and standard-shape. For an in-house team, that might be NDA triage or PIA drafting. For a law firm, that could be diligence document review or first-draft research memos. Avoid piloting Claude on novel or high-stakes matters without strong human review.

**Pro-tip:** Have your champions leverage pre-configured plugins so they get value in the first session. If a lawyer opens Claude Cowork and does not know what to do or what the desired outcome is, they're unlikely to open it again. If they open it, type /nda-triage, and get a clean redline in ninety seconds, they're more likely to return.

## Phase 2: Pilot

At this stage, champions are running real workflows with real matter data and measuring the pilot's success against pre-defined criteria. Time saved is a common metric, specifically tracking the team's cycle time on the pilot job before and after Claude. Another is how often a lawyer keeps Claude's draft without a meaningful rewrite. Together, these two criteria help you assess whether the pilot is working.

Another strong signal that a pilot is working is when champions start to build their own skills. A privacy counsel takes the DPIA workflow she has been running by hand and turns it into a skill with the firm's template and approval flow embedded. That is now a skill the rest of the legal team can begin using immediately.

In most pilots, Claude's product surfaces come online in a specific order. Skills and plugins come first because they are low-risk and high-reuse. The Microsoft 365 add-ins come next, extending what a pilot team has built into Word, Excel, PowerPoint, and Outlook. Claude Cowork tends to come in at the back end of the pilot, when the team is ready to move from single-document work to matter-level work that spans files and apps.

**Pro-tip:** Schedule weekly check-ins with your pilot teams. They surface edge cases fast, like citation hallucination or jurisdiction-specific variations, and you want to hear about them while they are fresh.

## Phase 3: Scale

At this stage, plugins and skills that worked during the pilot are being rolled out to more teams across the legal department or firm through admin-managed [plugin marketplaces (opens in new tab)](https://code.claude.com/docs/en/plugin-marketplaces). New hires benefit as well, as they start on day one with already-encoded workflows. Onboarding is faster and the whole team can work more efficiently.

Over time, skills begin compounding across teams. A skill built for one practice area can be adapted for another when their work shares structure. A commercial contract review workflow and an employment contract review workflow share most of their structure. Adding a second practice group usually goes faster than the first, and the firm's skill library grows.

**Pro-tip:** Align as a team on an intentional governance framework to enable scaling with confidence and velocity. Have an understanding of how skills are quality-controlled, tested before being rolled out, and maintained after deployment to be kept up-to-date and functional.

The table below summarizes the actions you would take at each stage and what you can expect to see as you go through rollout.

Rollout phases with the actions to take and what to expect at each stage

| Phase | Actions | Phase |
| --- | --- | --- |
| Foundation | Security and privilege review. Identify 2–3 champion teams. Install pre-built plugins. Connect 1–2 core systems (iManage/NetDocuments, Thomson Reuters/Ironclad). | Champions reporting back use cases. First "this saved me an hour" moments. |
| Pilot | Champions run real workflows. Weekly check-ins. Measure against defined criteria. Demo wins to adjacent practice groups. | Measurable time savings. Champions building and sharing custom skills. Pull from other teams. |
| Scale | Admin-provisioned plugin marketplace. Encode pilot learnings as firm-wide skills. Onboard the next wave of users. | Skills shared across practice areas. New hires ramping on encoded workflows. Declining support tickets for "how do I do this." |

## Practice and segment use cases

The work legal teams tend to bring to Claude first is document-heavy and follows a standard shape, with human review before it ships. Still, Claude takes on the drafting so reviewers can focus on the work that requires judgment, like client counseling and final contract review. The sections below show what that looks like across in-house teams and different legal practices. They are illustrative rather than exhaustive, and legal use cases continue to expand as model intelligence and tool use evolves.

### In-house legal departments

In-house teams spend most of their time on documents that need to ship fast and are reviewed before going to the business or to outside counsel. Claude speeds up the drafting, giving counsel more time for the work that requires judgment, with:

* Contract review and redlining against playbook
* NDA triage and counterparty paper review
* Privacy impact assessments and data subject requests
* Outside counsel billing review and matter management
* Marketing copy and product feature review
* Board materials preparation and corporate governance tasks
* Regulatory monitoring and compliance updates

### Transactional review

Transactional practices spend the majority of their time on documents that follow standard formats and partner-led review. Claude can compress diligence cycles and improve coverage with:

* M&A diligence document review and summary memos
* Pitch book preparation and competitive analysis
* Comparable transaction analysis
* CIM and offering document drafting
* Closing checklist tracking

### Litigation and disputes

Litigation practices process huge volumes of unstructured material on tight timelines. Claude can shorten review cycles and improve consistency with:

* Discovery document review and privilege coding
* Deposition preparation and witness summaries
* Brief drafting and citation checking
* Pleadings analysis and motion drafting
* Expert report review

### Compliance and regulatory

Compliance and regulatory teams sit across structured filings and unstructured guidance, much of it in regulated jurisdictions. Claude can improve accuracy and timeliness across the program with:

* Regulatory filing preparation and review
* Audit response and gap analysis
* Policy drafting and jurisdictional comparison
* AI governance and vendor review
* KYC/AML screening and escalation

## Frequently asked questions for CIOs and IT leaders

To help you get up and running, here are some common questions related to Claude and Claude Cowork that legal teams might need to address for their CIOs.

**Note:** The questions below cover Claude.ai (web and desktop chat) and Claude Cowork (desktop application). Custom applications built on the Claude Platform have additional configuration options handled directly with the account team.

**Where are Claude.ai and Claude Cowork hosted?** Both are SaaS products hosted by Anthropic. Firms that need workloads to run inside their own cloud perimeter typically build custom applications on the Claude Platform via Amazon Bedrock, Google Vertex AI, or Microsoft Foundry, rather than using Claude.ai or Cowork directly.

**What does Claude Cowork install on user endpoints?** Cowork is a signed desktop application available for macOS and Windows. It runs as a standard user-space application, requires no kernel-level components, and updates through standard auto-update channels. IT can deploy and manage it through MDM and standard endpoint management tools.

**How does Claude Cowork access local files?** Cowork only reads files in folders the user explicitly grants access to from inside the application. Access is scoped per user, the same way modern desktop applications handle file permissions on macOS and Windows. There is no background indexing of the user's drive.

**Is our data used to train Claude's models?** No. Anthropic does not train on inputs or outputs from Enterprise Plan accounts using Claude.ai or Cowork.

**What retention controls are available?** Enterprise plans support custom data retention, including zero-retention configurations, for both Claude.ai conversations and Cowork sessions.

**Do you support Zero Data Retention (ZDR)?** ZDR is available on the Claude Platform (API) and Claude Code for approved customers. Claude.ai and Claude Cowork are stateful products—conversation history, Projects, and Cowork sessions require server-side storage to function—so ZDR does not apply there. Enterprise plans for those surfaces support custom retention windows configurable down to 30 days, and Anthropic does not train on customer data on any surface.

**What identity and access controls do you support?** Enterprise plans include SSO via SAML, SCIM for user provisioning, role-based access controls, and admin-managed plugin marketplaces for both surfaces.

**What certifications do you hold?** Anthropic is ISO/IEC 42001:2023 certified for responsible AI management and SOC 2 Type II audited. Additional documentation is available at [trust.anthropic.com (opens in new tab)](https://trust.anthropic.com).

**How does Claude Cowork integrate with our document management system?** Cowork connects to iManage, NetDocuments, Box, and more document management systems through MCP connectors. The connectors authenticate as the end user and respect entitlements at the matter and folder level, so Cowork only sees what the user already has access to.

**How is attorney-client privilege protected?** Privilege protection rests on access control and data handling. Connectors in Cowork honor the access controls already configured in your DMS or matter management system. Anthropic does not train on customer data, and Enterprise plans support custom retention. Firms working with privileged content typically pair this with firm-defined policies on which matters and document types can be processed.

**How do we set firm-wide policies and guardrails?** Plugins, skills, and connectors can be provisioned through admin-managed marketplaces in both Claude.ai and Claude Cowork rather than installed per user. This gives IT a single place to control which workflows are available and which approval steps are required before output moves downstream.

**Who are the subprocessors?** A current list of Anthropic subprocessors is published at [trust.anthropic.com (opens in new tab)](https://trust.anthropic.com) and updated as the list changes.

Learn more in our [Claude Cowork Enterprise Admin Guide (opens in new tab)](https://claude.com/resources/tutorials/claude-cowork-enterprise-administrator-guide).
