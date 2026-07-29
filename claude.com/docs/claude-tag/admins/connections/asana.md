<!-- source: https://claude.com/docs/claude-tag/admins/connections/asana -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

Connections are added inside an [Access bundle](https://claude.com/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.

Connecting Asana lets Claude file tasks and pull project status from any channel under the bundle’s scope. You add it as a connection inside an [Access bundle](https://claude.com/docs/claude-tag/admins/add-connections); the credential belongs to the agent, not to any person.
Pair this connection with the Asana plugin from Anthropic’s plugin marketplace so Claude knows how to call the API; see [Attach plugins](https://claude.com/docs/claude-tag/admins/add-connections#attach-plugins). This is an HTTP API connection, not an MCP server or a personal claude.ai connector.

##  Create the credential in Asana

On every Asana plan, create the personal access token from a dedicated Asana seat for Claude, and give that seat access to only the projects and teams Claude needs. Per Asana’s guidance, avoid service account tokens, which carry organization-wide access.
Asana’s own guide for creating the credential is at [developers.asana.com](https://developers.asana.com/docs/personal-access-token).

##  Add the connection to a bundle

In the bundle, click **Connect** next to **Asana**.

| Field | Value |
| --- | --- |
| Claude’s personal access token | The personal access token from Asana |
| Allowed websites | `app.asana.com` |

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](https://claude.com/docs/claude-tag/concepts/agent-identity#agent-proxy).

##  Verify the connection

In a channel under the bundle’s scope, in a new thread:

```
@Claude what can you access from this channel?
```

Asana appears in the list once the connection is live. New threads pick up the connection on their own; in an existing thread, ask Claude to use the service by name.

##  Related resources

* [What this connection adds](https://claude.com/docs/claude-tag/users/use-cases/track-projects): the issue tracking use cases
* [Give Claude access](https://claude.com/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
