<!-- source: https://platform.claude.com/docs/en/api/cli/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/cli/beta -->

<!-- chunk-start -->

      - `beta_managed_agents_static_bearer_auth_response: object`

        Static bearer token credential details for an MCP server.

        - `mcp_server_url: string`

          URL of the MCP server this credential authenticates against.

        - `type: "static_bearer"`

      - `beta_managed_agents_environment_variable_auth_response: object`

        Environment variable credential details. The secret value is never returned.

        - `injection_location: object`

          Where in the outbound request the secret value is substituted.

          - `body: boolean`

            Whether the placeholder is substituted in the request body.

          - `header: boolean`

            Whether the placeholder is substituted in request header values.

        - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

          Outbound hosts the secret value is substituted on.

          - `beta_managed_agents_unrestricted_credential_networking_response: object`

            The secret is substituted on any host the session's Environment network policy permits egress to.

            - `type: "unrestricted"`

          - `beta_managed_agents_limited_credential_networking_response: object`

            The secret is substituted only on requests to the listed hosts.

            - `allowed_hosts: array of string`

              Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

            - `type: "limited"`

        - `secret_name: string`

          Name of the environment variable.

        - `type: "environment_variable"`

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `metadata: map[string]`

      Arbitrary key-value metadata attached to the credential.

    - `type: "vault_credential"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `vault_id: string`

      Identifier of the vault this credential belongs to.

    - `display_name: optional string`

      Human-readable name for the credential.

  - `next_page: optional string`

    Pagination token for the next page, or null if no more results.

#### Example

```bash
ant beta:vaults:credentials list \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
      "archived_at": null,
      "auth": {
        "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
        "type": "static_bearer"
      },
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {
        "environment": "production"
      },
      "type": "vault_credential",
      "updated_at": "2026-03-15T10:00:00Z",
      "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "display_name": "Example credential"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Get Credential

`$ ant beta:vaults:credentials retrieve`

**GET** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

#### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--credential-id: string`

  Path param: Path parameter credential_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_credential: object`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `beta_managed_agents_mcp_oauth_auth_response: object`

      OAuth credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "mcp_oauth"`

      - `expires_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `refresh: optional object`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: string`

          OAuth client ID.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `beta_managed_agents_token_endpoint_auth_none_response: object`

            Token endpoint requires no client authentication.

            - `type: "none"`

          - `beta_managed_agents_token_endpoint_auth_basic_response: object`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

          - `beta_managed_agents_token_endpoint_auth_post_response: object`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `beta_managed_agents_static_bearer_auth_response: object`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "static_bearer"`

    - `beta_managed_agents_environment_variable_auth_response: object`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: object`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `beta_managed_agents_unrestricted_credential_networking_response: object`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

        - `beta_managed_agents_limited_credential_networking_response: object`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: array of string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: "limited"`

      - `secret_name: string`

        Name of the environment variable.

      - `type: "environment_variable"`

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the credential.

  - `type: "vault_credential"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name: optional string`

    Human-readable name for the credential.

#### Example

```bash
ant beta:vaults:credentials retrieve \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

### Update Credential

`$ ant beta:vaults:credentials update`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

#### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--credential-id: string`

  Path param: Path parameter credential_id

- `--auth: optional BetaManagedAgentsMCPOAuthUpdateParams or BetaManagedAgentsStaticBearerUpdateParams or BetaManagedAgentsEnvironmentVariableUpdateParams`

  Body param: Updated authentication details for a credential.

- `--display-name: optional string`

  Body param: Updated human-readable name for the credential. 1-255 characters.

  minLength: 1, maxLength: 255

- `--metadata: optional map[string]`

  Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_credential: object`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `beta_managed_agents_mcp_oauth_auth_response: object`

      OAuth credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "mcp_oauth"`

      - `expires_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `refresh: optional object`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: string`

          OAuth client ID.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `beta_managed_agents_token_endpoint_auth_none_response: object`

            Token endpoint requires no client authentication.

            - `type: "none"`

          - `beta_managed_agents_token_endpoint_auth_basic_response: object`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

          - `beta_managed_agents_token_endpoint_auth_post_response: object`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `beta_managed_agents_static_bearer_auth_response: object`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "static_bearer"`

    - `beta_managed_agents_environment_variable_auth_response: object`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: object`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `beta_managed_agents_unrestricted_credential_networking_response: object`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

        - `beta_managed_agents_limited_credential_networking_response: object`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: array of string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: "limited"`

      - `secret_name: string`

        Name of the environment variable.

      - `type: "environment_variable"`

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the credential.

  - `type: "vault_credential"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name: optional string`

    Human-readable name for the credential.

#### Example

```bash
ant beta:vaults:credentials update \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

### Delete Credential

`$ ant beta:vaults:credentials delete`

**DELETE** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

#### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--credential-id: string`

  Path param: Path parameter credential_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_deleted_credential: object`

  Confirmation of a deleted credential.

  - `id: string`

    Unique identifier of the deleted credential.

  - `type: "vault_credential_deleted"`

#### Example

```bash
ant beta:vaults:credentials delete \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

### Archive Credential

`$ ant beta:vaults:credentials archive`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

#### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--credential-id: string`

  Path param: Path parameter credential_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_credential: object`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `beta_managed_agents_mcp_oauth_auth_response: object`

      OAuth credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "mcp_oauth"`

      - `expires_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `refresh: optional object`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: string`

          OAuth client ID.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `beta_managed_agents_token_endpoint_auth_none_response: object`

            Token endpoint requires no client authentication.

            - `type: "none"`

          - `beta_managed_agents_token_endpoint_auth_basic_response: object`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

          - `beta_managed_agents_token_endpoint_auth_post_response: object`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `beta_managed_agents_static_bearer_auth_response: object`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "static_bearer"`

    - `beta_managed_agents_environment_variable_auth_response: object`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: object`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `beta_managed_agents_unrestricted_credential_networking_response: object`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

        - `beta_managed_agents_limited_credential_networking_response: object`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: array of string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: "limited"`

      - `secret_name: string`

        Name of the environment variable.

      - `type: "environment_variable"`

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the credential.

  - `type: "vault_credential"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name: optional string`

    Human-readable name for the credential.

#### Example

```bash
ant beta:vaults:credentials archive \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

### Validate Credential

`$ ant beta:vaults:credentials mcp-oauth-validate`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

#### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--credential-id: string`

  Path param: Path parameter credential_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_credential_validation: object`

  Result of live-probing a credential against its configured MCP server.

  - `credential_id: string`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: boolean`

    Whether the credential has a refresh token configured.

  - `mcp_probe: object`

    The failing step of an MCP validation probe.

    - `http_response: object`

      An HTTP response captured during a credential validation probe.

      - `body: string`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: boolean`

        Whether `body` was truncated.

      - `content_type: string`

        Value of the `Content-Type` response header.

      - `status_code: number`

        HTTP status code.

        format: int32

    - `method: string`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `refresh: object`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `http_response: object`

      An HTTP response captured during a credential validation probe.

      - `body: string`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: boolean`

        Whether `body` was truncated.

      - `content_type: string`

        Value of the `Content-Type` response header.

      - `status_code: number`

        HTTP status code.

        format: int32

    - `status: "succeeded" or "failed" or "connect_error" or "no_refresh_token"`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `"succeeded"`

      - `"failed"`

      - `"connect_error"`

      - `"no_refresh_token"`

  - `status: "valid" or "invalid" or "unknown"`

    Overall verdict of a credential validation probe.

    - `"valid"`

    - `"invalid"`

    - `"unknown"`

  - `type: "vault_credential_validation"`

  - `validated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: string`

    Identifier of the vault containing the credential.

#### Example

```bash
ant beta:vaults:credentials mcp-oauth-validate \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
```

##### Response (200)

```json
{
  "credential_id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "has_refresh_token": true,
  "mcp_probe": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "method": "method"
  },
  "refresh": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "status": "succeeded"
  },
  "status": "valid",
  "type": "vault_credential_validation",
  "validated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv"
}
```

## Beta › Memory Stores

### Create a memory store

`$ ant beta:memory-stores create`

**POST** `/v1/memory_stores`

Create a memory store

#### Parameters

- `--name: string`

  Body param: Human-readable name for the store. Required; 1–255 characters; no control characters. The mount-path slug under `/mnt/memory/` is derived from this name (lowercased, non-alphanumeric runs collapsed to a hyphen). Names need not be unique within a workspace.

  minLength: 1, maxLength: 255

- `--description: optional string`

  Body param: Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent.

  maxLength: 1024

- `--metadata: optional map[string]`

  Body param: Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Not visible to the agent.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_memory_store: object`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: "memory_store"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `archived_at: optional string`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: optional string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: optional map[string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```bash
ant beta:memory-stores create \
  --api-key my-anthropic-api-key \
  --name x
```

##### Response (200)

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

### List memory stores

`$ ant beta:memory-stores list`

**GET** `/v1/memory_stores`

List memory stores

#### Parameters

- `--created-at-gte: optional string`

  Query param: Return only stores whose `created_at` is at or after this time (inclusive). Sent on the wire as `created_at[gte]`.

  format: date-time

- `--created-at-lte: optional string`

  Query param: Return only stores whose `created_at` is at or before this time (inclusive). Sent on the wire as `created_at[lte]`.

  format: date-time

- `--include-archived: optional boolean`

  Query param: When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

- `--limit: optional number`

  Query param: Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

  format: int32

- `--page: optional string`

  Query param: Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaManagedAgentsListMemoryStoresResponse: object`

  A page of `memory_store` results, ordered by `created_at` descending (newest first).

  - `data: optional array of BetaManagedAgentsMemoryStore`

    Memory stores on this page, newest first. Empty when there are no stores matching the filters.

    - `id: string`

      Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `name: string`

      Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

    - `type: "memory_store"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `archived_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `description: optional string`

      Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

    - `metadata: optional map[string]`

      Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

  - `next_page: optional string`

    Opaque cursor for the next page (a `page_...` value). Pass as `page` on the next request. `null` when there are no more results.

#### Example

```bash
ant beta:memory-stores list \
  --api-key my-anthropic-api-key
```

##### Response (200)

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

### Retrieve a memory store

`$ ant beta:memory-stores retrieve`

**GET** `/v1/memory_stores/{memory_store_id}`

Retrieve a memory store

#### Parameters

- `--memory-store-id: string`

  Path parameter memory_store_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_memory_store: object`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: "memory_store"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `archived_at: optional string`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: optional string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: optional map[string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```bash
ant beta:memory-stores retrieve \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

##### Response (200)

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

### Update a memory store

`$ ant beta:memory-stores update`

**POST** `/v1/memory_stores/{memory_store_id}`

Update a memory store

#### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--description: optional string`

  Body param: New description for the store, up to 1024 characters. Pass an empty string to clear it.

  maxLength: 1024

- `--metadata: optional map[string]`

  Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `--name: optional string`

  Body param: New human-readable name for the store. 1–255 characters; no control characters. Renaming changes the slug used for the store's `mount_path` in sessions created after the update.

  minLength: 1, maxLength: 255

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_memory_store: object`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: "memory_store"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `archived_at: optional string`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: optional string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: optional map[string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```bash
ant beta:memory-stores update \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

##### Response (200)

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

### Delete a memory store

`$ ant beta:memory-stores delete`

**DELETE** `/v1/memory_stores/{memory_store_id}`

Delete a memory store

#### Parameters

- `--memory-store-id: string`

  Path parameter memory_store_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_deleted_memory_store: object`

  Confirmation that a `memory_store` was deleted.

  - `id: string`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `type: "memory_store_deleted"`

#### Example

```bash
ant beta:memory-stores delete \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

##### Response (200)

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

### Archive a memory store

`$ ant beta:memory-stores archive`

**POST** `/v1/memory_stores/{memory_store_id}/archive`

Archive a memory store

#### Parameters

- `--memory-store-id: string`

  Path parameter memory_store_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_memory_store: object`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: "memory_store"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `archived_at: optional string`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: optional string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: optional map[string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```bash
ant beta:memory-stores archive \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

##### Response (200)

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

## Beta › Memory Stores › Memories

### Create a memory

`$ ant beta:memory-stores:memories create`

**POST** `/v1/memory_stores/{memory_store_id}/memories`

Create a memory

#### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--content: string`

  Body param: UTF-8 text content for the new memory. Maximum 100 kB (102,400 bytes). Required; pass `""` explicitly to create an empty memory.

- `--path: string`

  Body param: Hierarchical path for the new memory, e.g. `/projects/foo/notes.md`. Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive.

  minLength: 2, maxLength: 1024

- `--view: optional "basic" or "full"`

  Query param: Query parameter for view

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_memory: object`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: string`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    format: int32

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: "memory"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `content: optional string`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

#### Example

```bash
ant beta:memory-stores:memories create \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --content content \
  --path xx
```

##### Response (200)

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

### List memories

`$ ant beta:memory-stores:memories list`

**GET** `/v1/memory_stores/{memory_store_id}/memories`

List memories

#### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--depth: optional number`

  Query param: `0` (or omitted) returns all descendants below `path_prefix` (recursive). `1` returns immediate children only; deeper entries roll up as `memory_prefix` items. `depth=1` behaves like `ls`; omitting `depth` behaves like `find`.

  format: int32

- `--limit: optional number`

  Query param: Maximum number of items to return per page. Must be between 1 and 100. Defaults to 20 when omitted. Capped at 20 when `view=full`. Both `memory` and `memory_prefix` items count toward the limit.

  format: int32

- `--page: optional string`

  Query param: Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

- `--path-prefix: optional string`

  Query param: Optional path prefix filter. Must end with `/` (segment-aligned), e.g., `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

- `--view: optional "basic" or "full"`

  Query param: Which projection of each `memory` to return. Defaults to `basic` (content omitted). `full` populates `content` on each item and caps `limit` at 20; use this as the bulk-read path for export and sync.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaManagedAgentsListMemoriesResult: object`

  Response payload for [List memories](/docs/en/api/beta/memory_stores/memories/list).

  - `data: optional array of BetaManagedAgentsMemoryListItem`

    One page of results. Each item is either a `memory` object or, when `depth` was set, a `memory_prefix` rollup marker. Items are returned in a stable, server-defined order.

    - `beta_managed_agents_memory: object`

      A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

      - `id: string`

        Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

      - `content_sha256: string`

        Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

      - `content_size_bytes: number`

        Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

        format: int32

      - `created_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `memory_store_id: string`

        ID of the memory store this memory belongs to (a `memstore_...` value).

      - `memory_version_id: string`

        ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

      - `path: string`

        Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

      - `type: "memory"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `content: optional string`

        The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

    - `beta_managed_agents_memory_prefix: object`

      A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

      - `path: string`

        The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

      - `type: "memory_prefix"`

  - `next_page: optional string`

    Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.

#### Example

```bash
ant beta:memory-stores:memories list \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

##### Response (200)

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

### Retrieve a memory

`$ ant beta:memory-stores:memories retrieve`

**GET** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a memory

#### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--memory-id: string`

  Path param: Path parameter memory_id

- `--view: optional "basic" or "full"`

  Query param: Query parameter for view

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_memory: object`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: string`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    format: int32

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: "memory"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `content: optional string`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

#### Example

```bash
ant beta:memory-stores:memories retrieve \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-id memory_id
```

##### Response (200)

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

### Update a memory

`$ ant beta:memory-stores:memories update`

**POST** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a memory

#### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--memory-id: string`

  Path param: Path parameter memory_id

- `--view: optional "basic" or "full"`

  Query param: Query parameter for view

- `--content: optional string`

  Body param: New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

- `--path: optional string`

  Body param: New path for the memory (a rename). Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive. The memory's `id` is preserved across renames. Omit to leave the path unchanged.

  minLength: 2, maxLength: 1024

