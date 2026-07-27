<!-- source: https://claude.com/docs/claude-tag/admins/connections/custom -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

Connections are added inside an [Access bundle](https://claude.com/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.

For a service that doesn’t have a preset Connect button, use **Connect another tool** on the bundle’s Credentials tab. This works for any service with an HTTP API. The [Snowflake](https://claude.com/docs/claude-tag/admins/connections/snowflake) and [Salesforce](https://claude.com/docs/claude-tag/admins/connections/salesforce) guides are worked examples.

##  Add a custom HTTP API

###  What you need from the service

* A service-account credential (an API key, token, or OAuth client) — not your personal login
* The API host (for example `api.example.com`)
* How the API authenticates (which header or flow it expects)

See [Create a dedicated account per service](https://claude.com/docs/claude-tag/admins/add-connections#create-a-dedicated-account-per-service) for the service-account patterns.

###  Fill out the Connect another tool form

| Field | What to enter |
| --- | --- |
| **Name** | A label for this connection (for example “Internal billing API”) |
| **Credential type** | Pick the type that matches how the API authenticates; see [Credential types](#credential-types) |
| **Allowed websites** | The API’s host (for example `api.example.com`). A wildcard is allowed as the leftmost label. You can’t enter `*` alone here; a credential is always limited to specific hosts (see [Allow all hosts](https://claude.com/docs/claude-tag/admins/add-connections#allow-all-hosts)). The credential is sent only to hosts you list here. |
| **Path prefixes** (optional) | Restrict the credential to specific URL paths under the host. Shown only for the OAuth 2.0 authorization code type. |
| **Custom headers** | Any extra headers the API requires beyond the credential. Shown only for the Bearer credential type. |

###  Credential types

| Type | Use for |
| --- | --- |
| **Bearer** | An API key or token sent as `Authorization: Bearer <token>`. Most SaaS REST APIs. |
| **Basic** | HTTP Basic authentication (`Authorization: Basic <base64(user:password)>`) |
| **Body parameter** | A token the API expects in the request body or query string instead of a header |
| **AWS SigV4** | AWS services and APIs that require Signature Version 4 signing |
| **GCP access token (with Service Account Key)** | Google Cloud APIs; the proxy exchanges the SA key for an access token |
| **GCP IAP (with Service Account Key)** | Google Cloud services behind Identity-Aware Proxy |
| **OAuth 2.0 JWT bearer** | APIs that accept a JWT signed with your private key in exchange for an access token (Salesforce, DocuSign) |
| **OAuth 2.0 client credentials** | Machine-to-machine OAuth with a client ID and secret |
| **OAuth 2.0 authorization code (3-legged)** | OAuth with a user-consent step; the connection stores the resulting refresh token |
| **GitHub App** | GitHub repositories; covered separately at [Configure GitHub access](https://claude.com/docs/claude-tag/admins/configure-github) |

If you’re unsure which type, check the service’s API authentication docs for which header or flow it expects.

###  AWS SigV4

Use the **AWS SigV4** credential type for AWS service APIs (S3, Lambda, Amazon Bedrock, an API Gateway endpoint with IAM authorization). Agent Proxy reads the AWS service and signing region from the hostname and signs each outbound request with the credential at the boundary, so neither the model nor the sandbox holds the keys. The host must be an `amazonaws.com` endpoint; the proxy can’t sign requests to an API Gateway custom domain or to a non-AWS API that uses Signature Version 4.

| Field | Value |
| --- | --- |
| Access key ID | The IAM user or role access key, for example `AKIAIOSFODNN7EXAMPLE` |
| Secret access key | The matching secret access key |
| Session token | Optional. Only needed for temporary credentials from AWS STS. |
| Allowed websites | The AWS service endpoint host, for example `s3.us-east-1.amazonaws.com` or `abc123.execute-api.us-east-1.amazonaws.com` |

Use long-lived credentials from a dedicated IAM user where you can. Temporary STS credentials work but expire on their own schedule, and the connection stops working when they do; you re-enter all three values to rotate.
Claude can call the endpoint with `curl`, an AWS SDK, or the AWS CLI. The sandbox holds no real AWS credentials, so a CLI or SDK signs the request with placeholder values; Agent Proxy strips that signature and re-signs with the stored credential before the request leaves for AWS. The one shape it can’t re-sign is chunked payload signing. If Claude reports that chunked signing isn’t supported through the proxy, have it set `payload_signing_enabled = false` in `~/.aws/config` and retry.

####  When AWS returns `SignatureDoesNotMatch`

A `SignatureDoesNotMatch` response from AWS means the request AWS received doesn’t match the one Agent Proxy signed.

| Check | What to do |
| --- | --- |
| The access key ID and secret access key belong to the same IAM identity | Re-enter the access key ID, secret access key, and session token together. The form is write-only, so a partial update can leave them mismatched. |
| No proxy or gateway of your own sits between Anthropic and AWS | A second proxy that adds, strips, or reorders headers, or that re-signs the request, invalidates the signature Agent Proxy attached. Point **Allowed websites** at the AWS endpoint directly. |

A dropped or expired session token is a different failure: AWS rejects it with a token error such as `InvalidClientTokenId`, not `SignatureDoesNotMatch`. Rotate all three fields.

##  Add a custom MCP server

To give Claude an MCP server (one you run, or a vendor’s hosted MCP endpoint), the pattern is a plugin plus a credential:

1

Add a plugin that declares the MCP server

In the bundle’s **Plugins** tab (or via your [skills repository](https://claude.com/docs/claude-tag/admins/skills-repo)), add a plugin whose `.mcp.json` points at the server URL. The plugin tells Claude the server exists and how to call it.

2

Add a credential for the server's host

On the **Credentials** tab, click **Connect another tool** and add a credential for the MCP server’s host (for example, a Bearer token with **Allowed websites** set to `your-mcp-host.example.com`). This lets the call leave the sandbox with auth attached.

The plugin’s `.mcp.json` is loaded because it’s part of an attached plugin; an `.mcp.json` checked into a repository Claude clones is not loaded.

##  Verify the connection

In a channel under the bundle’s scope, in a new thread, ask Claude to make a small read against the API:

```
@Claude can you reach api.example.com? Try a GET on /health.
```

Check the service’s own audit log to confirm the call landed under your service account.

##  Related resources

* [Give Claude access](https://claude.com/docs/claude-tag/admins/add-connections): the full connection model
* [Allow a host without a credential](https://claude.com/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential): for public APIs that need no auth
* [Allow all hosts](https://claude.com/docs/claude-tag/admins/add-connections#allow-all-hosts): the egress option that lets Claude reach any public host without a credential
