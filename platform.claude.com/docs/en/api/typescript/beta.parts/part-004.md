<!-- source: https://platform.claude.com/docs/en/api/typescript/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/typescript/beta -->

<!-- chunk-start -->

    Where in the outbound request the secret value is substituted.

    - `body: boolean`

      Whether the placeholder is substituted in the request body.

    - `header: boolean`

      Whether the placeholder is substituted in request header values.

  - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse`

    Outbound hosts the secret value is substituted on.

    - `BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

      The secret is substituted on any host the session's Environment network policy permits egress to.

      - `type: "unrestricted"`

        - `"unrestricted"`

    - `BetaManagedAgentsLimitedCredentialNetworkingResponse`

      The secret is substituted only on requests to the listed hosts.

      - `allowed_hosts: Array<string>`

        Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

      - `type: "limited"`

        - `"limited"`

  - `secret_name: string`

    Name of the environment variable.

  - `type: "environment_variable"`

    - `"environment_variable"`

### Beta Managed Agents Environment Variable Create Params

- `BetaManagedAgentsEnvironmentVariableCreateParams`

  Parameters for creating an environment variable credential.

  - `networking: BetaManagedAgentsCredentialNetworkingParams`

    Outbound hosts the secret value is substituted on.

    - `BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `type: "unrestricted"`

        - `"unrestricted"`

    - `BetaManagedAgentsLimitedCredentialNetworkingParams`

      Substitute the secret only on requests to the listed hosts.

      - `allowed_hosts: Array<string>`

        Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

      - `type: "limited"`

        - `"limited"`

  - `secret_name: string`

    Name of the environment variable. Immutable after create.

  - `secret_value: string`

    Secret value. Write-only; never returned in responses.

  - `type: "environment_variable"`

    - `"environment_variable"`

  - `injection_location?: BetaManagedAgentsInjectionLocationParams`

    Where in the outbound request the secret value may be substituted.

    - `body?: boolean`

      Substitute when the placeholder appears in the request body.

    - `header?: boolean`

      Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Environment Variable Update Params

- `BetaManagedAgentsEnvironmentVariableUpdateParams`

  Parameters for updating an environment variable credential. `secret_name` is immutable.

  - `type: "environment_variable"`

    - `"environment_variable"`

  - `injection_location?: BetaManagedAgentsInjectionLocationUpdateParams`

    Updated injection location.

    - `body?: boolean`

      Substitute when the placeholder appears in the request body.

    - `header?: boolean`

      Substitute when the placeholder appears in a request header value.

  - `networking?: BetaManagedAgentsCredentialNetworkingParams | null`

    Updated networking scope. Full replacement.

    - `BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `type: "unrestricted"`

        - `"unrestricted"`

    - `BetaManagedAgentsLimitedCredentialNetworkingParams`

      Substitute the secret only on requests to the listed hosts.

      - `allowed_hosts: Array<string>`

        Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

      - `type: "limited"`

        - `"limited"`

  - `secret_value?: string | null`

    Updated secret value.

### Beta Managed Agents Injection Location Params

- `BetaManagedAgentsInjectionLocationParams`

  Where in the outbound request the secret value may be substituted.

  - `body?: boolean`

    Substitute when the placeholder appears in the request body.

  - `header?: boolean`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Injection Location Response

- `BetaManagedAgentsInjectionLocationResponse`

  Where in the outbound request the secret value is substituted.

  - `body: boolean`

    Whether the placeholder is substituted in the request body.

  - `header: boolean`

    Whether the placeholder is substituted in request header values.

### Beta Managed Agents Injection Location Update Params

- `BetaManagedAgentsInjectionLocationUpdateParams`

  Updated injection location.

  - `body?: boolean`

    Substitute when the placeholder appears in the request body.

  - `header?: boolean`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Limited Credential Networking Params

- `BetaManagedAgentsLimitedCredentialNetworkingParams`

  Substitute the secret only on requests to the listed hosts.

  - `allowed_hosts: Array<string>`

    Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

  - `type: "limited"`

    - `"limited"`

### Beta Managed Agents Limited Credential Networking Response

- `BetaManagedAgentsLimitedCredentialNetworkingResponse`

  The secret is substituted only on requests to the listed hosts.

  - `allowed_hosts: Array<string>`

    Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

  - `type: "limited"`

    - `"limited"`

### Beta Managed Agents MCP OAuth Auth Response

- `BetaManagedAgentsMCPOAuthAuthResponse`

  OAuth credential details for an MCP server.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "mcp_oauth"`

    - `"mcp_oauth"`

  - `expires_at?: string | null`

    A timestamp in RFC 3339 format

  - `refresh?: BetaManagedAgentsMCPOAuthRefreshResponse | null`

    OAuth refresh token configuration returned in credential responses.

    - `client_id: string`

      OAuth client ID.

    - `token_endpoint: string`

      Token endpoint URL used to refresh the access token.

    - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

      Token endpoint requires no client authentication.

      - `BetaManagedAgentsTokenEndpointAuthNoneResponse`

        Token endpoint requires no client authentication.

        - `type: "none"`

          - `"none"`

      - `BetaManagedAgentsTokenEndpointAuthBasicResponse`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `type: "client_secret_basic"`

          - `"client_secret_basic"`

      - `BetaManagedAgentsTokenEndpointAuthPostResponse`

        Token endpoint uses POST body authentication with client credentials.

        - `type: "client_secret_post"`

          - `"client_secret_post"`

    - `resource?: string | null`

      OAuth resource indicator.

    - `scope?: string | null`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Create Params

- `BetaManagedAgentsMCPOAuthCreateParams`

  Parameters for creating an MCP OAuth credential.

  - `access_token: string`

    OAuth access token.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "mcp_oauth"`

    - `"mcp_oauth"`

  - `expires_at?: string | null`

    A timestamp in RFC 3339 format

  - `refresh?: BetaManagedAgentsMCPOAuthRefreshParams | null`

    OAuth refresh token parameters for creating a credential with refresh support.

    - `client_id: string`

      OAuth client ID.

    - `refresh_token: string`

      OAuth refresh token.

    - `token_endpoint: string`

      Token endpoint URL used to refresh the access token.

    - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam | BetaManagedAgentsTokenEndpointAuthBasicParam | BetaManagedAgentsTokenEndpointAuthPostParam`

      Token endpoint requires no client authentication.

      - `BetaManagedAgentsTokenEndpointAuthNoneParam`

        Token endpoint requires no client authentication.

        - `type: "none"`

          - `"none"`

      - `BetaManagedAgentsTokenEndpointAuthBasicParam`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `client_secret: string`

          OAuth client secret.

        - `type: "client_secret_basic"`

          - `"client_secret_basic"`

      - `BetaManagedAgentsTokenEndpointAuthPostParam`

        Token endpoint uses POST body authentication with client credentials.

        - `client_secret: string`

          OAuth client secret.

        - `type: "client_secret_post"`

          - `"client_secret_post"`

    - `resource?: string | null`

      OAuth resource indicator.

    - `scope?: string | null`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Params

- `BetaManagedAgentsMCPOAuthRefreshParams`

  OAuth refresh token parameters for creating a credential with refresh support.

  - `client_id: string`

    OAuth client ID.

  - `refresh_token: string`

    OAuth refresh token.

  - `token_endpoint: string`

    Token endpoint URL used to refresh the access token.

  - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam | BetaManagedAgentsTokenEndpointAuthBasicParam | BetaManagedAgentsTokenEndpointAuthPostParam`

    Token endpoint requires no client authentication.

    - `BetaManagedAgentsTokenEndpointAuthNoneParam`

      Token endpoint requires no client authentication.

      - `type: "none"`

        - `"none"`

    - `BetaManagedAgentsTokenEndpointAuthBasicParam`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `client_secret: string`

        OAuth client secret.

      - `type: "client_secret_basic"`

        - `"client_secret_basic"`

    - `BetaManagedAgentsTokenEndpointAuthPostParam`

      Token endpoint uses POST body authentication with client credentials.

      - `client_secret: string`

        OAuth client secret.

      - `type: "client_secret_post"`

        - `"client_secret_post"`

  - `resource?: string | null`

    OAuth resource indicator.

  - `scope?: string | null`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Response

- `BetaManagedAgentsMCPOAuthRefreshResponse`

  OAuth refresh token configuration returned in credential responses.

  - `client_id: string`

    OAuth client ID.

  - `token_endpoint: string`

    Token endpoint URL used to refresh the access token.

  - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

    Token endpoint requires no client authentication.

    - `BetaManagedAgentsTokenEndpointAuthNoneResponse`

      Token endpoint requires no client authentication.

      - `type: "none"`

        - `"none"`

    - `BetaManagedAgentsTokenEndpointAuthBasicResponse`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `type: "client_secret_basic"`

        - `"client_secret_basic"`

    - `BetaManagedAgentsTokenEndpointAuthPostResponse`

      Token endpoint uses POST body authentication with client credentials.

      - `type: "client_secret_post"`

        - `"client_secret_post"`

  - `resource?: string | null`

    OAuth resource indicator.

  - `scope?: string | null`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Update Params

- `BetaManagedAgentsMCPOAuthRefreshUpdateParams`

  Parameters for updating OAuth refresh token configuration.

  - `refresh_token?: string | null`

    Updated OAuth refresh token.

  - `scope?: string | null`

    Updated OAuth scope for the refresh request.

  - `token_endpoint_auth?: BetaManagedAgentsTokenEndpointAuthBasicUpdateParam | BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

    Updated HTTP Basic authentication parameters for the token endpoint.

    - `BetaManagedAgentsTokenEndpointAuthBasicUpdateParam`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `type: "client_secret_basic"`

        - `"client_secret_basic"`

      - `client_secret?: string | null`

        Updated OAuth client secret.

    - `BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

      Updated POST body authentication parameters for the token endpoint.

      - `type: "client_secret_post"`

        - `"client_secret_post"`

      - `client_secret?: string | null`

        Updated OAuth client secret.

### Beta Managed Agents MCP OAuth Update Params

- `BetaManagedAgentsMCPOAuthUpdateParams`

  Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

  - `type: "mcp_oauth"`

    - `"mcp_oauth"`

  - `access_token?: string | null`

    Updated OAuth access token.

  - `expires_at?: string | null`

    A timestamp in RFC 3339 format

  - `refresh?: BetaManagedAgentsMCPOAuthRefreshUpdateParams | null`

    Parameters for updating OAuth refresh token configuration.

    - `refresh_token?: string | null`

      Updated OAuth refresh token.

    - `scope?: string | null`

      Updated OAuth scope for the refresh request.

    - `token_endpoint_auth?: BetaManagedAgentsTokenEndpointAuthBasicUpdateParam | BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `BetaManagedAgentsTokenEndpointAuthBasicUpdateParam`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `type: "client_secret_basic"`

          - `"client_secret_basic"`

        - `client_secret?: string | null`

          Updated OAuth client secret.

      - `BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

        Updated POST body authentication parameters for the token endpoint.

        - `type: "client_secret_post"`

          - `"client_secret_post"`

        - `client_secret?: string | null`

          Updated OAuth client secret.

