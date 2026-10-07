<!-- source: https://claude.com/resources/guides/deploying-claude-across-your-organization/how-anthropic-teams-use-cowork -->

Chapter 069 min read

# How teams at Anthropic use Claude Cowork

9 min read

11 min remaining

Four teams at Anthropic, four archetypes of knowledge work: data-heavy (finance), document-heavy (legal), relationship-heavy (sales), cross-functional (product). Each followed the same pattern: start with a specific pain point, build a plugin, iterate. Read another way, each climbed the same five levels, just against different work. Here's how employees at Anthropic use Claude Cowork, with patterns and best practices applicable to your own organizations.

## Finance and strategy

### The problem

Financial analysis at Anthropic requires deep knowledge of data warehouse schemas, complex SQL, and front-end engineering cycles the team didn't have. Dashboard builds took weeks. Alerts surfaced raw metrics with no context: "revenue down 3%" instead of "revenue down 3% driven by a dip in APAC enterprise renewals." The institutional knowledge of which tables to query and how to interpret them lived in two or three people's heads.

### The approach

The team's first step was connecting Claude Cowork to the data warehouse via MCP and asking ad-hoc questions against live data. The jump to building skills was encoding the four queries they kept re-running as skills: an insight agent for ad-hoc questions, a financial statements skill that produces standard reports, a variance analysis skill that explains deltas rather than only flagging them, and a dashboard builder that generates interactive HTML dashboards from a description of what you want to see.

The true unlock, however, came when they shipped a company-wide data skill anyone at Anthropic can install. It knows the schema, the naming conventions, and the quirks of the tables so that a PM or a sales manager can ask a question of the warehouse without knowing SQL or which of seventeen tables has the number they need.

### The impact

Development velocity moved from weeks to hours. Non-technical team members build interactive dashboards without filing a ticket. One account executive built a book-of-business dashboard, credit usage, per-account ARR, momentum indicators, drill-downs, that he uses multiple times a day. His manager now uses it to look across every rep on her team.

Alerts got useful, too. When a metric moves, Claude pulls the context and surfaces the likely driver alongside the number. The conversation moves from "what happened"? to "what do we do about it?"

## Legal

### The problem

Legal is information-dense, high-stakes, and chronically bottlenecked. Throughput work, including regulatory monitoring across jurisdictions, internal comms, and ticket triage, consumed hours better spent on judgment calls and complex legal questions. Before Claude, the team's institutional knowledge lived in memos, risk frameworks, and a policy wiki most people hadn't read in full.

### The approach

The team built the Legal plugin in an afternoon, not by coding anything, but by pointing Claude at their actual work product: the memos, the risk frameworks, the policy docs. The plugin is markdown files that tell Claude how Anthropic's legal team thinks about risk, reviews launches, and structures advice.

As Pike describes it, the project is recursive: he used Claude to build the plugin, and now uses the plugin every day to do his actual job. The plugin is [open-source on GitHub (opens in new tab)](https://claude.com/lp/cowork-for-legal) alongside the other knowledge-work plugins, because there's nothing proprietary about it. It's system instructions, not case law.

Legal is the clearest example in the company of skipping rungs of the Claude Cowork adoption ladder. Because the team's process was already written down in memos and frameworks, Pike could "here's our policy folder, draft this launch review" to a department plugin in a single afternoon.

### The impact

The Anthropic legal team saw the immediate returns when adopting Claude Cowork. Regulatory monitoring across dozens of jurisdictions went from reading everything and hoping you catch what matters to reading what Claude flagged and deciding. The team reads what's material instead of triaging the full feed.

Biweekly legal updates for the executive team used to take the better part of a day to compile. Now they take a fraction of that, because Claude does the synthesis across intake tickets, Slack threads, and matter status before anyone opens a doc.

And the team pointed Claude at 742 Jira tickets, the full legal intake backlog, and asked what the work actually looked like. The analysis reshaped how the team structures intake: which categories can be templated, which need a human from the start, and where the queue was backing up and why.

The plugin is generic out of the box and gets good when customized. The version Anthropic Legal runs internally has the team's playbooks, risk frameworks, and what they call the Legal Constitution baked in.

## Sales

### The problem

Reps spent more time documenting work than doing it. The context for any given account lives in Salesforce, email, Gong recordings, Slack, and somebody's memory, and before every call, someone has to reassemble it. Thirty minutes of prep for a call you might get fifteen minutes of useful conversation out of, multiplied across a book of hundreds of accounts.

### The approach

The sales plugin encodes how the team's best sellers work as five skills: a morning briefing that organizes the day, call prep that pulls the full account context into one brief, post-call follow-up that drafts the email and updates the opportunity, competitive intelligence that tracks what's moving in the market, and asset creation that generates custom collateral on demand.

These Claude Cowork-powered systems surface information to the rep rather than requiring the rep to go find it.

### The impact

The morning briefing organizes the day in about two minutes: today's calls, which deals need attention, what changed overnight. Call prep that took thirty minutes of manual research happens in the background while you're on the previous call.

One rep built a skill that auto-updates Salesforce opportunities after calls: Claude takes the call context, fills in every required field, and writes the description, use cases, notes, and next steps, formatted the way he wants them. He started with a validation step on every update. After enough manual checks confirmed Claude was getting it right, he removed the validation and lets it run. That progression, run it supervised, then run it scheduled, is the Level 2 to Level 3 move, and it saves hours per week.

Another Sales team hack? For ticket filing, copy a customer Slack thread into Claude Cowork, ask it to summarize, create the ticket, and post it to the finance-tickets channel after approval. Thirty seconds versus three to five minutes. A teammate used Claude Cowork to bulk-correct a field that was wrong across hundreds of Salesforce records, the kind of fix that would otherwise be a painful manual afternoon or a ticket to ops.

## Product management

### The problem

Product management work spans dozens of activities daily and most of it happens in meetings. The failure mode is things slipping through the cracks: a decision made in a meeting that nobody wrote down, a customer insight from a sales call that never made it into the PRD. Before Claude Cowork, Claude couldn't help with the core PM work, strategy, roadmaps, PRDs, because it lacked the organizational context to say anything useful.

### The approach

The biggest unlock for PMs was plugin stacking. Rather than one PM plugin, the team layers several: the productivity plugin for personal context and calendar, the data plugin for live analytics, the sales plugin for customer insights from calls and tickets, and the product plugin for PRD structure and roadmap methodology.

Individually, each plugin is useful. Stacked, Claude has org context, real usage data, actual customer quotes, and a framework for turning all of it into a PRD, at the same time, in the same session.

### The impact

PRDs get written from real data and customer context rather than generic templates. Claude pulls the usage numbers, surfaces the relevant customer feedback, and drafts against the team's PRD structure. The PM's job shifts from gathering to deciding.

The compounding effect of layering plugins is worth noting. Each plugin is useful on its own. Together they're more than the sum, because the context from one informs the others: a customer complaint from the sales plugin shapes the priority call in the product plugin, grounded in the usage data from the data plugin.
