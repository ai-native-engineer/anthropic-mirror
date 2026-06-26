<!-- source: https://claude.com/docs/third-party/claude-desktop/configuration -->

Claude Desktop on third-party (3P) is configured entirely through OS-native managed preferences: a `.mobileconfig` profile on macOS or registry policy on Windows. This page documents every supported key. For the desktop release each key first appeared in, see the [configuration changelog](/docs/third-party/claude-desktop/configuration-changelog).
The easiest way to author a configuration is the in-app configuration window (**Developer → Configure third-party inference**), which validates values, shows per-provider requirements, and exports directly to `.mobileconfig` or `.reg`. Use this reference when you need to author policy by hand, audit an existing profile, or understand exactly what a key does.

##  How keys are read

| Platform | Managed (MDM) location | Local (user) location |
| --- | --- | --- |
| macOS | `/Library/Managed Preferences/<user>/com.anthropic.claudefordesktop.plist` | `~/Library/Application Support/Claude-3p/configLibrary/` |
| Windows | `HKLM\SOFTWARE\Policies\Claude` (machine), `HKCU\SOFTWARE\Policies\Claude` (user) | `%LOCALAPPDATA%\Claude-3p\configLibrary\` |

The local location is a directory: `_meta.json` records which saved configuration is applied, and each configuration is a `<id>.json` file alongside it. The in-app configuration window writes here.
When a managed source is present, it wins and locally written values are ignored. Configuration is read **once at launch**, so fully quit and reopen the app after any change. See [Installation and setup](/docs/third-party/claude-desktop/installation) for the full precedence rules.

###  Value types

All values are stored as **strings** in the OS preference store, even booleans and arrays.

| Documented type | What to write | Example |
| --- | --- | --- |
| string | Plain string | `vertex` |
| boolean | `"true"` or `"false"` (or `1` / `0`) | `"true"` |
| integer | Decimal string | `"3600"` |
| string[] (JSON) | JSON array **encoded as a string** (not a native plist/registry array) | `["claude-sonnet-4","claude-opus-4"]` |
| object (JSON) | JSON object mapping name to value, as a string | `{"X-Org-Id":"team1"}` |
| object[] (JSON) | JSON array of objects, as a string | see [`managedMcpServers`](#managedmcpservers) |

The most common configuration mistake is writing array- or object-typed keys as native plist/registry structures. Keys like `inferenceModels`, `inferenceGatewayOidc`, `managedMcpServers`, `coworkEgressAllowedHosts`, and `otlpHeaders` must be **JSON strings**. In a `.mobileconfig`, that means a single `<string>` element containing `[...]` or `{...}` — not an `<array>`, not a `<dict>`, and not separate keys with dotted names like `inferenceGatewayOidc.clientId`.

##  Reference

The reference below is generated from the configuration schema and grouped to match the sidebar of the in-app configuration window. The **Availability** column shows whether a key can be set in an MDM profile, returned from a [bootstrap server](/docs/third-party/claude-desktop/bootstrap), or both.

##  Connection

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `inferenceCustomHeaders` | `object` | MDM + Bootstrap | — | Extra HTTP headers sent on every inference request to the configured provider. For tenant routing, org IDs, Bedrock Guardrails, etc. Previously named `inferenceGatewayHeaders`. |
| `inferenceSessionLifetimeSec` | `integer` | MDM + Bootstrap | — | How long a sign-in stays valid under your IdP’s session policy. Shows a re-authenticate banner before it expires. |
| `inferenceCredentialHelper` | `string` | MDM only | — | Absolute path to an executable that prints the credential, optionally with per-request headers. |
| `inferenceCredentialHelperTtlSec` | `integer` | MDM only | `3600` | Helper output is cached for this many seconds. Re-runs at the next session start after expiry. Defaults to `3600`. |
| `inferenceCredentialHelperTimeoutSec` | `integer` | MDM only | `60` | Maximum wait for the helper executable to finish. Raise this if the helper opens a browser for interactive sign-in. Defaults to `60`. Range: 1–600. |
| `inferenceCredentialHelperSilentRefreshEnabled` | `boolean` | MDM only | `true` | When a session’s credential expires, re-run the helper with CLAUDE\_HELPER\_CONTEXT=mid-session-refresh to recover silently. Turn this off if your helper can’t run non-interactively. Defaults to `true`. |
| `inferenceProvider` | `enum` | MDM + Bootstrap | — | Selects the inference backend. Setting this key activates third-party mode. One of: `gateway`, `anthropic`, `bedrock`, `mantle`, `vertex`, `foundry`. |
| `inferenceCredentialKind` | `enum` | MDM + Bootstrap | — | Selects the credential source. When set, only that source is used (no fallback). One of: `static`, `helper-script`, `interactive`, `vendor-profile`, `oauth`, `workforce`. |

###  Anthropic

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `inferenceAnthropicApiKey` | `string` | MDM + Bootstrap | — | Leave blank to fetch a key via browser sign-in, or to supply the key via a credential helper. |

###  Bedrock

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `inferenceBedrockRegion` | `string` | MDM + Bootstrap | — | AWS region for the Bedrock runtime endpoint. |
| `inferenceBedrockBaseUrl` | `string` | MDM + Bootstrap | — | For VPC endpoints or gateway proxies. Host origin only. |
| `inferenceBedrockServiceTier` | `enum` | MDM + Bootstrap | — | Sent as the X-Amzn-Bedrock-Service-Tier header. Leave unset for on-demand. One of: `flex`, `priority`. |
| `inferenceBedrockBearerToken` | `string` | MDM + Bootstrap | — |  |
| `inferenceBedrockSsoStartUrl` | `string` | MDM + Bootstrap | — | Enables in-app AWS sign-in (no AWS CLI needed). Set with the three SSO fields below. |
| `inferenceBedrockSsoRegion` | `string` | MDM + Bootstrap | — | IAM Identity Center home region. |
| `inferenceBedrockSsoAccountId` | `string` | MDM + Bootstrap | — | 12-digit AWS account ID assigned to users in IAM Identity Center. |
| `inferenceBedrockSsoRoleName` | `string` | MDM + Bootstrap | — | IAM Identity Center permission-set name granting bedrock:InvokeModel\* on the account above. |
| `inferenceBedrockProfile` | `string` | MDM only | — |  |
| `inferenceBedrockAwsDir` | `string` | MDM only | — | Folder with AWS config/credentials. Defaults to ~/.aws when no bearer token is set. |
| `inferenceBedrockAwsCliPath` | `string` | MDM only | — | Absolute path to the aws executable. Leave unset to find it on PATH. |

###  Foundry

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `inferenceFoundryResource` | `string` | MDM + Bootstrap | — | Azure AI Foundry resource name used to construct the endpoint URL. |
| `inferenceFoundryApiKey` | `string` | MDM + Bootstrap | — |  |
| `inferenceFoundryTenantId` | `string` | MDM only | — | Directory (tenant) ID of the Entra ID app registration that has the Cognitive Services scope. |
| `inferenceFoundryClientId` | `string` | MDM only | — | Application (client) ID of the Entra ID app registration. The app must allow public client flows for device code. |

###  Gateway

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `inferenceGatewayBaseUrl` | `string` | MDM + Bootstrap | — | Full URL of the inference gateway endpoint. |
| `inferenceGatewayApiKey` | `string` | MDM + Bootstrap | — |  |
| `inferenceGatewayAuthScheme` | `enum` | MDM + Bootstrap | `bearer` | How the gateway credential is sent on the wire (Authorization: Bearer vs x-api-key header). One of: `bearer`, `x-api-key`. Defaults to `bearer`. |
| `inferenceGatewayOidc` | `object` | MDM + Bootstrap | — | External IdP for gateway sign-in. The user authenticates against this issuer; the resulting token (ID token by default) is sent to the gateway as the Bearer credential. Leave unset only if the gateway is its own OAuth authorization server. |

###  Models

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `modelDiscoveryEnabled` | `boolean` | MDM + Bootstrap | — | Auto-populate the model picker from the provider at launch. |
| `inferenceModels` | `object[]` | MDM + Bootstrap | — | Override the auto-discovered model list. First entry is the default. |

###  Vertex

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `inferenceVertexProjectId` | `string` | MDM + Bootstrap | — |  |
| `inferenceVertexRegion` | `string` | MDM + Bootstrap | — | GCP region where your Vertex AI Claude models are deployed. |
| `inferenceVertexBaseUrl` | `string` | MDM + Bootstrap | — | PSC endpoint, if using one. |
| `inferenceVertexOAuthClientId` | `string` | MDM + Bootstrap | — | Desktop-app OAuth client ID. Enables Sign in with Google instead of a credentials file. |
| `inferenceVertexOAuthClientSecret` | `string` | MDM + Bootstrap | — | Secret for the Desktop-app OAuth client above. |
| `inferenceVertexOAuthScopes` | `string` | MDM + Bootstrap | — | Override the Google OAuth scopes (space-separated). Leave blank for the default. |
| `inferenceVertexOAuthLoginHint` | `string` | MDM + Bootstrap | — | Pre-fill Google’s account chooser and forward to your federated IdP. {username} expands to the OS login name. |
| `inferenceVertexWorkforceAudience` | `string` | MDM + Bootstrap | — | Workforce-pool provider audience. When set, sign-in uses your own IdP plus a GCP STS exchange instead of a Google identity. |
| `inferenceVertexWorkforceUserProject` | `string` | MDM + Bootstrap | — | GCP project for STS billing and quota. Defaults to the Vertex project ID above. |
| `inferenceVertexWorkforceOidc` | `object` | MDM + Bootstrap | — | Your organization’s OIDC IdP. The app runs an authorization-code-with-PKCE flow against this issuer and exchanges the returned ID token at GCP STS. |
| `inferenceVertexCredentialsFile` | `string` | MDM only | — | Absolute path to service-account JSON. Leave blank to fall back to ADC. |

##  Workspace restrictions

###  Authentication

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `disableDeploymentModeChooser` | `boolean` | MDM only | `false` | Users see only this provider at the login screen. The option to sign in to Claude.ai is hidden. Defaults to `false`. |
| `disableDeepLinkRegistration` | `boolean` | MDM only | `false` | Stop external apps and websites from opening Cowork via claude:// links. Defaults to `false`. |

###  Chat Surface

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `chatTabEnabled` | `boolean` | MDM + Bootstrap · Beta | — | Enable the Chat tab. Quick questions and drafting. |
| `chatAdvancedFileAnalysisEnabled` | `boolean` | MDM + Bootstrap · Beta | — | Allow Claude to run code in a local sandbox to analyze attached files it can’t read natively — like Excel and PowerPoint — and perform inline data analysis. The sandbox can only read files attached to the conversation and has no network access. Off by default. |

###  Code Surface

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `isClaudeCodeForDesktopEnabled` | `boolean` | MDM + Bootstrap | `true` | Enable the Code tab. Claude writes and runs code. Defaults to `true`. |

###  Cowork Surface

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `coworkTabEnabled` | `boolean` | MDM + Bootstrap | `true` | Enable the Cowork tab. Claude works on longer tasks like research, analysis, and documents. Defaults to `true`. |

###  Workspace

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `disabledBuiltinTools` | `string[]` | MDM + Bootstrap | — | Built-in tools removed from Cowork. |
| `disableBundledSkills` | `boolean` | MDM + Bootstrap | — | Disables Claude Code’s bundled skills and workflows (deep-research and similar). Use where they cannot function, for instance when WebFetch is egress-blocked and the gateway does not forward the WebSearch server tool. |
| `builtinToolPolicy` | `object` | MDM + Bootstrap | — | Per-tool approval policy. “ask” requires user approval before each call; “allow” is the default. Use Disabled built-in tools to remove a tool entirely. |
| `autoModeEnabled` | `boolean` | MDM + Bootstrap | `false` | Offer Auto mode in the Cowork and Code permission selectors. Claude decides which actions need approval. Defaults to `false`. |
| `allowedWorkspaceFolders` | `object[]` | MDM + Bootstrap | — | Folders users may attach as a workspace. Leave unset for unrestricted access. Supports ~ and a fixed set of environment variables. |
| `coworkEgressAllowedHosts` | `string[]` | MDM + Bootstrap | — | Hostnames the agent’s tools may reach from the Cowork and Code tabs. Also surfaced under Egress Requirements. |
| `requireCoworkFullVmSandbox` | `boolean` | MDM + Bootstrap · Deprecated | `false` | Runs tools inside an isolated VM instead of the host. Stronger isolation; slower file access and no host-process tools. Defaults to `false`. |

##  Connectors & extensions

###  Extensions

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `isDesktopExtensionEnabled` | `boolean` | MDM + Bootstrap | `true` | .dxt and .mcpb installs. Defaults to `true`. Previously named `isDxtEnabled`. |
| `isDesktopExtensionSignatureRequired` | `boolean` | MDM + Bootstrap | `false` | Reject desktop extensions that are not signed by a trusted publisher. Defaults to `false`. Previously named `isDxtSignatureRequired`. |

###  Mcp

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `managedMcpServers` | `object[]` | MDM + Bootstrap | — | Org-pushed MCP servers: remote (HTTP/SSE) or local (stdio command). May embed bearer tokens. |
| `isLocalDevMcpEnabled` | `boolean` | MDM + Bootstrap | `true` | Local stdio servers added via the Developer settings. Remote servers come from the managed list above, or plugins mounted to a user’s computer by an organization admin. Defaults to `true`. |

##  Telemetry & updates

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `deploymentOrganizationUuid` | `string` | MDM + Bootstrap | — | A UUID you generate. Tags telemetry so Anthropic support can locate your fleet’s events. If unset, a shared placeholder UUID is sent and your events can’t be distinguished from other unconfigured deployments. Not used for auth. |
| `disableEssentialTelemetry` | `boolean` | MDM only | `false` | Crash and performance reports to Anthropic. Defaults to `false`. |
| `disableNonessentialTelemetry` | `boolean` | MDM + Bootstrap | `false` | Product-usage analytics and diagnostic-report uploads. No message content. Defaults to `false`. |
| `disableNonessentialServices` | `boolean` | MDM + Bootstrap | `false` | Favicon fetch and the artifact-preview iframe origin. Artifacts will not render. Defaults to `false`. |

###  Auto Update

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `disableAutoUpdates` | `boolean` | MDM + Bootstrap | `false` | Stop Cowork from fetching updates. You’ll need to push new versions yourself. Defaults to `false`. |
| `autoUpdaterEnforcementHours` | `integer` | MDM + Bootstrap | — | Hours before a downloaded update force-installs. Blank = 72-hour default. Range: 1–72. |

###  Otlp

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `otlpEndpoint` | `string` | MDM + Bootstrap | — | Where Cowork sends OpenTelemetry logs and metrics. Leave blank to disable. |
| `otlpProtocol` | `enum` | MDM + Bootstrap | `http/protobuf` | grpc or http/protobuf. One of: `http/protobuf`, `http/json`, `grpc`. Defaults to `http/protobuf`. |
| `otlpHeaders` | `object` | MDM + Bootstrap | — | Optional auth headers for the collector. |
| `otlpResourceAttributes` | `object` | MDM + Bootstrap | — | Extra resource attributes to attach to every span/metric. |
| `otlpDesktopLogLevel` | `enum` | MDM + Bootstrap | `error` | Controls the Claude Desktop application’s events, separate from Cowork and Code sessions. Defaults to error. One of: `off`, `error`, `warn`, `info`, `debug`. Defaults to `error`. |
| `otlpContentCapture` | `enum[]` | MDM + Bootstrap | — | Content categories the desktop exporter sends unredacted to your collector. Leave empty to redact all content (default). |

##  Usage limits

###  Token Limits

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `inferenceMaxTokensPerWindow` | `integer` | MDM + Bootstrap | — | Per-user soft cap, counted client-side over the duration below. Not a server-enforced quota. |
| `inferenceTokenWindowHours` | `integer` | MDM + Bootstrap | — | Tumbling window length for the token cap. Max 720 hours (30 days). Range: 1–720. |

##  Appearance

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `banner` | `object` | MDM + Bootstrap | — | A persistent banner across the top of the app window after sign-in. |

##  Plugins & skills

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `organizationPluginsUrl` | `string` | MDM + Bootstrap | — | Typically supplied by your bootstrap server. Ignored when bootstrap is disabled. |
| `orgPluginSettings` | `object[]` | MDM + Bootstrap | — | Admin policy applied to plugin-delivered MCP servers. |

##  Source

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `claudeAiImport` | `object` | Bootstrap only | — |  |

###  Bootstrap

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `bootstrapEnabled` | `boolean` | MDM only | `true` | Fetch and apply the URL above at launch. Turn off to keep the URL saved but skip the fetch. Defaults to `true`. |
| `bootstrapUrl` | `string` | MDM only | — | HTTPS endpoint that returns a per-user JSON config overlay. Values from the response override local settings and become read-only. |
| `bootstrapOidc` | `object` | MDM only | — | When set, the bootstrap request sends a Bearer token from a browser sign-in (authorization-code-with-PKCE). |

##  Guides

###  Recommended security profiles

The profiles below are illustrative examples rather than built-in presets, and the labels are descriptive only. Use them as starting points and adjust for your environment. Layer the inference-provider keys for your cloud on top of whichever profile you choose.

* Standard
* Restricted
* Locked down

Recommended for most enterprise deployments. Telemetry and auto-updates stay on so Anthropic can diagnose issues and ship fixes; users can extend Claude Desktop with their own connectors.

| Key | Value |
| [`deploymentOrganizationUuid`](#deploymentorganizationuuid) | `<your-org-uuid>` |
| [`autoUpdaterEnforcementHours`](#autoupdaterenforcementhours) | `24` |
| [`isDesktopExtensionSignatureRequired`](#isdesktopextensionsignaturerequired) | `true` |
| [`otlpEndpoint`](#otlpendpoint) | `<your-collector>` |

For regulated environments that need to control what users can connect Claude Desktop to, while keeping Anthropic supportability.

| Key | Value |
| [`deploymentOrganizationUuid`](#deploymentorganizationuuid) | `<your-org-uuid>` |
| [`disableNonessentialTelemetry`](#disablenonessentialtelemetry) | `true` |
| [`disableNonessentialServices`](#disablenonessentialservices) | `true` |
| [`isLocalDevMcpEnabled`](#islocaldevmcpenabled) | `false` |
| [`isDesktopExtensionEnabled`](#isdesktopextensionenabled) | `false` |
| [`allowedWorkspaceFolders`](#allowedworkspacefolders) | `[{"path":"~/Documents/Claude"}]` |
| [`coworkEgressAllowedHosts`](#coworkegressallowedhosts) | `["*.example.corp"]` |
| [`otlpEndpoint`](#otlpendpoint) | `<your-collector>` |

For air-gapped or maximally restricted environments. **The only traffic leaving the device goes to your inference endpoint and OTLP collector.** With this profile, Anthropic has zero remote visibility, so your team owns log collection and update distribution.

| Key | Value |
| [`disableEssentialTelemetry`](#disableessentialtelemetry) | `true` |
| [`disableNonessentialTelemetry`](#disablenonessentialtelemetry) | `true` |
| [`disableNonessentialServices`](#disablenonessentialservices) | `true` |
| [`disableAutoUpdates`](#disableautoupdates) | `true` |
| [`isLocalDevMcpEnabled`](#islocaldevmcpenabled) | `false` |
| [`isDesktopExtensionEnabled`](#isdesktopextensionenabled) | `false` |
| [`disabledBuiltinTools`](#disabledbuiltintools) | `["WebSearch","WebFetch"]` |
| [`coworkEgressAllowedHosts`](#coworkegressallowedhosts) | `[]` |
| [`allowedWorkspaceFolders`](#allowedworkspacefolders) | `[{"path":"~/Documents/Claude"}]` |
| [`otlpEndpoint`](#otlpendpoint) | `<your-collector>` |

[Installation and setup](/docs/third-party/claude-desktop/installation)[Configuration changelog](/docs/third-party/claude-desktop/configuration-changelog)