- `--precondition: optional object`

  Body param: Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_memory: object`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: string`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    format: int32

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: "memory"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `content: optional string`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

#### Example

```bash
ant beta:memory-stores:memories update \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-id memory_id
```

##### Response (200)

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

### Delete a memory

`$ ant beta:memory-stores:memories delete`

**DELETE** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

#### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--memory-id: string`

  Path param: Path parameter memory_id

- `--expected-content-sha256: optional string`

  Query param: Query parameter for expected_content_sha256

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_deleted_memory: object`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). Deleting a memory does not erase its version history: its versions remain listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) while they are retained (each version is kept for at least the version retention period after it was written, unless the store itself is deleted).

  - `id: string`

    ID of the deleted memory (a `mem_...` value).

  - `type: "memory_deleted"`

#### Example

```bash
ant beta:memory-stores:memories delete \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-id memory_id
```

##### Response (200)

```json
{
  "id": "id",
  "type": "memory_deleted"
}
```

## Beta › Memory Stores › Memory Versions

### List memory versions

`$ ant beta:memory-stores:memory-versions list`

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

#### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--api-key-id: optional string`

  Query param: Query parameter for api_key_id

- `--created-at-gte: optional string`

  Query param: Return versions created at or after this time (inclusive).

  format: date-time

- `--created-at-lte: optional string`

  Query param: Return versions created at or before this time (inclusive).

  format: date-time

- `--limit: optional number`

  Query param: Query parameter for limit

  format: int32

- `--memory-id: optional string`

  Query param: Query parameter for memory_id

- `--operation: optional "created" or "modified" or "deleted"`

  Query param: Query parameter for operation

- `--page: optional string`

  Query param: Query parameter for page

- `--service-account-id: optional string`

  Query param: Query parameter for service_account_id

- `--session-id: optional string`

  Query param: Query parameter for session_id

- `--view: optional "basic" or "full"`

  Query param: Query parameter for view

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaManagedAgentsListMemoryVersionsResult: object`

  Response payload for [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `data: optional array of BetaManagedAgentsMemoryVersion`

    One page of `memory_version` objects, ordered by `created_at` descending (newest first), with `id` as tiebreak.

    - `id: string`

      Unique identifier for this version (a `memver_...` value).

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `memory_id: string`

      ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the memory's retained versions, including the `deleted` row while the lineage is retained.

    - `memory_store_id: string`

      ID of the memory store this version belongs to (a `memstore_...` value).

    - `operation: "created" or "modified" or "deleted"`

      The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

      - `"created"`

      - `"modified"`

      - `"deleted"`

    - `type: "memory_version"`

    - `content: optional string`

      The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

    - `content_sha256: optional string`

      Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    - `content_size_bytes: optional number`

      Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

      format: int32

    - `created_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor or BetaManagedAgentsServiceAccountActor`

      Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

      - `beta_managed_agents_session_actor: object`

        Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

        - `session_id: string`

          ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

          minLength: 1

        - `type: "session_actor"`

      - `beta_managed_agents_api_actor: object`

        Attribution for a write made directly via the public API (outside of any session).

        - `api_key_id: string`

          ID of the API key that performed the write. This identifies the key, not the secret.

          minLength: 1

        - `type: "api_actor"`

      - `beta_managed_agents_user_actor: object`

        Attribution for a write made by a human user through the Anthropic Console.

        - `type: "user_actor"`

        - `user_id: string`

          ID of the user who performed the write (a `user_...` value).

          minLength: 1

      - `beta_managed_agents_service_account_actor: object`

        Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

        - `service_account_id: string`

          ID of the service account that performed the write (a `svac_...` value).

          minLength: 1

        - `type: "service_account_actor"`

    - `path: optional string`

      The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

    - `redacted_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `redacted_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor or BetaManagedAgentsServiceAccountActor`

      Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

      - `beta_managed_agents_session_actor: object`

        Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `beta_managed_agents_api_actor: object`

        Attribution for a write made directly via the public API (outside of any session).

      - `beta_managed_agents_user_actor: object`

        Attribution for a write made by a human user through the Anthropic Console.

      - `beta_managed_agents_service_account_actor: object`

        Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

  - `next_page: optional string`

    Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.

#### Example

```bash
ant beta:memory-stores:memory-versions list \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

##### Response (200)

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

### Retrieve a memory version

`$ ant beta:memory-stores:memory-versions retrieve`

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

#### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--memory-version-id: string`

  Path param: Path parameter memory_version_id

- `--view: optional "basic" or "full"`

  Query param: Query parameter for view

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_memory_version: object`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and are not deleted with the memory; each version is retained for at least the version retention period after it was written, unless the store itself is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: string`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `memory_id: string`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the memory's retained versions, including the `deleted` row while the lineage is retained.

  - `memory_store_id: string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: "created" or "modified" or "deleted"`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

  - `content: optional string`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: optional string`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: optional number`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `created_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor or BetaManagedAgentsServiceAccountActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `beta_managed_agents_session_actor: object`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

        minLength: 1

      - `type: "session_actor"`

    - `beta_managed_agents_api_actor: object`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: string`

        ID of the API key that performed the write. This identifies the key, not the secret.

        minLength: 1

      - `type: "api_actor"`

    - `beta_managed_agents_user_actor: object`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: "user_actor"`

      - `user_id: string`

        ID of the user who performed the write (a `user_...` value).

        minLength: 1

    - `beta_managed_agents_service_account_actor: object`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `service_account_id: string`

        ID of the service account that performed the write (a `svac_...` value).

        minLength: 1

      - `type: "service_account_actor"`

  - `path: optional string`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

    format: date-time

  - `redacted_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor or BetaManagedAgentsServiceAccountActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `beta_managed_agents_session_actor: object`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

    - `beta_managed_agents_api_actor: object`

      Attribution for a write made directly via the public API (outside of any session).

    - `beta_managed_agents_user_actor: object`

      Attribution for a write made by a human user through the Anthropic Console.

    - `beta_managed_agents_service_account_actor: object`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

#### Example

```bash
ant beta:memory-stores:memory-versions retrieve \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-version-id memory_version_id
```

##### Response (200)

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

### Redact a memory version

`$ ant beta:memory-stores:memory-versions redact`

**POST** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a memory version

#### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--memory-version-id: string`

  Path param: Path parameter memory_version_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_memory_version: object`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and are not deleted with the memory; each version is retained for at least the version retention period after it was written, unless the store itself is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: string`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `memory_id: string`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the memory's retained versions, including the `deleted` row while the lineage is retained.

  - `memory_store_id: string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: "created" or "modified" or "deleted"`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

  - `content: optional string`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: optional string`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: optional number`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `created_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor or BetaManagedAgentsServiceAccountActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `beta_managed_agents_session_actor: object`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

        minLength: 1

      - `type: "session_actor"`

    - `beta_managed_agents_api_actor: object`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: string`

        ID of the API key that performed the write. This identifies the key, not the secret.

        minLength: 1

      - `type: "api_actor"`

    - `beta_managed_agents_user_actor: object`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: "user_actor"`

      - `user_id: string`

        ID of the user who performed the write (a `user_...` value).

        minLength: 1

    - `beta_managed_agents_service_account_actor: object`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `service_account_id: string`

        ID of the service account that performed the write (a `svac_...` value).

        minLength: 1

      - `type: "service_account_actor"`

  - `path: optional string`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

    format: date-time

  - `redacted_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor or BetaManagedAgentsServiceAccountActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `beta_managed_agents_session_actor: object`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

    - `beta_managed_agents_api_actor: object`

      Attribution for a write made directly via the public API (outside of any session).

    - `beta_managed_agents_user_actor: object`

      Attribution for a write made by a human user through the Anthropic Console.

    - `beta_managed_agents_service_account_actor: object`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

#### Example

```bash
ant beta:memory-stores:memory-versions redact \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-version-id memory_version_id
```

##### Response (200)

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

## Beta › Files

### Upload File

`$ ant beta:files upload`

**POST** `/v1/files`

Upload File

#### Parameters

- `--file: string`

  Body param: The file to upload

  format: binary

- `--expires-in-seconds: optional number`

  Body param: Seconds from upload until the file expires and its bytes become permanently unavailable. Must be between 3600 (one hour) and 7776000 (ninety days).

  minimum: 3600, maximum: 7776000

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_file_metadata: object`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: string`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `filename: string`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `mime_type: string`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `size_bytes: number`

    Size of the file in bytes.

    minimum: 0

  - `type: "file"`

    Object type.

    For files, this is always `"file"`.

  - `downloadable: optional boolean`

    Whether the file can be downloaded.

  - `expires_at: optional string`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `scope: optional object`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

#### Example

```bash
ant beta:files upload \
  --api-key my-anthropic-api-key \
  --file 'Example data'
```

##### Response (200)

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "expires_at": "2025-05-15T18:37:24.100435Z",
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

### List Files

`$ ant beta:files list`

**GET** `/v1/files`

List Files

#### Parameters

- `--id: optional array of string`

  Query param: Restrict the result set to Files whose `id` is in this list. At most 100 entries (after de-duplication). Mutually exclusive with `page` and `limit`. When supplied, the response is always a single page (`next_page` is null). IDs that do not resolve to a visible File — including deleted Files — are silently omitted.

- `--limit: optional number`

  Query param: Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  maximum: 1000, minimum: 1

- `--page: optional string`

  Query param: Opaque page cursor returned in a prior list response's `next_page`. Prefixed `page_`.

- `--scope-id: optional string`

  Query param: Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaFileListResponse: object`

  - `data: array of BetaFileMetadata`

    List of file metadata objects.

    - `id: string`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `created_at: string`

      RFC 3339 datetime string representing when the file was created.

      format: date-time

    - `filename: string`

      Original filename of the uploaded file.

      maxLength: 500, minLength: 1

    - `mime_type: string`

      MIME type of the file.

      maxLength: 255, minLength: 1

    - `size_bytes: number`

      Size of the file in bytes.

      minimum: 0

    - `type: "file"`

      Object type.

      For files, this is always `"file"`.

    - `downloadable: optional boolean`

      Whether the file can be downloaded.

    - `expires_at: optional string`

      RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

      format: date-time

    - `scope: optional object`

      The scope of this file, indicating the context in which it was created (e.g., a session).

      - `id: string`

        The ID of the scoping resource (e.g., the session ID).

      - `type: "session"`

        The type of scope (e.g., `"session"`).

  - `next_page: optional string`

    Opaque cursor for the next page. Supply as `?page=` to fetch the next page; null when there are no more results.

#### Example

```bash
ant beta:files list \
  --api-key my-anthropic-api-key
```

##### Response (200)

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
      "expires_at": "2025-05-15T18:37:24.100435Z",
      "scope": {
        "id": "id",
        "type": "session"
      }
    }
  ],
  "next_page": "next_page"
}
```

### Download File

`$ ant beta:files download`

**GET** `/v1/files/{file_id}/content`

Download File

#### Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `unnamed_schema_1: file path`

#### Example

```bash
ant beta:files download \
  --api-key my-anthropic-api-key \
  --file-id file_id
```

### Get File Metadata

`$ ant beta:files retrieve-metadata`

**GET** `/v1/files/{file_id}`

Get File Metadata

#### Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_file_metadata: object`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: string`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `filename: string`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `mime_type: string`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `size_bytes: number`

    Size of the file in bytes.

    minimum: 0

  - `type: "file"`

    Object type.

    For files, this is always `"file"`.

  - `downloadable: optional boolean`

    Whether the file can be downloaded.

  - `expires_at: optional string`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `scope: optional object`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

#### Example

```bash
ant beta:files retrieve-metadata \
  --api-key my-anthropic-api-key \
  --file-id file_id
```

##### Response (200)

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "expires_at": "2025-05-15T18:37:24.100435Z",
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

### Delete File

`$ ant beta:files delete`

**DELETE** `/v1/files/{file_id}`

Delete File

#### Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_deleted_file: object`

  - `id: string`

    ID of the deleted file.

  - `type: optional "file_deleted"`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

#### Example

```bash
ant beta:files delete \
  --api-key my-anthropic-api-key \
  --file-id file_id
```

##### Response (200)

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```

## Beta › Skills

### Create Skill

`$ ant beta:skills create`

**POST** `/v1/skills`

Create Skill

#### Parameters

- `--file: array of string`

  Body param: Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `--display-name: optional string`

  Body param: Human-readable, single-line label for the Skill. Maximum 255 characters.
  Always set: derived from the SKILL.md frontmatter `name` when omitted at
  creation. Not unique.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_skill: object`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

    format: date-time

  - `display_name: string`

    Human-readable, single-line label for the Skill. Maximum 255 characters.
    Always set: derived from the SKILL.md frontmatter `name` when omitted at
    creation. Not unique.

  - `latest_version_id: string`

    ID of the newest Skill Version — what `latest` references resolve to. Always set: a Skill holds at least one version.

  - `source: object`

    Where the Skill comes from.

    Possible values:

    * `"custom"`: authored by the platform user; private to their workspace
    * `"anthropic"`: published by Anthropic; shared and read-only
    * `"anthropic_example"`: Anthropic-published sample Skill
    * `"plugin"`: resolved from an installed plugin

    - `type: "custom" or "anthropic" or "anthropic_example" or "plugin"`

      Where the Skill comes from.

      Possible values:

      * `"custom"`: authored by the platform user; private to their workspace
      * `"anthropic"`: published by Anthropic; shared and read-only
      * `"anthropic_example"`: Anthropic-published sample Skill
      * `"plugin"`: resolved from an installed plugin

      - `"custom"`

      - `"anthropic"`

      - `"anthropic_example"`

      - `"plugin"`

  - `type: "skill"`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: string`

    ISO 8601 timestamp of when the skill was last updated.

    format: date-time

#### Example

```bash
ant beta:skills create \
  --api-key my-anthropic-api-key \
  --file 'Example data'
```

##### Response (200)

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "display_name",
  "latest_version_id": "latest_version_id",
  "source": {
    "type": "custom"
  },
  "type": "skill",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### List Skills

`$ ant beta:skills list`

**GET** `/v1/skills`

List Skills

#### Parameters

- `--limit: optional number`

  Query param: Number of results to return per page.

  Ranges from `1` to `1000`. Defaults to `20`.

  minimum: 1, maximum: 1000

- `--page: optional string`

  Query param: Pagination token for fetching a specific page of results.

  Pass the value from a previous response's `next_page` field to get the next page of results.

- `--source: optional string`

  Query param: Filter skills by source.

  If provided, only skills from the specified source will be returned:

  * `"custom"`: only return user-created skills
  * `"anthropic"`: only return Anthropic-created skills

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaListSkillsResponse: object`

  - `data: array of BetaSkill`

    List of skills.

    - `id: string`

      Unique identifier for the skill.

      The format and length of IDs may change over time.

    - `created_at: string`

      ISO 8601 timestamp of when the skill was created.

      format: date-time

    - `display_name: string`

      Human-readable, single-line label for the Skill. Maximum 255 characters.
      Always set: derived from the SKILL.md frontmatter `name` when omitted at
      creation. Not unique.

    - `latest_version_id: string`

      ID of the newest Skill Version — what `latest` references resolve to. Always set: a Skill holds at least one version.

    - `source: object`

      Where the Skill comes from.

      Possible values:

      * `"custom"`: authored by the platform user; private to their workspace
      * `"anthropic"`: published by Anthropic; shared and read-only
      * `"anthropic_example"`: Anthropic-published sample Skill
      * `"plugin"`: resolved from an installed plugin

      - `type: "custom" or "anthropic" or "anthropic_example" or "plugin"`

        Where the Skill comes from.

        Possible values:

        * `"custom"`: authored by the platform user; private to their workspace
        * `"anthropic"`: published by Anthropic; shared and read-only
        * `"anthropic_example"`: Anthropic-published sample Skill
        * `"plugin"`: resolved from an installed plugin

        - `"custom"`

        - `"anthropic"`

        - `"anthropic_example"`

        - `"plugin"`

    - `type: "skill"`

      Object type.

      For Skills, this is always `"skill"`.

    - `updated_at: string`

      ISO 8601 timestamp of when the skill was last updated.

      format: date-time

  - `next_page: string`

    Token for fetching the next page of results.

    If `null`, there are no more results available. Pass this value to the `page` parameter in the next request to get the next page.

