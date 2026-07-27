<!-- source: https://claude.com/docs/third-party/claude-desktop/configuration-changelog -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

Configuration keys by Claude Desktop release. Each section lists keys added in that release, with the MDM key name (for plist/registry deployment) and the equivalent JSON shape (for local-file or bootstrap remote configuration).

v1.24012.0

2026-07-21

| MDM key | Type | Description |
| --- | --- | --- |
| [`enduserAttribution`](https://claude.com/docs/third-party/claude-desktop/configuration#enduserattribution) | `boolean` | End-user attribution |
| [`userContentRendererUrl`](https://claude.com/docs/third-party/claude-desktop/configuration#usercontentrendererurl) | `string` | Artifact preview iframe origin |

**JSON (e.g. for non-MDM users or Bootstrap):**

```
{
  "deploymentDisplayName": "<string>",
  "deploymentDisplaySubtitle": "<string>",
  "enduserAttribution": "<boolean>",
  "userContentRendererUrl": "<string>"
}
```

v1.22209.3

2026-07-19

No configuration changes in this release.

v1.22209.0

2026-07-16

| MDM key | Type | Description |
| --- | --- | --- |
| [`otlpTracesEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#otlptracesenabled) | `boolean` | Export traces (beta) |

**JSON (e.g. for non-MDM users or Bootstrap):**

```
{
  "otlp": {
    "tracesEnabled": "<boolean>"
  }
}
```

v1.21459.3

2026-07-16

No configuration changes in this release.

v1.21459.0

2026-07-14

| MDM key | Type | Description |
| --- | --- | --- |
| [`disableFeatureDiscovery`](https://claude.com/docs/third-party/claude-desktop/configuration#disablefeaturediscovery) | `boolean` | Hide feature announcements |
| [`inferenceModels[].prefer1m`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencemodels) | `boolean` | New subfield: make the 1M-context variant the default picker selection when this model is the default entry. |
| [`managedMcpServers[].envHelper`](https://claude.com/docs/third-party/claude-desktop/configuration#managedmcpservers) | `string` | New subfield: helper executable that prints environment variables as JSON for a managed stdio server. |
| [`managedMcpServers[].envHelperTtlSec`](https://claude.com/docs/third-party/claude-desktop/configuration#managedmcpservers) | `integer` | New subfield: maximum age in seconds of a cached `envHelper` result (default 300). |
| [`managedMcpServers[].headersHelperRefreshBufferSec`](https://claude.com/docs/third-party/claude-desktop/configuration#managedmcpservers) | `integer` | New subfield: how many seconds before credential expiry the `headersHelper` re-runs (default 60). |
| [`toolSearchEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#toolsearchenabled) | `boolean` | Enable tool search |

**JSON (e.g. for non-MDM users or Bootstrap):**

```
{
  "featureDiscovery": {
    "disabled": "<boolean>"
  },
  "workspace": {
    "toolSearchEnabled": "<boolean>"
  }
}
```

**Changed:**

* `chatTabEnabled` and `chatAdvancedFileAnalysisEnabled` are no longer Beta: the Chat tab and advanced file analysis are generally available. Availability and defaults are unchanged, and both remain opt-in.
* `orgPluginSettings[].tools.permission` accepts a new `ask-session` value. In this release the value is accepted but behaves as `ask` (a prompt on every use); the once-per-session approval flow is not yet enabled.

v1.20186.9

2026-07-14

No configuration changes in this release.

v1.20186.0

2026-07-09

No configuration changes in this release.

v1.19367.0

2026-07-07

| MDM key | Type | Description |
| --- | --- | --- |
| [`inferenceFoundryAuthFlow`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencefoundryauthflow) | `enum` | Entra ID sign-in flow |
| [`microsoftAuthBroker`](https://claude.com/docs/third-party/claude-desktop/configuration#microsoftauthbroker) | `enum` | Microsoft 365 native sign-in broker |
| [`managedMcpServers[].startupTimeoutSec`](https://claude.com/docs/third-party/claude-desktop/configuration#managedmcpservers) | `integer` | New subfield: maximum wait in seconds for the server to start and list its tools. |

**JSON (e.g. for non-MDM users or Bootstrap):**

```
{
  "inference": {
    "credential": {
      "authFlow": "<device-code|browser>"
    }
  },
  "authentication": {
    "microsoftAuthBroker": "<auto|disabled>"
  }
}
```

**Changed:**

* `isDesktopExtensionEnabled` — default changed from `true` to `false`: Desktop Extensions (`.dxt`, `.mcpb`) no longer load unless explicitly enabled.
* `allowedPluginMarketplaces` (beta) — can now be delivered per-user through the bootstrap server; previously MDM-only.

v1.18286.2

2026-07-07

No configuration changes in this release.

v1.18286.0

2026-07-02

**Removed:**

* `disableDefaultPlugins` — third-party deployments always skip the default plugin marketplaces and standard deployments always include them, so the key no longer has an effect.

v1.17377.2

2026-07-01

No configuration changes in this release.

v1.17377.1

2026-06-30

| MDM key | Type | Description |
| --- | --- | --- |
| [`allowedPluginMarketplaces`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedpluginmarketplaces) | `object[]` | Admin-configured plugin marketplace git URLs appear under the Directory’s Organization tab. (MDM-only; not settable via bootstrap JSON.) |
| [`inferenceVertexWorkforceOidc.omitOfflineAccess`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencevertexworkforceoidc) | `boolean` | New subfield: omit `offline_access` from the OIDC scope request. |

**JSON (Non-MDM User, Bootstrap Remote):**

```
{
  "inference": {
    "credential": {
      "oidc": {
        "omitOfflineAccess": "<boolean>"
      }
    }
  }
}
```

v1.15962.2

2026-06-30

No configuration changes in this release.

v1.15962.1

2026-06-26

No configuration changes in this release.

v1.15962.0

2026-06-25

| MDM key | Type | Description |
| --- | --- | --- |
| [`otlpContentCapture`](https://claude.com/docs/third-party/claude-desktop/configuration#otlpcontentcapture) | `enum[]` | Content capture categories |
| [`disableBundledSkills`](https://claude.com/docs/third-party/claude-desktop/configuration#disablebundledskills) | `boolean` | Disable bundled skills and workflows |
| [`managedMcpServers[].server`](https://claude.com/docs/third-party/claude-desktop/configuration#managedmcpservers) | `enum` | Gained `"websearch"` — managed web search (Brave, Tavily, Exa or custom) |

**JSON (Non-MDM User, Bootstrap Remote):**

```
{
  "otlp": {
    "contentCapture": [
      "<userPrompts|assistantResponses|toolDetails|toolContent|rawApiBodies>"
    ]
  },
  "workspace": {
    "disableBundledSkills": "<boolean>"
  },
  "mcp": {
    "managedServers": [
      {
        "name": "Web search",
        "server": "websearch",
        "provider": "<brave|tavily|exa|custom>",
        "headers": { "<header-name>": "<string>" },
        "customUrl": "<string, provider=custom only>"
      }
    ]
  }
}
```

v1.15200.0

2026-06-23

No configuration changes in this release.

v1.14271.0

2026-06-18

| MDM key | Type | Description |
| --- | --- | --- |
| `chatAdvancedFileAnalysisEnabled` | `boolean` | Advanced file analysis |
| `inferenceSessionLifetimeSec` | `integer` | Sign-in session lifetime |

**JSON (Non-MDM User, Bootstrap Remote):**

```
{
  "chatSurface": {
    "advancedFileAnalysis": "<boolean>"
  },
  "inference": {
    "sessionLifetimeSec": "<integer>"
  }
}
```

**Deprecated:**

* `betaFeaturesEnabled` — Allow beta features (added and deprecated in this release)

v1.13576.0

2026-06-16

| MDM key | Type | Description |
| --- | --- | --- |
| `chatTabEnabled` | `boolean` | Allow Chat tab |
| `inferenceBedrockAwsCliPath` | `string` | AWS CLI path |

**JSON (Non-MDM User, Bootstrap Remote):**

```
{
  "chatSurface": {
    "enabled": "<boolean>"
  },
  "inference": {
    "awsEnv": {
      "awsCliPath": "<string>"
    }
  }
}
```

v1.12603.0

2026-06-11

| MDM key | Type | Description |
| --- | --- | --- |
| `inferenceVertexOAuthLoginHint` | `string` | Vertex OAuth login hint |

**JSON (Non-MDM User, Bootstrap Remote):**

```
{
  "inference": {
    "credential": {
      "loginHint": "<string>"
    }
  }
}
```

v1.10628.0

2026-06-03

| MDM key | Type | Description |
| --- | --- | --- |
| `inferenceVertexWorkforceAudience` | `string` | Workforce Identity audience |
| `inferenceVertexWorkforceUserProject` | `string` | Workforce Identity billing project |
| `inferenceVertexWorkforceOidc` | `object` | Workforce Identity IdP (OIDC) |
| `organizationPluginsUrl` | `string` | Organization plugins endpoint |
| `autoModeEnabled` | `boolean` | Allow Auto mode |
| `inferenceCredentialHelperSilentRefreshEnabled` | `boolean` | Re-run helper for silent refresh |
| `bootstrapEnabled` | `boolean` | Use bootstrap config |
| `bootstrapUrl` | `string` | Bootstrap config URL |
| `bootstrapOidc` | `object` | Bootstrap OIDC parameters |

**JSON (Non-MDM User, Bootstrap Remote):**

```
{
  "inference": {
    "credential": {
      "audience": "<string>",
      "userProject": "<string>",
      "oidc": {
        "issuer": "<string>",
        "authorizationUrl": "<string>",
        "tokenUrl": "<string>",
        "clientId": "<string>",
        "scopes": "<string>",
        "redirectPort": "<integer>"
      },
      "silentRefreshEnabled": "<boolean>"
    }
  }
}
```

v1.9659.0

2026-06-02

| MDM key | Type | Description |
| --- | --- | --- |
| `coworkTabEnabled` | `boolean` | Allow Cowork tab |

**JSON (Non-MDM User, Bootstrap Remote):**

```
{
  "coworkSurface": {
    "enabled": "<boolean>"
  }
}
```

v1.9255.0

2026-05-27

| MDM key | Type | Description |
| --- | --- | --- |
| `otlpDesktopLogLevel` | `enum` | Desktop telemetry export level |
| `inferenceFoundryTenantId` | `string` | Entra ID tenant ID |
| `inferenceFoundryClientId` | `string` | Entra ID client ID |

**JSON (Non-MDM User, Bootstrap Remote):**

```
{
  "otlp": {
    "desktopLogLevel": "<off|error|warn|info|debug>"
  },
  "inference": {
    "credential": {
      "tenantId": "<string>",
      "clientId": "<string>"
    }
  }
}
```

v1.8555.0

2026-05-25

| MDM key | Type | Description |
| --- | --- | --- |
| `inferenceCredentialKind` | `enum` | Credential kind |

**JSON (Non-MDM User, Bootstrap Remote):**

```
{
  "inference": {
    "credential": {
      "kind": "<static|helper-script|interactive|vendor-profile>"
    }
  }
}
```

v1.8089.0

2026-05-19

| MDM key | Type | Description |
| --- | --- | --- |
| `inferenceAnthropicApiKey` | `string` | Claude API key |
| `inferenceCustomHeaders` | `object` | Custom inference headers (renamed from `inferenceGatewayHeaders`) |
| `modelDiscoveryEnabled` | `boolean` | Model discovery |
| `orgPluginSettings` | `object` | Organization plugin settings |
| `builtinToolPolicy` | `object` | Built-in tool policy |
| `inferenceCredentialHelperTimeoutSec` | `integer` | Credential helper timeout |

**JSON (Non-MDM User, Bootstrap Remote):**

```
{
  "inference": {
    "credential": {
      "apiKey": "<string>",
      "timeoutSec": "<integer>"
    },
    "customHeaders": "<object>"
  }
}
```

v1.7196.0

2026-05-16

| MDM key | Type | Description |
| --- | --- | --- |
| `banner` | `object` | Organization banner |

v1.6889.0

2026-05-08

| MDM key | Type | Description |
| --- | --- | --- |
| `disableDeepLinkRegistration` | `boolean` | Disable claude:// deep-link handling |
| `inferenceGatewayOidc` | `object` | Gateway SSO IdP (OIDC) |

**JSON (Non-MDM User, Bootstrap Remote):**

```
{
  "inference": {
    "credential": {
      "oidc": {
        "issuer": "<string>",
        "authorizationUrl": "<string>",
        "tokenUrl": "<string>",
        "clientId": "<string>",
        "scopes": "<string>",
        "redirectPort": "<integer>",
        "bearerTokenType": "<id_token|access_token>",
        "appendOfflineAccess": "<boolean>"
      }
    }
  }
}
```

v1.6259.0

2026-05-06

| MDM key | Type | Description |
| --- | --- | --- |
| `inferenceBedrockSsoStartUrl` | `string` | AWS SSO start URL |
| `inferenceBedrockSsoRegion` | `string` | AWS SSO region |
| `inferenceBedrockSsoAccountId` | `string` | AWS SSO account ID |
| `inferenceBedrockSsoRoleName` | `string` | AWS SSO role name |

**JSON (Non-MDM User, Bootstrap Remote):**

```
{
  "inference": {
    "credential": {
      "ssoStartUrl": "<string>",
      "ssoRegion": "<string>",
      "ssoAccountId": "<string>",
      "ssoRoleName": "<string>"
    }
  }
}
```

v1.5354.0

2026-04-29

| MDM key | Type | Description |
| --- | --- | --- |
| `otlpResourceAttributes` | `object` | OpenTelemetry resource attributes |

**JSON (Non-MDM User, Bootstrap Remote):**

```
{
  "otlp": {
    "resourceAttributes": "<object>"
  }
}
```

v1.5186.0

2026-04-28

| MDM key | Type | Description |
| --- | --- | --- |
| `inferenceBedrockServiceTier` | `enum` | Bedrock service tier |

**JSON (Non-MDM User, Bootstrap Remote):**

```
{
  "inference": {
    "serviceTier": "<flex|priority>"
  }
}
```

v1.3834.0

2026-04-21

| MDM key | Type | Description |
| --- | --- | --- |
| `disableDeploymentModeChooser` | `boolean` | Disable Claude.ai sign-in |

v1.3036.0

2026-04-16

| MDM key | Type | Description |
| --- | --- | --- |
| `inferenceGatewayAuthScheme` | `enum` | Gateway auth scheme |

**JSON (Non-MDM User, Bootstrap Remote):**

```
{
  "inference": {
    "credential": {
      "authScheme": "<auto|x-api-key|bearer|sso>"
    }
  }
}
```

Baseline

| MDM key | Type | Description |
| --- | --- | --- |
| `isDesktopExtensionEnabled` | `boolean` | Allow desktop extensions (renamed from `isDxtEnabled`) |
| `isDesktopExtensionSignatureRequired` | `boolean` | Require signed extensions (renamed from `isDxtSignatureRequired`) |
| `isLocalDevMcpEnabled` | `boolean` | Allow user-added MCP servers |
| `isClaudeCodeForDesktopEnabled` | `boolean` | Allow Claude Code tab |
| `coworkEgressAllowedHosts` | `array<string>` | Allowed egress hosts |
| `otlpEndpoint` | `string` | OpenTelemetry collector endpoint |
| `otlpProtocol` | `enum` | OpenTelemetry exporter protocol |
| `otlpHeaders` | `object` | OpenTelemetry exporter headers |
| `autoUpdaterEnforcementHours` | `integer` | Auto-update enforcement window |
| `disableAutoUpdates` | `boolean` | Block auto-updates |
| `inferenceProvider` | `enum` | Inference provider |
| `inferenceGatewayBaseUrl` | `string` | Gateway base URL |
| `inferenceGatewayApiKey` | `string` | Gateway API key |
| `inferenceVertexProjectId` | `string` | GCP project ID |
| `inferenceVertexRegion` | `string` | GCP region |
| `inferenceVertexCredentialsFile` | `string` | GCP credentials file path |
| `inferenceVertexOAuthClientId` | `string` | Vertex OAuth client ID |
| `inferenceVertexOAuthClientSecret` | `string` | Vertex OAuth client secret |
| `inferenceVertexOAuthScopes` | `string` | Vertex OAuth scopes |
| `inferenceVertexBaseUrl` | `string` | Vertex AI base URL |
| `inferenceBedrockRegion` | `string` | AWS region |
| `inferenceBedrockBearerToken` | `string` | AWS bearer token |
| `inferenceBedrockBaseUrl` | `string` | Bedrock base URL |
| `inferenceBedrockProfile` | `string` | AWS profile name |
| `inferenceBedrockAwsDir` | `string` | AWS config directory |
| `inferenceFoundryResource` | `string` | Azure AI Foundry resource name |
| `inferenceFoundryApiKey` | `string` | Azure AI Foundry API key |
| `inferenceModels` | `array<string|object>` | Model list |
| `deploymentOrganizationUuid` | `string` | Organization UUID |
| `disableEssentialTelemetry` | `boolean` | Block essential telemetry |
| `disableNonessentialTelemetry` | `boolean` | Block nonessential telemetry |
| `disableNonessentialServices` | `boolean` | Block nonessential services |
| `managedMcpServers` | `array<object|object|object|null>` | Managed MCP servers |
| `disabledBuiltinTools` | `array<string>` | Disabled built-in tools |
| `allowedWorkspaceFolders` | `array<string|object>` | Allowed workspace folders |
| `inferenceCredentialHelper` | `string` | Helper script |
| `inferenceCredentialHelperTtlSec` | `integer` | Helper script TTL |
| `inferenceMaxTokensPerWindow` | `integer` | Max tokens per window |
| `inferenceTokenWindowHours` | `integer` | Token cap window |

**Deprecated:**

* `requireCoworkFullVmSandbox` — Require full VM sandbox
