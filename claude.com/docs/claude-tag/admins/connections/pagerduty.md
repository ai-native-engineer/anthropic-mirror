<!-- source: https://claude.com/docs/claude-tag/admins/connections/pagerduty -->

Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.

Connecting PagerDuty lets Claude read incidents and on-call schedules during incident work from any channel under the bundle’s scope. You add it as a connection inside an [Access bundle](/docs/claude-tag/admins/add-connections); the credential belongs to the agent, not to any person.
Pair this connection with the PagerDuty plugin from Anthropic’s plugin marketplace so Claude knows how to call the API; see [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins). This is an HTTP API connection, not an MCP server or a personal claude.ai connector.

##  Create the credential in PagerDuty

Generate a general-access read-only API key. A read-write key lets Claude acknowledge and resolve incidents; grant that only on a private incident-channel scope.
Creating a general-access key requires the PagerDuty Admin or Account Owner role; non-admins only see User Token keys, which also work but inherit that user’s permissions.
PagerDuty’s own guide for creating the credential is at [support.pagerduty.com](https://support.pagerduty.com/main/docs/api-access-keys#generate-a-general-access-rest-api-key).

##  Add the connection to a bundle

In the bundle, click **Connect** next to **PagerDuty**.

| Field | Value |
| Claude’s API key | The api key from PagerDuty |
| Allowed websites | `api.pagerduty.com` |

PagerDuty accounts on the EU service region use `api.eu.pagerduty.com` instead.
The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

##  Verify the connection

In a channel under the bundle’s scope, in a new thread:

@Claude what can you access from this channel?

PagerDuty appears in the list once the connection is live. New connections apply to new threads only.

* [What this connection adds](/docs/claude-tag/users/use-cases/watch-monitors): the monitoring use cases
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference

[Notion](/docs/claude-tag/admins/connections/notion)[Salesforce](/docs/claude-tag/admins/connections/salesforce)
