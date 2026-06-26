<!-- source: https://claude.com/docs/third-party/claude-desktop/bootstrap -->

Requires Claude Desktop **1.10270.0** or later. Earlier builds ignore the `bootstrapUrl` keys.

A static MDM profile is the same for every device. When configuration must vary by user (a per-user gateway credential, a per-team model allowlist, per-user OpenTelemetry attribution), host a **bootstrap server**: an HTTPS endpoint that authenticates the user against your identity provider and returns that user’s configuration as JSON.
When a bootstrap response is available, it **is** the effective configuration. The MDM profile supplies only the trust anchor (`bootstrapUrl`, optional `bootstrapOidc`, and the `bootstrapEnabled` opt-out), and Claude Desktop does not consult MDM for any key the bootstrap server is permitted to set. A bootstrap-settable key that your response **omits** is treated as unset, not inherited from MDM, so return every key you want applied.

Your bootstrap server is fully trusted. Its response can set inference credentials, the egress allowlist, MCP servers, and every other key in the [published schema](#response-schema). Treat compromise of this endpoint as credential compromise: restrict who can deploy it, log every response, and harden it as you would any secrets-issuing service.

The trust anchor itself can arrive via MDM **or** via the in-app configuration window. If your organization does not use MDM, distribute a small JSON file containing only `bootstrapUrl` and `bootstrapOidc` and have users load it from **Developer → Configure third-party inference → Import configuration**; the bootstrap server supplies everything else after sign-in. See [Installation](/docs/third-party/claude-desktop/installation) for both paths.

##  How it works

1. Your managed configuration (MDM or imported) sets `bootstrapUrl` (and `bootstrapOidc` if you use a separate identity provider).
2. At launch, the app authenticates the user via one of [two modes](#authentication) and sends `GET <bootstrapUrl>` with `Authorization: Bearer <token>`.
3. Your server validates the token, **authorizes** the caller against your directory or entitlement source, and returns a JSON object whose keys are the same managed-configuration key names documented in the [configuration reference](/docs/third-party/claude-desktop/configuration).
4. The app validates each key against the [response schema](#response-schema), drops anything it doesn’t recognize or that fails validation, and applies the result as the effective configuration.
5. The response is cached in memory (until your `expiresAt`, or 1 hour by default). The app also re-polls in the background every 30 minutes with a conditional request, so an unchanged configuration costs your server a `304` (see [Caching and `expiresAt`](#caching-and-expiresat)).

If the user has not yet signed in, or the fetch fails with no cached response from this session, the app starts in a degraded state with no inference provider configured and prompts the user to sign in.

###  Availability

The cached response is held **in memory only**. If your bootstrap server is unreachable when Claude Desktop launches, the user is in the degraded sign-in state until the server recovers; there is no on-disk fallback to a previous session’s response. Run the endpoint across multiple replicas or regions behind a load balancer; do not rely on response caching for availability, since responses are per-user and carry credentials (see the `Cache-Control: no-store` guidance under [Server responsibilities](#server-responsibilities)). If your configuration data lives in a database, a read replica of that store improves availability without caching responses. A failed refetch *during* a running session keeps the in-memory response and retries, so an outage that starts mid-session does not disrupt active users until they relaunch.
A refetch that returns different values does **not** change the running session. The app keeps the configuration it launched with — inference credentials, egress allowlist, MCP servers, and renderer state such as the model picker all stay on the boot-time values — and applies the new response at the next app launch. Plan changes accordingly: when rotating an inference credential, keep the previous credential valid until your fleet has relaunched rather than expecting propagation within a refetch interval.

##  Server responsibilities

Your bootstrap endpoint is a security boundary. The response can carry inference credentials, so an unauthenticated or under-authorized endpoint leaks those credentials to anyone who can reach the URL. Host it on your private network (VPC, corporate intranet, or behind your zero-trust access proxy) rather than the public internet; reachability from managed devices is sufficient.
**Authenticate.** Verify the bearer token’s signature against your identity provider’s JWKS, and check `iss`, `aud`, and `exp`. Reject anything else with `401`.
**Authorize.** Verifying the token proves *who* the caller is, not that they’re entitled to a configuration. Check the caller’s identity claim against your directory before returning a response:

| Identity provider | Stable per-user claim | Group/role claim |
| --- | --- | --- |
| Microsoft Entra ID | `oid` (directory object ID) | `roles` (app roles) or `groups` |
| Okta | `uid` or `sub` | `groups` (via a custom claim rule) |
| Generic OIDC | `sub` | provider-specific |

Return `403` when the token is valid but the caller is not entitled. Do not authorize on `email` or `preferred_username` alone; those claims are mutable and may be absent for guest or external-identity users.
**Key the response on the caller** when configuration needs to differ. A single default profile returned to every entitled user is valid; vary by user or group only where you need per-user credentials, model allowlists, or telemetry attribution.

###  Mapping groups to profiles

The common pattern is one profile per directory group or app role. For Entra, define an app role on the registration (for example `cowork-power-user`), assign it to a group via **Enterprise applications → Users and groups**, and select the profile from the token’s `roles` claim. For Okta, the equivalent is a `groups` claim on your custom authorization server; match on `payload.groups`. Moving a user between groups in your directory is picked up at the next refetch with no profile re-push to devices; the new configuration takes effect when the user’s app next launches.
A reference Node.js handler showing token validation, role-based authorization, and profile selection:

import { createRemoteJWKSet, jwtVerify } from "jose";

const TENANT = process.env.ENTRA_TENANT;
const CLIENT_ID = process.env.CLIENT_ID;
const JWKS = createRemoteJWKSet(
  new URL(`https://login.microsoftonline.com/${TENANT}/discovery/v2.0/keys`),
);

const BASE = {
  inferenceProvider: "gateway",
  inferenceGatewayBaseUrl: "https://YOUR_GATEWAY_HOST",
  inferenceGatewayAuthScheme: "bearer",
};
const PROFILES = {
  default: { ...BASE, inferenceModels: ["claude-sonnet-4-6"] },
  power: {
    ...BASE,
    inferenceModels: ["claude-opus-4-7", "claude-sonnet-4-6"],
    coworkEgressAllowedHosts: ["pypi.org", "registry.npmjs.org"],
  },
};
const ENTITLED_ROLES = new Set(["cowork-user", "cowork-power-user"]);

export async function handleBootstrap(req, res) {
  res.set("Cache-Control", "no-store");
  const token = (req.headers.authorization ?? "").replace(/^Bearer /, "");
  let payload;
  try {
    ({ payload } = await jwtVerify(token, JWKS, {
      issuer: `https://login.microsoftonline.com/${TENANT}/v2.0`,
      audience: CLIENT_ID,
      algorithms: ["RS256"],
    }));
  } catch {
    return res.status(401).json({ error: "invalid_token" });
  }
  const roles = payload.roles ?? [];
  if (!roles.some((r) => ENTITLED_ROLES.has(r))) {
    return res.status(403).json({ error: "not_entitled" });
  }
  const profile = roles.includes("cowork-power-user")
    ? PROFILES.power
    : PROFILES.default;
  return res
    .status(200)
    .json({ ...profile, expiresAt: Date.now() + 3600_000 });
}

Set `Cache-Control: no-store` on the response. Without it, a reverse proxy or CDN between the app and your endpoint may cache one user’s credentials and serve them to the next.

##  Authentication

The bootstrap request always carries a bearer token; there is no unauthenticated mode. Two ways to obtain that token, chosen by whether you set `bootstrapOidc` in MDM:

| Mode | When to use it | MDM keys |
| --- | --- | --- |
| **Separate identity provider (PKCE)** | Users sign in through your existing OIDC provider (Microsoft Entra ID, Okta, Ping, or any compliant provider). The app runs an OAuth authorization-code grant with PKCE in the system browser. | `bootstrapUrl` and `bootstrapOidc` |
| **Bootstrap server as authorization server (device code)** | Your bootstrap server (or the gateway it fronts) implements RFC 8414 discovery and the RFC 8628 device-code grant. One sign-in covers both the configuration fetch and inference when they share an origin. | `bootstrapUrl` only |

###  Separate identity provider (PKCE)

1

Register a public client in your identity provider

Register a native or public application with a loopback redirect URI and no client secret. The registration is identical to the one used for [gateway single sign-on](/docs/third-party/claude-desktop/gateway#set-up-single-sign-on); if you already have that, reuse it. See the [provider notes](#provider-notes) below for redirect-URI specifics.For Microsoft Entra ID, also set an **Application ID URI** on the registration (App registration → **Expose an API** → **Set**; accept the default `api://CLIENT_ID`). The `CLIENT_ID/.default` scope in the next step does not resolve without it.

2

Choose the scope your server will validate

The app sends the OAuth **access token** as the bearer. Your server validates that token’s `aud`, so the scope you request must produce a token whose audience your server accepts. This is provider-specific:

| Provider | Scope to request | Resulting `aud` |
| --- | --- | --- |
| Microsoft Entra ID | `openid offline_access CLIENT_ID/.default` | your client ID |
| Okta (custom authorization server) | `openid offline_access YOUR_API_SCOPE` | your authorization server’s audience |
| Generic OIDC | `openid offline_access` plus your API’s resource scope | provider-specific |

Include `offline_access` so the app receives a refresh token and can renew silently between launches.

For Entra, use the bare-GUID form `CLIENT_ID/.default`, **not** `api://CLIENT_ID/.default`. The `api://` form works on the initial authorize but fails on the refresh grant with `AADSTS90009` when the client and resource are the same application.

3

Validate the token in your server

See [Server responsibilities](#server-responsibilities). What the token’s `iss` and `aud` look like depends on your provider:

| Provider | `iss` to expect | `aud` to expect | JWKS URL |
| --- | --- | --- | --- |
| Microsoft Entra ID (token version `2`) | `https://login.microsoftonline.com/TENANT/v2.0` | your client ID | `https://login.microsoftonline.com/TENANT/discovery/v2.0/keys` |
| Okta (custom authorization server) | `https://YOUR_DOMAIN.okta.com/oauth2/AUTH_SERVER_ID` | the audience configured on that authorization server | `<issuer>/v1/keys` |

**Entra token version.** A new Entra app registration emits v1-format access tokens by default, with `iss` = `https://sts.windows.net/TENANT/` and `aud` = `api://CLIENT_ID`. Set the accepted-token-version field in the registration’s **Manifest** to `2` so tokens match the table above. The portal shows this field as either `accessTokenAcceptedVersion` or `api.requestedAccessTokenVersion` depending on the manifest view; set whichever you see. If you cannot change it, your server must accept both the v1 and v2 forms.**Group and role claims.** Entra does not emit `groups` or `roles` in access tokens by default. Enable the groups claim under App registration → **Token configuration**, or define **App roles** and assign users via **Enterprise applications**. The `oid` claim is always present. For Okta, add a `groups` claim on your custom authorization server with a group filter.

4

Configure and export from Claude Desktop

Install Claude Desktop on an admin workstation (see [Installation](/docs/third-party/claude-desktop/installation)). From the menu bar, open **Developer → Configure third-party inference**. In the **Source** section, fill in the **Bootstrap config URL** card:

| Field | Value |
| Bootstrap config URL | `https://YOUR_BOOTSTRAP_HOST/user/bootstrap` |
| Bootstrap OIDC parameters → Client ID | `YOUR_CLIENT_ID` |
| Bootstrap OIDC parameters → Issuer URL | `https://login.microsoftonline.com/YOUR_TENANT_ID/v2.0` |
| Bootstrap OIDC parameters → Scopes | `openid offline_access YOUR_CLIENT_ID/.default` |
| Bootstrap OIDC parameters → Redirect port | leave empty for Entra; set for Okta |

Click **Sign in** to test against your typed values. Once authenticated, the card shows the keys your server supplied. Click **Export** and choose the template format your MDM expects (`.mobileconfig`, ADMX, Intune OMA-URI JSON, or `.reg`). See [Deploy the configuration](/docs/third-party/claude-desktop/installation#5-deploy-the-configuration) for per-platform instructions.

####  Provider notes

| Provider | Redirect URI to register | Redirect port field | Additional setup |
| --- | --- | --- | --- |
| Microsoft Entra ID | `http://127.0.0.1/callback` under **Mobile and desktop applications** | Leave empty (any local port allowed) | Manifest: set the accepted-token-version field to `2`. **Expose an API**: set the Application ID URI. **Token configuration**: add the `groups` claim if your server authorizes on groups. |
| Okta | `http://127.0.0.1:53180/callback` (any fixed port) on a **Native** application | Set to the registered port | Create a custom authorization server with an audience your bootstrap server validates. |
| Other OIDC | `http://127.0.0.1/callback` | Set only if exact-port match is enforced | None |

Use `127.0.0.1`, not `localhost`.
The bootstrap sign-in is the only sign-in this page is concerned with. Any further authentication for inference depends on what your response provisions and is independent of bootstrap; see the relevant provider page ([gateway SSO](/docs/third-party/claude-desktop/gateway#single-sign-on-with-your-identity-provider), [Vertex](/docs/third-party/claude-desktop/vertex), [Bedrock](/docs/third-party/claude-desktop/bedrock), [Foundry](/docs/third-party/claude-desktop/foundry)).

###  Bootstrap server as authorization server (device code)

Set only `bootstrapUrl` in MDM. The app discovers your authorization endpoints via RFC 8414 and runs an RFC 8628 device-code grant. The bearer is reused for inference when `inferenceGatewayBaseUrl` shares the `bootstrapUrl` origin and `inferenceCredentialKind` is `interactive`, so the user signs in once for both.

1

Publish RFC 8414 discovery metadata

Serve a metadata document under the `bootstrapUrl` path. If `bootstrapUrl` ends in `/bootstrap` or `/user/bootstrap`, that suffix is stripped to form the issuer base.

GET https://YOUR_BOOTSTRAP_HOST/.well-known/oauth-authorization-server

{
  "issuer": "https://YOUR_BOOTSTRAP_HOST",
  "token_endpoint": "https://YOUR_BOOTSTRAP_HOST/oauth/token",
  "device_authorization_endpoint": "https://YOUR_BOOTSTRAP_HOST/oauth/device"
}

Every endpoint URL must share the `bootstrapUrl` origin. Metadata that points off-origin is rejected.

2

Implement the device-code grant

`POST` to `device_authorization_endpoint` returns:

{
  "device_code": "EXAMPLE-DEVICE-CODE-OPAQUE-TO-CLIENT",
  "user_code": "ABCD-EFGH",
  "verification_uri": "https://YOUR_BOOTSTRAP_HOST/activate",
  "verification_uri_complete": "https://YOUR_BOOTSTRAP_HOST/activate?user_code=ABCD-EFGH",
  "interval": 5,
  "expires_in": 600
}

`verification_uri` and `verification_uri_complete` must share the `bootstrapUrl` origin; federate behind your own pages rather than returning an upstream provider’s URL directly. The app opens the verification URL in the user’s browser and shows the user code.The app polls `token_endpoint` with `grant_type=urn:ietf:params:oauth:grant-type:device_code` and the `device_code`. Return `{"error":"authorization_pending"}` until the user approves, then:

{ "access_token": "eyJhbGciOiJSUzI1NiIs...", "expires_in": 3600 }

The polling interval is clamped between 1 and 30 seconds; the grant times out after 5 minutes; token TTL is clamped between 5 minutes and 24 hours.

3

Serve the configuration endpoint

On `GET <bootstrapUrl>` with a valid bearer, look up the user from the token claims and return their configuration (see [the HTTP contract](#the-http-contract)).

##  The HTTP contract

###  Request

GET /user/bootstrap HTTP/1.1
Host: YOUR_BOOTSTRAP_HOST
Authorization: Bearer eyJhbGciOiJSUzI1NiIs...
If-None-Match: "abc123"

The path is whatever you set in `bootstrapUrl`; there is no required path. Redirects are **not** followed: a `3xx` is treated as an error so a same-origin open redirect cannot exfiltrate the bearer. The request times out after 30 seconds.

###  Response

Return `200 OK` with `Content-Type: application/json` and a JSON object whose keys are a subset of the [published response schema](#response-schema). Keys use the exact managed-configuration key names. Unknown keys, keys that fail validation, and keys outside that schema are silently dropped; one bad key never invalidates the rest.

{
  "inferenceProvider": "gateway",
  "inferenceGatewayBaseUrl": "https://llm-gateway.example.corp",
  "inferenceCredentialKind": "interactive",
  "inferenceModels": ["claude-opus-4-7", "claude-sonnet-4-6"],
  "managedMcpServers": [{ "name": "internal-tools", "url": "https://mcp.example.corp/sse", "transport": "sse" }],
  "coworkEgressAllowedHosts": ["*.example.corp", "pypi.org"],
  "otlpResourceAttributes": { "user.email": "[email protected]", "team": "trading" },
  "expiresAt": 1778700000
}

| Status | App behavior |
| `200` | Parse and apply. |
| `304` | Re-serve the cached response (the app sends `If-None-Match` when it has one). |
| `401`, `403` | Discard the cached token and prompt the user to sign in again. A `401` on a background refresh keeps the running session and retries without prompting. Return `401` when the token is missing, expired, or the wrong audience; return `403` when the token is valid but the caller is not entitled. |
| Other non-2xx, or `3xx` | Fetch error. Falls back to the last good response from this session if one exists; otherwise the app stays in the degraded sign-in state. |

A `200` that is not a JSON object (an empty body, an HTML page from a captive portal or load balancer, or a JSON array) is a parse error. Make sure intermediate proxies do not rewrite the response.

###  Response schema

The full set of bootstrap-settable keys is published as a machine-readable JSON Schema, generated from the same source as the [configuration reference](/docs/third-party/claude-desktop/configuration) and updated with each release:

* [`/third-party/claude-desktop/schemas/bootstrap-config-v2.schema.json`](/docs/third-party/claude-desktop/schemas/bootstrap-config-v2.schema.json) (recommended): nested response format with a discriminated `inference` object.
* [`/third-party/claude-desktop/schemas/bootstrap-config-v1.schema.json`](/docs/third-party/claude-desktop/schemas/bootstrap-config-v1.schema.json): flat key format, kept for configurations authored before the v2 cutover. The app accepts either format.

Reference the schema with `"$schema"` in your response template, or with `# yaml-language-server: $schema=…` in YAML, for autocomplete and validation.
The response can supply any key in that schema, including inference credentials, model allowlists, MCP servers, the egress allowlist, telemetry endpoints, and the organization banner.

Organization plugins and skills can be delivered over the network by returning `organizationPluginsUrl` in the bootstrap response when using [device-code mode](#bootstrap-server-as-authorization-server-device-code), or through the filesystem `org-plugins/` directory described in [Connectors and extensions](/docs/third-party/claude-desktop/extensions). Network delivery is not available in PKCE mode.

A small set of keys are **structurally excluded** and ignored if returned:

* `bootstrapUrl`, `bootstrapOidc`, `bootstrapEnabled`: the trust anchor cannot redirect itself.
* `inferenceCredentialHelper` and other keys whose value is a local executable path: a network response cannot nominate code to run. `stdio`-transport entries in `managedMcpServers` are dropped for the same reason.
* Loopback hosts (`127.0.0.1`, `localhost`, `[::1]`) in any URL-valued key, regardless of scheme.

###  Caching and `expiresAt`

| Field | Type | Description |
| --- | --- | --- |
| `expiresAt` | `number` | Unix epoch (seconds or milliseconds) after which the client should re-fetch this document. Optional; when absent the client uses its default refresh interval. |

###  Origin pinning

When the bootstrap server is its own authorization server (no `bootstrapOidc`), the response is fenced: `inferenceGatewayBaseUrl`, `inferenceVertexBaseUrl`, `inferenceBedrockBaseUrl`, and `organizationPluginsUrl` must share the `bootstrapUrl` origin or the field is dropped. A compromised configuration response cannot redirect inference to an attacker-controlled host because the only host it can name is the one the user already authenticated to.
When you supply `bootstrapOidc`, your configuration server and gateway are independent hosts you control, so origin pinning is disabled and the response can name any HTTPS host. In this mode the bootstrap server’s integrity is the only control on where inference and MCP traffic are sent.

##  MDM configuration keys

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `bootstrapEnabled` | `boolean` | MDM only | `true` | Fetch and apply the URL above at launch. Turn off to keep the URL saved but skip the fetch. Defaults to `true`. |
| `bootstrapUrl` | `string` | MDM only | — | HTTPS endpoint that returns a per-user JSON config overlay. Values from the response override local settings and become read-only. |
| `bootstrapOidc` | `object` | MDM only | — | When set, the bootstrap request sends a Bearer token from a browser sign-in (authorization-code-with-PKCE). |

No `inferenceProvider` is needed in the MDM profile when using bootstrap; the response supplies it.

##  Troubleshooting

| Symptom | Likely cause |
| Identity provider shows `AADSTS900144` (Entra) or `invalid_request: scope` | `bootstrapOidc.scopes` is empty. It is required. |
| Server logs `unexpected "iss"` or `unexpected "aud"` for a valid Entra token | The app registration’s accepted-token-version is at its default. Set it to `2` in the Manifest, or accept both v1 (`sts.windows.net` / `api://CLIENT_ID`) and v2 forms in your server. |
| Sign-in succeeds in the browser but the app immediately re-prompts | Your server returned `401` or `403`. For `401`, check the `aud` match: the requested scope must produce a token whose audience your server validates. For `403`, the user authenticated but is not in the entitled group or role. |
| Entra returns `AADSTS500011` (“resource principal not found”) | The app registration has no Application ID URI. Set one under **Expose an API**. |
| Silent refresh fails after ~1 hour with `AADSTS90009` | `scopes` uses the `api://CLIENT_ID/.default` form. Use the bare-GUID `CLIENT_ID/.default` form. |
| Some keys you returned are not applied | They failed schema validation, are structurally excluded, or were dropped by origin pinning. The desktop log (`~/Library/Logs/Claude-3p/main.log` on macOS, `%LOCALAPPDATA%\Claude-3p\logs\main.log` on Windows) records which keys were dropped and why. |
| Browser opens to your identity provider’s device page instead of yours | In device-code mode, `verification_uri` must share the `bootstrapUrl` origin. Federate behind your own page. |

[Configuration changelog](/docs/third-party/claude-desktop/configuration-changelog)[Write a credential helper](/docs/third-party/claude-desktop/credential-helper)
