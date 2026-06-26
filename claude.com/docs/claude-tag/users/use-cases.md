<!-- source: https://claude.com/docs/claude-tag/users/use-cases -->

Each use case below links to a page with prompts to paste, what it needs connected, and how to set it up to [run on a schedule or watch the channel](/docs/claude-tag/users/proactivity) instead of asking each time.

If `@Claude` doesn’t autocomplete in your workspace, your admin hasn’t enabled Claude Tag. Send them the [setup guide](/docs/claude-tag/admins/setup-overview).

##  All use cases

| Use case | Who it’s for | What Claude does | Connections needed |
| --- | --- | --- | --- |
| [Catch up](/docs/claude-tag/users/use-cases/catch-up) | Anyone | Summarizes a thread, a channel, or what’s waiting on you | Nothing |
| [Triage requests](/docs/claude-tag/users/use-cases/triage-requests) | Support, ops, IT, any intake channel | Answers what it can, flags duplicates, routes the rest, rolls up themes | Nothing (issue tracker optional for filing) |
| [Turn threads into docs and tickets](/docs/claude-tag/users/use-cases/create-artifacts) | Anyone | Produces a decision doc, status memo, ticket, or send-ready reply from a discussion | Nothing (Drive or issue tracker optional) |
| [Track projects and chase approvals](/docs/claude-tag/users/use-cases/track-projects) | PMs, leads, anyone running a project channel | Posts standing status digests; follows up on stalled sign-offs | Nothing (issue tracker optional) |
| [Find answers in your docs](/docs/claude-tag/users/use-cases/find-answers) | Anyone | Looks up policies, runbooks, prior decisions; replies with the source | Google Drive, Notion, or Confluence |
| [Answer data questions](/docs/claude-tag/users/use-cases/answer-data-questions) | Analysts, data-adjacent teams | Runs warehouse queries, returns charts; or charts from Slack history alone | BigQuery, Snowflake, or Redshift (charts from Slack need none) |
| [Fix bugs](/docs/claude-tag/users/use-cases/fix-bugs) | Engineering | Reproduces the bug, opens a draft PR, follows CI to green | GitHub (Datadog, Sentry optional) |
| [Watch monitors and alerts](/docs/claude-tag/users/use-cases/watch-monitors) | On-call, SRE | Checks dashboards on a schedule; investigates alerts before anyone asks | Datadog, Sentry, or PagerDuty |
| [Pull deal and account state](/docs/claude-tag/users/use-cases/pull-deal-state) | Sales, customer success | Answers account questions in-thread; pre-call briefs; weekly pipeline digest | Salesforce, HubSpot, or Gong |

##  Use cases by connection

A connection is a tool an admin linked for the channel. Each one adds a category of work; ask `@Claude what can you access from this channel?` to see which your channel has.

| Connection | Examples | What it adds |
| --- | --- | --- |
| Knowledge and docs | Google Drive, Notion, Confluence | [Find answers in your docs](/docs/claude-tag/users/use-cases/find-answers) |
| Issue tracking | Linear, Jira, Asana | [Turn threads into tickets](/docs/claude-tag/users/use-cases/create-artifacts), [track projects](/docs/claude-tag/users/use-cases/track-projects) |
| Data warehouse | BigQuery, Snowflake | [Answer data questions](/docs/claude-tag/users/use-cases/answer-data-questions) with charts |
| Go-to-market | Salesforce, HubSpot, Gong | [Pull deal and account state](/docs/claude-tag/users/use-cases/pull-deal-state) |
| Monitoring | Datadog, Sentry, PagerDuty | [Watch monitors and alerts](/docs/claude-tag/users/use-cases/watch-monitors) |
| Code | GitHub | [Fix bugs](/docs/claude-tag/users/use-cases/fix-bugs), open pull requests, follow CI |

If a connection your work needs is missing, an admin can [add it](/docs/claude-tag/admins/add-connections).

* [Prompt library](/docs/claude-tag/users/prompt-library): the prompts from every entry, plus the operational ones, on one page
* [Good habits](/docs/claude-tag/users/good-habits): make any of these reliable
* [Set up routines](/docs/claude-tag/users/proactivity): turn any entry into a scheduled job

[Prompt library](/docs/claude-tag/users/prompt-library)[Triage requests](/docs/claude-tag/users/use-cases/triage-requests)