### Beta Managed Agents MCP Probe

- `BetaManagedAgentsMCPProbe`

  The failing step of an MCP validation probe.

  - `http_response: BetaManagedAgentsRefreshHTTPResponse | null`

    An HTTP response captured during a credential validation probe.

    - `body: string`

      Response body. May be truncated and has sensitive values scrubbed.

    - `body_truncated: boolean`

      Whether `body` was truncated.

    - `content_type: string`

      Value of the `Content-Type` response header.

    - `status_code: number`

      HTTP status code.

  - `method: string`

    The MCP method that failed (for example `initialize` or `tools/list`).

### Beta Managed Agents Refresh HTTP Response

- `BetaManagedAgentsRefreshHTTPResponse`

  An HTTP response captured during a credential validation probe.

  - `body: string`

    Response body. May be truncated and has sensitive values scrubbed.

  - `body_truncated: boolean`

    Whether `body` was truncated.

  - `content_type: string`

    Value of the `Content-Type` response header.

  - `status_code: number`

    HTTP status code.

### Beta Managed Agents Refresh Object

- `BetaManagedAgentsRefreshObject`

  Outcome of a refresh-token exchange attempted during credential validation.

  - `http_response: BetaManagedAgentsRefreshHTTPResponse | null`

    An HTTP response captured during a credential validation probe.

    - `body: string`

      Response body. May be truncated and has sensitive values scrubbed.

    - `body_truncated: boolean`

      Whether `body` was truncated.

    - `content_type: string`

      Value of the `Content-Type` response header.

    - `status_code: number`

      HTTP status code.

  - `status: "succeeded" | "failed" | "connect_error" | "no_refresh_token"`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `"succeeded"`

    - `"failed"`

    - `"connect_error"`

    - `"no_refresh_token"`

### Beta Managed Agents Static Bearer Auth Response

- `BetaManagedAgentsStaticBearerAuthResponse`

  Static bearer token credential details for an MCP server.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "static_bearer"`

    - `"static_bearer"`

### Beta Managed Agents Static Bearer Create Params

- `BetaManagedAgentsStaticBearerCreateParams`

  Parameters for creating a static bearer token credential.

  - `token: string`

    Static bearer token value.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "static_bearer"`

    - `"static_bearer"`

### Beta Managed Agents Static Bearer Update Params

- `BetaManagedAgentsStaticBearerUpdateParams`

  Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

  - `type: "static_bearer"`

    - `"static_bearer"`

  - `token?: string | null`

    Updated static bearer token value.

### Beta Managed Agents Token Endpoint Auth Basic Param

- `BetaManagedAgentsTokenEndpointAuthBasicParam`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `client_secret: string`

    OAuth client secret.

  - `type: "client_secret_basic"`

    - `"client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Response

- `BetaManagedAgentsTokenEndpointAuthBasicResponse`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `type: "client_secret_basic"`

    - `"client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `BetaManagedAgentsTokenEndpointAuthBasicUpdateParam`

  Updated HTTP Basic authentication parameters for the token endpoint.

  - `type: "client_secret_basic"`

    - `"client_secret_basic"`

  - `client_secret?: string | null`

    Updated OAuth client secret.

### Beta Managed Agents Token Endpoint Auth None Param

- `BetaManagedAgentsTokenEndpointAuthNoneParam`

  Token endpoint requires no client authentication.

  - `type: "none"`

    - `"none"`

### Beta Managed Agents Token Endpoint Auth None Response

- `BetaManagedAgentsTokenEndpointAuthNoneResponse`

  Token endpoint requires no client authentication.

  - `type: "none"`

    - `"none"`

### Beta Managed Agents Token Endpoint Auth Post Param

- `BetaManagedAgentsTokenEndpointAuthPostParam`

  Token endpoint uses POST body authentication with client credentials.

  - `client_secret: string`

    OAuth client secret.

  - `type: "client_secret_post"`

    - `"client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Response

- `BetaManagedAgentsTokenEndpointAuthPostResponse`

  Token endpoint uses POST body authentication with client credentials.

  - `type: "client_secret_post"`

    - `"client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

  Updated POST body authentication parameters for the token endpoint.

  - `type: "client_secret_post"`

    - `"client_secret_post"`

  - `client_secret?: string | null`

    Updated OAuth client secret.

### Beta Managed Agents Unrestricted Credential Networking Params

- `BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `type: "unrestricted"`

    - `"unrestricted"`

### Beta Managed Agents Unrestricted Credential Networking Response

- `BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

  The secret is substituted on any host the session's Environment network policy permits egress to.

  - `type: "unrestricted"`

    - `"unrestricted"`

# Memory Stores

## Create a memory store

`client.beta.memoryStores.create(MemoryStoreCreateParamsparams, RequestOptionsoptions?): BetaManagedAgentsMemoryStore`

**post** `/v1/memory_stores`

Create a memory store

### Parameters

- `params: MemoryStoreCreateParams`

  - `name: string`

    Body param: Human-readable name for the store. Required; 1–255 characters; no control characters. The mount-path slug under `/mnt/memory/` is derived from this name (lowercased, non-alphanumeric runs collapsed to a hyphen). Names need not be unique within a workspace.

  - `description?: string`

    Body param: Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent.

  - `metadata?: Record<string, string>`

    Body param: Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Not visible to the agent.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: "memory_store"`

    - `"memory_store"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `archived_at?: string | null`

    A timestamp in RFC 3339 format

  - `description?: string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata?: Record<string, string>`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemoryStore = await client.beta.memoryStores.create({ name: "x" });

console.log(betaManagedAgentsMemoryStore.id);
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

`client.beta.memoryStores.list(MemoryStoreListParamsparams?, RequestOptionsoptions?): PageCursor<BetaManagedAgentsMemoryStore>`

**get** `/v1/memory_stores`

List memory stores

### Parameters