#### Example

```bash
ant beta:skills list \
  --api-key my-anthropic-api-key
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "skill_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "display_name",
      "latest_version_id": "latest_version_id",
      "source": {
        "type": "custom"
      },
      "type": "skill",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "next_page": "next_page"
}
```

### Get Skill

`$ ant beta:skills retrieve`

**GET** `/v1/skills/{skill_id}`

Get Skill

#### Parameters

- `--skill-id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_skill: object`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

    format: date-time

  - `display_name: string`

    Human-readable, single-line label for the Skill. Maximum 255 characters.
    Always set: derived from the SKILL.md frontmatter `name` when omitted at
    creation. Not unique.

  - `latest_version_id: string`

    ID of the newest Skill Version — what `latest` references resolve to. Always set: a Skill holds at least one version.

  - `source: object`

    Where the Skill comes from.

    Possible values:

    * `"custom"`: authored by the platform user; private to their workspace
    * `"anthropic"`: published by Anthropic; shared and read-only
    * `"anthropic_example"`: Anthropic-published sample Skill
    * `"plugin"`: resolved from an installed plugin

    - `type: "custom" or "anthropic" or "anthropic_example" or "plugin"`

      Where the Skill comes from.

      Possible values:

      * `"custom"`: authored by the platform user; private to their workspace
      * `"anthropic"`: published by Anthropic; shared and read-only
      * `"anthropic_example"`: Anthropic-published sample Skill
      * `"plugin"`: resolved from an installed plugin

      - `"custom"`

      - `"anthropic"`

      - `"anthropic_example"`

      - `"plugin"`

  - `type: "skill"`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: string`

    ISO 8601 timestamp of when the skill was last updated.

    format: date-time

#### Example

```bash
ant beta:skills retrieve \
  --api-key my-anthropic-api-key \
  --skill-id skill_id
```

##### Response (200)

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "display_name",
  "latest_version_id": "latest_version_id",
  "source": {
    "type": "custom"
  },
  "type": "skill",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### Delete Skill

`$ ant beta:skills delete`

**DELETE** `/v1/skills/{skill_id}`

Delete Skill

#### Parameters

- `--skill-id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_deleted_skill: object`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `type: "skill_deleted"`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

#### Example

```bash
ant beta:skills delete \
  --api-key my-anthropic-api-key \
  --skill-id skill_id
```

##### Response (200)

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "skill_deleted"
}
```

## Beta › Skills › Versions

### Create Skill Version

`$ ant beta:skills:versions create`

**POST** `/v1/skills/{skill_id}/versions`

Create Skill Version

#### Parameters

- `--skill-id: string`

  Path param: Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--file: array of string`

  Body param: Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_skill_version: object`

  - `id: string`

    Unique identifier for this Skill Version. The id addresses the version in
    paths and pins it in references.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

    format: date-time

  - `description: string`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `name: string`

    The Skill's immutable kebab-case slug, set at creation from the first
    upload's SKILL.md frontmatter `name` (or its enclosing directory). Every
    later upload must resolve to the same value. Also the top-level directory
    of the Skill's mounted files and the base name of a downloaded archive.

  - `skill_id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `type: "skill_version"`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

#### Example

```bash
ant beta:skills:versions create \
  --api-key my-anthropic-api-key \
  --skill-id skill_id \
  --file 'Example data'
```

##### Response (200)

```json
{
  "id": "id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "description",
  "name": "name",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "skill_version"
}
```

### List Skill Versions

`$ ant beta:skills:versions list`

**GET** `/v1/skills/{skill_id}/versions`

List Skill Versions

#### Parameters

- `--skill-id: string`

  Path param: Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--limit: optional number`

  Query param: Number of results to return per page.

  Ranges from `1` to `1000`. Defaults to `20`.

  minimum: 1, maximum: 1000

- `--page: optional string`

  Query param: Optionally set to the `next_page` token from the previous response.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaListSkillVersionsResponse: object`

  - `data: array of BetaSkillVersion`

    List of skills.

    - `id: string`

      Unique identifier for this Skill Version. The id addresses the version in
      paths and pins it in references.

    - `created_at: string`

      ISO 8601 timestamp of when the skill was created.

      format: date-time

    - `description: string`

      Description of the skill version.

      This is extracted from the SKILL.md file in the skill upload.

    - `name: string`

      The Skill's immutable kebab-case slug, set at creation from the first
      upload's SKILL.md frontmatter `name` (or its enclosing directory). Every
      later upload must resolve to the same value. Also the top-level directory
      of the Skill's mounted files and the base name of a downloaded archive.

    - `skill_id: string`

      Unique identifier for the skill.

      The format and length of IDs may change over time.

    - `type: "skill_version"`

      Object type.

      For Skill Versions, this is always `"skill_version"`.

  - `next_page: string`

    Token for fetching the next page of results.

    If `null`, there are no more results available. Pass this value to the `page` parameter in the next request to get the next page.

#### Example

```bash
ant beta:skills:versions list \
  --api-key my-anthropic-api-key \
  --skill-id skill_id
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "description",
      "name": "name",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "skill_version"
    }
  ],
  "next_page": "next_page"
}
```

### Download Skill Version Content

`$ ant beta:skills:versions download`

**GET** `/v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

#### Parameters

- `--skill-id: string`

  Path param: Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--version: string`

  Path param: Identifies the skill version by its version ID.

  Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `unnamed_schema_2: file path`

#### Example

```bash
ant beta:skills:versions download \
  --api-key my-anthropic-api-key \
  --skill-id skill_id \
  --version version
```

### Get Skill Version

`$ ant beta:skills:versions retrieve`

**GET** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

#### Parameters

- `--skill-id: string`

  Path param: Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--version: string`

  Path param: Identifies the skill version: a version ID, or the literal `latest` for the skill's most recent version.

  Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_skill_version: object`

  - `id: string`

    Unique identifier for this Skill Version. The id addresses the version in
    paths and pins it in references.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

    format: date-time

  - `description: string`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `name: string`

    The Skill's immutable kebab-case slug, set at creation from the first
    upload's SKILL.md frontmatter `name` (or its enclosing directory). Every
    later upload must resolve to the same value. Also the top-level directory
    of the Skill's mounted files and the base name of a downloaded archive.

  - `skill_id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `type: "skill_version"`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

#### Example

```bash
ant beta:skills:versions retrieve \
  --api-key my-anthropic-api-key \
  --skill-id skill_id \
  --version version
```

##### Response (200)

```json
{
  "id": "id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "description",
  "name": "name",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "skill_version"
}
```

### Delete Skill Version

`$ ant beta:skills:versions delete`

**DELETE** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

#### Parameters

- `--skill-id: string`

  Path param: Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--version: string`

  Path param: Identifies the skill version by its version ID.

  Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_deleted_skill_version: object`

  - `id: string`

    Unique identifier for this Skill Version. The id addresses the version in
    paths and pins it in references.

  - `type: "skill_version_deleted"`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

#### Example

```bash
ant beta:skills:versions delete \
  --api-key my-anthropic-api-key \
  --skill-id skill_id \
  --version version
```

##### Response (200)

```json
{
  "id": "id",
  "type": "skill_version_deleted"
}
```

## Beta › User Profiles

### Create User Profile

`$ ant beta:user-profiles create`

**POST** `/v1/user_profiles`

Create User Profile

#### Parameters

- `--access-type: optional "application" or "passthrough"`

  Body param: How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

- `--external-id: optional string`

  Body param: Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

  minLength: 1, maxLength: 255

- `--metadata: optional map[string]`

  Body param: Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

- `--name: optional string`

  Body param: Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a resold-to company (`relationship` `resold` / `access_type` `passthrough`), that company's name where known. Maximum 255 characters.

  minLength: 1, maxLength: 255

- `--relationship: optional "external" or "resold" or "internal"`

  Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_user_profile: object`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: map[BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" or "pending" or "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `access_type: optional "application" or "passthrough"`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id: optional string`

    Platform's own identifier for this user. Not enforced unique.

  - `name: optional string`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: optional "external" or "resold" or "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

#### Example

```bash
ant beta:user-profiles create \
  --api-key my-anthropic-api-key
```

##### Response (200)

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

### List User Profiles

`$ ant beta:user-profiles list`

**GET** `/v1/user_profiles`

List User Profiles

#### Parameters

- `--limit: optional number`

  Query param: Query parameter for limit

  format: int32

- `--order: optional "asc" or "desc"`

  Query param: Query parameter for order

- `--page: optional string`

  Query param: Query parameter for page

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaListUserProfilesResponse: object`

  - `data: array of BetaUserProfile`

    User profiles on this page.

    - `id: string`

      Unique identifier for this user profile, prefixed `uprof_`.

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `metadata: map[string]`

      Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

    - `trust_grants: map[BetaUserProfileTrustGrant]`

      Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

      - `status: "active" or "pending" or "rejected"`

        Status of the trust grant.

        - `"active"`

        - `"pending"`

        - `"rejected"`

    - `type: "user_profile"`

      Object type. Always `user_profile`.

    - `updated_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `access_type: optional "application" or "passthrough"`

      How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

      - `"application"`

      - `"passthrough"`

    - `external_id: optional string`

      Platform's own identifier for this user. Not enforced unique.

    - `name: optional string`

      Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

    - `relationship: optional "external" or "resold" or "internal"`

      How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

      - `"external"`

      - `"resold"`

      - `"internal"`

  - `next_page: string`

    Cursor for the next page, or `null` when there are no more results.

#### Example

```bash
ant beta:user-profiles list \
  --api-key my-anthropic-api-key
```

##### Response (200)

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

### Get User Profile

`$ ant beta:user-profiles retrieve`

**GET** `/v1/user_profiles/{user_profile_id}`

Get User Profile

#### Parameters

- `--user-profile-id: string`

  Path parameter user_profile_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_user_profile: object`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: map[BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" or "pending" or "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `access_type: optional "application" or "passthrough"`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id: optional string`

    Platform's own identifier for this user. Not enforced unique.

  - `name: optional string`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: optional "external" or "resold" or "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

#### Example

```bash
ant beta:user-profiles retrieve \
  --api-key my-anthropic-api-key \
  --user-profile-id uprof_011CZkZCu8hGbp5mYRQgUmz9
```

##### Response (200)

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

### Update User Profile

`$ ant beta:user-profiles update`

**POST** `/v1/user_profiles/{user_profile_id}`

Update User Profile

#### Parameters

- `--user-profile-id: string`

  Path param: Path parameter user_profile_id

- `--access-type: optional "application" or "passthrough"`

  Body param: How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

- `--external-id: optional string`

  Body param: If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

  minLength: 1, maxLength: 255

- `--metadata: optional map[string]`

  Body param: Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

- `--name: optional string`

  Body param: If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

  minLength: 1, maxLength: 255

- `--relationship: optional "external" or "resold" or "internal"`

  Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_user_profile: object`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: map[BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" or "pending" or "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `access_type: optional "application" or "passthrough"`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id: optional string`

    Platform's own identifier for this user. Not enforced unique.

  - `name: optional string`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: optional "external" or "resold" or "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

#### Example

```bash
ant beta:user-profiles update \
  --api-key my-anthropic-api-key \
  --user-profile-id uprof_011CZkZCu8hGbp5mYRQgUmz9
```

##### Response (200)

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

### Create Enrollment URL

`$ ant beta:user-profiles create-enrollment-url`

**POST** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

#### Parameters

- `--user-profile-id: string`

  Path parameter user_profile_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_user_profile_enrollment_url: object`

  - `expires_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "enrollment_url"`

    Object type. Always `enrollment_url`.

  - `url: string`

    Enrollment URL to send to the end user. Valid until `expires_at`.

#### Example

```bash
ant beta:user-profiles create-enrollment-url \
  --api-key my-anthropic-api-key \
  --user-profile-id uprof_011CZkZCu8hGbp5mYRQgUmz9
```

##### Response (200)

```json
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```

## Beta › Dreams

### Create a Dream

`$ ant beta:dreams create`

**POST** `/v1/dreams`

Create a Dream

#### Parameters

- `--input: array of BetaDreamInput`

  Body param

- `--model: string or BetaDreamModelConfigParam`

  Body param: Model identifier and configuration applied to every pipeline stage.

- `--instructions: optional string`

  Body param

  minLength: 1, maxLength: 4096

- `--output-behavior: optional BetaOutputBehaviorCreateNew or BetaOutputBehaviorUpdateExisting`

  Body param: The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_dream: object`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `ended_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `error: object`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `beta_dream_memory_store_input: object`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "memory_store"`

    - `beta_dream_sessions_input: object`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

  - `instructions: string`

  - `model: object`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehaviorCreateNew or BetaOutputBehaviorUpdateExisting`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `beta_output_behavior_create_new: object`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: "create_new"`

    - `beta_output_behavior_update_existing: object`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "update_existing"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

  - `session_id: string`

  - `status: "pending" or "running" or "completed" or 2 more`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

  - `usage: object`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

```bash
ant beta:dreams create \
  --api-key my-anthropic-api-key \
  --input '{memory_store_id: x, type: memory_store}' \
  --model string
```

##### Response (200)

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

### List Dreams

`$ ant beta:dreams list`

**GET** `/v1/dreams`

List Dreams

#### Parameters

- `--created-at-gt: optional string`

  Query param: Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

  format: date-time

- `--created-at-lt: optional string`

  Query param: Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

  format: date-time

- `--include-archived: optional boolean`

  Query param: Query parameter for include_archived

- `--limit: optional number`

  Query param: Query parameter for limit

  format: int32

- `--page: optional string`

  Query param: Query parameter for page

- `--status: optional array of BetaDreamStatus`

  Query param: Filter by lifecycle status. Repeat the parameter to match any of multiple statuses. Empty applies no status filter.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaListDreamsResponse: object`

  - `data: array of BetaDream`

    - `id: string`

    - `archived_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `ended_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `error: object`

      Failure detail for a Dream whose `status` is `failed`.

      - `message: string`

      - `type: string`

    - `inputs: array of BetaDreamInput`

      - `beta_dream_memory_store_input: object`

        An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

        - `memory_store_id: string`

          minLength: 1

        - `type: "memory_store"`

      - `beta_dream_sessions_input: object`

        Input session transcripts the dream reads.

        - `session_ids: array of string`

        - `type: "sessions"`

    - `instructions: string`

    - `model: object`

      Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

      - `id: string`

        Model identifier, e.g. "claude-opus-5". 1-256 characters.

        minLength: 1, maxLength: 256

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `output_behavior: BetaOutputBehaviorCreateNew or BetaOutputBehaviorUpdateExisting`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `beta_output_behavior_create_new: object`

        The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

        - `type: "create_new"`

      - `beta_output_behavior_update_existing: object`

        The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

        - `memory_store_id: string`

          minLength: 1

        - `type: "update_existing"`

    - `outputs: array of BetaDreamOutput`

      - `memory_store_id: string`

      - `type: "memory_store"`

    - `session_id: string`

    - `status: "pending" or "running" or "completed" or 2 more`

      Lifecycle status of a Dream.

      - `"pending"`

      - `"running"`

      - `"completed"`

      - `"failed"`

      - `"canceled"`

    - `type: "dream"`

    - `usage: object`

      Cumulative token usage for the dream across every pipeline stage.

      - `cache_creation_input_tokens: number`

        Total tokens used to create prompt-cache entries (sum of all TTL tiers).

        format: int32

      - `cache_read_input_tokens: number`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: number`

        Total uncached input tokens consumed across every pipeline stage.

        format: int32

      - `output_tokens: number`

        Total output tokens generated across every pipeline stage.

        format: int32

  - `next_page: string`

