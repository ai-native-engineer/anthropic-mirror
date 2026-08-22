<!-- source: https://platform.claude.com/docs/en/api/csharp/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/csharp/beta -->

<!-- chunk-start -->

        Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

      - `required Type Type`

        - `"limited"Limited`

  - `string? SecretValue`

    Updated secret value.

### Beta Managed Agents Injection Location Params

- `class BetaManagedAgentsInjectionLocationParams:`

  Where in the outbound request the secret value may be substituted.

  - `Boolean Body`

    Substitute when the placeholder appears in the request body.

  - `Boolean Header`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Injection Location Response

- `class BetaManagedAgentsInjectionLocationResponse:`

  Where in the outbound request the secret value is substituted.

  - `required Boolean Body`

    Whether the placeholder is substituted in the request body.

  - `required Boolean Header`

    Whether the placeholder is substituted in request header values.

### Beta Managed Agents Injection Location Update Params

- `class BetaManagedAgentsInjectionLocationUpdateParams:`

  Updated injection location.

  - `Boolean Body`

    Substitute when the placeholder appears in the request body.

  - `Boolean Header`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Limited Credential Networking Params

- `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

  Substitute the secret only on requests to the listed hosts.

  - `required IReadOnlyList<string> AllowedHosts`

    Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

  - `required Type Type`

    - `"limited"Limited`

### Beta Managed Agents Limited Credential Networking Response

- `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

  The secret is substituted only on requests to the listed hosts.

  - `required IReadOnlyList<string> AllowedHosts`

    Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

  - `required Type Type`

    - `"limited"Limited`

### Beta Managed Agents MCP OAuth Auth Response

- `class BetaManagedAgentsMcpOAuthAuthResponse:`

  OAuth credential details for an MCP server.

  - `required string McpServerUrl`

    URL of the MCP server this credential authenticates against.

  - `required Type Type`

    - `"mcp_oauth"McpOAuth`

  - `DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsMcpOAuthRefreshResponse? Refresh`

    OAuth refresh token configuration returned in credential responses.

    - `required string ClientID`

      OAuth client ID.

    - `required string TokenEndpoint`

      Token endpoint URL used to refresh the access token.

    - `required TokenEndpointAuth TokenEndpointAuth`

      Token endpoint requires no client authentication.

      - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

        Token endpoint requires no client authentication.

        - `required Type Type`

          - `"none"None`

      - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `required Type Type`

          - `"client_secret_basic"ClientSecretBasic`

      - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

        Token endpoint uses POST body authentication with client credentials.

        - `required Type Type`

          - `"client_secret_post"ClientSecretPost`

    - `string? Resource`

      OAuth resource indicator.

    - `string? Scope`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Create Params

- `class BetaManagedAgentsMcpOAuthCreateParams:`

  Parameters for creating an MCP OAuth credential.

  - `required string AccessToken`

    OAuth access token.

  - `required string McpServerUrl`

    URL of the MCP server this credential authenticates against.

  - `required Type Type`

    - `"mcp_oauth"McpOAuth`

  - `DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsMcpOAuthRefreshParams? Refresh`

    OAuth refresh token parameters for creating a credential with refresh support.

    - `required string ClientID`

      OAuth client ID.

    - `required string RefreshToken`

      OAuth refresh token.

    - `required string TokenEndpoint`

      Token endpoint URL used to refresh the access token.

    - `required TokenEndpointAuth TokenEndpointAuth`

      Token endpoint requires no client authentication.

      - `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

        Token endpoint requires no client authentication.

        - `required Type Type`

          - `"none"None`

      - `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `required string ClientSecret`

          OAuth client secret.

        - `required Type Type`

          - `"client_secret_basic"ClientSecretBasic`

      - `class BetaManagedAgentsTokenEndpointAuthPostParam:`

        Token endpoint uses POST body authentication with client credentials.

        - `required string ClientSecret`

          OAuth client secret.

        - `required Type Type`

          - `"client_secret_post"ClientSecretPost`

    - `string? Resource`

      OAuth resource indicator.

    - `string? Scope`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Params

- `class BetaManagedAgentsMcpOAuthRefreshParams:`

  OAuth refresh token parameters for creating a credential with refresh support.

  - `required string ClientID`

    OAuth client ID.

  - `required string RefreshToken`

    OAuth refresh token.

  - `required string TokenEndpoint`

    Token endpoint URL used to refresh the access token.

  - `required TokenEndpointAuth TokenEndpointAuth`

    Token endpoint requires no client authentication.

    - `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

      Token endpoint requires no client authentication.

      - `required Type Type`

        - `"none"None`

    - `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `required string ClientSecret`

        OAuth client secret.

      - `required Type Type`

        - `"client_secret_basic"ClientSecretBasic`

    - `class BetaManagedAgentsTokenEndpointAuthPostParam:`

      Token endpoint uses POST body authentication with client credentials.

      - `required string ClientSecret`

        OAuth client secret.

      - `required Type Type`

        - `"client_secret_post"ClientSecretPost`

  - `string? Resource`

    OAuth resource indicator.

  - `string? Scope`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Response

- `class BetaManagedAgentsMcpOAuthRefreshResponse:`

  OAuth refresh token configuration returned in credential responses.

  - `required string ClientID`

    OAuth client ID.

  - `required string TokenEndpoint`

    Token endpoint URL used to refresh the access token.

  - `required TokenEndpointAuth TokenEndpointAuth`

    Token endpoint requires no client authentication.

    - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

      Token endpoint requires no client authentication.

      - `required Type Type`

        - `"none"None`

    - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `required Type Type`

        - `"client_secret_basic"ClientSecretBasic`

    - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

      Token endpoint uses POST body authentication with client credentials.

      - `required Type Type`

        - `"client_secret_post"ClientSecretPost`

  - `string? Resource`

    OAuth resource indicator.

  - `string? Scope`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Update Params

- `class BetaManagedAgentsMcpOAuthRefreshUpdateParams:`

  Parameters for updating OAuth refresh token configuration.

  - `string? RefreshToken`

    Updated OAuth refresh token.

  - `string? Scope`

    Updated OAuth scope for the refresh request.

  - `TokenEndpointAuth TokenEndpointAuth`

    Updated HTTP Basic authentication parameters for the token endpoint.

    - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `required Type Type`

        - `"client_secret_basic"ClientSecretBasic`

      - `string? ClientSecret`

        Updated OAuth client secret.

    - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

      Updated POST body authentication parameters for the token endpoint.

      - `required Type Type`

        - `"client_secret_post"ClientSecretPost`

      - `string? ClientSecret`

        Updated OAuth client secret.

### Beta Managed Agents MCP OAuth Update Params

- `class BetaManagedAgentsMcpOAuthUpdateParams:`

  Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

  - `required Type Type`

    - `"mcp_oauth"McpOAuth`

  - `string? AccessToken`

    Updated OAuth access token.

  - `DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsMcpOAuthRefreshUpdateParams? Refresh`

    Parameters for updating OAuth refresh token configuration.

    - `string? RefreshToken`

      Updated OAuth refresh token.

    - `string? Scope`

      Updated OAuth scope for the refresh request.

    - `TokenEndpointAuth TokenEndpointAuth`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `required Type Type`

          - `"client_secret_basic"ClientSecretBasic`

        - `string? ClientSecret`

          Updated OAuth client secret.

      - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

        Updated POST body authentication parameters for the token endpoint.

        - `required Type Type`

          - `"client_secret_post"ClientSecretPost`

        - `string? ClientSecret`

          Updated OAuth client secret.

### Beta Managed Agents MCP Probe

- `class BetaManagedAgentsMcpProbe:`

  The failing step of an MCP validation probe.

  - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

    An HTTP response captured during a credential validation probe.

    - `required string Body`

      Response body. May be truncated and has sensitive values scrubbed.

    - `required Boolean BodyTruncated`

      Whether `body` was truncated.

    - `required string ContentType`

      Value of the `Content-Type` response header.

    - `required Int StatusCode`

      HTTP status code.

  - `required string Method`

    The MCP method that failed (for example `initialize` or `tools/list`).

### Beta Managed Agents Refresh HTTP Response

- `class BetaManagedAgentsRefreshHttpResponse:`

  An HTTP response captured during a credential validation probe.

  - `required string Body`

    Response body. May be truncated and has sensitive values scrubbed.

  - `required Boolean BodyTruncated`

    Whether `body` was truncated.

  - `required string ContentType`

    Value of the `Content-Type` response header.

  - `required Int StatusCode`

    HTTP status code.

### Beta Managed Agents Refresh Object

- `class BetaManagedAgentsRefreshObject:`

  Outcome of a refresh-token exchange attempted during credential validation.

  - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

    An HTTP response captured during a credential validation probe.

    - `required string Body`

      Response body. May be truncated and has sensitive values scrubbed.

    - `required Boolean BodyTruncated`

      Whether `body` was truncated.

    - `required string ContentType`

      Value of the `Content-Type` response header.

    - `required Int StatusCode`

      HTTP status code.

  - `required Status Status`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `"succeeded"Succeeded`

    - `"failed"Failed`

    - `"connect_error"ConnectError`

    - `"no_refresh_token"NoRefreshToken`

### Beta Managed Agents Static Bearer Auth Response

- `class BetaManagedAgentsStaticBearerAuthResponse:`

  Static bearer token credential details for an MCP server.

  - `required string McpServerUrl`

    URL of the MCP server this credential authenticates against.

  - `required Type Type`

    - `"static_bearer"StaticBearer`

### Beta Managed Agents Static Bearer Create Params

- `class BetaManagedAgentsStaticBearerCreateParams:`

  Parameters for creating a static bearer token credential.

  - `required string Token`

    Static bearer token value.

  - `required string McpServerUrl`

    URL of the MCP server this credential authenticates against.

  - `required Type Type`

    - `"static_bearer"StaticBearer`

### Beta Managed Agents Static Bearer Update Params

- `class BetaManagedAgentsStaticBearerUpdateParams:`

  Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

  - `required Type Type`

    - `"static_bearer"StaticBearer`

  - `string? Token`

    Updated static bearer token value.

### Beta Managed Agents Token Endpoint Auth Basic Param

- `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `required string ClientSecret`

    OAuth client secret.

  - `required Type Type`

    - `"client_secret_basic"ClientSecretBasic`

### Beta Managed Agents Token Endpoint Auth Basic Response

- `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `required Type Type`

    - `"client_secret_basic"ClientSecretBasic`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

  Updated HTTP Basic authentication parameters for the token endpoint.

  - `required Type Type`

    - `"client_secret_basic"ClientSecretBasic`

  - `string? ClientSecret`

    Updated OAuth client secret.

### Beta Managed Agents Token Endpoint Auth None Param

- `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

  Token endpoint requires no client authentication.

  - `required Type Type`

    - `"none"None`

### Beta Managed Agents Token Endpoint Auth None Response

- `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

  Token endpoint requires no client authentication.

  - `required Type Type`

    - `"none"None`

### Beta Managed Agents Token Endpoint Auth Post Param

- `class BetaManagedAgentsTokenEndpointAuthPostParam:`

  Token endpoint uses POST body authentication with client credentials.

  - `required string ClientSecret`

    OAuth client secret.

  - `required Type Type`

    - `"client_secret_post"ClientSecretPost`

### Beta Managed Agents Token Endpoint Auth Post Response

- `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

  Token endpoint uses POST body authentication with client credentials.

  - `required Type Type`

    - `"client_secret_post"ClientSecretPost`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

  Updated POST body authentication parameters for the token endpoint.

  - `required Type Type`

    - `"client_secret_post"ClientSecretPost`

  - `string? ClientSecret`

    Updated OAuth client secret.

### Beta Managed Agents Unrestricted Credential Networking Params

- `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `required Type Type`

    - `"unrestricted"Unrestricted`

### Beta Managed Agents Unrestricted Credential Networking Response

