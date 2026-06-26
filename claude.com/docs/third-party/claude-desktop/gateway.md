<!-- source: https://claude.com/docs/third-party/claude-desktop/gateway -->

To use a self-hosted LLM gateway (for example LiteLLM, Portkey, or an in-house proxy) as the inference provider, set `inferenceProvider` to `gateway` and supply the base URL and credentials described below.
The gateway must implement the Anthropic [Messages API](https://docs.claude.com/en/api/messages):

* `POST /v1/messages` with [streaming](https://docs.claude.com/en/api/streaming) and [tool use](https://docs.claude.com/en/docs/tool-use) is required.
* `GET /v1/models` is optional. If the gateway implements it, Claude Desktop on 3P auto-discovers available models; if not, set `inferenceModels` explicitly.

The data-residency and “no conversation data sent to Anthropic” statements elsewhere in these pages apply to a gateway deployment provided your gateway does not route inference to Anthropic-operated infrastructure (directly to the Anthropic API or via Microsoft Foundry). Data handling is otherwise determined by the gateway you operate and the upstream provider it routes to.

##  Choose an authentication approach

| Scenario | Use | Notes |
| --- | --- | --- |
| Proof of concept, or your gateway already issues per-team keys | [Static API key](#static-api-key) (`inferenceGatewayApiKey`) | A long-lived secret distributed in the managed profile. |
| Per-user attribution and identity-provider enforcement (MFA, conditional access) | [Single sign-on](#single-sign-on-with-your-identity-provider) (`inferenceGatewayOidc`) | Each user signs in with their own work account. Requires app version 1.5.0 or later. |
| Your organization already has tooling that obtains a gateway credential | [Credential helper](/docs/third-party/claude-desktop/configuration#inferencecredentialhelper) (`inferenceCredentialHelper`) | An executable that prints the gateway credential to stdout at runtime. |

##  Prepare devices

###  Static API key

No per-device preparation is required. Generate an API key in your gateway and place it in the managed configuration as `inferenceGatewayApiKey` (see [Configure the app](#configure-the-app)).

###  Single sign-on with your identity provider

Instead of distributing a shared gateway API key, you can have each user sign in with their own work account. The first time a user opens Claude Desktop, the app opens their browser to your organization’s normal sign-in page (Microsoft Entra ID, Okta, or any OpenID Connect provider). After they sign in, the app sends a per-user token to your gateway on every request, and your gateway checks that token to confirm who the user is.
This gives you per-user attribution in your gateway logs, lets your identity provider enforce MFA and conditional access, and means there is no long-lived credential to distribute or rotate.
You need three things in place:

* An LLM gateway that can validate JSON Web Tokens (LiteLLM, Kong, Envoy, and Azure API Management all support this)
* Admin access to your identity provider to register a new application
* A way to push managed configuration to user devices (your existing MDM)

The walkthrough below uses Microsoft Entra ID. An Okta variant follows.

####  Set up single sign-on

1

Register an application in Entra ID

In the [Microsoft Entra admin center](https://entra.microsoft.com), go to **Identity → Applications → App registrations** and select **New registration**. Give it a name such as `Claude Desktop gateway`, choose **Accounts in this organizational directory only**, and select **Register**.On the overview page, copy the **Application (client) ID** and **Directory (tenant) ID**. You will use both in the next two steps.Open the **Authentication** blade, select **Add a platform**, and choose **Mobile and desktop applications**. Under **Custom redirect URIs**, add exactly:

http://127.0.0.1/callback

A few details that matter here: use `127.0.0.1` (not `localhost`), include the `/callback` path, and add it under the **Mobile and desktop applications** platform specifically. That platform is the only one Entra allows to use any local port, which the app needs because it picks a free port at sign-in time. You do not need a client secret or any additional API permissions.

2

Configure your gateway to validate the token

Tell your gateway to accept the bearer token only if it was issued by your tenant **for this application**. In LiteLLM that looks like:

general_settings:
  litellm_jwtauth:
    public_key_url: https://login.microsoftonline.com/YOUR_TENANT_ID/discovery/v2.0/keys
    audience: YOUR_CLIENT_ID
    user_id_jwt_field: oid

Replace `YOUR_TENANT_ID` and `YOUR_CLIENT_ID` with the values from step 1.

The `audience` line is required. Without it, your gateway accepts tokens issued to any application in your tenant, not just this one.

For Kong, Envoy, or Azure API Management, configure the equivalent JWT validation policy with the same JWKS URL and audience.

3

Configure in the app

Open the in-app configuration window (**Developer → Configure third-party inference**). In the **Connection** section, set **Inference provider** to **Gateway** and **Credential kind** to **Interactive sign-in**. This hides the API-key field and reveals **Gateway SSO IdP (OIDC)**:

| Field | Value |
| Gateway base URL | `https://llm-gateway.example.corp` |
| Credential kind | **Interactive sign-in** |
| Gateway SSO IdP (OIDC) → Client ID | `YOUR_CLIENT_ID` |
| Gateway SSO IdP (OIDC) → Issuer URL | `https://login.microsoftonline.com/YOUR_TENANT_ID/v2.0` |
| Gateway SSO IdP (OIDC) → Scopes | *leave empty for the default* |
| Gateway SSO IdP (OIDC) → Redirect port | *leave empty* |

Then click **Export** to produce a `.mobileconfig` (macOS) or `.reg` (Windows) file for your MDM. See [Installation and setup](/docs/third-party/claude-desktop/installation) for the export and deployment workflow.When a user next opens Claude Desktop, they see a **Sign in to your organization** button. Clicking it opens their browser to your Entra sign-in page; once they approve, they return to the app and can start working. The app keeps them signed in and refreshes the token in the background, so they will not see the browser again unless their session is revoked or expires under your tenant’s policy.

####  Using Okta instead

In the Okta Admin Console, create a **Native** application with the **Authorization Code** and **Refresh Token** grant types. Okta requires the redirect URI to match exactly, including the port, so pick a fixed port (for example `53180`), register `http://127.0.0.1:53180/callback`, and set that same port in **Gateway SSO IdP (OIDC)**:

| Field | Value |
| Client ID | `YOUR_CLIENT_ID` |
| Issuer URL | `https://YOUR_ORG.okta.com` |
| Scopes | *leave empty for the default* |
| Redirect port | `53180` |

Use the **issuer** value, not the **Metadata URI**. Okta’s admin console shows the metadata URI (ending in `/.well-known/openid-configuration`) prominently — that is the discovery document the app fetches *from* the issuer, not the issuer itself. If you are unsure, open the metadata URI in a browser and copy the `"issuer"` field from the JSON response. For a custom Okta authorization server the issuer is `https://YOUR_ORG.okta.com/oauth2/AUTH_SERVER_ID`.

Point your gateway’s JWT validation at `https://YOUR_ORG.okta.com/oauth2/v1/keys` with `audience` set to the Okta client ID.

####  Map users at the gateway

Claude Desktop forwards the identity provider’s token to your gateway verbatim — it does not add, remove, or rewrite any claims. With the default scopes (`openid profile email offline_access`), the ID token your gateway receives contains the standard OIDC `sub`, `email`, and `name` claims, plus whatever your provider includes for the `profile` scope. You can confirm exactly what is present by base64-decoding the middle segment of the `Authorization: Bearer` value your gateway receives.
Key the gateway’s user record on the provider’s immutable user ID rather than email, so the record survives email or name changes:

| Provider | Stable user-ID claim |
| Entra ID | `oid` |
| Okta and most other OIDC providers | `sub` |

If your gateway has no existing user records to preserve, the simplest setup is to auto-provision on first sign-in. For LiteLLM, extend the validation block from step 2:

general_settings:
  enable_jwt_auth: true
  litellm_jwtauth:
    public_key_url: https://YOUR_ORG.okta.com/oauth2/v1/keys
    audience: YOUR_CLIENT_ID
    user_id_jwt_field: sub          # use "oid" for Entra ID
    user_email_jwt_field: email
    user_id_upsert: true

If you need additional claims (for example, a `groups` claim for team-level budgets), add them on your identity provider’s authorization server — they pass through to the gateway unchanged. To request a non-default scope, set `scopes` in `inferenceGatewayOidc` (see [Single sign-on configuration keys](#single-sign-on-configuration-keys)).

####  Refresh tokens and session lifetime

Silent token refresh requires a refresh token from your identity provider, which in turn requires the `offline_access` scope on the authorization request. Whether Claude Desktop sends that scope depends on how you set `scopes` and `bearerTokenType`:

* **`scopes` left unset** — the default (`openid profile email offline_access`) includes `offline_access`, so a refresh token is issued.
* **`bearerTokenType: "access_token"`** — Claude Desktop automatically appends `offline_access` to whatever `scopes` value you supply, unless `appendOfflineAccess` is set to `false`.
* **`bearerTokenType: "id_token"` (the default) with `scopes` set explicitly** — Claude Desktop does **not** add `offline_access` for you. Include it in your `scopes` value if you want silent refresh; without it, users are prompted to sign in again each time the ID token expires (commonly about one hour).

Per [OpenID Connect Core 1.0 §11](https://openid.net/specs/openid-connect-core-1_0.html#OfflineAccess), requesting `offline_access` signals that the client may use the refresh token while the user is not present, and the provider must obtain consent for it. Claude Desktop therefore does not add this scope to an administrator-supplied `scopes` value in the default mode, so that requesting offline access remains an explicit choice.
**Authorization servers that reject `offline_access`.** Standard OIDC providers (Entra ID, Okta, Auth0) accept `offline_access` and require it to issue a refresh token, so the automatic append is what you want. If your authorization server instead rejects unrecognized scopes with an `invalid_scope` error — for example, servers that issue refresh tokens via a provider-specific scope rather than `offline_access` — set `appendOfflineAccess` to `false` and include your provider’s own refresh-token scope in `scopes` directly.

##  Configure the app

Open the in-app configuration window (**Developer → Configure third-party inference**). In the **Connection** section, set **Inference provider** to **Gateway**, then fill in the **Gateway credentials** card:

| Field | Value |
| Gateway base URL | `https://llm-gateway.example.corp` |
| Gateway API key | your gateway key (or a placeholder if your gateway has none) |
| Credential kind | **Static API key** (default), or **Interactive sign-in** for [single sign-on](#single-sign-on-with-your-identity-provider) |
| Gateway auth scheme | **Bearer** (default) or **x-api-key** |

Then click **Export** to produce a `.mobileconfig` (macOS) or `.reg` (Windows) file for your MDM. See [Installation and setup](/docs/third-party/claude-desktop/installation) for the export and deployment workflow.

###  Configuration keys

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `inferenceGatewayBaseUrl` | `string` | MDM + Bootstrap | — | Full URL of the inference gateway endpoint. |
| `inferenceGatewayApiKey` | `string` | MDM + Bootstrap | — |  |
| `inferenceGatewayAuthScheme` | `enum` | MDM + Bootstrap | `bearer` | How the gateway credential is sent on the wire (Authorization: Bearer vs x-api-key header). One of: `bearer`, `x-api-key`. Defaults to `bearer`. |
| `inferenceGatewayOidc` | `object` | MDM + Bootstrap | — | External IdP for gateway sign-in. The user authenticates against this issuer; the resulting token (ID token by default) is sent to the gateway as the Bearer credential. Leave unset only if the gateway is its own OAuth authorization server. |

To send additional HTTP headers on every inference request (tenant routing, org IDs, and similar), set [`inferenceCustomHeaders`](/docs/third-party/claude-desktop/configuration#inferencecustomheaders). It applies to all providers, not just gateways.

###  Single sign-on configuration keys

Single sign-on is enabled by setting `inferenceCredentialKind` to `interactive` **and** supplying `inferenceGatewayOidc`. Both are required — `interactive` alone (without `inferenceGatewayOidc`) selects a different mode where the gateway itself acts as the authorization server.

| Setting | MDM key | Required | Description |
| --- | --- | --- | --- |
| Credential kind | `inferenceCredentialKind` | Yes — must be `interactive` | Selects sign-in instead of an API key. |
| Gateway SSO IdP (OIDC) | `inferenceGatewayOidc` | Yes | A **single JSON object** describing the identity provider (fields below). The resulting token is sent to the gateway as the bearer credential. |

The `inferenceGatewayOidc` value is one JSON object with these fields:

| Field | Required | Description |
| --- | --- | --- |
| `clientId` | Yes | Application (client) ID registered with the identity provider. |
| `issuer` | Yes\* | OIDC issuer URL — the base URL only, **without** `/.well-known/openid-configuration`. The app appends that path itself to discover the authorization and token endpoints. |
| `authorizationUrl` | No\* | Explicit OIDC authorization endpoint. Use together with `tokenUrl` instead of `issuer` when the identity provider does not serve `/.well-known/openid-configuration`. Ignored when `issuer` is set. |
| `tokenUrl` | No\* | Explicit OIDC token endpoint. Must be set together with `authorizationUrl`. Ignored when `issuer` is set. |
| `scopes` | No | Space-separated OIDC scopes. Defaults to `openid profile email offline_access`. Required when `bearerTokenType` is `access_token`. See [Refresh tokens and session lifetime](#refresh-tokens-and-session-lifetime) for how this field interacts with silent refresh. |
| `redirectPort` | No | Fixed local port for the loopback redirect. Leave unset to let the app choose an ephemeral port (Entra). Set when the provider requires an exact port match (Okta). |
| `bearerTokenType` | No | Which token the app sends to the gateway as the `Authorization: Bearer` value. `id_token` (the default) sends the OIDC ID token — the gateway validates it offline against the provider’s JWKS with `aud` equal to the client ID. `access_token` sends the OAuth access token instead — use this for gateways that validate as an OAuth resource server rather than validating the ID token directly. When set to `access_token`, `scopes` is required. |
| `appendOfflineAccess` | No | Whether to automatically append `offline_access` to `scopes` in `access_token` mode. Defaults to `true`. Set to `false` only if your authorization server rejects `offline_access` as an unrecognized scope. See [Refresh tokens and session lifetime](#refresh-tokens-and-session-lifetime). |

\* Either `issuer`, or both `authorizationUrl` and `tokenUrl`, is required.

`inferenceGatewayOidc` is **one MDM key whose value is a JSON string** — not separate keys like `inferenceGatewayOidc.clientId`. See [how object-typed keys are encoded](/docs/third-party/claude-desktop/configuration#value-types). The in-app **Export** produces the correct format automatically.

In a macOS `.mobileconfig` payload (Okta example):

<key>inferenceCredentialKind</key>
<string>interactive</string>
<key>inferenceGatewayOidc</key>
<string>{"issuer":"https://YOUR_ORG.okta.com","clientId":"YOUR_CLIENT_ID","redirectPort":53180}</string>

Earlier app versions used `inferenceGatewayAuthScheme: "sso"` to select this mode. That value is deprecated; set `inferenceCredentialKind: "interactive"` instead. Existing deployments that still send `inferenceGatewayAuthScheme: "sso"` continue to work.

###  Models

When `inferenceModels` is unset, Claude Desktop on 3P populates the model picker from your gateway’s `GET /v1/models` response. Auto-discovery shows only models whose IDs are recognizably Claude; if your gateway advertises models under opaque aliases, set `inferenceModels` explicitly. Set [`inferenceModels`](/docs/third-party/claude-desktop/configuration#inferencemodels) to override discovery with an explicit list — the picker will show exactly the entries you provide. Use the model IDs your gateway expects (for example `bedrock/us.anthropic.claude-opus-4-7` for a LiteLLM-style routing prefix).

###  MCP tool search

[MCP tool search](https://code.claude.com/docs/en/mcp#scale-with-mcp-tool-search) is disabled by default when routing through a gateway, because most proxies do not forward `tool_reference` content blocks. If your gateway passes them through unchanged — LiteLLM in passthrough mode and Cloudflare AI Gateway both do — set the environment variable `ENABLE_TOOL_SEARCH=true` to re-enable it.

##  Troubleshoot

**`gateway SSO: server does not advertise device_authorization_endpoint`** — The app could not read your `inferenceGatewayOidc` value, so it fell back to treating the gateway itself as the sign-in server. Almost always this means the value is not a valid JSON string (for example, separate dotted keys, or a plist `<dict>` instead of a `<string>`). Re-export from the in-app configuration window, or copy the `.mobileconfig` snippet above.
**`OIDC discovery failed (HTTP 404)` or `(HTTP 405)`** — The `issuer` value is not the issuer base URL. Most often the metadata URI (ending in `/.well-known/openid-configuration`) was pasted instead, which doubles the path. Remove that suffix so `issuer` is just `https://YOUR_ORG.okta.com` (or the equivalent for your provider).
**`no credential configured for provider "gateway": set inferenceCredentialKind or one of the credential fields`** — `inferenceCredentialKind: "interactive"` is not present in the pushed configuration.
**Browser shows “Connected” but the app reports the sign-in failed, or `Token exchange failed (HTTP 401)`** — The browser step succeeded, but the identity provider rejected the follow-up token request. This usually means the IdP application is registered as a confidential (Web) client, which expects a client secret. Claude is a public PKCE client and doesn’t send one. Register a public/native client instead: **Native Application** in Okta, or the **Mobile and desktop applications** platform in Entra ID. Application type generally can’t be changed after creation, so you may need to create a new one.

Google Workspace can be used as the identity provider, but in the default `id_token` mode Google does not issue a fresh ID token on background refresh, so users are prompted to sign in again roughly once an hour. Setting `bearerTokenType` to `access_token` avoids this. Entra ID and Okta are not affected in either mode.

[Write a credential helper](/docs/third-party/claude-desktop/credential-helper)[Bedrock](/docs/third-party/claude-desktop/bedrock)
