<!-- source: https://claude.com/docs/third-party/claude-desktop/configuration-changelog -->

Configuration keys by Claude Desktop release. Each section lists keys added in that release, with the MDM key name (for plist/registry deployment) and the equivalent JSON shape (for local-file or bootstrap remote configuration).

1.15962

| MDM key | Type | Description |
| --- | --- | --- |
| [`otlpContentCapture`](/docs/third-party/claude-desktop/configuration#otlpcontentcapture) | `enum[]` | Content capture categories |
| [`disableBundledSkills`](/docs/third-party/claude-desktop/configuration#disablebundledskills) | `boolean` | Disable bundled skills and workflows |
| [`managedMcpServers[].server`](/docs/third-party/claude-desktop/configuration#managedmcpservers) | `enum` | Gained `"websearch"` — managed web search (Brave, Tavily, Exa or custom) |

**JSON (Non-MDM User, Bootstrap Remote):**

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

1.15200

No configuration changes in this release.

1.14271

| MDM key | Type | Description |
| --- | --- | --- |
| `chatAdvancedFileAnalysisEnabled` | `boolean` | Advanced file analysis |
| `inferenceSessionLifetimeSec` | `integer` | Sign-in session lifetime |

**JSON (Non-MDM User, Bootstrap Remote):**

{
  "chatSurface": {
    "advancedFileAnalysis": "<boolean>"
  },
  "inference": {
    "sessionLifetimeSec": "<integer>"
  }
}

**Deprecated:**

* `betaFeaturesEnabled` — Allow beta features (added and deprecated in this release)

1.13576

| MDM key | Type | Description |
| --- | --- | --- |
| `chatTabEnabled` | `boolean` | Allow Chat tab |
| `inferenceBedrockAwsCliPath` | `string` | AWS CLI path |

**JSON (Non-MDM User, Bootstrap Remote):**

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

1.12603

| MDM key | Type | Description |
| --- | --- | --- |
| `inferenceVertexOAuthLoginHint` | `string` | Vertex OAuth login hint |

**JSON (Non-MDM User, Bootstrap Remote):**

{
  "inference": {
    "credential": {
      "loginHint": "<string>"
    }
  }
}

1.10628

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

1.9659

| MDM key | Type | Description |
| --- | --- | --- |
| `coworkTabEnabled` | `boolean` | Allow Cowork tab |

**JSON (Non-MDM User, Bootstrap Remote):**

{
  "coworkSurface": {
    "enabled": "<boolean>"
  }
}

1.9255

| MDM key | Type | Description |
| --- | --- | --- |
| `otlpDesktopLogLevel` | `enum` | Desktop telemetry export level |
| `inferenceFoundryTenantId` | `string` | Entra ID tenant ID |
| `inferenceFoundryClientId` | `string` | Entra ID client ID |

**JSON (Non-MDM User, Bootstrap Remote):**

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

1.8555

| MDM key | Type | Description |
| --- | --- | --- |
| `inferenceCredentialKind` | `enum` | Credential kind |

**JSON (Non-MDM User, Bootstrap Remote):**

{
  "inference": {
    "credential": {
      "kind": "<static|helper-script|interactive|vendor-profile>"
    }
  }
}

1.8089

| MDM key | Type | Description |
| --- | --- | --- |
| `inferenceAnthropicApiKey` | `string` | Claude API key |
| `inferenceCustomHeaders` | `object` | Custom inference headers (renamed from `inferenceGatewayHeaders`) |
| `modelDiscoveryEnabled` | `boolean` | Model discovery |
| `orgPluginSettings` | `object` | Organization plugin settings |
| `builtinToolPolicy` | `object` | Built-in tool policy |
| `inferenceCredentialHelperTimeoutSec` | `integer` | Credential helper timeout |

**JSON (Non-MDM User, Bootstrap Remote):**

{
  "inference": {
    "credential": {
      "apiKey": "<string>",
      "timeoutSec": "<integer>"
    },
    "customHeaders": "<object>"
  }
}

1.7196

| MDM key | Type | Description |
| --- | --- | --- |
| `banner` | `object` | Organization banner |

1.6889

| MDM key | Type | Description |
| --- | --- | --- |
| `disableDeepLinkRegistration` | `boolean` | Disable claude:// deep-link handling |
| `inferenceGatewayOidc` | `object` | Gateway SSO IdP (OIDC) |

**JSON (Non-MDM User, Bootstrap Remote):**

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

1.6259

| MDM key | Type | Description |
| --- | --- | --- |
| `inferenceBedrockSsoStartUrl` | `string` | AWS SSO start URL |
| `inferenceBedrockSsoRegion` | `string` | AWS SSO region |
| `inferenceBedrockSsoAccountId` | `string` | AWS SSO account ID |
| `inferenceBedrockSsoRoleName` | `string` | AWS SSO role name |

**JSON (Non-MDM User, Bootstrap Remote):**

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

1.5354

| MDM key | Type | Description |
| --- | --- | --- |
| `otlpResourceAttributes` | `object` | OpenTelemetry resource attributes |

**JSON (Non-MDM User, Bootstrap Remote):**

{
  "otlp": {
    "resourceAttributes": "<object>"
  }
}

1.5186

| MDM key | Type | Description |
| --- | --- | --- |
| `inferenceBedrockServiceTier` | `enum` | Bedrock service tier |

**JSON (Non-MDM User, Bootstrap Remote):**

{
  "inference": {
    "serviceTier": "<flex|priority>"
  }
}

1.3834

| MDM key | Type | Description |
| --- | --- | --- |
| `disableDeploymentModeChooser` | `boolean` | Disable Claude.ai sign-in |

1.3036

| MDM key | Type | Description |
| --- | --- | --- |
| `inferenceGatewayAuthScheme` | `enum` | Gateway auth scheme |

**JSON (Non-MDM User, Bootstrap Remote):**

{
  "inference": {
    "credential": {
      "authScheme": "<auto|x-api-key|bearer|sso>"
    }
  }
}

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

[Configuration reference](/docs/third-party/claude-desktop/configuration)[Per-user configuration with a bootstrap server](/docs/third-party/claude-desktop/bootstrap)
