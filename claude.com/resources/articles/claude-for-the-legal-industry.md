<!-- source: https://claude.com/resources/articles/claude-for-the-legal-industry -->

Earlier this year we released our first legal plugin, and in the months since, legal professionals have become the most engaged Claude Cowork users of any knowledge-work function. We’re now building on that with a much larger set of tools.

Legal work runs on a specific technology stack: contract lifecycle systems, research platforms, document management, e-discovery, data rooms, firm-specific precedents, and much more. Claude now connects to all of it through several key building blocks. First, [MCP connectors](https://claude.ai/directory/connectors) bring your legal work (the documents, communications, and records tied to specific matters) into Claude. Secondly, practice-area plugins package the tasks that lawyers run most often. And finally, because both are built on open protocols, firms and in-house teams can customize Claude to match the way they actually practice.

Today we’re introducing 20+ new MCP connectors that link Claude to the software the legal industry already relies on, and 12 new plugins tailored to specific legal work and practice areas. And finally, we're partnering with the Free Law Project, the Justice Technology Association, and others working to put legal help within reach of people who can’t currently access it.

‍

## Claude works where legal teams work

Claude meets legal teams where they are, working directly inside Microsoft Word, Outlook, Excel, and PowerPoint while carrying context across all four apps. A redline finished in Word doesn’t need to be re-explained when it becomes a cover note in Outlook, a closing checklist in Excel, or a board summary in PowerPoint.

In **Word**, Claude skills—reusable instructions that encode a team's playbooks and standards—handle drafting, redlining, and clause-by-clause comparisons against those playbooks, tracking every change and explaining the reasoning behind it. They also take on the rote work in between every turn: scrubbing internal comments before a draft goes to the counterparty, running a final formatting check on an execution copy, and pulling fallback language from approved playbooks.

In **Outlook**, Claude triages incoming matter work: flagging contract requests, drafting responses and cover notes, and scheduling follow-ups so nothing pile ups.

In **Claude Cowork**, the same connectors and plugins are available for work that spans many documents: triaging a batch of contracts, clearing a product feature for launch, and drafting a note on regulatory developments for the board. Scheduled tasks can automate recurring work such as weekly regulatory update sweeps or intake triage.

And with **Projects**, matter teams get a persistent workspace where precedents and prior drafts are retained across every conversation.

## New connectors across the legal stack

New MCP connectors let Claude interact with the systems that legal teams already rely on.

**Contract lifecycle and drafting**

* **Definely**, which gives live, deterministic access to contract structure for review: resolve definitions, validate cross-references, map dependencies, and run structural diffs to see how edits propagate across an agreement;**‍**
* **Docusign,** which connects Claude to your agreement data so you can quickly surface key terms like renewal dates and obligations, and orchestrate agreement workflows across the contract lifecycle, from drafting through signature and post signature management;
* **Ironclad**, which lets Claude access your contract repository and workflows and ask questions about contracts in plain language, with results automatically scoped to each user's permissions.

**Deal rooms and transaction documents**:

* **Box**, which connects Claude to content stored in Box to search and access files, query documents, create or update content, and extract metadata fields, while enforcing existing Box security and access policies;
* **Datasite**, which connects Claude to your Datasite virtual data room—the secure workspace where thousands of M&A deals are facilitated annually—to set up folder structures, invite users, search documents, track buyer Q&A, and audit data room readiness.

**Document management:**

* **iManage,** a knowledge work platform, gives Claude permission-bound, auditable access to governed iManage content, including matter history, documents, and institutional knowledge, eliminating the need for bulk exports or custom integrations;**‍**
* **NetDocuments**, which lets Claude search and retrieve documents from your NetDocuments repository and draft new documents based on your precedents, with full respect for your organization's permissions and governance policies.

**Expert networks and skills:**

* **Lawve AI,** which offers a curated library of legal AI skills written by practicing lawyers, in-house counsel, and legal technologists, searchable from inside Claude;
* **The L Suite,** which offers two MCP connectors from their leading in-house counsel community: (1) Lloyd, which allows The L Suite members to connect Claude with the Braintrust member platform; and (2) TopCounsel, which helps any in-house counsel find the right outside counsel for a specific matter based on The L Suite's proprietary dataset and ranking algorithm.

**E-discovery and review:**

* **Consilio**, which puts a client’s own live matters and Consilio’s Aurora Legal AI at Claude's fingertips, with every response scoped to what the user is already entitled to see;
* **Everlaw**, which provides a litigation platform, lets Claude search, organize, and retrieve documents from Everlaw projects using metadata, keywords, and document types, with direct review links;
* **Relativity**, which lets Claude stand up matters, shape workspace schema, govern access, and analyze usage in its AI platform for legal data intelligence, RelativityOne.

**Fiduciary-grade workflows:**

* **Thomson Reuters,** which connects Claude to CoCounsel Legal, a fiduciary-grade system for end-to-end drafting, research, review, and validation across all major practice areas, serving as an AI assistant for high-stakes legal work, grounded in Westlaw primary law, Practical Law guidance, KeyCite, and your own documents, with transparent and verifiable outputs.

**Legal research and case law:**

* **Legal Data Hunter**, which gives Claude access to the world's fastest growing legal corpus: 31M+ documents from 160+ jurisdictions, including EU consolidated law, case law from supreme and constitutional courts, and official doctrine;
* **Midpage**, which connects Claude to a database of case law for complex legal research, opinion review, and work product, with everything hyperlinked to real sources for easy verification;
* **Trellis**, which gives Claude direct access to the largest state trial-court dataset in the US, including dockets, rulings, verdicts, and filings, for judge and opposing-counsel analytics and motion drafting.

**Legal AI assistants:**

* **Harvey**, which brings Harvey's legal intelligence into Claude, supporting general legal inquiries, analysis over Vault projects, and research questions for select knowledge sources;
* **Solve Intelligence**, which connects Claude to patent and non-patent literature, legal texts, SEP technical standards, and the open web for prior-art search, claim mapping, and patent drafting.

**Public service**

* **BoardWise**, which guides licensed professionals facing state board matters: helping them understand deadlines, navigate their situation, and draft structured response letters tailored to their jurisdiction;
* **Courtroom5**, which provides legal guidance to the roughly 80% of civil litigants who appear in court without an attorney, with jurisdiction-aware case intake, deadline calculation, and next-step guidance across all 50 states;
* **Descrybe**, which gives Claude legal-research tools for working with primary law: search cases by concept or citation, check treatment status, find citing authorities, and verify quoted language;
* **Free Law Project**, which connects Claude to CourtListener's millions of US court opinions, PACER dockets, judge profiles, oral arguments, and citation data.

## Practice-area plugins

Legal work looks different depending on the seat you're in. We're releasing 12 practice-area plugins (download them from the Legal Marketplace, [here](https://github.com/anthropics/claude-for-legal)), each built around a specific legal role. Every plugin starts with a short setup interview that learns your practice: your playbook, your escalation chain, your risk calibration, your house style, so Claude’s answers are not generic but rather tailored for your team. These include:

* **Commercial Legal** reviews vendor agreements and NDAs against your playbooks and routes escalations with a plain-language summary for business stakeholders.
* **Corporate Legal** handles M&A: diligence across the data room, disclosure schedules, board consents, and the closing checklist. It can be configured for board work, public-company governance, or entity compliance.
* **Employment Legal** covers hires, terminations, worker classification, leave deadlines, and investigations, and drafts policies with state-specific rules built in.
* **Privacy Legal** reviews DPAs against your playbook, triages PIAs and DPIAs, prepares DSAR responses within statutory timelines, and flags gaps between written policy and actual practice.
* **Product Legal** runs launch reviews against your internal framework, checks marketing claims for substantiation, and answers risk questions from teams across the business.
* **Regulatory Legal** monitors regulatory developments, filters them to your materiality threshold, compares new rules against your policy library, and tracks gaps and comment deadlines.
* **AI Governance Legal** triages AI use cases against your governance tiers, runs impact assessments, reviews vendor AI terms, and can draft a starting AI policy.
* **IP Legal** conducts trademark clearance and freedom-to-operate triage, drafts and responds to cease-and-desist letters, handles DMCA takedowns and open-source compliance, and screens invention disclosures.
* **Litigation Legal** manages matter intake and portfolio tracking, legal holds, demand letters, subpoena triage, chronologies, deposition preparation, privilege logs, and brief drafting.
* **Law Student** provides Socratic drilling, case briefs, IRAC grading, and bar preparation with jurisdiction-specific distinctions.
* **Legal Clinic** manages client intake, deadline tracking, case memos, and the supervisor review queue.
* **Legal Builder Hub** finds and installs community-built legal skills from public registries, running a security review, license check, and freshness check on every install and update.

Each agent template can be installed in Cowork or Claude Code with a click, and produces outputs that match institutional drafting standards. [A subset of these](https://github.com/anthropics/claude-for-legal) (Commercial Legal, Corporate Legal, Litigation Legal, Product Legal, Litigation Legal) are also available as cookbooks that can be deployed as Managed Agents in the Claude Platform for programmatic use. Teams can layer on their own precedents and playbooks to customize the skills.

Every legal organization works differently, and no single set of plugins can cover every practice. The plugin and skill ecosystem are open protocols, and early contributors including **Box, Legal Quants, Lawve AI**, and **Thomson Reuters** have already shipped skills, plugins, and style conventions of their own. Any partner can submit connectors and skills through the [Directory](https://preview.claude.ai/local_sessions/link).

## Democratizing access to legal services with AI

Legal services are out of reach for many people and small businesses, and the gap is widening. We’re working with the **Free Law Project**, **Justice Technology Association** and other legal aid and Public Service organizations to help make legal services more affordable and available.

Qualifying legal aid clinics, public defenders, and nonprofit legal services organizations can gain access to significantly discounted pricing through the [Claude for Nonprofits program](https://claude.com/solutions/nonprofits). Free and low-cost tools from BoardWise, Courtroom5, Descrybe, and Free Law Project are available to Claude users via MCP connectors as well.

> “"Most people don't know they have legal rights until it's too late to use them. Claude can now meet them where they are — in the moment they're scared and searching for answers."  - Sonja Ebron, CEO & Co-Founder, Courtroom5”

## Trusted across the legal industry

Firms and in-house teams have moved from testing Claude to running their practice on it — and the legal tools they rely on are increasingly built on Claude too. At our [Briefing: Enterprise Agents](https://www.anthropic.com/events/the-briefing-enterprise-agents-virtual-event) in February, Thomson Reuters showcased CoCounsel rebuilt on the Claude Agent SDK; with today's release, that integration runs both ways. Harvey, Solve Intelligence, and others below are doing the same.

These updates build on Claude Opus 4.7, our most capable publicly available model for legal reasoning and long-document work.

Here’s what legal teams and ecosystem partners have told us about working with Claude:

![EvenUp](https://assets.claude.com/466446f5f59635a264efe3e688a42b51c0e88976.svg)

> “PI law presents some of the toughest challenges for AI: reasoning across large volumes of medical records and billing data, identifying critical facts, and executing complex workflows with consistency and accuracy. Claude Opus 4.8 delivers a new level of reasoning, reliability, and long-context performance. EvenUp adds proprietary PI data, domain expertise, and purpose-built workflows on top.”

Rami Karabibar, CEO and CoFounder

![Solve Intelligence](https://assets.claude.com/2819327500f71d308c553acac2e114468c0e86fa.svg)

> “We're seeing major improvements in Claude Opus 4.7's multimodal understanding, from reading chemical structures to interpreting complex technical diagrams. The higher resolution support is helping Solve Intelligence build best-in-class tools for life sciences patent workflows, from drafting and prosecution to infringement detection and invalidity charting.”

Sanj Ahilan, Chief Research Officer

![Eve Legal](https://assets.claude.com/f1efc487a08ab700dd2f0a0d09e717745da3e2d0.svg)

> “We evaluate every model against 24+ legal-specific scorers — citation accuracy, ungrounded case quotes, memory leakage, refusal correctness — because in litigation, an authoritative-sounding hallucination is worse than no answer. Claude wins our internal bake-offs every time on the metrics that matter for legal work, particularly grounding and citation faithfulness. That's why the highest-stakes parts of our pipeline run on Anthropic.”

Jay Madheswaran, CEO and Co-Founder

![Freshfields](https://assets.claude.com/631c9f975e09f01ae344ef9004351099cc0d918b.svg)

> “Our approach in the Freshfields Lab has always been to build on the best available technology. Claude’s capabilities have become an essential part of our proprietary AI-powered solutions. With this collaboration, we are going further: co-developing agentic workflows with Anthropic that can handle multi-step legal tasks end-to-end. For our clients, that translates into faster, more precise and more scalable legal services.””

Gerrit Beckhaus, Partner and Co-Head

![Accenture](https://assets.claude.com/eef8a51d4b99d31d65fa28d41f247f85bc363b45.svg)

> “My legal team at Accenture put Claude to work on everyday legal matters, and we have been very excited to see how productivity gains could be realized.”

Mindy Lok, Global IP Legal Lead and Legal Chief Technology Officer

![Thomson Reuters](https://assets.claude.com/3c80d8dc7dbf6556d1137977873dee26eaffae1d.svg)

> “The future of AI won’t be defined by where the work happens, it will be defined by whether the results can be trusted. In professional settings, that means AI grounded in authoritative content, validated for accuracy, and built with security at its core. That is the next frontier of trusted AI, and it’s where Thomson Reuters is leading through our work with Anthropic.””

Joel Hron, CTO

![Quinn Emanuel Urquhart & Sullivan](https://assets.claude.com/9a319a911bf5466e2baf48bd08ee6bb10df98427.png)

> “I built our litigation platform on Claude with virtually no coding background — I needed it for a real trial. The breakthrough was treating Claude like a member of the case team: onboard it with chronology, key excerpts, and themes the way you'd onboard a partner joining mid-case. The work product is far beyond what I would've done on my own — probably ever.”

Christopher D. Kercher, Partner, Founder & Head of AI & Data Analytics

![Harvey](https://assets.claude.com/9447073367b83132335cb2c191c36bef275f48e6.svg)

> “Legal is one of the most compelling industries for AI transformation, which is why we're excited to deepen our partnership with Anthropic. Claude Opus 4.7 scored 90.9% on Harvey's BigLaw Bench, the highest of any Claude model, and the Harvey for Claude Connector brings our legal intelligence directly into Claude.”

Winston Weinberg, CEO & Co-Founder

![Crosby](https://assets.claude.com/9815d36508ab5cbef0ba2782bc26371f19356894.svg)

> “Claude for Word brings the power of Claude's agents inside of lawyers' critical daily workflows. This frees up our team to focus on what matters most: lawyers applying expert judgment to complex edge cases, and engineers using rich context to build self-improving systems for clients.”

Ryan Daniels, Co-Founder & CEO

![Legora](https://assets.claude.com/666fbd8fbde356286a5ac8370b994f246c08fb10.svg)

> “Opus 4.7 is a step forward in reasoning for complex legal work — stronger consistency across long documents, better handling of nuanced instructions, and improved reliability in high-stakes workflows. Anthropic builds the underlying intelligence; Legora turns it into production-ready systems, embedding Claude into the workflows, safeguards, and interfaces lawyers can trust in practice. That combination is what drives real impact for legal professionals.”

Jake Lauritzen, CTO

![Holland & Knight](https://assets.claude.com/b8faaa7f6a90ceca02b29e39d7376ccd7dedda75.svg)

> “At Holland & Knight, we appreciate that Everlaw is working with Anthropic and offering access to their tool through an MCP. We are applying Claude’s capabilities across many litigation workflows and see significant potential in realizing them in the right context. Everlaw allows us to bring the right evidence into the equation, unlocking additional power.”

Manfred Gabriel, Partner

![EvenUp](https://assets.claude.com/466446f5f59635a264efe3e688a42b51c0e88976.svg)

> “PI law presents some of the toughest challenges for AI: reasoning across large volumes of medical records and billing data, identifying critical facts, and executing complex workflows with consistency and accuracy. Claude Opus 4.8 delivers a new level of reasoning, reliability, and long-context performance. EvenUp adds proprietary PI data, domain expertise, and purpose-built workflows on top.”

Rami Karabibar, CEO and CoFounder

![Solve Intelligence](https://assets.claude.com/2819327500f71d308c553acac2e114468c0e86fa.svg)

> “We're seeing major improvements in Claude Opus 4.7's multimodal understanding, from reading chemical structures to interpreting complex technical diagrams. The higher resolution support is helping Solve Intelligence build best-in-class tools for life sciences patent workflows, from drafting and prosecution to infringement detection and invalidity charting.”

Sanj Ahilan, Chief Research Officer

![Eve Legal](https://assets.claude.com/f1efc487a08ab700dd2f0a0d09e717745da3e2d0.svg)

> “We evaluate every model against 24+ legal-specific scorers — citation accuracy, ungrounded case quotes, memory leakage, refusal correctness — because in litigation, an authoritative-sounding hallucination is worse than no answer. Claude wins our internal bake-offs every time on the metrics that matter for legal work, particularly grounding and citation faithfulness. That's why the highest-stakes parts of our pipeline run on Anthropic.”

Jay Madheswaran, CEO and Co-Founder

![Freshfields](https://assets.claude.com/631c9f975e09f01ae344ef9004351099cc0d918b.svg)

> “Our approach in the Freshfields Lab has always been to build on the best available technology. Claude’s capabilities have become an essential part of our proprietary AI-powered solutions. With this collaboration, we are going further: co-developing agentic workflows with Anthropic that can handle multi-step legal tasks end-to-end. For our clients, that translates into faster, more precise and more scalable legal services.””

Gerrit Beckhaus, Partner and Co-Head

![Accenture](https://assets.claude.com/eef8a51d4b99d31d65fa28d41f247f85bc363b45.svg)

> “My legal team at Accenture put Claude to work on everyday legal matters, and we have been very excited to see how productivity gains could be realized.”

Mindy Lok, Global IP Legal Lead and Legal Chief Technology Officer

![Thomson Reuters](https://assets.claude.com/3c80d8dc7dbf6556d1137977873dee26eaffae1d.svg)

> “The future of AI won’t be defined by where the work happens, it will be defined by whether the results can be trusted. In professional settings, that means AI grounded in authoritative content, validated for accuracy, and built with security at its core. That is the next frontier of trusted AI, and it’s where Thomson Reuters is leading through our work with Anthropic.””

Joel Hron, CTO

1/11

## Getting started

The [new connectors](https://claude.ai/directory/connectors) and [practice-area plugins](https://github.com/anthropics/claude-for-legal) are open source and available in Claude Cowork. Enterprise admins can enable them in your workspace settings. [Learn more here](http://www.claude.com/solutions/legal) or [contact our sales team](https://claude.com/contact-sales).

Register for our [launch webinar](http://website.anthropic.com/webinars/how-legal-teams-put-claude-to-work) to see the new features in action – we'll share live product walkthroughs, and cover how law firms and in-house teams can get the most out of Claude and the connected ecosystem. Builders can also explore community-maintained skills via Legal Quants and Lawvable.

For legal aid and access-to-justice organizations who are interested in partnering, get in touch via our [Nonprofits program](https://claude.com/solutions/nonprofits).

‍

[ArticleOct 1, 2026

### Customize Claude Code with mods

Change how Claude Code behaves and looks with a few lines of TypeScript.

Claude Code](https://claude.com/resources/articles/claude-code-mods)[ArticleSep 30, 2026

### Claude for Government is now generally available

Claude Code CLI and Claude for Microsoft 365 also now available in early access.](https://claude.com/resources/articles/claude-for-government-is-now-generally-available)[ArticleSep 25, 2026

### Build plugins for Claude

You can now submit plugins to the Claude directory through a new developer portal, track them through review, and see usage analytics once they’re live.

Claude apps](https://claude.com/resources/articles/build-plugins-for-claude)[ArticleSep 24, 2026

### Claude Tag now supports personal connectors in channels

Claude Tag can now use your connectors for requests you make in a channel. Nobody else can use them, and you're in control of how to present the output.

Claude Tag](https://claude.com/resources/articles/claude-tag-now-supports-personal-connectors-in-channels)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