- `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

  The secret is substituted on any host the session's Environment network policy permits egress to.

  - `required Type Type`

    - `"unrestricted"Unrestricted`

# Memory Stores

## Create a memory store

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Create(MemoryStoreCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores`

Create a memory store

### Parameters

- `MemoryStoreCreateParams parameters`

  - `required string name`

    Body param: Human-readable name for the store. Required; 1–255 characters; no control characters. The mount-path slug under `/mnt/memory/` is derived from this name (lowercased, non-alphanumeric runs collapsed to a hyphen). Names need not be unique within a workspace.

  - `string description`

    Body param: Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent.

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Not visible to the agent.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `required string ID`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required Type Type`

    - `"memory_store"MemoryStore`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `string Description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```csharp
MemoryStoreCreateParams parameters = new() { Name = "x" };

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Create(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

## List memory stores

`MemoryStoreListPageResponse Beta.MemoryStores.List(MemoryStoreListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores`

List memory stores

### Parameters

- `MemoryStoreListParams parameters`

  - `DateTimeOffset createdAtGte`

    Query param: Return only stores whose `created_at` is at or after this time (inclusive). Sent on the wire as `created_at[gte]`.

  - `DateTimeOffset createdAtLte`

    Query param: Return only stores whose `created_at` is at or before this time (inclusive). Sent on the wire as `created_at[lte]`.

  - `Boolean includeArchived`

    Query param: When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

  - `Int limit`

    Query param: Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

  - `string page`

    Query param: Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class MemoryStoreListPageResponse:`

  A page of `memory_store` results, ordered by `created_at` descending (newest first).

  - `IReadOnlyList<BetaManagedAgentsMemoryStore> Data`

    Memory stores on this page, newest first. Empty when there are no stores matching the filters.

    - `required string ID`

      Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string Name`

      Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

    - `required Type Type`

      - `"memory_store"MemoryStore`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

    - `DateTimeOffset? ArchivedAt`

      A timestamp in RFC 3339 format

    - `string Description`

      Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

    - `IReadOnlyDictionary<string, string> Metadata`

      Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

  - `string? NextPage`

    Opaque cursor for the next page (a `page_...` value). Pass as `page` on the next request. `null` when there are no more results.

### Example

```csharp
MemoryStoreListParams parameters = new();

var page = await client.Beta.MemoryStores.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "name": "name",
      "type": "memory_store",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "metadata": {
        "foo": "string"
      }
    }
  ],
  "next_page": "next_page"
}
```

## Retrieve a memory store

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Retrieve(MemoryStoreRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores/{memory_store_id}`

Retrieve a memory store

### Parameters

- `MemoryStoreRetrieveParams parameters`

  - `required string memoryStoreID`

    Path parameter memory_store_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `required string ID`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required Type Type`

    - `"memory_store"MemoryStore`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `string Description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```csharp
MemoryStoreRetrieveParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

## Update a memory store

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Update(MemoryStoreUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores/{memory_store_id}`

Update a memory store

### Parameters

- `MemoryStoreUpdateParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `string? description`

    Body param: New description for the store, up to 1024 characters. Pass an empty string to clear it.

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `string? name`

    Body param: New human-readable name for the store. 1–255 characters; no control characters. Renaming changes the slug used for the store's `mount_path` in sessions created after the update.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `required string ID`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required Type Type`

    - `"memory_store"MemoryStore`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `string Description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```csharp
MemoryStoreUpdateParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Update(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

## Delete a memory store

`BetaManagedAgentsDeletedMemoryStore Beta.MemoryStores.Delete(MemoryStoreDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/memory_stores/{memory_store_id}`

Delete a memory store

### Parameters

- `MemoryStoreDeleteParams parameters`

  - `required string memoryStoreID`

    Path parameter memory_store_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsDeletedMemoryStore:`

  Confirmation that a `memory_store` was deleted.

  - `required string ID`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `required Type Type`

    - `"memory_store_deleted"MemoryStoreDeleted`

### Example

```csharp
MemoryStoreDeleteParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsDeletedMemoryStore = await client.Beta.MemoryStores.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedMemoryStore);
```

#### Response

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

## Archive a memory store

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Archive(MemoryStoreArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores/{memory_store_id}/archive`

Archive a memory store

### Parameters

- `MemoryStoreArchiveParams parameters`

  - `required string memoryStoreID`

    Path parameter memory_store_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `required string ID`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required Type Type`

    - `"memory_store"MemoryStore`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `string Description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```csharp
MemoryStoreArchiveParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Archive(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

## Domain Types

### Beta Managed Agents Deleted Memory Store

- `class BetaManagedAgentsDeletedMemoryStore:`

  Confirmation that a `memory_store` was deleted.

  - `required string ID`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `required Type Type`

    - `"memory_store_deleted"MemoryStoreDeleted`

### Beta Managed Agents Memory Store

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `required string ID`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required Type Type`

    - `"memory_store"MemoryStore`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `string Description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

# Memories

## Create a memory

`BetaManagedAgentsMemory Beta.MemoryStores.Memories.Create(MemoryCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores/{memory_store_id}/memories`

Create a memory

### Parameters

- `MemoryCreateParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string? content`

    Body param: UTF-8 text content for the new memory. Maximum 100 kB (102,400 bytes). Required; pass `""` explicitly to create an empty memory.

  - `required string path`

    Body param: Hierarchical path for the new memory, e.g. `/projects/foo/notes.md`. Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive.

  - `BetaManagedAgentsMemoryView view`

    Query param: Query parameter for view

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `required string ID`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `required string ContentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `required Int ContentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `required string MemoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `required string Path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `required Type Type`

    - `"memory"Memory`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? Content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```csharp
MemoryCreateParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    Content = "content",
    Path = "xx",
};

var betaManagedAgentsMemory = await client.Beta.MemoryStores.Memories.Create(parameters);

Console.WriteLine(betaManagedAgentsMemory);
```

#### Response

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

## List memories

`MemoryListPageResponse Beta.MemoryStores.Memories.List(MemoryListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores/{memory_store_id}/memories`

List memories

### Parameters

- `MemoryListParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `Int depth`

    Query param: `0` (or omitted) returns all descendants below `path_prefix` (recursive). `1` returns immediate children only; deeper entries roll up as `memory_prefix` items. `depth=1` behaves like `ls`; omitting `depth` behaves like `find`.

  - `Int limit`

    Query param: Maximum number of items to return per page. Must be between 1 and 100. Defaults to 20 when omitted. Capped at 20 when `view=full`. Both `memory` and `memory_prefix` items count toward the limit.

  - `string page`

    Query param: Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

  - `string pathPrefix`

    Query param: Optional path prefix filter. Must end with `/` (segment-aligned), e.g., `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

  - `BetaManagedAgentsMemoryView view`

    Query param: Which projection of each `memory` to return. Defaults to `basic` (content omitted). `full` populates `content` on each item and caps `limit` at 20; use this as the bulk-read path for export and sync.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class MemoryListPageResponse:`

  Response payload for [List memories](/docs/en/api/beta/memory_stores/memories/list).

  - `IReadOnlyList<BetaManagedAgentsMemoryListItem> Data`

    One page of results. Each item is either a `memory` object or, when `depth` was set, a `memory_prefix` rollup marker. Items are returned in a stable, server-defined order.

    - `class BetaManagedAgentsMemory:`

      A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

      - `required string ID`

        Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

      - `required string ContentSha256`

        Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

      - `required Int ContentSizeBytes`

        Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

      - `required DateTimeOffset CreatedAt`

        A timestamp in RFC 3339 format

      - `required string MemoryStoreID`

        ID of the memory store this memory belongs to (a `memstore_...` value).

      - `required string MemoryVersionID`

        ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

      - `required string Path`

        Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

      - `required Type Type`

        - `"memory"Memory`

      - `required DateTimeOffset UpdatedAt`

        A timestamp in RFC 3339 format

      - `string? Content`

        The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

    - `class BetaManagedAgentsMemoryPrefix:`

      A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

      - `required string Path`

        The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

      - `required Type Type`

        - `"memory_prefix"MemoryPrefix`

  - `string? NextPage`

    Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.

### Example

```csharp
MemoryListParams parameters = new() { MemoryStoreID = "memory_store_id" };

var page = await client.Beta.MemoryStores.Memories.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_store_id": "memory_store_id",
      "memory_version_id": "memory_version_id",
      "path": "path",
      "type": "memory",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "content": "content"
    }
  ],
  "next_page": "next_page"
}
```

## Retrieve a memory

`BetaManagedAgentsMemory Beta.MemoryStores.Memories.Retrieve(MemoryRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a memory

### Parameters

- `MemoryRetrieveParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryID`

    Path param: Path parameter memory_id

  - `BetaManagedAgentsMemoryView view`

    Query param: Query parameter for view

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `required string ID`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `required string ContentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `required Int ContentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `required string MemoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `required string Path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `required Type Type`

    - `"memory"Memory`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? Content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```csharp
MemoryRetrieveParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryID = "memory_id",
};

