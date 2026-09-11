<!-- source: https://platform.claude.com/docs/en/api/csharp/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/csharp/beta -->

<!-- chunk-start -->

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

  - `string workspaceID`

    Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `JsonElement Type = "tunnel_certificate"`

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

#### Example

```csharp
CertificateListParams parameters = new() { TunnelID = "tunnel_id" };

var page = await client.Beta.Tunnels.Certificates.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "expires_at": "2019-12-27T18:11:19.117Z",
      "fingerprint": "fingerprint",
      "tunnel_id": "tunnel_id",
      "type": "tunnel_certificate"
    }
  ],
  "next_page": "next_page"
}
```

### Archive Tunnel Certificate

`BetaTunnelCertificate Beta.Tunnels.Certificates.Archive(parameters, cancellationToken = default)`

**POST** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

#### Parameters

- `CertificateArchiveParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `required string certificateID`

    Path param: Path parameter certificate_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

  - `string workspaceID`

    Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `JsonElement Type = "tunnel_certificate"`

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

#### Example

```csharp
CertificateArchiveParams parameters = new()
{
    TunnelID = "tunnel_id",
    CertificateID = "certificate_id",
};

var betaTunnelCertificate = await client.Beta.Tunnels.Certificates.Archive(parameters);

Console.WriteLine(betaTunnelCertificate);
```

##### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

## Beta › Organization

### Get Current Organization

`BetaOrganization Beta.Organization.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/me`

Retrieve information about the organization associated with the authenticated API key.

#### Parameters

- `OrganizationRetrieveParams parameters`

#### Returns

- `class BetaOrganization:`

  - `JsonElement Type = "organization"`

    Object type.

    For Organizations, this is always `"organization"`.

  - `required string ID`

    ID of the Organization.

    format: uuid

  - `required string Name`

    Name of the Organization.

#### Example

```csharp
OrganizationRetrieveParams parameters = new();

var betaOrganization = await client.Beta.Organization.Retrieve(parameters);

Console.WriteLine(betaOrganization);
```

##### Response (200)

```json
{
  "id": "12345678-1234-5678-1234-567812345678",
  "name": "Organization Name",
  "type": "organization"
}
```

## Beta › Organization › API Keys

### List API Keys

`ApiKeyListPage Beta.Organization.ApiKeys.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/api_keys`

List API Keys

#### Parameters

- `ApiKeyListParams parameters`

  - `string afterID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `string? createdByUserID`

    Filter by the ID of the User who created the object.

  - `long limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

  - `Status? status`

    Filter by API key status.

    - `Active("active")`

    - `Archived("archived")`

    - `Expired("expired")`

    - `Inactive("inactive")`

  - `string? workspaceID`

    Filter by Workspace ID.

#### Returns

- `class BetaApiKey:`

  - `JsonElement Type = "api_key"`

    Object type.

    For API Keys, this is always `"api_key"`.

  - `required string ID`

    ID of the API key.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the API Key was created.

    format: date-time

  - `required BetaApiKeyCreatedBy? CreatedBy`

    The ID and type of the actor that created the API key, or `null` when the
    creator is not recorded (legacy, workload-identity-federated, or
    system-created keys).

    - `required Type Type`

      Type of the actor that created the object.

      - `ServiceAccount("service_account")`

      - `User("user")`

    - `required string ID`

      ID of the actor that created the object.

  - `required DateTimeOffset? ExpiresAt`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

    format: date-time

  - `required string Name`

    Name of the API key.

  - `required string? PartialKeyHint`

    Partially redacted hint for the API key.

  - `required Principal? Principal`

    The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

    - `class BetaApiKeyUserActor:`

      - `JsonElement Type = "user_actor"`

        Principal type. Always `"user_actor"` for a User.

      - `required string UserID`

        ID of the User the API key acts as.

    - `class BetaApiKeyServiceAccountActor:`

      - `JsonElement Type = "service_account_actor"`

        Principal type. Always `"service_account_actor"` for a Service Account.

      - `required string ServiceAccountID`

        ID of the Service Account the API key acts as.

  - `required Scope Scope`

    Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

    - `class BetaApiKeyOrganizationScope:`

      - `JsonElement Type = "organization"`

        Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

    - `class BetaApiKeyWorkspaceScope:`

      - `JsonElement Type = "workspace"`

        Scope type. Always `"workspace"`: the API key belongs to one Workspace.

      - `required string WorkspaceID`

        ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.

  - `required Status Status`

    Status of the API key.

    - `Active("active")`

    - `Archived("archived")`

    - `Expired("expired")`

    - `Inactive("inactive")`

  - `required string? WorkspaceID`

    **Deprecated**: Use `scope` instead. `workspace_id` is `null` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

    Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

#### Example

```csharp
ApiKeyListParams parameters = new();