#### Example

```bash
ant beta:dreams list \
  --api-key my-anthropic-api-key
```

##### Response (200)

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

### Get a Dream

`$ ant beta:dreams retrieve`

**GET** `/v1/dreams/{dream_id}`

Get a Dream

#### Parameters

- `--dream-id: string`

  Path parameter dream_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_dream: object`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `ended_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `error: object`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `beta_dream_memory_store_input: object`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "memory_store"`

    - `beta_dream_sessions_input: object`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

  - `instructions: string`

  - `model: object`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehaviorCreateNew or BetaOutputBehaviorUpdateExisting`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `beta_output_behavior_create_new: object`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: "create_new"`

    - `beta_output_behavior_update_existing: object`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "update_existing"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

  - `session_id: string`

  - `status: "pending" or "running" or "completed" or 2 more`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

  - `usage: object`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

```bash
ant beta:dreams retrieve \
  --api-key my-anthropic-api-key \
  --dream-id dream_id
```

##### Response (200)

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

### Cancel a Dream

`$ ant beta:dreams cancel`

**POST** `/v1/dreams/{dream_id}/cancel`

Cancel a Dream

#### Parameters

- `--dream-id: string`

  Path parameter dream_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_dream: object`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `ended_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `error: object`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `beta_dream_memory_store_input: object`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "memory_store"`

    - `beta_dream_sessions_input: object`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

  - `instructions: string`

  - `model: object`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehaviorCreateNew or BetaOutputBehaviorUpdateExisting`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `beta_output_behavior_create_new: object`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: "create_new"`

    - `beta_output_behavior_update_existing: object`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "update_existing"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

  - `session_id: string`

  - `status: "pending" or "running" or "completed" or 2 more`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

  - `usage: object`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

```bash
ant beta:dreams cancel \
  --api-key my-anthropic-api-key \
  --dream-id dream_id
```

##### Response (200)

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

### Archive a Dream

`$ ant beta:dreams archive`

**POST** `/v1/dreams/{dream_id}/archive`

Archive a Dream

#### Parameters

- `--dream-id: string`

  Path parameter dream_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_dream: object`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `ended_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `error: object`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `beta_dream_memory_store_input: object`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "memory_store"`

    - `beta_dream_sessions_input: object`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

  - `instructions: string`

  - `model: object`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehaviorCreateNew or BetaOutputBehaviorUpdateExisting`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `beta_output_behavior_create_new: object`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: "create_new"`

    - `beta_output_behavior_update_existing: object`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "update_existing"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

  - `session_id: string`

  - `status: "pending" or "running" or "completed" or 2 more`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

  - `usage: object`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

```bash
ant beta:dreams archive \
  --api-key my-anthropic-api-key \
  --dream-id dream_id
```

##### Response (200)

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

## Beta › Tunnels

### Create Tunnel

`$ ant beta:tunnels create`

**POST** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

#### Parameters

- `--display-name: optional string`

  Body param: Optional human-readable name for the tunnel (1-255 characters).

  minLength: 1, maxLength: 255

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_tunnel: object`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

#### Example

```bash
ant beta:tunnels create \
  --api-key my-anthropic-api-key
```

##### Response (200)

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

### Get Tunnel

`$ ant beta:tunnels retrieve`

**GET** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

#### Parameters

- `--tunnel-id: string`

  Path parameter tunnel_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_tunnel: object`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

#### Example

```bash
ant beta:tunnels retrieve \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id
```

##### Response (200)

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

### List Tunnels

`$ ant beta:tunnels list`

**GET** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

#### Parameters

- `--include-archived: optional boolean`

  Query param: Whether to include archived tunnels in the results. Defaults to false.

- `--limit: optional number`

  Query param: Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

  format: int32

- `--page: optional string`

  Query param: Opaque pagination cursor from a previous `list_tunnels` response.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaListTunnelsResponse: object`

  A paginated list of tunnels.

  - `data: array of BetaTunnel`

    List of tunnels, ordered by created_at descending.

    - `id: string`

      Unique identifier for the tunnel, prefixed with `tnl_`.

    - `archived_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `display_name: string`

      Human-readable name for the tunnel (1-255 characters). Null if unset.

    - `domain: string`

      Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

    - `type: "tunnel"`

  - `next_page: string`

    Pagination cursor for the next page, or null if no more results.

#### Example

```bash
ant beta:tunnels list \
  --api-key my-anthropic-api-key
```

##### Response (200)

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

### Archive Tunnel

`$ ant beta:tunnels archive`

**POST** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

#### Parameters

- `--tunnel-id: string`

  Path parameter tunnel_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_tunnel: object`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

#### Example

```bash
ant beta:tunnels archive \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id
```

##### Response (200)

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

### Reveal Tunnel Token

`$ ant beta:tunnels reveal-token`

**POST** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

#### Parameters

- `--tunnel-id: string`

  Path parameter tunnel_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_tunnel_token: object`

  A tunnel's connector token.

  - `id: string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: string`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: "tunnel_token"`

#### Example

```bash
ant beta:tunnels reveal-token \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id
```

##### Response (200)

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

### Rotate Tunnel Token

`$ ant beta:tunnels rotate-token`

**POST** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

#### Parameters

- `--tunnel-id: string`

  Path param: Path parameter tunnel_id

- `--reason: optional string`

  Body param: Optional free-text reason for the rotation, recorded for audit.

  maxLength: 1024

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_tunnel_token: object`

  A tunnel's connector token.

  - `id: string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: string`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: "tunnel_token"`

#### Example

```bash
ant beta:tunnels rotate-token \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id
```

##### Response (200)

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

## Beta › Tunnels › Certificates

### Create Tunnel Certificate

`$ ant beta:tunnels:certificates create`

**POST** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

#### Parameters

- `--tunnel-id: string`

  Path param: Path parameter tunnel_id

- `--ca-certificate-pem: string`

  Body param: PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

  maxLength: 8192

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_tunnel_certificate: object`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `expires_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

#### Example

```bash
ant beta:tunnels:certificates create \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id \
  --ca-certificate-pem ca_certificate_pem
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

### Get Tunnel Certificate

`$ ant beta:tunnels:certificates retrieve`

**GET** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

#### Parameters

- `--tunnel-id: string`

  Path param: Path parameter tunnel_id

- `--certificate-id: string`

  Path param: Path parameter certificate_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_tunnel_certificate: object`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `expires_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

#### Example

```bash
ant beta:tunnels:certificates retrieve \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id \
  --certificate-id certificate_id
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

### List Tunnel Certificates

`$ ant beta:tunnels:certificates list`

**GET** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

#### Parameters

- `--tunnel-id: string`

  Path param: Path parameter tunnel_id

- `--include-archived: optional boolean`

  Query param: Whether to include archived certificates in the results. Defaults to false.

- `--limit: optional number`

  Query param: Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

  format: int32

- `--page: optional string`

  Query param: Opaque pagination cursor from a previous `list_tunnel_certificates` response.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaListTunnelCertificatesResponse: object`

  The tunnel's certificates.

  - `data: array of BetaTunnelCertificate`

    List of certificates, ordered by created_at descending.

    - `id: string`

      Unique identifier for the certificate, prefixed with `tcrt_`.

    - `archived_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `expires_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `fingerprint: string`

      Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

    - `tunnel_id: string`

      ID of the tunnel the certificate is registered against.

    - `type: "tunnel_certificate"`

  - `next_page: string`

    Pagination cursor for the next page, or null if no more results.

#### Example

```bash
ant beta:tunnels:certificates list \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id
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

`$ ant beta:tunnels:certificates archive`

**POST** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

#### Parameters

- `--tunnel-id: string`

  Path param: Path parameter tunnel_id

- `--certificate-id: string`

  Path param: Path parameter certificate_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_tunnel_certificate: object`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `expires_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

#### Example

```bash
ant beta:tunnels:certificates archive \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id \
  --certificate-id certificate_id
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

`$ ant beta:organization retrieve`

**GET** `/v1/organizations/me`

Retrieve information about the organization associated with the authenticated API key.

#### Returns

- `beta_organization: object`

  - `id: string`

    ID of the Organization.

    format: uuid

  - `name: string`

    Name of the Organization.

  - `type: "organization"`

    Object type.

    For Organizations, this is always `"organization"`.

#### Example

```bash
ant beta:organization retrieve \
  --api-key my-anthropic-api-key
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

`$ ant beta:organization:api-keys list`

**GET** `/v1/organizations/api_keys`

List API Keys

#### Parameters

- `--after-id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `--before-id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `--created-by-user-id: optional string`

  Filter by the ID of the User who created the object.

- `--limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  maximum: 1000, minimum: 1

- `--status: optional "active" or "archived" or "expired" or "inactive"`

  Filter by API key status.

- `--workspace-id: optional string`

  Filter by Workspace ID.

#### Returns

- `BetaListResponse_ApiKey_: object`

  - `data: array of BetaAPIKey`

    - `id: string`

      ID of the API key.

    - `created_at: string`

      RFC 3339 datetime string indicating when the API Key was created.

      format: date-time

    - `created_by: object`

      The ID and type of the actor that created the API key, or `null` when the
      creator is not recorded (legacy, workload-identity-federated, or
      system-created keys).

      - `id: string`

        ID of the actor that created the object.

      - `type: "service_account" or "user"`

        Type of the actor that created the object.

        - `"service_account"`

        - `"user"`

    - `expires_at: string`

      RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

      format: date-time

    - `name: string`

      Name of the API key.

    - `partial_key_hint: string`

      Partially redacted hint for the API key.

    - `principal: BetaAPIKeyUserActor or BetaAPIKeyServiceAccountActor`

      The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

      - `beta_api_key_user_actor: object`

        - `type: "user_actor"`

          Principal type. Always `"user_actor"` for a User.

        - `user_id: string`

          ID of the User the API key acts as.

      - `beta_api_key_service_account_actor: object`

        - `service_account_id: string`

          ID of the Service Account the API key acts as.

        - `type: "service_account_actor"`

          Principal type. Always `"service_account_actor"` for a Service Account.

    - `scope: BetaAPIKeyOrganizationScope or BetaAPIKeyWorkspaceScope`

      Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

      - `beta_api_key_organization_scope: object`

        - `type: "organization"`

          Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

      - `beta_api_key_workspace_scope: object`

        - `type: "workspace"`

          Scope type. Always `"workspace"`: the API key belongs to one Workspace.

        - `workspace_id: string`

          ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.

    - `status: "active" or "archived" or "expired" or "inactive"`

      Status of the API key.

      - `"active"`

      - `"archived"`

      - `"expired"`

      - `"inactive"`

    - `type: "api_key"`

      Object type.

      For API Keys, this is always `"api_key"`.

    - `workspace_id: string`

      **Deprecated**: Use `scope` instead. `workspace_id` is `null` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

      Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

  - `first_id: string`

    First ID in the `data` list. Can be used as the `before_id` for the previous page.

  - `has_more: boolean`

    Indicates if there are more results in the requested page direction.

  - `last_id: string`

    Last ID in the `data` list. Can be used as the `after_id` for the next page.

#### Example

```bash
ant beta:organization:api-keys list \
  --api-key my-anthropic-api-key
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

### Get API Key

`$ ant beta:organization:api-keys retrieve`

**GET** `/v1/organizations/api_keys/{api_key_id}`

Get API Key

#### Parameters

- `--api-key-id: string`

  ID of the API key.

#### Returns

- `beta_api_key: object`

  - `id: string`

    ID of the API key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the API Key was created.

    format: date-time

  - `created_by: object`

    The ID and type of the actor that created the API key, or `null` when the
    creator is not recorded (legacy, workload-identity-federated, or
    system-created keys).

    - `id: string`

      ID of the actor that created the object.

    - `type: "service_account" or "user"`

      Type of the actor that created the object.

      - `"service_account"`

      - `"user"`

  - `expires_at: string`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

    format: date-time

  - `name: string`

    Name of the API key.

  - `partial_key_hint: string`

    Partially redacted hint for the API key.

  - `principal: BetaAPIKeyUserActor or BetaAPIKeyServiceAccountActor`

    The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

    - `beta_api_key_user_actor: object`

      - `type: "user_actor"`

        Principal type. Always `"user_actor"` for a User.

      - `user_id: string`

        ID of the User the API key acts as.

    - `beta_api_key_service_account_actor: object`

      - `service_account_id: string`

        ID of the Service Account the API key acts as.

      - `type: "service_account_actor"`

        Principal type. Always `"service_account_actor"` for a Service Account.

  - `scope: BetaAPIKeyOrganizationScope or BetaAPIKeyWorkspaceScope`

    Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

    - `beta_api_key_organization_scope: object`

      - `type: "organization"`

        Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

    - `beta_api_key_workspace_scope: object`

      - `type: "workspace"`

        Scope type. Always `"workspace"`: the API key belongs to one Workspace.

      - `workspace_id: string`

        ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.

  - `status: "active" or "archived" or "expired" or "inactive"`

    Status of the API key.

    - `"active"`

    - `"archived"`

    - `"expired"`

    - `"inactive"`

  - `type: "api_key"`

    Object type.

    For API Keys, this is always `"api_key"`.

  - `workspace_id: string`

    **Deprecated**: Use `scope` instead. `workspace_id` is `null` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

    Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

#### Example

```bash
ant beta:organization:api-keys retrieve \
  --api-key my-anthropic-api-key \
  --api-key-id api_key_id
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

`$ ant beta:organization:api-keys update`

**POST** `/v1/organizations/api_keys/{api_key_id}`

Update API Key

#### Parameters

- `--api-key-id: string`

  ID of the API key.

- `--name: optional string`

  Name of the API key.

  maxLength: 500, minLength: 1

- `--status: optional "active" or "archived" or "inactive"`

  Status of the API key.

#### Returns

- `beta_api_key: object`

  - `id: string`

    ID of the API key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the API Key was created.

    format: date-time

  - `created_by: object`

    The ID and type of the actor that created the API key, or `null` when the
    creator is not recorded (legacy, workload-identity-federated, or
    system-created keys).

    - `id: string`

      ID of the actor that created the object.

    - `type: "service_account" or "user"`

      Type of the actor that created the object.

      - `"service_account"`

      - `"user"`

  - `expires_at: string`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

    format: date-time

  - `name: string`

    Name of the API key.

  - `partial_key_hint: string`

    Partially redacted hint for the API key.

  - `principal: BetaAPIKeyUserActor or BetaAPIKeyServiceAccountActor`

    The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

    - `beta_api_key_user_actor: object`

      - `type: "user_actor"`

        Principal type. Always `"user_actor"` for a User.

      - `user_id: string`

        ID of the User the API key acts as.

    - `beta_api_key_service_account_actor: object`

      - `service_account_id: string`

        ID of the Service Account the API key acts as.

      - `type: "service_account_actor"`

        Principal type. Always `"service_account_actor"` for a Service Account.

  - `scope: BetaAPIKeyOrganizationScope or BetaAPIKeyWorkspaceScope`

    Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

    - `beta_api_key_organization_scope: object`

      - `type: "organization"`

        Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

    - `beta_api_key_workspace_scope: object`

      - `type: "workspace"`

        Scope type. Always `"workspace"`: the API key belongs to one Workspace.

      - `workspace_id: string`

        ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.

  - `status: "active" or "archived" or "expired" or "inactive"`

    Status of the API key.

    - `"active"`

    - `"archived"`

    - `"expired"`

    - `"inactive"`

  - `type: "api_key"`

    Object type.

    For API Keys, this is always `"api_key"`.

  - `workspace_id: string`

    **Deprecated**: Use `scope` instead. `workspace_id` is `null` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

    Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

#### Example

```bash
ant beta:organization:api-keys update \
  --api-key my-anthropic-api-key \
  --api-key-id api_key_id
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