var betaManagedAgentsMemory = await client.Beta.MemoryStores.Memories.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsMemory);
```

#### Response

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

## Update a memory

`BetaManagedAgentsMemory Beta.MemoryStores.Memories.Update(MemoryUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a memory

### Parameters

- `MemoryUpdateParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryID`

    Path param: Path parameter memory_id

  - `BetaManagedAgentsMemoryView view`

    Query param: Query parameter for view

  - `string? content`

    Body param: New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

  - `string? path`

    Body param: New path for the memory (a rename). Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive. The memory's `id` is preserved across renames. Omit to leave the path unchanged.

  - `BetaManagedAgentsPrecondition precondition`

    Body param: Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `required string ID`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `required string ContentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `required Int ContentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `required string MemoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `required string Path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `required Type Type`

    - `"memory"Memory`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? Content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```csharp
MemoryUpdateParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryID = "memory_id",
};

var betaManagedAgentsMemory = await client.Beta.MemoryStores.Memories.Update(parameters);

Console.WriteLine(betaManagedAgentsMemory);
```

#### Response

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

## Delete a memory

`BetaManagedAgentsDeletedMemory Beta.MemoryStores.Memories.Delete(MemoryDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

### Parameters

- `MemoryDeleteParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryID`

    Path param: Path parameter memory_id

  - `string expectedContentSha256`

    Query param: Query parameter for expected_content_sha256

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsDeletedMemory:`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `required string ID`

    ID of the deleted memory (a `mem_...` value).

  - `required Type Type`

    - `"memory_deleted"MemoryDeleted`

### Example

```csharp
MemoryDeleteParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryID = "memory_id",
};

var betaManagedAgentsDeletedMemory = await client.Beta.MemoryStores.Memories.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedMemory);
```

#### Response

```json
{
  "id": "id",
  "type": "memory_deleted"
}
```

## Domain Types

### Beta Managed Agents Conflict Error

- `class BetaManagedAgentsConflictError:`

  - `required Type Type`

    - `"conflict_error"ConflictError`

  - `string Message`

### Beta Managed Agents Content Sha256 Precondition

- `class BetaManagedAgentsContentSha256Precondition:`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `required Type Type`

    - `"content_sha256"ContentSha256`

  - `string ContentSha256`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

### Beta Managed Agents Deleted Memory

- `class BetaManagedAgentsDeletedMemory:`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `required string ID`

    ID of the deleted memory (a `mem_...` value).

  - `required Type Type`

    - `"memory_deleted"MemoryDeleted`

### Beta Managed Agents Error

- `class BetaManagedAgentsError: A class that can be one of several variants.union`

  - `class BetaInvalidRequestError:`

    - `required string Message`

    - `JsonElement Type "invalid_request_error"constant`

  - `class BetaAuthenticationError:`

    - `required string Message`

    - `JsonElement Type "authentication_error"constant`

  - `class BetaBillingError:`

    - `required string Message`

    - `JsonElement Type "billing_error"constant`

  - `class BetaPermissionError:`

    - `required string Message`

    - `JsonElement Type "permission_error"constant`

  - `class BetaNotFoundError:`

    - `required string Message`

    - `JsonElement Type "not_found_error"constant`

  - `class BetaRateLimitError:`

    - `required string Message`

    - `JsonElement Type "rate_limit_error"constant`

  - `class BetaGatewayTimeoutError:`

    - `required string Message`

    - `JsonElement Type "timeout_error"constant`

  - `class BetaApiError:`

    - `required string Message`

    - `JsonElement Type "api_error"constant`

  - `class BetaOverloadedError:`

    - `required string Message`

    - `JsonElement Type "overloaded_error"constant`

  - `class BetaManagedAgentsMemoryPreconditionFailedError:`

    - `required Type Type`

      - `"memory_precondition_failed_error"MemoryPreconditionFailedError`

    - `string Message`

  - `class BetaManagedAgentsMemoryPathConflictError:`

    - `required Type Type`

      - `"memory_path_conflict_error"MemoryPathConflictError`

    - `string ConflictingMemoryID`

    - `string ConflictingPath`

    - `string Message`

  - `class BetaManagedAgentsConflictError:`

    - `required Type Type`

      - `"conflict_error"ConflictError`

    - `string Message`

### Beta Managed Agents Memory

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `required string ID`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `required string ContentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `required Int ContentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `required string MemoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `required string Path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `required Type Type`

    - `"memory"Memory`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? Content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Beta Managed Agents Memory List Item

- `class BetaManagedAgentsMemoryListItem: A class that can be one of several variants.union`

  One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

  - `class BetaManagedAgentsMemory:`

    A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

    - `required string ID`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `required string ContentSha256`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `required Int ContentSizeBytes`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string MemoryStoreID`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `required string MemoryVersionID`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `required string Path`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `required Type Type`

      - `"memory"Memory`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

    - `string? Content`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `class BetaManagedAgentsMemoryPrefix:`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `required string Path`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `required Type Type`

      - `"memory_prefix"MemoryPrefix`

### Beta Managed Agents Memory Path Conflict Error

- `class BetaManagedAgentsMemoryPathConflictError:`

  - `required Type Type`

    - `"memory_path_conflict_error"MemoryPathConflictError`

  - `string ConflictingMemoryID`

  - `string ConflictingPath`

  - `string Message`

### Beta Managed Agents Memory Precondition Failed Error

- `class BetaManagedAgentsMemoryPreconditionFailedError:`

  - `required Type Type`

    - `"memory_precondition_failed_error"MemoryPreconditionFailedError`

  - `string Message`

### Beta Managed Agents Memory Prefix

- `class BetaManagedAgentsMemoryPrefix:`

  A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

  - `required string Path`

    The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

  - `required Type Type`

    - `"memory_prefix"MemoryPrefix`

### Beta Managed Agents Memory View

- `enum BetaManagedAgentsMemoryView:`

  Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

  - `"basic"Basic`

  - `"full"Full`

### Beta Managed Agents Precondition

- `class BetaManagedAgentsPrecondition:`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `required Type Type`

    - `"content_sha256"ContentSha256`

  - `string ContentSha256`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

# Memory Versions

## List memory versions

`MemoryVersionListPageResponse Beta.MemoryStores.MemoryVersions.List(MemoryVersionListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

### Parameters

- `MemoryVersionListParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `string apiKeyID`

    Query param: Query parameter for api_key_id

  - `DateTimeOffset createdAtGte`

    Query param: Return versions created at or after this time (inclusive).

  - `DateTimeOffset createdAtLte`

    Query param: Return versions created at or before this time (inclusive).

  - `Int limit`

    Query param: Query parameter for limit

  - `string memoryID`

    Query param: Query parameter for memory_id

  - `BetaManagedAgentsMemoryVersionOperation operation`

    Query param: Query parameter for operation

  - `string page`

    Query param: Query parameter for page

  - `string serviceAccountID`

    Query param: Query parameter for service_account_id

  - `string sessionID`

    Query param: Query parameter for session_id

  - `BetaManagedAgentsMemoryView view`

    Query param: Query parameter for view

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class MemoryVersionListPageResponse:`

  Response payload for [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `IReadOnlyList<BetaManagedAgentsMemoryVersion> Data`

    One page of `memory_version` objects, ordered by `created_at` descending (newest first), with `id` as tiebreak.

    - `required string ID`

      Unique identifier for this version (a `memver_...` value).

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string MemoryID`

      ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

    - `required string MemoryStoreID`

      ID of the memory store this version belongs to (a `memstore_...` value).

    - `required BetaManagedAgentsMemoryVersionOperation Operation`

      The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

      - `"created"Created`

      - `"modified"Modified`

      - `"deleted"Deleted`

    - `required Type Type`

      - `"memory_version"MemoryVersion`

    - `string? Content`

      The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

    - `string? ContentSha256`

      Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    - `Int? ContentSizeBytes`

      Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    - `BetaManagedAgentsActor CreatedBy`

      Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

      - `class BetaManagedAgentsSessionActor:`

        Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

        - `required string SessionID`

          ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

        - `required Type Type`

          - `"session_actor"SessionActor`

      - `class BetaManagedAgentsApiActor:`

        Attribution for a write made directly via the public API (outside of any session).

        - `required string ApiKeyID`

          ID of the API key that performed the write. This identifies the key, not the secret.

        - `required Type Type`

          - `"api_actor"ApiActor`

      - `class BetaManagedAgentsUserActor:`

        Attribution for a write made by a human user through the Anthropic Console.

        - `required Type Type`

          - `"user_actor"UserActor`

        - `required string UserID`

          ID of the user who performed the write (a `user_...` value).

      - `class BetaManagedAgentsServiceAccountActor:`

        Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

        - `required string ServiceAccountID`

          ID of the service account that performed the write (a `svac_...` value).

        - `JsonElement Type "service_account_actor"constant`

    - `string? Path`

      The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

    - `DateTimeOffset? RedactedAt`

      A timestamp in RFC 3339 format

    - `BetaManagedAgentsActor RedactedBy`

      Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

  - `string? NextPage`

    Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.

### Example

```csharp
MemoryVersionListParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var page = await client.Beta.MemoryStores.MemoryVersions.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_id": "memory_id",
      "memory_store_id": "memory_store_id",
      "operation": "created",
      "type": "memory_version",
      "content": "content",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_by": {
        "session_id": "x",
        "type": "session_actor"
      },
      "path": "path",
      "redacted_at": "2019-12-27T18:11:19.117Z",
      "redacted_by": {
        "session_id": "x",
        "type": "session_actor"
      }
    }
  ],
  "next_page": "next_page"
}
```

## Retrieve a memory version

`BetaManagedAgentsMemoryVersion Beta.MemoryStores.MemoryVersions.Retrieve(MemoryVersionRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

### Parameters

- `MemoryVersionRetrieveParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryVersionID`

    Path param: Path parameter memory_version_id

  - `BetaManagedAgentsMemoryView view`

    Query param: Query parameter for view

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemoryVersion:`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `required string ID`

    Unique identifier for this version (a `memver_...` value).

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `required string MemoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `required BetaManagedAgentsMemoryVersionOperation Operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"Created`

    - `"modified"Modified`

    - `"deleted"Deleted`

  - `required Type Type`

    - `"memory_version"MemoryVersion`

  - `string? Content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `string? ContentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Int? ContentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `BetaManagedAgentsActor CreatedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `required string SessionID`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `required Type Type`

        - `"session_actor"SessionActor`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `required string ApiKeyID`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `required Type Type`

        - `"api_actor"ApiActor`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `required Type Type`

        - `"user_actor"UserActor`

      - `required string UserID`

        ID of the user who performed the write (a `user_...` value).

    - `class BetaManagedAgentsServiceAccountActor:`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `required string ServiceAccountID`

        ID of the service account that performed the write (a `svac_...` value).

      - `JsonElement Type "service_account_actor"constant`

  - `string? Path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `DateTimeOffset? RedactedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsActor RedactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```csharp
MemoryVersionRetrieveParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryVersionID = "memory_version_id",
};

var betaManagedAgentsMemoryVersion = await client.Beta.MemoryStores.MemoryVersions.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsMemoryVersion);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_id": "memory_id",
  "memory_store_id": "memory_store_id",
  "operation": "created",
  "type": "memory_version",
  "content": "content",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_by": {
    "session_id": "x",
    "type": "session_actor"
  },
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
  }
}
```

## Redact a memory version

`BetaManagedAgentsMemoryVersion Beta.MemoryStores.MemoryVersions.Redact(MemoryVersionRedactParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a memory version

### Parameters

- `MemoryVersionRedactParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryVersionID`

    Path param: Path parameter memory_version_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemoryVersion:`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `required string ID`

    Unique identifier for this version (a `memver_...` value).

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `required string MemoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `required BetaManagedAgentsMemoryVersionOperation Operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"Created`

    - `"modified"Modified`

    - `"deleted"Deleted`

  - `required Type Type`

    - `"memory_version"MemoryVersion`

  - `string? Content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `string? ContentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Int? ContentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `BetaManagedAgentsActor CreatedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `required string SessionID`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `required Type Type`

        - `"session_actor"SessionActor`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `required string ApiKeyID`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `required Type Type`

        - `"api_actor"ApiActor`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `required Type Type`

        - `"user_actor"UserActor`

      - `required string UserID`

        ID of the user who performed the write (a `user_...` value).

    - `class BetaManagedAgentsServiceAccountActor:`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `required string ServiceAccountID`

        ID of the service account that performed the write (a `svac_...` value).

      - `JsonElement Type "service_account_actor"constant`

  - `string? Path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `DateTimeOffset? RedactedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsActor RedactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```csharp
MemoryVersionRedactParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryVersionID = "memory_version_id",
};

var betaManagedAgentsMemoryVersion = await client.Beta.MemoryStores.MemoryVersions.Redact(parameters);

