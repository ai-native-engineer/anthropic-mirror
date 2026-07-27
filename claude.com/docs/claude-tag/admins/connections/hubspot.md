<!-- source: https://claude.com/docs/claude-tag/admins/connections/hubspot -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

Connections are added inside an [Access bundle](https://claude.com/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.

Connecting HubSpot lets Claude pull pipeline, deal, and contact state from any channel under the bundle’s scope. You add it as a connection inside an [Access bundle](https://claude.com/docs/claude-tag/admins/add-connections); the credential belongs to the agent, not to any person.
Pair this connection with the HubSpot plugin from Anthropic’s plugin marketplace so Claude knows how to call the API; see [Attach plugins](https://claude.com/docs/claude-tag/admins/add-connections#attach-plugins). This is an HTTP API connection, not an MCP server or a personal claude.ai connector.

##  Create the credential in HubSpot

Create a private app and select the read scopes you need (typically `crm.objects.contacts.read`, `crm.objects.companies.read`, `crm.objects.deals.read`). The private app acts as its own identity in HubSpot’s audit log.
HubSpot’s own guide for creating the credential is at [developers.hubspot.com](https://developers.hubspot.com/docs/apps/legacy-apps/private-apps/overview).

##  Add the connection to a bundle

In the bundle, click **Connect** next to **HubSpot**.

| Field | Value |
| --- | --- |
| Claude’s private app token | The private app token from HubSpot |
| Allowed websites | `api.hubapi.com` (preset). To add a different host, use the **Advanced** tab. |

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](https://claude.com/docs/claude-tag/concepts/agent-identity#agent-proxy).

##  Verify the connection

In a channel under the bundle’s scope, in a new thread:

```
@Claude what can you access from this channel?
```

HubSpot appears in the list once the connection is live. New threads pick up the connection on their own; in an existing thread, ask Claude to use the service by name.

##  Related resources

* [What this connection adds](https://claude.com/docs/claude-tag/users/use-cases/pull-deal-state): the go-to-market use cases
* [Give Claude access](https://claude.com/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
