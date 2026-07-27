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
| Jira and Confluence (custom) | Issue tracking | [Connect Jira and Confluence](https://claude.com/docs/claude-tag/admins/connections/atlassian) |
| Notion | Knowledge and docs | [Connect Notion](https://claude.com/docs/claude-tag/admins/connections/notion) |
| Google (Drive, Calendar, Gmail) | Knowledge and docs | [Connect Google](https://claude.com/docs/claude-tag/admins/connections/google) |
| HubSpot | Go-to-market | [Connect HubSpot](https://claude.com/docs/claude-tag/admins/connections/hubspot) |
| Salesforce (custom) | Go-to-market | [Connect Salesforce](https://claude.com/docs/claude-tag/admins/connections/salesforce) |
| Gong | Go-to-market | [Connect Gong](https://claude.com/docs/claude-tag/admins/connections/gong) |
| GitLab | Code | [Connect GitLab](https://claude.com/docs/claude-tag/admins/connections/gitlab) |
| BigQuery (custom) | Data warehouse | [Connect BigQuery](https://claude.com/docs/claude-tag/admins/connections/bigquery) |
| Snowflake (custom) | Data warehouse | [Connect Snowflake](https://claude.com/docs/claude-tag/admins/connections/snowflake) |
| Stripe | Billing | [Connect Stripe](https://claude.com/docs/claude-tag/admins/connections/stripe) |
| Vercel | Deployments | [Connect Vercel](https://claude.com/docs/claude-tag/admins/connections/vercel) |

GitHub is managed through the Claude GitHub App rather than a connection in this list; see [Configure GitHub access](https://claude.com/docs/claude-tag/admins/configure-github).
Services marked (custom) have no preset button. Add them with **Connect another tool** following their guide.
The presets and guides cover common services, not the full set Claude can connect to. Any app with an API can be added as a custom connection or a custom MCP server. See [Connect a custom service](https://claude.com/docs/claude-tag/admins/connections/custom) for the credential types and form fields.