Console.WriteLine(betaManagedAgentsMemoryVersion);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_id": "memory_id",
  "memory_store_id": "memory_store_id",
  "operation": "created",
  "type": "memory_version",
  "content": "content",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_by": {
    "session_id": "x",
    "type": "session_actor"
  },
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
  }
}
```

## Domain Types

### Beta Managed Agents Actor

- `class BetaManagedAgentsActor: A class that can be one of several variants.union`

  Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

  - `class BetaManagedAgentsSessionActor:`

    Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

    - `required string SessionID`

      ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

    - `required Type Type`

      - `"session_actor"SessionActor`

  - `class BetaManagedAgentsApiActor:`

    Attribution for a write made directly via the public API (outside of any session).

    - `required string ApiKeyID`

      ID of the API key that performed the write. This identifies the key, not the secret.

    - `required Type Type`

      - `"api_actor"ApiActor`

  - `class BetaManagedAgentsUserActor:`

    Attribution for a write made by a human user through the Anthropic Console.

    - `required Type Type`

      - `"user_actor"UserActor`

    - `required string UserID`

      ID of the user who performed the write (a `user_...` value).

  - `class BetaManagedAgentsServiceAccountActor:`

    Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

    - `required string ServiceAccountID`

      ID of the service account that performed the write (a `svac_...` value).

    - `JsonElement Type "service_account_actor"constant`

### Beta Managed Agents API Actor

- `class BetaManagedAgentsApiActor:`

  Attribution for a write made directly via the public API (outside of any session).

  - `required string ApiKeyID`

    ID of the API key that performed the write. This identifies the key, not the secret.

  - `required Type Type`

    - `"api_actor"ApiActor`

### Beta Managed Agents Memory Version

- `class BetaManagedAgentsMemoryVersion:`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `required string ID`

    Unique identifier for this version (a `memver_...` value).

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `required string MemoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `required BetaManagedAgentsMemoryVersionOperation Operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"Created`

    - `"modified"Modified`

    - `"deleted"Deleted`

  - `required Type Type`

    - `"memory_version"MemoryVersion`

  - `string? Content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `string? ContentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Int? ContentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `BetaManagedAgentsActor CreatedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `required string SessionID`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `required Type Type`

        - `"session_actor"SessionActor`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `required string ApiKeyID`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `required Type Type`

        - `"api_actor"ApiActor`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `required Type Type`

        - `"user_actor"UserActor`

      - `required string UserID`

        ID of the user who performed the write (a `user_...` value).

    - `class BetaManagedAgentsServiceAccountActor:`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `required string ServiceAccountID`

        ID of the service account that performed the write (a `svac_...` value).

      - `JsonElement Type "service_account_actor"constant`

  - `string? Path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `DateTimeOffset? RedactedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsActor RedactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Beta Managed Agents Memory Version Operation

- `enum BetaManagedAgentsMemoryVersionOperation:`

  The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

  - `"created"Created`

  - `"modified"Modified`

  - `"deleted"Deleted`

### Beta Managed Agents Service Account Actor

- `class BetaManagedAgentsServiceAccountActor:`

  Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

  - `required string ServiceAccountID`

    ID of the service account that performed the write (a `svac_...` value).

  - `JsonElement Type "service_account_actor"constant`

### Beta Managed Agents Session Actor

- `class BetaManagedAgentsSessionActor:`

  Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

  - `required string SessionID`

    ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

  - `required Type Type`

    - `"session_actor"SessionActor`

### Beta Managed Agents User Actor

- `class BetaManagedAgentsUserActor:`

  Attribution for a write made by a human user through the Anthropic Console.

  - `required Type Type`

    - `"user_actor"UserActor`

  - `required string UserID`

    ID of the user who performed the write (a `user_...` value).

# Files

## Upload File

`BetaFileMetadata Beta.Files.Upload(FileUploadParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/files`

Upload File

### Parameters

- `FileUploadParams parameters`

  - `required string file`

    Body param: The file to upload

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaFileMetadata:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing when the file was created.

  - `required string Filename`

    Original filename of the uploaded file.

  - `required string MimeType`

    MIME type of the file.

  - `required Long SizeBytes`

    Size of the file in bytes.

  - `JsonElement Type "file"constant`

    Object type.

    For files, this is always `"file"`.

  - `Boolean Downloadable`

    Whether the file can be downloaded.

  - `BetaFileScope? Scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `required string ID`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonElement Type "session"constant`

      The type of scope (e.g., `"session"`).

### Example

```csharp
FileUploadParams parameters = new()
{
    File = Encoding.UTF8.GetBytes("Example data")
};

var betaFileMetadata = await client.Beta.Files.Upload(parameters);

Console.WriteLine(betaFileMetadata);
```

#### Response

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

## List Files

`FileListPageResponse Beta.Files.List(FileListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/files`

List Files

### Parameters

- `FileListParams parameters`

  - `string afterID`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Long limit`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

  - `string scopeID`

    Query param: Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class FileListPageResponse:`

  - `required IReadOnlyList<BetaFileMetadata> Data`

    List of file metadata objects.

    - `required string ID`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `required DateTimeOffset CreatedAt`

      RFC 3339 datetime string representing when the file was created.

    - `required string Filename`

      Original filename of the uploaded file.

    - `required string MimeType`

      MIME type of the file.

    - `required Long SizeBytes`

      Size of the file in bytes.

    - `JsonElement Type "file"constant`

      Object type.

      For files, this is always `"file"`.

    - `Boolean Downloadable`

      Whether the file can be downloaded.

    - `BetaFileScope? Scope`

      The scope of this file, indicating the context in which it was created (e.g., a session).

      - `required string ID`

        The ID of the scoping resource (e.g., the session ID).

      - `JsonElement Type "session"constant`

        The type of scope (e.g., `"session"`).

  - `string? FirstID`

    ID of the first file in this page of results.

  - `Boolean HasMore`

    Whether there are more results available.

  - `string? LastID`

    ID of the last file in this page of results.

### Example

```csharp
FileListParams parameters = new();

var page = await client.Beta.Files.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "created_at": "2025-04-15T18:37:24.100435Z",
      "filename": "document.pdf",
      "mime_type": "application/pdf",
      "size_bytes": 102400,
      "type": "file",
      "downloadable": false,
      "scope": {
        "id": "id",
        "type": "session"
      }
    }
  ],
  "first_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "has_more": true,
  "last_id": "file_013Zva2CMHLNnXjNJJKqJ2EF"
}
```

## Download File

`HttpResponse Beta.Files.Download(FileDownloadParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/files/{file_id}/content`

Download File

### Parameters

- `FileDownloadParams parameters`

  - `required string fileID`

    ID of the File.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Example

```csharp
FileDownloadParams parameters = new() { FileID = "file_id" };

var response = await client.Beta.Files.Download(parameters);

Console.WriteLine(response);
```

## Get File Metadata

`BetaFileMetadata Beta.Files.RetrieveMetadata(FileRetrieveMetadataParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/files/{file_id}`

Get File Metadata

### Parameters

- `FileRetrieveMetadataParams parameters`

  - `required string fileID`

    ID of the File.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaFileMetadata:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing when the file was created.

  - `required string Filename`

    Original filename of the uploaded file.

  - `required string MimeType`

    MIME type of the file.

  - `required Long SizeBytes`

    Size of the file in bytes.

  - `JsonElement Type "file"constant`

    Object type.

    For files, this is always `"file"`.

  - `Boolean Downloadable`

    Whether the file can be downloaded.

  - `BetaFileScope? Scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `required string ID`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonElement Type "session"constant`

      The type of scope (e.g., `"session"`).

### Example

```csharp
FileRetrieveMetadataParams parameters = new() { FileID = "file_id" };

var betaFileMetadata = await client.Beta.Files.RetrieveMetadata(parameters);

Console.WriteLine(betaFileMetadata);
```

#### Response

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

## Delete File

`BetaDeletedFile Beta.Files.Delete(FileDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/files/{file_id}`

Delete File

### Parameters

- `FileDeleteParams parameters`

  - `required string fileID`

    ID of the File.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaDeletedFile:`

  - `required string ID`

    ID of the deleted file.

  - `Type Type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"FileDeleted`

### Example

```csharp
FileDeleteParams parameters = new() { FileID = "file_id" };

var betaDeletedFile = await client.Beta.Files.Delete(parameters);

Console.WriteLine(betaDeletedFile);
```

#### Response

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```

## Domain Types

### Beta Deleted File

- `class BetaDeletedFile:`

  - `required string ID`

    ID of the deleted file.

  - `Type Type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"FileDeleted`

### Beta File Metadata

- `class BetaFileMetadata:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing when the file was created.

  - `required string Filename`

    Original filename of the uploaded file.

  - `required string MimeType`

    MIME type of the file.

  - `required Long SizeBytes`

    Size of the file in bytes.

  - `JsonElement Type "file"constant`

    Object type.

    For files, this is always `"file"`.

  - `Boolean Downloadable`

    Whether the file can be downloaded.

  - `BetaFileScope? Scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `required string ID`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonElement Type "session"constant`

      The type of scope (e.g., `"session"`).

### Beta File Scope

- `class BetaFileScope:`

  - `required string ID`

    The ID of the scoping resource (e.g., the session ID).

  - `JsonElement Type "session"constant`

    The type of scope (e.g., `"session"`).

# Skills

## Create Skill

`SkillCreateResponse Beta.Skills.Create(SkillCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/skills`

Create Skill

### Parameters

- `SkillCreateParams parameters`

  - `required IReadOnlyList<string> files`

    Body param: Files to upload for the skill.

    All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

  - `string? displayTitle`

    Body param: Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class SkillCreateResponse:`

  - `required string ID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string CreatedAt`

    ISO 8601 timestamp of when the skill was created.

  - `required string? DisplayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `required string? LatestVersion`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `required string Source`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `required string Type`

    Object type.

    For Skills, this is always `"skill"`.

  - `required string UpdatedAt`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```csharp
SkillCreateParams parameters = new()
{
    Files =
    [
        Encoding.UTF8.GetBytes("Example data")
    ],
};

var skill = await client.Beta.Skills.Create(parameters);

Console.WriteLine(skill);
```

#### Response

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

## List Skills

`SkillListPageResponse Beta.Skills.List(SkillListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/skills`

List Skills

### Parameters

- `SkillListParams parameters`

  - `Long limit`

    Query param: Number of results to return per page.

    Maximum value is 100. Defaults to 20.

  - `string? page`

    Query param: Pagination token for fetching a specific page of results.

    Pass the value from a previous response's `next_page` field to get the next page of results.

  - `string? source`

    Query param: Filter skills by source.

    If provided, only skills from the specified source will be returned:

    * `"custom"`: only return user-created skills
    * `"anthropic"`: only return Anthropic-created skills

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class SkillListPageResponse:`

  - `required IReadOnlyList<SkillListResponse> Data`

    List of skills.

    - `required string ID`

      Unique identifier for the skill.

      The format and length of IDs may change over time.

    - `required string CreatedAt`

      ISO 8601 timestamp of when the skill was created.

    - `required string? DisplayTitle`

      Display title for the skill.

      This is a human-readable label that is not included in the prompt sent to the model.

    - `required string? LatestVersion`

      The latest version identifier for the skill.

      This represents the most recent version of the skill that has been created.

    - `required string Source`

      Source of the skill.

      This may be one of the following values:

      * `"custom"`: the skill was created by a user
      * `"anthropic"`: the skill was created by Anthropic

    - `required string Type`

      Object type.

      For Skills, this is always `"skill"`.

    - `required string UpdatedAt`

      ISO 8601 timestamp of when the skill was last updated.

  - `required Boolean HasMore`

    Whether there are more results available.

    If `true`, there are additional results that can be fetched using the `next_page` token.

  - `required string? NextPage`

    Token for fetching the next page of results.

    If `null`, there are no more results available. Pass this value to the `page` parameter in the next request to get the next page.

### Example

```csharp
SkillListParams parameters = new();

var page = await client.Beta.Skills.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "skill_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_title": "My Custom Skill",
      "latest_version": "1759178010641129",
      "source": "custom",
      "type": "type",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Skill

`SkillRetrieveResponse Beta.Skills.Retrieve(SkillRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/skills/{skill_id}`

Get Skill

### Parameters

- `SkillRetrieveParams parameters`

  - `required string skillID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class SkillRetrieveResponse:`

  - `required string ID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string CreatedAt`

    ISO 8601 timestamp of when the skill was created.

  - `required string? DisplayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `required string? LatestVersion`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `required string Source`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `required string Type`

    Object type.

    For Skills, this is always `"skill"`.

  - `required string UpdatedAt`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```csharp
SkillRetrieveParams parameters = new() { SkillID = "skill_id" };

var skill = await client.Beta.Skills.Retrieve(parameters);

Console.WriteLine(skill);
```

#### Response

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

## Delete Skill

`SkillDeleteResponse Beta.Skills.Delete(SkillDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/skills/{skill_id}`

Delete Skill

### Parameters

- `SkillDeleteParams parameters`

  - `required string skillID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class SkillDeleteResponse:`

  - `required string ID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string Type`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

### Example

```csharp
SkillDeleteParams parameters = new() { SkillID = "skill_id" };

var skill = await client.Beta.Skills.Delete(parameters);

Console.WriteLine(skill);
```

#### Response

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type"
}
```

# Versions

## Create Skill Version

`VersionCreateResponse Beta.Skills.Versions.Create(VersionCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/skills/{skill_id}/versions`

Create Skill Version

### Parameters

- `VersionCreateParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required IReadOnlyList<string> files`

    Body param: Files to upload for the skill.

    All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class VersionCreateResponse:`

  - `required string ID`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `required string CreatedAt`

    ISO 8601 timestamp of when the skill version was created.

  - `required string Description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `required string Directory`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `required string Name`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `required string SkillID`

    Identifier for the skill that this version belongs to.

  - `required string Type`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `required string Version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```csharp
VersionCreateParams parameters = new()
{
    SkillID = "skill_id",
    Files =
    [
        Encoding.UTF8.GetBytes("Example data")
    ],
};

var version = await client.Beta.Skills.Versions.Create(parameters);

Console.WriteLine(version);
```

#### Response

```json
{
  "id": "skillver_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "A custom skill for doing something useful",
  "directory": "my-skill",
  "name": "my-skill",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type",
  "version": "1759178010641129"
}
```

## List Skill Versions

`VersionListPageResponse Beta.Skills.Versions.List(VersionListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/skills/{skill_id}/versions`

List Skill Versions

### Parameters

- `VersionListParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Long? limit`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

  - `string? page`

    Query param: Optionally set to the `next_page` token from the previous response.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class VersionListPageResponse:`

  - `required IReadOnlyList<VersionListResponse> Data`

    List of skill versions.

    - `required string ID`

      Unique identifier for the skill version.

      The format and length of IDs may change over time.

    - `required string CreatedAt`

      ISO 8601 timestamp of when the skill version was created.

    - `required string Description`

      Description of the skill version.

      This is extracted from the SKILL.md file in the skill upload.

    - `required string Directory`

      Directory name of the skill version.

      This is the top-level directory name that was extracted from the uploaded files.

    - `required string Name`

      Human-readable name of the skill version.

      This is extracted from the SKILL.md file in the skill upload.

    - `required string SkillID`

      Identifier for the skill that this version belongs to.

    - `required string Type`

      Object type.

      For Skill Versions, this is always `"skill_version"`.

    - `required string Version`

      Version identifier for the skill.

      Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `required Boolean HasMore`

    Indicates if there are more results in the requested page direction.

  - `required string? NextPage`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

### Example

```csharp
VersionListParams parameters = new() { SkillID = "skill_id" };

var page = await client.Beta.Skills.Versions.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "skillver_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "A custom skill for doing something useful",
      "directory": "my-skill",
      "name": "my-skill",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "type",
      "version": "1759178010641129"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Download Skill Version Content

`HttpResponse Beta.Skills.Versions.Download(VersionDownloadParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

### Parameters

- `VersionDownloadParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string version`

    Path param: Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Example

```csharp
VersionDownloadParams parameters = new()
{
    SkillID = "skill_id",
    Version = "version",
};

var response = await client.Beta.Skills.Versions.Download(parameters);

Console.WriteLine(response);
```

## Get Skill Version

`VersionRetrieveResponse Beta.Skills.Versions.Retrieve(VersionRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

### Parameters

- `VersionRetrieveParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string version`

    Path param: Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class VersionRetrieveResponse:`

  - `required string ID`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `required string CreatedAt`

    ISO 8601 timestamp of when the skill version was created.

  - `required string Description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `required string Directory`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `required string Name`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `required string SkillID`

    Identifier for the skill that this version belongs to.

  - `required string Type`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `required string Version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```csharp
VersionRetrieveParams parameters = new()
{
    SkillID = "skill_id",
    Version = "version",
};

var version = await client.Beta.Skills.Versions.Retrieve(parameters);

Console.WriteLine(version);
```

#### Response

```json
{
  "id": "skillver_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "A custom skill for doing something useful",
  "directory": "my-skill",
  "name": "my-skill",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type",
  "version": "1759178010641129"
}
```

## Delete Skill Version

`VersionDeleteResponse Beta.Skills.Versions.Delete(VersionDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

### Parameters

- `VersionDeleteParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string version`

    Path param: Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class VersionDeleteResponse:`

  - `required string ID`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `required string Type`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

### Example

```csharp
VersionDeleteParams parameters = new()
{
    SkillID = "skill_id",
    Version = "version",
};

var version = await client.Beta.Skills.Versions.Delete(parameters);

Console.WriteLine(version);
```

#### Response

```json
{
  "id": "1759178010641129",
  "type": "type"
}
```

# User Profiles

## Create User Profile

`BetaUserProfile Beta.UserProfiles.Create(UserProfileCreateParams?parameters, CancellationTokencancellationToken = default)`

**post** `/v1/user_profiles`

Create User Profile

### Parameters

- `UserProfileCreateParams parameters`

  - `AccessType accessType`

    Body param: How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"Application`

    - `"passthrough"Passthrough`

  - `string? externalID`

    Body param: Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

  - `string? name`

    Body param: Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a resold-to company (`relationship` `resold` / `access_type` `passthrough`), that company's name where known. Maximum 255 characters.

  - `Relationship relationship`

    Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"External`

    - `"resold"Resold`

    - `"internal"Internal`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaUserProfile:`

  - `required string ID`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `required Status Status`

      Status of the trust grant.

      - `"active"Active`

      - `"pending"Pending`

      - `"rejected"Rejected`

  - `required Type Type`

    Object type. Always `user_profile`.

    - `"user_profile"UserProfile`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `AccessType AccessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"Application`

    - `"passthrough"Passthrough`

  - `string? ExternalID`

    Platform's own identifier for this user. Not enforced unique.

  - `string? Name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Relationship Relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"External`

    - `"resold"Resold`

    - `"internal"Internal`

### Example

```csharp
UserProfileCreateParams parameters = new();

var betaUserProfile = await client.Beta.UserProfiles.Create(parameters);

Console.WriteLine(betaUserProfile);
```

#### Response

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "access_type": "application",
  "external_id": "user_12345",
  "name": "Example User",
  "relationship": "external"
}
```

## List User Profiles

`UserProfileListPageResponse Beta.UserProfiles.List(UserProfileListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/user_profiles`

List User Profiles

### Parameters

- `UserProfileListParams parameters`

  - `Int limit`

    Query param: Query parameter for limit

  - `Order order`

    Query param: Query parameter for order

    - `"asc"Asc`

    - `"desc"Desc`

  - `string page`

    Query param: Query parameter for page

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class UserProfileListPageResponse:`

  - `required IReadOnlyList<BetaUserProfile> Data`

    User profiles on this page.

    - `required string ID`

      Unique identifier for this user profile, prefixed `uprof_`.

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required IReadOnlyDictionary<string, string> Metadata`

      Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

    - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

      Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

      - `required Status Status`

        Status of the trust grant.

        - `"active"Active`

        - `"pending"Pending`

        - `"rejected"Rejected`

    - `required Type Type`

      Object type. Always `user_profile`.

      - `"user_profile"UserProfile`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

    - `AccessType AccessType`

      How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

      - `"application"Application`

      - `"passthrough"Passthrough`

    - `string? ExternalID`

      Platform's own identifier for this user. Not enforced unique.

    - `string? Name`

      Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

    - `Relationship Relationship`

      How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

      - `"external"External`

      - `"resold"Resold`

      - `"internal"Internal`

  - `required string? NextPage`

    Cursor for the next page, or `null` when there are no more results.

### Example

```csharp
UserProfileListParams parameters = new();

var page = await client.Beta.UserProfiles.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {},
      "trust_grants": {
        "cyber": {
          "status": "active"
        }
      },
      "type": "user_profile",
      "updated_at": "2026-03-15T10:00:00Z",
      "access_type": "application",
      "external_id": "user_12345",
      "name": "Example User",
      "relationship": "external"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get User Profile

`BetaUserProfile Beta.UserProfiles.Retrieve(UserProfileRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/user_profiles/{user_profile_id}`

Get User Profile

### Parameters

- `UserProfileRetrieveParams parameters`

  - `required string userProfileID`

    Path parameter user_profile_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaUserProfile:`

  - `required string ID`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `required Status Status`

      Status of the trust grant.

      - `"active"Active`

      - `"pending"Pending`

      - `"rejected"Rejected`

  - `required Type Type`

    Object type. Always `user_profile`.

    - `"user_profile"UserProfile`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `AccessType AccessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"Application`

    - `"passthrough"Passthrough`

  - `string? ExternalID`

    Platform's own identifier for this user. Not enforced unique.

  - `string? Name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Relationship Relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"External`

    - `"resold"Resold`

    - `"internal"Internal`

### Example

```csharp
UserProfileRetrieveParams parameters = new()
{
    UserProfileID = "uprof_011CZkZCu8hGbp5mYRQgUmz9"
};

var betaUserProfile = await client.Beta.UserProfiles.Retrieve(parameters);

Console.WriteLine(betaUserProfile);
```

#### Response

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "access_type": "application",
  "external_id": "user_12345",
  "name": "Example User",
  "relationship": "external"
}
```

## Update User Profile

`BetaUserProfile Beta.UserProfiles.Update(UserProfileUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `UserProfileUpdateParams parameters`

  - `required string userProfileID`

    Path param: Path parameter user_profile_id

  - `AccessType? accessType`

    Body param: How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"Application`

    - `"passthrough"Passthrough`

  - `string? externalID`

    Body param: If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

  - `string? name`

    Body param: If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

  - `Relationship? relationship`

    Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"External`

    - `"resold"Resold`

    - `"internal"Internal`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaUserProfile:`

  - `required string ID`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `required Status Status`

      Status of the trust grant.

      - `"active"Active`

      - `"pending"Pending`

      - `"rejected"Rejected`

  - `required Type Type`

    Object type. Always `user_profile`.

    - `"user_profile"UserProfile`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `AccessType AccessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"Application`

    - `"passthrough"Passthrough`

  - `string? ExternalID`

    Platform's own identifier for this user. Not enforced unique.

  - `string? Name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Relationship Relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"External`

    - `"resold"Resold`

    - `"internal"Internal`

### Example

```csharp
UserProfileUpdateParams parameters = new()
{
    UserProfileID = "uprof_011CZkZCu8hGbp5mYRQgUmz9"
};

var betaUserProfile = await client.Beta.UserProfiles.Update(parameters);

Console.WriteLine(betaUserProfile);
```

#### Response

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "access_type": "application",
  "external_id": "user_12345",
  "name": "Example User",
  "relationship": "external"
}
```

## Create Enrollment URL

`BetaUserProfileEnrollmentUrl Beta.UserProfiles.CreateEnrollmentUrl(UserProfileCreateEnrollmentUrlParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Parameters

- `UserProfileCreateEnrollmentUrlParams parameters`

  - `required string userProfileID`

    Path parameter user_profile_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaUserProfileEnrollmentUrl:`

  - `required DateTimeOffset ExpiresAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    Object type. Always `enrollment_url`.

    - `"enrollment_url"EnrollmentUrl`

  - `required string Url`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

```csharp
UserProfileCreateEnrollmentUrlParams parameters = new()
{
    UserProfileID = "uprof_011CZkZCu8hGbp5mYRQgUmz9"
};

var betaUserProfileEnrollmentUrl = await client.Beta.UserProfiles.CreateEnrollmentUrl(parameters);

Console.WriteLine(betaUserProfileEnrollmentUrl);
```

#### Response

```json
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```

## Domain Types

### Beta User Profile

- `class BetaUserProfile:`

  - `required string ID`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `required Status Status`

      Status of the trust grant.

      - `"active"Active`

      - `"pending"Pending`

      - `"rejected"Rejected`

  - `required Type Type`

    Object type. Always `user_profile`.

    - `"user_profile"UserProfile`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `AccessType AccessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"Application`

    - `"passthrough"Passthrough`

  - `string? ExternalID`

    Platform's own identifier for this user. Not enforced unique.

  - `string? Name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Relationship Relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"External`

    - `"resold"Resold`

    - `"internal"Internal`

### Beta User Profile Enrollment URL

- `class BetaUserProfileEnrollmentUrl:`

  - `required DateTimeOffset ExpiresAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    Object type. Always `enrollment_url`.

    - `"enrollment_url"EnrollmentUrl`

  - `required string Url`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Beta User Profile Trust Grant

- `class BetaUserProfileTrustGrant:`

  - `required Status Status`

    Status of the trust grant.

    - `"active"Active`

    - `"pending"Pending`

    - `"rejected"Rejected`

# Dreams

## Create a Dream

`BetaDream Beta.Dreams.Create(DreamCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/dreams`

Create a Dream

### Parameters

- `DreamCreateParams parameters`

  - `required IReadOnlyList<BetaDreamInput> inputs`

    Body param

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"memory_store"MemoryStore`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

        - `"sessions"Sessions`

  - `required Model model`

    Body param: Model identifier and configuration applied to every pipeline stage.

    - `string`

    - `class BetaDreamModelConfigParam:`

      Model identifier and configuration applied to every pipeline stage.

      - `required string ID`

        Model identifier, e.g. "claude-opus-5". 1-256 characters.

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"Standard`

        - `"fast"Fast`

  - `string? instructions`

    Body param

  - `BetaOutputBehavior outputBehavior`

    Body param: The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? EndedAt`

    A timestamp in RFC 3339 format

  - `required BetaDreamError? Error`

    Failure detail for a Dream whose `status` is `failed`.

    - `required string Message`

    - `required string Type`

  - `required IReadOnlyList<BetaDreamInput> Inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"memory_store"MemoryStore`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

        - `"sessions"Sessions`

  - `required string? Instructions`

  - `required BetaDreamModelConfig Model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `required string ID`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"Standard`

      - `"fast"Fast`

  - `required BetaOutputBehavior OutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `required Type Type`

        - `"create_new"CreateNew`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"update_existing"UpdateExisting`

  - `required IReadOnlyList<BetaDreamOutput> Outputs`

    - `required string MemoryStoreID`

    - `required Type Type`

      - `"memory_store"MemoryStore`

  - `required string? SessionID`

  - `required BetaDreamStatus Status`

    Lifecycle status of a Dream.

    - `"pending"Pending`

    - `"running"Running`

    - `"completed"Completed`

    - `"failed"Failed`

    - `"canceled"Canceled`

  - `required Type Type`

    - `"dream"Dream`

  - `required BetaDreamUsage Usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `required Int CacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `required Int CacheReadInputTokens`

      Total tokens read from prompt cache.

    - `required Int InputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `required Int OutputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```csharp
DreamCreateParams parameters = new()
{
    Inputs =
    [
        new BetaDreamMemoryStoreInput()
        {
            MemoryStoreID = "x",
            Type = Type.MemoryStore,
        },
    ],
    Model = "string",
};

var betaDream = await client.Beta.Dreams.Create(parameters);

Console.WriteLine(betaDream);
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## List Dreams

`DreamListPageResponse Beta.Dreams.List(DreamListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/dreams`

List Dreams

### Parameters

- `DreamListParams parameters`

  - `DateTimeOffset createdAtGt`

    Query param: Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

  - `DateTimeOffset createdAtLt`

    Query param: Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

  - `Boolean includeArchived`

    Query param: Query parameter for include_archived

  - `Int limit`

    Query param: Query parameter for limit

  - `string page`

    Query param: Query parameter for page

  - `IReadOnlyList<BetaDreamStatus> statuses`

    Query param: Filter by lifecycle status. Repeat the parameter to match any of multiple statuses. Empty applies no status filter.

    - `"pending"Pending`

    - `"running"Running`

    - `"completed"Completed`

    - `"failed"Failed`

    - `"canceled"Canceled`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class DreamListPageResponse:`

  - `required IReadOnlyList<BetaDream> Data`

    - `required string ID`

    - `required DateTimeOffset? ArchivedAt`

      A timestamp in RFC 3339 format

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required DateTimeOffset? EndedAt`

      A timestamp in RFC 3339 format

    - `required BetaDreamError? Error`

      Failure detail for a Dream whose `status` is `failed`.

      - `required string Message`

      - `required string Type`

    - `required IReadOnlyList<BetaDreamInput> Inputs`

      - `class BetaDreamMemoryStoreInput:`

        An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

        - `required string MemoryStoreID`

        - `required Type Type`

          - `"memory_store"MemoryStore`

      - `class BetaDreamSessionsInput:`

        Input session transcripts the dream reads.

        - `required IReadOnlyList<string> SessionIds`

        - `required Type Type`

          - `"sessions"Sessions`

    - `required string? Instructions`

    - `required BetaDreamModelConfig Model`

      Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

      - `required string ID`

        Model identifier, e.g. "claude-opus-5". 1-256 characters.

      - `Speed Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"Standard`

        - `"fast"Fast`

    - `required BetaOutputBehavior OutputBehavior`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `class BetaOutputBehaviorCreateNew:`

        The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

        - `required Type Type`

          - `"create_new"CreateNew`

      - `class BetaOutputBehaviorUpdateExisting:`

        The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

        - `required string MemoryStoreID`

        - `required Type Type`

          - `"update_existing"UpdateExisting`

    - `required IReadOnlyList<BetaDreamOutput> Outputs`

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"memory_store"MemoryStore`

    - `required string? SessionID`

    - `required BetaDreamStatus Status`

      Lifecycle status of a Dream.

      - `"pending"Pending`

      - `"running"Running`

      - `"completed"Completed`

      - `"failed"Failed`

      - `"canceled"Canceled`

    - `required Type Type`

      - `"dream"Dream`

    - `required BetaDreamUsage Usage`

      Cumulative token usage for the dream across every pipeline stage.

      - `required Int CacheCreationInputTokens`

        Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      - `required Int CacheReadInputTokens`

        Total tokens read from prompt cache.

      - `required Int InputTokens`

        Total uncached input tokens consumed across every pipeline stage.

      - `required Int OutputTokens`

        Total output tokens generated across every pipeline stage.

  - `required string? NextPage`

### Example

```csharp
DreamListParams parameters = new();

var page = await client.Beta.Dreams.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "ended_at": "2019-12-27T18:11:19.117Z",
      "error": {
        "message": "message",
        "type": "type"
      },
      "inputs": [
        {
          "memory_store_id": "x",
          "type": "memory_store"
        }
      ],
      "instructions": "instructions",
      "model": {
        "id": "x",
        "speed": "standard"
      },
      "output_behavior": {
        "type": "create_new"
      },
      "outputs": [
        {
          "memory_store_id": "memory_store_id",
          "type": "memory_store"
        }
      ],
      "session_id": "session_id",
      "status": "pending",
      "type": "dream",
      "usage": {
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0
      }
    }
  ],
  "next_page": "next_page"
}
```

## Get a Dream

`BetaDream Beta.Dreams.Retrieve(DreamRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/dreams/{dream_id}`

Get a Dream

### Parameters

- `DreamRetrieveParams parameters`

  - `required string dreamID`

    Path parameter dream_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? EndedAt`

    A timestamp in RFC 3339 format

  - `required BetaDreamError? Error`

    Failure detail for a Dream whose `status` is `failed`.

    - `required string Message`

    - `required string Type`

  - `required IReadOnlyList<BetaDreamInput> Inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"memory_store"MemoryStore`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

        - `"sessions"Sessions`

  - `required string? Instructions`

  - `required BetaDreamModelConfig Model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `required string ID`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"Standard`

      - `"fast"Fast`

  - `required BetaOutputBehavior OutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `required Type Type`

        - `"create_new"CreateNew`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"update_existing"UpdateExisting`

  - `required IReadOnlyList<BetaDreamOutput> Outputs`

    - `required string MemoryStoreID`

    - `required Type Type`

      - `"memory_store"MemoryStore`

  - `required string? SessionID`

  - `required BetaDreamStatus Status`

    Lifecycle status of a Dream.

    - `"pending"Pending`

    - `"running"Running`

    - `"completed"Completed`

    - `"failed"Failed`

    - `"canceled"Canceled`

  - `required Type Type`

    - `"dream"Dream`

  - `required BetaDreamUsage Usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `required Int CacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `required Int CacheReadInputTokens`

      Total tokens read from prompt cache.

    - `required Int InputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `required Int OutputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```csharp
DreamRetrieveParams parameters = new() { DreamID = "dream_id" };

var betaDream = await client.Beta.Dreams.Retrieve(parameters);

Console.WriteLine(betaDream);
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Cancel a Dream

`BetaDream Beta.Dreams.Cancel(DreamCancelParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/dreams/{dream_id}/cancel`

Cancel a Dream

### Parameters

- `DreamCancelParams parameters`

  - `required string dreamID`

    Path parameter dream_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? EndedAt`

    A timestamp in RFC 3339 format

  - `required BetaDreamError? Error`

    Failure detail for a Dream whose `status` is `failed`.

    - `required string Message`

    - `required string Type`

  - `required IReadOnlyList<BetaDreamInput> Inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"memory_store"MemoryStore`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

        - `"sessions"Sessions`

  - `required string? Instructions`

  - `required BetaDreamModelConfig Model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `required string ID`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"Standard`

      - `"fast"Fast`

  - `required BetaOutputBehavior OutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `required Type Type`

        - `"create_new"CreateNew`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"update_existing"UpdateExisting`

  - `required IReadOnlyList<BetaDreamOutput> Outputs`

    - `required string MemoryStoreID`

    - `required Type Type`

      - `"memory_store"MemoryStore`

  - `required string? SessionID`

  - `required BetaDreamStatus Status`

    Lifecycle status of a Dream.

    - `"pending"Pending`

    - `"running"Running`

    - `"completed"Completed`

    - `"failed"Failed`

    - `"canceled"Canceled`

  - `required Type Type`

    - `"dream"Dream`

  - `required BetaDreamUsage Usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `required Int CacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `required Int CacheReadInputTokens`

      Total tokens read from prompt cache.

    - `required Int InputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `required Int OutputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```csharp
DreamCancelParams parameters = new() { DreamID = "dream_id" };

var betaDream = await client.Beta.Dreams.Cancel(parameters);

Console.WriteLine(betaDream);
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Archive a Dream

`BetaDream Beta.Dreams.Archive(DreamArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/dreams/{dream_id}/archive`

Archive a Dream

### Parameters

- `DreamArchiveParams parameters`

  - `required string dreamID`

    Path parameter dream_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? EndedAt`

    A timestamp in RFC 3339 format

  - `required BetaDreamError? Error`

    Failure detail for a Dream whose `status` is `failed`.

    - `required string Message`

    - `required string Type`

  - `required IReadOnlyList<BetaDreamInput> Inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"memory_store"MemoryStore`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

        - `"sessions"Sessions`

  - `required string? Instructions`

  - `required BetaDreamModelConfig Model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `required string ID`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"Standard`

      - `"fast"Fast`

  - `required BetaOutputBehavior OutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `required Type Type`

        - `"create_new"CreateNew`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"update_existing"UpdateExisting`

  - `required IReadOnlyList<BetaDreamOutput> Outputs`

    - `required string MemoryStoreID`

    - `required Type Type`

      - `"memory_store"MemoryStore`

  - `required string? SessionID`

  - `required BetaDreamStatus Status`

    Lifecycle status of a Dream.

    - `"pending"Pending`

    - `"running"Running`

    - `"completed"Completed`

    - `"failed"Failed`

    - `"canceled"Canceled`

  - `required Type Type`

    - `"dream"Dream`

  - `required BetaDreamUsage Usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `required Int CacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `required Int CacheReadInputTokens`

      Total tokens read from prompt cache.

    - `required Int InputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `required Int OutputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```csharp
DreamArchiveParams parameters = new() { DreamID = "dream_id" };

var betaDream = await client.Beta.Dreams.Archive(parameters);

Console.WriteLine(betaDream);
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Domain Types

### Beta Dream

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? EndedAt`

    A timestamp in RFC 3339 format

  - `required BetaDreamError? Error`

    Failure detail for a Dream whose `status` is `failed`.

    - `required string Message`

    - `required string Type`

  - `required IReadOnlyList<BetaDreamInput> Inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"memory_store"MemoryStore`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

        - `"sessions"Sessions`

  - `required string? Instructions`

  - `required BetaDreamModelConfig Model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `required string ID`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"Standard`

      - `"fast"Fast`

  - `required BetaOutputBehavior OutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `required Type Type`

        - `"create_new"CreateNew`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"update_existing"UpdateExisting`

  - `required IReadOnlyList<BetaDreamOutput> Outputs`

    - `required string MemoryStoreID`

    - `required Type Type`

      - `"memory_store"MemoryStore`

  - `required string? SessionID`

  - `required BetaDreamStatus Status`

    Lifecycle status of a Dream.

    - `"pending"Pending`

    - `"running"Running`

    - `"completed"Completed`

    - `"failed"Failed`

    - `"canceled"Canceled`

  - `required Type Type`

    - `"dream"Dream`

  - `required BetaDreamUsage Usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `required Int CacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `required Int CacheReadInputTokens`

      Total tokens read from prompt cache.

    - `required Int InputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `required Int OutputTokens`

      Total output tokens generated across every pipeline stage.

### Beta Dream Error

- `class BetaDreamError:`

  Failure detail for a Dream whose `status` is `failed`.

  - `required string Message`

  - `required string Type`

### Beta Dream Input

- `class BetaDreamInput: A class that can be one of several variants.union`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `class BetaDreamMemoryStoreInput:`

    An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

    - `required string MemoryStoreID`

    - `required Type Type`

      - `"memory_store"MemoryStore`

  - `class BetaDreamSessionsInput:`

    Input session transcripts the dream reads.

    - `required IReadOnlyList<string> SessionIds`

    - `required Type Type`

      - `"sessions"Sessions`

### Beta Dream Memory Store Input

- `class BetaDreamMemoryStoreInput:`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `required string MemoryStoreID`

  - `required Type Type`

    - `"memory_store"MemoryStore`

### Beta Dream Memory Store Output

- `class BetaDreamMemoryStoreOutput:`

  An output memory store the dream writes consolidated memories into.

  - `required string MemoryStoreID`

  - `required Type Type`

    - `"memory_store"MemoryStore`

### Beta Dream Model Config

- `class BetaDreamModelConfig:`

  Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

  - `required string ID`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

  - `Speed Speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"Standard`

    - `"fast"Fast`

### Beta Dream Model Config Param

- `class BetaDreamModelConfigParam:`

  Model identifier and configuration applied to every pipeline stage.

  - `required string ID`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

  - `Speed? Speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"Standard`

    - `"fast"Fast`

### Beta Dream Output

- `class BetaDreamOutput:`

  An output memory store the dream writes consolidated memories into.

  - `required string MemoryStoreID`

  - `required Type Type`

    - `"memory_store"MemoryStore`

### Beta Dream Sessions Input

- `class BetaDreamSessionsInput:`

  Input session transcripts the dream reads.

  - `required IReadOnlyList<string> SessionIds`

  - `required Type Type`

    - `"sessions"Sessions`

### Beta Dream Status

- `enum BetaDreamStatus:`

  Lifecycle status of a Dream.

  - `"pending"Pending`

  - `"running"Running`

  - `"completed"Completed`

  - `"failed"Failed`

  - `"canceled"Canceled`

### Beta Dream Usage

- `class BetaDreamUsage:`

  Cumulative token usage for the dream across every pipeline stage.

  - `required Int CacheCreationInputTokens`

    Total tokens used to create prompt-cache entries (sum of all TTL tiers).

  - `required Int CacheReadInputTokens`

    Total tokens read from prompt cache.

  - `required Int InputTokens`

    Total uncached input tokens consumed across every pipeline stage.

  - `required Int OutputTokens`

    Total output tokens generated across every pipeline stage.

### Beta Output Behavior

- `class BetaOutputBehavior: A class that can be one of several variants.union`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `class BetaOutputBehaviorCreateNew:`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `required Type Type`

      - `"create_new"CreateNew`

  - `class BetaOutputBehaviorUpdateExisting:`

    The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

    - `required string MemoryStoreID`

    - `required Type Type`

      - `"update_existing"UpdateExisting`

### Beta Output Behavior Create New

- `class BetaOutputBehaviorCreateNew:`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `required Type Type`

    - `"create_new"CreateNew`

### Beta Output Behavior Update Existing

- `class BetaOutputBehaviorUpdateExisting:`

  The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

  - `required string MemoryStoreID`

  - `required Type Type`

    - `"update_existing"UpdateExisting`

# Tunnels

## Create Tunnel

`BetaTunnel Beta.Tunnels.Create(TunnelCreateParams?parameters, CancellationTokencancellationToken = default)`

**post** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

### Parameters

- `TunnelCreateParams parameters`

  - `string? displayName`

    Body param: Optional human-readable name for the tunnel (1-255 characters).

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `required string ID`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? DisplayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `required string Domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonElement Type "tunnel"constant`

### Example

```csharp
TunnelCreateParams parameters = new();

var betaTunnel = await client.Beta.Tunnels.Create(parameters);

Console.WriteLine(betaTunnel);
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

## Get Tunnel

`BetaTunnel Beta.Tunnels.Retrieve(TunnelRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

### Parameters

- `TunnelRetrieveParams parameters`

  - `required string tunnelID`

    Path parameter tunnel_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `required string ID`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? DisplayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `required string Domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonElement Type "tunnel"constant`

### Example

```csharp
TunnelRetrieveParams parameters = new() { TunnelID = "tunnel_id" };

var betaTunnel = await client.Beta.Tunnels.Retrieve(parameters);

Console.WriteLine(betaTunnel);
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

## List Tunnels

`TunnelListPageResponse Beta.Tunnels.List(TunnelListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

### Parameters

- `TunnelListParams parameters`

  - `Boolean includeArchived`

    Query param: Whether to include archived tunnels in the results. Defaults to false.

  - `Int limit`

    Query param: Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

  - `string page`

    Query param: Opaque pagination cursor from a previous `list_tunnels` response.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class TunnelListPageResponse:`

  A paginated list of tunnels.

  - `required IReadOnlyList<BetaTunnel> Data`

    List of tunnels, ordered by created_at descending.

    - `required string ID`

      Unique identifier for the tunnel, prefixed with `tnl_`.

    - `required DateTimeOffset? ArchivedAt`

      A timestamp in RFC 3339 format

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string? DisplayName`

      Human-readable name for the tunnel (1-255 characters). Null if unset.

    - `required string Domain`

      Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

    - `JsonElement Type "tunnel"constant`

  - `required string? NextPage`

    Pagination cursor for the next page, or null if no more results.

### Example

```csharp
TunnelListParams parameters = new();

var page = await client.Beta.Tunnels.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "display_name": "display_name",
      "domain": "domain",
      "type": "tunnel"
    }
  ],
  "next_page": "next_page"
}
```

## Archive Tunnel

`BetaTunnel Beta.Tunnels.Archive(TunnelArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

### Parameters

- `TunnelArchiveParams parameters`

  - `required string tunnelID`

    Path parameter tunnel_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `required string ID`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? DisplayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `required string Domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonElement Type "tunnel"constant`

### Example

```csharp
TunnelArchiveParams parameters = new() { TunnelID = "tunnel_id" };

var betaTunnel = await client.Beta.Tunnels.Archive(parameters);

Console.WriteLine(betaTunnel);
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

## Reveal Tunnel Token

`BetaTunnelToken Beta.Tunnels.RevealToken(TunnelRevealTokenParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

### Parameters

- `TunnelRevealTokenParams parameters`

  - `required string tunnelID`

    Path parameter tunnel_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnelToken:`

  A tunnel's connector token.

  - `required string ID`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `required string TunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `JsonElement Type "tunnel_token"constant`

### Example

```csharp
TunnelRevealTokenParams parameters = new() { TunnelID = "tunnel_id" };

var betaTunnelToken = await client.Beta.Tunnels.RevealToken(parameters);

Console.WriteLine(betaTunnelToken);
```

#### Response

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

## Rotate Tunnel Token

`BetaTunnelToken Beta.Tunnels.RotateToken(TunnelRotateTokenParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

### Parameters

- `TunnelRotateTokenParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `string? reason`

    Body param: Optional free-text reason for the rotation, recorded for audit.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnelToken:`

  A tunnel's connector token.

  - `required string ID`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `required string TunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `JsonElement Type "tunnel_token"constant`

### Example

```csharp
TunnelRotateTokenParams parameters = new() { TunnelID = "tunnel_id" };

var betaTunnelToken = await client.Beta.Tunnels.RotateToken(parameters);

Console.WriteLine(betaTunnelToken);
```

#### Response

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

## Domain Types

### Beta Tunnel

- `class BetaTunnel:`

  An MCP tunnel.

  - `required string ID`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? DisplayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `required string Domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonElement Type "tunnel"constant`

### Beta Tunnel Token

- `class BetaTunnelToken:`

  A tunnel's connector token.

  - `required string ID`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `required string TunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `JsonElement Type "tunnel_token"constant`

# Certificates

## Create Tunnel Certificate

`BetaTunnelCertificate Beta.Tunnels.Certificates.Create(CertificateCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

### Parameters

- `CertificateCreateParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `required string caCertificatePem`

    Body param: PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

  - `JsonElement Type "tunnel_certificate"constant`

### Example

```csharp
CertificateCreateParams parameters = new()
{
    TunnelID = "tunnel_id",
    CaCertificatePem = "ca_certificate_pem",
};

var betaTunnelCertificate = await client.Beta.Tunnels.Certificates.Create(parameters);

Console.WriteLine(betaTunnelCertificate);
```

#### Response

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

## Get Tunnel Certificate

`BetaTunnelCertificate Beta.Tunnels.Certificates.Retrieve(CertificateRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

### Parameters

- `CertificateRetrieveParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `required string certificateID`

    Path param: Path parameter certificate_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

  - `JsonElement Type "tunnel_certificate"constant`

### Example

```csharp
CertificateRetrieveParams parameters = new()
{
    TunnelID = "tunnel_id",
    CertificateID = "certificate_id",
};

var betaTunnelCertificate = await client.Beta.Tunnels.Certificates.Retrieve(parameters);

Console.WriteLine(betaTunnelCertificate);
```

#### Response

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

## List Tunnel Certificates

`CertificateListPageResponse Beta.Tunnels.Certificates.List(CertificateListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

### Parameters

- `CertificateListParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `Boolean includeArchived`

    Query param: Whether to include archived certificates in the results. Defaults to false.

  - `Int limit`

    Query param: Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

  - `string page`

    Query param: Opaque pagination cursor from a previous `list_tunnel_certificates` response.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class CertificateListPageResponse:`

  The tunnel's certificates.

  - `required IReadOnlyList<BetaTunnelCertificate> Data`

    List of certificates, ordered by created_at descending.

    - `required string ID`

      Unique identifier for the certificate, prefixed with `tcrt_`.

    - `required DateTimeOffset? ArchivedAt`

      A timestamp in RFC 3339 format

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required DateTimeOffset? ExpiresAt`

      A timestamp in RFC 3339 format

    - `required string Fingerprint`

      Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

    - `required string TunnelID`

      ID of the tunnel the certificate is registered against.

    - `JsonElement Type "tunnel_certificate"constant`

  - `required string? NextPage`

    Pagination cursor for the next page, or null if no more results.

### Example

```csharp
CertificateListParams parameters = new() { TunnelID = "tunnel_id" };

var page = await client.Beta.Tunnels.Certificates.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

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

## Archive Tunnel Certificate

`BetaTunnelCertificate Beta.Tunnels.Certificates.Archive(CertificateArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

### Parameters

- `CertificateArchiveParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `required string certificateID`

    Path param: Path parameter certificate_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

  - `JsonElement Type "tunnel_certificate"constant`

### Example

```csharp
CertificateArchiveParams parameters = new()
{
    TunnelID = "tunnel_id",
    CertificateID = "certificate_id",
};

var betaTunnelCertificate = await client.Beta.Tunnels.Certificates.Archive(parameters);

Console.WriteLine(betaTunnelCertificate);
```

#### Response

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

## Domain Types

### Beta Tunnel Certificate

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

  - `JsonElement Type "tunnel_certificate"constant`

# Webhooks

## Domain Types

### Beta Webhook Agent Archived Event Data

- `class BetaWebhookAgentArchivedEventData:`

  - `required string ID`

    ID of the agent that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "agent.archived"constant`

  - `required string WorkspaceID`

### Beta Webhook Agent Created Event Data

- `class BetaWebhookAgentCreatedEventData:`

  - `required string ID`

    ID of the agent that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "agent.created"constant`

  - `required string WorkspaceID`

### Beta Webhook Agent Deleted Event Data

- `class BetaWebhookAgentDeletedEventData:`

  - `required string ID`

    ID of the agent that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "agent.deleted"constant`

  - `required string WorkspaceID`

### Beta Webhook Agent Updated Event Data

- `class BetaWebhookAgentUpdatedEventData:`

  - `required string ID`

    ID of the agent that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "agent.updated"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Archived Event Data

- `class BetaWebhookDeploymentArchivedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment.archived"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Created Event Data

- `class BetaWebhookDeploymentCreatedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment.created"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Deleted Event Data

- `class BetaWebhookDeploymentDeletedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment.deleted"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Paused Event Data

- `class BetaWebhookDeploymentPausedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment.paused"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Run Failed Event Data

- `class BetaWebhookDeploymentRunFailedEventData:`

  - `required string ID`

    ID of the deployment run that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment_run.failed"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Run Started Event Data

- `class BetaWebhookDeploymentRunStartedEventData:`

  - `required string ID`

    ID of the deployment run that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment_run.started"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Run Succeeded Event Data

- `class BetaWebhookDeploymentRunSucceededEventData:`

  - `required string ID`

    ID of the deployment run that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment_run.succeeded"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Unpaused Event Data

- `class BetaWebhookDeploymentUnpausedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment.unpaused"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Updated Event Data

- `class BetaWebhookDeploymentUpdatedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment.updated"constant`

  - `required string WorkspaceID`

### Beta Webhook Environment Archived Event Data

- `class BetaWebhookEnvironmentArchivedEventData:`

  - `required string ID`

    ID of the environment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "environment.archived"constant`

  - `required string WorkspaceID`

### Beta Webhook Environment Created Event Data

- `class BetaWebhookEnvironmentCreatedEventData:`

  - `required string ID`

    ID of the environment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "environment.created"constant`

  - `required string WorkspaceID`

### Beta Webhook Environment Deleted Event Data

- `class BetaWebhookEnvironmentDeletedEventData:`

  - `required string ID`

    ID of the environment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "environment.deleted"constant`

  - `required string WorkspaceID`

### Beta Webhook Environment Updated Event Data

- `class BetaWebhookEnvironmentUpdatedEventData:`

  - `required string ID`

    ID of the environment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "environment.updated"constant`

  - `required string WorkspaceID`

### Beta Webhook Event

- `class BetaWebhookEvent:`

  - `required string ID`

    Unique event identifier for idempotency.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 timestamp when the event occurred.

  - `required BetaWebhookEventData Data`

    - `class BetaWebhookSessionCreatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionPendingEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.pending"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionRunningEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.running"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionIdledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionRequiresActionEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.requires_action"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionArchivedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionDeletedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusRescheduledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_rescheduled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusRunStartedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_run_started"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusIdledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusTerminatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_terminated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadCreatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `JsonElement Type "session.thread_created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadIdledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `JsonElement Type "session.thread_idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadTerminatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `JsonElement Type "session.thread_terminated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.outcome_evaluation_ended"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCreatedEventData:`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultArchivedEventData:`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultDeletedEventData:`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialCreatedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.created"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialArchivedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.archived"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialDeletedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.deleted"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.refresh_failed"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookSessionUpdatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.updated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentCreatedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "agent.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentArchivedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "agent.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentDeletedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "agent.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentPausedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.paused"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunFailedEventData:`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment_run.failed"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentCreatedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentUpdatedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.updated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentUnpausedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.unpaused"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentUpdatedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "agent.updated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentArchivedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunStartedEventData:`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment_run.started"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentDeletedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunSucceededEventData:`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment_run.succeeded"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentCreatedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "environment.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentUpdatedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "environment.updated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentArchivedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "environment.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentDeletedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "environment.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreCreatedEventData:`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "memory_store.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreArchivedEventData:`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "memory_store.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreDeletedEventData:`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "memory_store.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionBudgetReachedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.budget_reached"constant`

      - `required string WorkspaceID`

  - `JsonElement Type "event"constant`

    Object type. Always `event` for webhook payloads.

### Beta Webhook Event Data

- `class BetaWebhookEventData: A class that can be one of several variants.union`

  - `class BetaWebhookSessionCreatedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.created"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionPendingEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.pending"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionRunningEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.running"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionIdledEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.idled"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionRequiresActionEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.requires_action"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionArchivedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.archived"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionDeletedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.deleted"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusRescheduledEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.status_rescheduled"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusRunStartedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.status_run_started"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusIdledEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.status_idled"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusTerminatedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.status_terminated"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionThreadCreatedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string SessionThreadID`

      ID of the session thread this event refers to.

    - `JsonElement Type "session.thread_created"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionThreadIdledEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string SessionThreadID`

      ID of the session thread this event refers to.

    - `JsonElement Type "session.thread_idled"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionThreadTerminatedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string SessionThreadID`

      ID of the session thread this event refers to.

    - `JsonElement Type "session.thread_terminated"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.outcome_evaluation_ended"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCreatedEventData:`

    - `required string ID`

      ID of the vault that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault.created"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultArchivedEventData:`

    - `required string ID`

      ID of the vault that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault.archived"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultDeletedEventData:`

    - `required string ID`

      ID of the vault that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault.deleted"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialCreatedEventData:`

    - `required string ID`

      ID of the vault credential that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault_credential.created"constant`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialArchivedEventData:`

    - `required string ID`

      ID of the vault credential that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault_credential.archived"constant`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialDeletedEventData:`

    - `required string ID`

      ID of the vault credential that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault_credential.deleted"constant`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

    - `required string ID`

      ID of the vault credential that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault_credential.refresh_failed"constant`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookSessionUpdatedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.updated"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookAgentCreatedEventData:`

    - `required string ID`

      ID of the agent that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "agent.created"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookAgentArchivedEventData:`

    - `required string ID`

      ID of the agent that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "agent.archived"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookAgentDeletedEventData:`

    - `required string ID`

      ID of the agent that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "agent.deleted"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentPausedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment.paused"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentRunFailedEventData:`

    - `required string ID`

      ID of the deployment run that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment_run.failed"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentCreatedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment.created"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentUpdatedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment.updated"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentUnpausedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment.unpaused"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookAgentUpdatedEventData:`

    - `required string ID`

      ID of the agent that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "agent.updated"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentArchivedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment.archived"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentRunStartedEventData:`

    - `required string ID`

      ID of the deployment run that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment_run.started"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentDeletedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment.deleted"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentRunSucceededEventData:`

    - `required string ID`

      ID of the deployment run that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment_run.succeeded"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookEnvironmentCreatedEventData:`

    - `required string ID`

      ID of the environment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "environment.created"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookEnvironmentUpdatedEventData:`

    - `required string ID`

      ID of the environment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "environment.updated"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookEnvironmentArchivedEventData:`

    - `required string ID`

      ID of the environment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "environment.archived"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookEnvironmentDeletedEventData:`

    - `required string ID`

      ID of the environment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "environment.deleted"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookMemoryStoreCreatedEventData:`

    - `required string ID`

      ID of the memory store that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "memory_store.created"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookMemoryStoreArchivedEventData:`

    - `required string ID`

      ID of the memory store that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "memory_store.archived"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookMemoryStoreDeletedEventData:`

    - `required string ID`

      ID of the memory store that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "memory_store.deleted"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionBudgetReachedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.budget_reached"constant`

    - `required string WorkspaceID`

### Beta Webhook Memory Store Archived Event Data

- `class BetaWebhookMemoryStoreArchivedEventData:`

  - `required string ID`

    ID of the memory store that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "memory_store.archived"constant`

  - `required string WorkspaceID`

### Beta Webhook Memory Store Created Event Data

- `class BetaWebhookMemoryStoreCreatedEventData:`

  - `required string ID`

    ID of the memory store that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "memory_store.created"constant`

  - `required string WorkspaceID`

### Beta Webhook Memory Store Deleted Event Data

- `class BetaWebhookMemoryStoreDeletedEventData:`

  - `required string ID`

    ID of the memory store that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "memory_store.deleted"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.archived"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Budget Reached Event Data

- `class BetaWebhookSessionBudgetReachedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.budget_reached"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.created"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.deleted"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.idled"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.outcome_evaluation_ended"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.pending"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.requires_action"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.running"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.status_idled"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Status Rescheduled Event Data

- `class BetaWebhookSessionStatusRescheduledEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.status_rescheduled"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.status_run_started"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.status_terminated"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string SessionThreadID`

    ID of the session thread this event refers to.

  - `JsonElement Type "session.thread_created"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string SessionThreadID`

    ID of the session thread this event refers to.

  - `JsonElement Type "session.thread_idled"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string SessionThreadID`

    ID of the session thread this event refers to.

  - `JsonElement Type "session.thread_terminated"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Updated Event Data

- `class BetaWebhookSessionUpdatedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.updated"constant`

  - `required string WorkspaceID`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData:`

  - `required string ID`

    ID of the vault that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault.archived"constant`

  - `required string WorkspaceID`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData:`

  - `required string ID`

    ID of the vault that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault.created"constant`

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData:`

  - `required string ID`

    ID of the vault credential that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault_credential.archived"constant`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData:`

  - `required string ID`

    ID of the vault credential that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault_credential.created"constant`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData:`

  - `required string ID`

    ID of the vault credential that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault_credential.deleted"constant`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData:`

  - `required string ID`

    ID of the vault credential that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault_credential.refresh_failed"constant`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData:`

  - `required string ID`

    ID of the vault that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault.deleted"constant`

  - `required string WorkspaceID`

### Unwrap Webhook Event

- `class UnwrapWebhookEvent:`

  - `required string ID`

    Unique event identifier for idempotency.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 timestamp when the event occurred.

  - `required BetaWebhookEventData Data`

    - `class BetaWebhookSessionCreatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionPendingEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.pending"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionRunningEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.running"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionIdledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionRequiresActionEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.requires_action"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionArchivedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionDeletedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusRescheduledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_rescheduled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusRunStartedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_run_started"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusIdledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusTerminatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_terminated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadCreatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `JsonElement Type "session.thread_created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadIdledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `JsonElement Type "session.thread_idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadTerminatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `JsonElement Type "session.thread_terminated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.outcome_evaluation_ended"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCreatedEventData:`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultArchivedEventData:`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultDeletedEventData:`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialCreatedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.created"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialArchivedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.archived"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialDeletedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.deleted"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.refresh_failed"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookSessionUpdatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.updated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentCreatedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "agent.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentArchivedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "agent.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentDeletedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "agent.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentPausedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.paused"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunFailedEventData:`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment_run.failed"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentCreatedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentUpdatedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.updated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentUnpausedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.unpaused"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentUpdatedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "agent.updated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentArchivedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunStartedEventData:`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment_run.started"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentDeletedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunSucceededEventData:`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment_run.succeeded"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentCreatedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "environment.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentUpdatedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "environment.updated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentArchivedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "environment.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentDeletedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "environment.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreCreatedEventData:`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "memory_store.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreArchivedEventData:`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "memory_store.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreDeletedEventData:`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "memory_store.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionBudgetReachedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.budget_reached"constant`

      - `required string WorkspaceID`

  - `JsonElement Type "event"constant`

    Object type. Always `event` for webhook payloads.
