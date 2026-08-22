<!-- source: https://platform.claude.com/docs/en/api/python/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/python/beta -->

<!-- chunk-start -->

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

- `class BetaManagedAgentsVault: …`

  A vault that stores credentials for use by agents during sessions.

  - `id: str`

    Unique identifier for the vault.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: str`

    Human-readable name for the vault.

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the vault.

  - `type: Literal["vault"]`

    - `"vault"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_vault = client.beta.vaults.create(
    display_name="Example vault",
)
print(beta_managed_agents_vault.id)
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## List Vaults

`beta.vaults.list(VaultListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsVault]`

**get** `/v1/vaults`

List Vaults

### Parameters

- `include_archived: Optional[bool]`

  Whether to include archived vaults in the results.

- `limit: Optional[int]`

  Maximum number of vaults to return per page. Defaults to 20, maximum 100.

- `page: Optional[str]`

  Opaque pagination token from a previous `list_vaults` response.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsVault: …`

  A vault that stores credentials for use by agents during sessions.

  - `id: str`

    Unique identifier for the vault.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: str`

    Human-readable name for the vault.

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the vault.

  - `type: Literal["vault"]`

    - `"vault"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.vaults.list()
page = page.data[0]
print(page.id)
```

#### Response

```json
{
  "data": [
    {
      "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "display_name": "Example vault",
      "metadata": {
        "environment": "production"
      },
      "type": "vault",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Vault

`beta.vaults.retrieve(strvault_id, VaultRetrieveParams**kwargs)  -> BetaManagedAgentsVault`

**get** `/v1/vaults/{vault_id}`

Get Vault

### Parameters

- `vault_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsVault: …`

  A vault that stores credentials for use by agents during sessions.

  - `id: str`

    Unique identifier for the vault.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: str`

    Human-readable name for the vault.

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the vault.

  - `type: Literal["vault"]`

    - `"vault"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_vault = client.beta.vaults.retrieve(
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_vault.id)
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Update Vault

`beta.vaults.update(strvault_id, VaultUpdateParams**kwargs)  -> BetaManagedAgentsVault`

**post** `/v1/vaults/{vault_id}`

Update Vault

### Parameters

- `vault_id: str`

- `display_name: Optional[str]`

  Updated human-readable name for the vault. 1-255 characters.

- `metadata: Optional[Dict[str, Optional[str]]]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsVault: …`

  A vault that stores credentials for use by agents during sessions.

  - `id: str`

    Unique identifier for the vault.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: str`

    Human-readable name for the vault.

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the vault.

  - `type: Literal["vault"]`

    - `"vault"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_vault = client.beta.vaults.update(
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_vault.id)
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Delete Vault

`beta.vaults.delete(strvault_id, VaultDeleteParams**kwargs)  -> BetaManagedAgentsDeletedVault`

**delete** `/v1/vaults/{vault_id}`

Delete Vault

### Parameters

- `vault_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsDeletedVault: …`

  Confirmation of a deleted vault.

  - `id: str`

    Unique identifier of the deleted vault.

  - `type: Literal["vault_deleted"]`

    - `"vault_deleted"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_deleted_vault = client.beta.vaults.delete(
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_deleted_vault.id)
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

## Archive Vault

`beta.vaults.archive(strvault_id, VaultArchiveParams**kwargs)  -> BetaManagedAgentsVault`

**post** `/v1/vaults/{vault_id}/archive`

Archive Vault

### Parameters

- `vault_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsVault: …`

  A vault that stores credentials for use by agents during sessions.

  - `id: str`

    Unique identifier for the vault.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: str`

    Human-readable name for the vault.

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the vault.

  - `type: Literal["vault"]`

    - `"vault"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_vault = client.beta.vaults.archive(
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_vault.id)
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Domain Types

### Beta Managed Agents Deleted Vault

- `class BetaManagedAgentsDeletedVault: …`

  Confirmation of a deleted vault.

  - `id: str`

    Unique identifier of the deleted vault.

  - `type: Literal["vault_deleted"]`

    - `"vault_deleted"`

### Beta Managed Agents Vault

- `class BetaManagedAgentsVault: …`

  A vault that stores credentials for use by agents during sessions.

  - `id: str`

    Unique identifier for the vault.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: str`

    Human-readable name for the vault.

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the vault.

  - `type: Literal["vault"]`

    - `"vault"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

# Credentials

## Create Credential

`beta.vaults.credentials.create(strvault_id, CredentialCreateParams**kwargs)  -> BetaManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials`

Create Credential

### Parameters

- `vault_id: str`

- `auth: Auth`

  Authentication details for creating a credential.

  - `class BetaManagedAgentsMCPOAuthCreateParams: …`

    Parameters for creating an MCP OAuth credential.

    - `access_token: str`

      OAuth access token.

    - `mcp_server_url: str`

      URL of the MCP server this credential authenticates against.

    - `type: Literal["mcp_oauth"]`

      - `"mcp_oauth"`

    - `expires_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `refresh: Optional[BetaManagedAgentsMCPOAuthRefreshParams]`

      OAuth refresh token parameters for creating a credential with refresh support.

      - `client_id: str`

        OAuth client ID.

      - `refresh_token: str`

        OAuth refresh token.

      - `token_endpoint: str`

        Token endpoint URL used to refresh the access token.

      - `token_endpoint_auth: TokenEndpointAuth`

        Token endpoint requires no client authentication.

        - `class BetaManagedAgentsTokenEndpointAuthNoneParam: …`

          Token endpoint requires no client authentication.

          - `type: Literal["none"]`

            - `"none"`

        - `class BetaManagedAgentsTokenEndpointAuthBasicParam: …`

          Token endpoint uses HTTP Basic authentication with client credentials.

          - `client_secret: str`

            OAuth client secret.

          - `type: Literal["client_secret_basic"]`

            - `"client_secret_basic"`

        - `class BetaManagedAgentsTokenEndpointAuthPostParam: …`

          Token endpoint uses POST body authentication with client credentials.

          - `client_secret: str`

            OAuth client secret.

          - `type: Literal["client_secret_post"]`

            - `"client_secret_post"`

      - `resource: Optional[str]`

        OAuth resource indicator.

      - `scope: Optional[str]`

        OAuth scope for the refresh request.

  - `class BetaManagedAgentsStaticBearerCreateParams: …`

    Parameters for creating a static bearer token credential.

    - `token: str`

      Static bearer token value.

    - `mcp_server_url: str`

      URL of the MCP server this credential authenticates against.

    - `type: Literal["static_bearer"]`

      - `"static_bearer"`

  - `class BetaManagedAgentsEnvironmentVariableCreateParams: …`

    Parameters for creating an environment variable credential.

    - `networking: BetaManagedAgentsCredentialNetworkingParams`

      Outbound hosts the secret value is substituted on.

      - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams: …`

        Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

        - `type: Literal["unrestricted"]`

          - `"unrestricted"`

      - `class BetaManagedAgentsLimitedCredentialNetworkingParams: …`

        Substitute the secret only on requests to the listed hosts.

        - `allowed_hosts: List[str]`

          Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

        - `type: Literal["limited"]`

          - `"limited"`

    - `secret_name: str`

      Name of the environment variable. Immutable after create.

    - `secret_value: str`

      Secret value. Write-only; never returned in responses.

    - `type: Literal["environment_variable"]`

      - `"environment_variable"`

    - `injection_location: Optional[BetaManagedAgentsInjectionLocationParams]`

      Where in the outbound request the secret value may be substituted.

      - `body: Optional[bool]`

        Substitute when the placeholder appears in the request body.

      - `header: Optional[bool]`

        Substitute when the placeholder appears in a request header value.

- `display_name: Optional[str]`

  Human-readable name for the credential. Up to 255 characters.

