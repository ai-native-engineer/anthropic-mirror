<!-- source: https://claude.com/resources/tutorials/claude-enterprise-administrator-guide -->

# Claude Enterprise Administrator Guide

Walk through the four phases of a successful Claude Enterprise deployment: Technical Setup, Change Management & Launch, Enablement & Training, and Scaling Adoption. Includes Claude Code seat configuration and a complete resource directory.

  Professional
* Product

  Claude.ai
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/claude-enterprise-administrator-guide

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

*Deployment, Configuration, and Adoption Playbook*

This guide walks you through the four phases of a successful Claude Enterprise deployment: Technical Setup, Change Management & Launch, Enablement & Training, and Scaling Adoption. It also covers Claude.ai and Claude Code access controls, configuration options, and seat management.

**Phase 1: Technical Setup**

* Authentication & Access
* User Provisioning Options
* Security & Compliance
* Claude Code Access & Seat Configuration

**Phase 2: Change Management & Launch**

* Define Success Metrics
* Identify & Enable Champions
* Launch Communications

**Phase 3: Enablement & Training**

* Self-Service Learning Resources
* Feature-Specific Guides
* Claude Code Training Resources
* Internal Support Channels

**Phase 4: Scaling Adoption**

* Expanding Across Teams
* Measuring Impact
* Feature Rollout & Governance
* Sustaining Momentum

**Appendix:** Resource Directory

## Phase 1: Technical Setup

**Complete these technical configuration steps before launching Claude to your organization.**

### Authentication & Access

**Follow these steps to configure SSO:**

Claude Enterprise supports SAML 2.0 and OIDC (OpenID Connect) for single sign-on (SSO). See [Setting Up SSO](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso) for detailed configuration steps.

1. **Test SSO:** Configure with a small pilot group before broad rollout.
2. **Enable domain capture:** Automatically route users from your domain to your workspace. See [Domain Capture Setup](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning).
3. **Enforce SSO:** Require SSO for all access once configuration is validated.

### User Provisioning Options

Choose your provisioning method based on your organization's needs. See [User Provisioning Overview](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning) for setup instructions.

1. **SCIM (recommended):** System for Cross-domain Identity Management enables automatic sync from your identity provider (IdP). See [SCIM Setup Guide](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning).
2. **Just-in-Time (JIT):** Users are created upon first SSO login. Simple to set up but offers less control over access.
3. **Manual:** Admin-managed invitations via the [Admin Console](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans). Best for small, controlled pilots.

> **Example: Phased Rollout with SCIM**
>
> Many organizations use SCIM for a phased rollout approach:
>
> 1. Start with a pilot group of 50-100 users synced via SCIM
> 2. Monitor adoption and gather feedback for 2–4 weeks
> 3. Gradually expand SCIM groups to include additional departments
> 4. Enable organization-wide access once processes are established

### Security & Compliance

Claude Enterprise includes robust security and compliance features designed for enterprise environments:

