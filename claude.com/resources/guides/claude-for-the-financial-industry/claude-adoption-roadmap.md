<!-- source: https://claude.com/resources/guides/claude-for-the-financial-industry/claude-adoption-roadmap -->

Chapter 048 min read

# Claude adoption roadmap

8 min read

11 min remaining

Most successful Claude rollouts follow this sequence: the team lays the foundation for a pilot program, runs a pilot, and scales out to the rest of the organization. [Anthropic's recommended adoption playbook (opens in new tab)](https://claude.com/resources/tutorials/scaling-workflows-with-claude-cowork-at-your-organization) maps out these three phases.

## Phase 1: Lay the foundation

Before launching a Claude pilot program, the responsible team needs to put all access and connectors in place. For most firms, this means standing up Claude on the first-party API, Amazon Bedrock, Google Vertex AI, or Microsoft Foundry—whichever keeps Claude inside the firm's existing cloud perimeter. Enterprise controls for SSO, SCIM, audit logs, and custom data retention need to be configured at this stage. Scope governance in parallel: model risk management, SEC/FINRA alignment, and data-privacy (GDPR/CCPA) review should run alongside access setup.

The connector set usually starts with the Microsoft 365 connector for Outlook, Teams, SharePoint, and OneDrive access, plus one or two market data research or document providers that the pilot team uses. Those could be FactSet, S&P Capital IQ, Morningstar, Moody's, Chronograph, Egnyte, etc. Firms can install these a la carte as MCP connectors, or access them inside one of [Anthropic's finance plugins (opens in new tab)](https://claude.com/resources/articles/cowork-plugins-finance) (note: they still need to be set up individually).

Next, choose the teams that will be using the pilot and let them surface use cases that matter to their function rather than prescribing from above. Choose two or three champion teams rather than one. A single team gives you one data point, while two or three teams will tell you whether, for example, the time savings and quality gains are repeatable or came from one team's motivation and skill. Pick teams with a motivated lead who's already experimenting with AI, as they are likely to surface the real use cases faster.

Pick work that's document-heavy and standard-shape. For front-office work, that might be creating the first draft of a research note, a pitch book section, or a credit memo. In back-office, that could be a KYC file review, a regulatory filing, or a claims summary. Avoid piloting Claude on novel or high-stakes work.

**Pro-tip:** Have your champions leverage pre-configured plugins so they get value in the first session. The cold-start problem is real: if someone opens Claude Cowork and doesn't know what to do, they'll close it. But if they open it, type /morning-briefing, and get something useful in ninety seconds, they return.

## Phase 2: Pilot

At this stage, champions are running real workflows with real data and measuring the pilot's success against criteria you have defined upfront. Time saved is a common metric used here, tracking the team's cycle time on the pilot job before and after Claude. Another one is how often a user keeps Claude's draft without a meaningful rewrite. Together, these two criteria help you assess whether the pilot is working.

Another strong signal that a pilot is working is when champions start to build their own skills. For example, a credit analyst takes the memo workflow she's been running by hand and turns it into a skill with the firm's template, credit policy, and approval flow embedded, and that is now a skill the rest of the org can begin using immediately.

In most pilots, Claude's product surfaces come online in a specific order. Skills and plugins come first because they're low-risk and high-reuse. The Microsoft 365 add-ins come next, extending what a pilot team has built into Excel, PowerPoint, Word, and Outlook, where the bulk of front- and back-office work actually happens. Claude Cowork tends to come in at the back end of the pilot, when the team's ready to move from single-document work to project-level work that spans files and apps.

**Pro-tip:** Schedule weekly check-ins with your pilot teams; they surface edge cases fast and you want to hear about them while they're fresh and in time to course-correct before a wider rollout.

## Phase 3: Scale

At this stage, plugins and skills that worked during the pilot are being rolled out to more teams across the organization through admin-managed plugin marketplaces. New hires benefit as well, as they start on day one with already encoded workflows. Onboarding is faster and the whole team can work more efficiently.

Over time, skills begin compounding across teams. A skill built for one team can be adapted for another when their work shares workflows or structure. For example, a fraud review workflow and an AML check workflow share most of their structure. Adding a second team usually goes faster than the first, and the firm's skill library grows.

**Pro-tip:** Provision plugins at the admin level rather than letting individuals install them ad hoc. Admin-provisioned plugins give you consistency across teams, security controls from the first user, and a single place to push updates when you improve a workflow.

The table below summarizes the actions you would take at each stage and what you can expect to see as you go through rollout.

Rollout phases with the actions to take and what to expect at each stage

| Phase | Actions | Phase |
| --- | --- | --- |
| Foundation | Security review. Identify 2–3 champion teams. Install pre-built plugins. Connect 1–2 core systems. | Champions reporting back use cases. First "this saved me an hour" moments. |
| Pilot | Champions run real workflows. Weekly check-ins. Measure against defined criteria. Demo wins to adjacent teams. | Measurable time savings. Champions building and scheduling custom skills. Pull from other teams. |
| Scale | Admin-provisioned plugin marketplace. Encode pilot learnings as org-wide skills. Onboard the next wave of users. | Skills shared across teams. New hires ramping on encoded workflows. Declining support tickets for "how do I do this." |

## Industry use cases

The work financial services teams tend to bring to Claude first is output-heavy (spreadsheets, presentations, documents), follows a standard shape, and gets reviewed by a senior person before it ships. For example, Claude takes on the drafting so reviewers can focus on the work that requires judgment. The sections below show what that looks like across four financial services sectors. They are illustrative, rather than exhaustive.

If your team is doing interesting and impactful work with Claude that we haven't mentioned here, reach out at sales@anthropic.com.

### Investment banking and private equity

Teams spend most of their time on documents that need to get built fast and are reviewed by senior bankers. Claude speeds up the drafting, saving analysts hours and reducing deal cycle times with:

* Pitch book drafting
* [Comps tables and valuations support (opens in new tab)](https://claude.com/resources/use-cases/build-financial-models)
* CIM / teaser creation
* LBO model build and analysis

### Retail and commercial banking

Teams spend the majority of their time on documents that follow standard formats. Claude can reduce turnaround times for underwriting and improve coverage ratios with:

* Branch P&L reporting
* Branch policy and procedure lookup for frontline staff
* Deal origination pitches

### Wealth and asset management

Portfolio managers and client-facing teams need to turn positions, performance, and research into material a client can read. Claude handles the document production so the PM can spend time on judgment calls and can enable higher AUM per advisor, reduced reporting time, and lower recon error rates with:

* [Portfolio reporting and investment committee memos (opens in new tab)](https://claude.com/resources/use-cases/draft-investment-memos)
* LBO model build and review
* Performance decks
* [Month-end close and reconciliation support (opens in new tab)](https://claude.com/resources/use-cases/reconcile-transactions-across-your-accounts)

### Insurance

Insurance work sits across a mix of structured data and unstructured documents, much of it in regulated filings. Claude can improve accuracy across the books, from filing accuracy to effective tax rates and recon error rates with:

* Actuarial workbook review
* Regulatory filing slides prep
* Scenario and liability modeling