- `metadata: Optional[Dict[str, str]]`

  Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsCredential: …`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: str`

    Unique identifier for the credential.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `auth: Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse: …`

      OAuth credential details for an MCP server.

      - `mcp_server_url: str`

        URL of the MCP server this credential authenticates against.

      - `type: Literal["mcp_oauth"]`

        - `"mcp_oauth"`

      - `expires_at: Optional[datetime]`

        A timestamp in RFC 3339 format

      - `refresh: Optional[BetaManagedAgentsMCPOAuthRefreshResponse]`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: str`

          OAuth client ID.

        - `token_endpoint: str`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: TokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse: …`

            Token endpoint requires no client authentication.

            - `type: Literal["none"]`

              - `"none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse: …`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: Literal["client_secret_basic"]`

              - `"client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse: …`

            Token endpoint uses POST body authentication with client credentials.

            - `type: Literal["client_secret_post"]`

              - `"client_secret_post"`

        - `resource: Optional[str]`

          OAuth resource indicator.

        - `scope: Optional[str]`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse: …`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: str`

        URL of the MCP server this credential authenticates against.

      - `type: Literal["static_bearer"]`

        - `"static_bearer"`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse: …`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: bool`

          Whether the placeholder is substituted in the request body.

        - `header: bool`

          Whether the placeholder is substituted in request header values.

      - `networking: Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse: …`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: Literal["unrestricted"]`

            - `"unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse: …`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: List[str]`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: Literal["limited"]`

            - `"limited"`

      - `secret_name: str`

        Name of the environment variable.

      - `type: Literal["environment_variable"]`

        - `"environment_variable"`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the credential.

  - `type: Literal["vault_credential"]`

    - `"vault_credential"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_id: str`

    Identifier of the vault this credential belongs to.

  - `display_name: Optional[str]`

    Human-readable name for the credential.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_credential = client.beta.vaults.credentials.create(
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
    auth={
        "token": "bearer_exampletoken",
        "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
        "type": "static_bearer",
    },
)
print(beta_managed_agents_credential.id)
```

#### Response

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

## List Credentials

`beta.vaults.credentials.list(strvault_id, CredentialListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsCredential]`

**get** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Parameters

- `vault_id: str`

- `include_archived: Optional[bool]`

  Whether to include archived credentials in the results.

- `limit: Optional[int]`

  Maximum number of credentials to return per page. Defaults to 20, maximum 100.

- `page: Optional[str]`

  Opaque pagination token from a previous `list_credentials` response.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsCredential: …`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: str`

    Unique identifier for the credential.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `auth: Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse: …`

      OAuth credential details for an MCP server.

      - `mcp_server_url: str`

        URL of the MCP server this credential authenticates against.

      - `type: Literal["mcp_oauth"]`

        - `"mcp_oauth"`

      - `expires_at: Optional[datetime]`

        A timestamp in RFC 3339 format

      - `refresh: Optional[BetaManagedAgentsMCPOAuthRefreshResponse]`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: str`

          OAuth client ID.

        - `token_endpoint: str`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: TokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse: …`

            Token endpoint requires no client authentication.

            - `type: Literal["none"]`

              - `"none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse: …`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: Literal["client_secret_basic"]`

              - `"client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse: …`

            Token endpoint uses POST body authentication with client credentials.

            - `type: Literal["client_secret_post"]`

              - `"client_secret_post"`

        - `resource: Optional[str]`

          OAuth resource indicator.

        - `scope: Optional[str]`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse: …`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: str`

        URL of the MCP server this credential authenticates against.

      - `type: Literal["static_bearer"]`

        - `"static_bearer"`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse: …`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: bool`

          Whether the placeholder is substituted in the request body.

        - `header: bool`

          Whether the placeholder is substituted in request header values.

      - `networking: Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse: …`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: Literal["unrestricted"]`

            - `"unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse: …`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: List[str]`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: Literal["limited"]`

            - `"limited"`

      - `secret_name: str`

        Name of the environment variable.

      - `type: Literal["environment_variable"]`

        - `"environment_variable"`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the credential.

  - `type: Literal["vault_credential"]`

    - `"vault_credential"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_id: str`

    Identifier of the vault this credential belongs to.

  - `display_name: Optional[str]`

    Human-readable name for the credential.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.vaults.credentials.list(
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
page = page.data[0]
print(page.id)
```

#### Response

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

## Get Credential

`beta.vaults.credentials.retrieve(strcredential_id, CredentialRetrieveParams**kwargs)  -> BetaManagedAgentsCredential`

**get** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

### Parameters

- `vault_id: str`

- `credential_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsCredential: …`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: str`

    Unique identifier for the credential.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `auth: Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse: …`

      OAuth credential details for an MCP server.

      - `mcp_server_url: str`

        URL of the MCP server this credential authenticates against.

      - `type: Literal["mcp_oauth"]`

        - `"mcp_oauth"`

      - `expires_at: Optional[datetime]`

        A timestamp in RFC 3339 format

      - `refresh: Optional[BetaManagedAgentsMCPOAuthRefreshResponse]`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: str`

          OAuth client ID.

        - `token_endpoint: str`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: TokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse: …`

            Token endpoint requires no client authentication.

            - `type: Literal["none"]`

              - `"none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse: …`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: Literal["client_secret_basic"]`

              - `"client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse: …`

            Token endpoint uses POST body authentication with client credentials.

            - `type: Literal["client_secret_post"]`

              - `"client_secret_post"`

        - `resource: Optional[str]`

          OAuth resource indicator.

        - `scope: Optional[str]`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse: …`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: str`

        URL of the MCP server this credential authenticates against.

      - `type: Literal["static_bearer"]`

        - `"static_bearer"`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse: …`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: bool`

          Whether the placeholder is substituted in the request body.

        - `header: bool`

          Whether the placeholder is substituted in request header values.

      - `networking: Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse: …`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: Literal["unrestricted"]`

            - `"unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse: …`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: List[str]`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: Literal["limited"]`

            - `"limited"`

      - `secret_name: str`

        Name of the environment variable.

      - `type: Literal["environment_variable"]`

        - `"environment_variable"`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the credential.

  - `type: Literal["vault_credential"]`

    - `"vault_credential"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_id: str`

    Identifier of the vault this credential belongs to.

  - `display_name: Optional[str]`

    Human-readable name for the credential.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_credential = client.beta.vaults.credentials.retrieve(
    credential_id="vcrd_011CZkZEMt8gZan2iYOQfSkw",
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_credential.id)
```

#### Response

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

## Update Credential

`beta.vaults.credentials.update(strcredential_id, CredentialUpdateParams**kwargs)  -> BetaManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Parameters

- `vault_id: str`

- `credential_id: str`

- `auth: Optional[Auth]`

  Updated authentication details for a credential.

  - `class BetaManagedAgentsMCPOAuthUpdateParams: …`

    Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

    - `type: Literal["mcp_oauth"]`

      - `"mcp_oauth"`

    - `access_token: Optional[str]`

      Updated OAuth access token.

    - `expires_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `refresh: Optional[BetaManagedAgentsMCPOAuthRefreshUpdateParams]`

      Parameters for updating OAuth refresh token configuration.

      - `refresh_token: Optional[str]`

        Updated OAuth refresh token.

      - `scope: Optional[str]`

        Updated OAuth scope for the refresh request.

      - `token_endpoint_auth: Optional[TokenEndpointAuth]`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam: …`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `type: Literal["client_secret_basic"]`

            - `"client_secret_basic"`

          - `client_secret: Optional[str]`

            Updated OAuth client secret.

        - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam: …`

          Updated POST body authentication parameters for the token endpoint.

          - `type: Literal["client_secret_post"]`

            - `"client_secret_post"`

          - `client_secret: Optional[str]`

            Updated OAuth client secret.

  - `class BetaManagedAgentsStaticBearerUpdateParams: …`

    Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

    - `type: Literal["static_bearer"]`

      - `"static_bearer"`

    - `token: Optional[str]`

      Updated static bearer token value.

  - `class BetaManagedAgentsEnvironmentVariableUpdateParams: …`

    Parameters for updating an environment variable credential. `secret_name` is immutable.

    - `type: Literal["environment_variable"]`

      - `"environment_variable"`

    - `injection_location: Optional[BetaManagedAgentsInjectionLocationUpdateParams]`

      Updated injection location.

      - `body: Optional[bool]`

        Substitute when the placeholder appears in the request body.

      - `header: Optional[bool]`

        Substitute when the placeholder appears in a request header value.

    - `networking: Optional[BetaManagedAgentsCredentialNetworkingParams]`

      Updated networking scope. Full replacement.

      - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams: …`

        Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

        - `type: Literal["unrestricted"]`

          - `"unrestricted"`

      - `class BetaManagedAgentsLimitedCredentialNetworkingParams: …`

        Substitute the secret only on requests to the listed hosts.

        - `allowed_hosts: List[str]`

          Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

        - `type: Literal["limited"]`

          - `"limited"`

    - `secret_value: Optional[str]`

      Updated secret value.

- `display_name: Optional[str]`

  Updated human-readable name for the credential. 1-255 characters.

- `metadata: Optional[Dict[str, Optional[str]]]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsCredential: …`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: str`

    Unique identifier for the credential.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `auth: Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse: …`

      OAuth credential details for an MCP server.

      - `mcp_server_url: str`

        URL of the MCP server this credential authenticates against.

      - `type: Literal["mcp_oauth"]`

        - `"mcp_oauth"`

      - `expires_at: Optional[datetime]`

        A timestamp in RFC 3339 format

      - `refresh: Optional[BetaManagedAgentsMCPOAuthRefreshResponse]`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: str`

          OAuth client ID.

        - `token_endpoint: str`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: TokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse: …`

            Token endpoint requires no client authentication.

            - `type: Literal["none"]`

              - `"none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse: …`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: Literal["client_secret_basic"]`

              - `"client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse: …`

            Token endpoint uses POST body authentication with client credentials.

            - `type: Literal["client_secret_post"]`

              - `"client_secret_post"`

        - `resource: Optional[str]`

          OAuth resource indicator.

        - `scope: Optional[str]`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse: …`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: str`

        URL of the MCP server this credential authenticates against.

      - `type: Literal["static_bearer"]`

        - `"static_bearer"`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse: …`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: bool`

          Whether the placeholder is substituted in the request body.

        - `header: bool`

          Whether the placeholder is substituted in request header values.

      - `networking: Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse: …`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: Literal["unrestricted"]`

            - `"unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse: …`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: List[str]`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: Literal["limited"]`

            - `"limited"`

      - `secret_name: str`

        Name of the environment variable.

      - `type: Literal["environment_variable"]`

        - `"environment_variable"`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the credential.

  - `type: Literal["vault_credential"]`

    - `"vault_credential"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_id: str`

    Identifier of the vault this credential belongs to.

  - `display_name: Optional[str]`

    Human-readable name for the credential.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_credential = client.beta.vaults.credentials.update(
    credential_id="vcrd_011CZkZEMt8gZan2iYOQfSkw",
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_credential.id)
```

#### Response

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

## Delete Credential

`beta.vaults.credentials.delete(strcredential_id, CredentialDeleteParams**kwargs)  -> BetaManagedAgentsDeletedCredential`

**delete** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

### Parameters

- `vault_id: str`

- `credential_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsDeletedCredential: …`

  Confirmation of a deleted credential.

  - `id: str`

    Unique identifier of the deleted credential.

  - `type: Literal["vault_credential_deleted"]`

    - `"vault_credential_deleted"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_deleted_credential = client.beta.vaults.credentials.delete(
    credential_id="vcrd_011CZkZEMt8gZan2iYOQfSkw",
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_deleted_credential.id)
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

## Archive Credential

`beta.vaults.credentials.archive(strcredential_id, CredentialArchiveParams**kwargs)  -> BetaManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

### Parameters

- `vault_id: str`

- `credential_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsCredential: …`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: str`

    Unique identifier for the credential.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `auth: Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse: …`

      OAuth credential details for an MCP server.

      - `mcp_server_url: str`

        URL of the MCP server this credential authenticates against.

      - `type: Literal["mcp_oauth"]`

        - `"mcp_oauth"`

      - `expires_at: Optional[datetime]`

        A timestamp in RFC 3339 format

      - `refresh: Optional[BetaManagedAgentsMCPOAuthRefreshResponse]`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: str`

          OAuth client ID.

        - `token_endpoint: str`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: TokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse: …`

            Token endpoint requires no client authentication.

            - `type: Literal["none"]`

              - `"none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse: …`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: Literal["client_secret_basic"]`

              - `"client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse: …`

            Token endpoint uses POST body authentication with client credentials.

            - `type: Literal["client_secret_post"]`

              - `"client_secret_post"`

        - `resource: Optional[str]`

          OAuth resource indicator.

        - `scope: Optional[str]`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse: …`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: str`

        URL of the MCP server this credential authenticates against.

      - `type: Literal["static_bearer"]`

        - `"static_bearer"`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse: …`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: bool`

          Whether the placeholder is substituted in the request body.

        - `header: bool`

          Whether the placeholder is substituted in request header values.

      - `networking: Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse: …`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: Literal["unrestricted"]`

            - `"unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse: …`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: List[str]`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: Literal["limited"]`

            - `"limited"`

      - `secret_name: str`

        Name of the environment variable.

      - `type: Literal["environment_variable"]`

        - `"environment_variable"`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the credential.

  - `type: Literal["vault_credential"]`

    - `"vault_credential"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_id: str`

    Identifier of the vault this credential belongs to.

  - `display_name: Optional[str]`

    Human-readable name for the credential.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_credential = client.beta.vaults.credentials.archive(
    credential_id="vcrd_011CZkZEMt8gZan2iYOQfSkw",
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_credential.id)
```

#### Response

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

## Validate Credential

`beta.vaults.credentials.mcp_oauth_validate(strcredential_id, CredentialMCPOAuthValidateParams**kwargs)  -> BetaManagedAgentsCredentialValidation`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

### Parameters

- `vault_id: str`

- `credential_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsCredentialValidation: …`

  Result of live-probing a credential against its configured MCP server.

  - `credential_id: str`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: bool`

    Whether the credential has a refresh token configured.

  - `mcp_probe: Optional[BetaManagedAgentsMCPProbe]`

    The failing step of an MCP validation probe.

    - `http_response: Optional[BetaManagedAgentsRefreshHTTPResponse]`

      An HTTP response captured during a credential validation probe.

      - `body: str`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: bool`

        Whether `body` was truncated.

      - `content_type: str`

        Value of the `Content-Type` response header.

      - `status_code: int`

        HTTP status code.

    - `method: str`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `refresh: Optional[BetaManagedAgentsRefreshObject]`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `http_response: Optional[BetaManagedAgentsRefreshHTTPResponse]`

      An HTTP response captured during a credential validation probe.

    - `status: Literal["succeeded", "failed", "connect_error", "no_refresh_token"]`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `"succeeded"`

      - `"failed"`

      - `"connect_error"`

      - `"no_refresh_token"`

  - `status: BetaManagedAgentsCredentialValidationStatus`

    Overall verdict of a credential validation probe.

    - `"valid"`

    - `"invalid"`

    - `"unknown"`

  - `type: Literal["vault_credential_validation"]`

    - `"vault_credential_validation"`

  - `validated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_id: str`

    Identifier of the vault containing the credential.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_credential_validation = (
    client.beta.vaults.credentials.mcp_oauth_validate(
        credential_id="vcrd_011CZkZEMt8gZan2iYOQfSkw",
        vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
    )
)
print(beta_managed_agents_credential_validation.credential_id)
```

#### Response

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

## Domain Types

### Beta Managed Agents Credential

- `class BetaManagedAgentsCredential: …`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: str`

    Unique identifier for the credential.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `auth: Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse: …`

      OAuth credential details for an MCP server.

      - `mcp_server_url: str`

        URL of the MCP server this credential authenticates against.

      - `type: Literal["mcp_oauth"]`

        - `"mcp_oauth"`

      - `expires_at: Optional[datetime]`

        A timestamp in RFC 3339 format

      - `refresh: Optional[BetaManagedAgentsMCPOAuthRefreshResponse]`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: str`

          OAuth client ID.

        - `token_endpoint: str`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: TokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse: …`

            Token endpoint requires no client authentication.

            - `type: Literal["none"]`

              - `"none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse: …`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: Literal["client_secret_basic"]`

              - `"client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse: …`

            Token endpoint uses POST body authentication with client credentials.

            - `type: Literal["client_secret_post"]`

              - `"client_secret_post"`

        - `resource: Optional[str]`

          OAuth resource indicator.

        - `scope: Optional[str]`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse: …`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: str`

        URL of the MCP server this credential authenticates against.

      - `type: Literal["static_bearer"]`

        - `"static_bearer"`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse: …`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: bool`

          Whether the placeholder is substituted in the request body.

        - `header: bool`

          Whether the placeholder is substituted in request header values.

      - `networking: Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse: …`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: Literal["unrestricted"]`

            - `"unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse: …`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: List[str]`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: Literal["limited"]`

            - `"limited"`

      - `secret_name: str`

        Name of the environment variable.

      - `type: Literal["environment_variable"]`

        - `"environment_variable"`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the credential.

  - `type: Literal["vault_credential"]`

    - `"vault_credential"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_id: str`

    Identifier of the vault this credential belongs to.

  - `display_name: Optional[str]`

    Human-readable name for the credential.

### Beta Managed Agents Credential Networking Params

- `BetaManagedAgentsCredentialNetworkingParams`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams: …`

    Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

    - `type: Literal["unrestricted"]`

      - `"unrestricted"`

  - `class BetaManagedAgentsLimitedCredentialNetworkingParams: …`

    Substitute the secret only on requests to the listed hosts.

    - `allowed_hosts: List[str]`

      Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

    - `type: Literal["limited"]`

      - `"limited"`

### Beta Managed Agents Credential Validation

- `class BetaManagedAgentsCredentialValidation: …`

  Result of live-probing a credential against its configured MCP server.

  - `credential_id: str`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: bool`

    Whether the credential has a refresh token configured.

  - `mcp_probe: Optional[BetaManagedAgentsMCPProbe]`

    The failing step of an MCP validation probe.

    - `http_response: Optional[BetaManagedAgentsRefreshHTTPResponse]`

      An HTTP response captured during a credential validation probe.

      - `body: str`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: bool`

        Whether `body` was truncated.

      - `content_type: str`

        Value of the `Content-Type` response header.

      - `status_code: int`

        HTTP status code.

    - `method: str`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `refresh: Optional[BetaManagedAgentsRefreshObject]`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `http_response: Optional[BetaManagedAgentsRefreshHTTPResponse]`

      An HTTP response captured during a credential validation probe.

    - `status: Literal["succeeded", "failed", "connect_error", "no_refresh_token"]`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `"succeeded"`

      - `"failed"`

      - `"connect_error"`

      - `"no_refresh_token"`

  - `status: BetaManagedAgentsCredentialValidationStatus`

    Overall verdict of a credential validation probe.

    - `"valid"`

    - `"invalid"`

    - `"unknown"`

  - `type: Literal["vault_credential_validation"]`

    - `"vault_credential_validation"`

  - `validated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_id: str`

    Identifier of the vault containing the credential.

### Beta Managed Agents Credential Validation Status

- `Literal["valid", "invalid", "unknown"]`

  Overall verdict of a credential validation probe.

  - `"valid"`

  - `"invalid"`

  - `"unknown"`

### Beta Managed Agents Deleted Credential

- `class BetaManagedAgentsDeletedCredential: …`

  Confirmation of a deleted credential.

  - `id: str`

    Unique identifier of the deleted credential.

  - `type: Literal["vault_credential_deleted"]`

    - `"vault_credential_deleted"`

### Beta Managed Agents Environment Variable Auth Response

- `class BetaManagedAgentsEnvironmentVariableAuthResponse: …`

  Environment variable credential details. The secret value is never returned.

  - `injection_location: BetaManagedAgentsInjectionLocationResponse`

    Where in the outbound request the secret value is substituted.

    - `body: bool`

      Whether the placeholder is substituted in the request body.

    - `header: bool`

      Whether the placeholder is substituted in request header values.

  - `networking: Networking`

    Outbound hosts the secret value is substituted on.

    - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse: …`

      The secret is substituted on any host the session's Environment network policy permits egress to.

      - `type: Literal["unrestricted"]`

        - `"unrestricted"`

    - `class BetaManagedAgentsLimitedCredentialNetworkingResponse: …`

      The secret is substituted only on requests to the listed hosts.

      - `allowed_hosts: List[str]`

        Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

      - `type: Literal["limited"]`

        - `"limited"`

  - `secret_name: str`

    Name of the environment variable.

  - `type: Literal["environment_variable"]`

    - `"environment_variable"`

### Beta Managed Agents Environment Variable Create Params

- `class BetaManagedAgentsEnvironmentVariableCreateParams: …`

  Parameters for creating an environment variable credential.

  - `networking: BetaManagedAgentsCredentialNetworkingParams`

    Outbound hosts the secret value is substituted on.

    - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams: …`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `type: Literal["unrestricted"]`

        - `"unrestricted"`

    - `class BetaManagedAgentsLimitedCredentialNetworkingParams: …`

      Substitute the secret only on requests to the listed hosts.

      - `allowed_hosts: List[str]`

        Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

      - `type: Literal["limited"]`

        - `"limited"`

  - `secret_name: str`

    Name of the environment variable. Immutable after create.

  - `secret_value: str`

    Secret value. Write-only; never returned in responses.

  - `type: Literal["environment_variable"]`

    - `"environment_variable"`

  - `injection_location: Optional[BetaManagedAgentsInjectionLocationParams]`

    Where in the outbound request the secret value may be substituted.

    - `body: Optional[bool]`

      Substitute when the placeholder appears in the request body.

    - `header: Optional[bool]`

      Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Environment Variable Update Params

- `class BetaManagedAgentsEnvironmentVariableUpdateParams: …`

  Parameters for updating an environment variable credential. `secret_name` is immutable.

  - `type: Literal["environment_variable"]`

    - `"environment_variable"`

  - `injection_location: Optional[BetaManagedAgentsInjectionLocationUpdateParams]`

    Updated injection location.

    - `body: Optional[bool]`

      Substitute when the placeholder appears in the request body.

    - `header: Optional[bool]`

      Substitute when the placeholder appears in a request header value.

  - `networking: Optional[BetaManagedAgentsCredentialNetworkingParams]`

    Updated networking scope. Full replacement.

    - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams: …`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `type: Literal["unrestricted"]`

        - `"unrestricted"`

    - `class BetaManagedAgentsLimitedCredentialNetworkingParams: …`

      Substitute the secret only on requests to the listed hosts.

      - `allowed_hosts: List[str]`

        Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

      - `type: Literal["limited"]`

        - `"limited"`

  - `secret_value: Optional[str]`

    Updated secret value.

### Beta Managed Agents Injection Location Params

- `class BetaManagedAgentsInjectionLocationParams: …`

  Where in the outbound request the secret value may be substituted.

  - `body: Optional[bool]`

    Substitute when the placeholder appears in the request body.

  - `header: Optional[bool]`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Injection Location Response

- `class BetaManagedAgentsInjectionLocationResponse: …`

  Where in the outbound request the secret value is substituted.

  - `body: bool`

    Whether the placeholder is substituted in the request body.

  - `header: bool`

    Whether the placeholder is substituted in request header values.

### Beta Managed Agents Injection Location Update Params

- `class BetaManagedAgentsInjectionLocationUpdateParams: …`

  Updated injection location.

  - `body: Optional[bool]`

    Substitute when the placeholder appears in the request body.

  - `header: Optional[bool]`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Limited Credential Networking Params

- `class BetaManagedAgentsLimitedCredentialNetworkingParams: …`

  Substitute the secret only on requests to the listed hosts.

  - `allowed_hosts: List[str]`

    Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

  - `type: Literal["limited"]`

    - `"limited"`

### Beta Managed Agents Limited Credential Networking Response

- `class BetaManagedAgentsLimitedCredentialNetworkingResponse: …`

  The secret is substituted only on requests to the listed hosts.

  - `allowed_hosts: List[str]`

    Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

  - `type: Literal["limited"]`

    - `"limited"`

### Beta Managed Agents MCP OAuth Auth Response

- `class BetaManagedAgentsMCPOAuthAuthResponse: …`

  OAuth credential details for an MCP server.

  - `mcp_server_url: str`

    URL of the MCP server this credential authenticates against.

  - `type: Literal["mcp_oauth"]`

    - `"mcp_oauth"`

  - `expires_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `refresh: Optional[BetaManagedAgentsMCPOAuthRefreshResponse]`

    OAuth refresh token configuration returned in credential responses.

    - `client_id: str`

      OAuth client ID.

    - `token_endpoint: str`

      Token endpoint URL used to refresh the access token.

    - `token_endpoint_auth: TokenEndpointAuth`

      Token endpoint requires no client authentication.

      - `class BetaManagedAgentsTokenEndpointAuthNoneResponse: …`

        Token endpoint requires no client authentication.

        - `type: Literal["none"]`

          - `"none"`

      - `class BetaManagedAgentsTokenEndpointAuthBasicResponse: …`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `type: Literal["client_secret_basic"]`

          - `"client_secret_basic"`

      - `class BetaManagedAgentsTokenEndpointAuthPostResponse: …`

        Token endpoint uses POST body authentication with client credentials.

        - `type: Literal["client_secret_post"]`

          - `"client_secret_post"`

    - `resource: Optional[str]`

      OAuth resource indicator.

    - `scope: Optional[str]`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Create Params

- `class BetaManagedAgentsMCPOAuthCreateParams: …`

  Parameters for creating an MCP OAuth credential.

  - `access_token: str`

    OAuth access token.

  - `mcp_server_url: str`

    URL of the MCP server this credential authenticates against.

  - `type: Literal["mcp_oauth"]`

    - `"mcp_oauth"`

  - `expires_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `refresh: Optional[BetaManagedAgentsMCPOAuthRefreshParams]`

    OAuth refresh token parameters for creating a credential with refresh support.

    - `client_id: str`

      OAuth client ID.

    - `refresh_token: str`

      OAuth refresh token.

    - `token_endpoint: str`

      Token endpoint URL used to refresh the access token.

    - `token_endpoint_auth: TokenEndpointAuth`

      Token endpoint requires no client authentication.

      - `class BetaManagedAgentsTokenEndpointAuthNoneParam: …`

        Token endpoint requires no client authentication.

        - `type: Literal["none"]`

          - `"none"`

      - `class BetaManagedAgentsTokenEndpointAuthBasicParam: …`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `client_secret: str`

          OAuth client secret.

        - `type: Literal["client_secret_basic"]`

          - `"client_secret_basic"`

      - `class BetaManagedAgentsTokenEndpointAuthPostParam: …`

        Token endpoint uses POST body authentication with client credentials.

        - `client_secret: str`

          OAuth client secret.

        - `type: Literal["client_secret_post"]`

          - `"client_secret_post"`

    - `resource: Optional[str]`

      OAuth resource indicator.

    - `scope: Optional[str]`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Params

- `class BetaManagedAgentsMCPOAuthRefreshParams: …`

  OAuth refresh token parameters for creating a credential with refresh support.

  - `client_id: str`

    OAuth client ID.

  - `refresh_token: str`

    OAuth refresh token.

  - `token_endpoint: str`

    Token endpoint URL used to refresh the access token.

  - `token_endpoint_auth: TokenEndpointAuth`

    Token endpoint requires no client authentication.

    - `class BetaManagedAgentsTokenEndpointAuthNoneParam: …`

      Token endpoint requires no client authentication.

      - `type: Literal["none"]`

        - `"none"`

    - `class BetaManagedAgentsTokenEndpointAuthBasicParam: …`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `client_secret: str`

        OAuth client secret.

      - `type: Literal["client_secret_basic"]`

        - `"client_secret_basic"`

    - `class BetaManagedAgentsTokenEndpointAuthPostParam: …`

      Token endpoint uses POST body authentication with client credentials.

      - `client_secret: str`

        OAuth client secret.

      - `type: Literal["client_secret_post"]`

        - `"client_secret_post"`

  - `resource: Optional[str]`

    OAuth resource indicator.

  - `scope: Optional[str]`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Response

- `class BetaManagedAgentsMCPOAuthRefreshResponse: …`

  OAuth refresh token configuration returned in credential responses.

  - `client_id: str`

    OAuth client ID.

  - `token_endpoint: str`

    Token endpoint URL used to refresh the access token.

  - `token_endpoint_auth: TokenEndpointAuth`

    Token endpoint requires no client authentication.

    - `class BetaManagedAgentsTokenEndpointAuthNoneResponse: …`

      Token endpoint requires no client authentication.

      - `type: Literal["none"]`

        - `"none"`

    - `class BetaManagedAgentsTokenEndpointAuthBasicResponse: …`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `type: Literal["client_secret_basic"]`

        - `"client_secret_basic"`

    - `class BetaManagedAgentsTokenEndpointAuthPostResponse: …`

      Token endpoint uses POST body authentication with client credentials.

      - `type: Literal["client_secret_post"]`

        - `"client_secret_post"`

  - `resource: Optional[str]`

    OAuth resource indicator.

  - `scope: Optional[str]`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Update Params

- `class BetaManagedAgentsMCPOAuthRefreshUpdateParams: …`

  Parameters for updating OAuth refresh token configuration.

  - `refresh_token: Optional[str]`

    Updated OAuth refresh token.

  - `scope: Optional[str]`

    Updated OAuth scope for the refresh request.

  - `token_endpoint_auth: Optional[TokenEndpointAuth]`

    Updated HTTP Basic authentication parameters for the token endpoint.

    - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam: …`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `type: Literal["client_secret_basic"]`

        - `"client_secret_basic"`

      - `client_secret: Optional[str]`

        Updated OAuth client secret.

    - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam: …`

      Updated POST body authentication parameters for the token endpoint.

      - `type: Literal["client_secret_post"]`

        - `"client_secret_post"`

      - `client_secret: Optional[str]`

        Updated OAuth client secret.

### Beta Managed Agents MCP OAuth Update Params

- `class BetaManagedAgentsMCPOAuthUpdateParams: …`

  Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

  - `type: Literal["mcp_oauth"]`

    - `"mcp_oauth"`

  - `access_token: Optional[str]`

    Updated OAuth access token.

  - `expires_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `refresh: Optional[BetaManagedAgentsMCPOAuthRefreshUpdateParams]`

    Parameters for updating OAuth refresh token configuration.

    - `refresh_token: Optional[str]`

      Updated OAuth refresh token.

    - `scope: Optional[str]`

      Updated OAuth scope for the refresh request.

    - `token_endpoint_auth: Optional[TokenEndpointAuth]`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam: …`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `type: Literal["client_secret_basic"]`

          - `"client_secret_basic"`

        - `client_secret: Optional[str]`

          Updated OAuth client secret.

      - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam: …`

        Updated POST body authentication parameters for the token endpoint.

        - `type: Literal["client_secret_post"]`

          - `"client_secret_post"`

        - `client_secret: Optional[str]`

          Updated OAuth client secret.

### Beta Managed Agents MCP Probe

- `class BetaManagedAgentsMCPProbe: …`

  The failing step of an MCP validation probe.

  - `http_response: Optional[BetaManagedAgentsRefreshHTTPResponse]`

    An HTTP response captured during a credential validation probe.

    - `body: str`

      Response body. May be truncated and has sensitive values scrubbed.

    - `body_truncated: bool`

      Whether `body` was truncated.

    - `content_type: str`

      Value of the `Content-Type` response header.

    - `status_code: int`

      HTTP status code.

  - `method: str`

    The MCP method that failed (for example `initialize` or `tools/list`).

### Beta Managed Agents Refresh HTTP Response

- `class BetaManagedAgentsRefreshHTTPResponse: …`

  An HTTP response captured during a credential validation probe.

  - `body: str`

    Response body. May be truncated and has sensitive values scrubbed.

  - `body_truncated: bool`

    Whether `body` was truncated.

  - `content_type: str`

    Value of the `Content-Type` response header.

  - `status_code: int`

    HTTP status code.

### Beta Managed Agents Refresh Object

- `class BetaManagedAgentsRefreshObject: …`

  Outcome of a refresh-token exchange attempted during credential validation.

  - `http_response: Optional[BetaManagedAgentsRefreshHTTPResponse]`

    An HTTP response captured during a credential validation probe.

    - `body: str`

      Response body. May be truncated and has sensitive values scrubbed.

    - `body_truncated: bool`

      Whether `body` was truncated.

    - `content_type: str`

      Value of the `Content-Type` response header.

    - `status_code: int`

      HTTP status code.

  - `status: Literal["succeeded", "failed", "connect_error", "no_refresh_token"]`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `"succeeded"`

    - `"failed"`

    - `"connect_error"`

    - `"no_refresh_token"`

### Beta Managed Agents Static Bearer Auth Response

- `class BetaManagedAgentsStaticBearerAuthResponse: …`

  Static bearer token credential details for an MCP server.

  - `mcp_server_url: str`

    URL of the MCP server this credential authenticates against.

  - `type: Literal["static_bearer"]`

    - `"static_bearer"`

### Beta Managed Agents Static Bearer Create Params

- `class BetaManagedAgentsStaticBearerCreateParams: …`

  Parameters for creating a static bearer token credential.

  - `token: str`

    Static bearer token value.

  - `mcp_server_url: str`

    URL of the MCP server this credential authenticates against.

  - `type: Literal["static_bearer"]`

    - `"static_bearer"`

### Beta Managed Agents Static Bearer Update Params

- `class BetaManagedAgentsStaticBearerUpdateParams: …`

  Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

  - `type: Literal["static_bearer"]`

    - `"static_bearer"`

  - `token: Optional[str]`

    Updated static bearer token value.

### Beta Managed Agents Token Endpoint Auth Basic Param

- `class BetaManagedAgentsTokenEndpointAuthBasicParam: …`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `client_secret: str`

    OAuth client secret.

  - `type: Literal["client_secret_basic"]`

    - `"client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Response

- `class BetaManagedAgentsTokenEndpointAuthBasicResponse: …`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `type: Literal["client_secret_basic"]`

    - `"client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam: …`

  Updated HTTP Basic authentication parameters for the token endpoint.

  - `type: Literal["client_secret_basic"]`

    - `"client_secret_basic"`

  - `client_secret: Optional[str]`

    Updated OAuth client secret.

### Beta Managed Agents Token Endpoint Auth None Param

- `class BetaManagedAgentsTokenEndpointAuthNoneParam: …`

  Token endpoint requires no client authentication.

  - `type: Literal["none"]`

    - `"none"`

### Beta Managed Agents Token Endpoint Auth None Response

- `class BetaManagedAgentsTokenEndpointAuthNoneResponse: …`

  Token endpoint requires no client authentication.

  - `type: Literal["none"]`

    - `"none"`

### Beta Managed Agents Token Endpoint Auth Post Param

- `class BetaManagedAgentsTokenEndpointAuthPostParam: …`

  Token endpoint uses POST body authentication with client credentials.

  - `client_secret: str`

    OAuth client secret.

  - `type: Literal["client_secret_post"]`

    - `"client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Response

- `class BetaManagedAgentsTokenEndpointAuthPostResponse: …`

  Token endpoint uses POST body authentication with client credentials.

  - `type: Literal["client_secret_post"]`

    - `"client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam: …`

  Updated POST body authentication parameters for the token endpoint.

  - `type: Literal["client_secret_post"]`

    - `"client_secret_post"`

  - `client_secret: Optional[str]`

    Updated OAuth client secret.

### Beta Managed Agents Unrestricted Credential Networking Params

- `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams: …`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `type: Literal["unrestricted"]`

    - `"unrestricted"`

### Beta Managed Agents Unrestricted Credential Networking Response

- `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse: …`

  The secret is substituted on any host the session's Environment network policy permits egress to.

  - `type: Literal["unrestricted"]`

    - `"unrestricted"`

# Memory Stores

## Create a memory store

`beta.memory_stores.create(MemoryStoreCreateParams**kwargs)  -> BetaManagedAgentsMemoryStore`

**post** `/v1/memory_stores`

Create a memory store

### Parameters

- `name: str`

  Human-readable name for the store. Required; 1–255 characters; no control characters. The mount-path slug under `/mnt/memory/` is derived from this name (lowercased, non-alphanumeric runs collapsed to a hyphen). Names need not be unique within a workspace.

- `description: Optional[str]`

  Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent.

- `metadata: Optional[Dict[str, str]]`

  Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Not visible to the agent.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsMemoryStore: …`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: str`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `name: str`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: Literal["memory_store"]`

    - `"memory_store"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: Optional[Dict[str, str]]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_memory_store = client.beta.memory_stores.create(
    name="x",
)
print(beta_managed_agents_memory_store.id)
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

`beta.memory_stores.list(MemoryStoreListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsMemoryStore]`

**get** `/v1/memory_stores`

List memory stores

### Parameters

- `created_at_gte: Optional[Union[str, datetime]]`

  Return only stores whose `created_at` is at or after this time (inclusive). Sent on the wire as `created_at[gte]`.

- `created_at_lte: Optional[Union[str, datetime]]`

  Return only stores whose `created_at` is at or before this time (inclusive). Sent on the wire as `created_at[lte]`.

- `include_archived: Optional[bool]`

  When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

- `limit: Optional[int]`

  Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

- `page: Optional[str]`

  Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsMemoryStore: …`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: str`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `name: str`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: Literal["memory_store"]`

    - `"memory_store"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: Optional[Dict[str, str]]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.memory_stores.list()
page = page.data[0]
print(page.id)
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

`beta.memory_stores.retrieve(strmemory_store_id, MemoryStoreRetrieveParams**kwargs)  -> BetaManagedAgentsMemoryStore`

**get** `/v1/memory_stores/{memory_store_id}`

Retrieve a memory store

### Parameters

- `memory_store_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsMemoryStore: …`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: str`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `name: str`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: Literal["memory_store"]`

    - `"memory_store"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: Optional[Dict[str, str]]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_memory_store = client.beta.memory_stores.retrieve(
    memory_store_id="memory_store_id",
)
print(beta_managed_agents_memory_store.id)
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

`beta.memory_stores.update(strmemory_store_id, MemoryStoreUpdateParams**kwargs)  -> BetaManagedAgentsMemoryStore`

**post** `/v1/memory_stores/{memory_store_id}`

Update a memory store

### Parameters

- `memory_store_id: str`

- `description: Optional[str]`

  New description for the store, up to 1024 characters. Pass an empty string to clear it.

- `metadata: Optional[Dict[str, Optional[str]]]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `name: Optional[str]`

  New human-readable name for the store. 1–255 characters; no control characters. Renaming changes the slug used for the store's `mount_path` in sessions created after the update.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsMemoryStore: …`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: str`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `name: str`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: Literal["memory_store"]`

    - `"memory_store"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: Optional[Dict[str, str]]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_memory_store = client.beta.memory_stores.update(
    memory_store_id="memory_store_id",
)
print(beta_managed_agents_memory_store.id)
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

`beta.memory_stores.delete(strmemory_store_id, MemoryStoreDeleteParams**kwargs)  -> BetaManagedAgentsDeletedMemoryStore`

**delete** `/v1/memory_stores/{memory_store_id}`

Delete a memory store

### Parameters

- `memory_store_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsDeletedMemoryStore: …`

  Confirmation that a `memory_store` was deleted.

  - `id: str`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `type: Literal["memory_store_deleted"]`

    - `"memory_store_deleted"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_deleted_memory_store = client.beta.memory_stores.delete(
    memory_store_id="memory_store_id",
)
print(beta_managed_agents_deleted_memory_store.id)
```

#### Response

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

## Archive a memory store

`beta.memory_stores.archive(strmemory_store_id, MemoryStoreArchiveParams**kwargs)  -> BetaManagedAgentsMemoryStore`

**post** `/v1/memory_stores/{memory_store_id}/archive`

Archive a memory store

### Parameters

- `memory_store_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsMemoryStore: …`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: str`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `name: str`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: Literal["memory_store"]`

    - `"memory_store"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: Optional[Dict[str, str]]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_memory_store = client.beta.memory_stores.archive(
    memory_store_id="memory_store_id",
)
print(beta_managed_agents_memory_store.id)
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

- `class BetaManagedAgentsDeletedMemoryStore: …`

  Confirmation that a `memory_store` was deleted.

  - `id: str`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `type: Literal["memory_store_deleted"]`

    - `"memory_store_deleted"`

### Beta Managed Agents Memory Store

- `class BetaManagedAgentsMemoryStore: …`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: str`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `name: str`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: Literal["memory_store"]`

    - `"memory_store"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: Optional[Dict[str, str]]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

# Memories

## Create a memory

`beta.memory_stores.memories.create(strmemory_store_id, MemoryCreateParams**kwargs)  -> BetaManagedAgentsMemory`

**post** `/v1/memory_stores/{memory_store_id}/memories`

Create a memory

### Parameters

- `memory_store_id: str`

- `content: Optional[str]`

  UTF-8 text content for the new memory. Maximum 100 kB (102,400 bytes). Required; pass `""` explicitly to create an empty memory.

- `path: str`

  Hierarchical path for the new memory, e.g. `/projects/foo/notes.md`. Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive.

- `view: Optional[BetaManagedAgentsMemoryView]`

  Query parameter for view

  - `"basic"`

  - `"full"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsMemory: …`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: str`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: str`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: int`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `memory_store_id: str`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: str`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: str`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: Literal["memory"]`

    - `"memory"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `content: Optional[str]`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_memory = client.beta.memory_stores.memories.create(
    memory_store_id="memory_store_id",
    content="content",
    path="xx",
)
print(beta_managed_agents_memory.id)
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

`beta.memory_stores.memories.list(strmemory_store_id, MemoryListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsMemoryListItem]`

**get** `/v1/memory_stores/{memory_store_id}/memories`

List memories

### Parameters

- `memory_store_id: str`

- `depth: Optional[int]`

  `0` (or omitted) returns all descendants below `path_prefix` (recursive). `1` returns immediate children only; deeper entries roll up as `memory_prefix` items. `depth=1` behaves like `ls`; omitting `depth` behaves like `find`.

- `limit: Optional[int]`

  Maximum number of items to return per page. Must be between 1 and 100. Defaults to 20 when omitted. Capped at 20 when `view=full`. Both `memory` and `memory_prefix` items count toward the limit.

- `page: Optional[str]`

  Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

- `path_prefix: Optional[str]`

  Optional path prefix filter. Must end with `/` (segment-aligned), e.g., `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

- `view: Optional[BetaManagedAgentsMemoryView]`

  Which projection of each `memory` to return. Defaults to `basic` (content omitted). `full` populates `content` on each item and caps `limit` at 20; use this as the bulk-read path for export and sync.

  - `"basic"`

  - `"full"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `BetaManagedAgentsMemoryListItem`

  One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

  - `class BetaManagedAgentsMemory: …`

    A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

    - `id: str`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `content_sha256: str`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `content_size_bytes: int`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `created_at: datetime`

      A timestamp in RFC 3339 format

    - `memory_store_id: str`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `memory_version_id: str`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `path: str`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `type: Literal["memory"]`

      - `"memory"`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

    - `content: Optional[str]`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `class BetaManagedAgentsMemoryPrefix: …`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `path: str`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `type: Literal["memory_prefix"]`

      - `"memory_prefix"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.memory_stores.memories.list(
    memory_store_id="memory_store_id",
)
page = page.data[0]
print(page)
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

`beta.memory_stores.memories.retrieve(strmemory_id, MemoryRetrieveParams**kwargs)  -> BetaManagedAgentsMemory`

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a memory

### Parameters

- `memory_store_id: str`

- `memory_id: str`

- `view: Optional[BetaManagedAgentsMemoryView]`

  Query parameter for view

  - `"basic"`

  - `"full"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsMemory: …`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: str`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: str`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: int`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `memory_store_id: str`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: str`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: str`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: Literal["memory"]`

    - `"memory"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `content: Optional[str]`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_memory = client.beta.memory_stores.memories.retrieve(
    memory_id="memory_id",
    memory_store_id="memory_store_id",
)
print(beta_managed_agents_memory.id)
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

`beta.memory_stores.memories.update(strmemory_id, MemoryUpdateParams**kwargs)  -> BetaManagedAgentsMemory`

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a memory

### Parameters

- `memory_store_id: str`

- `memory_id: str`

- `view: Optional[BetaManagedAgentsMemoryView]`

  Query parameter for view

  - `"basic"`

  - `"full"`

- `content: Optional[str]`

  New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

- `path: Optional[str]`

  New path for the memory (a rename). Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive. The memory's `id` is preserved across renames. Omit to leave the path unchanged.

- `precondition: Optional[BetaManagedAgentsPreconditionParam]`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `type: Literal["content_sha256"]`

    - `"content_sha256"`

  - `content_sha256: Optional[str]`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsMemory: …`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: str`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: str`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: int`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `memory_store_id: str`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: str`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: str`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: Literal["memory"]`

    - `"memory"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `content: Optional[str]`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_memory = client.beta.memory_stores.memories.update(
    memory_id="memory_id",
    memory_store_id="memory_store_id",
)
print(beta_managed_agents_memory.id)
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

`beta.memory_stores.memories.delete(strmemory_id, MemoryDeleteParams**kwargs)  -> BetaManagedAgentsDeletedMemory`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

### Parameters

- `memory_store_id: str`

- `memory_id: str`

- `expected_content_sha256: Optional[str]`

  Query parameter for expected_content_sha256

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsDeletedMemory: …`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `id: str`

    ID of the deleted memory (a `mem_...` value).

  - `type: Literal["memory_deleted"]`

    - `"memory_deleted"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_deleted_memory = client.beta.memory_stores.memories.delete(
    memory_id="memory_id",
    memory_store_id="memory_store_id",
)
print(beta_managed_agents_deleted_memory.id)
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

- `class BetaManagedAgentsConflictError: …`

  - `type: Literal["conflict_error"]`

    - `"conflict_error"`

  - `message: Optional[str]`

### Beta Managed Agents Content Sha256 Precondition

- `class BetaManagedAgentsContentSha256Precondition: …`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `type: Literal["content_sha256"]`

    - `"content_sha256"`

  - `content_sha256: Optional[str]`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

### Beta Managed Agents Deleted Memory

- `class BetaManagedAgentsDeletedMemory: …`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `id: str`

    ID of the deleted memory (a `mem_...` value).

  - `type: Literal["memory_deleted"]`

    - `"memory_deleted"`

### Beta Managed Agents Error

- `BetaManagedAgentsError`

  - `class BetaInvalidRequestError: …`

    - `message: str`

    - `type: Literal["invalid_request_error"]`

      - `"invalid_request_error"`

  - `class BetaAuthenticationError: …`

    - `message: str`

    - `type: Literal["authentication_error"]`

      - `"authentication_error"`

  - `class BetaBillingError: …`

    - `message: str`

    - `type: Literal["billing_error"]`

      - `"billing_error"`

  - `class BetaPermissionError: …`

    - `message: str`

    - `type: Literal["permission_error"]`

      - `"permission_error"`

  - `class BetaNotFoundError: …`

    - `message: str`

    - `type: Literal["not_found_error"]`

      - `"not_found_error"`

  - `class BetaRateLimitError: …`

    - `message: str`

    - `type: Literal["rate_limit_error"]`

      - `"rate_limit_error"`

  - `class BetaGatewayTimeoutError: …`

    - `message: str`

    - `type: Literal["timeout_error"]`

      - `"timeout_error"`

  - `class BetaAPIError: …`

    - `message: str`

    - `type: Literal["api_error"]`

      - `"api_error"`

  - `class BetaOverloadedError: …`

    - `message: str`

    - `type: Literal["overloaded_error"]`

      - `"overloaded_error"`

  - `class BetaManagedAgentsMemoryPreconditionFailedError: …`

    - `type: Literal["memory_precondition_failed_error"]`

      - `"memory_precondition_failed_error"`

    - `message: Optional[str]`

  - `class BetaManagedAgentsMemoryPathConflictError: …`

    - `type: Literal["memory_path_conflict_error"]`

      - `"memory_path_conflict_error"`

    - `conflicting_memory_id: Optional[str]`

    - `conflicting_path: Optional[str]`

    - `message: Optional[str]`

  - `class BetaManagedAgentsConflictError: …`

    - `type: Literal["conflict_error"]`

      - `"conflict_error"`

    - `message: Optional[str]`

### Beta Managed Agents Memory

- `class BetaManagedAgentsMemory: …`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: str`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: str`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: int`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `memory_store_id: str`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: str`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: str`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: Literal["memory"]`

    - `"memory"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `content: Optional[str]`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Beta Managed Agents Memory List Item

- `BetaManagedAgentsMemoryListItem`

  One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

  - `class BetaManagedAgentsMemory: …`

    A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

    - `id: str`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `content_sha256: str`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `content_size_bytes: int`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `created_at: datetime`

      A timestamp in RFC 3339 format

    - `memory_store_id: str`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `memory_version_id: str`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `path: str`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `type: Literal["memory"]`

      - `"memory"`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

    - `content: Optional[str]`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `class BetaManagedAgentsMemoryPrefix: …`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `path: str`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `type: Literal["memory_prefix"]`

      - `"memory_prefix"`

### Beta Managed Agents Memory Path Conflict Error

- `class BetaManagedAgentsMemoryPathConflictError: …`

  - `type: Literal["memory_path_conflict_error"]`

    - `"memory_path_conflict_error"`

  - `conflicting_memory_id: Optional[str]`

  - `conflicting_path: Optional[str]`

  - `message: Optional[str]`

### Beta Managed Agents Memory Precondition Failed Error

- `class BetaManagedAgentsMemoryPreconditionFailedError: …`

  - `type: Literal["memory_precondition_failed_error"]`

    - `"memory_precondition_failed_error"`

  - `message: Optional[str]`

### Beta Managed Agents Memory Prefix

- `class BetaManagedAgentsMemoryPrefix: …`

  A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

  - `path: str`

    The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

  - `type: Literal["memory_prefix"]`

    - `"memory_prefix"`

### Beta Managed Agents Memory View

- `Literal["basic", "full"]`

  Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

  - `"basic"`

  - `"full"`

### Beta Managed Agents Precondition

- `class BetaManagedAgentsPrecondition: …`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `type: Literal["content_sha256"]`

    - `"content_sha256"`

  - `content_sha256: Optional[str]`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

# Memory Versions

## List memory versions

`beta.memory_stores.memory_versions.list(strmemory_store_id, MemoryVersionListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsMemoryVersion]`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

### Parameters

- `memory_store_id: str`

- `api_key_id: Optional[str]`

  Query parameter for api_key_id

- `created_at_gte: Optional[Union[str, datetime]]`

  Return versions created at or after this time (inclusive).

- `created_at_lte: Optional[Union[str, datetime]]`

  Return versions created at or before this time (inclusive).

- `limit: Optional[int]`

  Query parameter for limit

- `memory_id: Optional[str]`

  Query parameter for memory_id

- `operation: Optional[BetaManagedAgentsMemoryVersionOperation]`

  Query parameter for operation

  - `"created"`

  - `"modified"`

  - `"deleted"`

- `page: Optional[str]`

  Query parameter for page

- `service_account_id: Optional[str]`

  Query parameter for service_account_id

- `session_id: Optional[str]`

  Query parameter for session_id

- `view: Optional[BetaManagedAgentsMemoryView]`

  Query parameter for view

  - `"basic"`

  - `"full"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsMemoryVersion: …`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: str`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `memory_id: str`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: str`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: Literal["memory_version"]`

    - `"memory_version"`

  - `content: Optional[str]`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: Optional[str]`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: Optional[int]`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by: Optional[BetaManagedAgentsActor]`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor: …`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: str`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: Literal["session_actor"]`

        - `"session_actor"`

    - `class BetaManagedAgentsAPIActor: …`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: str`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: Literal["api_actor"]`

        - `"api_actor"`

    - `class BetaManagedAgentsUserActor: …`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: Literal["user_actor"]`

        - `"user_actor"`

      - `user_id: str`

        ID of the user who performed the write (a `user_...` value).

    - `class BetaManagedAgentsServiceAccountActor: …`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `service_account_id: str`

        ID of the service account that performed the write (a `svac_...` value).

      - `type: Literal["service_account_actor"]`

        - `"service_account_actor"`

  - `path: Optional[str]`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `redacted_by: Optional[BetaManagedAgentsActor]`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.memory_stores.memory_versions.list(
    memory_store_id="memory_store_id",
)
page = page.data[0]
print(page.id)
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

`beta.memory_stores.memory_versions.retrieve(strmemory_version_id, MemoryVersionRetrieveParams**kwargs)  -> BetaManagedAgentsMemoryVersion`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

### Parameters

- `memory_store_id: str`

- `memory_version_id: str`

- `view: Optional[BetaManagedAgentsMemoryView]`

  Query parameter for view

  - `"basic"`

  - `"full"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsMemoryVersion: …`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: str`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `memory_id: str`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: str`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: Literal["memory_version"]`

    - `"memory_version"`

  - `content: Optional[str]`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: Optional[str]`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: Optional[int]`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by: Optional[BetaManagedAgentsActor]`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor: …`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: str`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: Literal["session_actor"]`

        - `"session_actor"`

    - `class BetaManagedAgentsAPIActor: …`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: str`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: Literal["api_actor"]`

        - `"api_actor"`

    - `class BetaManagedAgentsUserActor: …`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: Literal["user_actor"]`

        - `"user_actor"`

      - `user_id: str`

        ID of the user who performed the write (a `user_...` value).

    - `class BetaManagedAgentsServiceAccountActor: …`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `service_account_id: str`

        ID of the service account that performed the write (a `svac_...` value).

      - `type: Literal["service_account_actor"]`

        - `"service_account_actor"`

  - `path: Optional[str]`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `redacted_by: Optional[BetaManagedAgentsActor]`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_memory_version = client.beta.memory_stores.memory_versions.retrieve(
    memory_version_id="memory_version_id",
    memory_store_id="memory_store_id",
)
print(beta_managed_agents_memory_version.id)
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

`beta.memory_stores.memory_versions.redact(strmemory_version_id, MemoryVersionRedactParams**kwargs)  -> BetaManagedAgentsMemoryVersion`

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a memory version

### Parameters

- `memory_store_id: str`

- `memory_version_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaManagedAgentsMemoryVersion: …`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: str`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `memory_id: str`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: str`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: Literal["memory_version"]`

    - `"memory_version"`

  - `content: Optional[str]`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: Optional[str]`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: Optional[int]`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by: Optional[BetaManagedAgentsActor]`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor: …`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: str`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: Literal["session_actor"]`

        - `"session_actor"`

    - `class BetaManagedAgentsAPIActor: …`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: str`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: Literal["api_actor"]`

        - `"api_actor"`

    - `class BetaManagedAgentsUserActor: …`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: Literal["user_actor"]`

        - `"user_actor"`

      - `user_id: str`

        ID of the user who performed the write (a `user_...` value).

    - `class BetaManagedAgentsServiceAccountActor: …`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `service_account_id: str`

        ID of the service account that performed the write (a `svac_...` value).

      - `type: Literal["service_account_actor"]`

        - `"service_account_actor"`

  - `path: Optional[str]`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `redacted_by: Optional[BetaManagedAgentsActor]`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_memory_version = client.beta.memory_stores.memory_versions.redact(
    memory_version_id="memory_version_id",
    memory_store_id="memory_store_id",
)
print(beta_managed_agents_memory_version.id)
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

- `BetaManagedAgentsActor`

  Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

  - `class BetaManagedAgentsSessionActor: …`

    Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

    - `session_id: str`

      ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

    - `type: Literal["session_actor"]`

      - `"session_actor"`

  - `class BetaManagedAgentsAPIActor: …`

    Attribution for a write made directly via the public API (outside of any session).

    - `api_key_id: str`

      ID of the API key that performed the write. This identifies the key, not the secret.

    - `type: Literal["api_actor"]`

      - `"api_actor"`

  - `class BetaManagedAgentsUserActor: …`

    Attribution for a write made by a human user through the Anthropic Console.

    - `type: Literal["user_actor"]`

      - `"user_actor"`

    - `user_id: str`

      ID of the user who performed the write (a `user_...` value).

  - `class BetaManagedAgentsServiceAccountActor: …`

    Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

    - `service_account_id: str`

      ID of the service account that performed the write (a `svac_...` value).

    - `type: Literal["service_account_actor"]`

      - `"service_account_actor"`

### Beta Managed Agents API Actor

- `class BetaManagedAgentsAPIActor: …`

  Attribution for a write made directly via the public API (outside of any session).

  - `api_key_id: str`

    ID of the API key that performed the write. This identifies the key, not the secret.

  - `type: Literal["api_actor"]`

    - `"api_actor"`

### Beta Managed Agents Memory Version

- `class BetaManagedAgentsMemoryVersion: …`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: str`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `memory_id: str`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: str`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: Literal["memory_version"]`

    - `"memory_version"`

  - `content: Optional[str]`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: Optional[str]`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: Optional[int]`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by: Optional[BetaManagedAgentsActor]`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor: …`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: str`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: Literal["session_actor"]`

        - `"session_actor"`

    - `class BetaManagedAgentsAPIActor: …`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: str`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: Literal["api_actor"]`

        - `"api_actor"`

    - `class BetaManagedAgentsUserActor: …`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: Literal["user_actor"]`

        - `"user_actor"`

      - `user_id: str`

        ID of the user who performed the write (a `user_...` value).

    - `class BetaManagedAgentsServiceAccountActor: …`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `service_account_id: str`

        ID of the service account that performed the write (a `svac_...` value).

      - `type: Literal["service_account_actor"]`

        - `"service_account_actor"`

  - `path: Optional[str]`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `redacted_by: Optional[BetaManagedAgentsActor]`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Beta Managed Agents Memory Version Operation

- `Literal["created", "modified", "deleted"]`

  The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

  - `"created"`

  - `"modified"`

  - `"deleted"`

### Beta Managed Agents Service Account Actor

- `class BetaManagedAgentsServiceAccountActor: …`

  Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

  - `service_account_id: str`

    ID of the service account that performed the write (a `svac_...` value).

  - `type: Literal["service_account_actor"]`

    - `"service_account_actor"`

### Beta Managed Agents Session Actor

- `class BetaManagedAgentsSessionActor: …`

  Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

  - `session_id: str`

    ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

  - `type: Literal["session_actor"]`

    - `"session_actor"`

### Beta Managed Agents User Actor

- `class BetaManagedAgentsUserActor: …`

  Attribution for a write made by a human user through the Anthropic Console.

  - `type: Literal["user_actor"]`

    - `"user_actor"`

  - `user_id: str`

    ID of the user who performed the write (a `user_...` value).

# Files

## Upload File

`beta.files.upload(FileUploadParams**kwargs)  -> BetaFileMetadata`

**post** `/v1/files`

Upload File

### Parameters

- `file: FileTypes`

  The file to upload

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaFileMetadata: …`

  - `id: str`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: datetime`

    RFC 3339 datetime string representing when the file was created.

  - `filename: str`

    Original filename of the uploaded file.

  - `mime_type: str`

    MIME type of the file.

  - `size_bytes: int`

    Size of the file in bytes.

  - `type: Literal["file"]`

    Object type.

    For files, this is always `"file"`.

    - `"file"`

  - `downloadable: Optional[bool]`

    Whether the file can be downloaded.

  - `scope: Optional[BetaFileScope]`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: str`

      The ID of the scoping resource (e.g., the session ID).

    - `type: Literal["session"]`

      The type of scope (e.g., `"session"`).

      - `"session"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_file_metadata = client.beta.files.upload(
    file=b"Example data",
)
print(beta_file_metadata.id)
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

`beta.files.list(FileListParams**kwargs)  -> SyncPage[BetaFileMetadata]`

**get** `/v1/files`

List Files

### Parameters

- `after_id: Optional[str]`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: Optional[str]`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit: Optional[int]`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `scope_id: Optional[str]`

  Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaFileMetadata: …`

  - `id: str`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: datetime`

    RFC 3339 datetime string representing when the file was created.

  - `filename: str`

    Original filename of the uploaded file.

  - `mime_type: str`

    MIME type of the file.

  - `size_bytes: int`

    Size of the file in bytes.

  - `type: Literal["file"]`

    Object type.

    For files, this is always `"file"`.

    - `"file"`

  - `downloadable: Optional[bool]`

    Whether the file can be downloaded.

  - `scope: Optional[BetaFileScope]`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: str`

      The ID of the scoping resource (e.g., the session ID).

    - `type: Literal["session"]`

      The type of scope (e.g., `"session"`).

      - `"session"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.files.list()
page = page.data[0]
print(page.id)
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

`beta.files.download(strfile_id, FileDownloadParams**kwargs)  -> BinaryResponseContent`

**get** `/v1/files/{file_id}/content`

Download File

### Parameters

- `file_id: str`

  ID of the File.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `BinaryResponseContent`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
response = client.beta.files.download(
    file_id="file_id",
)
print(response)
content = response.read()
print(content)
```

## Get File Metadata

`beta.files.retrieve_metadata(strfile_id, FileRetrieveMetadataParams**kwargs)  -> BetaFileMetadata`

**get** `/v1/files/{file_id}`

Get File Metadata

### Parameters

- `file_id: str`

  ID of the File.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaFileMetadata: …`

  - `id: str`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: datetime`

    RFC 3339 datetime string representing when the file was created.

  - `filename: str`

    Original filename of the uploaded file.

  - `mime_type: str`

    MIME type of the file.

  - `size_bytes: int`

    Size of the file in bytes.

  - `type: Literal["file"]`

    Object type.

    For files, this is always `"file"`.

    - `"file"`

  - `downloadable: Optional[bool]`

    Whether the file can be downloaded.

  - `scope: Optional[BetaFileScope]`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: str`

      The ID of the scoping resource (e.g., the session ID).

    - `type: Literal["session"]`

      The type of scope (e.g., `"session"`).

      - `"session"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_file_metadata = client.beta.files.retrieve_metadata(
    file_id="file_id",
)
print(beta_file_metadata.id)
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

`beta.files.delete(strfile_id, FileDeleteParams**kwargs)  -> BetaDeletedFile`

**delete** `/v1/files/{file_id}`

Delete File

### Parameters

- `file_id: str`

  ID of the File.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaDeletedFile: …`

  - `id: str`

    ID of the deleted file.

  - `type: Optional[Literal["file_deleted"]]`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_deleted_file = client.beta.files.delete(
    file_id="file_id",
)
print(beta_deleted_file.id)
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

- `class BetaDeletedFile: …`

  - `id: str`

    ID of the deleted file.

  - `type: Optional[Literal["file_deleted"]]`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"`

### Beta File Metadata

- `class BetaFileMetadata: …`

  - `id: str`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: datetime`

    RFC 3339 datetime string representing when the file was created.

  - `filename: str`

    Original filename of the uploaded file.

  - `mime_type: str`

    MIME type of the file.

  - `size_bytes: int`

    Size of the file in bytes.

  - `type: Literal["file"]`

    Object type.

    For files, this is always `"file"`.

    - `"file"`

  - `downloadable: Optional[bool]`

    Whether the file can be downloaded.

  - `scope: Optional[BetaFileScope]`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: str`

      The ID of the scoping resource (e.g., the session ID).

    - `type: Literal["session"]`

      The type of scope (e.g., `"session"`).

      - `"session"`

### Beta File Scope

- `class BetaFileScope: …`

  - `id: str`

    The ID of the scoping resource (e.g., the session ID).

  - `type: Literal["session"]`

    The type of scope (e.g., `"session"`).

    - `"session"`

# Skills

## Create Skill

`beta.skills.create(SkillCreateParams**kwargs)  -> SkillCreateResponse`

**post** `/v1/skills`

Create Skill

### Parameters

- `files: Sequence[FileTypes]`

  Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `display_title: Optional[str]`

  Display title for the skill.

  This is a human-readable label that is not included in the prompt sent to the model.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class SkillCreateResponse: …`

  - `id: str`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: str`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: Optional[str]`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: Optional[str]`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: str`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: str`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: str`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
skill = client.beta.skills.create(
    files=[b"Example data"],
)
print(skill.id)
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

`beta.skills.list(SkillListParams**kwargs)  -> SyncPageCursor[SkillListResponse]`

**get** `/v1/skills`

List Skills

### Parameters

- `limit: Optional[int]`

  Number of results to return per page.

  Maximum value is 100. Defaults to 20.

- `page: Optional[str]`

  Pagination token for fetching a specific page of results.

  Pass the value from a previous response's `next_page` field to get the next page of results.

- `source: Optional[str]`

  Filter skills by source.

  If provided, only skills from the specified source will be returned:

  * `"custom"`: only return user-created skills
  * `"anthropic"`: only return Anthropic-created skills

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class SkillListResponse: …`

  - `id: str`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: str`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: Optional[str]`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: Optional[str]`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: str`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: str`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: str`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.skills.list()
page = page.data[0]
print(page.id)
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

`beta.skills.retrieve(strskill_id, SkillRetrieveParams**kwargs)  -> SkillRetrieveResponse`

**get** `/v1/skills/{skill_id}`

Get Skill

### Parameters

- `skill_id: str`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class SkillRetrieveResponse: …`

  - `id: str`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: str`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: Optional[str]`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: Optional[str]`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: str`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: str`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: str`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
skill = client.beta.skills.retrieve(
    skill_id="skill_id",
)
print(skill.id)
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

`beta.skills.delete(strskill_id, SkillDeleteParams**kwargs)  -> SkillDeleteResponse`

**delete** `/v1/skills/{skill_id}`

Delete Skill

### Parameters

- `skill_id: str`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class SkillDeleteResponse: …`

  - `id: str`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `type: str`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
skill = client.beta.skills.delete(
    skill_id="skill_id",
)
print(skill.id)
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

- `class SkillCreateResponse: …`

  - `id: str`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: str`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: Optional[str]`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: Optional[str]`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: str`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: str`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: str`

    ISO 8601 timestamp of when the skill was last updated.

### Skill List Response

- `class SkillListResponse: …`

  - `id: str`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: str`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: Optional[str]`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: Optional[str]`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: str`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: str`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: str`

    ISO 8601 timestamp of when the skill was last updated.

### Skill Retrieve Response

- `class SkillRetrieveResponse: …`

  - `id: str`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: str`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: Optional[str]`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: Optional[str]`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: str`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: str`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: str`

    ISO 8601 timestamp of when the skill was last updated.

### Skill Delete Response

- `class SkillDeleteResponse: …`

  - `id: str`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `type: str`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

# Versions

## Create Skill Version

`beta.skills.versions.create(strskill_id, VersionCreateParams**kwargs)  -> VersionCreateResponse`

**post** `/v1/skills/{skill_id}/versions`

Create Skill Version

### Parameters

- `skill_id: str`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `files: Sequence[FileTypes]`

  Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class VersionCreateResponse: …`

  - `id: str`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: str`

    ISO 8601 timestamp of when the skill version was created.

  - `description: str`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: str`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: str`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: str`

    Identifier for the skill that this version belongs to.

  - `type: str`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: str`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
version = client.beta.skills.versions.create(
    skill_id="skill_id",
    files=[b"Example data"],
)
print(version.id)
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

`beta.skills.versions.list(strskill_id, VersionListParams**kwargs)  -> SyncPageCursor[VersionListResponse]`

**get** `/v1/skills/{skill_id}/versions`

List Skill Versions

### Parameters

- `skill_id: str`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `limit: Optional[int]`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `page: Optional[str]`

  Optionally set to the `next_page` token from the previous response.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class VersionListResponse: …`

  - `id: str`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: str`

    ISO 8601 timestamp of when the skill version was created.

  - `description: str`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: str`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: str`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: str`

    Identifier for the skill that this version belongs to.

  - `type: str`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: str`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.skills.versions.list(
    skill_id="skill_id",
)
page = page.data[0]
print(page.id)
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

`beta.skills.versions.download(strversion, VersionDownloadParams**kwargs)  -> BinaryResponseContent`

**get** `/v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

### Parameters

- `skill_id: str`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: str`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `BinaryResponseContent`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
response = client.beta.skills.versions.download(
    version="version",
    skill_id="skill_id",
)
print(response)
content = response.read()
print(content)
```

## Get Skill Version

`beta.skills.versions.retrieve(strversion, VersionRetrieveParams**kwargs)  -> VersionRetrieveResponse`

**get** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

### Parameters

- `skill_id: str`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: str`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class VersionRetrieveResponse: …`

  - `id: str`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: str`

    ISO 8601 timestamp of when the skill version was created.

  - `description: str`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: str`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: str`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: str`

    Identifier for the skill that this version belongs to.

  - `type: str`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: str`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
version = client.beta.skills.versions.retrieve(
    version="version",
    skill_id="skill_id",
)
print(version.id)
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

`beta.skills.versions.delete(strversion, VersionDeleteParams**kwargs)  -> VersionDeleteResponse`

**delete** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

### Parameters

- `skill_id: str`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: str`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class VersionDeleteResponse: …`

  - `id: str`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `type: str`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
version = client.beta.skills.versions.delete(
    version="version",
    skill_id="skill_id",
)
print(version.id)
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

- `class VersionCreateResponse: …`

  - `id: str`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: str`

    ISO 8601 timestamp of when the skill version was created.

  - `description: str`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: str`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: str`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: str`

    Identifier for the skill that this version belongs to.

  - `type: str`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: str`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Version List Response

- `class VersionListResponse: …`

  - `id: str`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: str`

    ISO 8601 timestamp of when the skill version was created.

  - `description: str`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: str`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: str`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: str`

    Identifier for the skill that this version belongs to.

  - `type: str`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: str`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Version Retrieve Response

- `class VersionRetrieveResponse: …`

  - `id: str`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: str`

    ISO 8601 timestamp of when the skill version was created.

  - `description: str`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: str`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: str`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: str`

    Identifier for the skill that this version belongs to.

  - `type: str`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: str`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Version Delete Response

- `class VersionDeleteResponse: …`

  - `id: str`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `type: str`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

# User Profiles

## Create User Profile

`beta.user_profiles.create(UserProfileCreateParams**kwargs)  -> BetaUserProfile`

**post** `/v1/user_profiles`

Create User Profile

### Parameters

- `access_type: Optional[Literal["application", "passthrough"]]`

  How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

  - `"application"`

  - `"passthrough"`

- `external_id: Optional[str]`

  Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

- `metadata: Optional[Dict[str, str]]`

  Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

- `name: Optional[str]`

  Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a resold-to company (`relationship` `resold` / `access_type` `passthrough`), that company's name where known. Maximum 255 characters.

- `relationship: Optional[Literal["external", "resold", "internal"]]`

  How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

  - `"external"`

  - `"resold"`

  - `"internal"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaUserProfile: …`

  - `id: str`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Dict[str, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: Literal["active", "pending", "rejected"]`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: Literal["user_profile"]`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `access_type: Optional[Literal["application", "passthrough"]]`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id: Optional[str]`

    Platform's own identifier for this user. Not enforced unique.

  - `name: Optional[str]`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: Optional[Literal["external", "resold", "internal"]]`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_user_profile = client.beta.user_profiles.create()
print(beta_user_profile.id)
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

`beta.user_profiles.list(UserProfileListParams**kwargs)  -> SyncPageCursor[BetaUserProfile]`

**get** `/v1/user_profiles`

List User Profiles

### Parameters

- `limit: Optional[int]`

  Query parameter for limit

- `order: Optional[Literal["asc", "desc"]]`

  Query parameter for order

  - `"asc"`

  - `"desc"`

- `page: Optional[str]`

  Query parameter for page

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaUserProfile: …`

  - `id: str`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Dict[str, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: Literal["active", "pending", "rejected"]`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: Literal["user_profile"]`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `access_type: Optional[Literal["application", "passthrough"]]`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id: Optional[str]`

    Platform's own identifier for this user. Not enforced unique.

  - `name: Optional[str]`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: Optional[Literal["external", "resold", "internal"]]`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.user_profiles.list()
page = page.data[0]
print(page.id)
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

`beta.user_profiles.retrieve(struser_profile_id, UserProfileRetrieveParams**kwargs)  -> BetaUserProfile`

**get** `/v1/user_profiles/{user_profile_id}`

Get User Profile

### Parameters

- `user_profile_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaUserProfile: …`

  - `id: str`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Dict[str, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: Literal["active", "pending", "rejected"]`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: Literal["user_profile"]`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `access_type: Optional[Literal["application", "passthrough"]]`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id: Optional[str]`

    Platform's own identifier for this user. Not enforced unique.

  - `name: Optional[str]`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: Optional[Literal["external", "resold", "internal"]]`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_user_profile = client.beta.user_profiles.retrieve(
    user_profile_id="uprof_011CZkZCu8hGbp5mYRQgUmz9",
)
print(beta_user_profile.id)
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

`beta.user_profiles.update(struser_profile_id, UserProfileUpdateParams**kwargs)  -> BetaUserProfile`

**post** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `user_profile_id: str`

- `access_type: Optional[Literal["application", "passthrough"]]`

  How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

  - `"application"`

  - `"passthrough"`

- `external_id: Optional[str]`

  If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

- `metadata: Optional[Dict[str, str]]`

  Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

- `name: Optional[str]`

  If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

- `relationship: Optional[Literal["external", "resold", "internal"]]`

  How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

  - `"external"`

  - `"resold"`

  - `"internal"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaUserProfile: …`

  - `id: str`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Dict[str, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: Literal["active", "pending", "rejected"]`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: Literal["user_profile"]`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `access_type: Optional[Literal["application", "passthrough"]]`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id: Optional[str]`

    Platform's own identifier for this user. Not enforced unique.

  - `name: Optional[str]`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: Optional[Literal["external", "resold", "internal"]]`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_user_profile = client.beta.user_profiles.update(
    user_profile_id="uprof_011CZkZCu8hGbp5mYRQgUmz9",
)
print(beta_user_profile.id)
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

`beta.user_profiles.create_enrollment_url(struser_profile_id, UserProfileCreateEnrollmentURLParams**kwargs)  -> BetaUserProfileEnrollmentURL`

**post** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Parameters

- `user_profile_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaUserProfileEnrollmentURL: …`

  - `expires_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["enrollment_url"]`

    Object type. Always `enrollment_url`.

    - `"enrollment_url"`

  - `url: str`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_user_profile_enrollment_url = client.beta.user_profiles.create_enrollment_url(
    user_profile_id="uprof_011CZkZCu8hGbp5mYRQgUmz9",
)
print(beta_user_profile_enrollment_url.expires_at)
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

- `class BetaUserProfile: …`

  - `id: str`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Dict[str, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: Literal["active", "pending", "rejected"]`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: Literal["user_profile"]`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `access_type: Optional[Literal["application", "passthrough"]]`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id: Optional[str]`

    Platform's own identifier for this user. Not enforced unique.

  - `name: Optional[str]`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: Optional[Literal["external", "resold", "internal"]]`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

### Beta User Profile Enrollment URL

- `class BetaUserProfileEnrollmentURL: …`

  - `expires_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["enrollment_url"]`

    Object type. Always `enrollment_url`.

    - `"enrollment_url"`

  - `url: str`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Beta User Profile Trust Grant

- `class BetaUserProfileTrustGrant: …`

  - `status: Literal["active", "pending", "rejected"]`

    Status of the trust grant.

    - `"active"`

    - `"pending"`

    - `"rejected"`

# Dreams

## Create a Dream

`beta.dreams.create(DreamCreateParams**kwargs)  -> BetaDream`

**post** `/v1/dreams`

Create a Dream

### Parameters

- `inputs: Iterable[BetaDreamInputParam]`

  - `class BetaDreamMemoryStoreInput: …`

    An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

    - `memory_store_id: str`

    - `type: Literal["memory_store"]`

      - `"memory_store"`

  - `class BetaDreamSessionsInput: …`

    Input session transcripts the dream reads.

    - `session_ids: List[str]`

    - `type: Literal["sessions"]`

      - `"sessions"`

- `model: Model`

  Model identifier and configuration applied to every pipeline stage.

  - `str`

  - `class BetaDreamModelConfigParam: …`

    Model identifier and configuration applied to every pipeline stage.

    - `id: str`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

- `instructions: Optional[str]`

- `output_behavior: Optional[BetaOutputBehaviorParam]`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `class BetaOutputBehaviorCreateNew: …`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `type: Literal["create_new"]`

      - `"create_new"`

  - `class BetaOutputBehaviorUpdateExisting: …`

    The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

    - `memory_store_id: str`

    - `type: Literal["update_existing"]`

      - `"update_existing"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaDream: …`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: str`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `ended_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `error: Optional[BetaDreamError]`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: str`

    - `type: str`

  - `inputs: List[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput: …`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: str`

      - `type: Literal["memory_store"]`

        - `"memory_store"`

    - `class BetaDreamSessionsInput: …`

      Input session transcripts the dream reads.

      - `session_ids: List[str]`

      - `type: Literal["sessions"]`

        - `"sessions"`

  - `instructions: Optional[str]`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: str`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew: …`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: Literal["create_new"]`

        - `"create_new"`

    - `class BetaOutputBehaviorUpdateExisting: …`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: str`

      - `type: Literal["update_existing"]`

        - `"update_existing"`

  - `outputs: List[BetaDreamOutput]`

    - `memory_store_id: str`

    - `type: Literal["memory_store"]`

      - `"memory_store"`

  - `session_id: Optional[str]`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: Literal["dream"]`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: int`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: int`

      Total tokens read from prompt cache.

    - `input_tokens: int`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: int`

      Total output tokens generated across every pipeline stage.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_dream = client.beta.dreams.create(
    inputs=[
        {
            "memory_store_id": "x",
            "type": "memory_store",
        }
    ],
    model="string",
)
print(beta_dream.id)
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

`beta.dreams.list(DreamListParams**kwargs)  -> SyncPageCursor[BetaDream]`

**get** `/v1/dreams`

List Dreams

### Parameters

- `created_at_gt: Optional[Union[str, datetime]]`

  Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

- `created_at_lt: Optional[Union[str, datetime]]`

  Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

- `include_archived: Optional[bool]`

  Query parameter for include_archived

- `limit: Optional[int]`

  Query parameter for limit

- `page: Optional[str]`

  Query parameter for page

- `statuses: Optional[List[BetaDreamStatus]]`

  Filter by lifecycle status. Repeat the parameter to match any of multiple statuses. Empty applies no status filter.

  - `"pending"`

  - `"running"`

  - `"completed"`

  - `"failed"`

  - `"canceled"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaDream: …`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: str`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `ended_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `error: Optional[BetaDreamError]`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: str`

    - `type: str`

  - `inputs: List[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput: …`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: str`

      - `type: Literal["memory_store"]`

        - `"memory_store"`

    - `class BetaDreamSessionsInput: …`

      Input session transcripts the dream reads.

      - `session_ids: List[str]`

      - `type: Literal["sessions"]`

        - `"sessions"`

  - `instructions: Optional[str]`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: str`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew: …`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: Literal["create_new"]`

        - `"create_new"`

    - `class BetaOutputBehaviorUpdateExisting: …`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: str`

      - `type: Literal["update_existing"]`

        - `"update_existing"`

  - `outputs: List[BetaDreamOutput]`

    - `memory_store_id: str`

    - `type: Literal["memory_store"]`

      - `"memory_store"`

  - `session_id: Optional[str]`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: Literal["dream"]`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: int`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: int`

      Total tokens read from prompt cache.

    - `input_tokens: int`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: int`

      Total output tokens generated across every pipeline stage.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.dreams.list()
page = page.data[0]
print(page.id)
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

`beta.dreams.retrieve(strdream_id, DreamRetrieveParams**kwargs)  -> BetaDream`

**get** `/v1/dreams/{dream_id}`

Get a Dream

### Parameters

- `dream_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaDream: …`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: str`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `ended_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `error: Optional[BetaDreamError]`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: str`

    - `type: str`

  - `inputs: List[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput: …`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: str`

      - `type: Literal["memory_store"]`

        - `"memory_store"`

    - `class BetaDreamSessionsInput: …`

      Input session transcripts the dream reads.

      - `session_ids: List[str]`

      - `type: Literal["sessions"]`

        - `"sessions"`

  - `instructions: Optional[str]`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: str`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew: …`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: Literal["create_new"]`

        - `"create_new"`

    - `class BetaOutputBehaviorUpdateExisting: …`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: str`

      - `type: Literal["update_existing"]`

        - `"update_existing"`

  - `outputs: List[BetaDreamOutput]`

    - `memory_store_id: str`

    - `type: Literal["memory_store"]`

      - `"memory_store"`

  - `session_id: Optional[str]`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: Literal["dream"]`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: int`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: int`

      Total tokens read from prompt cache.

    - `input_tokens: int`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: int`

      Total output tokens generated across every pipeline stage.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_dream = client.beta.dreams.retrieve(
    dream_id="dream_id",
)
print(beta_dream.id)
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

`beta.dreams.cancel(strdream_id, DreamCancelParams**kwargs)  -> BetaDream`

**post** `/v1/dreams/{dream_id}/cancel`

Cancel a Dream

### Parameters

- `dream_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaDream: …`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: str`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `ended_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `error: Optional[BetaDreamError]`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: str`

    - `type: str`

  - `inputs: List[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput: …`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: str`

      - `type: Literal["memory_store"]`

        - `"memory_store"`

    - `class BetaDreamSessionsInput: …`

      Input session transcripts the dream reads.

      - `session_ids: List[str]`

      - `type: Literal["sessions"]`

        - `"sessions"`

  - `instructions: Optional[str]`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: str`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew: …`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: Literal["create_new"]`

        - `"create_new"`

    - `class BetaOutputBehaviorUpdateExisting: …`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: str`

      - `type: Literal["update_existing"]`

        - `"update_existing"`

  - `outputs: List[BetaDreamOutput]`

    - `memory_store_id: str`

    - `type: Literal["memory_store"]`

      - `"memory_store"`

  - `session_id: Optional[str]`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: Literal["dream"]`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: int`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: int`

      Total tokens read from prompt cache.

    - `input_tokens: int`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: int`

      Total output tokens generated across every pipeline stage.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_dream = client.beta.dreams.cancel(
    dream_id="dream_id",
)
print(beta_dream.id)
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

`beta.dreams.archive(strdream_id, DreamArchiveParams**kwargs)  -> BetaDream`

**post** `/v1/dreams/{dream_id}/archive`

Archive a Dream

### Parameters

- `dream_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaDream: …`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: str`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `ended_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `error: Optional[BetaDreamError]`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: str`

    - `type: str`

  - `inputs: List[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput: …`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: str`

      - `type: Literal["memory_store"]`

        - `"memory_store"`

    - `class BetaDreamSessionsInput: …`

      Input session transcripts the dream reads.

      - `session_ids: List[str]`

      - `type: Literal["sessions"]`

        - `"sessions"`

  - `instructions: Optional[str]`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: str`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew: …`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: Literal["create_new"]`

        - `"create_new"`

    - `class BetaOutputBehaviorUpdateExisting: …`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: str`

      - `type: Literal["update_existing"]`

        - `"update_existing"`

  - `outputs: List[BetaDreamOutput]`

    - `memory_store_id: str`

    - `type: Literal["memory_store"]`

      - `"memory_store"`

  - `session_id: Optional[str]`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: Literal["dream"]`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: int`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: int`

      Total tokens read from prompt cache.

    - `input_tokens: int`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: int`

      Total output tokens generated across every pipeline stage.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_dream = client.beta.dreams.archive(
    dream_id="dream_id",
)
print(beta_dream.id)
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

- `class BetaDream: …`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: str`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `ended_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `error: Optional[BetaDreamError]`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: str`

    - `type: str`

  - `inputs: List[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput: …`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: str`

      - `type: Literal["memory_store"]`

        - `"memory_store"`

    - `class BetaDreamSessionsInput: …`

      Input session transcripts the dream reads.

      - `session_ids: List[str]`

      - `type: Literal["sessions"]`

        - `"sessions"`

  - `instructions: Optional[str]`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: str`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew: …`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: Literal["create_new"]`

        - `"create_new"`

    - `class BetaOutputBehaviorUpdateExisting: …`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: str`

      - `type: Literal["update_existing"]`

        - `"update_existing"`

  - `outputs: List[BetaDreamOutput]`

    - `memory_store_id: str`

    - `type: Literal["memory_store"]`

      - `"memory_store"`

  - `session_id: Optional[str]`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: Literal["dream"]`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: int`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: int`

      Total tokens read from prompt cache.

    - `input_tokens: int`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: int`

      Total output tokens generated across every pipeline stage.

### Beta Dream Error

- `class BetaDreamError: …`

  Failure detail for a Dream whose `status` is `failed`.

  - `message: str`

  - `type: str`

### Beta Dream Input

- `BetaDreamInput`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `class BetaDreamMemoryStoreInput: …`

    An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

    - `memory_store_id: str`

    - `type: Literal["memory_store"]`

      - `"memory_store"`

  - `class BetaDreamSessionsInput: …`

    Input session transcripts the dream reads.

    - `session_ids: List[str]`

    - `type: Literal["sessions"]`

      - `"sessions"`

### Beta Dream Memory Store Input

- `class BetaDreamMemoryStoreInput: …`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `memory_store_id: str`

  - `type: Literal["memory_store"]`

    - `"memory_store"`

### Beta Dream Memory Store Output

- `class BetaDreamMemoryStoreOutput: …`

  An output memory store the dream writes consolidated memories into.

  - `memory_store_id: str`

  - `type: Literal["memory_store"]`

    - `"memory_store"`

### Beta Dream Model Config

- `class BetaDreamModelConfig: …`

  Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

  - `id: str`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

  - `speed: Optional[Literal["standard", "fast"]]`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Dream Model Config Param

- `class BetaDreamModelConfigParam: …`

  Model identifier and configuration applied to every pipeline stage.

  - `id: str`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

  - `speed: Optional[Literal["standard", "fast"]]`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Dream Output

- `class BetaDreamOutput: …`

  An output memory store the dream writes consolidated memories into.

  - `memory_store_id: str`

  - `type: Literal["memory_store"]`

    - `"memory_store"`

### Beta Dream Sessions Input

- `class BetaDreamSessionsInput: …`

  Input session transcripts the dream reads.

  - `session_ids: List[str]`

  - `type: Literal["sessions"]`

    - `"sessions"`

### Beta Dream Status

- `Literal["pending", "running", "completed", 2 more]`

  Lifecycle status of a Dream.

  - `"pending"`

  - `"running"`

  - `"completed"`

  - `"failed"`

  - `"canceled"`

### Beta Dream Usage

- `class BetaDreamUsage: …`

  Cumulative token usage for the dream across every pipeline stage.

  - `cache_creation_input_tokens: int`

    Total tokens used to create prompt-cache entries (sum of all TTL tiers).

  - `cache_read_input_tokens: int`

    Total tokens read from prompt cache.

  - `input_tokens: int`

    Total uncached input tokens consumed across every pipeline stage.

  - `output_tokens: int`

    Total output tokens generated across every pipeline stage.

### Beta Output Behavior

- `BetaOutputBehavior`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `class BetaOutputBehaviorCreateNew: …`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `type: Literal["create_new"]`

      - `"create_new"`

  - `class BetaOutputBehaviorUpdateExisting: …`

    The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

    - `memory_store_id: str`

    - `type: Literal["update_existing"]`

      - `"update_existing"`

### Beta Output Behavior Create New

- `class BetaOutputBehaviorCreateNew: …`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `type: Literal["create_new"]`

    - `"create_new"`

### Beta Output Behavior Update Existing

- `class BetaOutputBehaviorUpdateExisting: …`

  The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

  - `memory_store_id: str`

  - `type: Literal["update_existing"]`

    - `"update_existing"`

# Tunnels

## Create Tunnel

`beta.tunnels.create(TunnelCreateParams**kwargs)  -> BetaTunnel`

**post** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

### Parameters

- `display_name: Optional[str]`

  Optional human-readable name for the tunnel (1-255 characters).

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaTunnel: …`

  An MCP tunnel.

  - `id: str`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: Optional[str]`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: str`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: Literal["tunnel"]`

    - `"tunnel"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_tunnel = client.beta.tunnels.create()
print(beta_tunnel.id)
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

`beta.tunnels.retrieve(strtunnel_id, TunnelRetrieveParams**kwargs)  -> BetaTunnel`

**get** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

### Parameters

- `tunnel_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaTunnel: …`

  An MCP tunnel.

  - `id: str`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: Optional[str]`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: str`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: Literal["tunnel"]`

    - `"tunnel"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_tunnel = client.beta.tunnels.retrieve(
    tunnel_id="tunnel_id",
)
print(beta_tunnel.id)
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

`beta.tunnels.list(TunnelListParams**kwargs)  -> SyncPageCursor[BetaTunnel]`

**get** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

### Parameters

- `include_archived: Optional[bool]`

  Whether to include archived tunnels in the results. Defaults to false.

- `limit: Optional[int]`

  Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

- `page: Optional[str]`

  Opaque pagination cursor from a previous `list_tunnels` response.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaTunnel: …`

  An MCP tunnel.

  - `id: str`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: Optional[str]`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: str`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: Literal["tunnel"]`

    - `"tunnel"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.tunnels.list()
page = page.data[0]
print(page.id)
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

`beta.tunnels.archive(strtunnel_id, TunnelArchiveParams**kwargs)  -> BetaTunnel`

**post** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

### Parameters

- `tunnel_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaTunnel: …`

  An MCP tunnel.

  - `id: str`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: Optional[str]`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: str`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: Literal["tunnel"]`

    - `"tunnel"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_tunnel = client.beta.tunnels.archive(
    tunnel_id="tunnel_id",
)
print(beta_tunnel.id)
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

`beta.tunnels.reveal_token(strtunnel_id, TunnelRevealTokenParams**kwargs)  -> BetaTunnelToken`

**post** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

### Parameters

- `tunnel_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaTunnelToken: …`

  A tunnel's connector token.

  - `id: str`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: str`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: Literal["tunnel_token"]`

    - `"tunnel_token"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_tunnel_token = client.beta.tunnels.reveal_token(
    tunnel_id="tunnel_id",
)
print(beta_tunnel_token.id)
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

`beta.tunnels.rotate_token(strtunnel_id, TunnelRotateTokenParams**kwargs)  -> BetaTunnelToken`

**post** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

### Parameters

- `tunnel_id: str`

- `reason: Optional[str]`

  Optional free-text reason for the rotation, recorded for audit.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaTunnelToken: …`

  A tunnel's connector token.

  - `id: str`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: str`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: Literal["tunnel_token"]`

    - `"tunnel_token"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_tunnel_token = client.beta.tunnels.rotate_token(
    tunnel_id="tunnel_id",
)
print(beta_tunnel_token.id)
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

- `class BetaTunnel: …`

  An MCP tunnel.

  - `id: str`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: Optional[str]`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: str`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: Literal["tunnel"]`

    - `"tunnel"`

### Beta Tunnel Token

- `class BetaTunnelToken: …`

  A tunnel's connector token.

  - `id: str`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: str`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: Literal["tunnel_token"]`

    - `"tunnel_token"`

# Certificates

## Create Tunnel Certificate

`beta.tunnels.certificates.create(strtunnel_id, CertificateCreateParams**kwargs)  -> BetaTunnelCertificate`

**post** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

### Parameters

- `tunnel_id: str`

- `ca_certificate_pem: str`

  PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaTunnelCertificate: …`

  A CA certificate attached to a tunnel.

  - `id: str`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `expires_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `fingerprint: str`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: str`

    ID of the tunnel the certificate is registered against.

  - `type: Literal["tunnel_certificate"]`

    - `"tunnel_certificate"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_tunnel_certificate = client.beta.tunnels.certificates.create(
    tunnel_id="tunnel_id",
    ca_certificate_pem="ca_certificate_pem",
)
print(beta_tunnel_certificate.id)
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

`beta.tunnels.certificates.retrieve(strcertificate_id, CertificateRetrieveParams**kwargs)  -> BetaTunnelCertificate`

**get** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

### Parameters

- `tunnel_id: str`

- `certificate_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaTunnelCertificate: …`

  A CA certificate attached to a tunnel.

  - `id: str`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `expires_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `fingerprint: str`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: str`

    ID of the tunnel the certificate is registered against.

  - `type: Literal["tunnel_certificate"]`

    - `"tunnel_certificate"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_tunnel_certificate = client.beta.tunnels.certificates.retrieve(
    certificate_id="certificate_id",
    tunnel_id="tunnel_id",
)
print(beta_tunnel_certificate.id)
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

`beta.tunnels.certificates.list(strtunnel_id, CertificateListParams**kwargs)  -> SyncPageCursor[BetaTunnelCertificate]`

**get** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

### Parameters

- `tunnel_id: str`

- `include_archived: Optional[bool]`

  Whether to include archived certificates in the results. Defaults to false.

- `limit: Optional[int]`

  Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

- `page: Optional[str]`

  Opaque pagination cursor from a previous `list_tunnel_certificates` response.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaTunnelCertificate: …`

  A CA certificate attached to a tunnel.

  - `id: str`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `expires_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `fingerprint: str`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: str`

    ID of the tunnel the certificate is registered against.

  - `type: Literal["tunnel_certificate"]`

    - `"tunnel_certificate"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.tunnels.certificates.list(
    tunnel_id="tunnel_id",
)
page = page.data[0]
print(page.id)
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

`beta.tunnels.certificates.archive(strcertificate_id, CertificateArchiveParams**kwargs)  -> BetaTunnelCertificate`

**post** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

### Parameters

- `tunnel_id: str`

- `certificate_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

- `class BetaTunnelCertificate: …`

  A CA certificate attached to a tunnel.

  - `id: str`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `expires_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `fingerprint: str`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: str`

    ID of the tunnel the certificate is registered against.

  - `type: Literal["tunnel_certificate"]`

    - `"tunnel_certificate"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_tunnel_certificate = client.beta.tunnels.certificates.archive(
    certificate_id="certificate_id",
    tunnel_id="tunnel_id",
)
print(beta_tunnel_certificate.id)
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

- `class BetaTunnelCertificate: …`

  A CA certificate attached to a tunnel.

  - `id: str`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `expires_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `fingerprint: str`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: str`

    ID of the tunnel the certificate is registered against.

  - `type: Literal["tunnel_certificate"]`

    - `"tunnel_certificate"`

# Webhooks

## Domain Types

### Beta Webhook Agent Archived Event Data

- `class BetaWebhookAgentArchivedEventData: …`

  - `id: str`

    ID of the agent that triggered the event.

  - `organization_id: str`

  - `type: Literal["agent.archived"]`

    - `"agent.archived"`

  - `workspace_id: str`

### Beta Webhook Agent Created Event Data

- `class BetaWebhookAgentCreatedEventData: …`

  - `id: str`

    ID of the agent that triggered the event.

  - `organization_id: str`

  - `type: Literal["agent.created"]`

    - `"agent.created"`

  - `workspace_id: str`

### Beta Webhook Agent Deleted Event Data

- `class BetaWebhookAgentDeletedEventData: …`

  - `id: str`

    ID of the agent that triggered the event.

  - `organization_id: str`

  - `type: Literal["agent.deleted"]`

    - `"agent.deleted"`

  - `workspace_id: str`

### Beta Webhook Agent Updated Event Data

- `class BetaWebhookAgentUpdatedEventData: …`

  - `id: str`

    ID of the agent that triggered the event.

  - `organization_id: str`

  - `type: Literal["agent.updated"]`

    - `"agent.updated"`

  - `workspace_id: str`

### Beta Webhook Deployment Archived Event Data

- `class BetaWebhookDeploymentArchivedEventData: …`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment.archived"]`

    - `"deployment.archived"`

  - `workspace_id: str`

### Beta Webhook Deployment Created Event Data

- `class BetaWebhookDeploymentCreatedEventData: …`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment.created"]`

    - `"deployment.created"`

  - `workspace_id: str`

### Beta Webhook Deployment Deleted Event Data

- `class BetaWebhookDeploymentDeletedEventData: …`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment.deleted"]`

    - `"deployment.deleted"`

  - `workspace_id: str`

### Beta Webhook Deployment Paused Event Data

- `class BetaWebhookDeploymentPausedEventData: …`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment.paused"]`

    - `"deployment.paused"`

  - `workspace_id: str`

### Beta Webhook Deployment Run Failed Event Data

- `class BetaWebhookDeploymentRunFailedEventData: …`

  - `id: str`

    ID of the deployment run that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment_run.failed"]`

    - `"deployment_run.failed"`

  - `workspace_id: str`

### Beta Webhook Deployment Run Started Event Data

- `class BetaWebhookDeploymentRunStartedEventData: …`

  - `id: str`

    ID of the deployment run that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment_run.started"]`

    - `"deployment_run.started"`

  - `workspace_id: str`

### Beta Webhook Deployment Run Succeeded Event Data

- `class BetaWebhookDeploymentRunSucceededEventData: …`

  - `id: str`

    ID of the deployment run that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment_run.succeeded"]`

    - `"deployment_run.succeeded"`

  - `workspace_id: str`

### Beta Webhook Deployment Unpaused Event Data

- `class BetaWebhookDeploymentUnpausedEventData: …`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment.unpaused"]`

    - `"deployment.unpaused"`

  - `workspace_id: str`

### Beta Webhook Deployment Updated Event Data

- `class BetaWebhookDeploymentUpdatedEventData: …`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment.updated"]`

    - `"deployment.updated"`

  - `workspace_id: str`

### Beta Webhook Environment Archived Event Data

- `class BetaWebhookEnvironmentArchivedEventData: …`

  - `id: str`

    ID of the environment that triggered the event.

  - `organization_id: str`

  - `type: Literal["environment.archived"]`

    - `"environment.archived"`

  - `workspace_id: str`

### Beta Webhook Environment Created Event Data

- `class BetaWebhookEnvironmentCreatedEventData: …`

  - `id: str`

    ID of the environment that triggered the event.

  - `organization_id: str`

  - `type: Literal["environment.created"]`

    - `"environment.created"`

  - `workspace_id: str`

### Beta Webhook Environment Deleted Event Data

- `class BetaWebhookEnvironmentDeletedEventData: …`

  - `id: str`

    ID of the environment that triggered the event.

  - `organization_id: str`

  - `type: Literal["environment.deleted"]`

    - `"environment.deleted"`

  - `workspace_id: str`

### Beta Webhook Environment Updated Event Data

- `class BetaWebhookEnvironmentUpdatedEventData: …`

  - `id: str`

    ID of the environment that triggered the event.

  - `organization_id: str`

  - `type: Literal["environment.updated"]`

    - `"environment.updated"`

  - `workspace_id: str`

### Beta Webhook Event

- `class BetaWebhookEvent: …`

  - `id: str`

    Unique event identifier for idempotency.

  - `created_at: datetime`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `class BetaWebhookSessionCreatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.created"]`

        - `"session.created"`

      - `workspace_id: str`

    - `class BetaWebhookSessionPendingEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.pending"]`

        - `"session.pending"`

      - `workspace_id: str`

    - `class BetaWebhookSessionRunningEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.running"]`

        - `"session.running"`

      - `workspace_id: str`

    - `class BetaWebhookSessionIdledEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.idled"]`

        - `"session.idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionRequiresActionEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.requires_action"]`

        - `"session.requires_action"`

      - `workspace_id: str`

    - `class BetaWebhookSessionArchivedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.archived"]`

        - `"session.archived"`

      - `workspace_id: str`

    - `class BetaWebhookSessionDeletedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.deleted"]`

        - `"session.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusRescheduledEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_rescheduled"]`

        - `"session.status_rescheduled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusRunStartedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_run_started"]`

        - `"session.status_run_started"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusIdledEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_idled"]`

        - `"session.status_idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusTerminatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_terminated"]`

        - `"session.status_terminated"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadCreatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `type: Literal["session.thread_created"]`

        - `"session.thread_created"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadIdledEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `type: Literal["session.thread_idled"]`

        - `"session.thread_idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadTerminatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `type: Literal["session.thread_terminated"]`

        - `"session.thread_terminated"`

      - `workspace_id: str`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.outcome_evaluation_ended"]`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: str`

    - `class BetaWebhookVaultCreatedEventData: …`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.created"]`

        - `"vault.created"`

      - `workspace_id: str`

    - `class BetaWebhookVaultArchivedEventData: …`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.archived"]`

        - `"vault.archived"`

      - `workspace_id: str`

    - `class BetaWebhookVaultDeletedEventData: …`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.deleted"]`

        - `"vault.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialCreatedEventData: …`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.created"]`

        - `"vault_credential.created"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialArchivedEventData: …`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.archived"]`

        - `"vault_credential.archived"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialDeletedEventData: …`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.deleted"]`

        - `"vault_credential.deleted"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData: …`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.refresh_failed"]`

        - `"vault_credential.refresh_failed"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookSessionUpdatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.updated"]`

        - `"session.updated"`

      - `workspace_id: str`

    - `class BetaWebhookAgentCreatedEventData: …`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `type: Literal["agent.created"]`

        - `"agent.created"`

      - `workspace_id: str`

    - `class BetaWebhookAgentArchivedEventData: …`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `type: Literal["agent.archived"]`

        - `"agent.archived"`

      - `workspace_id: str`

    - `class BetaWebhookAgentDeletedEventData: …`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `type: Literal["agent.deleted"]`

        - `"agent.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentPausedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.paused"]`

        - `"deployment.paused"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunFailedEventData: …`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment_run.failed"]`

        - `"deployment_run.failed"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentCreatedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.created"]`

        - `"deployment.created"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentUpdatedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.updated"]`

        - `"deployment.updated"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentUnpausedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.unpaused"]`

        - `"deployment.unpaused"`

      - `workspace_id: str`

    - `class BetaWebhookAgentUpdatedEventData: …`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `type: Literal["agent.updated"]`

        - `"agent.updated"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentArchivedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.archived"]`

        - `"deployment.archived"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunStartedEventData: …`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment_run.started"]`

        - `"deployment_run.started"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentDeletedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.deleted"]`

        - `"deployment.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunSucceededEventData: …`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment_run.succeeded"]`

        - `"deployment_run.succeeded"`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentCreatedEventData: …`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `type: Literal["environment.created"]`

        - `"environment.created"`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentUpdatedEventData: …`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `type: Literal["environment.updated"]`

        - `"environment.updated"`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentArchivedEventData: …`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `type: Literal["environment.archived"]`

        - `"environment.archived"`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentDeletedEventData: …`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `type: Literal["environment.deleted"]`

        - `"environment.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreCreatedEventData: …`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `type: Literal["memory_store.created"]`

        - `"memory_store.created"`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreArchivedEventData: …`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `type: Literal["memory_store.archived"]`

        - `"memory_store.archived"`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreDeletedEventData: …`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `type: Literal["memory_store.deleted"]`

        - `"memory_store.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookSessionBudgetReachedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.budget_reached"]`

        - `"session.budget_reached"`

      - `workspace_id: str`

  - `type: Literal["event"]`

    Object type. Always `event` for webhook payloads.

    - `"event"`

### Beta Webhook Event Data

- `BetaWebhookEventData`

  - `class BetaWebhookSessionCreatedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.created"]`

      - `"session.created"`

    - `workspace_id: str`

  - `class BetaWebhookSessionPendingEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.pending"]`

      - `"session.pending"`

    - `workspace_id: str`

  - `class BetaWebhookSessionRunningEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.running"]`

      - `"session.running"`

    - `workspace_id: str`

  - `class BetaWebhookSessionIdledEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.idled"]`

      - `"session.idled"`

    - `workspace_id: str`

  - `class BetaWebhookSessionRequiresActionEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.requires_action"]`

      - `"session.requires_action"`

    - `workspace_id: str`

  - `class BetaWebhookSessionArchivedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.archived"]`

      - `"session.archived"`

    - `workspace_id: str`

  - `class BetaWebhookSessionDeletedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.deleted"]`

      - `"session.deleted"`

    - `workspace_id: str`

  - `class BetaWebhookSessionStatusRescheduledEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.status_rescheduled"]`

      - `"session.status_rescheduled"`

    - `workspace_id: str`

  - `class BetaWebhookSessionStatusRunStartedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.status_run_started"]`

      - `"session.status_run_started"`

    - `workspace_id: str`

  - `class BetaWebhookSessionStatusIdledEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.status_idled"]`

      - `"session.status_idled"`

    - `workspace_id: str`

  - `class BetaWebhookSessionStatusTerminatedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.status_terminated"]`

      - `"session.status_terminated"`

    - `workspace_id: str`

  - `class BetaWebhookSessionThreadCreatedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `session_thread_id: str`

      ID of the session thread this event refers to.

    - `type: Literal["session.thread_created"]`

      - `"session.thread_created"`

    - `workspace_id: str`

  - `class BetaWebhookSessionThreadIdledEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `session_thread_id: str`

      ID of the session thread this event refers to.

    - `type: Literal["session.thread_idled"]`

      - `"session.thread_idled"`

    - `workspace_id: str`

  - `class BetaWebhookSessionThreadTerminatedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `session_thread_id: str`

      ID of the session thread this event refers to.

    - `type: Literal["session.thread_terminated"]`

      - `"session.thread_terminated"`

    - `workspace_id: str`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.outcome_evaluation_ended"]`

      - `"session.outcome_evaluation_ended"`

    - `workspace_id: str`

  - `class BetaWebhookVaultCreatedEventData: …`

    - `id: str`

      ID of the vault that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault.created"]`

      - `"vault.created"`

    - `workspace_id: str`

  - `class BetaWebhookVaultArchivedEventData: …`

    - `id: str`

      ID of the vault that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault.archived"]`

      - `"vault.archived"`

    - `workspace_id: str`

  - `class BetaWebhookVaultDeletedEventData: …`

    - `id: str`

      ID of the vault that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault.deleted"]`

      - `"vault.deleted"`

    - `workspace_id: str`

  - `class BetaWebhookVaultCredentialCreatedEventData: …`

    - `id: str`

      ID of the vault credential that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault_credential.created"]`

      - `"vault_credential.created"`

    - `vault_id: str`

      ID of the vault that owns this credential.

    - `workspace_id: str`

  - `class BetaWebhookVaultCredentialArchivedEventData: …`

    - `id: str`

      ID of the vault credential that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault_credential.archived"]`

      - `"vault_credential.archived"`

    - `vault_id: str`

      ID of the vault that owns this credential.

    - `workspace_id: str`

  - `class BetaWebhookVaultCredentialDeletedEventData: …`

    - `id: str`

      ID of the vault credential that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault_credential.deleted"]`

      - `"vault_credential.deleted"`

    - `vault_id: str`

      ID of the vault that owns this credential.

    - `workspace_id: str`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData: …`

    - `id: str`

      ID of the vault credential that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault_credential.refresh_failed"]`

      - `"vault_credential.refresh_failed"`

    - `vault_id: str`

      ID of the vault that owns this credential.

    - `workspace_id: str`

  - `class BetaWebhookSessionUpdatedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.updated"]`

      - `"session.updated"`

    - `workspace_id: str`

  - `class BetaWebhookAgentCreatedEventData: …`

    - `id: str`

      ID of the agent that triggered the event.

    - `organization_id: str`

    - `type: Literal["agent.created"]`

      - `"agent.created"`

    - `workspace_id: str`

  - `class BetaWebhookAgentArchivedEventData: …`

    - `id: str`

      ID of the agent that triggered the event.

    - `organization_id: str`

    - `type: Literal["agent.archived"]`

      - `"agent.archived"`

    - `workspace_id: str`

  - `class BetaWebhookAgentDeletedEventData: …`

    - `id: str`

      ID of the agent that triggered the event.

    - `organization_id: str`

    - `type: Literal["agent.deleted"]`

      - `"agent.deleted"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentPausedEventData: …`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment.paused"]`

      - `"deployment.paused"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentRunFailedEventData: …`

    - `id: str`

      ID of the deployment run that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment_run.failed"]`

      - `"deployment_run.failed"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentCreatedEventData: …`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment.created"]`

      - `"deployment.created"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentUpdatedEventData: …`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment.updated"]`

      - `"deployment.updated"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentUnpausedEventData: …`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment.unpaused"]`

      - `"deployment.unpaused"`

    - `workspace_id: str`

  - `class BetaWebhookAgentUpdatedEventData: …`

    - `id: str`

      ID of the agent that triggered the event.

    - `organization_id: str`

    - `type: Literal["agent.updated"]`

      - `"agent.updated"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentArchivedEventData: …`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment.archived"]`

      - `"deployment.archived"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentRunStartedEventData: …`

    - `id: str`

      ID of the deployment run that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment_run.started"]`

      - `"deployment_run.started"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentDeletedEventData: …`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment.deleted"]`

      - `"deployment.deleted"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentRunSucceededEventData: …`

    - `id: str`

      ID of the deployment run that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment_run.succeeded"]`

      - `"deployment_run.succeeded"`

    - `workspace_id: str`

  - `class BetaWebhookEnvironmentCreatedEventData: …`

    - `id: str`

      ID of the environment that triggered the event.

    - `organization_id: str`

    - `type: Literal["environment.created"]`

      - `"environment.created"`

    - `workspace_id: str`

  - `class BetaWebhookEnvironmentUpdatedEventData: …`

    - `id: str`

      ID of the environment that triggered the event.

    - `organization_id: str`

    - `type: Literal["environment.updated"]`

      - `"environment.updated"`

    - `workspace_id: str`

  - `class BetaWebhookEnvironmentArchivedEventData: …`

    - `id: str`

      ID of the environment that triggered the event.

    - `organization_id: str`

    - `type: Literal["environment.archived"]`

      - `"environment.archived"`

    - `workspace_id: str`

  - `class BetaWebhookEnvironmentDeletedEventData: …`

    - `id: str`

      ID of the environment that triggered the event.

    - `organization_id: str`

    - `type: Literal["environment.deleted"]`

      - `"environment.deleted"`

    - `workspace_id: str`

  - `class BetaWebhookMemoryStoreCreatedEventData: …`

    - `id: str`

      ID of the memory store that triggered the event.

    - `organization_id: str`

    - `type: Literal["memory_store.created"]`

      - `"memory_store.created"`

    - `workspace_id: str`

  - `class BetaWebhookMemoryStoreArchivedEventData: …`

    - `id: str`

      ID of the memory store that triggered the event.

    - `organization_id: str`

    - `type: Literal["memory_store.archived"]`

      - `"memory_store.archived"`

    - `workspace_id: str`

  - `class BetaWebhookMemoryStoreDeletedEventData: …`

    - `id: str`

      ID of the memory store that triggered the event.

    - `organization_id: str`

    - `type: Literal["memory_store.deleted"]`

      - `"memory_store.deleted"`

    - `workspace_id: str`

  - `class BetaWebhookSessionBudgetReachedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.budget_reached"]`

      - `"session.budget_reached"`

    - `workspace_id: str`

### Beta Webhook Memory Store Archived Event Data

- `class BetaWebhookMemoryStoreArchivedEventData: …`

  - `id: str`

    ID of the memory store that triggered the event.

  - `organization_id: str`

  - `type: Literal["memory_store.archived"]`

    - `"memory_store.archived"`

  - `workspace_id: str`

### Beta Webhook Memory Store Created Event Data

- `class BetaWebhookMemoryStoreCreatedEventData: …`

  - `id: str`

    ID of the memory store that triggered the event.

  - `organization_id: str`

  - `type: Literal["memory_store.created"]`

    - `"memory_store.created"`

  - `workspace_id: str`

### Beta Webhook Memory Store Deleted Event Data

- `class BetaWebhookMemoryStoreDeletedEventData: …`

  - `id: str`

    ID of the memory store that triggered the event.

  - `organization_id: str`

  - `type: Literal["memory_store.deleted"]`

    - `"memory_store.deleted"`

  - `workspace_id: str`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.archived"]`

    - `"session.archived"`

  - `workspace_id: str`

### Beta Webhook Session Budget Reached Event Data

- `class BetaWebhookSessionBudgetReachedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.budget_reached"]`

    - `"session.budget_reached"`

  - `workspace_id: str`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.created"]`

    - `"session.created"`

  - `workspace_id: str`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.deleted"]`

    - `"session.deleted"`

  - `workspace_id: str`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.idled"]`

    - `"session.idled"`

  - `workspace_id: str`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.outcome_evaluation_ended"]`

    - `"session.outcome_evaluation_ended"`

  - `workspace_id: str`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.pending"]`

    - `"session.pending"`

  - `workspace_id: str`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.requires_action"]`

    - `"session.requires_action"`

  - `workspace_id: str`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.running"]`

    - `"session.running"`

  - `workspace_id: str`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.status_idled"]`

    - `"session.status_idled"`

  - `workspace_id: str`

### Beta Webhook Session Status Rescheduled Event Data

- `class BetaWebhookSessionStatusRescheduledEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.status_rescheduled"]`

    - `"session.status_rescheduled"`

  - `workspace_id: str`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.status_run_started"]`

    - `"session.status_run_started"`

  - `workspace_id: str`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.status_terminated"]`

    - `"session.status_terminated"`

  - `workspace_id: str`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `session_thread_id: str`

    ID of the session thread this event refers to.

  - `type: Literal["session.thread_created"]`

    - `"session.thread_created"`

  - `workspace_id: str`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `session_thread_id: str`

    ID of the session thread this event refers to.

  - `type: Literal["session.thread_idled"]`

    - `"session.thread_idled"`

  - `workspace_id: str`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `session_thread_id: str`

    ID of the session thread this event refers to.

  - `type: Literal["session.thread_terminated"]`

    - `"session.thread_terminated"`

  - `workspace_id: str`

### Beta Webhook Session Updated Event Data

- `class BetaWebhookSessionUpdatedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.updated"]`

    - `"session.updated"`

  - `workspace_id: str`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData: …`

  - `id: str`

    ID of the vault that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault.archived"]`

    - `"vault.archived"`

  - `workspace_id: str`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData: …`

  - `id: str`

    ID of the vault that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault.created"]`

    - `"vault.created"`

  - `workspace_id: str`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData: …`

  - `id: str`

    ID of the vault credential that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault_credential.archived"]`

    - `"vault_credential.archived"`

  - `vault_id: str`

    ID of the vault that owns this credential.

  - `workspace_id: str`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData: …`

  - `id: str`

    ID of the vault credential that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault_credential.created"]`

    - `"vault_credential.created"`

  - `vault_id: str`

    ID of the vault that owns this credential.

  - `workspace_id: str`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData: …`

  - `id: str`

    ID of the vault credential that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault_credential.deleted"]`

    - `"vault_credential.deleted"`

  - `vault_id: str`

    ID of the vault that owns this credential.

  - `workspace_id: str`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData: …`

  - `id: str`

    ID of the vault credential that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault_credential.refresh_failed"]`

    - `"vault_credential.refresh_failed"`

  - `vault_id: str`

    ID of the vault that owns this credential.

  - `workspace_id: str`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData: …`

  - `id: str`

    ID of the vault that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault.deleted"]`

    - `"vault.deleted"`

  - `workspace_id: str`

### Unwrap Webhook Event

- `class UnwrapWebhookEvent: …`

  - `id: str`

    Unique event identifier for idempotency.

  - `created_at: datetime`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `class BetaWebhookSessionCreatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.created"]`

        - `"session.created"`

      - `workspace_id: str`

    - `class BetaWebhookSessionPendingEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.pending"]`

        - `"session.pending"`

      - `workspace_id: str`

    - `class BetaWebhookSessionRunningEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.running"]`

        - `"session.running"`

      - `workspace_id: str`

    - `class BetaWebhookSessionIdledEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.idled"]`

        - `"session.idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionRequiresActionEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.requires_action"]`

        - `"session.requires_action"`

      - `workspace_id: str`

    - `class BetaWebhookSessionArchivedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.archived"]`

        - `"session.archived"`

      - `workspace_id: str`

    - `class BetaWebhookSessionDeletedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.deleted"]`

        - `"session.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusRescheduledEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_rescheduled"]`

        - `"session.status_rescheduled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusRunStartedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_run_started"]`

        - `"session.status_run_started"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusIdledEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_idled"]`

        - `"session.status_idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusTerminatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_terminated"]`

        - `"session.status_terminated"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadCreatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `type: Literal["session.thread_created"]`

        - `"session.thread_created"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadIdledEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `type: Literal["session.thread_idled"]`

        - `"session.thread_idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadTerminatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `type: Literal["session.thread_terminated"]`

        - `"session.thread_terminated"`

      - `workspace_id: str`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.outcome_evaluation_ended"]`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: str`

    - `class BetaWebhookVaultCreatedEventData: …`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.created"]`

        - `"vault.created"`

      - `workspace_id: str`

    - `class BetaWebhookVaultArchivedEventData: …`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.archived"]`

        - `"vault.archived"`

      - `workspace_id: str`

    - `class BetaWebhookVaultDeletedEventData: …`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.deleted"]`

        - `"vault.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialCreatedEventData: …`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.created"]`

        - `"vault_credential.created"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialArchivedEventData: …`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.archived"]`

        - `"vault_credential.archived"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialDeletedEventData: …`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.deleted"]`

        - `"vault_credential.deleted"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData: …`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.refresh_failed"]`

        - `"vault_credential.refresh_failed"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookSessionUpdatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.updated"]`

        - `"session.updated"`

      - `workspace_id: str`

    - `class BetaWebhookAgentCreatedEventData: …`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `type: Literal["agent.created"]`

        - `"agent.created"`

      - `workspace_id: str`

    - `class BetaWebhookAgentArchivedEventData: …`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `type: Literal["agent.archived"]`

        - `"agent.archived"`

      - `workspace_id: str`

    - `class BetaWebhookAgentDeletedEventData: …`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `type: Literal["agent.deleted"]`

        - `"agent.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentPausedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.paused"]`

        - `"deployment.paused"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunFailedEventData: …`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment_run.failed"]`

        - `"deployment_run.failed"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentCreatedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.created"]`

        - `"deployment.created"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentUpdatedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.updated"]`

        - `"deployment.updated"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentUnpausedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.unpaused"]`

        - `"deployment.unpaused"`

      - `workspace_id: str`

    - `class BetaWebhookAgentUpdatedEventData: …`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `type: Literal["agent.updated"]`

        - `"agent.updated"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentArchivedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.archived"]`

        - `"deployment.archived"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunStartedEventData: …`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment_run.started"]`

        - `"deployment_run.started"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentDeletedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.deleted"]`

        - `"deployment.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunSucceededEventData: …`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment_run.succeeded"]`

        - `"deployment_run.succeeded"`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentCreatedEventData: …`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `type: Literal["environment.created"]`

        - `"environment.created"`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentUpdatedEventData: …`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `type: Literal["environment.updated"]`

        - `"environment.updated"`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentArchivedEventData: …`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `type: Literal["environment.archived"]`

        - `"environment.archived"`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentDeletedEventData: …`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `type: Literal["environment.deleted"]`

        - `"environment.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreCreatedEventData: …`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `type: Literal["memory_store.created"]`

        - `"memory_store.created"`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreArchivedEventData: …`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `type: Literal["memory_store.archived"]`

        - `"memory_store.archived"`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreDeletedEventData: …`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `type: Literal["memory_store.deleted"]`

        - `"memory_store.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookSessionBudgetReachedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.budget_reached"]`

        - `"session.budget_reached"`

      - `workspace_id: str`

  - `type: Literal["event"]`

    Object type. Always `event` for webhook payloads.

    - `"event"`