Review security details at the [Anthropic Trust Center](https://trust.anthropic.com) and in the [Enterprise Plan Overview](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan).

1. **Data retention:** Conversations are retained per your policy and exportable via the [Compliance API](https://trust.anthropic.com/) and [Audit Logs](https://support.claude.com/en/articles/9970975-how-to-access-audit-logs), which also provide full activity logging for security monitoring.
2. **No model training:** Your organization's data is not used to train Claude models by default.
3. **Role-based access:** Primary Owner, Owner, and Member roles provide granular permissions. See [Member Roles Guide](https://support.claude.com/en/articles/9267276-roles-and-permissions).

### Pre-Launch Checklist

* Important considerations before setting up Identity Management — [Important Considerations](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)
* SSO configured and tested — [Setting Up SSO](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)
* User provisioning configured — [Provisioning Guide](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning)
* Security review completed with IT and information security teams
* Data retention policies documented
* Compliance API and Audit log access configured — [Trust Center](https://trust.anthropic.com/) and [Audit Logs](https://support.claude.com/en/articles/9970975-how-to-access-audit-logs)
* Set up Connectors — [Information on Connectors](https://support.claude.com/en/articles/11176164-pre-built-web-connectors-using-remote-mcp)
* Admin roles assigned — [Member Roles](https://support.claude.com/en/articles/9267276-roles-and-permissions)
* Claude Code seat configuration completed (see next section)

### Claude Code Access & Seat Configuration

#### Understanding Claude Enterprise Seat Types for Claude Code

Claude Enterprise offers different seat types depending on your pricing model. The following table summarizes the options and their Claude Code access implications:

| Pricing Model | Seat Type | Claude Code Access |
| --- | --- | --- |
| Seat-Based (Legacy) | Standard | No |
| Seat-Based (Legacy) | Premium | Yes |
| Usage-Based | Chat | No |
| Usage-Based | Chat + Code | Yes |
| Usage-Based | Claude Enterprise | Yes |

#### Admin Steps to Enable Claude Code

Follow these steps to enable Claude Code access for your users:

1. **Navigate to Settings > Organization > Members** in your Claude Enterprise admin console.
2. **For legacy seat-based plans:** Purchase Premium seats and assign them to users who need Claude Code access. Only Primary Owners/Owners can manage seat assignments.
3. **For usage-based plans:** Assign seats to users who need Claude Code. Configure spend limits as needed (defaults to $0). [See information here on setting spend limits.](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan#h_f7838fc97d)

#### User Authentication for Claude Code

Share the following steps with end users to connect Claude Code to their enterprise account:

* **Install Claude Code:** Run the command below that corresponds to your operating system to install Claude Code.
  + **macOS / Linux / WSL:** `curl -fsSL https://claude.ai/install.sh | bash`
  + **Windows (PowerShell):** `irm https://claude.ai/install.ps1 | iex`
* **Start Claude Code:** Type "claude" in your terminal.
* **Select login method:** Choose "Claude account with subscription".
* **Authenticate via Enterprise SSO** with your corporate credentials.
* **Your seat subscription will be linked to Claude Code** automatically upon successful authentication.

> **Troubleshooting**
>
> * If already logged in via a different account, run `/logout` first, then `/login`
> * Run "claude update" if not seeing the enterprise auth option
>   + Restart terminal after updates
>   + Console API key users switching to access via Claude Enterprise seats: Run `/logout`, then `/login` and select "Claude account with subscription"

#### Admin Monitoring for Claude Code

Monitor and manage Claude Code usage across your organization:

* Navigate to Analytics > Claude Code to view usage analytics
* Monitor usage across all surfaces (Claude.ai + Claude Code)

> **Important**
>
> Claude Code access requires a Premium seat (legacy model), or a Chat + Code or Claude Enterprise seat (usage-based model). Standard and Chat-only seats do NOT include Claude Code access.
>
> For organizations migrating from Console/API-based Claude Code access, users must re-authenticate via Enterprise SSO to link their subscription.

## Phase 2: Change Management & Launch

A successful Claude deployment requires thoughtful change management to drive adoption and demonstrate value.

### Define Success Metrics

Establish clear metrics to measure the success of your Claude deployment:

| Metric Category | Metric | Target | Measurement Method |
| --- | --- | --- | --- |
| Activity | Weekly Active Users | 70% of licensed seats | Admin Dashboard |
| Activity | Messages per User per Week | 25+ messages | Usage Analytics |
| Activity | Feature Adoption (Projects, Artifacts) | 40% of active users | Feature Analytics |
| Impact | Time Saved per User per Week | 3+ hours | User Survey |
| Impact | User Satisfaction Score | 4.0+ / 5.0 | Quarterly Survey |
| Impact | Tasks Augmented by Claude | 5+ per week | User Self-Report |

### Identify & Enable Champions

Champions are enthusiastic early adopters who can help drive adoption across their teams:

* Select 2–3 champions per department or team
* Provide champions with early access and advanced training
* Equip champions with talking points and demo guidance
* Create a champions Slack channel or Teams group for peer support
* Recognize and reward champion contributions to adoption

### Launch Communications

Plan a multi-channel communication strategy for your launch:

* **Pre-Launch (2 weeks before):** Communications highlighting benefits and use cases
* **Launch Day:** Executive announcement, getting started guide, training schedule
* **Post-Launch (Week 1):** Tips and tricks, success stories from pilot users
* **Ongoing:** Weekly tips, monthly newsletters, quarterly business reviews

## Phase 3: Enablement & Training

Provide comprehensive training resources to help users get the most from Claude.

### Structured Training Programs

Deploying Claude is a technical milestone, but adoption depends on whether people know how to use it effectively. A structured training program ensures users move past initial curiosity into productive, habitual use — and reduces the support burden on your IT and champion teams.

* **All-Staff 101 Sessions:** Workshops (30–60 min) covering the basics — navigating the interface, writing effective prompts, and using core features like Projects and Artifacts. Run at launch and repeat for new hire cohorts.
* **Department-Level Enablement:** Targeted sessions built around each team's actual workflows, with an executive sponsor to signal leadership support. Partner with team leads to identify high-value use cases and provide ready-to-use prompt templates. Schedule a follow-up 2–4 weeks later to address questions from real usage.
* **Office Hours:** Weekly or biweekly drop-in sessions where users bring real work and get hands-on help from champions. Especially valuable in the first 30–60 days.
* **LMS Integration:** If your organization uses an LMS, package Claude training into trackable courses to monitor enablement coverage and tie completion to access or feature rollout milestones.

### Self-Service Learning Resources

Direct users to these Anthropic-provided learning resources:

* [Anthropic Academy](https://anthropic.skilljar.com) — Interactive courses covering Claude fundamentals, prompt engineering, and advanced features
* [Use Case Library](https://claude.com/resources/use-cases/category/professional) — Curated examples of Claude applications across different business functions
* [Help Center](https://support.claude.com) — Comprehensive documentation and FAQs on Claude Enterprise
* [Docs Site](https://docs.claude.com/) — Comprehensive support for Claude Code and API use

### Feature-Specific Guides

Ensure users understand key enterprise features:

[**Projects**](https://support.claude.com/en/articles/9517075-what-are-projects)**:** Organize conversations by topic, client, or workflow. Projects maintain context across conversations and can be shared with team members.

[**Artifacts**](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)**:** Create and iterate on documents, code, analyses, and visualizations within conversations. Artifacts can be exported and shared.

[**Skills**](https://support.claude.com/en/articles/12512176-what-are-skills)**:** Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks.

[**Enterprise Search**](https://support.claude.com/en/articles/12489464-using-enterprise-search)**:** Connect internal knowledge bases and documents to Claude for organization-specific answers. Supports various file formats and integrations.

### Claude Code Training Resources

Provide these resources to help users get started with Claude Code:

* [Quick Start Guide](https://code.claude.com/docs/en/overview)
* [Claude Code Walkthrough](https://anthropic.skilljar.com/claude-code-in-action)
* [Mastering Claude Code in 30 minutes](https://www.youtube.com/watch?v=6eBSHbLKuN0)
* [Claude Code — DeepLearning.ai Short Course](https://www.deeplearning.ai/short-courses/claude-code-a-highly-agentic-coding-assistant/)
* [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
* [Building and Prototyping with Claude Code](https://www.youtube.com/watch?v=DAQJvGjlgVM)

### Internal Support Channels

Establish ongoing support infrastructure for your Claude users:

* Dedicated Slack/Teams channel for Claude questions and tips
* Weekly office hours with champions or power users
* IT helpdesk integration for access and technical issues
* Monthly user group meetings to share best practices
* Dedicated Claude Code support channel for developer-specific questions

## Phase 4: Scaling Adoption

After initial deployment, focus on expanding usage, building internal ownership, and demonstrating sustained value across the organization.

### Expanding Across Teams

Prioritize teams with strong use case fit and willing champions. For each new team:

* Conduct a brief needs assessment to identify high-value workflows
* Provision seats (including Claude Code for developer teams) and deliver tailored onboarding
* Appoint a local champion to drive adoption and share early wins across the organization

### Measuring Impact

Shift from tracking activity metrics to demonstrating business value. Focus on outcomes that matter to leadership:

* Track adoption (active users, department penetration, feature usage) via the Admin dashboards and API
* Measure productivity gains (hours saved, tasks augmented) through periodic user surveys
* Pair quantitative data with qualitative examples – short case studies from team leads illustrating real impact
* Establish a regular reporting cadence (e.g., quarterly business reviews) to keep stakeholders informed

### Feature Rollout & Governance

Introduce advanced capabilities gradually so teams can build confidence without feeling overwhelmed. A natural progression might move from core features (Projects, Artifacts, Connectors) to intelligence features (Enterprise Search, Research) to integrations (Claude Code, Skills) and finally to automation (Cowork, custom connectors).

As usage grows, revisit your governance posture:

* Review data retention policies, audit log cadences, and project visibility defaults
* Maintain an allowlist of approved connectors and extensions, routing new requests through your standard IT governance process
* Configure usage guardrails to manage consumption as the user base expands

### Sustaining Momentum

Long-term success depends on building internal ownership and feedback loops:

* Designate a program owner and consider forming a lightweight Center of Excellence to curate prompts, Skills, and playbooks
* Run periodic user surveys, champion roundtables, and usage analytics reviews to surface what's working and what needs attention
* Refresh training materials quarterly to reflect new features and lessons learned
* Incorporate Claude onboarding into your standard new hire orientation
* At each phase of rollout, consider a brief retrospective:
  + What use cases emerged?
  + What barriers remain?
  + What should change for the next phase?

## Appendix: Resource Directory

A comprehensive directory of support, training, and enablement resources for Claude Enterprise administrators and end users.

### Getting Started

**Essential resources for new deployments and first-time users:**

* [Getting started with Claude](https://support.claude.com/en/articles/8114491-getting-started-with-claude) — First steps, basic navigation, and starting your first conversation
* [What are some things I can use Claude for?](https://support.claude.com/en/articles/7996845-what-are-some-things-i-can-use-claude-for) — Common use cases including writing, analysis, coding, research, and creative tasks
* [What is the Enterprise plan?](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan) — Enterprise features including SSO, SCIM, audit logs, custom retention, and dedicated support
* [Release Notes](https://support.claude.com/en/articles/12138966-release-notes) — Chronological log of new features, improvements, and changes across all Claude products
* [How to get support](https://support.claude.com/en/articles/9015913-how-to-get-support) — Contacting Anthropic support, submitting tickets, and self-service resources

### Training & Enablement

**Resources to upskill your organization on Claude:**

* [Anthropic Academy](https://anthropic.skilljar.com) — Self-paced courses on prompt engineering, Claude features, and best practices
* [Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering) — Comprehensive documentation on advanced prompt engineering techniques
* [Introduction to Prompt Design](https://support.claude.com/en/articles/7996853-introduction-to-prompt-design) — Foundational prompt engineering principles
* [Claude Enterprise Help Center](https://support.claude.com) — Central hub for all Claude help articles and documentation
* [Use Case Library](https://www.anthropic.com/customers) — Real-world examples of how organizations use Claude

### Identity & Access Management

* [Identity Management](https://support.claude.com/en/collections/17270717-identity-management-sso-jit-scim) — SSO setup (SAML 2.0 / OIDC), JIT and SCIM provisioning, and IdP migration
* [Restrict access with IP allowlisting](https://support.claude.com/en/articles/13200993-restrict-access-to-claude-with-ip-allowlisting) — Network-level access control by restricting Claude to approved IP ranges
* [Enforce Tenant Restrictions](https://support.claude.com/en/articles/13198485-enforce-network-level-access-control-with-tenant-restrictions) — Prevent users from accessing unauthorized Claude organizations from your network
* [Configuring session security settings](https://support.claude.com/en/articles/13163631-configuring-session-security-settings) — Session timeout, re-authentication, and session management policies

### User & Seat Management

* [Managing members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans) — Inviting, removing, and managing user roles from the admin console
* [Roles and Permissions](https://support.claude.com/en/articles/9267276-roles-and-permissions) — Owner, Admin, and Member permission levels
* [Purchasing and managing seats](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans) — Seat allocation, scaling, and license management
* [Find and join your organization](https://support.claude.com/en/articles/13566435-find-and-join-a-team-or-enterprise-organization) — How end users discover and join their company's Claude organization
* [Migrating individual accounts to Enterprise](https://support.claude.com/en/articles/9267400-can-individuals-with-pro-or-max-plan-accounts-migrate-them-to-team-or-enterprise-plan-organizations) — Migration paths and data handling when transitioning plan types
* [What happens to a user's data when removed?](https://support.claude.com/en/articles/12053672-what-happens-to-a-user-s-data-when-they-are-removed-from-a-team-or-enterprise-organization) — Data retention and cleanup policies when removing users

### Governance & Compliance

* [Exporting organization data](https://support.claude.com/en/articles/13346720-how-can-i-export-my-organization-s-data) — Bulk data export for compliance, migration, or backup
* [Usage analytics](https://support.claude.com/en/articles/12883420-usage-analytics-for-team-and-enterprise-plans) — Dashboard for tracking adoption, usage patterns, and seat utilization
* [Audit logs](https://support.claude.com/en/articles/9970975-how-to-access-audit-logs) — Track user activity, conversations, and admin changes
* [Custom Data Retention Controls](https://support.claude.com/en/articles/10440198-custom-data-retention-controls-for-enterprise-plans) — Configure retention windows from 1 day to indefinite
* [Compliance API](https://support.claude.com/en/articles/13015708-how-can-i-access-the-compliance-api) — Programmatic access for DLP, eDiscovery, and regulatory needs
* [HIPAA-ready Enterprise plans](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans) — HIPAA compliance capabilities, BAA availability, and healthcare configuration
* [Business Associate Agreements (BAA)](https://support.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers) — How to request and execute a BAA with Anthropic
* [Security & Compliance Overview (Trust Center)](https://trust.anthropic.com) — Certifications (SOC 2 Type II, CSA STAR), pen test reports, and compliance documentation

### Billing & Usage

* [Enterprise billing](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan) — Billing structure, invoicing, and payment options
* [Extra usage controls](https://support.claude.com/en/articles/12005970-extra-usage-for-team-and-seat-based-enterprise-plans) — Overage pricing and usage guardrails for organizational plans
* [Usage limits and best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices) — Tips for staying within limits and optimizing conversation efficiency

### Admin Controls

* [Project visibility and sharing](https://support.claude.com/en/articles/9519189-project-visibility-and-sharing) — Admin controls for project sharing policies
* [Disabling public projects](https://support.claude.com/en/articles/9927533-how-can-i-disable-public-projects) — Restrict project sharing to internal-only
* [Managing user feedback settings](https://support.claude.com/en/articles/10504844-managing-user-feedback-settings-on-team-and-enterprise-plans) — Configure whether user feedback is shared with Anthropic
* [Cowork for Enterprise](https://support.claude.com/en/articles/13455879-cowork-for-team-and-enterprise-plans) — Enabling and configuring Cowork mode for your organization
* [Visual and interactive content controls](https://support.claude.com/en/articles/13663666-visual-and-interactive-content-for-team-and-enterprise-plans) — Admin controls for visual content generation features

### Projects & Knowledge Management

* [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects) — Persistent workspaces for grouping conversations, uploading reference files, and setting custom instructions
* [Examples of projects you can create](https://support.claude.com/en/articles/9529781-examples-of-projects-you-can-create) — Use case inspiration across different roles and workflows
* [RAG for projects](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects) — How Claude searches uploaded project files for grounded, accurate responses
* [Chat search and memory](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context) — Search past conversations and let Claude remember key details across sessions

### Content Creation & Artifacts

* [What are artifacts?](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them) — Interactive content blocks for code, documents, websites, and visualizations
* [Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude) — Generate Word docs, spreadsheets, presentations, and other file types
* [Visual and interactive content](https://support.claude.com/en/articles/13641943-visual-and-interactive-content) — Charts, diagrams, interactive web apps, and visual outputs
* [Uploading files to Claude](https://support.claude.com/en/articles/8241126-uploading-files-to-claude) — Supported file types, size limits, and best practices

### Research & Reasoning

* [Using Research](https://support.claude.com/en/articles/11088861-using-research-on-claude) — Deep research mode that searches the web and synthesizes findings into comprehensive reports
* [Web search](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search) — Real-time web search to supplement Claude's knowledge with current information
* [Extended thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking) — Step-by-step reasoning for complex problems
* [When to use search vs. thinking vs. Research](https://support.claude.com/en/articles/11095361-when-should-i-use-web-search-extended-thinking-and-research) — Decision guide for choosing the right tool

### Skills & Customization

* [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills) — Reusable instruction sets that teach Claude specialized workflows and domain expertise
* [How to create custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) — Build skills through natural conversation or manual configuration
* [Provisioning Skills for your organization](https://support.claude.com/en/articles/13119606-provisioning-and-managing-skills-for-your-organization) — Deploy skills across teams and manage the organizational skills catalog

### Cowork & Desktop Agent

* [Getting started with Cowork](https://support.claude.com/en/articles/13345190-getting-started-with-cowork) — Desktop agent mode where Claude creates files, runs code, and automates workflows
* [Using Cowork safely](https://support.claude.com/en/articles/13364135-using-cowork-safely) — Safety guidelines and sandboxing details

### Personalization

* [Personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) — Memory, preferred name, and options that shape Claude's responses
* [Custom styles](https://support.claude.com/en/articles/10181068-configure-and-use-styles) — Create and apply response styles (concise, detailed, formal, casual, etc.)
* [Language preferences](https://support.claude.com/en/articles/10769299-how-to-use-claude-in-your-preferred-language) — Multilingual support and language settings

### Enterprise Search & Data

* [Using Enterprise Search](https://support.claude.com/en/articles/12489464-using-enterprise-search) — Search across connected organizational data sources within Claude

### Integration Overview

* [When to use desktop vs. web connectors](https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors) — Comparison of web-based (Remote MCP) and desktop connector architectures
* [Interactive Connectors](https://support.claude.com/en/articles/13454812-using-interactive-connectors-in-claude) — Connectors that let Claude take actions (not just read data) in external tools

### Pre-Built Connectors

**Ready-to-use integrations with popular enterprise tools:**

* [Google Drive](https://support.claude.com/en/articles/10166901-using-the-google-drive-integration) — Access, search, and reference Google Drive files in conversations
* [GitHub](https://support.claude.com/en/articles/10167454-using-the-github-integration) — Browse repos, review PRs, search code, and manage issues
* [Slack](https://support.claude.com/en/articles/11506255-getting-started-with-claude-in-slack) — Install and use the Claude Slack app in your workspace
* [Microsoft 365](https://support.claude.com/en/articles/12542951-enabling-and-using-the-microsoft-365-connector) — Connect Outlook, OneDrive, Teams, and other M365 services
* [Microsoft 365 Security Guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide) — Data handling, permissions, and security architecture for the M365 connector
* [All pre-built web connectors](https://support.claude.com/en/articles/11176164-pre-built-web-connectors-using-remote-mcp) — Full list of available pre-built connectors using Remote MCP

### Custom Connectors

**Build your own connectors for proprietary or specialized tools:**

* [Building custom connectors](https://support.claude.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers) — Technical guide for developing and deploying Remote MCP server connectors
* [Building desktop extensions with MCPB](https://support.claude.com/en/articles/12922929-building-desktop-extensions-with-mcpb) — MCPB tooling for installable desktop extensions

### Desktop & Browser

* [Claude Desktop](https://support.claude.com/en/collections/16163169-claude-desktop) — Installation, enterprise deployment (Windows/macOS via MDM), managed configuration, and extension allowlists
* [Claude in Chrome](https://support.claude.com/en/collections/18031491-claude-in-chrome) — Browser extension setup, permissions, admin controls, safety best practices, and troubleshooting

### Mobile

* [Claude Mobile Apps](https://support.claude.com/en/collections/9387080-claude-mobile-apps) — iOS and Android installation, voice mode, dictation, widgets, and shortcuts

### Productivity Suites

* [Claude in Excel](https://support.claude.com/en/articles/12650343-using-claude-in-excel) — AI-powered formulas, data analysis, and chart creation within Excel
* [Claude in PowerPoint](https://support.claude.com/en/articles/13521390-using-claude-in-powerpoint) — Generate and edit slide decks directly inside PowerPoint
* [Google Sheets add-on](https://support.claude.com/en/articles/13162029-google-sheets-add-on) — Data analysis and formula help directly in Google Sheets

### Developer Tools

* [Claude in Xcode](https://support.claude.com/en/articles/12293051-using-claude-in-xcode) — Code completion, debugging, and refactoring in Apple's Xcode IDE
* [Claude in Microsoft Foundry](https://support.claude.com/en/articles/12864745-using-claude-in-microsoft-foundry) — Access Claude models through Microsoft's AI Foundry platform

### Claude Code Setup & Configuration

* [Claude Code](https://support.claude.com/en/collections/14445694-claude-code) — Team/Enterprise setup, model configuration, security reviews, and usage analytics
* [Using Claude Code with Team or Enterprise Plan](https://support.claude.com/en/articles/11845131-using-claude-code-with-your-team-or-enterprise-plan) — Configuration and deployment for organizational plans
* [Claude Code Usage Analytics](https://support.claude.com/en/articles/12157520-claude-code-usage-analytics) — Track adoption and usage across your organization
* [Claude Code Troubleshooting](https://support.claude.com/en/articles/12386420-claude-code-faq) — Common issues, fixes, and debugging steps

### Claude Code Training

* [Anthropic Academy — Claude Code in Action](https://anthropic.skilljar.com) — Self-paced course on Claude Code workflows

### Function-Specific Guides

**Share these guides with team leads to accelerate adoption in their departments:**

* [Claude for Engineering Teams](https://support.claude.com/en/articles/9945689-claude-for-engineering) — Code review, debugging, architecture, and technical workflows
* [Claude for Marketing Teams](https://support.claude.com/en/articles/9945697-claude-for-marketing) — Content creation, campaign analysis, and brand voice
* [Claude for Sales Teams](https://support.claude.com/en/articles/9945703-claude-for-sales) — Outreach drafting, research, and pipeline management
* [Claude for Product Management](https://support.claude.com/en/articles/9999062-claude-for-product-management) — PRDs, competitive analysis, and user research synthesis
* [Claude for Human Resources](https://support.claude.com/en/articles/9998942-claude-for-human-resources) — Policy drafting, interview prep, and employee communications

### Industry Solutions

**Specialized resources and connectors for regulated and vertical industries:**

* [Claude for Financial Services](https://support.claude.com/en/collections/13972013-claude-for-financial-services) — Getting started, workflows, prompting strategies, skills, and market data connectors (FactSet, S&P Global, Moody's, Morningstar, PitchBook, LSEG, Aiera, Daloopa)
* [Claude for Life Sciences](https://support.claude.com/en/collections/16142619-claude-for-life-sciences) — Getting started plus connectors for BioRender, PubMed, Benchling, Synapse.org, 10x Genomics, and Scholar Gateway
* [Claude for Education](https://support.claude.com/en/collections/12630177-claude-for-education) — Admin deployment guide, Canvas LTI integration, FERPA-compliant data controls, and end-user FAQs
* [Claude for Nonprofits](https://support.claude.com/en/collections/17047088-claude-for-nonprofits) — Getting started plus connectors for Benevity, Blackbaud, and Candid

### Privacy & Data Handling

* [Privacy practices](https://support.claude.com/en/articles/10035659-where-can-i-learn-more-about-anthropic-s-privacy-practices) — How Anthropic handles user data, model training, and privacy controls
* [Who can view my conversations?](https://support.claude.com/en/articles/8325621-i-would-like-to-input-sensitive-data-into-my-chats-with-claude-who-can-view-my-conversations) — Data visibility, access controls, and conversation privacy by plan type
* [Data ownership for teams](https://support.claude.com/en/articles/9265372-who-owns-and-manages-the-data-of-my-team) — Data ownership policies for organizational plans
* [Data Processor vs. Controller](https://support.claude.com/en/articles/9267385-does-anthropic-act-as-a-data-processor-or-controller) — GDPR role clarification for Anthropic's data handling
* [Data deletion for Enterprise](https://support.claude.com/en/articles/9796617-can-you-delete-data-that-i-sent-via-team-and-enterprise-plans) — Data deletion requests and processes for organizational plans
* [Data Processing Addendum (DPA)](https://support.claude.com/en/articles/7996862-how-do-i-view-and-sign-your-data-processing-addendum-dpa) — Self-service DPA signing for GDPR compliance
* [Safeguards](https://support.claude.com/en/collections/4078535-safeguards) — Usage policy, safeguard appeals, agent guidelines, content reporting, and vulnerability reporting

### Troubleshooting

**Common issues and resolution guides:**

* [Understanding error messages](https://support.claude.com/en/articles/12466728-understanding-claude-error-messages) — Decode common error messages and their solutions
* [Incorrect or misleading responses](https://support.claude.com/en/articles/8525154-claude-is-providing-incorrect-or-misleading-responses-what-s-going-on) — Understanding hallucinations and how to get more accurate answers
* [Content filtering errors](https://support.claude.com/en/articles/9205721-why-am-i-receiving-an-output-blocked-by-content-filtering-policy-error) — Why outputs may be blocked and how to adjust your approach

### Video Tutorials

**Share these video walkthroughs with your team for visual, hands-on learning.**

#### Getting Started Videos

* [Getting started with Claude.ai](https://support.claude.com/en/articles/12997377-getting-started-with-claude-ai) — Interface walkthrough, first conversation, and key features
* [Intro to Artifacts](https://support.claude.com/en/articles/9945615-intro-to-artifacts) — Creating and using artifacts in conversations
* [Intro to Projects](https://support.claude.com/en/articles/9945648-intro-to-projects) — Setting up and managing projects
* [Intro to Connectors](https://support.claude.com/en/articles/13123742-intro-to-connectors) — Connecting external tools and data sources
* [Using Research](https://support.claude.com/en/articles/11106443-using-research) — Demo of deep research capabilities

#### Feature Deep Dives

* [Connect your tools for a smarter AI companion](https://support.claude.com/en/articles/11817150-connect-your-tools-to-unlock-a-smarter-more-capable-ai-companion) — Setting up integrations for enhanced capabilities
* [Create and edit files to eliminate busy work](https://support.claude.com/en/articles/12143746-create-and-edit-files-with-claude-to-eliminate-hours-of-busy-work) — Document automation with Claude's file creation features
* [Prototype AI apps with artifacts](https://support.claude.com/en/articles/11649438-prototype-ai-powered-apps-with-claude-artifacts) — Building functional app prototypes using artifacts
* [Teach Claude your way of working using skills](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills) — Creating and applying skills for consistent outputs
* [Create a skill through conversation](https://support.claude.com/en/articles/12599426-how-to-create-a-skill-with-claude-through-conversation) — Building skills via natural conversation
* [Claude in Chrome](https://support.claude.com/en/articles/12431227-simplify-your-browsing-experience-with-claude-in-chrome) — Walkthrough of the Claude in Chrome extension

#### Integration Tutorials

* [Using the GitHub integration](https://support.claude.com/en/articles/9945670-using-the-github-integration) — GitHub connector setup and usage
* [Using the Google Docs integration](https://support.claude.com/en/articles/10389539-using-the-google-docs-integration) — Working with Google Docs in Claude

#### Function & Industry Videos

* [Claude for Engineering](https://support.claude.com/en/articles/9945689-claude-for-engineering) — Code review, debugging, architecture, and technical workflows
* [Claude for Marketing](https://support.claude.com/en/articles/9945697-claude-for-marketing) — Content creation, campaign analysis, and brand voice
* [Claude for Sales](https://support.claude.com/en/articles/9945703-claude-for-sales) — Outreach drafting, research, and pipeline management
* [Claude for Product Management](https://support.claude.com/en/articles/9999062-claude-for-product-management) — PRDs, competitive analysis, and user research synthesis
* [Claude for Human Resources](https://support.claude.com/en/articles/9998942-claude-for-human-resources) — Policy drafting, interview prep, and employee communications
* [Investment Research](https://support.claude.com/en/articles/12068906-using-claude-for-financial-services-for-investment-research) — Market data connectors for equity research workflows
* [Analysis and Modeling](https://support.claude.com/en/articles/12068923-using-claude-for-financial-services-for-analysis-and-modeling) — DCF modeling, comp analysis, and financial statement analysis
* [Investment Memos](https://support.claude.com/en/articles/12068945-using-claude-for-financial-services-for-investment-memos) — Drafting investment memos and thesis documentation
* [Browse all video tutorials](https://support.claude.com/en/collections/10548294-video-tutorials) — Full collection of 26 video tutorials

## Related tutorials

[Tasks to try with @Claude in your workspace](/resources/tutorials/tasks-to-try-with-claude-tag-in-your-workspace)Tasks to try with @Claude in your workspace

Tasks to try with @Claude in your workspace

Tutorial

[Tutorial](/resources/tutorials/tasks-to-try-with-claude-tag-in-your-workspace)Tutorial

[Best practices for using @Claude](/resources/tutorials/best-practices-using-claude-tag)Best practices for using @Claude

Best practices for using @Claude

Tutorial

[Tutorial](/resources/tutorials/best-practices-using-claude-tag)Tutorial

[Using Claude Cowork for legal: answer fast questions on past decisions](/resources/tutorials/using-claude-cowork-for-legal-question-briefing)Using Claude Cowork for legal: answer fast questions on past decisions

Using Claude Cowork for legal: answer fast questions on past decisions

Tutorial

[Tutorial](/resources/tutorials/using-claude-cowork-for-legal-question-briefing)Tutorial

[Using Claude Cowork for marketing ops: run a weekly review that preps itself](/resources/tutorials/using-claude-cowork-for-marketing-ops-review)Using Claude Cowork for marketing ops: run a weekly review that preps itself

Using Claude Cowork for marketing ops: run a weekly review that preps itself

Tutorial

[Tutorial](/resources/tutorials/using-claude-cowork-for-marketing-ops-review)Tutorial
