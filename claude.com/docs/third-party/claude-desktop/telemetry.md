<!-- source: https://claude.com/docs/third-party/claude-desktop/telemetry -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

When Claude Desktop on third-party (3P) is configured with Google Cloud’s Agent Platform, Amazon Bedrock, or Microsoft Foundry, the app sends conversation content only to your configured inference endpoint. For Microsoft Foundry, how data is handled beyond that endpoint depends on the deployment’s hosting option; see [Claude in Microsoft Foundry](https://claude.com/docs/third-party/claude-desktop/foundry). The app does, by default, send a small amount of operational telemetry (crash reports and product analytics) that helps Anthropic diagnose issues and improve the product. Each category can be disabled independently via managed configuration.
This page covers what each category contains, how to turn it off, and the complete set of outbound hostnames the app uses so you can configure your perimeter firewall.

##  Telemetry categories

###  Essential telemetry

Crash reports, error stack traces, and performance timings. Contains diagnostic metadata (app version, OS, error type, redacted stack frames) but **never prompt or response content**. Attributed to your organization via `deploymentOrganizationUuid` so Anthropic support can find issues you report.

| Setting | Default | Effect when `true` |
| --- | --- | --- |
| `disableEssentialTelemetry` | `false` | No crash or error data leaves the device. |

Disabling essential telemetry opts you into a **manual support model**. Anthropic will have zero remote visibility into failures on your fleet, so to get help with an issue your team will need to collect application logs from affected machines and send them to Anthropic directly. Leave this enabled during initial rollout.

###  Non-essential telemetry

Product-usage analytics: feature adoption, session counts, UI interactions. Used to understand how Claude Desktop is used in aggregate. Contains no prompt or response content. Also gates the **Send** button in Help → Generate Diagnostic Report; with this disabled, diagnostic bundles can only be saved locally.

| Setting | Default | Effect when `true` |
| --- | --- | --- |
| `disableNonessentialTelemetry` | `false` | No product analytics leave the device. |

Leaving this enabled also adds `api.anthropic.com` to the [agent egress allowlist](#required-egress-paths) automatically, so Claude Code can deliver its usage telemetry from inside the sandbox. Allow that host at the perimeter too; it appears in the non-essential telemetry table below.

###  Non-essential services

Cosmetic third-party fetches: favicons for connectors shown in the UI, the MCP connector directory lookup, the sandboxed iframe that renders interactive artifact previews, and the sandboxed iframes that render [MCP Apps](https://claude.com/docs/connectors/building/mcp-apps/getting-started), the interactive widgets connectors can display. Disabling these degrades the UI (generic icons, no directory suggestions, static artifact previews, and connector tool results shown as text instead of widgets) but doesn’t affect functionality.

| Setting | Default | Effect when `true` |
| --- | --- | --- |
| `disableNonessentialServices` | `false` | Favicon, artifact-preview, and MCP App widget fetches are blocked. Connectors that return MCP Apps show the tool’s text result instead of the widget. |

###  Auto-updates

Checks Anthropic’s update feed and downloads new builds.

| Setting | Default | Effect when `true` |
| --- | --- | --- |
| `disableAutoUpdates` | `false` | The app never checks for or downloads updates. Your IT team must redistribute new builds. |

##  Sending telemetry to your own collector

Independently of what’s sent to Anthropic, you can export session activity to your own OpenTelemetry collector by setting `otlpEndpoint`. This is the recommended way to retain an audit trail in environments that disable Anthropic-bound telemetry.
For third-party deployments, the export includes session metadata (event names, durations, token counts, result counts, errors) by default, but not message content. See [Monitoring](https://claude.com/docs/cowork/monitoring) for the event schema and the [`otlp*` keys](https://claude.com/docs/third-party/claude-desktop/configuration#otlpendpoint) in the configuration reference.
The export carries logs and metrics. Cowork sessions, Code sessions, and the desktop application’s own events arrive under the `service.name` values `cowork`, `claude-code-desktop`, and `claude-desktop` respectively. The app adds the collector host to the sandbox egress allowlist automatically, so `otlpEndpoint` does not need an entry in `coworkEgressAllowedHosts`; your perimeter firewall still needs to allow the host.
For collector authentication headers, extra resource attributes, and the log level of the desktop application’s own event stream, see [`otlpHeaders`, `otlpResourceAttributes`, and `otlpDesktopLogLevel`](https://claude.com/docs/third-party/claude-desktop/configuration#otlpheaders) in the configuration reference.

###  Exporter protocol

The `otlpProtocol` key selects the transport for the telemetry export to your collector: `http/protobuf` (the default), `http/json`, or `grpc`. The protocol applies per session type:

* [Code](https://claude.com/docs/third-party/claude-desktop/code) sessions export over the protocol as configured, including `grpc`.
* Cowork sessions do not support gRPC export. When `otlpProtocol` is set to `grpc`, Cowork sessions export over `http/protobuf` instead; other protocol values apply as configured.

The fallback changes the protocol only, not the endpoint. When `otlpProtocol` is `grpc`, Cowork’s export goes to the same `otlpEndpoint` over HTTP; if that address is your collector’s OTLP/gRPC receiver (conventionally port 4317), Cowork telemetry never reaches the collector. To receive telemetry from both session types with one collector, set `otlpProtocol` to `http/protobuf` and point `otlpEndpoint` at the collector’s OTLP/HTTP receiver (conventionally port 4318).

###  Content capture

To include content in the export, set `otlpContentCapture` to an array of categories:

| Category | Captures |
| --- | --- |
| `userPrompts` | User message text |
| `assistantResponses` | Model response text |
| `toolDetails` | Tool input arguments (for example, the web-search query string) |
| `toolContent` | Tool output content |
| `rawApiBodies` | Full inference request and response bodies |

On Claude Desktop version 1.17377 or later, enabling `userPrompts` also captures model responses, even if `assistantResponses` is not listed. On those versions, no `otlpContentCapture` configuration captures user prompts without model responses.
Content is exported only to your configured `otlpEndpoint`. Anthropic does not receive it.

###  Traces (beta)

The export carries logs (events) and metrics; it does not include traces unless you enable them. To export OpenTelemetry traces as well, set `otlpTracesEnabled` to `true`. Cowork and Code sessions then record a trace for each user interaction, with spans for model requests and tool executions, and every event emitted during a span carries that span’s `trace_id` and `span_id`. This lets your backend correlate a prompt’s events end-to-end natively, with no transformation on ingest.
Traces use the same `otlpEndpoint` and `otlpProtocol` as the rest of the export, including the Cowork gRPC fallback described in [Exporter protocol](#exporter-protocol). Span and span-event content is gated by the same `otlpContentCapture` categories as events: with no categories enabled, traces carry metadata only (timing, tool names, durations, token counts). Captured content appears primarily on events; spans stay close to metadata.
Two scope notes:

* The metrics in this export don’t carry trace context, so trace-based correlation covers traces and events. Correlate metrics with a session via the `session.id` attribute.
* Trace export uses Claude Code’s session-tracing beta, and the span structure may change while the feature is in beta.

`otlpTracesEnabled` requires Claude Desktop **1.22209.0** or later.

##  Required egress paths

Claude Desktop on 3P has **two** independent network boundaries:

1. **Perimeter firewall:** your corporate network controls what the device can reach. The hostnames below are what you allowlist here.
2. **Agent egress allowlist:** the [`coworkEgressAllowedHosts`](https://claude.com/docs/third-party/claude-desktop/configuration#coworkegressallowedhosts) key controls what the agent’s web-fetch and shell tools can reach. This is independent of, and stricter than, the perimeter.

The **Egress Requirements** section of the in-app configuration window is the authoritative source for your deployment. It computes the exact allowlist from your current settings, updates as you change them, and can export the list as a text file for your firewall team. Use the tables below as a static reference; defer to the configuration window for the precise set your build requires.

All traffic is HTTPS on port 443. Allowlist by hostname (SNI); path-level rules aren’t required.

###  Always required

| Host | Purpose |
| --- | --- |
| `downloads.claude.ai` | VM workspace bundle and Claude CLI binary, fetched at session start. **Without this, Cowork sessions cannot start**, unless the app was installed with the [offline installer variant](https://claude.com/docs/third-party/claude-desktop/installation#offline-installation), which includes both components in the installer package. |

###  Inference provider

The host(s) for your configured provider. These carry conversation content.

* Google Cloud's Agent Platform
* Amazon Bedrock
* Microsoft Foundry
* Gateway

| Host | Purpose |
| --- | --- |
| `<region>-aiplatform.googleapis.com` | Model inference for single regions. The `global` region uses `aiplatform.googleapis.com`, and the `eu` / `us` multi-regions use `aiplatform.eu.rep.googleapis.com` / `aiplatform.us.rep.googleapis.com`. Replaced by the host of `inferenceVertexBaseUrl` if set. |
| `oauth2.googleapis.com` | Google auth token exchange |
| `sts.googleapis.com` | Google auth token exchange |
| `accounts.google.com` | Google auth token exchange |
| `iamcredentials.googleapis.com` | Google auth token exchange |

| Host | Purpose |
| --- | --- |
| `bedrock-runtime.<region>.amazonaws.com` | Model inference. Replaced by the host of `inferenceBedrockBaseUrl` if set. |
| `bedrock.<region>.amazonaws.com` | Control plane (model discovery) |
| `sts.amazonaws.com`, `sts.<region>.amazonaws.com` | STS token exchange (profile auth only) |
| `portal.sso.<region>.amazonaws.com`, `oidc.<region>.amazonaws.com` | AWS SSO (profile auth only) |

With `inferenceBedrockBearerToken` set, the runtime and control-plane hosts are required.For AWS GovCloud regions (`us-gov-*`), the app automatically uses the FIPS endpoints instead: `bedrock-runtime-fips.<region>.amazonaws.com` and `bedrock-fips.<region>.amazonaws.com`.

| Host | Purpose |
| --- | --- |
| `<resource>.services.ai.azure.com` | Model inference |
| `login.microsoftonline.com` | Entra ID auth (interactive sign-in only) |

| Host | Purpose |
| --- | --- |
| Host of `inferenceGatewayBaseUrl` | Model inference |

###  Auto-updates (`disableAutoUpdates: false`)

| Host | Purpose |
| --- | --- |
| `claude.ai` | Update feed |
| `api.anthropic.com` | Update feed |
| `downloads.claude.ai` | Update binaries (already required above) |

###  Essential telemetry (`disableEssentialTelemetry: false`)

| Host | Purpose |
| --- | --- |
| `sentry.io` | Crash and error reporting (apex; some firewalls don’t match it under `*.sentry.io`) |
| `*.sentry.io` | Crash and error reporting |
| `*.ingest.us.sentry.io` | Crash and error reporting (listed separately for firewalls that match wildcards one label deep) |
| `browser-intake-us5-datadoghq.com` | Performance timing. The configuration window lists additional regional Datadog intake hosts. |

###  Non-essential telemetry (`disableNonessentialTelemetry: false`)

| Host | Purpose |
| --- | --- |
| `a-cdn.anthropic.com` | Analytics SDK |
| `api.anthropic.com` | Claude Code usage telemetry, sent from inside the agent sandbox |
| `a-api.anthropic.com` | Analytics events |
| `claude.ai` | Analytics events |

###  Non-essential services (`disableNonessentialServices: false`)

| Host | Purpose |
| --- | --- |
| `api.anthropic.com` | MCP connector directory |
| `www.claudeusercontent.com` | Artifact preview iframe |
| `*.claudemcpcontent.com` | [MCP Apps](https://claude.com/docs/connectors/building/mcp-apps/getting-started), the interactive widgets connectors can render. Each widget loads in a sandboxed iframe on its own generated subdomain, so allowlist the wildcard. |
| `assets.claude.ai` | Fonts loaded by MCP App widget iframes |
| `cdnjs.cloudflare.com`, `cdn.jsdelivr.net`, `fonts.googleapis.com` | Artifact preview asset CDNs |
| `www.google.com`, `*.gstatic.com` | Connector favicons |

###  Optional features

| Host | Required when |
| --- | --- |
| Host of `otlpEndpoint` | OpenTelemetry export is configured |
| `github.com`, `objects.githubusercontent.com`, `pypi.org`, `files.pythonhosted.org` | Python-based desktop extensions are enabled |
| Hosts of each entry in `managedMcpServers` (server URL, plus `oauth.authorizationServer` and `login.microsoftonline.com` if configured) | Managed MCP servers are configured |
| Hosts in `coworkEgressAllowedHosts` | Sandbox web access is configured |

##  Disabling all Anthropic-bound connections

With `disableEssentialTelemetry`, `disableNonessentialTelemetry`, `disableNonessentialServices`, and `disableAutoUpdates` all set to `true`, the desktop application makes **no outbound connections to Anthropic-operated hosts at runtime**. The only required egress is `downloads.claude.ai` (for the VM bundle at session start) and your inference provider. With the [offline installer variant](https://claude.com/docs/third-party/claude-desktop/installation#offline-installation), `downloads.claude.ai` is not needed either, and your inference provider is the only required egress. This describes the application’s own connections; what happens to conversation content after it reaches your inference provider is governed by that provider; see the [Overview](https://claude.com/docs/third-party/claude-desktop/overview).
See the [Locked down profile](https://claude.com/docs/third-party/claude-desktop/configuration#recommended-security-profiles) for a complete configuration.

##  Proxy support

The Cowork sandbox honors the host operating system’s proxy configuration, including PAC (proxy auto-configuration) files. If the device routes HTTPS through a corporate proxy, the sandbox will too, with no additional configuration required.

###  TLS-intercepting proxies on macOS

If your proxy performs TLS interception, it presents its own certificate authority. Claude configures its CLI processes to trust the macOS System keychain in addition to the bundled CA roots, so a corporate CA installed there normally works without extra setup.
If inference or tool requests still fail certificate verification, the CA was likely added with policy-restricted trust: certificates installed via `security add-trusted-cert -p ssl …` are trusted by Safari and Chrome but are not picked up by the CLI runtime’s keychain reader. Re-add the CA with full root trust (omit `-p`):

```
sudo security add-trusted-cert -d -r trustRoot \
  -k /Library/Keychains/System.keychain /path/to/corp-ca.pem
```

If the certificate is MDM-managed and you cannot change how it is installed, set `NODE_EXTRA_CA_CERTS` as a fallback, then quit and relaunch Claude:

```
security find-certificate -a -p /Library/Keychains/System.keychain > ~/corp-ca.pem
launchctl setenv NODE_EXTRA_CA_CERTS "$HOME/corp-ca.pem"
```

`launchctl setenv` makes the variable visible to apps launched from Finder or the Dock (shell-profile exports only reach terminal sessions). It applies until the next reboot; to make it permanent, run the command from a LaunchAgent at login.
