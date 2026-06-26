<!-- source: https://claude.com/docs/claude-tag/admins/connections/snowflake -->

Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.

Connecting Snowflake lets Claude run queries against your warehouse from any channel under the bundle’s scope. Add it as a custom credential with **Connect another app**; Snowflake has no preset button in the picker.
This is an HTTP API connection, not a personal claude.ai connector.

##  Create the credential in Snowflake

Create a dedicated Snowflake user for the agent with a read-only role scoped to the databases and schemas Claude should query. Generate a programmatic access token for that user.
Snowflake’s guide for the SQL REST API and authentication is at [docs.snowflake.com](https://docs.snowflake.com/en/developer-guide/sql-api/authenticating).

##  Add the connection to a bundle

In the bundle, click **Connect another app** at the bottom and choose **Bearer**. Bearer is the only supported credential type for Snowflake; key-pair authentication is not currently supported.

| Field | Value |
| Credential type | **Bearer** |
| Custom headers | Add a row with **Name** `Authorization`, **Prefix** `Bearer` , and **Value** set to the programmatic access token from Snowflake |
| Allowed websites | `<your-account>.snowflakecomputing.com` |

Replace `<your-account>` with your Snowflake account identifier. To change the host later, open the **⋮** menu on this connection in the bundle’s Credentials tab and choose **Edit**.
The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

##  Verify the connection

In a channel under the bundle’s scope, in a new thread:

@Claude what can you access from this channel?

Snowflake appears in the list once the connection is live. New connections apply to new threads only.

* [What this connection adds](/docs/claude-tag/users/use-cases/answer-data-questions): warehouse questions answered with charts in the thread
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference

[Sentry](/docs/claude-tag/admins/connections/sentry)[Stripe](/docs/claude-tag/admins/connections/stripe)
