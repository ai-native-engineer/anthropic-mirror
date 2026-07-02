<!-- source: https://claude.com/docs/claude-tag/admins/connections/atlassian -->

Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.

Connecting Atlassian Cloud lets Claude read and search Confluence pages and read, comment on, and update Jira issues from any channel under the bundle’s scope. Jira and Confluence don’t have a preset Connect button, so you add them through **Connect another app** as a [custom connection](/docs/claude-tag/admins/connections/custom). One credential covers both products on the same Atlassian site.
This is an HTTP API connection, not an MCP server or a personal claude.ai connector. Pair it with a plugin that covers Jira and Confluence so Claude knows how to call the API; see [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins).

##  Create the credential in Atlassian

Create a dedicated Atlassian account for Claude (for example `[email protected]`) and add it to the Jira projects and Confluence spaces it should reach. The connection can read whatever this account can read, so a dedicated account keeps Claude’s reach to exactly what you grant it.
Sign in as that account and create an API token at [id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens). Atlassian shows the token once; store it somewhere you can retrieve it.

##  Add the connection to a bundle

On the bundle’s **Credentials** tab, click **Connect another app**.

| Field | Value |
| --- | --- |
| Name | A label such as “Atlassian (Jira and Confluence)“ |
| Credential type | **Basic** |
| Username | The dedicated account’s email address |
| Password | The API token from Atlassian |
| Allowed websites | `your-domain.atlassian.net` (your site’s hostname) |

Atlassian Cloud’s REST APIs authenticate with HTTP Basic, where the username is the account email and the password is the API token. An API token sent as a Bearer header is not accepted on Atlassian Cloud; pick **Basic**, not **Bearer**.
The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

Atlassian Data Center (self-hosted) uses a personal access token sent as a Bearer header instead of Basic auth. For a Data Center instance, pick **Bearer** as the credential type and add your instance’s hostname under **Allowed websites**. The instance must be reachable from the public internet.

##  Verify the connection

In a channel under the bundle’s scope, in a new thread, ask Claude to fetch one issue or page by key or URL. The call lands under the dedicated account in Atlassian’s audit log.

```
@Claude can you read PROJ-123 from Jira?
```

New connections apply to new threads only.

##  Related resources

* [Custom connection](/docs/claude-tag/admins/connections/custom): the form fields and credential types in full
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full connection model and how to scope a dedicated account

[Asana](/docs/claude-tag/admins/connections/asana)[Datadog](/docs/claude-tag/admins/connections/datadog)
