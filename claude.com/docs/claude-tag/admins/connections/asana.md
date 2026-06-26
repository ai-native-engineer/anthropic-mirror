<!-- source: https://claude.com/docs/claude-tag/admins/connections/asana -->

Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.

Connecting Asana lets Claude file tasks and pull project status from any channel under the bundle’s scope. You add it as a connection inside an [Access bundle](/docs/claude-tag/admins/add-connections); the credential belongs to the agent, not to any person.
Pair this connection with the Asana plugin from Anthropic’s plugin marketplace so Claude knows how to call the API; see [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins). This is an HTTP API connection, not an MCP server or a personal claude.ai connector.

##  Create the credential in Asana

Asana’s service accounts are an Enterprise feature; on other plans, create the personal access token from a dedicated Asana seat for Claude.
Asana’s own guide for creating the credential is at [developers.asana.com](https://developers.asana.com/docs/personal-access-token).

##  Add the connection to a bundle

In the bundle, click **Connect** next to **Asana**.

| Field | Value |
| Claude’s personal access token | The personal access token from Asana |
| Allowed websites | `app.asana.com` |

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

##  Verify the connection

In a channel under the bundle’s scope, in a new thread:

@Claude what can you access from this channel?

Asana appears in the list once the connection is live. New connections apply to new threads only.

* [What this connection adds](/docs/claude-tag/users/use-cases/track-projects): the issue tracking use cases
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference

[Custom connection](/docs/claude-tag/admins/connections/custom)[Datadog](/docs/claude-tag/admins/connections/datadog)
