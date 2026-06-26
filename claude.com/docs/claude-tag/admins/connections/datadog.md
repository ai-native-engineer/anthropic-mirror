<!-- source: https://claude.com/docs/claude-tag/admins/connections/datadog -->

Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.

Connecting Datadog lets Claude query metrics, logs, and monitors during debugging from any channel under the bundle’s scope. You add it as a connection inside an [Access bundle](/docs/claude-tag/admins/add-connections); the credential belongs to the agent, not to any person.
Pair this connection with the Datadog plugin from Anthropic’s plugin marketplace so Claude knows how to call the API; see [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins). This is an HTTP API connection, not an MCP server or a personal claude.ai connector.

##  Create the credential in Datadog

Create both an API key and an Application key under a service account in Datadog. The Application key carries the read scopes; restrict it to read-only roles.
Datadog’s own guide for creating the credential is at [docs.datadoghq.com](https://docs.datadoghq.com/account_management/api-app-keys/).

##  Add the connection to a bundle

In the bundle, click **Connect** next to Datadog. The picker has two Datadog entries: **Datadog** for accounts on `api.datadoghq.com` (US1, the default site) and **Datadog (US5)** for accounts on `api.us5.datadoghq.com`. Pick the one that matches your Datadog site.

| Field | Value |
| Claude’s API key | The api key from Datadog |
| Claude’s application key | The application key from Datadog |
| Allowed websites | Prefilled by the preset; override for other sites (see below) |

Datadog has a separate API host per site, and a key only works against its own. If your account is on a site other than US1 or US5, override Allowed websites with your site’s API host: `api.us3.datadoghq.com`, `api.datadoghq.eu`, `api.ap1.datadoghq.com`, or `api.ddog-gov.com`. To change the host later, open the **⋮** menu on this connection in the bundle’s Credentials tab and choose **Edit**.
The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

##  Verify the connection

In a channel under the bundle’s scope, in a new thread:

@Claude what can you access from this channel?

Datadog appears in the list once the connection is live. New connections apply to new threads only.

* [What this connection adds](/docs/claude-tag/users/use-cases/watch-monitors): the monitoring use cases
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference

[Asana](/docs/claude-tag/admins/connections/asana)[GitLab](/docs/claude-tag/admins/connections/gitlab)
