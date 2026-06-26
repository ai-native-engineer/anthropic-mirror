<!-- source: https://claude.com/docs/claude-tag/admins/connections/overview -->

Each guide covers one service: how to create the credential as a dedicated identity, what to paste into the Access bundle, and the Allowed websites value. For the model behind connections (credential types, Agent Proxy, allowed websites), see [Give Claude access](/docs/claude-tag/admins/add-connections).

Always connect a dedicated account for Claude (for example, `[email protected]`), not your personal login. Anyone in a channel under the bundle’s [scope](/docs/claude-tag/admins/attach-to-scope) can use the connection through Claude, so whatever this account can reach is available to every member of those channels. See [Create a dedicated account per service](/docs/claude-tag/admins/add-connections#create-a-dedicated-account-per-service).

| Service | Category | Guide |
| --- | --- | --- |
| Datadog | Monitoring | [Connect Datadog](/docs/claude-tag/admins/connections/datadog) |
| Sentry | Monitoring | [Connect Sentry](/docs/claude-tag/admins/connections/sentry) |
| PagerDuty | Monitoring | [Connect PagerDuty](/docs/claude-tag/admins/connections/pagerduty) |
| Linear | Issue tracking | [Connect Linear](/docs/claude-tag/admins/connections/linear) |
| Asana | Issue tracking | [Connect Asana](/docs/claude-tag/admins/connections/asana) |
| Notion | Knowledge and docs | [Connect Notion](/docs/claude-tag/admins/connections/notion) |
| Google (Drive, Calendar, Gmail) | Knowledge and docs | [Connect Google](/docs/claude-tag/admins/connections/google) |
| HubSpot | Go-to-market | [Connect HubSpot](/docs/claude-tag/admins/connections/hubspot) |
| Salesforce (custom) | Go-to-market | [Connect Salesforce](/docs/claude-tag/admins/connections/salesforce) |
| Gong | Go-to-market | [Connect Gong](/docs/claude-tag/admins/connections/gong) |
| GitLab | Code | [Connect GitLab](/docs/claude-tag/admins/connections/gitlab) |
| Snowflake (custom) | Data warehouse | [Connect Snowflake](/docs/claude-tag/admins/connections/snowflake) |
| Stripe | Billing | [Connect Stripe](/docs/claude-tag/admins/connections/stripe) |
| Vercel | Deployments | [Connect Vercel](/docs/claude-tag/admins/connections/vercel) |

GitHub is configured separately through the Claude GitHub App; see [Configure GitHub access](/docs/claude-tag/admins/configure-github).
Services marked (custom) have no preset button; add them with **Connect another app** following their guide. For a service without a guide, see the credential-type table on [Connect a custom service](/docs/claude-tag/admins/connections/custom#credential-types).

[GitHub access](/docs/claude-tag/admins/configure-github)[Custom connection](/docs/claude-tag/admins/connections/custom)