- `params: MemoryStoreListParams`

  - `"created_at[gte]"?: string`

    Query param: Return only stores whose `created_at` is at or after this time (inclusive). Sent on the wire as `created_at[gte]`.

  - `"created_at[lte]"?: string`

    Query param: Return only stores whose `created_at` is at or before this time (inclusive). Sent on the wire as `created_at[lte]`.

  - `include_archived?: boolean`

    Query param: When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

  - `limit?: number`

    Query param: Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

  - `page?: string`

    Query param: Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: "memory_store"`

    - `"memory_store"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `archived_at?: string | null`

    A timestamp in RFC 3339 format

  - `description?: string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata?: Record<string, string>`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsMemoryStore of client.beta.memoryStores.list()) {
  console.log(betaManagedAgentsMemoryStore.id);
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

`client.beta.memoryStores.retrieve(stringmemoryStoreID, MemoryStoreRetrieveParamsparams?, RequestOptionsoptions?): BetaManagedAgentsMemoryStore`

**get** `/v1/memory_stores/{memory_store_id}`

Retrieve a memory store

### Parameters

- `memoryStoreID: string`

- `params: MemoryStoreRetrieveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: "memory_store"`

    - `"memory_store"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `archived_at?: string | null`

    A timestamp in RFC 3339 format

  - `description?: string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata?: Record<string, string>`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemoryStore = await client.beta.memoryStores.retrieve(
  "memory_store_id"
);

console.log(betaManagedAgentsMemoryStore.id);
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

`client.beta.memoryStores.update(stringmemoryStoreID, MemoryStoreUpdateParamsparams, RequestOptionsoptions?): BetaManagedAgentsMemoryStore`

**post** `/v1/memory_stores/{memory_store_id}`

Update a memory store

### Parameters

- `memoryStoreID: string`

- `params: MemoryStoreUpdateParams`

  - `description?: string | null`

    Body param: New description for the store, up to 1024 characters. Pass an empty string to clear it.

  - `metadata?: Record<string, string | null> | null`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `name?: string | null`

    Body param: New human-readable name for the store. 1–255 characters; no control characters. Renaming changes the slug used for the store's `mount_path` in sessions created after the update.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: "memory_store"`

    - `"memory_store"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `archived_at?: string | null`

    A timestamp in RFC 3339 format

  - `description?: string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata?: Record<string, string>`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemoryStore = await client.beta.memoryStores.update("memory_store_id");

console.log(betaManagedAgentsMemoryStore.id);
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

`client.beta.memoryStores.delete(stringmemoryStoreID, MemoryStoreDeleteParamsparams?, RequestOptionsoptions?): BetaManagedAgentsDeletedMemoryStore`

**delete** `/v1/memory_stores/{memory_store_id}`

Delete a memory store

### Parameters

- `memoryStoreID: string`

- `params: MemoryStoreDeleteParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaManagedAgentsDeletedMemoryStore`

  Confirmation that a `memory_store` was deleted.

  - `id: string`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `type: "memory_store_deleted"`

    - `"memory_store_deleted"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsDeletedMemoryStore = await client.beta.memoryStores.delete(
  "memory_store_id"
);

console.log(betaManagedAgentsDeletedMemoryStore.id);
```

#### Response

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

## Archive a memory store

`client.beta.memoryStores.archive(stringmemoryStoreID, MemoryStoreArchiveParamsparams?, RequestOptionsoptions?): BetaManagedAgentsMemoryStore`

**post** `/v1/memory_stores/{memory_store_id}/archive`

Archive a memory store

### Parameters

- `memoryStoreID: string`

- `params: MemoryStoreArchiveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: "memory_store"`

    - `"memory_store"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `archived_at?: string | null`

    A timestamp in RFC 3339 format

  - `description?: string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata?: Record<string, string>`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemoryStore = await client.beta.memoryStores.archive("memory_store_id");

console.log(betaManagedAgentsMemoryStore.id);
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

- `BetaManagedAgentsDeletedMemoryStore`

  Confirmation that a `memory_store` was deleted.

  - `id: string`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `type: "memory_store_deleted"`

    - `"memory_store_deleted"`

### Beta Managed Agents Memory Store

- `BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: "memory_store"`

    - `"memory_store"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `archived_at?: string | null`

    A timestamp in RFC 3339 format

  - `description?: string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata?: Record<string, string>`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

# Memories

## Create a memory

`client.beta.memoryStores.memories.create(stringmemoryStoreID, MemoryCreateParamsparams, RequestOptionsoptions?): BetaManagedAgentsMemory`

**post** `/v1/memory_stores/{memory_store_id}/memories`

Create a memory

### Parameters

- `memoryStoreID: string`

- `params: MemoryCreateParams`

  - `content: string | null`

    Body param: UTF-8 text content for the new memory. Maximum 100 kB (102,400 bytes). Required; pass `""` explicitly to create an empty memory.

  - `path: string`

    Body param: Hierarchical path for the new memory, e.g. `/projects/foo/notes.md`. Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive.

  - `view?: BetaManagedAgentsMemoryView`

    Query param: Query parameter for view

    - `"basic"`

    - `"full"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaManagedAgentsMemory`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: string`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: "memory"`

    - `"memory"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `content?: string | null`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemory = await client.beta.memoryStores.memories.create(
  "memory_store_id",
  { content: "content", path: "xx" }
);

console.log(betaManagedAgentsMemory.id);
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

`client.beta.memoryStores.memories.list(stringmemoryStoreID, MemoryListParamsparams?, RequestOptionsoptions?): PageCursor<BetaManagedAgentsMemoryListItem>`

**get** `/v1/memory_stores/{memory_store_id}/memories`

List memories

### Parameters

- `memoryStoreID: string`

- `params: MemoryListParams`

  - `depth?: number`

    Query param: `0` (or omitted) returns all descendants below `path_prefix` (recursive). `1` returns immediate children only; deeper entries roll up as `memory_prefix` items. `depth=1` behaves like `ls`; omitting `depth` behaves like `find`.

  - `limit?: number`

    Query param: Maximum number of items to return per page. Must be between 1 and 100. Defaults to 20 when omitted. Capped at 20 when `view=full`. Both `memory` and `memory_prefix` items count toward the limit.

  - `page?: string`

    Query param: Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

  - `path_prefix?: string`

    Query param: Optional path prefix filter. Must end with `/` (segment-aligned), e.g., `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

  - `view?: BetaManagedAgentsMemoryView`

    Query param: Which projection of each `memory` to return. Defaults to `basic` (content omitted). `full` populates `content` on each item and caps `limit` at 20; use this as the bulk-read path for export and sync.

    - `"basic"`

    - `"full"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaManagedAgentsMemoryListItem = BetaManagedAgentsMemory | BetaManagedAgentsMemoryPrefix`

  One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

  - `BetaManagedAgentsMemory`

    A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

    - `id: string`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `content_sha256: string`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `content_size_bytes: number`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `memory_store_id: string`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `memory_version_id: string`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `path: string`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `type: "memory"`

      - `"memory"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `content?: string | null`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `BetaManagedAgentsMemoryPrefix`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `path: string`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `type: "memory_prefix"`

      - `"memory_prefix"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsMemoryListItem of client.beta.memoryStores.memories.list(
  "memory_store_id"
)) {
  console.log(betaManagedAgentsMemoryListItem);
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

`client.beta.memoryStores.memories.retrieve(stringmemoryID, MemoryRetrieveParamsparams, RequestOptionsoptions?): BetaManagedAgentsMemory`

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a memory

### Parameters

- `memoryID: string`

- `params: MemoryRetrieveParams`

  - `memory_store_id: string`

    Path param: Path parameter memory_store_id

  - `view?: BetaManagedAgentsMemoryView`

    Query param: Query parameter for view

    - `"basic"`

    - `"full"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaManagedAgentsMemory`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: string`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: "memory"`

    - `"memory"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `content?: string | null`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemory = await client.beta.memoryStores.memories.retrieve("memory_id", {
  memory_store_id: "memory_store_id"
});

console.log(betaManagedAgentsMemory.id);
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

`client.beta.memoryStores.memories.update(stringmemoryID, MemoryUpdateParamsparams, RequestOptionsoptions?): BetaManagedAgentsMemory`

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a memory

### Parameters

- `memoryID: string`

- `params: MemoryUpdateParams`

  - `memory_store_id: string`

    Path param: Path parameter memory_store_id

  - `view?: BetaManagedAgentsMemoryView`

    Query param: Query parameter for view

    - `"basic"`

    - `"full"`

  - `content?: string | null`

    Body param: New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

  - `path?: string | null`

    Body param: New path for the memory (a rename). Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive. The memory's `id` is preserved across renames. Omit to leave the path unchanged.

  - `precondition?: BetaManagedAgentsPrecondition`

    Body param: Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

    - `type: "content_sha256"`

      - `"content_sha256"`

    - `content_sha256?: string`

      Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaManagedAgentsMemory`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: string`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: "memory"`

    - `"memory"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `content?: string | null`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemory = await client.beta.memoryStores.memories.update("memory_id", {
  memory_store_id: "memory_store_id"
});

console.log(betaManagedAgentsMemory.id);
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

`client.beta.memoryStores.memories.delete(stringmemoryID, MemoryDeleteParamsparams, RequestOptionsoptions?): BetaManagedAgentsDeletedMemory`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

### Parameters

- `memoryID: string`

- `params: MemoryDeleteParams`

  - `memory_store_id: string`

    Path param: Path parameter memory_store_id

  - `expected_content_sha256?: string`

    Query param: Query parameter for expected_content_sha256

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaManagedAgentsDeletedMemory`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `id: string`

    ID of the deleted memory (a `mem_...` value).

  - `type: "memory_deleted"`

    - `"memory_deleted"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsDeletedMemory = await client.beta.memoryStores.memories.delete(
  "memory_id",
  { memory_store_id: "memory_store_id" }
);

console.log(betaManagedAgentsDeletedMemory.id);
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

- `BetaManagedAgentsConflictError`

  - `type: "conflict_error"`

    - `"conflict_error"`

  - `message?: string`

### Beta Managed Agents Content Sha256 Precondition

- `BetaManagedAgentsContentSha256Precondition`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `type: "content_sha256"`

    - `"content_sha256"`

  - `content_sha256?: string`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

### Beta Managed Agents Deleted Memory

- `BetaManagedAgentsDeletedMemory`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `id: string`

    ID of the deleted memory (a `mem_...` value).

  - `type: "memory_deleted"`

    - `"memory_deleted"`

### Beta Managed Agents Error

- `BetaManagedAgentsError = BetaInvalidRequestError | BetaAuthenticationError | BetaBillingError | 9 more`

  - `BetaInvalidRequestError`

    - `message: string`

    - `type: "invalid_request_error"`

      - `"invalid_request_error"`

  - `BetaAuthenticationError`

    - `message: string`

    - `type: "authentication_error"`

      - `"authentication_error"`

  - `BetaBillingError`

    - `message: string`

    - `type: "billing_error"`

      - `"billing_error"`

  - `BetaPermissionError`

    - `message: string`

    - `type: "permission_error"`

      - `"permission_error"`

  - `BetaNotFoundError`

    - `message: string`

    - `type: "not_found_error"`

      - `"not_found_error"`

  - `BetaRateLimitError`

    - `message: string`

    - `type: "rate_limit_error"`

      - `"rate_limit_error"`

  - `BetaGatewayTimeoutError`

    - `message: string`

    - `type: "timeout_error"`

      - `"timeout_error"`

  - `BetaAPIError`

    - `message: string`

    - `type: "api_error"`

      - `"api_error"`

  - `BetaOverloadedError`

    - `message: string`

    - `type: "overloaded_error"`

      - `"overloaded_error"`

  - `BetaManagedAgentsMemoryPreconditionFailedError`

    - `type: "memory_precondition_failed_error"`

      - `"memory_precondition_failed_error"`

    - `message?: string`

  - `BetaManagedAgentsMemoryPathConflictError`

    - `type: "memory_path_conflict_error"`

      - `"memory_path_conflict_error"`

    - `conflicting_memory_id?: string`

    - `conflicting_path?: string`

    - `message?: string`

  - `BetaManagedAgentsConflictError`

    - `type: "conflict_error"`

      - `"conflict_error"`

    - `message?: string`

### Beta Managed Agents Memory

- `BetaManagedAgentsMemory`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: string`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: "memory"`

    - `"memory"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `content?: string | null`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Beta Managed Agents Memory List Item

- `BetaManagedAgentsMemoryListItem = BetaManagedAgentsMemory | BetaManagedAgentsMemoryPrefix`

  One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

  - `BetaManagedAgentsMemory`

    A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

    - `id: string`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `content_sha256: string`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `content_size_bytes: number`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `memory_store_id: string`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `memory_version_id: string`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `path: string`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `type: "memory"`

      - `"memory"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `content?: string | null`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `BetaManagedAgentsMemoryPrefix`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `path: string`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `type: "memory_prefix"`

      - `"memory_prefix"`

### Beta Managed Agents Memory Path Conflict Error

- `BetaManagedAgentsMemoryPathConflictError`

  - `type: "memory_path_conflict_error"`

    - `"memory_path_conflict_error"`

  - `conflicting_memory_id?: string`

  - `conflicting_path?: string`

  - `message?: string`

### Beta Managed Agents Memory Precondition Failed Error

- `BetaManagedAgentsMemoryPreconditionFailedError`

  - `type: "memory_precondition_failed_error"`

    - `"memory_precondition_failed_error"`

  - `message?: string`

### Beta Managed Agents Memory Prefix

- `BetaManagedAgentsMemoryPrefix`

  A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

  - `path: string`

    The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

  - `type: "memory_prefix"`

    - `"memory_prefix"`

### Beta Managed Agents Memory View

- `BetaManagedAgentsMemoryView = "basic" | "full"`

  Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

  - `"basic"`

  - `"full"`

### Beta Managed Agents Precondition

- `BetaManagedAgentsPrecondition`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `type: "content_sha256"`

    - `"content_sha256"`

  - `content_sha256?: string`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

# Memory Versions

## List memory versions

`client.beta.memoryStores.memoryVersions.list(stringmemoryStoreID, MemoryVersionListParamsparams?, RequestOptionsoptions?): PageCursor<BetaManagedAgentsMemoryVersion>`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

### Parameters

- `memoryStoreID: string`

- `params: MemoryVersionListParams`

  - `api_key_id?: string`

    Query param: Query parameter for api_key_id

  - `"created_at[gte]"?: string`

    Query param: Return versions created at or after this time (inclusive).

  - `"created_at[lte]"?: string`

    Query param: Return versions created at or before this time (inclusive).

  - `limit?: number`

    Query param: Query parameter for limit

  - `memory_id?: string`

    Query param: Query parameter for memory_id

  - `operation?: BetaManagedAgentsMemoryVersionOperation`

    Query param: Query parameter for operation

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `page?: string`

    Query param: Query parameter for page

  - `service_account_id?: string`

    Query param: Query parameter for service_account_id

  - `session_id?: string`

    Query param: Query parameter for session_id

  - `view?: BetaManagedAgentsMemoryView`

    Query param: Query parameter for view

    - `"basic"`

    - `"full"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaManagedAgentsMemoryVersion`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: string`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_id: string`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

    - `"memory_version"`

  - `content?: string | null`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256?: string | null`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes?: number | null`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by?: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `BetaManagedAgentsSessionActor`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

        ID of the user who performed the write (a `user_...` value).

    - `BetaManagedAgentsServiceAccountActor`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `service_account_id: string`

        ID of the service account that performed the write (a `svac_...` value).

      - `type: "service_account_actor"`

        - `"service_account_actor"`

  - `path?: string | null`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at?: string | null`

    A timestamp in RFC 3339 format

  - `redacted_by?: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsMemoryVersion of client.beta.memoryStores.memoryVersions.list(
  "memory_store_id"
)) {
  console.log(betaManagedAgentsMemoryVersion.id);
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

`client.beta.memoryStores.memoryVersions.retrieve(stringmemoryVersionID, MemoryVersionRetrieveParamsparams, RequestOptionsoptions?): BetaManagedAgentsMemoryVersion`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

### Parameters

- `memoryVersionID: string`

- `params: MemoryVersionRetrieveParams`

  - `memory_store_id: string`

    Path param: Path parameter memory_store_id

  - `view?: BetaManagedAgentsMemoryView`

    Query param: Query parameter for view

    - `"basic"`

    - `"full"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaManagedAgentsMemoryVersion`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: string`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_id: string`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

    - `"memory_version"`

  - `content?: string | null`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256?: string | null`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes?: number | null`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by?: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `BetaManagedAgentsSessionActor`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

        ID of the user who performed the write (a `user_...` value).

    - `BetaManagedAgentsServiceAccountActor`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `service_account_id: string`

        ID of the service account that performed the write (a `svac_...` value).

      - `type: "service_account_actor"`

        - `"service_account_actor"`

  - `path?: string | null`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at?: string | null`

    A timestamp in RFC 3339 format

  - `redacted_by?: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemoryVersion = await client.beta.memoryStores.memoryVersions.retrieve(
  "memory_version_id",
  { memory_store_id: "memory_store_id" }
);

console.log(betaManagedAgentsMemoryVersion.id);
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

`client.beta.memoryStores.memoryVersions.redact(stringmemoryVersionID, MemoryVersionRedactParamsparams, RequestOptionsoptions?): BetaManagedAgentsMemoryVersion`

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a memory version

### Parameters

- `memoryVersionID: string`

- `params: MemoryVersionRedactParams`

  - `memory_store_id: string`

    Path param: Path parameter memory_store_id

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaManagedAgentsMemoryVersion`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: string`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_id: string`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

    - `"memory_version"`

  - `content?: string | null`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256?: string | null`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes?: number | null`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by?: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `BetaManagedAgentsSessionActor`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

        ID of the user who performed the write (a `user_...` value).

    - `BetaManagedAgentsServiceAccountActor`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `service_account_id: string`

        ID of the service account that performed the write (a `svac_...` value).

      - `type: "service_account_actor"`

        - `"service_account_actor"`

  - `path?: string | null`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at?: string | null`

    A timestamp in RFC 3339 format

  - `redacted_by?: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemoryVersion = await client.beta.memoryStores.memoryVersions.redact(
  "memory_version_id",
  { memory_store_id: "memory_store_id" }
);

console.log(betaManagedAgentsMemoryVersion.id);
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

- `BetaManagedAgentsActor = BetaManagedAgentsSessionActor | BetaManagedAgentsAPIActor | BetaManagedAgentsUserActor | BetaManagedAgentsServiceAccountActor`

  Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

  - `BetaManagedAgentsSessionActor`

    Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

    - `session_id: string`

      ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

    - `type: "session_actor"`

      - `"session_actor"`

  - `BetaManagedAgentsAPIActor`

    Attribution for a write made directly via the public API (outside of any session).

    - `api_key_id: string`

      ID of the API key that performed the write. This identifies the key, not the secret.

    - `type: "api_actor"`

      - `"api_actor"`

  - `BetaManagedAgentsUserActor`

    Attribution for a write made by a human user through the Anthropic Console.

    - `type: "user_actor"`

      - `"user_actor"`

    - `user_id: string`

      ID of the user who performed the write (a `user_...` value).

  - `BetaManagedAgentsServiceAccountActor`

    Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

    - `service_account_id: string`

      ID of the service account that performed the write (a `svac_...` value).

    - `type: "service_account_actor"`

      - `"service_account_actor"`

### Beta Managed Agents API Actor

- `BetaManagedAgentsAPIActor`

  Attribution for a write made directly via the public API (outside of any session).

  - `api_key_id: string`

    ID of the API key that performed the write. This identifies the key, not the secret.

  - `type: "api_actor"`

    - `"api_actor"`

### Beta Managed Agents Memory Version

- `BetaManagedAgentsMemoryVersion`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: string`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_id: string`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

    - `"memory_version"`

  - `content?: string | null`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256?: string | null`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes?: number | null`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by?: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `BetaManagedAgentsSessionActor`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

        ID of the user who performed the write (a `user_...` value).

    - `BetaManagedAgentsServiceAccountActor`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `service_account_id: string`

        ID of the service account that performed the write (a `svac_...` value).

      - `type: "service_account_actor"`

        - `"service_account_actor"`

  - `path?: string | null`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at?: string | null`

    A timestamp in RFC 3339 format

  - `redacted_by?: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Beta Managed Agents Memory Version Operation

- `BetaManagedAgentsMemoryVersionOperation = "created" | "modified" | "deleted"`

  The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

  - `"created"`

  - `"modified"`

  - `"deleted"`

### Beta Managed Agents Service Account Actor

- `BetaManagedAgentsServiceAccountActor`

  Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

  - `service_account_id: string`

    ID of the service account that performed the write (a `svac_...` value).

  - `type: "service_account_actor"`

    - `"service_account_actor"`

### Beta Managed Agents Session Actor

- `BetaManagedAgentsSessionActor`

  Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

  - `session_id: string`

    ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

  - `type: "session_actor"`

    - `"session_actor"`

### Beta Managed Agents User Actor

- `BetaManagedAgentsUserActor`

  Attribution for a write made by a human user through the Anthropic Console.

  - `type: "user_actor"`

    - `"user_actor"`

  - `user_id: string`

    ID of the user who performed the write (a `user_...` value).

# Files

## Upload File

`client.beta.files.upload(FileUploadParamsparams, RequestOptionsoptions?): BetaFileMetadata`

**post** `/v1/files`

Upload File

### Parameters

- `params: FileUploadParams`

  - `file: Uploadable`

    Body param: The file to upload

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaFileMetadata`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: string`

    RFC 3339 datetime string representing when the file was created.

  - `filename: string`

    Original filename of the uploaded file.

  - `mime_type: string`

    MIME type of the file.

  - `size_bytes: number`

    Size of the file in bytes.

  - `type: "file"`

    Object type.

    For files, this is always `"file"`.

    - `"file"`

  - `downloadable?: boolean`

    Whether the file can be downloaded.

  - `scope?: BetaFileScope | null`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

      - `"session"`

### Example

```typescript
import fs from "fs";
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaFileMetadata = await client.beta.files.upload({
  file: fs.createReadStream("path/to/file")
});

console.log(betaFileMetadata.id);
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

`client.beta.files.list(FileListParamsparams?, RequestOptionsoptions?): Page<BetaFileMetadata>`

**get** `/v1/files`

List Files

### Parameters

- `params: FileListParams`

  - `after_id?: string`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `before_id?: string`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `limit?: number`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

  - `scope_id?: string`

    Query param: Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaFileMetadata`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: string`

    RFC 3339 datetime string representing when the file was created.

  - `filename: string`

    Original filename of the uploaded file.

  - `mime_type: string`

    MIME type of the file.

  - `size_bytes: number`

    Size of the file in bytes.

  - `type: "file"`

    Object type.

    For files, this is always `"file"`.

    - `"file"`

  - `downloadable?: boolean`

    Whether the file can be downloaded.

  - `scope?: BetaFileScope | null`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

      - `"session"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaFileMetadata of client.beta.files.list()) {
  console.log(betaFileMetadata.id);
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

`client.beta.files.download(stringfileID, FileDownloadParamsparams?, RequestOptionsoptions?): Response`

**get** `/v1/files/{file_id}/content`

Download File

### Parameters

- `fileID: string`

  ID of the File.

- `params: FileDownloadParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `unnamed_schema_1 = Response`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const response = await client.beta.files.download("file_id");

console.log(response);

const content = await response.blob();
console.log(content);
```

## Get File Metadata

`client.beta.files.retrieveMetadata(stringfileID, FileRetrieveMetadataParamsparams?, RequestOptionsoptions?): BetaFileMetadata`

**get** `/v1/files/{file_id}`

Get File Metadata

### Parameters

- `fileID: string`

  ID of the File.

- `params: FileRetrieveMetadataParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaFileMetadata`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: string`

    RFC 3339 datetime string representing when the file was created.

  - `filename: string`

    Original filename of the uploaded file.

  - `mime_type: string`

    MIME type of the file.

  - `size_bytes: number`

    Size of the file in bytes.

  - `type: "file"`

    Object type.

    For files, this is always `"file"`.

    - `"file"`

  - `downloadable?: boolean`

    Whether the file can be downloaded.

  - `scope?: BetaFileScope | null`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

      - `"session"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaFileMetadata = await client.beta.files.retrieveMetadata("file_id");

console.log(betaFileMetadata.id);
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

`client.beta.files.delete(stringfileID, FileDeleteParamsparams?, RequestOptionsoptions?): BetaDeletedFile`

**delete** `/v1/files/{file_id}`

Delete File

### Parameters

- `fileID: string`

  ID of the File.

- `params: FileDeleteParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaDeletedFile`

  - `id: string`

    ID of the deleted file.

  - `type?: "file_deleted"`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaDeletedFile = await client.beta.files.delete("file_id");

console.log(betaDeletedFile.id);
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

- `BetaDeletedFile`

  - `id: string`

    ID of the deleted file.

  - `type?: "file_deleted"`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"`

### Beta File Metadata

- `BetaFileMetadata`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: string`

    RFC 3339 datetime string representing when the file was created.

  - `filename: string`

    Original filename of the uploaded file.

  - `mime_type: string`

    MIME type of the file.

  - `size_bytes: number`

    Size of the file in bytes.

  - `type: "file"`

    Object type.

    For files, this is always `"file"`.

    - `"file"`

  - `downloadable?: boolean`

    Whether the file can be downloaded.

  - `scope?: BetaFileScope | null`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

      - `"session"`

### Beta File Scope

- `BetaFileScope`

  - `id: string`

    The ID of the scoping resource (e.g., the session ID).

  - `type: "session"`

    The type of scope (e.g., `"session"`).

    - `"session"`

# Skills

## Create Skill

`client.beta.skills.create(SkillCreateParamsparams, RequestOptionsoptions?): SkillCreateResponse`

**post** `/v1/skills`

Create Skill

### Parameters

- `params: SkillCreateParams`

  - `files: Array<Uploadable>`

    Body param: Files to upload for the skill.

    All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

  - `display_title?: string | null`

    Body param: Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `SkillCreateResponse`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: string | null`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: string | null`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: string`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: string`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: string`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const skill = await client.beta.skills.create({
  files: [fs.createReadStream("path/to/file")]
});

console.log(skill.id);
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

`client.beta.skills.list(SkillListParamsparams?, RequestOptionsoptions?): PageCursor<SkillListResponse>`

**get** `/v1/skills`

List Skills

### Parameters

- `params: SkillListParams`

  - `limit?: number`

    Query param: Number of results to return per page.

    Maximum value is 100. Defaults to 20.

  - `page?: string | null`

    Query param: Pagination token for fetching a specific page of results.

    Pass the value from a previous response's `next_page` field to get the next page of results.

  - `source?: string | null`

    Query param: Filter skills by source.

    If provided, only skills from the specified source will be returned:

    * `"custom"`: only return user-created skills
    * `"anthropic"`: only return Anthropic-created skills

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `SkillListResponse`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: string | null`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: string | null`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: string`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: string`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: string`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const skillListResponse of client.beta.skills.list()) {
  console.log(skillListResponse.id);
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

`client.beta.skills.retrieve(stringskillID, SkillRetrieveParamsparams?, RequestOptionsoptions?): SkillRetrieveResponse`

**get** `/v1/skills/{skill_id}`

Get Skill

### Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `params: SkillRetrieveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `SkillRetrieveResponse`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: string | null`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: string | null`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: string`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: string`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: string`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const skill = await client.beta.skills.retrieve("skill_id");

console.log(skill.id);
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

`client.beta.skills.delete(stringskillID, SkillDeleteParamsparams?, RequestOptionsoptions?): SkillDeleteResponse`

**delete** `/v1/skills/{skill_id}`

Delete Skill

### Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `params: SkillDeleteParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `SkillDeleteResponse`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `type: string`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const skill = await client.beta.skills.delete("skill_id");

console.log(skill.id);
```

#### Response

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type"
}
```

## Domain Types

### Skill Create Response

- `SkillCreateResponse`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: string | null`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: string | null`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: string`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: string`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: string`

    ISO 8601 timestamp of when the skill was last updated.

### Skill List Response

- `SkillListResponse`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: string | null`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: string | null`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: string`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: string`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: string`

    ISO 8601 timestamp of when the skill was last updated.

### Skill Retrieve Response

- `SkillRetrieveResponse`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: string | null`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: string | null`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: string`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: string`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: string`

    ISO 8601 timestamp of when the skill was last updated.

### Skill Delete Response

- `SkillDeleteResponse`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `type: string`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

# Versions

## Create Skill Version

`client.beta.skills.versions.create(stringskillID, VersionCreateParamsparams, RequestOptionsoptions?): VersionCreateResponse`

**post** `/v1/skills/{skill_id}/versions`

Create Skill Version

### Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `params: VersionCreateParams`

  - `files: Array<Uploadable>`

    Body param: Files to upload for the skill.

    All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `VersionCreateResponse`

  - `id: string`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill version was created.

  - `description: string`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: string`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: string`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: string`

    Identifier for the skill that this version belongs to.

  - `type: string`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const version = await client.beta.skills.versions.create("skill_id", {
  files: [fs.createReadStream("path/to/file")]
});

console.log(version.id);
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

`client.beta.skills.versions.list(stringskillID, VersionListParamsparams?, RequestOptionsoptions?): PageCursor<VersionListResponse>`

**get** `/v1/skills/{skill_id}/versions`

List Skill Versions

### Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `params: VersionListParams`

  - `limit?: number | null`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

  - `page?: string | null`

    Query param: Optionally set to the `next_page` token from the previous response.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `VersionListResponse`

  - `id: string`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill version was created.

  - `description: string`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: string`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: string`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: string`

    Identifier for the skill that this version belongs to.

  - `type: string`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const versionListResponse of client.beta.skills.versions.list("skill_id")) {
  console.log(versionListResponse.id);
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

`client.beta.skills.versions.download(stringversion, VersionDownloadParamsparams, RequestOptionsoptions?): Response`

**get** `/v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

### Parameters

- `version: string`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `params: VersionDownloadParams`

  - `skill_id: string`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `unnamed_schema_2 = Response`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const response = await client.beta.skills.versions.download("version", {
  skill_id: "skill_id"
});

console.log(response);

const content = await response.blob();
console.log(content);
```

## Get Skill Version

`client.beta.skills.versions.retrieve(stringversion, VersionRetrieveParamsparams, RequestOptionsoptions?): VersionRetrieveResponse`

**get** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

### Parameters

- `version: string`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `params: VersionRetrieveParams`

  - `skill_id: string`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `VersionRetrieveResponse`

  - `id: string`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill version was created.

  - `description: string`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: string`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: string`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: string`

    Identifier for the skill that this version belongs to.

  - `type: string`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const version = await client.beta.skills.versions.retrieve("version", {
  skill_id: "skill_id"
});

console.log(version.id);
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

`client.beta.skills.versions.delete(stringversion, VersionDeleteParamsparams, RequestOptionsoptions?): VersionDeleteResponse`

**delete** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

### Parameters

- `version: string`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `params: VersionDeleteParams`

  - `skill_id: string`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `VersionDeleteResponse`

  - `id: string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `type: string`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const version = await client.beta.skills.versions.delete("version", { skill_id: "skill_id" });

console.log(version.id);
```

#### Response

```json
{
  "id": "1759178010641129",
  "type": "type"
}
```

## Domain Types

### Version Create Response

- `VersionCreateResponse`

  - `id: string`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill version was created.

  - `description: string`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: string`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: string`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: string`

    Identifier for the skill that this version belongs to.

  - `type: string`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Version List Response

- `VersionListResponse`

  - `id: string`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill version was created.

  - `description: string`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: string`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: string`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: string`

    Identifier for the skill that this version belongs to.

  - `type: string`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Version Retrieve Response

- `VersionRetrieveResponse`

  - `id: string`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill version was created.

  - `description: string`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: string`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: string`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: string`

    Identifier for the skill that this version belongs to.

  - `type: string`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Version Delete Response

- `VersionDeleteResponse`

  - `id: string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `type: string`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

# User Profiles

## Create User Profile

`client.beta.userProfiles.create(UserProfileCreateParamsparams, RequestOptionsoptions?): BetaUserProfile`

**post** `/v1/user_profiles`

Create User Profile

### Parameters

- `params: UserProfileCreateParams`

  - `access_type?: "application" | "passthrough"`

    Body param: How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id?: string | null`

    Body param: Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

  - `metadata?: Record<string, string>`

    Body param: Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

  - `name?: string | null`

    Body param: Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a resold-to company (`relationship` `resold` / `access_type` `passthrough`), that company's name where known. Maximum 255 characters.

  - `relationship?: "external" | "resold" | "internal"`

    Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaUserProfile`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Record<string, BetaUserProfileTrustGrant>`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" | "pending" | "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `access_type?: "application" | "passthrough"`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id?: string | null`

    Platform's own identifier for this user. Not enforced unique.

  - `name?: string | null`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship?: "external" | "resold" | "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaUserProfile = await client.beta.userProfiles.create();

console.log(betaUserProfile.id);
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

`client.beta.userProfiles.list(UserProfileListParamsparams?, RequestOptionsoptions?): PageCursor<BetaUserProfile>`

**get** `/v1/user_profiles`

List User Profiles

### Parameters

- `params: UserProfileListParams`

  - `limit?: number`

    Query param: Query parameter for limit

  - `order?: "asc" | "desc"`

    Query param: Query parameter for order

    - `"asc"`

    - `"desc"`

  - `page?: string`

    Query param: Query parameter for page

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaUserProfile`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Record<string, BetaUserProfileTrustGrant>`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" | "pending" | "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `access_type?: "application" | "passthrough"`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id?: string | null`

    Platform's own identifier for this user. Not enforced unique.

  - `name?: string | null`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship?: "external" | "resold" | "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaUserProfile of client.beta.userProfiles.list()) {
  console.log(betaUserProfile.id);
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

`client.beta.userProfiles.retrieve(stringuserProfileID, UserProfileRetrieveParamsparams?, RequestOptionsoptions?): BetaUserProfile`

**get** `/v1/user_profiles/{user_profile_id}`

Get User Profile

### Parameters

- `userProfileID: string`

- `params: UserProfileRetrieveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaUserProfile`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Record<string, BetaUserProfileTrustGrant>`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" | "pending" | "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `access_type?: "application" | "passthrough"`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id?: string | null`

    Platform's own identifier for this user. Not enforced unique.

  - `name?: string | null`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship?: "external" | "resold" | "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaUserProfile = await client.beta.userProfiles.retrieve(
  "uprof_011CZkZCu8hGbp5mYRQgUmz9"
);

console.log(betaUserProfile.id);
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

`client.beta.userProfiles.update(stringuserProfileID, UserProfileUpdateParamsparams, RequestOptionsoptions?): BetaUserProfile`

**post** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `userProfileID: string`

- `params: UserProfileUpdateParams`

  - `access_type?: "application" | "passthrough" | null`

    Body param: How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id?: string | null`

    Body param: If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

  - `metadata?: Record<string, string>`

    Body param: Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

  - `name?: string | null`

    Body param: If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

  - `relationship?: "external" | "resold" | "internal" | null`

    Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaUserProfile`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Record<string, BetaUserProfileTrustGrant>`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" | "pending" | "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `access_type?: "application" | "passthrough"`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id?: string | null`

    Platform's own identifier for this user. Not enforced unique.

  - `name?: string | null`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship?: "external" | "resold" | "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaUserProfile = await client.beta.userProfiles.update(
  "uprof_011CZkZCu8hGbp5mYRQgUmz9"
);

console.log(betaUserProfile.id);
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

`client.beta.userProfiles.createEnrollmentURL(stringuserProfileID, UserProfileCreateEnrollmentURLParamsparams?, RequestOptionsoptions?): BetaUserProfileEnrollmentURL`

**post** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Parameters

- `userProfileID: string`

- `params: UserProfileCreateEnrollmentURLParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaUserProfileEnrollmentURL`

  - `expires_at: string`

    A timestamp in RFC 3339 format

  - `type: "enrollment_url"`

    Object type. Always `enrollment_url`.

    - `"enrollment_url"`

  - `url: string`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaUserProfileEnrollmentURL = await client.beta.userProfiles.createEnrollmentURL(
  "uprof_011CZkZCu8hGbp5mYRQgUmz9"
);

console.log(betaUserProfileEnrollmentURL.expires_at);
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

- `BetaUserProfile`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Record<string, BetaUserProfileTrustGrant>`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" | "pending" | "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `access_type?: "application" | "passthrough"`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id?: string | null`

    Platform's own identifier for this user. Not enforced unique.

  - `name?: string | null`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship?: "external" | "resold" | "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

### Beta User Profile Enrollment URL

- `BetaUserProfileEnrollmentURL`

  - `expires_at: string`

    A timestamp in RFC 3339 format

  - `type: "enrollment_url"`

    Object type. Always `enrollment_url`.

    - `"enrollment_url"`

  - `url: string`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Beta User Profile Trust Grant

- `BetaUserProfileTrustGrant`

  - `status: "active" | "pending" | "rejected"`

    Status of the trust grant.

    - `"active"`

    - `"pending"`

    - `"rejected"`

# Dreams

## Create a Dream

`client.beta.dreams.create(DreamCreateParamsparams, RequestOptionsoptions?): BetaDream`

**post** `/v1/dreams`

Create a Dream

### Parameters

- `params: DreamCreateParams`

  - `inputs: Array<BetaDreamInput>`

    Body param

    - `BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array<string>`

      - `type: "sessions"`

        - `"sessions"`

  - `model: string | BetaDreamModelConfigParam`

    Body param: Model identifier and configuration applied to every pipeline stage.

    - `string`

    - `BetaDreamModelConfigParam`

      Model identifier and configuration applied to every pipeline stage.

      - `id: string`

        Model identifier, e.g. "claude-opus-5". 1-256 characters.

      - `speed?: "standard" | "fast" | null`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `instructions?: string | null`

    Body param

  - `output_behavior?: BetaOutputBehavior`

    Body param: The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: "create_new"`

        - `"create_new"`

    - `BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: string`

      - `type: "update_existing"`

        - `"update_existing"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaDream`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `ended_at: string | null`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError | null`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: Array<BetaDreamInput>`

    - `BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array<string>`

      - `type: "sessions"`

        - `"sessions"`

  - `instructions: string | null`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed?: "standard" | "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: "create_new"`

        - `"create_new"`

    - `BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: string`

      - `type: "update_existing"`

        - `"update_existing"`

  - `outputs: Array<BetaDreamOutput>`

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `session_id: string | null`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaDream = await client.beta.dreams.create({
  inputs: [{ memory_store_id: "x", type: "memory_store" }],
  model: "string"
});

console.log(betaDream.id);
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

`client.beta.dreams.list(DreamListParamsparams?, RequestOptionsoptions?): PageCursor<BetaDream>`

**get** `/v1/dreams`

List Dreams

### Parameters

- `params: DreamListParams`

  - `"created_at[gt]"?: string`

    Query param: Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

  - `"created_at[lt]"?: string`

    Query param: Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

  - `include_archived?: boolean`

    Query param: Query parameter for include_archived

  - `limit?: number`

    Query param: Query parameter for limit

  - `page?: string`

    Query param: Query parameter for page

  - `statuses?: Array<BetaDreamStatus>`

    Query param: Filter by lifecycle status. Repeat the parameter to match any of multiple statuses. Empty applies no status filter.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaDream`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `ended_at: string | null`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError | null`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: Array<BetaDreamInput>`

    - `BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array<string>`

      - `type: "sessions"`

        - `"sessions"`

  - `instructions: string | null`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed?: "standard" | "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: "create_new"`

        - `"create_new"`

    - `BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: string`

      - `type: "update_existing"`

        - `"update_existing"`

  - `outputs: Array<BetaDreamOutput>`

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `session_id: string | null`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaDream of client.beta.dreams.list()) {
  console.log(betaDream.id);
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

`client.beta.dreams.retrieve(stringdreamID, DreamRetrieveParamsparams?, RequestOptionsoptions?): BetaDream`

**get** `/v1/dreams/{dream_id}`

Get a Dream

### Parameters

- `dreamID: string`

- `params: DreamRetrieveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaDream`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `ended_at: string | null`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError | null`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: Array<BetaDreamInput>`

    - `BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array<string>`

      - `type: "sessions"`

        - `"sessions"`

  - `instructions: string | null`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed?: "standard" | "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: "create_new"`

        - `"create_new"`

    - `BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: string`

      - `type: "update_existing"`

        - `"update_existing"`

  - `outputs: Array<BetaDreamOutput>`

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `session_id: string | null`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaDream = await client.beta.dreams.retrieve("dream_id");

console.log(betaDream.id);
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

`client.beta.dreams.cancel(stringdreamID, DreamCancelParamsparams?, RequestOptionsoptions?): BetaDream`

**post** `/v1/dreams/{dream_id}/cancel`

Cancel a Dream

### Parameters

- `dreamID: string`

- `params: DreamCancelParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaDream`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `ended_at: string | null`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError | null`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: Array<BetaDreamInput>`

    - `BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array<string>`

      - `type: "sessions"`

        - `"sessions"`

  - `instructions: string | null`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed?: "standard" | "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: "create_new"`

        - `"create_new"`

    - `BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: string`

      - `type: "update_existing"`

        - `"update_existing"`

  - `outputs: Array<BetaDreamOutput>`

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `session_id: string | null`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaDream = await client.beta.dreams.cancel("dream_id");

console.log(betaDream.id);
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

`client.beta.dreams.archive(stringdreamID, DreamArchiveParamsparams?, RequestOptionsoptions?): BetaDream`

**post** `/v1/dreams/{dream_id}/archive`

Archive a Dream

### Parameters

- `dreamID: string`

- `params: DreamArchiveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaDream`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `ended_at: string | null`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError | null`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: Array<BetaDreamInput>`

    - `BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array<string>`

      - `type: "sessions"`

        - `"sessions"`

  - `instructions: string | null`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed?: "standard" | "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: "create_new"`

        - `"create_new"`

    - `BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: string`

      - `type: "update_existing"`

        - `"update_existing"`

  - `outputs: Array<BetaDreamOutput>`

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `session_id: string | null`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaDream = await client.beta.dreams.archive("dream_id");

console.log(betaDream.id);
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

- `BetaDream`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `ended_at: string | null`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError | null`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: Array<BetaDreamInput>`

    - `BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array<string>`

      - `type: "sessions"`

        - `"sessions"`

  - `instructions: string | null`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed?: "standard" | "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: "create_new"`

        - `"create_new"`

    - `BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: string`

      - `type: "update_existing"`

        - `"update_existing"`

  - `outputs: Array<BetaDreamOutput>`

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `session_id: string | null`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

### Beta Dream Error

- `BetaDreamError`

  Failure detail for a Dream whose `status` is `failed`.

  - `message: string`

  - `type: string`

### Beta Dream Input

- `BetaDreamInput = BetaDreamMemoryStoreInput | BetaDreamSessionsInput`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `BetaDreamMemoryStoreInput`

    An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `BetaDreamSessionsInput`

    Input session transcripts the dream reads.

    - `session_ids: Array<string>`

    - `type: "sessions"`

      - `"sessions"`

### Beta Dream Memory Store Input

- `BetaDreamMemoryStoreInput`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `memory_store_id: string`

  - `type: "memory_store"`

    - `"memory_store"`

### Beta Dream Memory Store Output

- `BetaDreamMemoryStoreOutput`

  An output memory store the dream writes consolidated memories into.

  - `memory_store_id: string`

  - `type: "memory_store"`

    - `"memory_store"`

### Beta Dream Model Config

- `BetaDreamModelConfig`

  Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

  - `id: string`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

  - `speed?: "standard" | "fast"`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Dream Model Config Param

- `BetaDreamModelConfigParam`

  Model identifier and configuration applied to every pipeline stage.

  - `id: string`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

  - `speed?: "standard" | "fast" | null`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Dream Output

- `BetaDreamOutput`

  An output memory store the dream writes consolidated memories into.

  - `memory_store_id: string`

  - `type: "memory_store"`

    - `"memory_store"`

### Beta Dream Sessions Input

- `BetaDreamSessionsInput`

  Input session transcripts the dream reads.

  - `session_ids: Array<string>`

  - `type: "sessions"`

    - `"sessions"`

### Beta Dream Status

- `BetaDreamStatus = "pending" | "running" | "completed" | 2 more`

  Lifecycle status of a Dream.

  - `"pending"`

  - `"running"`

  - `"completed"`

  - `"failed"`

  - `"canceled"`

### Beta Dream Usage

- `BetaDreamUsage`

  Cumulative token usage for the dream across every pipeline stage.

  - `cache_creation_input_tokens: number`

    Total tokens used to create prompt-cache entries (sum of all TTL tiers).

  - `cache_read_input_tokens: number`

    Total tokens read from prompt cache.

  - `input_tokens: number`

    Total uncached input tokens consumed across every pipeline stage.

  - `output_tokens: number`

    Total output tokens generated across every pipeline stage.

### Beta Output Behavior

- `BetaOutputBehavior = BetaOutputBehaviorCreateNew | BetaOutputBehaviorUpdateExisting`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `BetaOutputBehaviorCreateNew`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `type: "create_new"`

      - `"create_new"`

  - `BetaOutputBehaviorUpdateExisting`

    The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

    - `memory_store_id: string`

    - `type: "update_existing"`

      - `"update_existing"`

### Beta Output Behavior Create New

- `BetaOutputBehaviorCreateNew`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `type: "create_new"`

    - `"create_new"`

### Beta Output Behavior Update Existing

- `BetaOutputBehaviorUpdateExisting`

  The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

  - `memory_store_id: string`

  - `type: "update_existing"`

    - `"update_existing"`

# Tunnels

## Create Tunnel

`client.beta.tunnels.create(TunnelCreateParamsparams, RequestOptionsoptions?): BetaTunnel`

**post** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

### Parameters

- `params: TunnelCreateParams`

  - `display_name?: string | null`

    Body param: Optional human-readable name for the tunnel (1-255 characters).

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaTunnel`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string | null`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

    - `"tunnel"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnel = await client.beta.tunnels.create();

console.log(betaTunnel.id);
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

`client.beta.tunnels.retrieve(stringtunnelID, TunnelRetrieveParamsparams?, RequestOptionsoptions?): BetaTunnel`

**get** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

### Parameters

- `tunnelID: string`

- `params: TunnelRetrieveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaTunnel`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string | null`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

    - `"tunnel"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnel = await client.beta.tunnels.retrieve("tunnel_id");

console.log(betaTunnel.id);
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

`client.beta.tunnels.list(TunnelListParamsparams?, RequestOptionsoptions?): PageCursor<BetaTunnel>`

**get** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

### Parameters

- `params: TunnelListParams`

  - `include_archived?: boolean`

    Query param: Whether to include archived tunnels in the results. Defaults to false.

  - `limit?: number`

    Query param: Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

  - `page?: string`

    Query param: Opaque pagination cursor from a previous `list_tunnels` response.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaTunnel`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string | null`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

    - `"tunnel"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaTunnel of client.beta.tunnels.list()) {
  console.log(betaTunnel.id);
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

`client.beta.tunnels.archive(stringtunnelID, TunnelArchiveParamsparams?, RequestOptionsoptions?): BetaTunnel`

**post** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

### Parameters

- `tunnelID: string`

- `params: TunnelArchiveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaTunnel`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string | null`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

    - `"tunnel"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnel = await client.beta.tunnels.archive("tunnel_id");

console.log(betaTunnel.id);
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

`client.beta.tunnels.revealToken(stringtunnelID, TunnelRevealTokenParamsparams?, RequestOptionsoptions?): BetaTunnelToken`

**post** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

### Parameters

- `tunnelID: string`

- `params: TunnelRevealTokenParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaTunnelToken`

  A tunnel's connector token.

  - `id: string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: string`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: "tunnel_token"`

    - `"tunnel_token"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnelToken = await client.beta.tunnels.revealToken("tunnel_id");

console.log(betaTunnelToken.id);
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

`client.beta.tunnels.rotateToken(stringtunnelID, TunnelRotateTokenParamsparams, RequestOptionsoptions?): BetaTunnelToken`

**post** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

### Parameters

- `tunnelID: string`

- `params: TunnelRotateTokenParams`

  - `reason?: string | null`

    Body param: Optional free-text reason for the rotation, recorded for audit.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaTunnelToken`

  A tunnel's connector token.

  - `id: string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: string`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: "tunnel_token"`

    - `"tunnel_token"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnelToken = await client.beta.tunnels.rotateToken("tunnel_id");

console.log(betaTunnelToken.id);
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

- `BetaTunnel`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string | null`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

    - `"tunnel"`

### Beta Tunnel Token

- `BetaTunnelToken`

  A tunnel's connector token.

  - `id: string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: string`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: "tunnel_token"`

    - `"tunnel_token"`

# Certificates

## Create Tunnel Certificate

`client.beta.tunnels.certificates.create(stringtunnelID, CertificateCreateParamsparams, RequestOptionsoptions?): BetaTunnelCertificate`

**post** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

### Parameters

- `tunnelID: string`

- `params: CertificateCreateParams`

  - `ca_certificate_pem: string`

    Body param: PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string | null`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

    - `"tunnel_certificate"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnelCertificate = await client.beta.tunnels.certificates.create("tunnel_id", {
  ca_certificate_pem: "ca_certificate_pem"
});

console.log(betaTunnelCertificate.id);
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

`client.beta.tunnels.certificates.retrieve(stringcertificateID, CertificateRetrieveParamsparams, RequestOptionsoptions?): BetaTunnelCertificate`

**get** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

### Parameters

- `certificateID: string`

- `params: CertificateRetrieveParams`

  - `tunnel_id: string`

    Path param: Path parameter tunnel_id

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string | null`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

    - `"tunnel_certificate"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnelCertificate = await client.beta.tunnels.certificates.retrieve(
  "certificate_id",
  { tunnel_id: "tunnel_id" }
);

console.log(betaTunnelCertificate.id);
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

`client.beta.tunnels.certificates.list(stringtunnelID, CertificateListParamsparams?, RequestOptionsoptions?): PageCursor<BetaTunnelCertificate>`

**get** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

### Parameters

- `tunnelID: string`

- `params: CertificateListParams`

  - `include_archived?: boolean`

    Query param: Whether to include archived certificates in the results. Defaults to false.

  - `limit?: number`

    Query param: Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

  - `page?: string`

    Query param: Opaque pagination cursor from a previous `list_tunnel_certificates` response.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string | null`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

    - `"tunnel_certificate"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaTunnelCertificate of client.beta.tunnels.certificates.list("tunnel_id")) {
  console.log(betaTunnelCertificate.id);
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

`client.beta.tunnels.certificates.archive(stringcertificateID, CertificateArchiveParamsparams, RequestOptionsoptions?): BetaTunnelCertificate`

**post** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

### Parameters

- `certificateID: string`

- `params: CertificateArchiveParams`

  - `tunnel_id: string`

    Path param: Path parameter tunnel_id

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string | null`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

    - `"tunnel_certificate"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnelCertificate = await client.beta.tunnels.certificates.archive(
  "certificate_id",
  { tunnel_id: "tunnel_id" }
);

console.log(betaTunnelCertificate.id);
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

- `BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string | null`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

    - `"tunnel_certificate"`

# Webhooks

## Domain Types

### Beta Webhook Agent Archived Event Data

- `BetaWebhookAgentArchivedEventData`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.archived"`

    - `"agent.archived"`

  - `workspace_id: string`

### Beta Webhook Agent Created Event Data

- `BetaWebhookAgentCreatedEventData`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.created"`

    - `"agent.created"`

  - `workspace_id: string`

### Beta Webhook Agent Deleted Event Data

- `BetaWebhookAgentDeletedEventData`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.deleted"`

    - `"agent.deleted"`

  - `workspace_id: string`

### Beta Webhook Agent Updated Event Data

- `BetaWebhookAgentUpdatedEventData`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.updated"`

    - `"agent.updated"`

  - `workspace_id: string`

### Beta Webhook Deployment Archived Event Data

- `BetaWebhookDeploymentArchivedEventData`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.archived"`

    - `"deployment.archived"`

  - `workspace_id: string`

### Beta Webhook Deployment Created Event Data

- `BetaWebhookDeploymentCreatedEventData`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.created"`

    - `"deployment.created"`

  - `workspace_id: string`

### Beta Webhook Deployment Deleted Event Data

- `BetaWebhookDeploymentDeletedEventData`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.deleted"`

    - `"deployment.deleted"`

  - `workspace_id: string`

### Beta Webhook Deployment Paused Event Data

- `BetaWebhookDeploymentPausedEventData`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.paused"`

    - `"deployment.paused"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Failed Event Data

- `BetaWebhookDeploymentRunFailedEventData`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.failed"`

    - `"deployment_run.failed"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Started Event Data

- `BetaWebhookDeploymentRunStartedEventData`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.started"`

    - `"deployment_run.started"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Succeeded Event Data

- `BetaWebhookDeploymentRunSucceededEventData`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.succeeded"`

    - `"deployment_run.succeeded"`

  - `workspace_id: string`

### Beta Webhook Deployment Unpaused Event Data

- `BetaWebhookDeploymentUnpausedEventData`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.unpaused"`

    - `"deployment.unpaused"`

  - `workspace_id: string`

### Beta Webhook Deployment Updated Event Data

- `BetaWebhookDeploymentUpdatedEventData`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.updated"`

    - `"deployment.updated"`

  - `workspace_id: string`

### Beta Webhook Environment Archived Event Data

- `BetaWebhookEnvironmentArchivedEventData`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.archived"`

    - `"environment.archived"`

  - `workspace_id: string`

### Beta Webhook Environment Created Event Data

- `BetaWebhookEnvironmentCreatedEventData`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.created"`

    - `"environment.created"`

  - `workspace_id: string`

### Beta Webhook Environment Deleted Event Data

- `BetaWebhookEnvironmentDeletedEventData`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.deleted"`

    - `"environment.deleted"`

  - `workspace_id: string`

### Beta Webhook Environment Updated Event Data

- `BetaWebhookEnvironmentUpdatedEventData`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.updated"`

    - `"environment.updated"`

  - `workspace_id: string`

### Beta Webhook Event

- `BetaWebhookEvent`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `BetaWebhookSessionCreatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

        - `"session.created"`

      - `workspace_id: string`

    - `BetaWebhookSessionPendingEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

        - `"session.pending"`

      - `workspace_id: string`

    - `BetaWebhookSessionRunningEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

        - `"session.running"`

      - `workspace_id: string`

    - `BetaWebhookSessionIdledEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

        - `"session.idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionRequiresActionEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

        - `"session.requires_action"`

      - `workspace_id: string`

    - `BetaWebhookSessionArchivedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

        - `"session.archived"`

      - `workspace_id: string`

    - `BetaWebhookSessionDeletedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

        - `"session.deleted"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRescheduledEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_rescheduled"`

        - `"session.status_rescheduled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRunStartedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

        - `"session.status_run_started"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusIdledEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

        - `"session.status_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusTerminatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

        - `"session.status_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadCreatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_created"`

        - `"session.thread_created"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadIdledEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_idled"`

        - `"session.thread_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadTerminatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_terminated"`

        - `"session.thread_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `BetaWebhookVaultCreatedEventData`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

        - `"vault.created"`

      - `workspace_id: string`

    - `BetaWebhookVaultArchivedEventData`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

        - `"vault.archived"`

      - `workspace_id: string`

    - `BetaWebhookVaultDeletedEventData`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

        - `"vault.deleted"`

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialCreatedEventData`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

        - `"vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialArchivedEventData`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

        - `"vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialDeletedEventData`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

        - `"vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialRefreshFailedEventData`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.refresh_failed"`

        - `"vault_credential.refresh_failed"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookSessionUpdatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.updated"`

        - `"session.updated"`

      - `workspace_id: string`

    - `BetaWebhookAgentCreatedEventData`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.created"`

        - `"agent.created"`

      - `workspace_id: string`

    - `BetaWebhookAgentArchivedEventData`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.archived"`

        - `"agent.archived"`

      - `workspace_id: string`

    - `BetaWebhookAgentDeletedEventData`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.deleted"`

        - `"agent.deleted"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentPausedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.paused"`

        - `"deployment.paused"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunFailedEventData`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.failed"`

        - `"deployment_run.failed"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentCreatedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.created"`

        - `"deployment.created"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUpdatedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.updated"`

        - `"deployment.updated"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUnpausedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.unpaused"`

        - `"deployment.unpaused"`

      - `workspace_id: string`

    - `BetaWebhookAgentUpdatedEventData`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.updated"`

        - `"agent.updated"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentArchivedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.archived"`

        - `"deployment.archived"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunStartedEventData`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.started"`

        - `"deployment_run.started"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentDeletedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.deleted"`

        - `"deployment.deleted"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunSucceededEventData`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.succeeded"`

        - `"deployment_run.succeeded"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentCreatedEventData`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.created"`

        - `"environment.created"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentUpdatedEventData`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.updated"`

        - `"environment.updated"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentArchivedEventData`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.archived"`

        - `"environment.archived"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentDeletedEventData`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.deleted"`

        - `"environment.deleted"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreCreatedEventData`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.created"`

        - `"memory_store.created"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreArchivedEventData`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.archived"`

        - `"memory_store.archived"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreDeletedEventData`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.deleted"`

        - `"memory_store.deleted"`

      - `workspace_id: string`

    - `BetaWebhookSessionBudgetReachedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.budget_reached"`

        - `"session.budget_reached"`

      - `workspace_id: string`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

    - `"event"`

### Beta Webhook Event Data

- `BetaWebhookEventData = BetaWebhookSessionCreatedEventData | BetaWebhookSessionPendingEventData | BetaWebhookSessionRunningEventData | 41 more`

  - `BetaWebhookSessionCreatedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.created"`

      - `"session.created"`

    - `workspace_id: string`

  - `BetaWebhookSessionPendingEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.pending"`

      - `"session.pending"`

    - `workspace_id: string`

  - `BetaWebhookSessionRunningEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.running"`

      - `"session.running"`

    - `workspace_id: string`

  - `BetaWebhookSessionIdledEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.idled"`

      - `"session.idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionRequiresActionEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.requires_action"`

      - `"session.requires_action"`

    - `workspace_id: string`

  - `BetaWebhookSessionArchivedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.archived"`

      - `"session.archived"`

    - `workspace_id: string`

  - `BetaWebhookSessionDeletedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.deleted"`

      - `"session.deleted"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusRescheduledEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_rescheduled"`

      - `"session.status_rescheduled"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusRunStartedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_run_started"`

      - `"session.status_run_started"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusIdledEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_idled"`

      - `"session.status_idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusTerminatedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_terminated"`

      - `"session.status_terminated"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadCreatedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_created"`

      - `"session.thread_created"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadIdledEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_idled"`

      - `"session.thread_idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadTerminatedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_terminated"`

      - `"session.thread_terminated"`

    - `workspace_id: string`

  - `BetaWebhookSessionOutcomeEvaluationEndedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.outcome_evaluation_ended"`

      - `"session.outcome_evaluation_ended"`

    - `workspace_id: string`

  - `BetaWebhookVaultCreatedEventData`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.created"`

      - `"vault.created"`

    - `workspace_id: string`

  - `BetaWebhookVaultArchivedEventData`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.archived"`

      - `"vault.archived"`

    - `workspace_id: string`

  - `BetaWebhookVaultDeletedEventData`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.deleted"`

      - `"vault.deleted"`

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialCreatedEventData`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.created"`

      - `"vault_credential.created"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialArchivedEventData`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.archived"`

      - `"vault_credential.archived"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialDeletedEventData`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.deleted"`

      - `"vault_credential.deleted"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialRefreshFailedEventData`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.refresh_failed"`

      - `"vault_credential.refresh_failed"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookSessionUpdatedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.updated"`

      - `"session.updated"`

    - `workspace_id: string`

  - `BetaWebhookAgentCreatedEventData`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.created"`

      - `"agent.created"`

    - `workspace_id: string`

  - `BetaWebhookAgentArchivedEventData`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.archived"`

      - `"agent.archived"`

    - `workspace_id: string`

  - `BetaWebhookAgentDeletedEventData`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.deleted"`

      - `"agent.deleted"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentPausedEventData`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.paused"`

      - `"deployment.paused"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunFailedEventData`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.failed"`

      - `"deployment_run.failed"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentCreatedEventData`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.created"`

      - `"deployment.created"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentUpdatedEventData`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.updated"`

      - `"deployment.updated"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentUnpausedEventData`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.unpaused"`

      - `"deployment.unpaused"`

    - `workspace_id: string`

  - `BetaWebhookAgentUpdatedEventData`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.updated"`

      - `"agent.updated"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentArchivedEventData`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.archived"`

      - `"deployment.archived"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunStartedEventData`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.started"`

      - `"deployment_run.started"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentDeletedEventData`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.deleted"`

      - `"deployment.deleted"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunSucceededEventData`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.succeeded"`

      - `"deployment_run.succeeded"`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentCreatedEventData`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.created"`

      - `"environment.created"`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentUpdatedEventData`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.updated"`

      - `"environment.updated"`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentArchivedEventData`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.archived"`

      - `"environment.archived"`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentDeletedEventData`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.deleted"`

      - `"environment.deleted"`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreCreatedEventData`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.created"`

      - `"memory_store.created"`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreArchivedEventData`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.archived"`

      - `"memory_store.archived"`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreDeletedEventData`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.deleted"`

      - `"memory_store.deleted"`

    - `workspace_id: string`

  - `BetaWebhookSessionBudgetReachedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.budget_reached"`

      - `"session.budget_reached"`

    - `workspace_id: string`

### Beta Webhook Memory Store Archived Event Data

- `BetaWebhookMemoryStoreArchivedEventData`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.archived"`

    - `"memory_store.archived"`

  - `workspace_id: string`

### Beta Webhook Memory Store Created Event Data

- `BetaWebhookMemoryStoreCreatedEventData`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.created"`

    - `"memory_store.created"`

  - `workspace_id: string`

### Beta Webhook Memory Store Deleted Event Data

- `BetaWebhookMemoryStoreDeletedEventData`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.deleted"`

    - `"memory_store.deleted"`

  - `workspace_id: string`

### Beta Webhook Session Archived Event Data

- `BetaWebhookSessionArchivedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.archived"`

    - `"session.archived"`

  - `workspace_id: string`

### Beta Webhook Session Budget Reached Event Data

- `BetaWebhookSessionBudgetReachedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.budget_reached"`

    - `"session.budget_reached"`

  - `workspace_id: string`

### Beta Webhook Session Created Event Data

- `BetaWebhookSessionCreatedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.created"`

    - `"session.created"`

  - `workspace_id: string`

### Beta Webhook Session Deleted Event Data

- `BetaWebhookSessionDeletedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.deleted"`

    - `"session.deleted"`

  - `workspace_id: string`

### Beta Webhook Session Idled Event Data

- `BetaWebhookSessionIdledEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.idled"`

    - `"session.idled"`

  - `workspace_id: string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `BetaWebhookSessionOutcomeEvaluationEndedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.outcome_evaluation_ended"`

    - `"session.outcome_evaluation_ended"`

  - `workspace_id: string`

### Beta Webhook Session Pending Event Data

- `BetaWebhookSessionPendingEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.pending"`

    - `"session.pending"`

  - `workspace_id: string`

### Beta Webhook Session Requires Action Event Data

- `BetaWebhookSessionRequiresActionEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.requires_action"`

    - `"session.requires_action"`

  - `workspace_id: string`

### Beta Webhook Session Running Event Data

- `BetaWebhookSessionRunningEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.running"`

    - `"session.running"`

  - `workspace_id: string`

### Beta Webhook Session Status Idled Event Data

- `BetaWebhookSessionStatusIdledEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_idled"`

    - `"session.status_idled"`

  - `workspace_id: string`

### Beta Webhook Session Status Rescheduled Event Data

- `BetaWebhookSessionStatusRescheduledEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_rescheduled"`

    - `"session.status_rescheduled"`

  - `workspace_id: string`

### Beta Webhook Session Status Run Started Event Data

- `BetaWebhookSessionStatusRunStartedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_run_started"`

    - `"session.status_run_started"`

  - `workspace_id: string`

### Beta Webhook Session Status Terminated Event Data

- `BetaWebhookSessionStatusTerminatedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_terminated"`

    - `"session.status_terminated"`

  - `workspace_id: string`

### Beta Webhook Session Thread Created Event Data

- `BetaWebhookSessionThreadCreatedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_created"`

    - `"session.thread_created"`

  - `workspace_id: string`

### Beta Webhook Session Thread Idled Event Data

- `BetaWebhookSessionThreadIdledEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_idled"`

    - `"session.thread_idled"`

  - `workspace_id: string`

### Beta Webhook Session Thread Terminated Event Data

- `BetaWebhookSessionThreadTerminatedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_terminated"`

    - `"session.thread_terminated"`

  - `workspace_id: string`

### Beta Webhook Session Updated Event Data

- `BetaWebhookSessionUpdatedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.updated"`

    - `"session.updated"`

  - `workspace_id: string`

### Beta Webhook Vault Archived Event Data

- `BetaWebhookVaultArchivedEventData`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.archived"`

    - `"vault.archived"`

  - `workspace_id: string`

### Beta Webhook Vault Created Event Data

- `BetaWebhookVaultCreatedEventData`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.created"`

    - `"vault.created"`

  - `workspace_id: string`

### Beta Webhook Vault Credential Archived Event Data

- `BetaWebhookVaultCredentialArchivedEventData`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.archived"`

    - `"vault_credential.archived"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Created Event Data

- `BetaWebhookVaultCredentialCreatedEventData`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.created"`

    - `"vault_credential.created"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Deleted Event Data

- `BetaWebhookVaultCredentialDeletedEventData`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.deleted"`

    - `"vault_credential.deleted"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `BetaWebhookVaultCredentialRefreshFailedEventData`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.refresh_failed"`

    - `"vault_credential.refresh_failed"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Deleted Event Data

- `BetaWebhookVaultDeletedEventData`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.deleted"`

    - `"vault.deleted"`

  - `workspace_id: string`

### Unwrap Webhook Event

- `UnwrapWebhookEvent`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `BetaWebhookSessionCreatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

        - `"session.created"`

      - `workspace_id: string`

    - `BetaWebhookSessionPendingEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

        - `"session.pending"`

      - `workspace_id: string`

    - `BetaWebhookSessionRunningEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

        - `"session.running"`

      - `workspace_id: string`

    - `BetaWebhookSessionIdledEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

        - `"session.idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionRequiresActionEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

        - `"session.requires_action"`

      - `workspace_id: string`

    - `BetaWebhookSessionArchivedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

        - `"session.archived"`

      - `workspace_id: string`

    - `BetaWebhookSessionDeletedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

        - `"session.deleted"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRescheduledEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_rescheduled"`

        - `"session.status_rescheduled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRunStartedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

        - `"session.status_run_started"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusIdledEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

        - `"session.status_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusTerminatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

        - `"session.status_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadCreatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_created"`

        - `"session.thread_created"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadIdledEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_idled"`

        - `"session.thread_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadTerminatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_terminated"`

        - `"session.thread_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `BetaWebhookVaultCreatedEventData`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

        - `"vault.created"`

      - `workspace_id: string`

    - `BetaWebhookVaultArchivedEventData`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

        - `"vault.archived"`

      - `workspace_id: string`

    - `BetaWebhookVaultDeletedEventData`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

        - `"vault.deleted"`

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialCreatedEventData`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

        - `"vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialArchivedEventData`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

        - `"vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialDeletedEventData`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

        - `"vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialRefreshFailedEventData`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.refresh_failed"`

        - `"vault_credential.refresh_failed"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookSessionUpdatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.updated"`

        - `"session.updated"`

      - `workspace_id: string`

    - `BetaWebhookAgentCreatedEventData`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.created"`

        - `"agent.created"`

      - `workspace_id: string`

    - `BetaWebhookAgentArchivedEventData`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.archived"`

        - `"agent.archived"`

      - `workspace_id: string`

    - `BetaWebhookAgentDeletedEventData`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.deleted"`

        - `"agent.deleted"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentPausedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.paused"`

        - `"deployment.paused"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunFailedEventData`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.failed"`

        - `"deployment_run.failed"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentCreatedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.created"`

        - `"deployment.created"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUpdatedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.updated"`

        - `"deployment.updated"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUnpausedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.unpaused"`

        - `"deployment.unpaused"`

      - `workspace_id: string`

    - `BetaWebhookAgentUpdatedEventData`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.updated"`

        - `"agent.updated"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentArchivedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.archived"`

        - `"deployment.archived"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunStartedEventData`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.started"`

        - `"deployment_run.started"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentDeletedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.deleted"`

        - `"deployment.deleted"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunSucceededEventData`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.succeeded"`

        - `"deployment_run.succeeded"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentCreatedEventData`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.created"`

        - `"environment.created"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentUpdatedEventData`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.updated"`

        - `"environment.updated"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentArchivedEventData`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.archived"`

        - `"environment.archived"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentDeletedEventData`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.deleted"`

        - `"environment.deleted"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreCreatedEventData`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.created"`

        - `"memory_store.created"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreArchivedEventData`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.archived"`

        - `"memory_store.archived"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreDeletedEventData`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.deleted"`

        - `"memory_store.deleted"`

      - `workspace_id: string`

    - `BetaWebhookSessionBudgetReachedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.budget_reached"`

        - `"session.budget_reached"`

      - `workspace_id: string`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

    - `"event"`
