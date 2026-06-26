<!-- source: https://claude.com/docs/claude-tag/admins/connections/sentry -->

Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.

Connecting Sentry lets Claude pull errors and stack traces into incident threads from any channel under the bundle’s scope. You add it as a connection inside an [Access bundle](/docs/claude-tag/admins/add-connections); the credential belongs to the agent, not to any person.
Pair this connection with the Sentry plugin from Anthropic’s plugin marketplace so Claude knows how to call the API; see [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins). This is an HTTP API connection, not an MCP server or a personal claude.ai connector.

##  Create the credential in Sentry

Create an internal-integration token in Sentry (Settings → Developer Settings → Internal Integrations) rather than a user auth token; scope it to the projects Claude should read.
The token starts with `sntrys_`. Prefer an internal-integration token over a user auth token so access is not tied to a person.
Sentry’s own guide for creating the credential is at [docs.sentry.io](https://docs.sentry.io/integrations/integration-platform/internal-integration/).

##  Add the connection to a bundle

In the bundle, click **Connect** next to **Sentry**.

| Field | Value |
| Claude’s auth token | The api key from Sentry |
| Allowed websites | `sentry.io` |

Self-hosted Sentry uses your own hostname instead of `sentry.io`.
The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

##  Verify the connection

In a channel under the bundle’s scope, in a new thread:

@Claude what can you access from this channel?

Sentry appears in the list once the connection is live. New connections apply to new threads only.

* [What this connection adds](/docs/claude-tag/users/use-cases/watch-monitors): the monitoring use cases
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference

[Salesforce](/docs/claude-tag/admins/connections/salesforce)[Snowflake](/docs/claude-tag/admins/connections/snowflake)
