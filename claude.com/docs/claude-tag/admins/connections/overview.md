<!-- source: https://claude.com/docs/claude-tag/admins/connections/overview -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

Each guide covers one service: how to create the credential as a dedicated identity, what to paste into the Access bundle, and the Allowed websites value. For the model behind connections (credential types, Agent Proxy, allowed websites), see [Give Claude access](https://claude.com/docs/claude-tag/admins/add-connections).

Always connect a dedicated account for Claude (for example, `claude@yourcompany.example.com`), not your personal login. Anyone in a channel under the bundle’s [scope](https://claude.com/docs/claude-tag/admins/attach-to-scope) can use the connection through Claude, so whatever this account can reach is available to every member of those channels. See [Create a dedicated account per service](https://claude.com/docs/claude-tag/admins/add-connections#create-a-dedicated-account-per-service).

| Service | Category | Guide |
| --- | --- | --- |
| Datadog | Monitoring | [Connect Datadog](https://claude.com/docs/claude-tag/admins/connections/datadog) |
| Sentry | Monitoring | [Connect Sentry](https://claude.com/docs/claude-tag/admins/connections/sentry) |
| PagerDuty | Monitoring | [Connect PagerDuty](https://claude.com/docs/claude-tag/admins/connections/pagerduty) |
| Linear | Issue tracking | [Connect Linear](https://claude.com/docs/claude-tag/admins/connections/linear) |
| Asana | Issue tracking | [Connect Asana](https://claude.com/docs/claude-tag/admins/connections/asana) |
| Jira and Confluence | Issue tracking | [Connect Jira and Confluence](https://claude.com/docs/claude-tag/admins/connections/atlassian) |
| Notion | Knowledge and docs | [Connect Notion](https://claude.com/docs/claude-tag/admins/connections/notion) |
| Google (Drive, Calendar, Gmail) | Knowledge and docs | [Connect Google](https://claude.com/docs/claude-tag/admins/connections/google) |
| HubSpot | Go-to-market | [Connect HubSpot](https://claude.com/docs/claude-tag/admins/connections/hubspot) |
| Salesforce | Go-to-market | [Connect Salesforce](https://claude.com/docs/claude-tag/admins/connections/salesforce) |
| Gong | Go-to-market | [Connect Gong](https://claude.com/docs/claude-tag/admins/connections/gong) |
| GitLab | Code | [Connect GitLab](https://claude.com/docs/claude-tag/admins/connections/gitlab) |
| BigQuery (custom) | Data warehouse | [Connect BigQuery](https://claude.com/docs/claude-tag/admins/connections/bigquery) |
| Snowflake | Data warehouse | [Connect Snowflake](https://claude.com/docs/claude-tag/admins/connections/snowflake) |
| Stripe | Billing | [Connect Stripe](https://claude.com/docs/claude-tag/admins/connections/stripe) |
| Vercel | Deployments | [Connect Vercel](https://claude.com/docs/claude-tag/admins/connections/vercel) |

GitHub is managed through the Claude GitHub App rather than a connection in this list; see [Configure GitHub access](https://claude.com/docs/claude-tag/admins/configure-github).
Services marked (custom) have no preset button. Add them with **Custom tool** following their guide.
The presets and guides cover common services, not the full set Claude can connect to. Any app with an API can be added as a custom connection or a custom MCP server. See [Connect a custom service](https://claude.com/docs/claude-tag/admins/connections/custom) for the credential types and form fields.

##  When a connection fails after setup

If Claude says it can’t reach a service you connected, start with the checks at the top of [Troubleshoot Claude Tag setup](https://claude.com/docs/claude-tag/admins/troubleshooting). Confirm the connection is in a bundle [attached to the channel’s scope](https://claude.com/docs/claude-tag/admins/attach-to-scope), and rerun the test in a new thread, since a session loads its connections when it starts.
Two entries on the troubleshooting page cover connection failures directly:

* [A connection works in one channel but not another](https://claude.com/docs/claude-tag/admins/troubleshooting#a-connection-works-in-one-channel-but-not-another): bundles attach per scope, so the failing channel’s scope is likely missing the bundle
* [I hit an authentication error and couldn’t finish this turn](https://claude.com/docs/claude-tag/admins/troubleshooting#i-hit-an-authentication-error-and-couldn%E2%80%99t-finish-this-turn): Claude posts that message when its own request fails an authentication check. A connected service’s failing credential surfaces as a tool error inside Claude’s reply instead