`$ ant beta:organization:external-keys create`

**POST** `/v1/organizations/external_keys`

Create an external key config owned by the caller's organization.

#### Parameters

- `--provider-config: BetaAWSExternalKeyConfig or BetaGCPExternalKeyConfig or BetaAzureExternalKeyConfigParam`

  KMS provider identity and auth coordinates.

- `--display-name: optional string`

  Human-friendly display name.

  maxLength: 255, minLength: 1

- `--geo: optional "us"`

  Data residency geo. Only `us` is supported.

#### Returns

- `beta_external_key: object`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `id: string`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `attachment: BetaExternalKeyAttachedAttachment or BetaExternalKeyUnattachedAttachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `beta_external_key_attached_attachment: object`

      - `type: "attached"`

    - `beta_external_key_unattached_attachment: object`

      - `type: "unattached"`

  - `created_at: string`

    format: date-time

  - `display_name: string`

    Human-friendly display name. Null if none was set.

  - `geo: string`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: BetaAWSExternalKeyConfig or BetaGCPExternalKeyConfig or BetaAzureExternalKeyConfig`

    KMS provider identity and auth coordinates.

    - `beta_aws_external_key_config: object`

      - `kms_arn: string`

        Full ARN of the AWS KMS key.

        maxLength: 2048

      - `type: "aws"`

      - `region: optional string`

        AWS region. Derived from `kms_arn` if omitted.

      - `role_arn: optional string`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `beta_gcp_external_key_config: object`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

      - `type: "gcp"`

    - `beta_azure_external_key_config: object`

      - `key_name: string`

        Name of the key within the vault.

      - `tenant_id: string`

        Azure AD tenant ID.

      - `type: "azure"`

      - `vault_uri: string`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `client_id: optional string`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `type: "external_key"`

  - `updated_at: string`

    format: date-time

#### Example

```bash
ant beta:organization:external-keys create \
  --api-key my-anthropic-api-key \
  --provider-config '{kms_arn: arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222, type: aws}'
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

`$ ant beta:organization:external-keys list`

**GET** `/v1/organizations/external_keys`

List external key configs in the caller's organization.

Results are ordered by creation time (newest first). Use the
`next_page` cursor from the response to fetch subsequent pages.

#### Parameters

- `--limit: optional number`

  Number of results per page.

  maximum: 100, minimum: 1

- `--page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Returns

- `BetaExternalKeyListResponse: object`

  Opaque-cursor page of external keys, ordered by creation time (newest first).

  - `data: array of BetaExternalKey`

    - `id: string`

      Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

    - `attachment: BetaExternalKeyAttachedAttachment or BetaExternalKeyUnattachedAttachment`

      Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

      - `beta_external_key_attached_attachment: object`

        - `type: "attached"`

      - `beta_external_key_unattached_attachment: object`

        - `type: "unattached"`

    - `created_at: string`

      format: date-time

    - `display_name: string`

      Human-friendly display name. Null if none was set.

    - `geo: string`

      Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

    - `provider_config: BetaAWSExternalKeyConfig or BetaGCPExternalKeyConfig or BetaAzureExternalKeyConfig`

      KMS provider identity and auth coordinates.

      - `beta_aws_external_key_config: object`

        - `kms_arn: string`

          Full ARN of the AWS KMS key.

          maxLength: 2048

        - `type: "aws"`

        - `region: optional string`

          AWS region. Derived from `kms_arn` if omitted.

        - `role_arn: optional string`

          **Deprecated**

          IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

      - `beta_gcp_external_key_config: object`

        - `key_name: string`

          Full resource name of the Cloud KMS key.

        - `type: "gcp"`

      - `beta_azure_external_key_config: object`

        - `key_name: string`

          Name of the key within the vault.

        - `tenant_id: string`

          Azure AD tenant ID.

        - `type: "azure"`

        - `vault_uri: string`

          Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

        - `client_id: optional string`

          Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

    - `type: "external_key"`

    - `updated_at: string`

      format: date-time

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results. Pass as `?page=` to fetch the next page.

#### Example

```bash
ant beta:organization:external-keys list \
  --api-key my-anthropic-api-key
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

`$ ant beta:organization:external-keys retrieve`

**GET** `/v1/organizations/external_keys/{external_key_id}`

Retrieve a single external key config in the caller's organization by ID.

#### Parameters

- `--external-key-id: string`

  ID of the External Key.

  maxLength: 2048

#### Returns

- `beta_external_key: object`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `id: string`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `attachment: BetaExternalKeyAttachedAttachment or BetaExternalKeyUnattachedAttachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `beta_external_key_attached_attachment: object`

      - `type: "attached"`

    - `beta_external_key_unattached_attachment: object`

      - `type: "unattached"`

  - `created_at: string`

    format: date-time

  - `display_name: string`

    Human-friendly display name. Null if none was set.

  - `geo: string`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: BetaAWSExternalKeyConfig or BetaGCPExternalKeyConfig or BetaAzureExternalKeyConfig`

    KMS provider identity and auth coordinates.

    - `beta_aws_external_key_config: object`

      - `kms_arn: string`

        Full ARN of the AWS KMS key.

        maxLength: 2048

      - `type: "aws"`

      - `region: optional string`

        AWS region. Derived from `kms_arn` if omitted.

      - `role_arn: optional string`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `beta_gcp_external_key_config: object`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

      - `type: "gcp"`

    - `beta_azure_external_key_config: object`

      - `key_name: string`

        Name of the key within the vault.

      - `tenant_id: string`

        Azure AD tenant ID.

      - `type: "azure"`

      - `vault_uri: string`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `client_id: optional string`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `type: "external_key"`

  - `updated_at: string`

    format: date-time

#### Example

```bash
ant beta:organization:external-keys retrieve \
  --api-key my-anthropic-api-key \
  --external-key-id external_key_id
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

`$ ant beta:organization:external-keys update`

**POST** `/v1/organizations/external_keys/{external_key_id}`

Partially update an external key config. Omitted fields are left unchanged.

`display_name` is always editable. `geo` and `provider_config` cannot
be changed once any workspace references this config, because previously
encrypted data requires the original key identity to decrypt.

#### Parameters

- `--external-key-id: string`

  ID of the External Key.

  maxLength: 2048

- `--display-name: optional string`

  Human-friendly display name.

  maxLength: 255, minLength: 1

- `--geo: optional "us"`

  Data residency geo. Only `us` is supported.

- `--provider-config: optional BetaAWSExternalKeyConfig or BetaGCPExternalKeyConfig or BetaAzureExternalKeyConfigParam`

  KMS provider identity and auth coordinates.

#### Returns

- `beta_external_key: object`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `id: string`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `attachment: BetaExternalKeyAttachedAttachment or BetaExternalKeyUnattachedAttachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `beta_external_key_attached_attachment: object`

      - `type: "attached"`

    - `beta_external_key_unattached_attachment: object`

      - `type: "unattached"`

  - `created_at: string`

    format: date-time

  - `display_name: string`

    Human-friendly display name. Null if none was set.

  - `geo: string`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: BetaAWSExternalKeyConfig or BetaGCPExternalKeyConfig or BetaAzureExternalKeyConfig`

    KMS provider identity and auth coordinates.

    - `beta_aws_external_key_config: object`

      - `kms_arn: string`

        Full ARN of the AWS KMS key.

        maxLength: 2048

      - `type: "aws"`

      - `region: optional string`

        AWS region. Derived from `kms_arn` if omitted.

      - `role_arn: optional string`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `beta_gcp_external_key_config: object`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

      - `type: "gcp"`

    - `beta_azure_external_key_config: object`

      - `key_name: string`

        Name of the key within the vault.

      - `tenant_id: string`

        Azure AD tenant ID.

      - `type: "azure"`

      - `vault_uri: string`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `client_id: optional string`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `type: "external_key"`

  - `updated_at: string`

    format: date-time

#### Example

```bash
ant beta:organization:external-keys update \
  --api-key my-anthropic-api-key \
  --external-key-id external_key_id
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

`$ ant beta:organization:external-keys delete`

**DELETE** `/v1/organizations/external_keys/{external_key_id}`

Delete an external key config.

The request is rejected if any workspace still references this config.

#### Parameters

- `--external-key-id: string`

  ID of the External Key.

  maxLength: 2048

#### Returns

- `BetaOrganizationExternalKeyDeleteResponse: object`

  - `id: string`

    ID of the deleted External Key.

  - `type: "external_key_deleted"`

#### Example

```bash
ant beta:organization:external-keys delete \
  --api-key my-anthropic-api-key \
  --external-key-id external_key_id
```

##### Response (200)

```json
{
  "id": "ekey_01AbCdEfGhIjKlMnOpQrStUv",
  "type": "external_key_deleted"
}
```

### Validate External Key

`$ ant beta:organization:external-keys validate`

**POST** `/v1/organizations/external_keys/{external_key_id}/validate`

Validate an external key config against the customer's KMS.

Anthropic performs an encrypt/decrypt roundtrip against the configured
KMS key and waits up to 30 seconds for the result. The response status is
`success` if the roundtrip succeeded, or `failure` with an error
message if it failed or timed out.

#### Parameters

- `--external-key-id: string`

  ID of the External Key.

  maxLength: 2048

#### Returns

- `BetaOrganizationExternalKeyValidateResponse: object`

  Result of a validation roundtrip against the customer's KMS.

  HTTP 200 for both outcomes — the operation completed; `status` says
  whether the key works.

  - `error: string`

    Error message when status is `failure`. Null otherwise.

  - `status: "failure" or "success"`

    `success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

    - `"failure"`

    - `"success"`

  - `type: "external_key_validation"`

#### Example

```bash
ant beta:organization:external-keys validate \
  --api-key my-anthropic-api-key \
  --external-key-id external_key_id
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

`$ ant beta:organization:federation:issuers create`

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

- `--issuer-url: string`

  Body param: The `iss` claim value to match against.

  minLength: 1

- `--name: string`

  Body param: Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  maxLength: 255, minLength: 1

- `--check-jti: optional boolean`

  Body param: Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Defaults to true. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

- `--jwks: optional BetaJWKSDiscovery or BetaJWKSExplicitURL or BetaJWKSInline`

  Body param: How signing keys are obtained. Defaults to OIDC discovery.

- `--max-jwt-lifetime-seconds: optional number`

  Body param: Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Defaults to 3600 (1h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  maximum: 176400, exclusiveMinimum: 0

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_federation_issuer: object`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `id: string`

    Tagged ID of the federation issuer.

  - `archived_at: string`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: boolean`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: string`

    When this issuer was created.

    format: date-time

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: string`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: BetaJWKSDiscovery or BetaJWKSExplicitURL or BetaJWKSInline`

    How signing keys are obtained for signature verification.

    - `beta_jwks_discovery: object`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: optional string`

        Set when the discovery URL differs from `issuer_url`.

    - `beta_jwks_explicit_url: object`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

      - `url: string`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `beta_jwks_inline: object`

      JWKS supplied directly; no network fetch.

      - `keys: array of map[unknown]`

        Inline JWK objects.

        minItems: 1

      - `type: "inline"`

  - `jwks_polling_disabled_at: string`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: object`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: string`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `type: "federation_issuer"`

  - `updated_at: string`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```bash
ant beta:organization:federation:issuers create \
  --api-key my-anthropic-api-key \
  --issuer-url x \
  --name x
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

`$ ant beta:organization:federation:issuers list`

**GET** `/v1/organizations/federation_issuers`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List federation issuers in your organization.

Archived issuers are excluded unless `include_archived=true`.

#### Parameters

- `--include-archived: optional boolean`

  Query param: Include archived resources. Defaults to false.

- `--limit: optional number`

  Query param: Number of results per page.

  maximum: 100, minimum: 1

- `--page: optional string`

  Query param: Opaque cursor from a previous response's `next_page`.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaFederationIssuerListResponse: object`

  - `data: array of BetaFederationIssuer`

    - `id: string`

      Tagged ID of the federation issuer.

    - `archived_at: string`

      If set, all rules referencing this issuer reject token exchange.

      format: date-time

    - `archived_by_actor_id: string`

      Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

    - `check_jti: boolean`

      Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

    - `created_at: string`

      When this issuer was created.

      format: date-time

    - `created_by_actor_id: string`

      Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

    - `issuer_url: string`

      The `iss` claim value. Incoming JWTs must match exactly.

    - `jwks: BetaJWKSDiscovery or BetaJWKSExplicitURL or BetaJWKSInline`

      How signing keys are obtained for signature verification.

      - `beta_jwks_discovery: object`

        JWKS via the issuer's OIDC discovery document.

        - `type: "discovery"`

        - `ca_cert_pem: optional string`

          Optional custom CA (PEM) for TLS verification of the JWKS fetch.

          maxLength: 8192

        - `discovery_base: optional string`

          Set when the discovery URL differs from `issuer_url`.

      - `beta_jwks_explicit_url: object`

        JWKS fetched from a fixed endpoint.

        - `type: "explicit_url"`

        - `url: string`

          JWKS endpoint.

          minLength: 1

        - `ca_cert_pem: optional string`

          Optional custom CA (PEM) for TLS verification of the JWKS fetch.

          maxLength: 8192

      - `beta_jwks_inline: object`

        JWKS supplied directly; no network fetch.

        - `keys: array of map[unknown]`

          Inline JWK objects.

          minItems: 1

        - `type: "inline"`

    - `jwks_polling_disabled_at: string`

      If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

      format: date-time

    - `max_jwt_lifetime_seconds: number`

      Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

    - `name: string`

      Admin-chosen slug identifier.

    - `poll_status: object`

      Status of automatic JWKS polling for a federation issuer.

      Anthropic periodically fetches the issuer's signing keys in the
      background. These fields summarize the most recent fetches so the
      health of the JWKS endpoint can be monitored.

      - `consecutive_failures: number`

        Consecutive fetch failures since the last success.

      - `last_fetched_at: string`

        When the last successful fetch completed.

        format: date-time

      - `next_poll_at: string`

        When the next fetch is scheduled. Null if paused.

        format: date-time

    - `type: "federation_issuer"`

    - `updated_at: string`

      When this issuer was last updated.

      format: date-time

    - `updated_by_actor_id: string`

      Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results.

#### Example