var page = await client.Beta.Organization.ApiKeys.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "type": "user"
      },
      "expires_at": "2024-10-30T23:58:27.427722Z",
      "name": "Developer Key",
      "partial_key_hint": "sk-ant-api03-R2D...igAA",
      "principal": {
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "scope": {
        "type": "workspace",
        "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
      },
      "status": "active",
      "type": "api_key",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Retrieve API Key (Admin API)

`BetaApiKey Beta.Organization.ApiKeys.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/api_keys/{api_key_id}`

Retrieve information about a single API key in your organization, looked up by its ID. This Admin API endpoint requires an Admin API key, is intended for programmatic key management, and never returns the key's secret value. To view or create your own API keys, go to [API keys](https://platform.claude.com/settings/keys) in the Claude Console.

#### Parameters

- `ApiKeyRetrieveParams parameters`

  - `required string apiKeyID`

    ID of the API key.

#### Returns

- `class BetaApiKey:`

  - `JsonElement Type = "api_key"`

    Object type.

    For API Keys, this is always `"api_key"`.

  - `required string ID`

    ID of the API key.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the API Key was created.

    format: date-time

  - `required BetaApiKeyCreatedBy? CreatedBy`

    The ID and type of the actor that created the API key, or `null` when the
    creator is not recorded (legacy, workload-identity-federated, or
    system-created keys).

    - `required Type Type`

      Type of the actor that created the object.

      - `ServiceAccount("service_account")`

      - `User("user")`

    - `required string ID`

      ID of the actor that created the object.

  - `required DateTimeOffset? ExpiresAt`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

    format: date-time

  - `required string Name`

    Name of the API key.

  - `required string? PartialKeyHint`

    Partially redacted hint for the API key.

  - `required Principal? Principal`

    The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

    - `class BetaApiKeyUserActor:`

      - `JsonElement Type = "user_actor"`

        Principal type. Always `"user_actor"` for a User.

      - `required string UserID`

        ID of the User the API key acts as.

    - `class BetaApiKeyServiceAccountActor:`

      - `JsonElement Type = "service_account_actor"`

        Principal type. Always `"service_account_actor"` for a Service Account.

      - `required string ServiceAccountID`

        ID of the Service Account the API key acts as.

  - `required Scope Scope`

    Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

    - `class BetaApiKeyOrganizationScope:`

      - `JsonElement Type = "organization"`

        Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

    - `class BetaApiKeyWorkspaceScope:`

      - `JsonElement Type = "workspace"`

        Scope type. Always `"workspace"`: the API key belongs to one Workspace.

      - `required string WorkspaceID`

        ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.

  - `required Status Status`

    Status of the API key.

    - `Active("active")`

    - `Archived("archived")`

    - `Expired("expired")`

    - `Inactive("inactive")`

  - `required string? WorkspaceID`

    **Deprecated**: Use `scope` instead. `workspace_id` is `null` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

    Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

#### Example

```csharp
ApiKeyRetrieveParams parameters = new() { ApiKeyID = "api_key_id" };

var betaApiKey = await client.Beta.Organization.ApiKeys.Retrieve(parameters);

Console.WriteLine(betaApiKey);
```

##### Response (200)

```json
{
  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "principal": {
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "scope": {
    "type": "workspace",
    "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  },
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

### Update API Key

`BetaApiKey Beta.Organization.ApiKeys.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/api_keys/{api_key_id}`

Update API Key

#### Parameters

- `ApiKeyUpdateParams parameters`

  - `required string apiKeyID`

    ID of the API key.

  - `string? name`

    Name of the API key.

    maxLength: 500, minLength: 1

  - `Status? status`

    Status of the API key.

    - `Active("active")`

    - `Archived("archived")`

    - `Inactive("inactive")`

#### Returns

- `class BetaApiKey:`

  - `JsonElement Type = "api_key"`

    Object type.

    For API Keys, this is always `"api_key"`.

  - `required string ID`

    ID of the API key.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the API Key was created.

    format: date-time

  - `required BetaApiKeyCreatedBy? CreatedBy`

    The ID and type of the actor that created the API key, or `null` when the
    creator is not recorded (legacy, workload-identity-federated, or
    system-created keys).

    - `required Type Type`

      Type of the actor that created the object.

      - `ServiceAccount("service_account")`

      - `User("user")`

    - `required string ID`

      ID of the actor that created the object.

  - `required DateTimeOffset? ExpiresAt`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

    format: date-time

  - `required string Name`

    Name of the API key.

  - `required string? PartialKeyHint`

    Partially redacted hint for the API key.

  - `required Principal? Principal`

    The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

    - `class BetaApiKeyUserActor:`

      - `JsonElement Type = "user_actor"`

        Principal type. Always `"user_actor"` for a User.

      - `required string UserID`

        ID of the User the API key acts as.

    - `class BetaApiKeyServiceAccountActor:`

      - `JsonElement Type = "service_account_actor"`

        Principal type. Always `"service_account_actor"` for a Service Account.

      - `required string ServiceAccountID`

        ID of the Service Account the API key acts as.

  - `required Scope Scope`

    Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

    - `class BetaApiKeyOrganizationScope:`

      - `JsonElement Type = "organization"`

        Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

    - `class BetaApiKeyWorkspaceScope:`

      - `JsonElement Type = "workspace"`

        Scope type. Always `"workspace"`: the API key belongs to one Workspace.

      - `required string WorkspaceID`

        ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.

  - `required Status Status`

    Status of the API key.

    - `Active("active")`

    - `Archived("archived")`

    - `Expired("expired")`

    - `Inactive("inactive")`

  - `required string? WorkspaceID`

    **Deprecated**: Use `scope` instead. `workspace_id` is `null` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

    Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

#### Example

```csharp
ApiKeyUpdateParams parameters = new() { ApiKeyID = "api_key_id" };

var betaApiKey = await client.Beta.Organization.ApiKeys.Update(parameters);

Console.WriteLine(betaApiKey);
```

##### Response (200)

```json
{
  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "principal": {
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "scope": {
    "type": "workspace",
    "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  },
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

## Beta › Organization › External Keys

### Create External Key

`BetaExternalKey Beta.Organization.ExternalKeys.Create(parameters, cancellationToken = default)`

**POST** `/v1/organizations/external_keys`

Create an external key config owned by the caller's organization.

#### Parameters

- `ExternalKeyCreateParams parameters`

  - `required ProviderConfig providerConfig`

    KMS provider identity and auth coordinates.

    - `class BetaAwsExternalKeyConfig:`

      - `JsonElement Type = "aws"`

      - `required string KmsArn`

        Full ARN of the AWS KMS key. On Claude Platform on AWS the key must be a single-Region key in your organization's own AWS account; cross-account keys, multi-Region keys, and alias ARNs are rejected.

        maxLength: 2048

      - `string? Region`

        AWS region. Derived from `kms_arn` if omitted.

      - `string? RoleArn`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key through its own intermediate role (or, on Claude Platform on AWS, with credentials AWS issues for the Workspace); this field is ignored.

    - `class BetaGcpExternalKeyConfig:`

      - `JsonElement Type = "gcp"`

      - `required string KeyName`

        Full resource name of the Cloud KMS key.

    - `class BetaAzureExternalKeyConfigParam:`

      Azure Key Vault provider configuration.

      - `JsonElement Type = "azure"`

      - `required string KeyName`

        Name of the key within the vault.

      - `required string TenantID`

        Azure AD tenant ID.

      - `required string VaultUri`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `string? ClientID`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `string? displayName`

    Human-friendly display name.

    maxLength: 255, minLength: 1

  - `Geo geo`

    Data residency geo. Only `us` is supported.

    - `Us("us")`

#### Returns

- `class BetaExternalKey:`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `JsonElement Type = "external_key"`

  - `required string ID`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `required Attachment Attachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `class BetaExternalKeyAttachedAttachment:`

      - `JsonElement Type = "attached"`

    - `class BetaExternalKeyUnattachedAttachment:`

      - `JsonElement Type = "unattached"`

  - `required DateTimeOffset CreatedAt`

    format: date-time

  - `required string? DisplayName`

    Human-friendly display name. Null if none was set.

  - `required string Geo`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `required ProviderConfig ProviderConfig`

    KMS provider identity and auth coordinates.

    - `class BetaAwsExternalKeyConfig:`

      - `JsonElement Type = "aws"`

      - `required string KmsArn`

        Full ARN of the AWS KMS key. On Claude Platform on AWS the key must be a single-Region key in your organization's own AWS account; cross-account keys, multi-Region keys, and alias ARNs are rejected.

        maxLength: 2048

      - `string? Region`

        AWS region. Derived from `kms_arn` if omitted.

      - `string? RoleArn`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key through its own intermediate role (or, on Claude Platform on AWS, with credentials AWS issues for the Workspace); this field is ignored.

    - `class BetaGcpExternalKeyConfig:`

      - `JsonElement Type = "gcp"`

      - `required string KeyName`

        Full resource name of the Cloud KMS key.

    - `class BetaAzureExternalKeyConfig:`

      - `JsonElement Type = "azure"`

      - `required string KeyName`

        Name of the key within the vault.

      - `required string TenantID`

        Azure AD tenant ID.

      - `required string VaultUri`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `string? ClientID`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `required DateTimeOffset UpdatedAt`

    format: date-time

#### Example

```csharp
ExternalKeyCreateParams parameters = new()
{
    ProviderConfig = new BetaAwsExternalKeyConfig()
    {
        KmsArn = "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
        Region = "us-east-1",
        RoleArn = "arn:aws:iam::111122223333:role/anthropic-cmek",
    },
};

var betaExternalKey = await client.Beta.Organization.ExternalKeys.Create(parameters);

Console.WriteLine(betaExternalKey);
```

##### Response (200)

```json
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "attachment": {
    "type": "attached"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "type": "aws",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### List External Keys

`ExternalKeyListPage Beta.Organization.ExternalKeys.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/external_keys`

List external key configs in the caller's organization.

Results are ordered by creation time (newest first). Use the
`next_page` cursor from the response to fetch subsequent pages.

#### Parameters

- `ExternalKeyListParams parameters`

  - `long limit`

    Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Opaque cursor from a previous response's `next_page`.

#### Returns

- `class BetaExternalKey:`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `JsonElement Type = "external_key"`

  - `required string ID`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `required Attachment Attachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `class BetaExternalKeyAttachedAttachment:`

      - `JsonElement Type = "attached"`

    - `class BetaExternalKeyUnattachedAttachment:`

      - `JsonElement Type = "unattached"`

  - `required DateTimeOffset CreatedAt`

    format: date-time

  - `required string? DisplayName`

    Human-friendly display name. Null if none was set.

  - `required string Geo`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `required ProviderConfig ProviderConfig`

    KMS provider identity and auth coordinates.

    - `class BetaAwsExternalKeyConfig:`

      - `JsonElement Type = "aws"`

      - `required string KmsArn`

        Full ARN of the AWS KMS key. On Claude Platform on AWS the key must be a single-Region key in your organization's own AWS account; cross-account keys, multi-Region keys, and alias ARNs are rejected.

        maxLength: 2048

      - `string? Region`

        AWS region. Derived from `kms_arn` if omitted.

      - `string? RoleArn`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key through its own intermediate role (or, on Claude Platform on AWS, with credentials AWS issues for the Workspace); this field is ignored.

    - `class BetaGcpExternalKeyConfig:`

      - `JsonElement Type = "gcp"`

      - `required string KeyName`

        Full resource name of the Cloud KMS key.

    - `class BetaAzureExternalKeyConfig:`

      - `JsonElement Type = "azure"`

      - `required string KeyName`

        Name of the key within the vault.

      - `required string TenantID`

        Azure AD tenant ID.

      - `required string VaultUri`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `string? ClientID`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `required DateTimeOffset UpdatedAt`

    format: date-time

#### Example

```csharp
ExternalKeyListParams parameters = new();

var page = await client.Beta.Organization.ExternalKeys.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
      "attachment": {
        "type": "attached"
      },
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "prod-us-key",
      "geo": "us",
      "provider_config": {
        "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
        "type": "aws",
        "region": "us-east-1",
        "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
      },
      "type": "external_key",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "next_page": "next_page"
}
```

### Get External Key

`BetaExternalKey Beta.Organization.ExternalKeys.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/external_keys/{external_key_id}`

Retrieve a single external key config in the caller's organization by ID.

#### Parameters

- `ExternalKeyRetrieveParams parameters`

  - `required string externalKeyID`

    ID of the External Key.

    maxLength: 2048

#### Returns

- `class BetaExternalKey:`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `JsonElement Type = "external_key"`

  - `required string ID`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `required Attachment Attachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `class BetaExternalKeyAttachedAttachment:`

      - `JsonElement Type = "attached"`

    - `class BetaExternalKeyUnattachedAttachment:`

      - `JsonElement Type = "unattached"`

  - `required DateTimeOffset CreatedAt`

    format: date-time

  - `required string? DisplayName`

    Human-friendly display name. Null if none was set.

  - `required string Geo`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `required ProviderConfig ProviderConfig`

    KMS provider identity and auth coordinates.

    - `class BetaAwsExternalKeyConfig:`

      - `JsonElement Type = "aws"`

      - `required string KmsArn`

        Full ARN of the AWS KMS key. On Claude Platform on AWS the key must be a single-Region key in your organization's own AWS account; cross-account keys, multi-Region keys, and alias ARNs are rejected.

        maxLength: 2048

      - `string? Region`

        AWS region. Derived from `kms_arn` if omitted.

      - `string? RoleArn`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key through its own intermediate role (or, on Claude Platform on AWS, with credentials AWS issues for the Workspace); this field is ignored.

    - `class BetaGcpExternalKeyConfig:`

      - `JsonElement Type = "gcp"`

      - `required string KeyName`

        Full resource name of the Cloud KMS key.

    - `class BetaAzureExternalKeyConfig:`

      - `JsonElement Type = "azure"`

      - `required string KeyName`

        Name of the key within the vault.

      - `required string TenantID`

        Azure AD tenant ID.

      - `required string VaultUri`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `string? ClientID`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `required DateTimeOffset UpdatedAt`

    format: date-time

#### Example

```csharp
ExternalKeyRetrieveParams parameters = new()
{
    ExternalKeyID = "external_key_id"
};

var betaExternalKey = await client.Beta.Organization.ExternalKeys.Retrieve(parameters);

Console.WriteLine(betaExternalKey);
```

##### Response (200)

```json
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "attachment": {
    "type": "attached"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "type": "aws",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### Update External Key

`BetaExternalKey Beta.Organization.ExternalKeys.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/external_keys/{external_key_id}`

Partially update an external key config. Omitted fields are left unchanged.

`display_name` is always editable. `geo` and `provider_config` cannot
be changed once any workspace references this config, because previously
encrypted data requires the original key identity to decrypt.

#### Parameters

- `ExternalKeyUpdateParams parameters`

  - `required string externalKeyID`

    ID of the External Key.

    maxLength: 2048

  - `string? displayName`

    Human-friendly display name.

    maxLength: 255, minLength: 1

  - `Geo? geo`

    Data residency geo. Only `us` is supported.

    - `Us("us")`

  - `ProviderConfig? providerConfig`

    KMS provider identity and auth coordinates.

    - `class BetaAwsExternalKeyConfig:`

      - `JsonElement Type = "aws"`

      - `required string KmsArn`

        Full ARN of the AWS KMS key. On Claude Platform on AWS the key must be a single-Region key in your organization's own AWS account; cross-account keys, multi-Region keys, and alias ARNs are rejected.

        maxLength: 2048

      - `string? Region`

        AWS region. Derived from `kms_arn` if omitted.

      - `string? RoleArn`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key through its own intermediate role (or, on Claude Platform on AWS, with credentials AWS issues for the Workspace); this field is ignored.

    - `class BetaGcpExternalKeyConfig:`

      - `JsonElement Type = "gcp"`

      - `required string KeyName`

        Full resource name of the Cloud KMS key.

    - `class BetaAzureExternalKeyConfigParam:`

      Azure Key Vault provider configuration.

      - `JsonElement Type = "azure"`

      - `required string KeyName`

        Name of the key within the vault.

      - `required string TenantID`

        Azure AD tenant ID.

      - `required string VaultUri`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `string? ClientID`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

#### Returns

- `class BetaExternalKey:`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `JsonElement Type = "external_key"`

  - `required string ID`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `required Attachment Attachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `class BetaExternalKeyAttachedAttachment:`

      - `JsonElement Type = "attached"`

    - `class BetaExternalKeyUnattachedAttachment:`

      - `JsonElement Type = "unattached"`

  - `required DateTimeOffset CreatedAt`

    format: date-time

  - `required string? DisplayName`

    Human-friendly display name. Null if none was set.

  - `required string Geo`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `required ProviderConfig ProviderConfig`

    KMS provider identity and auth coordinates.

    - `class BetaAwsExternalKeyConfig:`

      - `JsonElement Type = "aws"`

      - `required string KmsArn`

        Full ARN of the AWS KMS key. On Claude Platform on AWS the key must be a single-Region key in your organization's own AWS account; cross-account keys, multi-Region keys, and alias ARNs are rejected.

        maxLength: 2048

      - `string? Region`

        AWS region. Derived from `kms_arn` if omitted.

      - `string? RoleArn`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key through its own intermediate role (or, on Claude Platform on AWS, with credentials AWS issues for the Workspace); this field is ignored.

    - `class BetaGcpExternalKeyConfig:`

      - `JsonElement Type = "gcp"`

      - `required string KeyName`

        Full resource name of the Cloud KMS key.

    - `class BetaAzureExternalKeyConfig:`

      - `JsonElement Type = "azure"`

      - `required string KeyName`

        Name of the key within the vault.

      - `required string TenantID`

        Azure AD tenant ID.

      - `required string VaultUri`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `string? ClientID`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `required DateTimeOffset UpdatedAt`

    format: date-time

#### Example

```csharp
ExternalKeyUpdateParams parameters = new()
{
    ExternalKeyID = "external_key_id"
};

var betaExternalKey = await client.Beta.Organization.ExternalKeys.Update(parameters);

Console.WriteLine(betaExternalKey);
```

##### Response (200)

```json
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "attachment": {
    "type": "attached"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "type": "aws",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### Delete External Key

`ExternalKeyDeleteResponse Beta.Organization.ExternalKeys.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/external_keys/{external_key_id}`

Delete an external key config.

The request is rejected if any workspace still references this config.

#### Parameters

- `ExternalKeyDeleteParams parameters`

  - `required string externalKeyID`

    ID of the External Key.

    maxLength: 2048

#### Returns

- `class ExternalKeyDeleteResponse:`

  - `JsonElement Type = "external_key_deleted"`

  - `required string ID`

    ID of the deleted External Key.

#### Example

```csharp
ExternalKeyDeleteParams parameters = new()
{
    ExternalKeyID = "external_key_id"
};

var externalKey = await client.Beta.Organization.ExternalKeys.Delete(parameters);

Console.WriteLine(externalKey);
```

##### Response (200)

```json
{
  "id": "ekey_01AbCdEfGhIjKlMnOpQrStUv",
  "type": "external_key_deleted"
}
```

### Validate External Key

`ExternalKeyValidateResponse Beta.Organization.ExternalKeys.Validate(parameters, cancellationToken = default)`

**POST** `/v1/organizations/external_keys/{external_key_id}/validate`

Validate an external key config against the customer's KMS.

Anthropic performs an encrypt/decrypt roundtrip against the configured
KMS key and waits up to 30 seconds for the result. The response status is
`success` if the roundtrip succeeded, or `failure` with an error
message if it failed or timed out.

#### Parameters

- `ExternalKeyValidateParams parameters`

  - `required string externalKeyID`

    ID of the External Key.

    maxLength: 2048

#### Returns

- `class ExternalKeyValidateResponse:`

  Result of a validation roundtrip against the customer's KMS.

  HTTP 200 for both outcomes — the operation completed; `status` says
  whether the key works.

  - `JsonElement Type = "external_key_validation"`

  - `required string? Error`

    Error message when status is `failure`. Null otherwise.

  - `required Status Status`

    `success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

    - `Failure("failure")`

    - `Success("success")`

#### Example

```csharp
ExternalKeyValidateParams parameters = new()
{
    ExternalKeyID = "external_key_id"
};

var response = await client.Beta.Organization.ExternalKeys.Validate(parameters);

Console.WriteLine(response);
```

##### Response (200)

```json
{
  "error": "error",
  "status": "failure",
  "type": "external_key_validation"
}
```

## Beta › Organization › Federation › Issuers

### Create Federation Issuer

`BetaFederationIssuer Beta.Organization.Federation.Issuers.Create(parameters, cancellationToken = default)`

**POST** `/v1/organizations/federation_issuers`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Register an OIDC issuer that Anthropic will trust for workload identity
federation in your organization.

The `jwks` field controls how the issuer's signing keys are obtained and
takes one of three shapes selected by `type`: `discovery` (resolve keys
through OIDC discovery), `explicit_url` (fetch keys from a fixed JWKS
URL), or `inline` (provide a static key set). When `jwks.type` is
`discovery` and no `discovery_base` is set, the issuer URL must be
publicly reachable over HTTPS so Anthropic can fetch the discovery
document; for `explicit_url` and `inline` modes the issuer URL is only
matched as the JWT's `iss` claim and is not fetched.

#### Parameters

- `IssuerCreateParams parameters`

  - `required string issuerUrl`

    Body param: The `iss` claim value to match against.

    minLength: 1

  - `required string name`

    Body param: Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

    maxLength: 255, minLength: 1

  - `bool? checkJti`

    Body param: Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Defaults to true. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `Jwks jwks`

    Body param: How signing keys are obtained. Defaults to OIDC discovery.

    - `class BetaJwksDiscovery:`

      JWKS via the issuer's OIDC discovery document.

      - `JsonElement Type = "discovery"`

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `string? DiscoveryBase`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJwksExplicitUrl:`

      JWKS fetched from a fixed endpoint.

      - `JsonElement Type = "explicit_url"`

      - `required string Url`

        JWKS endpoint.

        minLength: 1

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJwksInline:`

      JWKS supplied directly; no network fetch.

      - `JsonElement Type = "inline"`

      - `required IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> Keys`

        Inline JWK objects.

        minItems: 1

  - `long? maxJwtLifetimeSeconds`

    Body param: Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Defaults to 3600 (1h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

    maximum: 176400, exclusiveMinimum: 0

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaFederationIssuer:`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `JsonElement Type = "federation_issuer"`

  - `required string ID`

    Tagged ID of the federation issuer.

  - `required DateTimeOffset? ArchivedAt`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `required bool CheckJti`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `required DateTimeOffset CreatedAt`

    When this issuer was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `required string IssuerUrl`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `required Jwks Jwks`

    How signing keys are obtained for signature verification.

    - `class BetaJwksDiscovery:`

      JWKS via the issuer's OIDC discovery document.

      - `JsonElement Type = "discovery"`

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `string? DiscoveryBase`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJwksExplicitUrl:`

      JWKS fetched from a fixed endpoint.

      - `JsonElement Type = "explicit_url"`

      - `required string Url`

        JWKS endpoint.

        minLength: 1

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJwksInline:`

      JWKS supplied directly; no network fetch.

      - `JsonElement Type = "inline"`

      - `required IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> Keys`

        Inline JWK objects.

        minItems: 1

  - `required DateTimeOffset? JwksPollingDisabledAt`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `required long MaxJwtLifetimeSeconds`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required BetaFederationIssuerPollStatus? PollStatus`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `required long ConsecutiveFailures`

      Consecutive fetch failures since the last success.

    - `required DateTimeOffset? LastFetchedAt`

      When the last successful fetch completed.

      format: date-time

    - `required DateTimeOffset? NextPollAt`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `required DateTimeOffset UpdatedAt`

    When this issuer was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```csharp
IssuerCreateParams parameters = new()
{
    IssuerUrl = "x",
    Name = "x",
};

var betaFederationIssuer = await client.Beta.Organization.Federation.Issuers.Create(parameters);

Console.WriteLine(betaFederationIssuer);
```

##### Response (200)

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### List Federation Issuers

`IssuerListPage Beta.Organization.Federation.Issuers.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/federation_issuers`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List federation issuers in your organization.

Archived issuers are excluded unless `include_archived=true`.

#### Parameters

- `IssuerListParams parameters`

  - `bool includeArchived`

    Query param: Include archived resources. Defaults to false.

  - `long limit`

    Query param: Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaFederationIssuer:`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `JsonElement Type = "federation_issuer"`

  - `required string ID`

    Tagged ID of the federation issuer.

  - `required DateTimeOffset? ArchivedAt`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `required bool CheckJti`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `required DateTimeOffset CreatedAt`

    When this issuer was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `required string IssuerUrl`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `required Jwks Jwks`

    How signing keys are obtained for signature verification.

    - `class BetaJwksDiscovery:`

      JWKS via the issuer's OIDC discovery document.

      - `JsonElement Type = "discovery"`

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `string? DiscoveryBase`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJwksExplicitUrl:`

      JWKS fetched from a fixed endpoint.

      - `JsonElement Type = "explicit_url"`

      - `required string Url`

        JWKS endpoint.

        minLength: 1

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJwksInline:`

      JWKS supplied directly; no network fetch.

      - `JsonElement Type = "inline"`

      - `required IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> Keys`

        Inline JWK objects.

        minItems: 1

  - `required DateTimeOffset? JwksPollingDisabledAt`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `required long MaxJwtLifetimeSeconds`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required BetaFederationIssuerPollStatus? PollStatus`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `required long ConsecutiveFailures`

      Consecutive fetch failures since the last success.

    - `required DateTimeOffset? LastFetchedAt`

      When the last successful fetch completed.

      format: date-time

    - `required DateTimeOffset? NextPollAt`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `required DateTimeOffset UpdatedAt`

    When this issuer was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```csharp
IssuerListParams parameters = new();

var page = await client.Beta.Organization.Federation.Issuers.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "check_jti": true,
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "issuer_url": "https://token.actions.githubusercontent.com",
      "jwks": {
        "type": "discovery",
        "ca_cert_pem": "ca_cert_pem",
        "discovery_base": "discovery_base"
      },
      "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
      "max_jwt_lifetime_seconds": 0,
      "name": "github-actions",
      "poll_status": {
        "consecutive_failures": 0,
        "last_fetched_at": "2019-12-27T18:11:19.117Z",
        "next_poll_at": "2019-12-27T18:11:19.117Z"
      },
      "type": "federation_issuer",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
    }
  ],
  "next_page": "next_page"
}
```

### Get Federation Issuer

`BetaFederationIssuer Beta.Organization.Federation.Issuers.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/federation_issuers/{federation_issuer_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a federation issuer by its ID (`fdis_...`).

#### Parameters

- `IssuerRetrieveParams parameters`

  - `required string federationIssuerID`

    ID of the federation issuer.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaFederationIssuer:`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `JsonElement Type = "federation_issuer"`

  - `required string ID`

    Tagged ID of the federation issuer.

  - `required DateTimeOffset? ArchivedAt`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `required bool CheckJti`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `required DateTimeOffset CreatedAt`

    When this issuer was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `required string IssuerUrl`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `required Jwks Jwks`

    How signing keys are obtained for signature verification.

    - `class BetaJwksDiscovery:`

      JWKS via the issuer's OIDC discovery document.

      - `JsonElement Type = "discovery"`

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `string? DiscoveryBase`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJwksExplicitUrl:`

      JWKS fetched from a fixed endpoint.

      - `JsonElement Type = "explicit_url"`

      - `required string Url`

        JWKS endpoint.

        minLength: 1

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJwksInline:`

      JWKS supplied directly; no network fetch.

      - `JsonElement Type = "inline"`

      - `required IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> Keys`

        Inline JWK objects.

        minItems: 1

  - `required DateTimeOffset? JwksPollingDisabledAt`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `required long MaxJwtLifetimeSeconds`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required BetaFederationIssuerPollStatus? PollStatus`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `required long ConsecutiveFailures`

      Consecutive fetch failures since the last success.

    - `required DateTimeOffset? LastFetchedAt`

      When the last successful fetch completed.

      format: date-time

    - `required DateTimeOffset? NextPollAt`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `required DateTimeOffset UpdatedAt`

    When this issuer was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```csharp
IssuerRetrieveParams parameters = new()
{
    FederationIssuerID = "federation_issuer_id"
};

var betaFederationIssuer = await client.Beta.Organization.Federation.Issuers.Retrieve(parameters);

Console.WriteLine(betaFederationIssuer);
```

##### Response (200)

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### Update Federation Issuer

`BetaFederationIssuer Beta.Organization.Federation.Issuers.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/federation_issuers/{federation_issuer_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Partially update a federation issuer.

Setting `jwks` replaces the full JWKS shape at once. Archived issuers
cannot be updated; this returns 400. Create a new issuer instead.

Updating an issuer that backs a rule with a scope outside
`workspace:developer` or `workspace:inference` requires a Console
session.

#### Parameters

- `IssuerUpdateParams parameters`

  - `required string federationIssuerID`

    Path param: ID of the federation issuer to update.

  - `bool? checkJti`

    Body param: Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `string? issuerUrl`

    Body param: Replaces the `iss` claim value to match against. For discovery-mode issuers without a `discovery_base`, this is also the URL Anthropic fetches the OIDC discovery document and signing keys from, so changing it repoints the JWKS source. Changing the issuer URL to a well-known shared platform is rejected while any live rule under this issuer would not constrain tenant identity.

    minLength: 1

  - `Jwks? jwks`

    Body param: Replaces the entire JWKS configuration.

    - `class BetaJwksDiscovery:`

      JWKS via the issuer's OIDC discovery document.

      - `JsonElement Type = "discovery"`

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `string? DiscoveryBase`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJwksExplicitUrl:`

      JWKS fetched from a fixed endpoint.

      - `JsonElement Type = "explicit_url"`

      - `required string Url`

        JWKS endpoint.

        minLength: 1

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJwksInline:`

      JWKS supplied directly; no network fetch.

      - `JsonElement Type = "inline"`

      - `required IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> Keys`

        Inline JWK objects.

        minItems: 1

  - `bool? jwksPollingDisabled`

    Body param: Only `false` is accepted, to re-enable polling after the system pauses it. Polling is paused automatically; sending `true` is rejected.

  - `long? maxJwtLifetimeSeconds`

    Body param: Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

    maximum: 176400, exclusiveMinimum: 0

  - `string? name`

    Body param: Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

    maxLength: 255, minLength: 1

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaFederationIssuer:`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `JsonElement Type = "federation_issuer"`

  - `required string ID`

    Tagged ID of the federation issuer.

  - `required DateTimeOffset? ArchivedAt`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `required bool CheckJti`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `required DateTimeOffset CreatedAt`

    When this issuer was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `required string IssuerUrl`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `required Jwks Jwks`

    How signing keys are obtained for signature verification.

    - `class BetaJwksDiscovery:`

      JWKS via the issuer's OIDC discovery document.

      - `JsonElement Type = "discovery"`

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `string? DiscoveryBase`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJwksExplicitUrl:`

      JWKS fetched from a fixed endpoint.

      - `JsonElement Type = "explicit_url"`

      - `required string Url`

        JWKS endpoint.

        minLength: 1

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJwksInline:`

      JWKS supplied directly; no network fetch.

      - `JsonElement Type = "inline"`

      - `required IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> Keys`

        Inline JWK objects.

        minItems: 1

  - `required DateTimeOffset? JwksPollingDisabledAt`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `required long MaxJwtLifetimeSeconds`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required BetaFederationIssuerPollStatus? PollStatus`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `required long ConsecutiveFailures`

      Consecutive fetch failures since the last success.

    - `required DateTimeOffset? LastFetchedAt`

      When the last successful fetch completed.

      format: date-time

    - `required DateTimeOffset? NextPollAt`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `required DateTimeOffset UpdatedAt`

    When this issuer was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```csharp
IssuerUpdateParams parameters = new()
{
    FederationIssuerID = "federation_issuer_id"
};

var betaFederationIssuer = await client.Beta.Organization.Federation.Issuers.Update(parameters);

Console.WriteLine(betaFederationIssuer);
```

##### Response (200)

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### Archive Federation Issuer

`BetaFederationIssuer Beta.Organization.Federation.Issuers.Archive(parameters, cancellationToken = default)`

**POST** `/v1/organizations/federation_issuers/{federation_issuer_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a federation issuer.

Idempotent; re-archiving returns the issuer with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still references the issuer; archive those rules first (a rule's
issuer cannot be changed), or recreate them against another issuer.

#### Parameters

- `IssuerArchiveParams parameters`

  - `required string federationIssuerID`

    ID of the federation issuer to archive.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaFederationIssuer:`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `JsonElement Type = "federation_issuer"`

  - `required string ID`

    Tagged ID of the federation issuer.

  - `required DateTimeOffset? ArchivedAt`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `required bool CheckJti`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `required DateTimeOffset CreatedAt`

    When this issuer was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `required string IssuerUrl`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `required Jwks Jwks`

    How signing keys are obtained for signature verification.

    - `class BetaJwksDiscovery:`

      JWKS via the issuer's OIDC discovery document.

      - `JsonElement Type = "discovery"`

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `string? DiscoveryBase`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJwksExplicitUrl:`

      JWKS fetched from a fixed endpoint.

      - `JsonElement Type = "explicit_url"`

      - `required string Url`

        JWKS endpoint.

        minLength: 1

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJwksInline:`

      JWKS supplied directly; no network fetch.

      - `JsonElement Type = "inline"`

      - `required IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> Keys`

        Inline JWK objects.

        minItems: 1

  - `required DateTimeOffset? JwksPollingDisabledAt`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `required long MaxJwtLifetimeSeconds`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required BetaFederationIssuerPollStatus? PollStatus`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `required long ConsecutiveFailures`

      Consecutive fetch failures since the last success.

    - `required DateTimeOffset? LastFetchedAt`

      When the last successful fetch completed.

      format: date-time

    - `required DateTimeOffset? NextPollAt`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `required DateTimeOffset UpdatedAt`

    When this issuer was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```csharp
IssuerArchiveParams parameters = new()
{
    FederationIssuerID = "federation_issuer_id"
};

var betaFederationIssuer = await client.Beta.Organization.Federation.Issuers.Archive(parameters);

Console.WriteLine(betaFederationIssuer);
```

##### Response (200)

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

## Beta › Organization › Federation › Rules

### Create Federation Rule

`BetaFederationRule Beta.Organization.Federation.Rules.Create(parameters, cancellationToken = default)`

**POST** `/v1/organizations/federation_rules`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Create a federation rule owned by your organization.

The referenced issuer and the target service account must already exist
in the same organization; invalid references are rejected with a 400
error. The workspace reference is validated. Membership is not checked
at rule creation: token exchange resolves a single enabled workspace per
call and is rejected unless the target service account is a member of
that workspace (it is implicitly a member of the default workspace).
Rules on well-known shared issuers (GitHub Actions, GitLab, Buildkite,
Terraform Cloud, Google) must constrain tenant identity via an
identity-bearing claim, a tenant-pinning subject prefix (such as
`repo:YOUR_ORG/...`), or a CEL condition referencing one of those
identity claims (e.g. `claims.repository_owner`). OAuth callers may only
manage rules whose `oauth_scope` is `workspace:developer` or
`workspace:inference`; other scopes require a Console session.

#### Parameters

- `RuleCreateParams parameters`

  - `required string issuerID`

    Body param: Tagged ID of the federation issuer.

  - `required BetaFederationRuleMatch match`

    Body param: Conditions the verified JWT must satisfy for this rule to apply. At least one of `subject_prefix` (other than a wildcard-only value like `*`), `claims`, or `condition` is required; `audience` alone is not sufficient.

  - `required string name`

    Body param: Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

    maxLength: 255, minLength: 1

  - `required string oauthScope`

    Body param: Space-separated OAuth scopes. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

    minLength: 1

  - `required BetaServiceAccountTarget target`

    Body param: Identity that tokens minted via this rule act as. Currently always a `service_account` target.

  - `bool appliesToAllWorkspaces`

    Body param: When true, enable this rule for every workspace in the org (including workspaces created later).

  - `IReadOnlyDictionary<string, string>? attributes`

    Body param: CEL expressions `{name: expr}` extracting named values from claims. Not yet supported; any non-empty value is rejected with 400.

  - `string? description`

    Body param: Optional free-text description.

    maxLength: 2000

  - `long tokenLifetimeSeconds`

    Body param: Lifetime in seconds for access tokens minted via this rule (60-86400). Defaults to 3600 (1h). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

    maximum: 86400, minimum: 60

  - `string? workspaceID`

    Body param: Tagged ID of the workspace to enable this rule for. Required unless `applies_to_all_workspaces` is true. Additional workspaces can be added via the `/federation_rules/{federation_rule_id}/workspaces` sub-resource.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaFederationRule:`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `JsonElement Type = "federation_rule"`

  - `required string ID`

    Tagged ID of the federation rule.

  - `required bool AppliesToAllWorkspaces`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `required DateTimeOffset? ArchivedAt`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `required IReadOnlyDictionary<string, string>? Attributes`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `required DateTimeOffset CreatedAt`

    When this rule was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `required string? Description`

    Optional free-text description.

  - `required string IssuerID`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `required string? IssuerName`

    Issuer's display name at read time.

  - `required BetaFederationRuleMatch Match`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `string? Audience`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `IReadOnlyDictionary<string, string>? Claims`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `string? Condition`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `string? SubjectPrefix`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `required string Name`

    Admin-chosen slug identifier.

  - `required string OAuthScope`

    Space-separated OAuth scopes granted on the minted token.

  - `required BetaServiceAccountTarget Target`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `JsonElement Type = "service_account"`

    - `required string ServiceAccountID`

      Tagged ID of the service account to mint tokens for.

    - `string? ServiceAccountName`

      Service account's display name at read time. Ignored on writes.

  - `required long TokenLifetimeSeconds`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `required DateTimeOffset UpdatedAt`

    When this rule was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `required string? WorkspaceID`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `required IReadOnlyList<string> WorkspaceIds`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```csharp
RuleCreateParams parameters = new()
{
    IssuerID = "issuer_id",
    Match = new()
    {
        Audience = "audience",
        Claims = new Dictionary<string, string>() { { "foo", "string" } },
        Condition = "condition",
        SubjectPrefix = "subject_prefix",
    },
    Name = "x",
    OAuthScope = "x",
    Target = new()
    {
        ServiceAccountID = "svac_01SDCCSbTxrXDpWc1phhtcfK",
        ServiceAccountName = "service_account_name",
    },
};

var betaFederationRule = await client.Beta.Organization.Federation.Rules.Create(parameters);

Console.WriteLine(betaFederationRule);
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

### List Federation Rules

`RuleListPage Beta.Organization.Federation.Rules.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/federation_rules`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List federation rules in your organization.

Optionally filter by issuer with `issuer_id`. Archived rules are excluded
unless `include_archived=true`.

#### Parameters

- `RuleListParams parameters`

  - `bool includeArchived`

    Query param: Include archived resources. Defaults to false.

  - `string? issuerID`

    Query param: Filter to rules referencing this federation issuer.

  - `long limit`

    Query param: Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaFederationRule:`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `JsonElement Type = "federation_rule"`

  - `required string ID`

    Tagged ID of the federation rule.

  - `required bool AppliesToAllWorkspaces`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `required DateTimeOffset? ArchivedAt`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `required IReadOnlyDictionary<string, string>? Attributes`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `required DateTimeOffset CreatedAt`

    When this rule was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `required string? Description`

    Optional free-text description.

  - `required string IssuerID`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `required string? IssuerName`

    Issuer's display name at read time.

  - `required BetaFederationRuleMatch Match`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `string? Audience`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `IReadOnlyDictionary<string, string>? Claims`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `string? Condition`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `string? SubjectPrefix`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `required string Name`

    Admin-chosen slug identifier.

  - `required string OAuthScope`

    Space-separated OAuth scopes granted on the minted token.

  - `required BetaServiceAccountTarget Target`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `JsonElement Type = "service_account"`

    - `required string ServiceAccountID`

      Tagged ID of the service account to mint tokens for.

    - `string? ServiceAccountName`

      Service account's display name at read time. Ignored on writes.

  - `required long TokenLifetimeSeconds`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `required DateTimeOffset UpdatedAt`

    When this rule was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `required string? WorkspaceID`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `required IReadOnlyList<string> WorkspaceIds`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```csharp
RuleListParams parameters = new();

var page = await client.Beta.Organization.Federation.Rules.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
      "applies_to_all_workspaces": true,
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "attributes": {
        "foo": "string"
      },
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "issuer_id": "issuer_id",
      "issuer_name": "issuer_name",
      "match": {
        "audience": "audience",
        "claims": {
          "foo": "string"
        },
        "condition": "condition",
        "subject_prefix": "subject_prefix"
      },
      "name": "prod-deploy-pipeline",
      "oauth_scope": "oauth_scope",
      "target": {
        "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
        "type": "service_account",
        "service_account_name": "service_account_name"
      },
      "token_lifetime_seconds": 0,
      "type": "federation_rule",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id",
      "workspace_id": "workspace_id",
      "workspace_ids": [
        "string"
      ]
    }
  ],
  "next_page": "next_page"
}
```

### Get Federation Rule

`BetaFederationRule Beta.Organization.Federation.Rules.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/federation_rules/{federation_rule_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a federation rule by its ID (`fdrl_...`).

#### Parameters

- `RuleRetrieveParams parameters`

  - `required string federationRuleID`

    ID of the federation rule.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaFederationRule:`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `JsonElement Type = "federation_rule"`

  - `required string ID`

    Tagged ID of the federation rule.

  - `required bool AppliesToAllWorkspaces`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `required DateTimeOffset? ArchivedAt`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `required IReadOnlyDictionary<string, string>? Attributes`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `required DateTimeOffset CreatedAt`

    When this rule was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `required string? Description`

    Optional free-text description.

  - `required string IssuerID`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `required string? IssuerName`

    Issuer's display name at read time.

  - `required BetaFederationRuleMatch Match`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `string? Audience`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `IReadOnlyDictionary<string, string>? Claims`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `string? Condition`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `string? SubjectPrefix`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `required string Name`

    Admin-chosen slug identifier.

  - `required string OAuthScope`

    Space-separated OAuth scopes granted on the minted token.

  - `required BetaServiceAccountTarget Target`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `JsonElement Type = "service_account"`

    - `required string ServiceAccountID`

      Tagged ID of the service account to mint tokens for.

    - `string? ServiceAccountName`

      Service account's display name at read time. Ignored on writes.

  - `required long TokenLifetimeSeconds`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `required DateTimeOffset UpdatedAt`

    When this rule was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `required string? WorkspaceID`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `required IReadOnlyList<string> WorkspaceIds`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```csharp
RuleRetrieveParams parameters = new()
{
    FederationRuleID = "federation_rule_id"
};

var betaFederationRule = await client.Beta.Organization.Federation.Rules.Retrieve(parameters);

Console.WriteLine(betaFederationRule);
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

### Update Federation Rule

`BetaFederationRule Beta.Organization.Federation.Rules.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/federation_rules/{federation_rule_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Partially update a federation rule.

`issuer_id` is immutable. `match` and `target` are replaced as whole
objects when set. Referenced service accounts and workspaces must exist
in your organization; invalid references are rejected with a 400 error.
Archived rules cannot be updated; this returns 400. Create a new rule
instead. Rules on well-known shared issuers (GitHub Actions, GitLab,
Buildkite, Terraform Cloud, Google) must constrain tenant identity via
an identity-bearing claim, a tenant-pinning subject prefix (such as
`repo:YOUR_ORG/...`), or a CEL condition referencing one of those
identity claims (e.g. `claims.repository_owner`). On these issuers the
requirement is re-checked on every update; if an existing rule's stored
match does not yet constrain tenant identity, any update (even a rename
or description change) must also supply a conforming `match` in the same
request. OAuth callers may only manage rules whose `oauth_scope` is
`workspace:developer` or `workspace:inference`; other scopes require a
Console session.

#### Parameters

- `RuleUpdateParams parameters`

  - `required string federationRuleID`

    Path param: ID of the federation rule to update.

  - `bool? appliesToAllWorkspaces`

    Body param: When true, enables this rule for every workspace in the org (including workspaces created later). Setting `false` is rejected with 400 if no workspace would remain enabled; a rule with only a legacy `workspace_id` binding continues to mint.

  - `IReadOnlyDictionary<string, string>? attributes`

    Body param: Replaces the CEL expressions `{name: expr}` extracting named values from claims. Send null to clear them. Not yet supported; any non-empty value is rejected with 400.

  - `string? description`

    Body param: Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

    maxLength: 2000

  - `BetaFederationRuleMatch? match`

    Body param: Does the incoming JWT qualify?

    All populated fields must pass; omitted fields are skipped. At least one
    of `subject_prefix` (other than a wildcard-only value like `*`), `claims`,
    or `condition` is required; `audience` alone is not sufficient.

  - `string? name`

    Body param: Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

    maxLength: 255, minLength: 1

  - `string? oauthScope`

    Body param: Replaces the space-separated OAuth scopes granted on minted tokens. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

    minLength: 1

  - `BetaServiceAccountTarget? target`

    Body param: Bind to a fixed service account by ID.

  - `long? tokenLifetimeSeconds`

    Body param: Replaces the lifetime in seconds for access tokens minted via this rule (60-86400). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

    maximum: 86400, minimum: 60

  - `string? workspaceID`

    Body param: Replaces the existing single workspace enablement (the previous one is removed). Rejected with 400 if the rule is enabled for more than one workspace; use the `/federation_rules/{federation_rule_id}/workspaces` sub-resource instead.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaFederationRule:`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `JsonElement Type = "federation_rule"`

  - `required string ID`

    Tagged ID of the federation rule.

  - `required bool AppliesToAllWorkspaces`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `required DateTimeOffset? ArchivedAt`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `required IReadOnlyDictionary<string, string>? Attributes`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `required DateTimeOffset CreatedAt`

    When this rule was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `required string? Description`

    Optional free-text description.

  - `required string IssuerID`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `required string? IssuerName`

    Issuer's display name at read time.

  - `required BetaFederationRuleMatch Match`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `string? Audience`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `IReadOnlyDictionary<string, string>? Claims`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `string? Condition`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `string? SubjectPrefix`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `required string Name`

    Admin-chosen slug identifier.

  - `required string OAuthScope`

    Space-separated OAuth scopes granted on the minted token.

  - `required BetaServiceAccountTarget Target`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `JsonElement Type = "service_account"`

    - `required string ServiceAccountID`

      Tagged ID of the service account to mint tokens for.

    - `string? ServiceAccountName`

      Service account's display name at read time. Ignored on writes.

  - `required long TokenLifetimeSeconds`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `required DateTimeOffset UpdatedAt`

    When this rule was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `required string? WorkspaceID`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `required IReadOnlyList<string> WorkspaceIds`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```csharp
RuleUpdateParams parameters = new() { FederationRuleID = "federation_rule_id" };

var betaFederationRule = await client.Beta.Organization.Federation.Rules.Update(parameters);

Console.WriteLine(betaFederationRule);
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

### Archive Federation Rule

`BetaFederationRule Beta.Organization.Federation.Rules.Archive(parameters, cancellationToken = default)`

**POST** `/v1/organizations/federation_rules/{federation_rule_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a federation rule.

Token exchange through this rule stops immediately. Idempotent;
re-archiving returns the rule with its original `archived_at`. Archiving
clears the rule's workspace targeting (`workspace_id` and
`workspace_ids` are emptied). Tokens already minted before archive
remain valid until they expire. OAuth callers may only manage rules
whose `oauth_scope` is `workspace:developer` or `workspace:inference`;
other scopes require a Console session.

#### Parameters

- `RuleArchiveParams parameters`

  - `required string federationRuleID`

    ID of the federation rule to archive.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaFederationRule:`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `JsonElement Type = "federation_rule"`

  - `required string ID`

    Tagged ID of the federation rule.

  - `required bool AppliesToAllWorkspaces`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `required DateTimeOffset? ArchivedAt`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `required IReadOnlyDictionary<string, string>? Attributes`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `required DateTimeOffset CreatedAt`

    When this rule was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `required string? Description`

    Optional free-text description.

  - `required string IssuerID`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `required string? IssuerName`

    Issuer's display name at read time.

  - `required BetaFederationRuleMatch Match`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `string? Audience`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `IReadOnlyDictionary<string, string>? Claims`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `string? Condition`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `string? SubjectPrefix`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `required string Name`

    Admin-chosen slug identifier.

  - `required string OAuthScope`

    Space-separated OAuth scopes granted on the minted token.

  - `required BetaServiceAccountTarget Target`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `JsonElement Type = "service_account"`

    - `required string ServiceAccountID`

      Tagged ID of the service account to mint tokens for.

    - `string? ServiceAccountName`

      Service account's display name at read time. Ignored on writes.

  - `required long TokenLifetimeSeconds`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `required DateTimeOffset UpdatedAt`

    When this rule was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `required string? WorkspaceID`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `required IReadOnlyList<string> WorkspaceIds`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```csharp
RuleArchiveParams parameters = new()
{
    FederationRuleID = "federation_rule_id"
};

var betaFederationRule = await client.Beta.Organization.Federation.Rules.Archive(parameters);

Console.WriteLine(betaFederationRule);
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

## Beta › Organization › Federation › Rules › Workspaces

### Add Federation Rule Workspace

`BetaFederationRuleWorkspace Beta.Organization.Federation.Rules.Workspaces.Add(parameters, cancellationToken = default)`

**POST** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Enable a federation rule for a workspace.

Idempotent; re-enabling returns the existing enablement. The rule and
workspace must both belong to your organization. Membership of the
rule's target service account in this workspace is not checked at
enablement: token exchange into this workspace is rejected unless the
target is a member (it is implicitly a member of the default workspace).
Archived rules are rejected with 400. OAuth callers may only manage rules
whose `oauth_scope` is `workspace:developer` or `workspace:inference`;
other scopes require a Console session.

#### Parameters

- `WorkspaceAddParams parameters`

  - `required string federationRuleID`

    Path param: ID of the federation rule.

  - `required string workspaceID`

    Body param: Tagged ID of the workspace to enable this rule for.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaFederationRuleWorkspace:`

  - `JsonElement Type = "federation_rule_workspace"`

  - `required DateTimeOffset CreatedAt`

    When this workspace was enabled for the rule.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `required string FederationRuleID`

    Tagged ID of the federation rule.

  - `required string WorkspaceID`

    Tagged ID of the workspace this rule is enabled for.

  - `required string? WorkspaceName`

    Workspace display name. Populated when listing; null in the enable response.

#### Example

```csharp
WorkspaceAddParams parameters = new()
{
    FederationRuleID = "federation_rule_id",
    WorkspaceID = "workspace_id",
};

var betaFederationRuleWorkspace = await client.Beta.Organization.Federation.Rules.Workspaces.Add(parameters);

Console.WriteLine(betaFederationRuleWorkspace);
```

##### Response (200)

```json
{
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace",
  "workspace_id": "workspace_id",
  "workspace_name": "workspace_name"
}
```

### List Federation Rule Workspaces

`WorkspaceListPage Beta.Organization.Federation.Rules.Workspaces.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List workspaces where this federation rule is enabled.

Returns all workspace enablements in a single response; the `limit` and
`page` parameters are accepted but have no effect, and `next_page` is
always `null`. Returns explicit per-workspace enablements only; for
rules with `applies_to_all_workspaces` or a legacy single
`workspace_id`, check those fields on the rule itself.

#### Parameters

- `WorkspaceListParams parameters`

  - `required string federationRuleID`

    Path param: ID of the federation rule.

  - `long limit`

    Query param: Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaFederationRuleWorkspace:`

  - `JsonElement Type = "federation_rule_workspace"`

  - `required DateTimeOffset CreatedAt`

    When this workspace was enabled for the rule.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `required string FederationRuleID`

    Tagged ID of the federation rule.

  - `required string WorkspaceID`

    Tagged ID of the workspace this rule is enabled for.

  - `required string? WorkspaceName`

    Workspace display name. Populated when listing; null in the enable response.

#### Example

```csharp
WorkspaceListParams parameters = new()
{
    FederationRuleID = "federation_rule_id"
};

var page = await client.Beta.Organization.Federation.Rules.Workspaces.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "federation_rule_id": "federation_rule_id",
      "type": "federation_rule_workspace",
      "workspace_id": "workspace_id",
      "workspace_name": "workspace_name"
    }
  ],
  "next_page": "next_page"
}
```

### Remove Federation Rule Workspace

`WorkspaceRemoveResponse Beta.Organization.Federation.Rules.Workspaces.Remove(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Disable a federation rule for a workspace.

Idempotent; succeeds even if the enablement was already removed. OAuth
callers may only manage rules whose `oauth_scope` is
`workspace:developer` or `workspace:inference`; other scopes require a
Console session.

#### Parameters

- `WorkspaceRemoveParams parameters`

  - `required string federationRuleID`

    Path param: ID of the federation rule.

  - `required string workspaceID`

    Path param: ID of the workspace to disable for.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class WorkspaceRemoveResponse:`

  - `JsonElement Type = "federation_rule_workspace_deleted"`

  - `required string FederationRuleID`

    Tagged ID of the federation rule.

  - `required string WorkspaceID`

    Tagged ID of the workspace named in the delete request. Removal is idempotent.

#### Example

```csharp
WorkspaceRemoveParams parameters = new()
{
    FederationRuleID = "federation_rule_id",
    WorkspaceID = "workspace_id",
};

var workspace = await client.Beta.Organization.Federation.Rules.Workspaces.Remove(parameters);

Console.WriteLine(workspace);
```

##### Response (200)

```json
{
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace_deleted",
  "workspace_id": "workspace_id"
}
```

## Beta › Organization › Invites

### Create Invite

`BetaOrganizationInvite Beta.Organization.Invites.Create(parameters, cancellationToken = default)`

**POST** `/v1/organizations/invites`

Invite a user to join the organization by email.

On plans that draw members from a finite pool of purchased seats, the invite automatically consumes a seat from the lowest tier with availability; there is no seat-tier parameter. When no seat is free the request fails with a 400 error rather than purchasing a seat.

#### Parameters

- `InviteCreateParams parameters`

  - `required string email`

    Email of the User.

    format: email

  - `required Role role`

    Role for the invited User.

    The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

    - `Billing("billing")`

    - `ClaudeCodeUser("claude_code_user")`

    - `Developer("developer")`

    - `Managed("managed")`

    - `User("user")`

  - `IReadOnlyList<string> rbacGroupIds`

    RBAC group IDs to assign to the User when the Invite is accepted. A non-empty array is accepted only for a Claude Enterprise organization with RBAC groups, and requires the key to carry the `write:rbac_groups` scope.

    maxItems: 100

#### Returns

- `class BetaOrganizationInvite:`

  - `JsonElement Type = "invite"`

    Object type.

    For Invites, this is always `"invite"`.

  - `required string ID`

    ID of the Invite.

  - `required DateTimeOffset? AcceptedAt`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `required string Email`

    Email of the User being invited.

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `required DateTimeOffset InvitedAt`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `required IReadOnlyList<string> RbacGroupIds`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin("admin")`

    - `Billing("billing")`

    - `ClaudeCodeUser("claude_code_user")`

    - `Developer("developer")`

    - `Managed("managed")`

    - `MembershipAdmin("membership_admin")`

    - `Owner("owner")`

    - `PrimaryOwner("primary_owner")`

    - `User("user")`

  - `required Status Status`

    Status of the Invite.

    - `Accepted("accepted")`

    - `Deleted("deleted")`

    - `Expired("expired")`

    - `Pending("pending")`

#### Example

```csharp
InviteCreateParams parameters = new()
{
    Email = "user@emaildomain.com",
    Role = Role.User,
};

var betaOrganizationInvite = await client.Beta.Organization.Invites.Create(parameters);

Console.WriteLine(betaOrganizationInvite);
```

##### Response (200)

```json
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "accepted_at": "2019-12-27T18:11:19.117Z",
  "email": "user@emaildomain.com",
  "expires_at": "2024-11-20T23:58:27.427722Z",
  "invited_at": "2024-10-30T23:58:27.427722Z",
  "rbac_group_ids": [
    "string"
  ],
  "role": "admin",
  "status": "pending",
  "type": "invite"
}
```

### List Invites

`InviteListPage Beta.Organization.Invites.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/invites`

List the organization's invites.

#### Parameters

- `InviteListParams parameters`

  - `string afterID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `string email`

    Filter by the email address the Invite was sent to. Matches the same way as the Users list's `email` filter (normalized, case-insensitive).

    format: email

  - `long limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

  - `IReadOnlyList<string> roles`

    Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

    Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

  - `IReadOnlyList<Status> statuses`

    Filter by Invite status. Repeatable; values are OR'ed together. Omit to return `pending`, `accepted`, and `expired` Invites alike.

    - `Accepted("accepted")`

    - `Expired("expired")`

    - `Pending("pending")`

#### Returns

- `class BetaOrganizationInvite:`

  - `JsonElement Type = "invite"`

    Object type.

    For Invites, this is always `"invite"`.

  - `required string ID`

    ID of the Invite.

  - `required DateTimeOffset? AcceptedAt`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `required string Email`

    Email of the User being invited.

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `required DateTimeOffset InvitedAt`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `required IReadOnlyList<string> RbacGroupIds`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin("admin")`

    - `Billing("billing")`

    - `ClaudeCodeUser("claude_code_user")`

    - `Developer("developer")`

    - `Managed("managed")`

    - `MembershipAdmin("membership_admin")`

    - `Owner("owner")`

    - `PrimaryOwner("primary_owner")`

    - `User("user")`

  - `required Status Status`

    Status of the Invite.

    - `Accepted("accepted")`

    - `Deleted("deleted")`

    - `Expired("expired")`

    - `Pending("pending")`

#### Example

```csharp
InviteListParams parameters = new();

var page = await client.Beta.Organization.Invites.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
      "accepted_at": "2019-12-27T18:11:19.117Z",
      "email": "user@emaildomain.com",
      "expires_at": "2024-11-20T23:58:27.427722Z",
      "invited_at": "2024-10-30T23:58:27.427722Z",
      "rbac_group_ids": [
        "string"
      ],
      "role": "admin",
      "status": "pending",
      "type": "invite"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Get Invite

`BetaOrganizationInvite Beta.Organization.Invites.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/invites/{invite_id}`

Retrieve an invite by ID.

#### Parameters

- `InviteRetrieveParams parameters`

  - `required string inviteID`

    ID of the Invite.

#### Returns

- `class BetaOrganizationInvite:`

  - `JsonElement Type = "invite"`

    Object type.

    For Invites, this is always `"invite"`.

  - `required string ID`

    ID of the Invite.

  - `required DateTimeOffset? AcceptedAt`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `required string Email`

    Email of the User being invited.

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `required DateTimeOffset InvitedAt`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `required IReadOnlyList<string> RbacGroupIds`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin("admin")`

    - `Billing("billing")`

    - `ClaudeCodeUser("claude_code_user")`

    - `Developer("developer")`

    - `Managed("managed")`

    - `MembershipAdmin("membership_admin")`

    - `Owner("owner")`

    - `PrimaryOwner("primary_owner")`

    - `User("user")`

  - `required Status Status`

    Status of the Invite.

    - `Accepted("accepted")`

    - `Deleted("deleted")`

    - `Expired("expired")`

    - `Pending("pending")`

#### Example

```csharp
InviteRetrieveParams parameters = new() { InviteID = "invite_id" };

var betaOrganizationInvite = await client.Beta.Organization.Invites.Retrieve(parameters);

Console.WriteLine(betaOrganizationInvite);
```

##### Response (200)

```json
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "accepted_at": "2019-12-27T18:11:19.117Z",
  "email": "user@emaildomain.com",
  "expires_at": "2024-11-20T23:58:27.427722Z",
  "invited_at": "2024-10-30T23:58:27.427722Z",
  "rbac_group_ids": [
    "string"
  ],
  "role": "admin",
  "status": "pending",
  "type": "invite"
}
```

### Delete Invite

`InviteDeleteResponse Beta.Organization.Invites.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/invites/{invite_id}`

Delete a pending invite.

#### Parameters

- `InviteDeleteParams parameters`

  - `required string inviteID`

    ID of the Invite.

#### Returns

- `class InviteDeleteResponse:`

  - `JsonElement Type = "invite_deleted"`

    Deleted object type.

    For Invites, this is always `"invite_deleted"`.

  - `required string ID`

    ID of the Invite.

#### Example

```csharp
InviteDeleteParams parameters = new() { InviteID = "invite_id" };

var invite = await client.Beta.Organization.Invites.Delete(parameters);

Console.WriteLine(invite);
```

##### Response (200)

```json
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "type": "invite_deleted"
}
```

## Beta › Organization › Service Accounts

### Create Service Account

`BetaServiceAccount Beta.Organization.ServiceAccounts.Create(parameters, cancellationToken = default)`

**POST** `/v1/organizations/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Create a service account.

A service account is a named workload identity that federation rules
target. `organization_role` is `developer` (default) or `admin`; a rule
may only be created or retargeted to grant `org:admin` scope when the
target's `organization_role` is `admin`. Creating an `admin`-role service
account requires an interactive credential (a user OAuth token or a
Console session) — a workload may only create `developer`-role service
accounts.

#### Parameters

- `ServiceAccountCreateParams parameters`

  - `required string name`

    Body param: Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

    maxLength: 255, minLength: 1

  - `string? description`

    Body param: Optional free-text description.

    maxLength: 2000

  - `OrganizationRole organizationRole`

    Body param: Org-level role. Defaults to `developer`.

    - `Admin("admin")`

    - `Developer("developer")`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `JsonElement Type = "service_account"`

  - `required string ID`

    Tagged ID of the service account.

  - `required DateTimeOffset? ArchivedAt`

    If set, this service account is archived.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `required DateTimeOffset CreatedAt`

    When this service account was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `required string? Description`

    Optional free-text description.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required OrganizationRole OrganizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `Admin("admin")`

    - `Developer("developer")`

  - `required DateTimeOffset UpdatedAt`

    When this service account was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```csharp
ServiceAccountCreateParams parameters = new() { Name = "ci-deploy-bot" };

var betaServiceAccount = await client.Beta.Organization.ServiceAccounts.Create(parameters);

Console.WriteLine(betaServiceAccount);
```

##### Response (200)

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### List Service Accounts

`ServiceAccountListPage Beta.Organization.ServiceAccounts.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List service accounts in the caller's organization.

Results are ordered by creation time, newest first. Use `limit` and the
`next_page` cursor to paginate; set `include_archived=true` to include
archived service accounts.

#### Parameters

- `ServiceAccountListParams parameters`

  - `bool includeArchived`

    Query param: Include archived resources. Defaults to false.

  - `long limit`

    Query param: Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `JsonElement Type = "service_account"`

  - `required string ID`

    Tagged ID of the service account.

  - `required DateTimeOffset? ArchivedAt`

    If set, this service account is archived.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `required DateTimeOffset CreatedAt`

    When this service account was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `required string? Description`

    Optional free-text description.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required OrganizationRole OrganizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `Admin("admin")`

    - `Developer("developer")`

  - `required DateTimeOffset UpdatedAt`

    When this service account was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```csharp
ServiceAccountListParams parameters = new();

var page = await client.Beta.Organization.ServiceAccounts.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "name": "ci-deploy-bot",
      "organization_role": "admin",
      "type": "service_account",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
    }
  ],
  "next_page": "next_page"
}
```

### Get Service Account

`BetaServiceAccount Beta.Organization.ServiceAccounts.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a service account by its ID (`svac_...`).

#### Parameters

- `ServiceAccountRetrieveParams parameters`

  - `required string serviceAccountID`

    ID of the service account.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `JsonElement Type = "service_account"`

  - `required string ID`

    Tagged ID of the service account.

  - `required DateTimeOffset? ArchivedAt`

    If set, this service account is archived.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `required DateTimeOffset CreatedAt`

    When this service account was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `required string? Description`

    Optional free-text description.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required OrganizationRole OrganizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `Admin("admin")`

    - `Developer("developer")`

  - `required DateTimeOffset UpdatedAt`

    When this service account was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```csharp
ServiceAccountRetrieveParams parameters = new()
{
    ServiceAccountID = "service_account_id"
};

var betaServiceAccount = await client.Beta.Organization.ServiceAccounts.Retrieve(parameters);

Console.WriteLine(betaServiceAccount);
```

##### Response (200)

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### Update Service Account

`BetaServiceAccount Beta.Organization.ServiceAccounts.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Update a service account.

Only `description` and `organization_role` are mutable; `name` cannot be
changed. Archived service accounts cannot be updated; this returns 400.
Setting `organization_role` to `admin` (even when unchanged) requires an
interactive credential (a user OAuth token or a Console session).

#### Parameters

- `ServiceAccountUpdateParams parameters`

  - `required string serviceAccountID`

    Path param: ID of the service account to update.

  - `string? description`

    Body param: Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

    maxLength: 2000

  - `OrganizationRole? organizationRole`

    Body param: Replaces the org-level role. Omit or send `null` to leave unchanged.

    - `Admin("admin")`

    - `Developer("developer")`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `JsonElement Type = "service_account"`

  - `required string ID`

    Tagged ID of the service account.

  - `required DateTimeOffset? ArchivedAt`

    If set, this service account is archived.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `required DateTimeOffset CreatedAt`

    When this service account was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `required string? Description`

    Optional free-text description.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required OrganizationRole OrganizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `Admin("admin")`

    - `Developer("developer")`

  - `required DateTimeOffset UpdatedAt`

    When this service account was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```csharp
ServiceAccountUpdateParams parameters = new()
{
    ServiceAccountID = "service_account_id"
};

var betaServiceAccount = await client.Beta.Organization.ServiceAccounts.Update(parameters);

Console.WriteLine(betaServiceAccount);
```

##### Response (200)

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### Archive Service Account

`BetaServiceAccount Beta.Organization.ServiceAccounts.Archive(parameters, cancellationToken = default)`

**POST** `/v1/organizations/service_accounts/{service_account_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a service account.

Idempotent; re-archiving returns the service account with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still targets this service account, same as issuer archival; archive
those rules first or change their target to another service account.

#### Parameters

- `ServiceAccountArchiveParams parameters`

  - `required string serviceAccountID`

    ID of the service account to archive.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `JsonElement Type = "service_account"`

  - `required string ID`

    Tagged ID of the service account.

  - `required DateTimeOffset? ArchivedAt`

    If set, this service account is archived.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `required DateTimeOffset CreatedAt`

    When this service account was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `required string? Description`

    Optional free-text description.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required OrganizationRole OrganizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `Admin("admin")`

    - `Developer("developer")`

  - `required DateTimeOffset UpdatedAt`

    When this service account was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```csharp
ServiceAccountArchiveParams parameters = new()
{
    ServiceAccountID = "service_account_id"
};

var betaServiceAccount = await client.Beta.Organization.ServiceAccounts.Archive(parameters);

Console.WriteLine(betaServiceAccount);
```

##### Response (200)

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

## Beta › Organization › Service Accounts › Workspaces

### Add Workspace To Service Account

`BetaServiceAccountWorkspaceMember Beta.Organization.ServiceAccounts.Workspaces.Add(parameters, cancellationToken = default)`

**POST** `/v1/organizations/service_accounts/{service_account_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Add a service account to a workspace with the given `workspace_role`.

Mirror of `POST /workspaces/{workspace_id}/service_accounts`, addressed
from the service-account side; both create the same membership. If the
service account is already an explicit member of the workspace, its
`workspace_role` is replaced with the value supplied here. Archived
workspaces return 400. Archived service accounts cannot be added and are
rejected.

#### Parameters

- `WorkspaceAddParams parameters`

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `required string workspaceID`

    Body param: Tagged workspace ID to add the service account to.

  - `required BetaNoBillingWorkspaceRole workspaceRole`

    Body param: Role to assign to the service account in this workspace.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `JsonElement Type = "service_account_workspace_member"`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
WorkspaceAddParams parameters = new()
{
    ServiceAccountID = "service_account_id",
    WorkspaceID = "workspace_id",
    WorkspaceRole = BetaNoBillingWorkspaceRole.WorkspaceAdmin,
};

var betaServiceAccountWorkspaceMember = await client.Beta.Organization.ServiceAccounts.Workspaces.Add(parameters);

Console.WriteLine(betaServiceAccountWorkspaceMember);
```

##### Response (200)

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

### List Workspaces For Service Account

`WorkspaceListPage Beta.Organization.ServiceAccounts.Workspaces.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/service_accounts/{service_account_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List the workspaces a service account is a member of.

Each entry includes the service account's `workspace_role` in that
workspace. Use `limit` and the `next_page` cursor to paginate. When the
service account has no explicit default-workspace membership, the
implicit (`implicit: true`) membership is returned as the first entry on
the first page; with `limit=1` the first page may return up to 2 entries
(the implicit entry plus one explicit membership) so a pagination cursor
can be derived. Memberships are returned only while
the service account is active. Without a `page` cursor, an archived
service account returns an empty list. A `page` cursor that does not
match an active membership returns a 400 invalid-request error. A cursor
stops matching when the membership is removed, the workspace is deleted,
or the service account is archived. Restart pagination from the first
page to recover.

#### Parameters

- `WorkspaceListParams parameters`

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `long limit`

    Query param: Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `JsonElement Type = "service_account_workspace_member"`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
WorkspaceListParams parameters = new()
{
    ServiceAccountID = "service_account_id"
};

var page = await client.Beta.Organization.ServiceAccounts.Workspaces.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "created_by_actor_id": "created_by_actor_id",
      "implicit": true,
      "service_account_id": "service_account_id",
      "type": "service_account_workspace_member",
      "workspace_id": "workspace_id",
      "workspace_role": "workspace_admin"
    }
  ],
  "next_page": "next_page"
}
```

### Remove Workspace From Service Account

`WorkspaceRemoveResponse Beta.Organization.ServiceAccounts.Workspaces.Remove(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Remove a service account from a workspace.

Mirror of `DELETE /workspaces/{workspace_id}/service_accounts/{service_account_id}`,
addressed from the service-account side. Removal is idempotent (returns
200 even if the membership was already removed). A DELETE against the
implicit default-workspace membership returns 200 but is a no-op and the
membership persists; deleting an explicit default-workspace row reverts
to the implicit `workspace_user` membership. Archived workspaces return
400.

#### Parameters

- `WorkspaceRemoveParams parameters`

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class WorkspaceRemoveResponse:`

  - `JsonElement Type = "service_account_workspace_member_deleted"`

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```csharp
WorkspaceRemoveParams parameters = new()
{
    ServiceAccountID = "service_account_id",
    WorkspaceID = "workspace_id",
};

var workspace = await client.Beta.Organization.ServiceAccounts.Workspaces.Remove(parameters);

Console.WriteLine(workspace);
```

##### Response (200)

```json
{
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member_deleted",
  "workspace_id": "workspace_id"
}
```

## Beta › Organization › Users

### List Users

`UserListPage Beta.Organization.Users.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/users`

List the organization's members.

#### Parameters

- `UserListParams parameters`

  - `string afterID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `string email`

    Filter by user email.

    format: email

  - `long limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

  - `IReadOnlyList<string> roles`

    Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

    Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

#### Returns

- `class BetaOrganizationUser:`

  - `JsonElement Type = "user"`

    Object type.

    For Users, this is always `"user"`.

  - `required string ID`

    ID of the User.

  - `required DateTimeOffset AddedAt`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `required string Email`

    Email of the User.

  - `required string Name`

    Name of the User.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin("admin")`

    - `Billing("billing")`

    - `ClaudeCodeUser("claude_code_user")`

    - `Developer("developer")`

    - `Managed("managed")`

    - `MembershipAdmin("membership_admin")`

    - `Owner("owner")`

    - `PrimaryOwner("primary_owner")`

    - `User("user")`

#### Example

```csharp
UserListParams parameters = new();

var page = await client.Beta.Organization.Users.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "added_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "name": "Jane Doe",
      "role": "admin",
      "type": "user"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Get User

`BetaOrganizationUser Beta.Organization.Users.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/users/{user_id}`

Retrieve a member of the organization by user ID.

#### Parameters

- `UserRetrieveParams parameters`

  - `required string userID`

    ID of the User.

#### Returns

- `class BetaOrganizationUser:`

  - `JsonElement Type = "user"`

    Object type.

    For Users, this is always `"user"`.

  - `required string ID`

    ID of the User.

  - `required DateTimeOffset AddedAt`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `required string Email`

    Email of the User.

  - `required string Name`

    Name of the User.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin("admin")`

    - `Billing("billing")`

    - `ClaudeCodeUser("claude_code_user")`

    - `Developer("developer")`

    - `Managed("managed")`

    - `MembershipAdmin("membership_admin")`

    - `Owner("owner")`

    - `PrimaryOwner("primary_owner")`

    - `User("user")`

#### Example

```csharp
UserRetrieveParams parameters = new() { UserID = "user_id" };

var betaOrganizationUser = await client.Beta.Organization.Users.Retrieve(parameters);

Console.WriteLine(betaOrganizationUser);
```

##### Response (200)

```json
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "admin",
  "type": "user"
}
```

### Update User

`BetaOrganizationUser Beta.Organization.Users.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/users/{user_id}`

Update a member's organization role.

#### Parameters

- `UserUpdateParams parameters`

  - `required string userID`

    ID of the User.

  - `required Role role`

    New role for the User.

    The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

    - `Billing("billing")`

    - `ClaudeCodeUser("claude_code_user")`

    - `Developer("developer")`

    - `Managed("managed")`

    - `User("user")`

#### Returns

- `class BetaOrganizationUser:`

  - `JsonElement Type = "user"`

    Object type.

    For Users, this is always `"user"`.

  - `required string ID`

    ID of the User.

  - `required DateTimeOffset AddedAt`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `required string Email`

    Email of the User.

  - `required string Name`

    Name of the User.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin("admin")`

    - `Billing("billing")`

    - `ClaudeCodeUser("claude_code_user")`

    - `Developer("developer")`

    - `Managed("managed")`

    - `MembershipAdmin("membership_admin")`

    - `Owner("owner")`

    - `PrimaryOwner("primary_owner")`

    - `User("user")`

#### Example

```csharp
UserUpdateParams parameters = new()
{
    UserID = "user_id",
    Role = Role.User,
};

var betaOrganizationUser = await client.Beta.Organization.Users.Update(parameters);

Console.WriteLine(betaOrganizationUser);
```

##### Response (200)

```json
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "admin",
  "type": "user"
}
```

### Remove User

`UserRemoveResponse Beta.Organization.Users.Remove(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/users/{user_id}`

Remove a member from the organization.

#### Parameters

- `UserRemoveParams parameters`

  - `required string userID`

    ID of the User.

#### Returns

- `class UserRemoveResponse:`

  - `JsonElement Type = "user_deleted"`

    Deleted object type.

    For Users, this is always `"user_deleted"`.

  - `required string ID`

    ID of the User.

#### Example

```csharp
UserRemoveParams parameters = new() { UserID = "user_id" };

var user = await client.Beta.Organization.Users.Remove(parameters);

Console.WriteLine(user);
```

##### Response (200)

```json
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "type": "user_deleted"
}
```

## Beta › Organization › Workspaces

### List Workspaces

`WorkspaceListPage Beta.Organization.Workspaces.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces`

List Workspaces

#### Parameters

- `WorkspaceListParams parameters`

  - `string afterID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `bool includeArchived`

    Whether to include Workspaces that have been archived in the response

  - `long limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

#### Returns

- `class BetaWorkspace:`

  - `JsonElement Type = "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

  - `required string ID`

    ID of the Workspace.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `required string CompartmentID`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK
    integration guide for the required key configuration; unless your organization
    is on Claude Platform on AWS, it includes a separate value used during key
    validation. On Claude Platform on AWS there is no separate validation value:
    the key is validated against this Workspace's own value when it is attached, so
    if your key policy uses the compartment condition, add this value to it before
    attaching the key.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `required BetaDataResidency DataResidency`

    Data residency configuration.

    - `required AllowedInferenceGeos AllowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `IReadOnlyList<string>`

      - `class Unrestricted:`

    - `required string DefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `required string WorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `required string DisplayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `required string? ExternalKeyID`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value is the AWS KMS key ARN, and the key must be a
    single-Region key in the same AWS account and Region as the Workspace. On that
    platform the key is validated against this Workspace when it is attached, so a
    key-policy problem is reported as an error on this request. This field is write-once:
    once a key is attached to a Workspace it cannot be detached or replaced. To
    rotate key material, rotate the underlying key on your cloud KMS; the
    `external_key_id` stays the same.

  - `required string Name`

    Name of the Workspace.

  - `required IReadOnlyDictionary<string, string> Tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```csharp
WorkspaceListParams parameters = new();

var page = await client.Beta.Organization.Workspaces.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "data_residency": {
        "allowed_inference_geos": "unrestricted",
        "default_inference_geo": "default_inference_geo",
        "workspace_geo": "workspace_geo"
      },
      "display_color": "#6C5BB9",
      "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
      "name": "Workspace Name",
      "tags": {
        "env": "prod",
        "team": "platform"
      },
      "type": "workspace"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Create Workspace

`BetaWorkspace Beta.Organization.Workspaces.Create(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces`

Create Workspace

#### Parameters

- `WorkspaceCreateParams parameters`

  - `required string name`

    Body param: Name of the Workspace.

    maxLength: 40, minLength: 1

  - `BetaDataResidencyCreateConfig? dataResidency`

    Body param: Data residency configuration for the workspace. If omitted, defaults to `workspace_geo: "us"`, `allowed_inference_geos: "unrestricted"`, and `default_inference_geo: "global"`.

  - `string? displayColor`

    Body param: Hex color code representing the Workspace in the Anthropic Console.

    maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

  - `string? externalKeyID`

    Body param: ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value is the AWS KMS key ARN, and the key must be a
    single-Region key in the same AWS account and Region as the Workspace. On that
    platform the key is validated against this Workspace when it is attached, so a
    key-policy problem is reported as an error on this request. This field is write-once:
    once a key is attached to a Workspace it cannot be detached or replaced. To
    rotate key material, rotate the underlying key on your cloud KMS; the
    `external_key_id` stays the same.

  - `IReadOnlyDictionary<string, string>? tags`

    Body param: User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaWorkspace:`

  - `JsonElement Type = "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

  - `required string ID`

    ID of the Workspace.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `required string CompartmentID`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK
    integration guide for the required key configuration; unless your organization
    is on Claude Platform on AWS, it includes a separate value used during key
    validation. On Claude Platform on AWS there is no separate validation value:
    the key is validated against this Workspace's own value when it is attached, so
    if your key policy uses the compartment condition, add this value to it before
    attaching the key.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `required BetaDataResidency DataResidency`

    Data residency configuration.

    - `required AllowedInferenceGeos AllowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `IReadOnlyList<string>`

      - `class Unrestricted:`

    - `required string DefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `required string WorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `required string DisplayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `required string? ExternalKeyID`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value is the AWS KMS key ARN, and the key must be a
    single-Region key in the same AWS account and Region as the Workspace. On that
    platform the key is validated against this Workspace when it is attached, so a
    key-policy problem is reported as an error on this request. This field is write-once:
    once a key is attached to a Workspace it cannot be detached or replaced. To
    rotate key material, rotate the underlying key on your cloud KMS; the
    `external_key_id` stays the same.

  - `required string Name`

    Name of the Workspace.

  - `required IReadOnlyDictionary<string, string> Tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```csharp
WorkspaceCreateParams parameters = new() { Name = "x" };

var betaWorkspace = await client.Beta.Organization.Workspaces.Create(parameters);

Console.WriteLine(betaWorkspace);
```

##### Response (200)

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

### Get Workspace

`BetaWorkspace Beta.Organization.Workspaces.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces/{workspace_id}`

Get Workspace

#### Parameters

- `WorkspaceRetrieveParams parameters`

  - `required string workspaceID`

    ID of the Workspace.

#### Returns

- `class BetaWorkspace:`

  - `JsonElement Type = "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

  - `required string ID`

    ID of the Workspace.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `required string CompartmentID`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK
    integration guide for the required key configuration; unless your organization
    is on Claude Platform on AWS, it includes a separate value used during key
    validation. On Claude Platform on AWS there is no separate validation value:
    the key is validated against this Workspace's own value when it is attached, so
    if your key policy uses the compartment condition, add this value to it before
    attaching the key.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `required BetaDataResidency DataResidency`

    Data residency configuration.

    - `required AllowedInferenceGeos AllowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `IReadOnlyList<string>`

      - `class Unrestricted:`

    - `required string DefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `required string WorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `required string DisplayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `required string? ExternalKeyID`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value is the AWS KMS key ARN, and the key must be a
    single-Region key in the same AWS account and Region as the Workspace. On that
    platform the key is validated against this Workspace when it is attached, so a
    key-policy problem is reported as an error on this request. This field is write-once:
    once a key is attached to a Workspace it cannot be detached or replaced. To
    rotate key material, rotate the underlying key on your cloud KMS; the
    `external_key_id` stays the same.

  - `required string Name`

    Name of the Workspace.

  - `required IReadOnlyDictionary<string, string> Tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```csharp
WorkspaceRetrieveParams parameters = new() { WorkspaceID = "workspace_id" };

var betaWorkspace = await client.Beta.Organization.Workspaces.Retrieve(parameters);

Console.WriteLine(betaWorkspace);
```

##### Response (200)

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

### Update Workspace

`BetaWorkspace Beta.Organization.Workspaces.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces/{workspace_id}`

Update Workspace

#### Parameters

- `WorkspaceUpdateParams parameters`

  - `required string workspaceID`

  - `BetaDataResidencyUpdateConfig? dataResidency`

    Data residency configuration for the workspace.

  - `string displayColor`

    Hex color code representing the Workspace in the Anthropic Console.

    maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

  - `string externalKeyID`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value is the AWS KMS key ARN, and the key must be a
    single-Region key in the same AWS account and Region as the Workspace. On that
    platform the key is validated against this Workspace when it is attached, so a
    key-policy problem is reported as an error on this request. This field is write-once:
    once a key is attached to a Workspace it cannot be detached or replaced. To
    rotate key material, rotate the underlying key on your cloud KMS; the
    `external_key_id` stays the same.

  - `string name`

    Name of the Workspace.

    maxLength: 40, minLength: 1

  - `IReadOnlyDictionary<string, string>? tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Returns

- `class BetaWorkspace:`

  - `JsonElement Type = "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

  - `required string ID`

    ID of the Workspace.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `required string CompartmentID`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK
    integration guide for the required key configuration; unless your organization
    is on Claude Platform on AWS, it includes a separate value used during key
    validation. On Claude Platform on AWS there is no separate validation value:
    the key is validated against this Workspace's own value when it is attached, so
    if your key policy uses the compartment condition, add this value to it before
    attaching the key.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `required BetaDataResidency DataResidency`

    Data residency configuration.

    - `required AllowedInferenceGeos AllowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `IReadOnlyList<string>`

      - `class Unrestricted:`

    - `required string DefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `required string WorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `required string DisplayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `required string? ExternalKeyID`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value is the AWS KMS key ARN, and the key must be a
    single-Region key in the same AWS account and Region as the Workspace. On that
    platform the key is validated against this Workspace when it is attached, so a
    key-policy problem is reported as an error on this request. This field is write-once:
    once a key is attached to a Workspace it cannot be detached or replaced. To
    rotate key material, rotate the underlying key on your cloud KMS; the
    `external_key_id` stays the same.

  - `required string Name`

    Name of the Workspace.

  - `required IReadOnlyDictionary<string, string> Tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```csharp
WorkspaceUpdateParams parameters = new() { WorkspaceID = "workspace_id" };

var betaWorkspace = await client.Beta.Organization.Workspaces.Update(parameters);

Console.WriteLine(betaWorkspace);
```

##### Response (200)

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

### Archive Workspace

`BetaWorkspace Beta.Organization.Workspaces.Archive(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces/{workspace_id}/archive`

Archive Workspace

#### Parameters

- `WorkspaceArchiveParams parameters`

  - `required string workspaceID`

#### Returns

- `class BetaWorkspace:`

  - `JsonElement Type = "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

  - `required string ID`

    ID of the Workspace.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `required string CompartmentID`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK
    integration guide for the required key configuration; unless your organization
    is on Claude Platform on AWS, it includes a separate value used during key
    validation. On Claude Platform on AWS there is no separate validation value:
    the key is validated against this Workspace's own value when it is attached, so
    if your key policy uses the compartment condition, add this value to it before
    attaching the key.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `required BetaDataResidency DataResidency`

    Data residency configuration.

    - `required AllowedInferenceGeos AllowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `IReadOnlyList<string>`

      - `class Unrestricted:`

    - `required string DefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `required string WorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `required string DisplayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `required string? ExternalKeyID`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value is the AWS KMS key ARN, and the key must be a
    single-Region key in the same AWS account and Region as the Workspace. On that
    platform the key is validated against this Workspace when it is attached, so a
    key-policy problem is reported as an error on this request. This field is write-once:
    once a key is attached to a Workspace it cannot be detached or replaced. To
    rotate key material, rotate the underlying key on your cloud KMS; the
    `external_key_id` stays the same.

  - `required string Name`

    Name of the Workspace.

  - `required IReadOnlyDictionary<string, string> Tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```csharp
WorkspaceArchiveParams parameters = new() { WorkspaceID = "workspace_id" };

var betaWorkspace = await client.Beta.Organization.Workspaces.Archive(parameters);

Console.WriteLine(betaWorkspace);
```

##### Response (200)

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

## Beta › Organization › Workspaces › Rate Limits

### List Workspace Rate Limits

`RateLimitListPage Beta.Organization.Workspaces.RateLimits.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces/{workspace_id}/rate_limits`

List rate-limit overrides configured for a workspace.

Returns only the groups and limiter types that have a workspace-level
override. Groups without overrides inherit the organization limits and
are not listed; use `GET /v1/organizations/rate_limits` to see those.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `RateLimitListParams parameters`

  - `required string workspaceID`

    The ID of the workspace.

  - `GroupType? groupType`

    Filter by group type.

    - `Batch("batch")`

    - `Files("files")`

    - `ModelGroup("model_group")`

    - `Skills("skills")`

    - `TokenCount("token_count")`

    - `WebSearch("web_search")`

  - `long? limit`

    Maximum number of items to return per page. Ranges from `1` to `1000`.

    When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

    maximum: 1000, minimum: 1

  - `string? page`

    Opaque cursor from a previous response's `next_page`.

#### Returns

- `class BetaWorkspaceRateLimit:`

  - `JsonElement Type = "workspace_rate_limit"`

    Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

  - `required GroupType GroupType`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `Batch("batch")`

    - `Files("files")`

    - `ModelGroup("model_group")`

    - `Skills("skills")`

    - `TokenCount("token_count")`

    - `WebSearch("web_search")`

  - `required IReadOnlyList<BetaWorkspaceRateLimitValue> Limits`

    The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.

    - `required string Type`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `required long? OrgLimit`

      The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

    - `required long Value`

      The workspace-level override value for this limiter type.

  - `required IReadOnlyList<string>? Models`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `required string RateLimitID`

    The `id` of the RateLimit group this override applies to.

  - `required string WorkspaceID`

    ID of the Workspace this override applies to.

#### Example

```csharp
RateLimitListParams parameters = new() { WorkspaceID = "workspace_id" };

var page = await client.Beta.Organization.Workspaces.RateLimits.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "group_type": "batch",
      "limits": [
        {
          "org_limit": 0,
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "rate_limit_id": "rate_limit_id",
      "type": "workspace_rate_limit",
      "workspace_id": "workspace_id"
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Workspaces › Members

### List Workspace Members

`MemberListPage Beta.Organization.Workspaces.Members.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces/{workspace_id}/members`

List Workspace Members

#### Parameters

- `MemberListParams parameters`

  - `required string workspaceID`

    ID of the Workspace.

  - `string afterID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `long limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

#### Returns

- `class BetaWorkspaceMember:`

  - `JsonElement Type = "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `required string UserID`

    ID of the User.

  - `required string WorkspaceID`

    ID of the Workspace.

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the Workspace Member.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
MemberListParams parameters = new() { WorkspaceID = "workspace_id" };

var page = await client.Beta.Organization.Workspaces.Members.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "type": "workspace_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "workspace_role": "workspace_admin"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Create Workspace Member

`BetaWorkspaceMember Beta.Organization.Workspaces.Members.Add(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces/{workspace_id}/members`

Create Workspace Member

#### Parameters

- `MemberAddParams parameters`

  - `required string workspaceID`

    ID of the Workspace.

  - `required string userID`

    ID of the User.

  - `required BetaNoBillingWorkspaceRole workspaceRole`

    Role of the new Workspace Member. Cannot be `workspace_billing`.

#### Returns

- `class BetaWorkspaceMember:`

  - `JsonElement Type = "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `required string UserID`

    ID of the User.

  - `required string WorkspaceID`

    ID of the Workspace.

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the Workspace Member.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
MemberAddParams parameters = new()
{
    WorkspaceID = "workspace_id",
    UserID = "user_01WCz1FkmYMm4gnmykNKUu3Q",
    WorkspaceRole = BetaNoBillingWorkspaceRole.WorkspaceAdmin,
};

var betaWorkspaceMember = await client.Beta.Organization.Workspaces.Members.Add(parameters);

Console.WriteLine(betaWorkspaceMember);
```

##### Response (200)

```json
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_admin"
}
```

### Get Workspace Member

`BetaWorkspaceMember Beta.Organization.Workspaces.Members.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Get Workspace Member

#### Parameters

- `MemberRetrieveParams parameters`

  - `required string workspaceID`

    ID of the Workspace.

  - `required string userID`

    ID of the User.

#### Returns

- `class BetaWorkspaceMember:`

  - `JsonElement Type = "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `required string UserID`

    ID of the User.

  - `required string WorkspaceID`

    ID of the Workspace.

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the Workspace Member.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
MemberRetrieveParams parameters = new()
{
    WorkspaceID = "workspace_id",
    UserID = "user_id",
};

var betaWorkspaceMember = await client.Beta.Organization.Workspaces.Members.Retrieve(parameters);

Console.WriteLine(betaWorkspaceMember);
```

##### Response (200)

```json
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_admin"
}
```

### Update Workspace Member

`BetaWorkspaceMember Beta.Organization.Workspaces.Members.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Update Workspace Member

#### Parameters

- `MemberUpdateParams parameters`

  - `required string workspaceID`

    Path param: ID of the Workspace.

  - `required string userID`

    Path param: ID of the User.

  - `required BetaWorkspaceRole workspaceRole`

    Body param: New workspace role for the User.

#### Returns

- `class BetaWorkspaceMember:`

  - `JsonElement Type = "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `required string UserID`

    ID of the User.

  - `required string WorkspaceID`

    ID of the Workspace.

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the Workspace Member.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
MemberUpdateParams parameters = new()
{
    WorkspaceID = "workspace_id",
    UserID = "user_id",
    WorkspaceRole = BetaWorkspaceRole.WorkspaceAdmin,
};

var betaWorkspaceMember = await client.Beta.Organization.Workspaces.Members.Update(parameters);

Console.WriteLine(betaWorkspaceMember);
```

##### Response (200)

```json
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_admin"
}
```

### Delete Workspace Member

`MemberRemoveResponse Beta.Organization.Workspaces.Members.Remove(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Delete Workspace Member

#### Parameters

- `MemberRemoveParams parameters`

  - `required string workspaceID`

    ID of the Workspace.

  - `required string userID`

    ID of the User.

#### Returns

- `class MemberRemoveResponse:`

  - `JsonElement Type = "workspace_member_deleted"`

    Deleted object type.

    For Workspace Members, this is always `"workspace_member_deleted"`.

  - `required string UserID`

    ID of the User.

  - `required string WorkspaceID`

    ID of the Workspace.

#### Example

```csharp
MemberRemoveParams parameters = new()
{
    WorkspaceID = "workspace_id",
    UserID = "user_id",
};

var member = await client.Beta.Organization.Workspaces.Members.Remove(parameters);

Console.WriteLine(member);
```

##### Response (200)

```json
{
  "type": "workspace_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

## Beta › Organization › Workspaces › Service Accounts

### List Service Account Workspace Members

`ServiceAccountListPage Beta.Organization.Workspaces.ServiceAccounts.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces/{workspace_id}/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List the service accounts that are members of a workspace.

Each entry includes the service account's `workspace_role`. Use `limit`
and the `next_page` cursor to paginate. Archived workspaces return 400;
use `GET /service_accounts/{id}/workspaces` to audit memberships of an
archived workspace. The implicit default-workspace membership is not
included in this list. Memberships of archived service accounts are
omitted from the results.

#### Parameters

- `ServiceAccountListParams parameters`

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `long limit`

    Query param: Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `JsonElement Type = "service_account_workspace_member"`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
ServiceAccountListParams parameters = new() { WorkspaceID = "workspace_id" };

var page = await client.Beta.Organization.Workspaces.ServiceAccounts.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "created_by_actor_id": "created_by_actor_id",
      "implicit": true,
      "service_account_id": "service_account_id",
      "type": "service_account_workspace_member",
      "workspace_id": "workspace_id",
      "workspace_role": "workspace_admin"
    }
  ],
  "next_page": "next_page"
}
```

### Create Service Account Workspace Member

`BetaServiceAccountWorkspaceMember Beta.Organization.Workspaces.ServiceAccounts.Add(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces/{workspace_id}/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Add a service account to a workspace with the given `workspace_role`.

The role determines what the service account can do in the workspace and
which workspace-scoped permissions it can be granted when authenticating
through federation. Every service account is already an implicit
`workspace_user` member of the default workspace; adding it explicitly
assigns a chosen role. If the service account is already an explicit
member of the workspace, its `workspace_role` is replaced with the
value supplied here. Archived workspaces return 400. Archived service
accounts cannot be added and are rejected.

#### Parameters

- `ServiceAccountAddParams parameters`

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `required string serviceAccountID`

    Body param: Tagged service account ID to add.

  - `required BetaNoBillingWorkspaceRole workspaceRole`

    Body param: Role to assign to the service account in this workspace.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `JsonElement Type = "service_account_workspace_member"`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
ServiceAccountAddParams parameters = new()
{
    WorkspaceID = "workspace_id",
    ServiceAccountID = "service_account_id",
    WorkspaceRole = BetaNoBillingWorkspaceRole.WorkspaceAdmin,
};

var betaServiceAccountWorkspaceMember = await client.Beta.Organization.Workspaces.ServiceAccounts.Add(parameters);

Console.WriteLine(betaServiceAccountWorkspaceMember);
```

##### Response (200)

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

### Get Service Account Workspace Member

`BetaServiceAccountWorkspaceMember Beta.Organization.Workspaces.ServiceAccounts.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a service account's membership in a workspace.

Returns the membership record, including the service account's
`workspace_role` in this workspace. Archived workspaces return 400. For
the default workspace, returns the implicit (`implicit: true`)
membership when no explicit membership exists; an explicitly added
membership is returned with its assigned role. An archived service
account returns 404.

#### Parameters

- `ServiceAccountRetrieveParams parameters`

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `JsonElement Type = "service_account_workspace_member"`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
ServiceAccountRetrieveParams parameters = new()
{
    WorkspaceID = "workspace_id",
    ServiceAccountID = "service_account_id",
};

var betaServiceAccountWorkspaceMember = await client.Beta.Organization.Workspaces.ServiceAccounts.Retrieve(parameters);

Console.WriteLine(betaServiceAccountWorkspaceMember);
```

##### Response (200)

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

### Update Service Account Workspace Member

`BetaServiceAccountWorkspaceMember Beta.Organization.Workspaces.ServiceAccounts.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Change a service account's role in a workspace.

The new `workspace_role` replaces the current one. Only explicit
memberships can be updated; to set a role on the implicit
default-workspace membership, add the service account explicitly with
`POST /workspaces/{workspace_id}/service_accounts`. Archived workspaces
return 400. Archived service accounts cannot be updated and are
rejected.

#### Parameters

- `ServiceAccountUpdateParams parameters`

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `required BetaNoBillingWorkspaceRole workspaceRole`

    Body param: New role for the service account in this workspace.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `JsonElement Type = "service_account_workspace_member"`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
ServiceAccountUpdateParams parameters = new()
{
    WorkspaceID = "workspace_id",
    ServiceAccountID = "service_account_id",
    WorkspaceRole = BetaNoBillingWorkspaceRole.WorkspaceAdmin,
};

var betaServiceAccountWorkspaceMember = await client.Beta.Organization.Workspaces.ServiceAccounts.Update(parameters);

Console.WriteLine(betaServiceAccountWorkspaceMember);
```

##### Response (200)

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

### Delete Service Account Workspace Member

`ServiceAccountRemoveResponse Beta.Organization.Workspaces.ServiceAccounts.Remove(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Remove a service account from a workspace.

Removal is idempotent (returns 200 even if the membership was already
removed). A DELETE against the implicit default-workspace membership
returns 200 but is a no-op and the membership persists; deleting an
explicit default-workspace row reverts to the implicit `workspace_user`
membership. Archived workspaces return 400.

#### Parameters

- `ServiceAccountRemoveParams parameters`

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class ServiceAccountRemoveResponse:`

  - `JsonElement Type = "service_account_workspace_member_deleted"`

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```csharp
ServiceAccountRemoveParams parameters = new()
{
    WorkspaceID = "workspace_id",
    ServiceAccountID = "service_account_id",
};

var serviceAccount = await client.Beta.Organization.Workspaces.ServiceAccounts.Remove(parameters);

Console.WriteLine(serviceAccount);
```

##### Response (200)

```json
{
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member_deleted",
  "workspace_id": "workspace_id"
}
```

## Beta › Organization › Rate Limits

### List Organization Rate Limits

`RateLimitListPage Beta.Organization.RateLimits.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/rate_limits`

List Messages API rate limits for your organization.

Each entry corresponds to one rate-limit group (either a model family
or an API-surface category such as the Files API or Message Batches)
and contains the set of limiter values that apply to it.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `RateLimitListParams parameters`

  - `GroupType? groupType`

    Filter by group type.

    - `Batch("batch")`

    - `Files("files")`

    - `ModelGroup("model_group")`

    - `Skills("skills")`

    - `TokenCount("token_count")`

    - `WebSearch("web_search")`

  - `long? limit`

    Maximum number of items to return per page. Ranges from `1` to `1000`.

    When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

    maximum: 1000, minimum: 1

  - `string? model`

    Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

  - `string? page`

    Opaque cursor from a previous response's `next_page`.

#### Returns

- `class BetaOrganizationRateLimit:`

  - `JsonElement Type = "rate_limit"`

    Object type. Always `rate_limit` for organization rate-limit entries.

  - `required string ID`

    Stable identifier for this rate-limit group within the organization.

  - `required GroupType GroupType`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `Batch("batch")`

    - `Files("files")`

    - `ModelGroup("model_group")`

    - `Skills("skills")`

    - `TokenCount("token_count")`

    - `WebSearch("web_search")`

  - `required IReadOnlyList<BetaOrganizationRateLimitValue> Limits`

    The limiter values that apply to this group.

    - `required string Type`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `required long Value`

      The configured limit value for this limiter type.

  - `required IReadOnlyList<string>? Models`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

#### Example

```csharp
RateLimitListParams parameters = new();

var page = await client.Beta.Organization.RateLimits.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "group_type": "batch",
      "limits": [
        {
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "type": "rate_limit"
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Compliance Settings

### Get Compliance Settings

`BetaComplianceSettings Beta.Organization.ComplianceSettings.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/compliance_settings`

Retrieve your organization's Compliance Settings.

Compliance Settings is a singleton resource: there is exactly one per
organization, addressed without an identifier. The `state` field reflects
whether the Compliance API is enabled. An organization with a parent
organization reads the state inherited from the parent's configuration.

#### Parameters

- `ComplianceSettingRetrieveParams parameters`

#### Returns

- `class BetaComplianceSettings:`

  - `JsonElement Type = "compliance_settings"`

  - `required BetaComplianceSettingsState State`

    Whether the Compliance API is enabled for this organization.

    - `class BetaComplianceSettingsStateEnabled:`

      - `JsonElement Type = "enabled"`

    - `class BetaComplianceSettingsStateDisabled:`

      - `JsonElement Type = "disabled"`

#### Example

```csharp
ComplianceSettingRetrieveParams parameters = new();

var betaComplianceSettings = await client.Beta.Organization.ComplianceSettings.Retrieve(parameters);

Console.WriteLine(betaComplianceSettings);
```

##### Response (200)

```json
{
  "state": {
    "type": "enabled"
  },
  "type": "compliance_settings"
}
```

### Update Compliance Settings

`BetaComplianceSettings Beta.Organization.ComplianceSettings.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/compliance_settings`

Update your organization's Compliance Settings.

Setting `state` to `enabled` turns on the Compliance API and begins
capturing organization activity events. Setting it to `disabled` turns
both off. `state` reflects whether the Compliance API is enabled.

A request that sets `state` to its current value succeeds and leaves the
resource unchanged. A `disabled` request stays in effect until a later
`enabled` request or the organization's next provisioning action that
enables Access Transparency: enabling Access Transparency also enables
the Compliance API, which serves its activity events, so such
provisioning (including re-runs) re-enables the Compliance API even
after a `disabled` request. Automated provisioning never disables
compliance settings.

#### Parameters

- `ComplianceSettingUpdateParams parameters`

  - `required BetaComplianceSettingsStateParam state`

    Desired state. Accepts the string shorthand "enabled" or "disabled" in place of the object form; the response always returns the canonical object form.

#### Returns

- `class BetaComplianceSettings:`

  - `JsonElement Type = "compliance_settings"`

  - `required BetaComplianceSettingsState State`

    Whether the Compliance API is enabled for this organization.

    - `class BetaComplianceSettingsStateEnabled:`

      - `JsonElement Type = "enabled"`

    - `class BetaComplianceSettingsStateDisabled:`

      - `JsonElement Type = "disabled"`

#### Example

```csharp
ComplianceSettingUpdateParams parameters = new()
{
    State = new BetaComplianceSettingsStateEnabledParam()
};

var betaComplianceSettings = await client.Beta.Organization.ComplianceSettings.Update(parameters);

Console.WriteLine(betaComplianceSettings);
```

##### Response (200)

```json
{
  "state": {
    "type": "enabled"
  },
  "type": "compliance_settings"
}
```
