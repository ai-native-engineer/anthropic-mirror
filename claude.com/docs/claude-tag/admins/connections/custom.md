<!-- source: https://claude.com/docs/claude-tag/admins/connections/custom -->

Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.

For a service that doesn’t have a preset Connect button, use **Connect another app** at the bottom of the bundle’s Credentials tab. This works for any service with an HTTP API. The [Snowflake](/docs/claude-tag/admins/connections/snowflake) and [Salesforce](/docs/claude-tag/admins/connections/salesforce) guides are worked examples.

##  Add a custom HTTP API

###  What you need from the service

* A service-account credential (an API key, token, or OAuth client) — not your personal login
* The API host (for example `api.example.com`)
* How the API authenticates (which header or flow it expects)

See [Create a dedicated account per service](/docs/claude-tag/admins/add-connections#create-a-dedicated-account-per-service) for the service-account patterns.

###  Fill out the Connect another app form

| Field | What to enter |
| **Name** | A label for this connection (for example “Internal billing API”) |
| **Credential type** | Pick the type that matches how the API authenticates; see [Credential types](#credential-types) |
| **Allowed websites** | The API’s host (for example `api.example.com`). A wildcard is allowed as the leftmost label. The credential is sent only to hosts you list here. |
| **Path prefixes** (optional) | Restrict the credential to specific URL paths under the host. Shown only for the OAuth 2.0 authorization code type. |
| **Custom headers** | Any extra headers the API requires beyond the credential. Shown only for the Bearer credential type. |

###  Credential types

| Type | Use for |
| **Bearer** | An API key or token sent as `Authorization: Bearer <token>`. Most SaaS REST APIs. |
| **Basic** | HTTP Basic authentication (`Authorization: Basic <base64(user:password)>`) |
| **Body parameter** | A token the API expects in the request body or query string instead of a header |
| **AWS SigV4** | AWS services and APIs that require Signature Version 4 signing |
| **GCP access token (with Service Account Key)** | Google Cloud APIs; the proxy exchanges the SA key for an access token |
| **GCP IAP (with Service Account Key)** | Google Cloud services behind Identity-Aware Proxy |
| **OAuth 2.0 JWT bearer** | APIs that accept a JWT signed with your private key in exchange for an access token (Salesforce, DocuSign) |
| **OAuth 2.0 client credentials** | Machine-to-machine OAuth with a client ID and secret |
| **OAuth 2.0 authorization code (3-legged)** | OAuth with a user-consent step; the connection stores the resulting refresh token |
| **GitHub App** | GitHub repositories; covered separately at [Configure GitHub access](/docs/claude-tag/admins/configure-github) |

If you’re unsure which type, check the service’s API authentication docs for which header or flow it expects.

##  Add a custom MCP server

To give Claude an MCP server (one you run, or a vendor’s hosted MCP endpoint), the pattern is a plugin plus a credential:

1

Add a plugin that declares the MCP server

In the bundle’s **Plugins** tab (or via your [skills repository](/docs/claude-tag/admins/skills-repo)), add a plugin whose `.mcp.json` points at the server URL. The plugin tells Claude the server exists and how to call it.

2

Add a credential for the server's host

On the **Credentials** tab, click **Connect another app** and add a credential for the MCP server’s host (for example, a Bearer token with **Allowed websites** set to `your-mcp-host.example.com`). This lets the call leave the sandbox with auth attached.

The plugin’s `.mcp.json` is loaded because it’s part of an attached plugin; an `.mcp.json` checked into a repository Claude clones is not loaded.

##  Verify the connection

In a channel under the bundle’s scope, in a new thread, ask Claude to make a small read against the API:

@Claude can you reach api.example.com? Try a GET on /health.

Check the service’s own audit log to confirm the call landed under your service account.

* [Give Claude access](/docs/claude-tag/admins/add-connections): the full connection model
* [Allow a host without a credential](/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential): for public APIs that need no auth

[Connection guides](/docs/claude-tag/admins/connections/overview)[Asana](/docs/claude-tag/admins/connections/asana)