```bash
ant beta:organization:federation:issuers list \
  --api-key my-anthropic-api-key
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

`$ ant beta:organization:federation:issuers retrieve`

**GET** `/v1/organizations/federation_issuers/{federation_issuer_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a federation issuer by its ID (`fdis_...`).

#### Parameters

- `--federation-issuer-id: string`

  ID of the federation issuer.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_federation_issuer: object`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `id: string`

    Tagged ID of the federation issuer.

  - `archived_at: string`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: boolean`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: string`

    When this issuer was created.

    format: date-time

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: string`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: BetaJWKSDiscovery or BetaJWKSExplicitURL or BetaJWKSInline`

    How signing keys are obtained for signature verification.

    - `beta_jwks_discovery: object`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: optional string`

        Set when the discovery URL differs from `issuer_url`.

    - `beta_jwks_explicit_url: object`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

      - `url: string`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `beta_jwks_inline: object`

      JWKS supplied directly; no network fetch.

      - `keys: array of map[unknown]`

        Inline JWK objects.

        minItems: 1

      - `type: "inline"`

  - `jwks_polling_disabled_at: string`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: object`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: string`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `type: "federation_issuer"`

  - `updated_at: string`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```bash
ant beta:organization:federation:issuers retrieve \
  --api-key my-anthropic-api-key \
  --federation-issuer-id federation_issuer_id
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

`$ ant beta:organization:federation:issuers update`

**POST** `/v1/organizations/federation_issuers/{federation_issuer_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Partially update a federation issuer.

Setting `jwks` replaces the full JWKS shape at once. Archived issuers
cannot be updated; this returns 400. Create a new issuer instead.

Updating an issuer that backs a rule with a scope outside
`workspace:developer` or `workspace:inference` requires a Console
session.

#### Parameters

- `--federation-issuer-id: string`

  Path param: ID of the federation issuer to update.

- `--check-jti: optional boolean`

  Body param: Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

- `--issuer-url: optional string`

  Body param: Replaces the `iss` claim value to match against. For discovery-mode issuers without a `discovery_base`, this is also the URL Anthropic fetches the OIDC discovery document and signing keys from, so changing it repoints the JWKS source. Changing the issuer URL to a well-known shared platform is rejected while any live rule under this issuer would not constrain tenant identity.

  minLength: 1

- `--jwks: optional BetaJWKSDiscovery or BetaJWKSExplicitURL or BetaJWKSInline`

  Body param: Replaces the entire JWKS configuration.

- `--jwks-polling-disabled: optional boolean`

  Body param: Only `false` is accepted, to re-enable polling after the system pauses it. Polling is paused automatically; sending `true` is rejected.

- `--max-jwt-lifetime-seconds: optional number`

  Body param: Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  maximum: 176400, exclusiveMinimum: 0

- `--name: optional string`

  Body param: Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  maxLength: 255, minLength: 1

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_federation_issuer: object`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `id: string`

    Tagged ID of the federation issuer.

  - `archived_at: string`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: boolean`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: string`

    When this issuer was created.

    format: date-time

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: string`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: BetaJWKSDiscovery or BetaJWKSExplicitURL or BetaJWKSInline`

    How signing keys are obtained for signature verification.

    - `beta_jwks_discovery: object`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: optional string`

        Set when the discovery URL differs from `issuer_url`.

    - `beta_jwks_explicit_url: object`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

      - `url: string`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `beta_jwks_inline: object`

      JWKS supplied directly; no network fetch.

      - `keys: array of map[unknown]`

        Inline JWK objects.

        minItems: 1

      - `type: "inline"`

  - `jwks_polling_disabled_at: string`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: object`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: string`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `type: "federation_issuer"`

  - `updated_at: string`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```bash
ant beta:organization:federation:issuers update \
  --api-key my-anthropic-api-key \
  --federation-issuer-id federation_issuer_id
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

`$ ant beta:organization:federation:issuers archive`

**POST** `/v1/organizations/federation_issuers/{federation_issuer_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a federation issuer.

Idempotent; re-archiving returns the issuer with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still references the issuer; archive those rules first (a rule's
issuer cannot be changed), or recreate them against another issuer.

#### Parameters

- `--federation-issuer-id: string`

  ID of the federation issuer to archive.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_federation_issuer: object`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `id: string`

    Tagged ID of the federation issuer.

  - `archived_at: string`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: boolean`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: string`

    When this issuer was created.

    format: date-time

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: string`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: BetaJWKSDiscovery or BetaJWKSExplicitURL or BetaJWKSInline`

    How signing keys are obtained for signature verification.

    - `beta_jwks_discovery: object`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: optional string`

        Set when the discovery URL differs from `issuer_url`.

    - `beta_jwks_explicit_url: object`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

      - `url: string`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `beta_jwks_inline: object`

      JWKS supplied directly; no network fetch.

      - `keys: array of map[unknown]`

        Inline JWK objects.

        minItems: 1

      - `type: "inline"`

  - `jwks_polling_disabled_at: string`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: object`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: string`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `type: "federation_issuer"`

  - `updated_at: string`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```bash
ant beta:organization:federation:issuers archive \
  --api-key my-anthropic-api-key \
  --federation-issuer-id federation_issuer_id
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

`$ ant beta:organization:federation:rules create`

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

- `--issuer-id: string`

  Body param: Tagged ID of the federation issuer.

- `--match: object`

  Body param: Conditions the verified JWT must satisfy for this rule to apply. At least one of `subject_prefix` (other than a wildcard-only value like `*`), `claims`, or `condition` is required; `audience` alone is not sufficient.

- `--name: string`

  Body param: Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  maxLength: 255, minLength: 1

- `--oauth-scope: string`

  Body param: Space-separated OAuth scopes. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

  minLength: 1

- `--target: object`

  Body param: Identity that tokens minted via this rule act as. Currently always a `service_account` target.

- `--applies-to-all-workspaces: optional boolean`

  Body param: When true, enable this rule for every workspace in the org (including workspaces created later).

- `--attributes: optional map[string]`

  Body param: CEL expressions `{name: expr}` extracting named values from claims. Not yet supported; any non-empty value is rejected with 400.

- `--description: optional string`

  Body param: Optional free-text description.

  maxLength: 2000

- `--token-lifetime-seconds: optional number`

  Body param: Lifetime in seconds for access tokens minted via this rule (60-86400). Defaults to 3600 (1h). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  maximum: 86400, minimum: 60

- `--workspace-id: optional string`

  Body param: Tagged ID of the workspace to enable this rule for. Required unless `applies_to_all_workspaces` is true. Additional workspaces can be added via the `/federation_rules/{federation_rule_id}/workspaces` sub-resource.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_federation_rule: object`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string`

    Issuer's display name at read time.

  - `match: object`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: optional map[string]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: optional string`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: object`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

    - `service_account_name: optional string`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

  - `updated_at: string`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```bash
ant beta:organization:federation:rules create \
  --api-key my-anthropic-api-key \
  --issuer-id issuer_id \
  --match '{}' \
  --name x \
  --oauth-scope x \
  --target '{service_account_id: svac_01SDCCSbTxrXDpWc1phhtcfK, type: service_account}'
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

`$ ant beta:organization:federation:rules list`

**GET** `/v1/organizations/federation_rules`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List federation rules in your organization.

Optionally filter by issuer with `issuer_id`. Archived rules are excluded
unless `include_archived=true`.

#### Parameters

- `--include-archived: optional boolean`

  Query param: Include archived resources. Defaults to false.

- `--issuer-id: optional string`

  Query param: Filter to rules referencing this federation issuer.

- `--limit: optional number`

  Query param: Number of results per page.

  maximum: 100, minimum: 1

- `--page: optional string`

  Query param: Opaque cursor from a previous response's `next_page`.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaFederationRuleListResponse: object`

  - `data: array of BetaFederationRule`

    - `id: string`

      Tagged ID of the federation rule.

    - `applies_to_all_workspaces: boolean`

      When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

    - `archived_at: string`

      If set, this rule is archived and rejects token exchange.

      format: date-time

    - `archived_by_actor_id: string`

      Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

    - `attributes: map[string]`

      CEL expressions extracting named values from claims. Not yet supported; always null.

    - `created_at: string`

      When this rule was created.

      format: date-time

    - `created_by_actor_id: string`

      Tagged ID (`user_`/`svac_`) of the actor that created this rule.

    - `description: string`

      Optional free-text description.

    - `issuer_id: string`

      Tagged ID of the issuer whose tokens this rule accepts.

    - `issuer_name: string`

      Issuer's display name at read time.

    - `match: object`

      Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

      - `audience: optional string`

        Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

        maxLength: 1024

      - `claims: optional map[string]`

        Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

      - `condition: optional string`

        CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

        maxLength: 4096

      - `subject_prefix: optional string`

        Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

        maxLength: 1024

    - `name: string`

      Admin-chosen slug identifier.

    - `oauth_scope: string`

      Space-separated OAuth scopes granted on the minted token.

    - `target: object`

      Identity that tokens minted via this rule act as. Currently always a `service_account` target.

      - `service_account_id: string`

        Tagged ID of the service account to mint tokens for.

      - `type: "service_account"`

      - `service_account_name: optional string`

        Service account's display name at read time. Ignored on writes.

    - `token_lifetime_seconds: number`

      Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

    - `type: "federation_rule"`

    - `updated_at: string`

      When this rule was last updated.

      format: date-time

    - `updated_by_actor_id: string`

      Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

    - `workspace_id: string`

      Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

    - `workspace_ids: array of string`

      Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results.

#### Example

```bash
ant beta:organization:federation:rules list \
  --api-key my-anthropic-api-key
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

`$ ant beta:organization:federation:rules retrieve`

**GET** `/v1/organizations/federation_rules/{federation_rule_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a federation rule by its ID (`fdrl_...`).

#### Parameters

- `--federation-rule-id: string`

  ID of the federation rule.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_federation_rule: object`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string`

    Issuer's display name at read time.

  - `match: object`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: optional map[string]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: optional string`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: object`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

    - `service_account_name: optional string`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

  - `updated_at: string`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```bash
ant beta:organization:federation:rules retrieve \
  --api-key my-anthropic-api-key \
  --federation-rule-id federation_rule_id
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

`$ ant beta:organization:federation:rules update`

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

- `--federation-rule-id: string`

  Path param: ID of the federation rule to update.

- `--applies-to-all-workspaces: optional boolean`

  Body param: When true, enables this rule for every workspace in the org (including workspaces created later). Setting `false` is rejected with 400 if no workspace would remain enabled; a rule with only a legacy `workspace_id` binding continues to mint.

- `--attributes: optional map[string]`

  Body param: Replaces the CEL expressions `{name: expr}` extracting named values from claims. Send null to clear them. Not yet supported; any non-empty value is rejected with 400.

- `--description: optional string`

  Body param: Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

  maxLength: 2000

- `--match: optional object`

  Body param: Does the incoming JWT qualify?

  All populated fields must pass; omitted fields are skipped. At least one
  of `subject_prefix` (other than a wildcard-only value like `*`), `claims`,
  or `condition` is required; `audience` alone is not sufficient.

- `--name: optional string`

  Body param: Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  maxLength: 255, minLength: 1

- `--oauth-scope: optional string`

  Body param: Replaces the space-separated OAuth scopes granted on minted tokens. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

  minLength: 1

- `--target: optional object`

  Body param: Bind to a fixed service account by ID.

- `--token-lifetime-seconds: optional number`

  Body param: Replaces the lifetime in seconds for access tokens minted via this rule (60-86400). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  maximum: 86400, minimum: 60

- `--workspace-id: optional string`

  Body param: Replaces the existing single workspace enablement (the previous one is removed). Rejected with 400 if the rule is enabled for more than one workspace; use the `/federation_rules/{federation_rule_id}/workspaces` sub-resource instead.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_federation_rule: object`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string`

    Issuer's display name at read time.

  - `match: object`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: optional map[string]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: optional string`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: object`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

    - `service_account_name: optional string`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

  - `updated_at: string`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```bash
ant beta:organization:federation:rules update \
  --api-key my-anthropic-api-key \
  --federation-rule-id federation_rule_id
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

`$ ant beta:organization:federation:rules archive`

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

- `--federation-rule-id: string`

  ID of the federation rule to archive.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_federation_rule: object`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string`

    Issuer's display name at read time.

  - `match: object`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: optional map[string]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: optional string`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: object`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

    - `service_account_name: optional string`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

  - `updated_at: string`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```bash
ant beta:organization:federation:rules archive \
  --api-key my-anthropic-api-key \
  --federation-rule-id federation_rule_id
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

`$ ant beta:organization:federation:rules:workspaces add`

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

- `--federation-rule-id: string`

  Path param: ID of the federation rule.

- `--workspace-id: string`

  Body param: Tagged ID of the workspace to enable this rule for.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_federation_rule_workspace: object`

  - `created_at: string`

    When this workspace was enabled for the rule.

    format: date-time

  - `created_by_actor_id: string`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `federation_rule_id: string`

    Tagged ID of the federation rule.

  - `type: "federation_rule_workspace"`

  - `workspace_id: string`

    Tagged ID of the workspace this rule is enabled for.

  - `workspace_name: string`

    Workspace display name. Populated when listing; null in the enable response.

#### Example

```bash
ant beta:organization:federation:rules:workspaces add \
  --api-key my-anthropic-api-key \
  --federation-rule-id federation_rule_id \
  --workspace-id workspace_id
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

`$ ant beta:organization:federation:rules:workspaces list`

**GET** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List workspaces where this federation rule is enabled.

Returns all workspace enablements in a single response; the `limit` and
`page` parameters are accepted but have no effect, and `next_page` is
always `null`. Returns explicit per-workspace enablements only; for
rules with `applies_to_all_workspaces` or a legacy single
`workspace_id`, check those fields on the rule itself.

#### Parameters

- `--federation-rule-id: string`

  Path param: ID of the federation rule.

- `--limit: optional number`

  Query param: Number of results per page.

  maximum: 100, minimum: 1

- `--page: optional string`

  Query param: Opaque cursor from a previous response's `next_page`.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaFederationRuleWorkspaceListResponse: object`

  - `data: array of BetaFederationRuleWorkspace`

    - `created_at: string`

      When this workspace was enabled for the rule.

      format: date-time

    - `created_by_actor_id: string`

      Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

    - `federation_rule_id: string`

      Tagged ID of the federation rule.

    - `type: "federation_rule_workspace"`

    - `workspace_id: string`

      Tagged ID of the workspace this rule is enabled for.

    - `workspace_name: string`

      Workspace display name. Populated when listing; null in the enable response.

  - `next_page: string`

    Opaque cursor for the next page; null when there are no more results.

#### Example

```bash
ant beta:organization:federation:rules:workspaces list \
  --api-key my-anthropic-api-key \
  --federation-rule-id federation_rule_id
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

`$ ant beta:organization:federation:rules:workspaces remove`

**DELETE** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Disable a federation rule for a workspace.

Idempotent; succeeds even if the enablement was already removed. OAuth
callers may only manage rules whose `oauth_scope` is
`workspace:developer` or `workspace:inference`; other scopes require a
Console session.

#### Parameters

- `--federation-rule-id: string`

  Path param: ID of the federation rule.

- `--workspace-id: string`

  Path param: ID of the workspace to disable for.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaOrganizationFederationRuleWorkspaceRemoveResponse: object`

  - `federation_rule_id: string`

    Tagged ID of the federation rule.

  - `type: "federation_rule_workspace_deleted"`

  - `workspace_id: string`

    Tagged ID of the workspace named in the delete request. Removal is idempotent.

#### Example

```bash
ant beta:organization:federation:rules:workspaces remove \
  --api-key my-anthropic-api-key \
  --federation-rule-id federation_rule_id \
  --workspace-id workspace_id
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

`$ ant beta:organization:invites create`

**POST** `/v1/organizations/invites`

Invite a user to join the organization by email.

On plans that draw members from a finite pool of purchased seats, the invite automatically consumes a seat from the lowest tier with availability; there is no seat-tier parameter. When no seat is free the request fails with a 400 error rather than purchasing a seat.

#### Parameters

- `--email: string`

  Email of the User.

  format: email

- `--role: "billing" or "claude_code_user" or "developer" or 2 more`

  Role for the invited User.

  The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

- `--rbac-group-id: optional array of string`

  RBAC group IDs to assign to the User when the Invite is accepted. A non-empty array is accepted only for a Claude Enterprise organization with RBAC groups, and requires the key to carry the `write:rbac_groups` scope.

  maxItems: 100

#### Returns

- `beta_organization_invite: object`

  - `id: string`

    ID of the Invite.

  - `accepted_at: string`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `email: string`

    Email of the User being invited.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `invited_at: string`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `rbac_group_ids: array of string`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `role: "admin" or "billing" or "claude_code_user" or 6 more`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

  - `status: "accepted" or "deleted" or "expired" or "pending"`

    Status of the Invite.

    - `"accepted"`

    - `"deleted"`

    - `"expired"`

    - `"pending"`

  - `type: "invite"`

    Object type.

    For Invites, this is always `"invite"`.

#### Example

```bash
ant beta:organization:invites create \
  --api-key my-anthropic-api-key \
  --email user@emaildomain.com \
  --role user
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

`$ ant beta:organization:invites list`

**GET** `/v1/organizations/invites`

List the organization's invites.

#### Parameters

- `--after-id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `--before-id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `--email: optional string`

  Filter by the email address the Invite was sent to. Matches the same way as the Users list's `email` filter (normalized, case-insensitive).

  format: email

- `--limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  maximum: 1000, minimum: 1

- `--role: optional array of string`

  Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

  Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

- `--status: optional array of "accepted" or "expired" or "pending"`

  Filter by Invite status. Repeatable; values are OR'ed together. Omit to return `pending`, `accepted`, and `expired` Invites alike.

#### Returns

- `BetaListResponse_InviteSchema_: object`

  - `data: array of BetaOrganizationInvite`

    - `id: string`

      ID of the Invite.

    - `accepted_at: string`

      RFC 3339 datetime string indicating when the Invite was accepted, or null.

      format: date-time

    - `email: string`

      Email of the User being invited.

    - `expires_at: string`

      RFC 3339 datetime string indicating when the Invite expires.

      format: date-time

    - `invited_at: string`

      RFC 3339 datetime string indicating when the Invite was created.

      format: date-time

    - `rbac_group_ids: array of string`

      RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

    - `role: "admin" or "billing" or "claude_code_user" or 6 more`

      Organization role of the User.

      - `"admin"`

      - `"billing"`

      - `"claude_code_user"`

      - `"developer"`

      - `"managed"`

      - `"membership_admin"`

      - `"owner"`

      - `"primary_owner"`

      - `"user"`

    - `status: "accepted" or "deleted" or "expired" or "pending"`

      Status of the Invite.

      - `"accepted"`

      - `"deleted"`

      - `"expired"`

      - `"pending"`

    - `type: "invite"`

      Object type.

      For Invites, this is always `"invite"`.

  - `first_id: string`

    First ID in the `data` list. Can be used as the `before_id` for the previous page.

  - `has_more: boolean`

    Indicates if there are more results in the requested page direction.

  - `last_id: string`

    Last ID in the `data` list. Can be used as the `after_id` for the next page.

#### Example

```bash
ant beta:organization:invites list \
  --api-key my-anthropic-api-key
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

`$ ant beta:organization:invites retrieve`

**GET** `/v1/organizations/invites/{invite_id}`

Retrieve an invite by ID.

#### Parameters

- `--invite-id: string`

  ID of the Invite.

#### Returns

- `beta_organization_invite: object`

  - `id: string`

    ID of the Invite.

  - `accepted_at: string`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `email: string`

    Email of the User being invited.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `invited_at: string`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `rbac_group_ids: array of string`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `role: "admin" or "billing" or "claude_code_user" or 6 more`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

  - `status: "accepted" or "deleted" or "expired" or "pending"`

    Status of the Invite.

    - `"accepted"`

    - `"deleted"`

    - `"expired"`

    - `"pending"`

  - `type: "invite"`

    Object type.

    For Invites, this is always `"invite"`.

#### Example

```bash
ant beta:organization:invites retrieve \
  --api-key my-anthropic-api-key \
  --invite-id invite_id
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

`$ ant beta:organization:invites delete`

**DELETE** `/v1/organizations/invites/{invite_id}`

Delete a pending invite.

#### Parameters

- `--invite-id: string`

  ID of the Invite.

#### Returns

- `BetaOrganizationInviteDeleteResponse: object`

  - `id: string`

    ID of the Invite.

  - `type: "invite_deleted"`

    Deleted object type.

    For Invites, this is always `"invite_deleted"`.

#### Example

```bash
ant beta:organization:invites delete \
  --api-key my-anthropic-api-key \
  --invite-id invite_id
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

`$ ant beta:organization:service-accounts create`

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

- `--name: string`

  Body param: Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  maxLength: 255, minLength: 1

- `--description: optional string`

  Body param: Optional free-text description.

  maxLength: 2000

- `--organization-role: optional "admin" or "developer"`

  Body param: Org-level role. Defaults to `developer`.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_service_account: object`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `id: string`

    Tagged ID of the service account.

  - `archived_at: string`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: string`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: string`

    Optional free-text description.

  - `name: string`

    Admin-chosen slug identifier.

  - `organization_role: "admin" or "developer"`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `type: "service_account"`

  - `updated_at: string`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```bash
ant beta:organization:service-accounts create \
  --api-key my-anthropic-api-key \
  --name ci-deploy-bot
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

`$ ant beta:organization:service-accounts list`

**GET** `/v1/organizations/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List service accounts in the caller's organization.

Results are ordered by creation time, newest first. Use `limit` and the
`next_page` cursor to paginate; set `include_archived=true` to include
archived service accounts.

#### Parameters

- `--include-archived: optional boolean`

  Query param: Include archived resources. Defaults to false.

- `--limit: optional number`

  Query param: Number of results per page.

  maximum: 100, minimum: 1

- `--page: optional string`

  Query param: Opaque cursor from a previous response's `next_page`.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaServiceAccountListResponse: object`

  - `data: array of BetaServiceAccount`

    - `id: string`

      Tagged ID of the service account.

    - `archived_at: string`

      If set, this service account is archived.

      format: date-time

    - `archived_by_actor_id: string`

      Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

    - `created_at: string`

      When this service account was created.

      format: date-time

    - `created_by_actor_id: string`

      Tagged ID (`user_`/`svac_`) of the actor that created this service account.

    - `description: string`

      Optional free-text description.

    - `name: string`

      Admin-chosen slug identifier.

    - `organization_role: "admin" or "developer"`

      Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

      - `"admin"`

      - `"developer"`

    - `type: "service_account"`

    - `updated_at: string`

      When this service account was last updated.

      format: date-time

    - `updated_by_actor_id: string`

      Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results.

#### Example

```bash
ant beta:organization:service-accounts list \
  --api-key my-anthropic-api-key
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

`$ ant beta:organization:service-accounts retrieve`

**GET** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a service account by its ID (`svac_...`).

#### Parameters

- `--service-account-id: string`

  ID of the service account.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_service_account: object`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `id: string`

    Tagged ID of the service account.

  - `archived_at: string`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: string`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: string`

    Optional free-text description.

  - `name: string`

    Admin-chosen slug identifier.

  - `organization_role: "admin" or "developer"`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `type: "service_account"`

  - `updated_at: string`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```bash
ant beta:organization:service-accounts retrieve \
  --api-key my-anthropic-api-key \
  --service-account-id service_account_id
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

`$ ant beta:organization:service-accounts update`

**POST** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Update a service account.

Only `description` and `organization_role` are mutable; `name` cannot be
changed. Archived service accounts cannot be updated; this returns 400.
Setting `organization_role` to `admin` (even when unchanged) requires an
interactive credential (a user OAuth token or a Console session).

#### Parameters

- `--service-account-id: string`

  Path param: ID of the service account to update.

- `--description: optional string`

  Body param: Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

  maxLength: 2000

- `--organization-role: optional "admin" or "developer"`

  Body param: Replaces the org-level role. Omit or send `null` to leave unchanged.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_service_account: object`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `id: string`

    Tagged ID of the service account.

  - `archived_at: string`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: string`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: string`

    Optional free-text description.

  - `name: string`

    Admin-chosen slug identifier.

  - `organization_role: "admin" or "developer"`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `type: "service_account"`

  - `updated_at: string`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```bash
ant beta:organization:service-accounts update \
  --api-key my-anthropic-api-key \
  --service-account-id service_account_id
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

`$ ant beta:organization:service-accounts archive`

**POST** `/v1/organizations/service_accounts/{service_account_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a service account.

Idempotent; re-archiving returns the service account with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still targets this service account, same as issuer archival; archive
those rules first or change their target to another service account.

#### Parameters

- `--service-account-id: string`

  ID of the service account to archive.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_service_account: object`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `id: string`

    Tagged ID of the service account.

  - `archived_at: string`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: string`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: string`

    Optional free-text description.

  - `name: string`

    Admin-chosen slug identifier.

  - `organization_role: "admin" or "developer"`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `type: "service_account"`

  - `updated_at: string`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```bash
ant beta:organization:service-accounts archive \
  --api-key my-anthropic-api-key \
  --service-account-id service_account_id
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

`$ ant beta:organization:service-accounts:workspaces add`

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

- `--service-account-id: string`

  Path param: ID of the service account.

- `--workspace-id: string`

  Body param: Tagged workspace ID to add the service account to.

- `--workspace-role: "workspace_admin" or "workspace_developer" or "workspace_restricted_developer" or "workspace_user"`

  Body param: Role to assign to the service account in this workspace.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_service_account_workspace_member: object`

  - `created_by_actor_id: string`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```bash
ant beta:organization:service-accounts:workspaces add \
  --api-key my-anthropic-api-key \
  --service-account-id service_account_id \
  --workspace-id workspace_id \
  --workspace-role workspace_admin
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

`$ ant beta:organization:service-accounts:workspaces list`

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

- `--service-account-id: string`

  Path param: ID of the service account.

- `--limit: optional number`

  Query param: Number of results per page.

  maximum: 100, minimum: 1

- `--page: optional string`

  Query param: Opaque cursor from a previous response's `next_page`.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaServiceAccountWorkspaceMemberListResponse: object`

  - `data: array of BetaServiceAccountWorkspaceMember`

    - `created_by_actor_id: string`

      Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

    - `implicit: boolean`

      True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

    - `service_account_id: string`

      Tagged service account ID (`svac_...`).

    - `type: "service_account_workspace_member"`

    - `workspace_id: string`

      Tagged workspace ID (`wrkspc_...`).

    - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

      Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

      - `"workspace_admin"`

      - `"workspace_billing"`

      - `"workspace_developer"`

      - `"workspace_restricted_developer"`

      - `"workspace_user"`

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results.

#### Example

```bash
ant beta:organization:service-accounts:workspaces list \
  --api-key my-anthropic-api-key \
  --service-account-id service_account_id
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

`$ ant beta:organization:service-accounts:workspaces remove`

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

- `--service-account-id: string`

  Path param: ID of the service account.

- `--workspace-id: string`

  Path param: ID of the workspace.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaOrganizationServiceAccountWorkspaceRemoveResponse: object`

  - `service_account_id: string`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `type: "service_account_workspace_member_deleted"`

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```bash
ant beta:organization:service-accounts:workspaces remove \
  --api-key my-anthropic-api-key \
  --service-account-id service_account_id \
  --workspace-id workspace_id
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

`$ ant beta:organization:users list`

**GET** `/v1/organizations/users`

List the organization's members.

#### Parameters

- `--after-id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `--before-id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `--email: optional string`

  Filter by user email.

  format: email

- `--limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  maximum: 1000, minimum: 1

- `--role: optional array of string`

  Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

  Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

#### Returns

- `BetaListResponse_User_: object`

  - `data: array of BetaOrganizationUser`

    - `id: string`

      ID of the User.

    - `added_at: string`

      RFC 3339 datetime string indicating when the User joined the Organization.

      format: date-time

    - `email: string`

      Email of the User.

    - `name: string`

      Name of the User.

    - `role: "admin" or "billing" or "claude_code_user" or 6 more`

      Organization role of the User.

      - `"admin"`

      - `"billing"`

      - `"claude_code_user"`

      - `"developer"`

      - `"managed"`

      - `"membership_admin"`

      - `"owner"`

      - `"primary_owner"`

      - `"user"`

    - `type: "user"`

      Object type.

      For Users, this is always `"user"`.

  - `first_id: string`

    First ID in the `data` list. Can be used as the `before_id` for the previous page.

  - `has_more: boolean`

    Indicates if there are more results in the requested page direction.

  - `last_id: string`

    Last ID in the `data` list. Can be used as the `after_id` for the next page.

#### Example

```bash
ant beta:organization:users list \
  --api-key my-anthropic-api-key
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

`$ ant beta:organization:users retrieve`

**GET** `/v1/organizations/users/{user_id}`

Retrieve a member of the organization by user ID.

#### Parameters

- `--user-id: string`

  ID of the User.

#### Returns

- `beta_organization_user: object`

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: "admin" or "billing" or "claude_code_user" or 6 more`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

#### Example

```bash
ant beta:organization:users retrieve \
  --api-key my-anthropic-api-key \
  --user-id user_id
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

`$ ant beta:organization:users update`

**POST** `/v1/organizations/users/{user_id}`

Update a member's organization role.

#### Parameters

- `--user-id: string`

  ID of the User.

- `--role: "billing" or "claude_code_user" or "developer" or 2 more`

  New role for the User.

  The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

#### Returns

- `beta_organization_user: object`

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: "admin" or "billing" or "claude_code_user" or 6 more`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

#### Example

```bash
ant beta:organization:users update \
  --api-key my-anthropic-api-key \
  --user-id user_id \
  --role user
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

`$ ant beta:organization:users remove`

**DELETE** `/v1/organizations/users/{user_id}`

Remove a member from the organization.

#### Parameters

- `--user-id: string`

  ID of the User.

#### Returns

- `BetaOrganizationUserRemoveResponse: object`

  - `id: string`

    ID of the User.

  - `type: "user_deleted"`

    Deleted object type.

    For Users, this is always `"user_deleted"`.

#### Example

```bash
ant beta:organization:users remove \
  --api-key my-anthropic-api-key \
  --user-id user_id
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

`$ ant beta:organization:workspaces list`

**GET** `/v1/organizations/workspaces`

List Workspaces

#### Parameters

- `--after-id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `--before-id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `--include-archived: optional boolean`

  Whether to include Workspaces that have been archived in the response

- `--limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  maximum: 1000, minimum: 1

#### Returns

- `BetaListResponse_Workspace_: object`

  - `data: array of BetaWorkspace`

    - `id: string`

      ID of the Workspace.

    - `archived_at: string`

      RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

      format: date-time

    - `compartment_id: string`

      Identifier for this Workspace's encryption compartment. When you configure a
      customer-managed encryption key (CMEK) on AWS, reference this value in your
      KMS key-policy condition so the key is scoped to this compartment. On GCP and
      Azure, Anthropic enforces the compartment binding automatically; you do not
      need to reference this value in your key configuration. See the CMEK integration guide for the
      required key configuration, including the value used during key validation.

    - `created_at: string`

      RFC 3339 datetime string indicating when the Workspace was created.

      format: date-time

    - `data_residency: object`

      Data residency configuration.

      - `allowed_inference_geos: array of string or "unrestricted"`

        Permitted inference geo values. 'unrestricted' means all geos are allowed.

        - `geos: array of string`

        - `unrestricted: "unrestricted"`

      - `default_inference_geo: string`

        Default inference geo applied when requests omit the parameter.

      - `workspace_geo: string`

        Geographic region for workspace data storage. Immutable after creation.

    - `display_color: string`

      Hex color code representing the Workspace in the Anthropic Console.

    - `external_key_id: string`

      ID of the customer-managed encryption key (CMEK) configuration to use for this
      Workspace. Setting this field requires CMEK to be enabled for your
      organization. When set, data stored for this Workspace is encrypted with the
      referenced key. Create key configurations with the External Keys API. This
      field is write-once: once a key is attached to a Workspace it cannot be
      detached or replaced. To rotate key material, rotate the underlying key on
      your cloud KMS; the `external_key_id` stays the same.

    - `name: string`

      Name of the Workspace.

    - `tags: map[string]`

      User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

    - `type: "workspace"`

      Object type.

      For Workspaces, this is always `"workspace"`.

  - `first_id: string`

    First ID in the `data` list. Can be used as the `before_id` for the previous page.

  - `has_more: boolean`

    Indicates if there are more results in the requested page direction.

  - `last_id: string`

    Last ID in the `data` list. Can be used as the `after_id` for the next page.

#### Example

```bash
ant beta:organization:workspaces list \
  --api-key my-anthropic-api-key
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

`$ ant beta:organization:workspaces create`

**POST** `/v1/organizations/workspaces`

Create Workspace

#### Parameters

- `--name: string`

  Body param: Name of the Workspace.

  maxLength: 40, minLength: 1

- `--data-residency: optional object`

  Body param: Data residency configuration for the workspace. If omitted, defaults to `workspace_geo: "us"`, `allowed_inference_geos: "unrestricted"`, and `default_inference_geo: "global"`.

- `--display-color: optional string`

  Body param: Hex color code representing the Workspace in the Anthropic Console.

  maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

- `--external-key-id: optional string`

  Body param: ID of the customer-managed encryption key (CMEK) configuration to use for this
  Workspace. Setting this field requires CMEK to be enabled for your
  organization. When set, data stored for this Workspace is encrypted with the
  referenced key. Create key configurations with the External Keys API. This
  field is write-once: once a key is attached to a Workspace it cannot be
  detached or replaced. To rotate key material, rotate the underlying key on
  your cloud KMS; the `external_key_id` stays the same.

- `--tags: optional map[string]`

  Body param: User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_workspace: object`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK integration guide for the
    required key configuration, including the value used during key validation.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: object`

    Data residency configuration.

    - `allowed_inference_geos: array of string or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `geos: array of string`

      - `unrestricted: "unrestricted"`

    - `default_inference_geo: string`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: string`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```bash
ant beta:organization:workspaces create \
  --api-key my-anthropic-api-key \
  --name x
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

`$ ant beta:organization:workspaces retrieve`

**GET** `/v1/organizations/workspaces/{workspace_id}`

Get Workspace

#### Parameters

- `--workspace-id: string`

  ID of the Workspace.

#### Returns

- `beta_workspace: object`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK integration guide for the
    required key configuration, including the value used during key validation.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: object`

    Data residency configuration.

    - `allowed_inference_geos: array of string or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `geos: array of string`

      - `unrestricted: "unrestricted"`

    - `default_inference_geo: string`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: string`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```bash
ant beta:organization:workspaces retrieve \
  --api-key my-anthropic-api-key \
  --workspace-id workspace_id
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

`$ ant beta:organization:workspaces update`

**POST** `/v1/organizations/workspaces/{workspace_id}`

Update Workspace

#### Parameters

- `--workspace-id: string`

- `--data-residency: optional object`

  Data residency configuration for the workspace.

- `--display-color: optional string`

  Hex color code representing the Workspace in the Anthropic Console.

  maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

- `--external-key-id: optional string`

  ID of the customer-managed encryption key (CMEK) configuration to use for this
  Workspace. Setting this field requires CMEK to be enabled for your
  organization. When set, data stored for this Workspace is encrypted with the
  referenced key. Create key configurations with the External Keys API. This
  field is write-once: once a key is attached to a Workspace it cannot be
  detached or replaced. To rotate key material, rotate the underlying key on
  your cloud KMS; the `external_key_id` stays the same.

- `--name: optional string`

  Name of the Workspace.

  maxLength: 40, minLength: 1

- `--tags: optional map[string]`

  User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Returns

- `beta_workspace: object`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK integration guide for the
    required key configuration, including the value used during key validation.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: object`

    Data residency configuration.

    - `allowed_inference_geos: array of string or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `geos: array of string`

      - `unrestricted: "unrestricted"`

    - `default_inference_geo: string`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: string`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```bash
ant beta:organization:workspaces update \
  --api-key my-anthropic-api-key \
  --workspace-id workspace_id
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

`$ ant beta:organization:workspaces archive`

**POST** `/v1/organizations/workspaces/{workspace_id}/archive`

Archive Workspace

#### Parameters

- `--workspace-id: string`

#### Returns

- `beta_workspace: object`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK integration guide for the
    required key configuration, including the value used during key validation.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: object`

    Data residency configuration.

    - `allowed_inference_geos: array of string or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `geos: array of string`

      - `unrestricted: "unrestricted"`

    - `default_inference_geo: string`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: string`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```bash
ant beta:organization:workspaces archive \
  --api-key my-anthropic-api-key \
  --workspace-id workspace_id
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

`$ ant beta:organization:workspaces:rate-limits list`

**GET** `/v1/organizations/workspaces/{workspace_id}/rate_limits`

List rate-limit overrides configured for a workspace.

Returns only the groups and limiter types that have a workspace-level
override. Groups without overrides inherit the organization limits and
are not listed; use `GET /v1/organizations/rate_limits` to see those.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `--workspace-id: string`

  The ID of the workspace.

- `--group-type: optional "batch" or "files" or "model_group" or 3 more`

  Filter by group type.

- `--limit: optional number`

  Maximum number of items to return per page. Ranges from `1` to `1000`.

  When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

  maximum: 1000, minimum: 1

- `--page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Returns

- `BetaWorkspaceRateLimitListResponse: object`

  - `data: array of BetaWorkspaceRateLimit`

    Rate-limit entries for the workspace, one per group that has at least one override.

    - `group_type: "batch" or "files" or "model_group" or 3 more`

      The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

      - `"batch"`

      - `"files"`

      - `"model_group"`

      - `"skills"`

      - `"token_count"`

      - `"web_search"`

    - `limits: array of BetaWorkspaceRateLimitValue`

      The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.

      - `org_limit: number`

        The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

      - `type: string`

        The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

      - `value: number`

        The workspace-level override value for this limiter type.

    - `models: array of string`

      Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

    - `rate_limit_id: string`

      The `id` of the RateLimit group this override applies to.

    - `type: "workspace_rate_limit"`

      Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

    - `workspace_id: string`

      ID of the Workspace this override applies to.

  - `next_page: string`

    Opaque cursor for the next page of results, or `null` when no entries remain beyond this response.

#### Example

```bash
ant beta:organization:workspaces:rate-limits list \
  --api-key my-anthropic-api-key \
  --workspace-id workspace_id
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

`$ ant beta:organization:workspaces:members list`

**GET** `/v1/organizations/workspaces/{workspace_id}/members`

List Workspace Members

#### Parameters

- `--workspace-id: string`

  ID of the Workspace.

- `--after-id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `--before-id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `--limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  maximum: 1000, minimum: 1

#### Returns

- `BetaListResponse_WorkspaceMemberSchema_: object`

  - `data: array of BetaWorkspaceMember`

    - `type: "workspace_member"`

      Object type.

      For Workspace Members, this is always `"workspace_member"`.

    - `user_id: string`

      ID of the User.

    - `workspace_id: string`

      ID of the Workspace.

    - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

      Role of the Workspace Member.

      - `"workspace_admin"`

      - `"workspace_billing"`

      - `"workspace_developer"`

      - `"workspace_restricted_developer"`

      - `"workspace_user"`

  - `first_id: string`

    First ID in the `data` list. Can be used as the `before_id` for the previous page.

  - `has_more: boolean`

    Indicates if there are more results in the requested page direction.

  - `last_id: string`

    Last ID in the `data` list. Can be used as the `after_id` for the next page.

#### Example

```bash
ant beta:organization:workspaces:members list \
  --api-key my-anthropic-api-key \
  --workspace-id workspace_id
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

`$ ant beta:organization:workspaces:members add`

**POST** `/v1/organizations/workspaces/{workspace_id}/members`

Create Workspace Member

#### Parameters

- `--workspace-id: string`

  ID of the Workspace.

- `--user-id: string`

  ID of the User.

- `--workspace-role: "workspace_admin" or "workspace_developer" or "workspace_restricted_developer" or "workspace_user"`

  Role of the new Workspace Member. Cannot be `workspace_billing`.

#### Returns

- `beta_workspace_member: object`

  - `type: "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the Workspace Member.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```bash
ant beta:organization:workspaces:members add \
  --api-key my-anthropic-api-key \
  --workspace-id workspace_id \
  --user-id user_01WCz1FkmYMm4gnmykNKUu3Q \
  --workspace-role workspace_admin
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

`$ ant beta:organization:workspaces:members retrieve`

**GET** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Get Workspace Member

#### Parameters

- `--workspace-id: string`

  ID of the Workspace.

- `--user-id: string`

  ID of the User.

#### Returns

- `beta_workspace_member: object`

  - `type: "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the Workspace Member.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```bash
ant beta:organization:workspaces:members retrieve \
  --api-key my-anthropic-api-key \
  --workspace-id workspace_id \
  --user-id user_id
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

`$ ant beta:organization:workspaces:members update`

**POST** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Update Workspace Member

#### Parameters

- `--workspace-id: string`

  Path param: ID of the Workspace.

- `--user-id: string`

  Path param: ID of the User.

- `--workspace-role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

  Body param: New workspace role for the User.

#### Returns

- `beta_workspace_member: object`

  - `type: "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the Workspace Member.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```bash
ant beta:organization:workspaces:members update \
  --api-key my-anthropic-api-key \
  --workspace-id workspace_id \
  --user-id user_id \
  --workspace-role workspace_admin
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

`$ ant beta:organization:workspaces:members remove`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Delete Workspace Member

#### Parameters

- `--workspace-id: string`

  ID of the Workspace.

- `--user-id: string`

  ID of the User.

#### Returns

- `BetaOrganizationWorkspaceMemberRemoveResponse: object`

  - `type: "workspace_member_deleted"`

    Deleted object type.

    For Workspace Members, this is always `"workspace_member_deleted"`.

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

#### Example

```bash
ant beta:organization:workspaces:members remove \
  --api-key my-anthropic-api-key \
  --workspace-id workspace_id \
  --user-id user_id
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

`$ ant beta:organization:workspaces:service-accounts list`

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

- `--workspace-id: string`

  Path param: ID of the workspace.

- `--limit: optional number`

  Query param: Number of results per page.

  maximum: 100, minimum: 1

- `--page: optional string`

  Query param: Opaque cursor from a previous response's `next_page`.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaServiceAccountWorkspaceMemberListResponse: object`

  - `data: array of BetaServiceAccountWorkspaceMember`

    - `created_by_actor_id: string`

      Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

    - `implicit: boolean`

      True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

    - `service_account_id: string`

      Tagged service account ID (`svac_...`).

    - `type: "service_account_workspace_member"`

    - `workspace_id: string`

      Tagged workspace ID (`wrkspc_...`).

    - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

      Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

      - `"workspace_admin"`

      - `"workspace_billing"`

      - `"workspace_developer"`

      - `"workspace_restricted_developer"`

      - `"workspace_user"`

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results.

#### Example

```bash
ant beta:organization:workspaces:service-accounts list \
  --api-key my-anthropic-api-key \
  --workspace-id workspace_id
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

`$ ant beta:organization:workspaces:service-accounts add`

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

- `--workspace-id: string`

  Path param: ID of the workspace.

- `--service-account-id: string`

  Body param: Tagged service account ID to add.

- `--workspace-role: "workspace_admin" or "workspace_developer" or "workspace_restricted_developer" or "workspace_user"`

  Body param: Role to assign to the service account in this workspace.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_service_account_workspace_member: object`

  - `created_by_actor_id: string`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```bash
ant beta:organization:workspaces:service-accounts add \
  --api-key my-anthropic-api-key \
  --workspace-id workspace_id \
  --service-account-id service_account_id \
  --workspace-role workspace_admin
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

`$ ant beta:organization:workspaces:service-accounts retrieve`

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

- `--workspace-id: string`

  Path param: ID of the workspace.

- `--service-account-id: string`

  Path param: ID of the service account.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_service_account_workspace_member: object`

  - `created_by_actor_id: string`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```bash
ant beta:organization:workspaces:service-accounts retrieve \
  --api-key my-anthropic-api-key \
  --workspace-id workspace_id \
  --service-account-id service_account_id
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

`$ ant beta:organization:workspaces:service-accounts update`

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

- `--workspace-id: string`

  Path param: ID of the workspace.

- `--service-account-id: string`

  Path param: ID of the service account.

- `--workspace-role: "workspace_admin" or "workspace_developer" or "workspace_restricted_developer" or "workspace_user"`

  Body param: New role for the service account in this workspace.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_service_account_workspace_member: object`

  - `created_by_actor_id: string`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```bash
ant beta:organization:workspaces:service-accounts update \
  --api-key my-anthropic-api-key \
  --workspace-id workspace_id \
  --service-account-id service_account_id \
  --workspace-role workspace_admin
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

`$ ant beta:organization:workspaces:service-accounts remove`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Remove a service account from a workspace.

Removal is idempotent (returns 200 even if the membership was already
removed). A DELETE against the implicit default-workspace membership
returns 200 but is a no-op and the membership persists; deleting an
explicit default-workspace row reverts to the implicit `workspace_user`
membership. Archived workspaces return 400.

#### Parameters

- `--workspace-id: string`

  Path param: ID of the workspace.

- `--service-account-id: string`

  Path param: ID of the service account.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaOrganizationWorkspaceServiceAccountRemoveResponse: object`

  - `service_account_id: string`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `type: "service_account_workspace_member_deleted"`

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```bash
ant beta:organization:workspaces:service-accounts remove \
  --api-key my-anthropic-api-key \
  --workspace-id workspace_id \
  --service-account-id service_account_id
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

`$ ant beta:organization:rate-limits list`

**GET** `/v1/organizations/rate_limits`

List Messages API rate limits for your organization.

Each entry corresponds to one rate-limit group (either a model family
or an API-surface category such as the Files API or Message Batches)
and contains the set of limiter values that apply to it.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `--group-type: optional "batch" or "files" or "model_group" or 3 more`

  Filter by group type.

- `--limit: optional number`

  Maximum number of items to return per page. Ranges from `1` to `1000`.

  When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

  maximum: 1000, minimum: 1

- `--model: optional string`

  Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

- `--page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Returns

- `BetaRateLimitListResponse: object`

  - `data: array of BetaOrganizationRateLimit`

    Rate-limit entries for the organization, one per group.

    - `id: string`

      Stable identifier for this rate-limit group within the organization.

    - `group_type: "batch" or "files" or "model_group" or 3 more`

      The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

      - `"batch"`

      - `"files"`

      - `"model_group"`

      - `"skills"`

      - `"token_count"`

      - `"web_search"`

    - `limits: array of BetaOrganizationRateLimitValue`

      The limiter values that apply to this group.

      - `type: string`

        The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

      - `value: number`

        The configured limit value for this limiter type.

    - `models: array of string`

      Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

    - `type: "rate_limit"`

      Object type. Always `rate_limit` for organization rate-limit entries.

  - `next_page: string`

    Opaque cursor for the next page of results, or `null` when no entries remain beyond this response.

#### Example

```bash
ant beta:organization:rate-limits list \
  --api-key my-anthropic-api-key
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
