<!-- source: https://academy.claude.com/use-cases/surface-themes-from-all-your-feedback-channels -->

Loading

## 1. Describe the task

In Cowork, Claude connects to multiple feedback sources at once (call transcripts in a folder, Slack, your CRM, Linear) and pulls from all of them in parallel to spot patterns across platforms.

Tell Claude what you're looking for: theme frequency, cross-platform patterns, representative quotes. It structures the feedback analysis around your priorities.

I need to understand what customers are really asking for by synthesizing feedback from multiple sources.

Sources:

* Call transcripts: Scattered across my downloads folder
* Slack in channels like #customer-feedback and #support-questions
* Salesforce: Opportunity notes and lost deal reasons
* Linear: Open feature requests and bug reports

Find the main themes and patterns across all sources — what keeps coming up? Give me counts by source, cross-platform patterns, and representative quotes. Then prioritize into product ideas based on frequency and business impact.



Open in Cowork

## 2. Give Claude context

[Cowork(opens in new tab)](https://academy.claude.com/tutorials/choosing-between-claude-cowork-or-chat) is a workspace in Claude, available in the [Claude Desktop(opens in new tab)](https://claude.com/download) app and — with remote sessions (in beta) — on web and mobile. It connects to your tools via [connectors(opens in new tab)](https://claude.com/connectors) and, run locally, also works with your local files. Give it access to your call transcripts and connect your other feedback sources. Cowork pulls from all of them in parallel.

**What to expect:** After your initial prompt in Cowork, Claude may ask you questions about what themes matter most or how to prioritize, then build a plan you can review in the sidebar. This helps it work more independently and surface more useful patterns.

### Required context

To get started:

* Download [Claude Desktop(opens in new tab)](https://claude.com/download) and start a Cowork session
* Select ***Work in a folder*** in the chat bar to give Cowork access to your call transcripts
* Add [connectors(opens in new tab)](https://claude.com/connectors) for Slack, CRM, and Linear

## 3. What Claude creates

Claude synthesizes feedback from all connected sources, identifies themes with counts and attribution, highlights patterns that appear across multiple platforms, and suggests prioritized product ideas.

I analyzed feedback from all four sources. Here's what emerged:

#### Top Themes by Frequency

1. **Mobile app issues (57 total)** — Calls: 11 | Slack: 31 | CRM: 1 | Linear: 14
2. **Reporting limitations (45 total)** — Calls: 15 | Slack: 23 | CRM: 2 | Linear: 5
3. **Salesforce integration (41 total)** — Calls: 18 | Slack: 12 | CRM: 8 | Linear: 3

#### Cross-Platform Patterns

**Mobile app (High Signal):** Appears in ALL four sources — this is genuine pain, not just vocal users.

**SSO integration (Revenue Signal):** Low volume overall but appears heavily in CRM lost deal notes. This is a deal-blocker, not a usage issue.

#### Prioritized Product Ideas

* Priority 1: Mobile app stability
* Priority 2: Okta SSO integration
* Priority 3: Report customization

## 4. Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Pull everything on one theme

Go deep on what matters most. Get every mention across all sources with full context — who said it, when, and what they were trying to do.

*"Pull every mention of mobile app issues across all four sources. For each one, give me the full context — who said it, when, what they were trying to accomplish, and how frustrated they seemed."*



Open in Cowork

### Build a roadmap proposal

Turn insights into a document for stakeholders. Cowork writes directly to your folder. Have it create a roadmap doc with evidence from the synthesis, ready to share with leadership.

*"Based on this analysis, draft a one-page roadmap proposal for Q1. Prioritize by cross-platform signal strength and business impact. Include the key quotes that support each recommendation."*



Open in Cowork

### Track what specific customers said

Follow up with customers who raised issues. See everything a specific customer mentioned across sources to prepare for a conversation.

*"What did Acme Corp say across all these sources? Pull everything they mentioned in calls, Slack, and CRM notes so I can follow up with them directly."*



Open in Cowork

## 5. Tricks, tips, and troubleshooting

### Try asking Claude to spin up subagents for parallel pulls

When pulling from multiple sources, you can ask Claude to spin up subagents to query Slack, Linear, and Salesforce simultaneously.

### Watch the progress panel and steer as Claude works

Cowork shows which sources Claude is querying and what it's finding in real time. If one platform is returning less than expected, you can adjust mid-process.

### Claude works with the files in your local folder

When you run Cowork locally, Claude reads your call transcripts and exports right where they live — in the folder you've shared — rather than you uploading them somewhere first. It can only see the folders and sources you give it access to.

## 6. Ready to try for yourself?

Use Cowork to connect your feedback sources and discover patterns you'd miss analyzing each one separately.

I need to understand what customers are really asking for by synthesizing feedback from multiple sources.

Sources:

• Call transcripts: Scattered across my downloads folder
• Slack in channels like #customer-feedback and #support-questions
• Salesforce: Opportunity notes and lost deal reasons
• Linear: Open feature requests and bug reports

Find the main themes and patterns across all sources — what keeps coming up? Give me counts by source, cross-platform patterns, and representative quotes. Then prioritize into product ideas based on frequency and business impact.

Try in Cowork
