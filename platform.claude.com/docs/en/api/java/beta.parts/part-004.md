<!-- source: https://platform.claude.com/docs/en/api/java/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/java/beta -->

<!-- chunk-start -->

  - `String message`

    Human-readable error description.

  - `Type type`

    - `VAULT_ARCHIVED_ERROR("vault_archived_error")`

### Beta Managed Agents Vault Not Found Run Error

- `class BetaManagedAgentsVaultNotFoundRunError:`

  A vault referenced by the deployment no longer exists.

  - `String message`

    Human-readable error description.

  - `Type type`

    - `VAULT_NOT_FOUND_ERROR("vault_not_found_error")`

### Beta Managed Agents Workspace Archived Run Error

- `class BetaManagedAgentsWorkspaceArchivedRunError:`

  The deployment's workspace was archived.

  - `String message`

    Human-readable error description.

  - `Type type`

    - `WORKSPACE_ARCHIVED_ERROR("workspace_archived_error")`

# Vaults

## Create Vault

`BetaManagedAgentsVault beta().vaults().create(VaultCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/vaults`

Create Vault

### Parameters

- `VaultCreateParams params`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `String displayName`

    Human-readable name for the vault. 1-255 characters.

  - `Optional<Metadata> metadata`

    Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `String id`

    Unique identifier for the vault.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

    - `VAULT("vault")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsVault;
import com.anthropic.models.beta.vaults.VaultCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VaultCreateParams params = VaultCreateParams.builder()
            .displayName("Example vault")
            .build();
        BetaManagedAgentsVault betaManagedAgentsVault = client.beta().vaults().create(params);
    }
}
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

`VaultListPage beta().vaults().list(VaultListParamsparams = VaultListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/vaults`

List Vaults

### Parameters

- `VaultListParams params`

  - `Optional<Boolean> includeArchived`

    Whether to include archived vaults in the results.

  - `Optional<Long> limit`

    Maximum number of vaults to return per page. Defaults to 20, maximum 100.

  - `Optional<String> page`

    Opaque pagination token from a previous `list_vaults` response.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `String id`

    Unique identifier for the vault.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

    - `VAULT("vault")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.VaultListPage;
import com.anthropic.models.beta.vaults.VaultListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VaultListPage page = client.beta().vaults().list();
    }
}
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

`BetaManagedAgentsVault beta().vaults().retrieve(VaultRetrieveParamsparams = VaultRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/vaults/{vault_id}`

Get Vault

### Parameters

- `VaultRetrieveParams params`

  - `Optional<String> vaultId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `String id`

    Unique identifier for the vault.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

    - `VAULT("vault")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsVault;
import com.anthropic.models.beta.vaults.VaultRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsVault betaManagedAgentsVault = client.beta().vaults().retrieve("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
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

`BetaManagedAgentsVault beta().vaults().update(VaultUpdateParamsparams = VaultUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/vaults/{vault_id}`

Update Vault

### Parameters

- `VaultUpdateParams params`

  - `Optional<String> vaultId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `Optional<String> displayName`

    Updated human-readable name for the vault. 1-255 characters.

  - `Optional<Metadata> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `String id`

    Unique identifier for the vault.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

    - `VAULT("vault")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsVault;
import com.anthropic.models.beta.vaults.VaultUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsVault betaManagedAgentsVault = client.beta().vaults().update("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
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

`BetaManagedAgentsDeletedVault beta().vaults().delete(VaultDeleteParamsparams = VaultDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/vaults/{vault_id}`

Delete Vault

### Parameters

- `VaultDeleteParams params`

  - `Optional<String> vaultId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsDeletedVault:`

  Confirmation of a deleted vault.

  - `String id`

    Unique identifier of the deleted vault.

  - `Type type`

    - `VAULT_DELETED("vault_deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsDeletedVault;
import com.anthropic.models.beta.vaults.VaultDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeletedVault betaManagedAgentsDeletedVault = client.beta().vaults().delete("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

## Archive Vault

`BetaManagedAgentsVault beta().vaults().archive(VaultArchiveParamsparams = VaultArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/vaults/{vault_id}/archive`

Archive Vault

### Parameters

- `VaultArchiveParams params`

  - `Optional<String> vaultId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `String id`

    Unique identifier for the vault.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

    - `VAULT("vault")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsVault;
import com.anthropic.models.beta.vaults.VaultArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsVault betaManagedAgentsVault = client.beta().vaults().archive("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
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

- `class BetaManagedAgentsDeletedVault:`

  Confirmation of a deleted vault.

  - `String id`

    Unique identifier of the deleted vault.

  - `Type type`

    - `VAULT_DELETED("vault_deleted")`

### Beta Managed Agents Vault

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `String id`

    Unique identifier for the vault.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

    - `VAULT("vault")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

# Credentials

## Create Credential

`BetaManagedAgentsCredential beta().vaults().credentials().create(CredentialCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/vaults/{vault_id}/credentials`

Create Credential

### Parameters

- `CredentialCreateParams params`

  - `Optional<String> vaultId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `Auth auth`

    Authentication details for creating a credential.

    - `class BetaManagedAgentsMcpOAuthCreateParams:`

      Parameters for creating an MCP OAuth credential.

      - `String accessToken`

        OAuth access token.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `MCP_OAUTH("mcp_oauth")`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

      - `Optional<BetaManagedAgentsMcpOAuthRefreshParams> refresh`

        OAuth refresh token parameters for creating a credential with refresh support.

        - `String clientId`

          OAuth client ID.

        - `String refreshToken`

          OAuth refresh token.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

            Token endpoint requires no client authentication.

            - `Type type`

              - `NONE("none")`

          - `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `String clientSecret`

              OAuth client secret.

            - `Type type`

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `class BetaManagedAgentsTokenEndpointAuthPostParam:`

            Token endpoint uses POST body authentication with client credentials.

            - `String clientSecret`

              OAuth client secret.

            - `Type type`

              - `CLIENT_SECRET_POST("client_secret_post")`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerCreateParams:`

      Parameters for creating a static bearer token credential.

      - `String token`

        Static bearer token value.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `STATIC_BEARER("static_bearer")`

    - `class BetaManagedAgentsEnvironmentVariableCreateParams:`

      Parameters for creating an environment variable credential.

      - `BetaManagedAgentsCredentialNetworkingParams networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `Type type`

            - `UNRESTRICTED("unrestricted")`

        - `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

          Substitute the secret only on requests to the listed hosts.

          - `List<String> allowedHosts`

            Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

          - `Type type`

            - `LIMITED("limited")`

      - `String secretName`

        Name of the environment variable. Immutable after create.

      - `String secretValue`

        Secret value. Write-only; never returned in responses.

      - `Type type`

        - `ENVIRONMENT_VARIABLE("environment_variable")`

      - `Optional<BetaManagedAgentsInjectionLocationParams> injectionLocation`

        Where in the outbound request the secret value may be substituted.

        - `Optional<Boolean> body`

          Substitute when the placeholder appears in the request body.

        - `Optional<Boolean> header`

          Substitute when the placeholder appears in a request header value.

  - `Optional<String> displayName`

    Human-readable name for the credential. Up to 255 characters.

  - `Optional<Metadata> metadata`

    Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `MCP_OAUTH("mcp_oauth")`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

              - `NONE("none")`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_POST("client_secret_post")`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `STATIC_BEARER("static_bearer")`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `BetaManagedAgentsInjectionLocationResponse injectionLocation`

        Where in the outbound request the secret value is substituted.

        - `boolean body`

          Whether the placeholder is substituted in the request body.

        - `boolean header`

          Whether the placeholder is substituted in request header values.

      - `Networking networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type type`

            - `UNRESTRICTED("unrestricted")`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `List<String> allowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type type`

            - `LIMITED("limited")`

      - `String secretName`

        Name of the environment variable.

      - `Type type`

        - `ENVIRONMENT_VARIABLE("environment_variable")`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

    - `VAULT_CREDENTIAL("vault_credential")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsStaticBearerCreateParams;
import com.anthropic.models.beta.vaults.credentials.CredentialCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialCreateParams params = CredentialCreateParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .auth(BetaManagedAgentsStaticBearerCreateParams.builder()
                .token("bearer_exampletoken")
                .mcpServerUrl("https://example-server.modelcontextprotocol.io/sse")
                .type(BetaManagedAgentsStaticBearerCreateParams.Type.STATIC_BEARER)
                .build())
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().create(params);
    }
}
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

`CredentialListPage beta().vaults().credentials().list(CredentialListParamsparams = CredentialListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Parameters

- `CredentialListParams params`

  - `Optional<String> vaultId`

  - `Optional<Boolean> includeArchived`

    Whether to include archived credentials in the results.

  - `Optional<Long> limit`

    Maximum number of credentials to return per page. Defaults to 20, maximum 100.

  - `Optional<String> page`

    Opaque pagination token from a previous `list_credentials` response.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `MCP_OAUTH("mcp_oauth")`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

              - `NONE("none")`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_POST("client_secret_post")`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `STATIC_BEARER("static_bearer")`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `BetaManagedAgentsInjectionLocationResponse injectionLocation`

        Where in the outbound request the secret value is substituted.

        - `boolean body`

          Whether the placeholder is substituted in the request body.

        - `boolean header`

          Whether the placeholder is substituted in request header values.

      - `Networking networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type type`

            - `UNRESTRICTED("unrestricted")`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `List<String> allowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type type`

            - `LIMITED("limited")`

      - `String secretName`

        Name of the environment variable.

      - `Type type`

        - `ENVIRONMENT_VARIABLE("environment_variable")`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

    - `VAULT_CREDENTIAL("vault_credential")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.CredentialListPage;
import com.anthropic.models.beta.vaults.credentials.CredentialListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialListPage page = client.beta().vaults().credentials().list("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
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

`BetaManagedAgentsCredential beta().vaults().credentials().retrieve(CredentialRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

### Parameters

- `CredentialRetrieveParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `MCP_OAUTH("mcp_oauth")`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

              - `NONE("none")`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_POST("client_secret_post")`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `STATIC_BEARER("static_bearer")`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `BetaManagedAgentsInjectionLocationResponse injectionLocation`

        Where in the outbound request the secret value is substituted.

        - `boolean body`

          Whether the placeholder is substituted in the request body.

        - `boolean header`

          Whether the placeholder is substituted in request header values.

      - `Networking networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type type`

            - `UNRESTRICTED("unrestricted")`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `List<String> allowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type type`

            - `LIMITED("limited")`

      - `String secretName`

        Name of the environment variable.

      - `Type type`

        - `ENVIRONMENT_VARIABLE("environment_variable")`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

    - `VAULT_CREDENTIAL("vault_credential")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.CredentialRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialRetrieveParams params = CredentialRetrieveParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().retrieve(params);
    }
}
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

`BetaManagedAgentsCredential beta().vaults().credentials().update(CredentialUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Parameters

- `CredentialUpdateParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `Optional<Auth> auth`

    Updated authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthUpdateParams:`

      Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

      - `Type type`

        - `MCP_OAUTH("mcp_oauth")`

      - `Optional<String> accessToken`

        Updated OAuth access token.

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

      - `Optional<BetaManagedAgentsMcpOAuthRefreshUpdateParams> refresh`

        Parameters for updating OAuth refresh token configuration.

        - `Optional<String> refreshToken`

          Updated OAuth refresh token.

        - `Optional<String> scope`

          Updated OAuth scope for the refresh request.

        - `Optional<TokenEndpointAuth> tokenEndpointAuth`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

            Updated HTTP Basic authentication parameters for the token endpoint.

            - `Type type`

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

            - `Optional<String> clientSecret`

              Updated OAuth client secret.

          - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

            Updated POST body authentication parameters for the token endpoint.

            - `Type type`

              - `CLIENT_SECRET_POST("client_secret_post")`

            - `Optional<String> clientSecret`

              Updated OAuth client secret.

    - `class BetaManagedAgentsStaticBearerUpdateParams:`

      Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

      - `Type type`

        - `STATIC_BEARER("static_bearer")`

      - `Optional<String> token`

        Updated static bearer token value.

    - `class BetaManagedAgentsEnvironmentVariableUpdateParams:`

      Parameters for updating an environment variable credential. `secret_name` is immutable.

      - `Type type`

        - `ENVIRONMENT_VARIABLE("environment_variable")`

      - `Optional<BetaManagedAgentsInjectionLocationUpdateParams> injectionLocation`

        Updated injection location.

        - `Optional<Boolean> body`

          Substitute when the placeholder appears in the request body.

        - `Optional<Boolean> header`

          Substitute when the placeholder appears in a request header value.

      - `Optional<BetaManagedAgentsCredentialNetworkingParams> networking`

        Updated networking scope. Full replacement.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `Type type`

            - `UNRESTRICTED("unrestricted")`

        - `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

          Substitute the secret only on requests to the listed hosts.

          - `List<String> allowedHosts`

            Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

          - `Type type`

            - `LIMITED("limited")`

      - `Optional<String> secretValue`

        Updated secret value.

  - `Optional<String> displayName`

    Updated human-readable name for the credential. 1-255 characters.

  - `Optional<Metadata> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `MCP_OAUTH("mcp_oauth")`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

              - `NONE("none")`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_POST("client_secret_post")`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `STATIC_BEARER("static_bearer")`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `BetaManagedAgentsInjectionLocationResponse injectionLocation`

        Where in the outbound request the secret value is substituted.

        - `boolean body`

          Whether the placeholder is substituted in the request body.

        - `boolean header`

          Whether the placeholder is substituted in request header values.

      - `Networking networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type type`

            - `UNRESTRICTED("unrestricted")`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `List<String> allowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type type`

            - `LIMITED("limited")`

      - `String secretName`

        Name of the environment variable.

      - `Type type`

        - `ENVIRONMENT_VARIABLE("environment_variable")`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

    - `VAULT_CREDENTIAL("vault_credential")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.CredentialUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialUpdateParams params = CredentialUpdateParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().update(params);
    }
}
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

`BetaManagedAgentsDeletedCredential beta().vaults().credentials().delete(CredentialDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

### Parameters

- `CredentialDeleteParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsDeletedCredential:`

  Confirmation of a deleted credential.

  - `String id`

    Unique identifier of the deleted credential.

  - `Type type`

    - `VAULT_CREDENTIAL_DELETED("vault_credential_deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsDeletedCredential;
import com.anthropic.models.beta.vaults.credentials.CredentialDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialDeleteParams params = CredentialDeleteParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsDeletedCredential betaManagedAgentsDeletedCredential = client.beta().vaults().credentials().delete(params);
    }
}
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

## Archive Credential

`BetaManagedAgentsCredential beta().vaults().credentials().archive(CredentialArchiveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

### Parameters

- `CredentialArchiveParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `MCP_OAUTH("mcp_oauth")`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

              - `NONE("none")`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_POST("client_secret_post")`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `STATIC_BEARER("static_bearer")`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `BetaManagedAgentsInjectionLocationResponse injectionLocation`

        Where in the outbound request the secret value is substituted.

        - `boolean body`

          Whether the placeholder is substituted in the request body.

        - `boolean header`

          Whether the placeholder is substituted in request header values.

      - `Networking networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type type`

            - `UNRESTRICTED("unrestricted")`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `List<String> allowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type type`

            - `LIMITED("limited")`

      - `String secretName`

        Name of the environment variable.

      - `Type type`

        - `ENVIRONMENT_VARIABLE("environment_variable")`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

    - `VAULT_CREDENTIAL("vault_credential")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.CredentialArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialArchiveParams params = CredentialArchiveParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().archive(params);
    }
}
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

`BetaManagedAgentsCredentialValidation beta().vaults().credentials().mcpOAuthValidate(CredentialMcpOAuthValidateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

### Parameters

- `CredentialMcpOAuthValidateParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsCredentialValidation:`

  Result of live-probing a credential against its configured MCP server.

  - `String credentialId`

    Unique identifier of the credential that was validated.

  - `boolean hasRefreshToken`

    Whether the credential has a refresh token configured.

  - `Optional<BetaManagedAgentsMcpProbe> mcpProbe`

    The failing step of an MCP validation probe.

    - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

      An HTTP response captured during a credential validation probe.

      - `String body`

        Response body. May be truncated and has sensitive values scrubbed.

      - `boolean bodyTruncated`

        Whether `body` was truncated.

      - `String contentType`

        Value of the `Content-Type` response header.

      - `long statusCode`

        HTTP status code.

    - `String method`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `Optional<BetaManagedAgentsRefreshObject> refresh`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

      An HTTP response captured during a credential validation probe.

    - `Status status`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `SUCCEEDED("succeeded")`

      - `FAILED("failed")`

      - `CONNECT_ERROR("connect_error")`

      - `NO_REFRESH_TOKEN("no_refresh_token")`

  - `BetaManagedAgentsCredentialValidationStatus status`

    Overall verdict of a credential validation probe.

    - `VALID("valid")`

    - `INVALID("invalid")`

    - `UNKNOWN("unknown")`

  - `Type type`

    - `VAULT_CREDENTIAL_VALIDATION("vault_credential_validation")`

  - `LocalDateTime validatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault containing the credential.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredentialValidation;
import com.anthropic.models.beta.vaults.credentials.CredentialMcpOAuthValidateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialMcpOAuthValidateParams params = CredentialMcpOAuthValidateParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsCredentialValidation betaManagedAgentsCredentialValidation = client.beta().vaults().credentials().mcpOAuthValidate(params);
    }
}
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

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `MCP_OAUTH("mcp_oauth")`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

              - `NONE("none")`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_POST("client_secret_post")`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `STATIC_BEARER("static_bearer")`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `BetaManagedAgentsInjectionLocationResponse injectionLocation`

        Where in the outbound request the secret value is substituted.

        - `boolean body`

          Whether the placeholder is substituted in the request body.

        - `boolean header`

          Whether the placeholder is substituted in request header values.

      - `Networking networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type type`

            - `UNRESTRICTED("unrestricted")`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `List<String> allowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type type`

            - `LIMITED("limited")`

      - `String secretName`

        Name of the environment variable.

      - `Type type`

        - `ENVIRONMENT_VARIABLE("environment_variable")`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

    - `VAULT_CREDENTIAL("vault_credential")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

### Beta Managed Agents Credential Networking Params

- `class BetaManagedAgentsCredentialNetworkingParams: A class that can be one of several variants.union`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

    Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

    - `Type type`

      - `UNRESTRICTED("unrestricted")`

  - `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

    Substitute the secret only on requests to the listed hosts.

    - `List<String> allowedHosts`

      Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

    - `Type type`

      - `LIMITED("limited")`

### Beta Managed Agents Credential Validation

- `class BetaManagedAgentsCredentialValidation:`

  Result of live-probing a credential against its configured MCP server.

  - `String credentialId`

    Unique identifier of the credential that was validated.

  - `boolean hasRefreshToken`

    Whether the credential has a refresh token configured.

  - `Optional<BetaManagedAgentsMcpProbe> mcpProbe`

    The failing step of an MCP validation probe.

    - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

      An HTTP response captured during a credential validation probe.

      - `String body`

        Response body. May be truncated and has sensitive values scrubbed.

      - `boolean bodyTruncated`

        Whether `body` was truncated.

      - `String contentType`

        Value of the `Content-Type` response header.

      - `long statusCode`

        HTTP status code.

    - `String method`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `Optional<BetaManagedAgentsRefreshObject> refresh`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

      An HTTP response captured during a credential validation probe.

    - `Status status`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `SUCCEEDED("succeeded")`

      - `FAILED("failed")`

      - `CONNECT_ERROR("connect_error")`

      - `NO_REFRESH_TOKEN("no_refresh_token")`

  - `BetaManagedAgentsCredentialValidationStatus status`

    Overall verdict of a credential validation probe.

    - `VALID("valid")`

    - `INVALID("invalid")`

    - `UNKNOWN("unknown")`

  - `Type type`

    - `VAULT_CREDENTIAL_VALIDATION("vault_credential_validation")`

  - `LocalDateTime validatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault containing the credential.

### Beta Managed Agents Credential Validation Status

- `enum BetaManagedAgentsCredentialValidationStatus:`

  Overall verdict of a credential validation probe.

  - `VALID("valid")`

  - `INVALID("invalid")`

  - `UNKNOWN("unknown")`

### Beta Managed Agents Deleted Credential

- `class BetaManagedAgentsDeletedCredential:`

  Confirmation of a deleted credential.

  - `String id`

    Unique identifier of the deleted credential.

  - `Type type`

    - `VAULT_CREDENTIAL_DELETED("vault_credential_deleted")`

### Beta Managed Agents Environment Variable Auth Response

- `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

  Environment variable credential details. The secret value is never returned.

  - `BetaManagedAgentsInjectionLocationResponse injectionLocation`

    Where in the outbound request the secret value is substituted.

    - `boolean body`

      Whether the placeholder is substituted in the request body.

    - `boolean header`

      Whether the placeholder is substituted in request header values.

  - `Networking networking`

    Outbound hosts the secret value is substituted on.

    - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

      The secret is substituted on any host the session's Environment network policy permits egress to.

      - `Type type`

        - `UNRESTRICTED("unrestricted")`

    - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

      The secret is substituted only on requests to the listed hosts.

      - `List<String> allowedHosts`

        Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

      - `Type type`

        - `LIMITED("limited")`

  - `String secretName`

    Name of the environment variable.

  - `Type type`

    - `ENVIRONMENT_VARIABLE("environment_variable")`

### Beta Managed Agents Environment Variable Create Params

- `class BetaManagedAgentsEnvironmentVariableCreateParams:`

  Parameters for creating an environment variable credential.

  - `BetaManagedAgentsCredentialNetworkingParams networking`

    Outbound hosts the secret value is substituted on.

    - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `Type type`

        - `UNRESTRICTED("unrestricted")`

    - `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

      Substitute the secret only on requests to the listed hosts.

      - `List<String> allowedHosts`

        Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

      - `Type type`

        - `LIMITED("limited")`

  - `String secretName`

    Name of the environment variable. Immutable after create.

  - `String secretValue`

    Secret value. Write-only; never returned in responses.

  - `Type type`

    - `ENVIRONMENT_VARIABLE("environment_variable")`

  - `Optional<BetaManagedAgentsInjectionLocationParams> injectionLocation`

    Where in the outbound request the secret value may be substituted.

    - `Optional<Boolean> body`

      Substitute when the placeholder appears in the request body.

    - `Optional<Boolean> header`

      Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Environment Variable Update Params

- `class BetaManagedAgentsEnvironmentVariableUpdateParams:`

  Parameters for updating an environment variable credential. `secret_name` is immutable.

  - `Type type`

    - `ENVIRONMENT_VARIABLE("environment_variable")`

  - `Optional<BetaManagedAgentsInjectionLocationUpdateParams> injectionLocation`

    Updated injection location.

    - `Optional<Boolean> body`

      Substitute when the placeholder appears in the request body.

    - `Optional<Boolean> header`

      Substitute when the placeholder appears in a request header value.

  - `Optional<BetaManagedAgentsCredentialNetworkingParams> networking`

    Updated networking scope. Full replacement.

    - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `Type type`

        - `UNRESTRICTED("unrestricted")`

    - `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

      Substitute the secret only on requests to the listed hosts.

      - `List<String> allowedHosts`

        Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

      - `Type type`

        - `LIMITED("limited")`

  - `Optional<String> secretValue`

    Updated secret value.

### Beta Managed Agents Injection Location Params

- `class BetaManagedAgentsInjectionLocationParams:`

  Where in the outbound request the secret value may be substituted.

  - `Optional<Boolean> body`

    Substitute when the placeholder appears in the request body.

  - `Optional<Boolean> header`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Injection Location Response

- `class BetaManagedAgentsInjectionLocationResponse:`

  Where in the outbound request the secret value is substituted.

  - `boolean body`

    Whether the placeholder is substituted in the request body.

  - `boolean header`

    Whether the placeholder is substituted in request header values.

### Beta Managed Agents Injection Location Update Params

- `class BetaManagedAgentsInjectionLocationUpdateParams:`

  Updated injection location.

  - `Optional<Boolean> body`

    Substitute when the placeholder appears in the request body.

  - `Optional<Boolean> header`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Limited Credential Networking Params

- `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

  Substitute the secret only on requests to the listed hosts.

  - `List<String> allowedHosts`

    Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

  - `Type type`

    - `LIMITED("limited")`

### Beta Managed Agents Limited Credential Networking Response

- `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

  The secret is substituted only on requests to the listed hosts.

  - `List<String> allowedHosts`

    Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

  - `Type type`

    - `LIMITED("limited")`

### Beta Managed Agents MCP OAuth Auth Response

- `class BetaManagedAgentsMcpOAuthAuthResponse:`

  OAuth credential details for an MCP server.

  - `String mcpServerUrl`

    URL of the MCP server this credential authenticates against.

  - `Type type`

    - `MCP_OAUTH("mcp_oauth")`

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

    OAuth refresh token configuration returned in credential responses.

    - `String clientId`

      OAuth client ID.

    - `String tokenEndpoint`

      Token endpoint URL used to refresh the access token.

    - `TokenEndpointAuth tokenEndpointAuth`

      Token endpoint requires no client authentication.

      - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

        Token endpoint requires no client authentication.

        - `Type type`

          - `NONE("none")`

      - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `Type type`

          - `CLIENT_SECRET_BASIC("client_secret_basic")`

      - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

        Token endpoint uses POST body authentication with client credentials.

        - `Type type`

          - `CLIENT_SECRET_POST("client_secret_post")`

    - `Optional<String> resource`

      OAuth resource indicator.

    - `Optional<String> scope`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Create Params

- `class BetaManagedAgentsMcpOAuthCreateParams:`

  Parameters for creating an MCP OAuth credential.

  - `String accessToken`

    OAuth access token.

  - `String mcpServerUrl`

    URL of the MCP server this credential authenticates against.

  - `Type type`

    - `MCP_OAUTH("mcp_oauth")`

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsMcpOAuthRefreshParams> refresh`

    OAuth refresh token parameters for creating a credential with refresh support.

    - `String clientId`

      OAuth client ID.

    - `String refreshToken`

      OAuth refresh token.

    - `String tokenEndpoint`

      Token endpoint URL used to refresh the access token.

    - `TokenEndpointAuth tokenEndpointAuth`

      Token endpoint requires no client authentication.

      - `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

        Token endpoint requires no client authentication.

        - `Type type`

          - `NONE("none")`

      - `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `String clientSecret`

          OAuth client secret.

        - `Type type`

          - `CLIENT_SECRET_BASIC("client_secret_basic")`

      - `class BetaManagedAgentsTokenEndpointAuthPostParam:`

        Token endpoint uses POST body authentication with client credentials.

        - `String clientSecret`

          OAuth client secret.

        - `Type type`

          - `CLIENT_SECRET_POST("client_secret_post")`

    - `Optional<String> resource`

      OAuth resource indicator.

    - `Optional<String> scope`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Params

- `class BetaManagedAgentsMcpOAuthRefreshParams:`

  OAuth refresh token parameters for creating a credential with refresh support.

  - `String clientId`

    OAuth client ID.

  - `String refreshToken`

    OAuth refresh token.

  - `String tokenEndpoint`

    Token endpoint URL used to refresh the access token.

  - `TokenEndpointAuth tokenEndpointAuth`

    Token endpoint requires no client authentication.

    - `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

      Token endpoint requires no client authentication.

      - `Type type`

        - `NONE("none")`

    - `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `String clientSecret`

        OAuth client secret.

      - `Type type`

        - `CLIENT_SECRET_BASIC("client_secret_basic")`

    - `class BetaManagedAgentsTokenEndpointAuthPostParam:`

      Token endpoint uses POST body authentication with client credentials.

      - `String clientSecret`

        OAuth client secret.

      - `Type type`

        - `CLIENT_SECRET_POST("client_secret_post")`

  - `Optional<String> resource`

    OAuth resource indicator.

  - `Optional<String> scope`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Response

- `class BetaManagedAgentsMcpOAuthRefreshResponse:`

  OAuth refresh token configuration returned in credential responses.

  - `String clientId`

    OAuth client ID.

  - `String tokenEndpoint`

    Token endpoint URL used to refresh the access token.

  - `TokenEndpointAuth tokenEndpointAuth`

    Token endpoint requires no client authentication.

    - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

      Token endpoint requires no client authentication.

      - `Type type`

        - `NONE("none")`

    - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `Type type`

        - `CLIENT_SECRET_BASIC("client_secret_basic")`

    - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

      Token endpoint uses POST body authentication with client credentials.

      - `Type type`

        - `CLIENT_SECRET_POST("client_secret_post")`

  - `Optional<String> resource`

    OAuth resource indicator.

  - `Optional<String> scope`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Update Params

- `class BetaManagedAgentsMcpOAuthRefreshUpdateParams:`

  Parameters for updating OAuth refresh token configuration.

  - `Optional<String> refreshToken`

    Updated OAuth refresh token.

  - `Optional<String> scope`

    Updated OAuth scope for the refresh request.

  - `Optional<TokenEndpointAuth> tokenEndpointAuth`

    Updated HTTP Basic authentication parameters for the token endpoint.

    - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `Type type`

        - `CLIENT_SECRET_BASIC("client_secret_basic")`

      - `Optional<String> clientSecret`

        Updated OAuth client secret.

    - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

      Updated POST body authentication parameters for the token endpoint.

      - `Type type`

        - `CLIENT_SECRET_POST("client_secret_post")`

      - `Optional<String> clientSecret`

        Updated OAuth client secret.

### Beta Managed Agents MCP OAuth Update Params

- `class BetaManagedAgentsMcpOAuthUpdateParams:`

  Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

  - `Type type`

    - `MCP_OAUTH("mcp_oauth")`

  - `Optional<String> accessToken`

    Updated OAuth access token.

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsMcpOAuthRefreshUpdateParams> refresh`

    Parameters for updating OAuth refresh token configuration.

    - `Optional<String> refreshToken`

      Updated OAuth refresh token.

    - `Optional<String> scope`

      Updated OAuth scope for the refresh request.

    - `Optional<TokenEndpointAuth> tokenEndpointAuth`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `Type type`

          - `CLIENT_SECRET_BASIC("client_secret_basic")`

        - `Optional<String> clientSecret`

          Updated OAuth client secret.

      - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

        Updated POST body authentication parameters for the token endpoint.

        - `Type type`

          - `CLIENT_SECRET_POST("client_secret_post")`

        - `Optional<String> clientSecret`

          Updated OAuth client secret.

### Beta Managed Agents MCP Probe

- `class BetaManagedAgentsMcpProbe:`

  The failing step of an MCP validation probe.

  - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

    An HTTP response captured during a credential validation probe.

    - `String body`

      Response body. May be truncated and has sensitive values scrubbed.

    - `boolean bodyTruncated`

      Whether `body` was truncated.

    - `String contentType`

      Value of the `Content-Type` response header.

    - `long statusCode`

      HTTP status code.

  - `String method`

    The MCP method that failed (for example `initialize` or `tools/list`).

### Beta Managed Agents Refresh HTTP Response

- `class BetaManagedAgentsRefreshHttpResponse:`

  An HTTP response captured during a credential validation probe.

  - `String body`

    Response body. May be truncated and has sensitive values scrubbed.

  - `boolean bodyTruncated`

    Whether `body` was truncated.

  - `String contentType`

    Value of the `Content-Type` response header.

  - `long statusCode`

    HTTP status code.

### Beta Managed Agents Refresh Object

- `class BetaManagedAgentsRefreshObject:`

  Outcome of a refresh-token exchange attempted during credential validation.

  - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

    An HTTP response captured during a credential validation probe.

    - `String body`

      Response body. May be truncated and has sensitive values scrubbed.

    - `boolean bodyTruncated`

      Whether `body` was truncated.

    - `String contentType`

      Value of the `Content-Type` response header.

    - `long statusCode`

      HTTP status code.

  - `Status status`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `SUCCEEDED("succeeded")`

    - `FAILED("failed")`

    - `CONNECT_ERROR("connect_error")`

    - `NO_REFRESH_TOKEN("no_refresh_token")`

### Beta Managed Agents Static Bearer Auth Response

- `class BetaManagedAgentsStaticBearerAuthResponse:`

  Static bearer token credential details for an MCP server.

  - `String mcpServerUrl`

    URL of the MCP server this credential authenticates against.

  - `Type type`

    - `STATIC_BEARER("static_bearer")`

### Beta Managed Agents Static Bearer Create Params

- `class BetaManagedAgentsStaticBearerCreateParams:`

  Parameters for creating a static bearer token credential.

  - `String token`

    Static bearer token value.

  - `String mcpServerUrl`

    URL of the MCP server this credential authenticates against.

  - `Type type`

    - `STATIC_BEARER("static_bearer")`

### Beta Managed Agents Static Bearer Update Params

- `class BetaManagedAgentsStaticBearerUpdateParams:`

  Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

  - `Type type`

    - `STATIC_BEARER("static_bearer")`

  - `Optional<String> token`

    Updated static bearer token value.

### Beta Managed Agents Token Endpoint Auth Basic Param

- `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `String clientSecret`

    OAuth client secret.

  - `Type type`

    - `CLIENT_SECRET_BASIC("client_secret_basic")`

### Beta Managed Agents Token Endpoint Auth Basic Response

- `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `Type type`

    - `CLIENT_SECRET_BASIC("client_secret_basic")`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

  Updated HTTP Basic authentication parameters for the token endpoint.

  - `Type type`

    - `CLIENT_SECRET_BASIC("client_secret_basic")`

  - `Optional<String> clientSecret`

    Updated OAuth client secret.

### Beta Managed Agents Token Endpoint Auth None Param

- `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

  Token endpoint requires no client authentication.

  - `Type type`

    - `NONE("none")`

### Beta Managed Agents Token Endpoint Auth None Response

- `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

  Token endpoint requires no client authentication.

  - `Type type`

    - `NONE("none")`

### Beta Managed Agents Token Endpoint Auth Post Param

- `class BetaManagedAgentsTokenEndpointAuthPostParam:`

  Token endpoint uses POST body authentication with client credentials.

  - `String clientSecret`

    OAuth client secret.

  - `Type type`

    - `CLIENT_SECRET_POST("client_secret_post")`

### Beta Managed Agents Token Endpoint Auth Post Response

- `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

  Token endpoint uses POST body authentication with client credentials.

  - `Type type`

    - `CLIENT_SECRET_POST("client_secret_post")`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

  Updated POST body authentication parameters for the token endpoint.

  - `Type type`

    - `CLIENT_SECRET_POST("client_secret_post")`

  - `Optional<String> clientSecret`

    Updated OAuth client secret.

### Beta Managed Agents Unrestricted Credential Networking Params

- `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `Type type`

    - `UNRESTRICTED("unrestricted")`

### Beta Managed Agents Unrestricted Credential Networking Response

- `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

  The secret is substituted on any host the session's Environment network policy permits egress to.

  - `Type type`

    - `UNRESTRICTED("unrestricted")`

# Memory Stores

## Create a memory store

`BetaManagedAgentsMemoryStore beta().memoryStores().create(MemoryStoreCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/memory_stores`

Create a memory store

### Parameters

- `MemoryStoreCreateParams params`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `String name`

    Human-readable name for the store. Required; 1–255 characters; no control characters. The mount-path slug under `/mnt/memory/` is derived from this name (lowercased, non-alphanumeric runs collapsed to a hyphen). Names need not be unique within a workspace.

  - `Optional<String> description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent.

  - `Optional<Metadata> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Not visible to the agent.

### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `String id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type type`

    - `MEMORY_STORE("memory_store")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `Optional<Metadata> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.BetaManagedAgentsMemoryStore;
import com.anthropic.models.beta.memorystores.MemoryStoreCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryStoreCreateParams params = MemoryStoreCreateParams.builder()
            .name("x")
            .build();
        BetaManagedAgentsMemoryStore betaManagedAgentsMemoryStore = client.beta().memoryStores().create(params);
    }
}
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

`MemoryStoreListPage beta().memoryStores().list(MemoryStoreListParamsparams = MemoryStoreListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/memory_stores`

List memory stores

### Parameters

- `MemoryStoreListParams params`

  - `Optional<LocalDateTime> createdAtGte`

    Return only stores whose `created_at` is at or after this time (inclusive). Sent on the wire as `created_at[gte]`.

  - `Optional<LocalDateTime> createdAtLte`

    Return only stores whose `created_at` is at or before this time (inclusive). Sent on the wire as `created_at[lte]`.

  - `Optional<Boolean> includeArchived`

    When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

  - `Optional<Long> limit`

    Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

  - `Optional<String> page`

    Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `String id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type type`

    - `MEMORY_STORE("memory_store")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `Optional<Metadata> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.MemoryStoreListPage;
import com.anthropic.models.beta.memorystores.MemoryStoreListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryStoreListPage page = client.beta().memoryStores().list();
    }
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

`BetaManagedAgentsMemoryStore beta().memoryStores().retrieve(MemoryStoreRetrieveParamsparams = MemoryStoreRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/memory_stores/{memory_store_id}`

Retrieve a memory store

### Parameters

- `MemoryStoreRetrieveParams params`

  - `Optional<String> memoryStoreId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `String id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type type`

    - `MEMORY_STORE("memory_store")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `Optional<Metadata> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.BetaManagedAgentsMemoryStore;
import com.anthropic.models.beta.memorystores.MemoryStoreRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsMemoryStore betaManagedAgentsMemoryStore = client.beta().memoryStores().retrieve("memory_store_id");
    }
}
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

`BetaManagedAgentsMemoryStore beta().memoryStores().update(MemoryStoreUpdateParamsparams = MemoryStoreUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/memory_stores/{memory_store_id}`

Update a memory store

### Parameters

- `MemoryStoreUpdateParams params`

  - `Optional<String> memoryStoreId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `Optional<String> description`

    New description for the store, up to 1024 characters. Pass an empty string to clear it.

  - `Optional<Metadata> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `Optional<String> name`

    New human-readable name for the store. 1–255 characters; no control characters. Renaming changes the slug used for the store's `mount_path` in sessions created after the update.

### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `String id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type type`

    - `MEMORY_STORE("memory_store")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `Optional<Metadata> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.BetaManagedAgentsMemoryStore;
import com.anthropic.models.beta.memorystores.MemoryStoreUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsMemoryStore betaManagedAgentsMemoryStore = client.beta().memoryStores().update("memory_store_id");
    }
}
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

`BetaManagedAgentsDeletedMemoryStore beta().memoryStores().delete(MemoryStoreDeleteParamsparams = MemoryStoreDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/memory_stores/{memory_store_id}`

Delete a memory store

### Parameters

- `MemoryStoreDeleteParams params`

  - `Optional<String> memoryStoreId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsDeletedMemoryStore:`

  Confirmation that a `memory_store` was deleted.

  - `String id`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `Type type`

    - `MEMORY_STORE_DELETED("memory_store_deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.BetaManagedAgentsDeletedMemoryStore;
import com.anthropic.models.beta.memorystores.MemoryStoreDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeletedMemoryStore betaManagedAgentsDeletedMemoryStore = client.beta().memoryStores().delete("memory_store_id");
    }
}
```

#### Response

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

## Archive a memory store

`BetaManagedAgentsMemoryStore beta().memoryStores().archive(MemoryStoreArchiveParamsparams = MemoryStoreArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/memory_stores/{memory_store_id}/archive`

Archive a memory store

### Parameters

- `MemoryStoreArchiveParams params`

  - `Optional<String> memoryStoreId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `String id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type type`

    - `MEMORY_STORE("memory_store")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `Optional<Metadata> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.BetaManagedAgentsMemoryStore;
import com.anthropic.models.beta.memorystores.MemoryStoreArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsMemoryStore betaManagedAgentsMemoryStore = client.beta().memoryStores().archive("memory_store_id");
    }
}
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

  - `String id`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `Type type`

    - `MEMORY_STORE_DELETED("memory_store_deleted")`

### Beta Managed Agents Memory Store

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `String id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type type`

    - `MEMORY_STORE("memory_store")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `Optional<Metadata> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

# Memories

## Create a memory

`BetaManagedAgentsMemory beta().memoryStores().memories().create(MemoryCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/memory_stores/{memory_store_id}/memories`

Create a memory

### Parameters

- `MemoryCreateParams params`

  - `Optional<String> memoryStoreId`

  - `Optional<BetaManagedAgentsMemoryView> view`

    Query parameter for view

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `Optional<String> content`

    UTF-8 text content for the new memory. Maximum 100 kB (102,400 bytes). Required; pass `""` explicitly to create an empty memory.

  - `String path`

    Hierarchical path for the new memory, e.g. `/projects/foo/notes.md`. Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive.

### Returns

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `String id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `String contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `long contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String memoryStoreId`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `String memoryVersionId`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `String path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type type`

    - `MEMORY("memory")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<String> content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memories.BetaManagedAgentsMemory;
import com.anthropic.models.beta.memorystores.memories.MemoryCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryCreateParams params = MemoryCreateParams.builder()
            .memoryStoreId("memory_store_id")
            .content("content")
            .path("xx")
            .build();
        BetaManagedAgentsMemory betaManagedAgentsMemory = client.beta().memoryStores().memories().create(params);
    }
}
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

`MemoryListPage beta().memoryStores().memories().list(MemoryListParamsparams = MemoryListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/memory_stores/{memory_store_id}/memories`

List memories

### Parameters

- `MemoryListParams params`

  - `Optional<String> memoryStoreId`

  - `Optional<Long> depth`

    `0` (or omitted) returns all descendants below `path_prefix` (recursive). `1` returns immediate children only; deeper entries roll up as `memory_prefix` items. `depth=1` behaves like `ls`; omitting `depth` behaves like `find`.

  - `Optional<Long> limit`

    Maximum number of items to return per page. Must be between 1 and 100. Defaults to 20 when omitted. Capped at 20 when `view=full`. Both `memory` and `memory_prefix` items count toward the limit.

  - `Optional<String> page`

    Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

  - `Optional<String> pathPrefix`

    Optional path prefix filter. Must end with `/` (segment-aligned), e.g., `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

  - `Optional<BetaManagedAgentsMemoryView> view`

    Which projection of each `memory` to return. Defaults to `basic` (content omitted). `full` populates `content` on each item and caps `limit` at 20; use this as the bulk-read path for export and sync.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsMemoryListItem: A class that can be one of several variants.union`

  One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

  - `class BetaManagedAgentsMemory:`

    A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

    - `String id`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `String contentSha256`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `long contentSizeBytes`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

    - `String memoryStoreId`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `String memoryVersionId`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `String path`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `Type type`

      - `MEMORY("memory")`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

    - `Optional<String> content`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `class BetaManagedAgentsMemoryPrefix:`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `String path`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `Type type`

      - `MEMORY_PREFIX("memory_prefix")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memories.MemoryListPage;
import com.anthropic.models.beta.memorystores.memories.MemoryListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryListPage page = client.beta().memoryStores().memories().list("memory_store_id");
    }
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

`BetaManagedAgentsMemory beta().memoryStores().memories().retrieve(MemoryRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a memory

### Parameters

- `MemoryRetrieveParams params`

  - `String memoryStoreId`

  - `Optional<String> memoryId`

  - `Optional<BetaManagedAgentsMemoryView> view`

    Query parameter for view

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `String id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `String contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `long contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String memoryStoreId`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `String memoryVersionId`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `String path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type type`

    - `MEMORY("memory")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<String> content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memories.BetaManagedAgentsMemory;
import com.anthropic.models.beta.memorystores.memories.MemoryRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryRetrieveParams params = MemoryRetrieveParams.builder()
            .memoryStoreId("memory_store_id")
            .memoryId("memory_id")
            .build();
        BetaManagedAgentsMemory betaManagedAgentsMemory = client.beta().memoryStores().memories().retrieve(params);
    }
}
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

`BetaManagedAgentsMemory beta().memoryStores().memories().update(MemoryUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a memory

### Parameters

- `MemoryUpdateParams params`

  - `String memoryStoreId`

  - `Optional<String> memoryId`

  - `Optional<BetaManagedAgentsMemoryView> view`

    Query parameter for view

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `Optional<String> content`

    New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

  - `Optional<String> path`

    New path for the memory (a rename). Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive. The memory's `id` is preserved across renames. Omit to leave the path unchanged.

  - `Optional<BetaManagedAgentsPrecondition> precondition`

    Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

### Returns

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `String id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `String contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `long contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String memoryStoreId`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `String memoryVersionId`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `String path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type type`

    - `MEMORY("memory")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<String> content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memories.BetaManagedAgentsMemory;
import com.anthropic.models.beta.memorystores.memories.MemoryUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryUpdateParams params = MemoryUpdateParams.builder()
            .memoryStoreId("memory_store_id")
            .memoryId("memory_id")
            .build();
        BetaManagedAgentsMemory betaManagedAgentsMemory = client.beta().memoryStores().memories().update(params);
    }
}
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

`BetaManagedAgentsDeletedMemory beta().memoryStores().memories().delete(MemoryDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

### Parameters

- `MemoryDeleteParams params`

  - `String memoryStoreId`

  - `Optional<String> memoryId`

  - `Optional<String> expectedContentSha256`

    Query parameter for expected_content_sha256

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsDeletedMemory:`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `String id`

    ID of the deleted memory (a `mem_...` value).

  - `Type type`

    - `MEMORY_DELETED("memory_deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memories.BetaManagedAgentsDeletedMemory;
import com.anthropic.models.beta.memorystores.memories.MemoryDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryDeleteParams params = MemoryDeleteParams.builder()
            .memoryStoreId("memory_store_id")
            .memoryId("memory_id")
            .build();
        BetaManagedAgentsDeletedMemory betaManagedAgentsDeletedMemory = client.beta().memoryStores().memories().delete(params);
    }
}
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

  - `Type type`

    - `CONFLICT_ERROR("conflict_error")`

  - `Optional<String> message`

### Beta Managed Agents Content Sha256 Precondition

- `class BetaManagedAgentsContentSha256Precondition:`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `Type type`

    - `CONTENT_SHA256("content_sha256")`

  - `Optional<String> contentSha256`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

### Beta Managed Agents Deleted Memory

- `class BetaManagedAgentsDeletedMemory:`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `String id`

    ID of the deleted memory (a `mem_...` value).

  - `Type type`

    - `MEMORY_DELETED("memory_deleted")`

### Beta Managed Agents Error

- `class BetaManagedAgentsError: A class that can be one of several variants.union`

  - `class BetaInvalidRequestError:`

    - `String message`

    - `JsonValue; type "invalid_request_error"constant`

      - `INVALID_REQUEST_ERROR("invalid_request_error")`

  - `class BetaAuthenticationError:`

    - `String message`

    - `JsonValue; type "authentication_error"constant`

      - `AUTHENTICATION_ERROR("authentication_error")`

  - `class BetaBillingError:`

    - `String message`

    - `JsonValue; type "billing_error"constant`

      - `BILLING_ERROR("billing_error")`

  - `class BetaPermissionError:`

    - `String message`

    - `JsonValue; type "permission_error"constant`

      - `PERMISSION_ERROR("permission_error")`

  - `class BetaNotFoundError:`

    - `String message`

    - `JsonValue; type "not_found_error"constant`

      - `NOT_FOUND_ERROR("not_found_error")`

  - `class BetaRateLimitError:`

    - `String message`

    - `JsonValue; type "rate_limit_error"constant`

      - `RATE_LIMIT_ERROR("rate_limit_error")`

  - `class BetaGatewayTimeoutError:`

    - `String message`

    - `JsonValue; type "timeout_error"constant`

      - `TIMEOUT_ERROR("timeout_error")`

  - `class BetaApiError:`

    - `String message`

    - `JsonValue; type "api_error"constant`

      - `API_ERROR("api_error")`

  - `class BetaOverloadedError:`

    - `String message`

    - `JsonValue; type "overloaded_error"constant`

      - `OVERLOADED_ERROR("overloaded_error")`

  - `class BetaManagedAgentsMemoryPreconditionFailedError:`

    - `Type type`

      - `MEMORY_PRECONDITION_FAILED_ERROR("memory_precondition_failed_error")`

    - `Optional<String> message`

  - `class BetaManagedAgentsMemoryPathConflictError:`

    - `Type type`

      - `MEMORY_PATH_CONFLICT_ERROR("memory_path_conflict_error")`

    - `Optional<String> conflictingMemoryId`

    - `Optional<String> conflictingPath`

    - `Optional<String> message`

  - `class BetaManagedAgentsConflictError:`

    - `Type type`

      - `CONFLICT_ERROR("conflict_error")`

    - `Optional<String> message`

### Beta Managed Agents Memory

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `String id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `String contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `long contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String memoryStoreId`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `String memoryVersionId`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `String path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type type`

    - `MEMORY("memory")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<String> content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Beta Managed Agents Memory List Item

- `class BetaManagedAgentsMemoryListItem: A class that can be one of several variants.union`

  One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

  - `class BetaManagedAgentsMemory:`

    A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

    - `String id`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `String contentSha256`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `long contentSizeBytes`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

    - `String memoryStoreId`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `String memoryVersionId`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `String path`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `Type type`

      - `MEMORY("memory")`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

    - `Optional<String> content`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `class BetaManagedAgentsMemoryPrefix:`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `String path`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `Type type`

      - `MEMORY_PREFIX("memory_prefix")`

### Beta Managed Agents Memory Path Conflict Error

- `class BetaManagedAgentsMemoryPathConflictError:`

  - `Type type`

    - `MEMORY_PATH_CONFLICT_ERROR("memory_path_conflict_error")`

  - `Optional<String> conflictingMemoryId`

  - `Optional<String> conflictingPath`

  - `Optional<String> message`

### Beta Managed Agents Memory Precondition Failed Error

- `class BetaManagedAgentsMemoryPreconditionFailedError:`

  - `Type type`

    - `MEMORY_PRECONDITION_FAILED_ERROR("memory_precondition_failed_error")`

  - `Optional<String> message`

### Beta Managed Agents Memory Prefix

- `class BetaManagedAgentsMemoryPrefix:`

  A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

  - `String path`

    The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

  - `Type type`

    - `MEMORY_PREFIX("memory_prefix")`

### Beta Managed Agents Memory View

- `enum BetaManagedAgentsMemoryView:`

  Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

  - `BASIC("basic")`

  - `FULL("full")`

### Beta Managed Agents Precondition

- `class BetaManagedAgentsPrecondition:`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `Type type`

    - `CONTENT_SHA256("content_sha256")`

  - `Optional<String> contentSha256`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

# Memory Versions

## List memory versions

`MemoryVersionListPage beta().memoryStores().memoryVersions().list(MemoryVersionListParamsparams = MemoryVersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

### Parameters

- `MemoryVersionListParams params`

  - `Optional<String> memoryStoreId`

  - `Optional<String> apiKeyId`

    Query parameter for api_key_id

  - `Optional<LocalDateTime> createdAtGte`

    Return versions created at or after this time (inclusive).

  - `Optional<LocalDateTime> createdAtLte`

    Return versions created at or before this time (inclusive).

  - `Optional<Long> limit`

    Query parameter for limit

  - `Optional<String> memoryId`

    Query parameter for memory_id

  - `Optional<BetaManagedAgentsMemoryVersionOperation> operation`

    Query parameter for operation

  - `Optional<String> page`

    Query parameter for page

  - `Optional<String> serviceAccountId`

    Query parameter for service_account_id

  - `Optional<String> sessionId`

    Query parameter for session_id

  - `Optional<BetaManagedAgentsMemoryView> view`

    Query parameter for view

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsMemoryVersion:`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `String id`

    Unique identifier for this version (a `memver_...` value).

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String memoryId`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `String memoryStoreId`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `BetaManagedAgentsMemoryVersionOperation operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `CREATED("created")`

    - `MODIFIED("modified")`

    - `DELETED("deleted")`

  - `Type type`

    - `MEMORY_VERSION("memory_version")`

  - `Optional<String> content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `Optional<String> contentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Optional<Long> contentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Optional<BetaManagedAgentsActor> createdBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `String sessionId`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `Type type`

        - `SESSION_ACTOR("session_actor")`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `String apiKeyId`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `Type type`

        - `API_ACTOR("api_actor")`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `Type type`

        - `USER_ACTOR("user_actor")`

      - `String userId`

        ID of the user who performed the write (a `user_...` value).

    - `class BetaManagedAgentsServiceAccountActor:`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `String serviceAccountId`

        ID of the service account that performed the write (a `svac_...` value).

      - `JsonValue; type "service_account_actor"constant`

        - `SERVICE_ACCOUNT_ACTOR("service_account_actor")`

  - `Optional<String> path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `Optional<LocalDateTime> redactedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsActor> redactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memoryversions.MemoryVersionListPage;
import com.anthropic.models.beta.memorystores.memoryversions.MemoryVersionListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryVersionListPage page = client.beta().memoryStores().memoryVersions().list("memory_store_id");
    }
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

`BetaManagedAgentsMemoryVersion beta().memoryStores().memoryVersions().retrieve(MemoryVersionRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

### Parameters

- `MemoryVersionRetrieveParams params`

  - `String memoryStoreId`

  - `Optional<String> memoryVersionId`

  - `Optional<BetaManagedAgentsMemoryView> view`

    Query parameter for view

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsMemoryVersion:`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `String id`

    Unique identifier for this version (a `memver_...` value).

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String memoryId`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `String memoryStoreId`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `BetaManagedAgentsMemoryVersionOperation operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `CREATED("created")`

    - `MODIFIED("modified")`

    - `DELETED("deleted")`

  - `Type type`

    - `MEMORY_VERSION("memory_version")`

  - `Optional<String> content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `Optional<String> contentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Optional<Long> contentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Optional<BetaManagedAgentsActor> createdBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `String sessionId`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `Type type`

        - `SESSION_ACTOR("session_actor")`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `String apiKeyId`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `Type type`

        - `API_ACTOR("api_actor")`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `Type type`

        - `USER_ACTOR("user_actor")`

      - `String userId`

        ID of the user who performed the write (a `user_...` value).

    - `class BetaManagedAgentsServiceAccountActor:`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `String serviceAccountId`

        ID of the service account that performed the write (a `svac_...` value).

      - `JsonValue; type "service_account_actor"constant`

        - `SERVICE_ACCOUNT_ACTOR("service_account_actor")`

  - `Optional<String> path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `Optional<LocalDateTime> redactedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsActor> redactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memoryversions.BetaManagedAgentsMemoryVersion;
import com.anthropic.models.beta.memorystores.memoryversions.MemoryVersionRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryVersionRetrieveParams params = MemoryVersionRetrieveParams.builder()
            .memoryStoreId("memory_store_id")
            .memoryVersionId("memory_version_id")
            .build();
        BetaManagedAgentsMemoryVersion betaManagedAgentsMemoryVersion = client.beta().memoryStores().memoryVersions().retrieve(params);
    }
}
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

`BetaManagedAgentsMemoryVersion beta().memoryStores().memoryVersions().redact(MemoryVersionRedactParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a memory version

### Parameters

- `MemoryVersionRedactParams params`

  - `String memoryStoreId`

  - `Optional<String> memoryVersionId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsMemoryVersion:`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `String id`

    Unique identifier for this version (a `memver_...` value).

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String memoryId`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `String memoryStoreId`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `BetaManagedAgentsMemoryVersionOperation operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `CREATED("created")`

    - `MODIFIED("modified")`

    - `DELETED("deleted")`

  - `Type type`

    - `MEMORY_VERSION("memory_version")`

  - `Optional<String> content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `Optional<String> contentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Optional<Long> contentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Optional<BetaManagedAgentsActor> createdBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `String sessionId`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `Type type`

        - `SESSION_ACTOR("session_actor")`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `String apiKeyId`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `Type type`

        - `API_ACTOR("api_actor")`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `Type type`

        - `USER_ACTOR("user_actor")`

      - `String userId`

        ID of the user who performed the write (a `user_...` value).

    - `class BetaManagedAgentsServiceAccountActor:`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `String serviceAccountId`

        ID of the service account that performed the write (a `svac_...` value).

      - `JsonValue; type "service_account_actor"constant`

        - `SERVICE_ACCOUNT_ACTOR("service_account_actor")`

  - `Optional<String> path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `Optional<LocalDateTime> redactedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsActor> redactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memoryversions.BetaManagedAgentsMemoryVersion;
import com.anthropic.models.beta.memorystores.memoryversions.MemoryVersionRedactParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryVersionRedactParams params = MemoryVersionRedactParams.builder()
            .memoryStoreId("memory_store_id")
            .memoryVersionId("memory_version_id")
            .build();
        BetaManagedAgentsMemoryVersion betaManagedAgentsMemoryVersion = client.beta().memoryStores().memoryVersions().redact(params);
    }
}
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

    - `String sessionId`

      ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

    - `Type type`

      - `SESSION_ACTOR("session_actor")`

  - `class BetaManagedAgentsApiActor:`

    Attribution for a write made directly via the public API (outside of any session).

    - `String apiKeyId`

      ID of the API key that performed the write. This identifies the key, not the secret.

    - `Type type`

      - `API_ACTOR("api_actor")`

  - `class BetaManagedAgentsUserActor:`

    Attribution for a write made by a human user through the Anthropic Console.

    - `Type type`

      - `USER_ACTOR("user_actor")`

    - `String userId`

      ID of the user who performed the write (a `user_...` value).

  - `class BetaManagedAgentsServiceAccountActor:`

    Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

    - `String serviceAccountId`

      ID of the service account that performed the write (a `svac_...` value).

    - `JsonValue; type "service_account_actor"constant`

      - `SERVICE_ACCOUNT_ACTOR("service_account_actor")`

### Beta Managed Agents API Actor

- `class BetaManagedAgentsApiActor:`

  Attribution for a write made directly via the public API (outside of any session).

  - `String apiKeyId`

    ID of the API key that performed the write. This identifies the key, not the secret.

  - `Type type`

    - `API_ACTOR("api_actor")`

### Beta Managed Agents Memory Version

- `class BetaManagedAgentsMemoryVersion:`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `String id`

    Unique identifier for this version (a `memver_...` value).

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String memoryId`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `String memoryStoreId`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `BetaManagedAgentsMemoryVersionOperation operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `CREATED("created")`

    - `MODIFIED("modified")`

    - `DELETED("deleted")`

  - `Type type`

    - `MEMORY_VERSION("memory_version")`

  - `Optional<String> content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `Optional<String> contentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Optional<Long> contentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Optional<BetaManagedAgentsActor> createdBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `String sessionId`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `Type type`

        - `SESSION_ACTOR("session_actor")`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `String apiKeyId`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `Type type`

        - `API_ACTOR("api_actor")`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `Type type`

        - `USER_ACTOR("user_actor")`

      - `String userId`

        ID of the user who performed the write (a `user_...` value).

    - `class BetaManagedAgentsServiceAccountActor:`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `String serviceAccountId`

        ID of the service account that performed the write (a `svac_...` value).

      - `JsonValue; type "service_account_actor"constant`

        - `SERVICE_ACCOUNT_ACTOR("service_account_actor")`

  - `Optional<String> path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `Optional<LocalDateTime> redactedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsActor> redactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Beta Managed Agents Memory Version Operation

- `enum BetaManagedAgentsMemoryVersionOperation:`

  The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

  - `CREATED("created")`

  - `MODIFIED("modified")`

  - `DELETED("deleted")`

### Beta Managed Agents Service Account Actor

- `class BetaManagedAgentsServiceAccountActor:`

  Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

  - `String serviceAccountId`

    ID of the service account that performed the write (a `svac_...` value).

  - `JsonValue; type "service_account_actor"constant`

    - `SERVICE_ACCOUNT_ACTOR("service_account_actor")`

### Beta Managed Agents Session Actor

- `class BetaManagedAgentsSessionActor:`

  Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

  - `String sessionId`

    ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

  - `Type type`

    - `SESSION_ACTOR("session_actor")`

### Beta Managed Agents User Actor

- `class BetaManagedAgentsUserActor:`

  Attribution for a write made by a human user through the Anthropic Console.

  - `Type type`

    - `USER_ACTOR("user_actor")`

  - `String userId`

    ID of the user who performed the write (a `user_...` value).

# Files

## Upload File

`BetaFileMetadata beta().files().upload(FileUploadParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/files`

Upload File

### Parameters

- `FileUploadParams params`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `String file`

    The file to upload

### Returns

- `class BetaFileMetadata:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing when the file was created.

  - `String filename`

    Original filename of the uploaded file.

  - `String mimeType`

    MIME type of the file.

  - `long sizeBytes`

    Size of the file in bytes.

  - `JsonValue; type "file"constant`

    Object type.

    For files, this is always `"file"`.

    - `FILE("file")`

  - `Optional<Boolean> downloadable`

    Whether the file can be downloaded.

  - `Optional<BetaFileScope> scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `String id`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonValue; type "session"constant`

      The type of scope (e.g., `"session"`).

      - `SESSION("session")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.files.BetaFileMetadata;
import com.anthropic.models.beta.files.FileUploadParams;
import java.io.ByteArrayInputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        FileUploadParams params = FileUploadParams.builder()
            .file(new ByteArrayInputStream("Example data".getBytes()))
            .build();
        BetaFileMetadata betaFileMetadata = client.beta().files().upload(params);
    }
}
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

`FileListPage beta().files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/files`

List Files

### Parameters

- `FileListParams params`

  - `Optional<String> afterId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `Optional<String> beforeId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Optional<Long> limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

  - `Optional<String> scopeId`

    Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaFileMetadata:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing when the file was created.

  - `String filename`

    Original filename of the uploaded file.

  - `String mimeType`

    MIME type of the file.

  - `long sizeBytes`

    Size of the file in bytes.

  - `JsonValue; type "file"constant`

    Object type.

    For files, this is always `"file"`.

    - `FILE("file")`

  - `Optional<Boolean> downloadable`

    Whether the file can be downloaded.

  - `Optional<BetaFileScope> scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `String id`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonValue; type "session"constant`

      The type of scope (e.g., `"session"`).

      - `SESSION("session")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.files.FileListPage;
import com.anthropic.models.beta.files.FileListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        FileListPage page = client.beta().files().list();
    }
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

`HttpResponse beta().files().download(FileDownloadParamsparams = FileDownloadParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/files/{file_id}/content`

Download File

### Parameters

- `FileDownloadParams params`

  - `Optional<String> fileId`

    ID of the File.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.HttpResponse;
import com.anthropic.models.beta.files.FileDownloadParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        HttpResponse response = client.beta().files().download("file_id");
    }
}
```

## Get File Metadata

`BetaFileMetadata beta().files().retrieveMetadata(FileRetrieveMetadataParamsparams = FileRetrieveMetadataParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/files/{file_id}`

Get File Metadata

### Parameters

- `FileRetrieveMetadataParams params`

  - `Optional<String> fileId`

    ID of the File.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaFileMetadata:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing when the file was created.

  - `String filename`

    Original filename of the uploaded file.

  - `String mimeType`

    MIME type of the file.

  - `long sizeBytes`

    Size of the file in bytes.

  - `JsonValue; type "file"constant`

    Object type.

    For files, this is always `"file"`.

    - `FILE("file")`

  - `Optional<Boolean> downloadable`

    Whether the file can be downloaded.

  - `Optional<BetaFileScope> scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `String id`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonValue; type "session"constant`

      The type of scope (e.g., `"session"`).

      - `SESSION("session")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.files.BetaFileMetadata;
import com.anthropic.models.beta.files.FileRetrieveMetadataParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaFileMetadata betaFileMetadata = client.beta().files().retrieveMetadata("file_id");
    }
}
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

`BetaDeletedFile beta().files().delete(FileDeleteParamsparams = FileDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/files/{file_id}`

Delete File

### Parameters

- `FileDeleteParams params`

  - `Optional<String> fileId`

    ID of the File.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaDeletedFile:`

  - `String id`

    ID of the deleted file.

  - `Optional<Type> type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `FILE_DELETED("file_deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.files.BetaDeletedFile;
import com.anthropic.models.beta.files.FileDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaDeletedFile betaDeletedFile = client.beta().files().delete("file_id");
    }
}
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

  - `String id`

    ID of the deleted file.

  - `Optional<Type> type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `FILE_DELETED("file_deleted")`

### Beta File Metadata

- `class BetaFileMetadata:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing when the file was created.

  - `String filename`

    Original filename of the uploaded file.

  - `String mimeType`

    MIME type of the file.

  - `long sizeBytes`

    Size of the file in bytes.

  - `JsonValue; type "file"constant`

    Object type.

    For files, this is always `"file"`.

    - `FILE("file")`

  - `Optional<Boolean> downloadable`

    Whether the file can be downloaded.

  - `Optional<BetaFileScope> scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `String id`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonValue; type "session"constant`

      The type of scope (e.g., `"session"`).

      - `SESSION("session")`

### Beta File Scope

- `class BetaFileScope:`

  - `String id`

    The ID of the scoping resource (e.g., the session ID).

  - `JsonValue; type "session"constant`

    The type of scope (e.g., `"session"`).

    - `SESSION("session")`

# Skills

## Create Skill

`SkillCreateResponse beta().skills().create(SkillCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/skills`

Create Skill

### Parameters

- `SkillCreateParams params`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `List<String> files`

    Files to upload for the skill.

    All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

  - `Optional<String> displayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

### Returns

- `class SkillCreateResponse:`

  - `String id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `String createdAt`

    ISO 8601 timestamp of when the skill was created.

  - `Optional<String> displayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `Optional<String> latestVersion`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `String source`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `String type`

    Object type.

    For Skills, this is always `"skill"`.

  - `String updatedAt`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.SkillCreateParams;
import com.anthropic.models.beta.skills.SkillCreateResponse;
import java.io.ByteArrayInputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        SkillCreateParams params = SkillCreateParams.builder()
            .addFile(new ByteArrayInputStream("Example data".getBytes()))
            .build();
        SkillCreateResponse skill = client.beta().skills().create(params);
    }
}
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

`SkillListPage beta().skills().list(SkillListParamsparams = SkillListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/skills`

List Skills

### Parameters

- `SkillListParams params`

  - `Optional<Long> limit`

    Number of results to return per page.

    Maximum value is 100. Defaults to 20.

  - `Optional<String> page`

    Pagination token for fetching a specific page of results.

    Pass the value from a previous response's `next_page` field to get the next page of results.

  - `Optional<String> source`

    Filter skills by source.

    If provided, only skills from the specified source will be returned:

    * `"custom"`: only return user-created skills
    * `"anthropic"`: only return Anthropic-created skills

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class SkillListResponse:`

  - `String id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `String createdAt`

    ISO 8601 timestamp of when the skill was created.

  - `Optional<String> displayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `Optional<String> latestVersion`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `String source`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `String type`

    Object type.

    For Skills, this is always `"skill"`.

  - `String updatedAt`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.SkillListPage;
import com.anthropic.models.beta.skills.SkillListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        SkillListPage page = client.beta().skills().list();
    }
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

`SkillRetrieveResponse beta().skills().retrieve(SkillRetrieveParamsparams = SkillRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/skills/{skill_id}`

Get Skill

### Parameters

- `SkillRetrieveParams params`

  - `Optional<String> skillId`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class SkillRetrieveResponse:`

  - `String id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `String createdAt`

    ISO 8601 timestamp of when the skill was created.

  - `Optional<String> displayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `Optional<String> latestVersion`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `String source`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `String type`

    Object type.

    For Skills, this is always `"skill"`.

  - `String updatedAt`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.SkillRetrieveParams;
import com.anthropic.models.beta.skills.SkillRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        SkillRetrieveResponse skill = client.beta().skills().retrieve("skill_id");
    }
}
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

`SkillDeleteResponse beta().skills().delete(SkillDeleteParamsparams = SkillDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/skills/{skill_id}`

Delete Skill

### Parameters

- `SkillDeleteParams params`

  - `Optional<String> skillId`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class SkillDeleteResponse:`

  - `String id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `String type`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.SkillDeleteParams;
import com.anthropic.models.beta.skills.SkillDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        SkillDeleteResponse skill = client.beta().skills().delete("skill_id");
    }
}
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

`VersionCreateResponse beta().skills().versions().create(VersionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/skills/{skill_id}/versions`

Create Skill Version

### Parameters

- `VersionCreateParams params`

  - `Optional<String> skillId`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `List<String> files`

    Files to upload for the skill.

    All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

### Returns

- `class VersionCreateResponse:`

  - `String id`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `String createdAt`

    ISO 8601 timestamp of when the skill version was created.

  - `String description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `String directory`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `String name`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `String skillId`

    Identifier for the skill that this version belongs to.

  - `String type`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `String version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.versions.VersionCreateParams;
import com.anthropic.models.beta.skills.versions.VersionCreateResponse;
import java.io.ByteArrayInputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VersionCreateParams params = VersionCreateParams.builder()
            .skillId("skill_id")
            .addFile(new ByteArrayInputStream("Example data".getBytes()))
            .build();
        VersionCreateResponse version = client.beta().skills().versions().create(params);
    }
}
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

`VersionListPage beta().skills().versions().list(VersionListParamsparams = VersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/skills/{skill_id}/versions`

List Skill Versions

### Parameters

- `VersionListParams params`

  - `Optional<String> skillId`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Optional<Long> limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

  - `Optional<String> page`

    Optionally set to the `next_page` token from the previous response.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class VersionListResponse:`

  - `String id`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `String createdAt`

    ISO 8601 timestamp of when the skill version was created.

  - `String description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `String directory`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `String name`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `String skillId`

    Identifier for the skill that this version belongs to.

  - `String type`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `String version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.versions.VersionListPage;
import com.anthropic.models.beta.skills.versions.VersionListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VersionListPage page = client.beta().skills().versions().list("skill_id");
    }
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

`HttpResponse beta().skills().versions().download(VersionDownloadParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

### Parameters

- `VersionDownloadParams params`

  - `String skillId`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Optional<String> version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.HttpResponse;
import com.anthropic.models.beta.skills.versions.VersionDownloadParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VersionDownloadParams params = VersionDownloadParams.builder()
            .skillId("skill_id")
            .version("version")
            .build();
        HttpResponse response = client.beta().skills().versions().download(params);
    }
}
```

## Get Skill Version

`VersionRetrieveResponse beta().skills().versions().retrieve(VersionRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

### Parameters

- `VersionRetrieveParams params`

  - `String skillId`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Optional<String> version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class VersionRetrieveResponse:`

  - `String id`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `String createdAt`

    ISO 8601 timestamp of when the skill version was created.

  - `String description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `String directory`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `String name`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `String skillId`

    Identifier for the skill that this version belongs to.

  - `String type`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `String version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.versions.VersionRetrieveParams;
import com.anthropic.models.beta.skills.versions.VersionRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VersionRetrieveParams params = VersionRetrieveParams.builder()
            .skillId("skill_id")
            .version("version")
            .build();
        VersionRetrieveResponse version = client.beta().skills().versions().retrieve(params);
    }
}
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

`VersionDeleteResponse beta().skills().versions().delete(VersionDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

### Parameters

- `VersionDeleteParams params`

  - `String skillId`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Optional<String> version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class VersionDeleteResponse:`

  - `String id`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `String type`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.versions.VersionDeleteParams;
import com.anthropic.models.beta.skills.versions.VersionDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VersionDeleteParams params = VersionDeleteParams.builder()
            .skillId("skill_id")
            .version("version")
            .build();
        VersionDeleteResponse version = client.beta().skills().versions().delete(params);
    }
}
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

`BetaUserProfile beta().userProfiles().create(UserProfileCreateParamsparams = UserProfileCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/user_profiles`

Create User Profile

### Parameters

- `UserProfileCreateParams params`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `Optional<AccessType> accessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `APPLICATION("application")`

    - `PASSTHROUGH("passthrough")`

  - `Optional<String> externalId`

    Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

  - `Optional<Metadata> metadata`

    Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

  - `Optional<String> name`

    Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a resold-to company (`relationship` `resold` / `access_type` `passthrough`), that company's name where known. Maximum 255 characters.

  - `Optional<Relationship> relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `EXTERNAL("external")`

    - `RESOLD("resold")`

    - `INTERNAL("internal")`

### Returns

- `class BetaUserProfile:`

  - `String id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `TrustGrants trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status status`

      Status of the trust grant.

      - `ACTIVE("active")`

      - `PENDING("pending")`

      - `REJECTED("rejected")`

  - `Type type`

    Object type. Always `user_profile`.

    - `USER_PROFILE("user_profile")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<AccessType> accessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `APPLICATION("application")`

    - `PASSTHROUGH("passthrough")`

  - `Optional<String> externalId`

    Platform's own identifier for this user. Not enforced unique.

  - `Optional<String> name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Optional<Relationship> relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `EXTERNAL("external")`

    - `RESOLD("resold")`

    - `INTERNAL("internal")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.userprofiles.BetaUserProfile;
import com.anthropic.models.beta.userprofiles.UserProfileCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaUserProfile betaUserProfile = client.beta().userProfiles().create();
    }
}
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

`UserProfileListPage beta().userProfiles().list(UserProfileListParamsparams = UserProfileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/user_profiles`

List User Profiles

### Parameters

- `UserProfileListParams params`

  - `Optional<Long> limit`

    Query parameter for limit

  - `Optional<Order> order`

    Query parameter for order

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<String> page`

    Query parameter for page

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaUserProfile:`

  - `String id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `TrustGrants trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status status`

      Status of the trust grant.

      - `ACTIVE("active")`

      - `PENDING("pending")`

      - `REJECTED("rejected")`

  - `Type type`

    Object type. Always `user_profile`.

    - `USER_PROFILE("user_profile")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<AccessType> accessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `APPLICATION("application")`

    - `PASSTHROUGH("passthrough")`

  - `Optional<String> externalId`

    Platform's own identifier for this user. Not enforced unique.

  - `Optional<String> name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Optional<Relationship> relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `EXTERNAL("external")`

    - `RESOLD("resold")`

    - `INTERNAL("internal")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.userprofiles.UserProfileListPage;
import com.anthropic.models.beta.userprofiles.UserProfileListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        UserProfileListPage page = client.beta().userProfiles().list();
    }
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

`BetaUserProfile beta().userProfiles().retrieve(UserProfileRetrieveParamsparams = UserProfileRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/user_profiles/{user_profile_id}`

Get User Profile

### Parameters

- `UserProfileRetrieveParams params`

  - `Optional<String> userProfileId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaUserProfile:`

  - `String id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `TrustGrants trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status status`

      Status of the trust grant.

      - `ACTIVE("active")`

      - `PENDING("pending")`

      - `REJECTED("rejected")`

  - `Type type`

    Object type. Always `user_profile`.

    - `USER_PROFILE("user_profile")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<AccessType> accessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `APPLICATION("application")`

    - `PASSTHROUGH("passthrough")`

  - `Optional<String> externalId`

    Platform's own identifier for this user. Not enforced unique.

  - `Optional<String> name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Optional<Relationship> relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `EXTERNAL("external")`

    - `RESOLD("resold")`

    - `INTERNAL("internal")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.userprofiles.BetaUserProfile;
import com.anthropic.models.beta.userprofiles.UserProfileRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaUserProfile betaUserProfile = client.beta().userProfiles().retrieve("uprof_011CZkZCu8hGbp5mYRQgUmz9");
    }
}
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

`BetaUserProfile beta().userProfiles().update(UserProfileUpdateParamsparams = UserProfileUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `UserProfileUpdateParams params`

  - `Optional<String> userProfileId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `Optional<AccessType> accessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `APPLICATION("application")`

    - `PASSTHROUGH("passthrough")`

  - `Optional<String> externalId`

    If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

  - `Optional<Metadata> metadata`

    Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

  - `Optional<String> name`

    If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

  - `Optional<Relationship> relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `EXTERNAL("external")`

    - `RESOLD("resold")`

    - `INTERNAL("internal")`

### Returns

- `class BetaUserProfile:`

  - `String id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `TrustGrants trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status status`

      Status of the trust grant.

      - `ACTIVE("active")`

      - `PENDING("pending")`

      - `REJECTED("rejected")`

  - `Type type`

    Object type. Always `user_profile`.

    - `USER_PROFILE("user_profile")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<AccessType> accessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `APPLICATION("application")`

    - `PASSTHROUGH("passthrough")`

  - `Optional<String> externalId`

    Platform's own identifier for this user. Not enforced unique.

  - `Optional<String> name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Optional<Relationship> relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `EXTERNAL("external")`

    - `RESOLD("resold")`

    - `INTERNAL("internal")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.userprofiles.BetaUserProfile;
import com.anthropic.models.beta.userprofiles.UserProfileUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaUserProfile betaUserProfile = client.beta().userProfiles().update("uprof_011CZkZCu8hGbp5mYRQgUmz9");
    }
}
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

`BetaUserProfileEnrollmentUrl beta().userProfiles().createEnrollmentUrl(UserProfileCreateEnrollmentUrlParamsparams = UserProfileCreateEnrollmentUrlParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Parameters

- `UserProfileCreateEnrollmentUrlParams params`

  - `Optional<String> userProfileId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaUserProfileEnrollmentUrl:`

  - `LocalDateTime expiresAt`

    A timestamp in RFC 3339 format

  - `Type type`

    Object type. Always `enrollment_url`.

    - `ENROLLMENT_URL("enrollment_url")`

  - `String url`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.userprofiles.BetaUserProfileEnrollmentUrl;
import com.anthropic.models.beta.userprofiles.UserProfileCreateEnrollmentUrlParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaUserProfileEnrollmentUrl betaUserProfileEnrollmentUrl = client.beta().userProfiles().createEnrollmentUrl("uprof_011CZkZCu8hGbp5mYRQgUmz9");
    }
}
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

  - `String id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `TrustGrants trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status status`

      Status of the trust grant.

      - `ACTIVE("active")`

      - `PENDING("pending")`

      - `REJECTED("rejected")`

  - `Type type`

    Object type. Always `user_profile`.

    - `USER_PROFILE("user_profile")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<AccessType> accessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `APPLICATION("application")`

    - `PASSTHROUGH("passthrough")`

  - `Optional<String> externalId`

    Platform's own identifier for this user. Not enforced unique.

  - `Optional<String> name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Optional<Relationship> relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `EXTERNAL("external")`

    - `RESOLD("resold")`

    - `INTERNAL("internal")`

### Beta User Profile Enrollment URL

- `class BetaUserProfileEnrollmentUrl:`

  - `LocalDateTime expiresAt`

    A timestamp in RFC 3339 format

  - `Type type`

    Object type. Always `enrollment_url`.

    - `ENROLLMENT_URL("enrollment_url")`

  - `String url`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Beta User Profile Trust Grant

- `class BetaUserProfileTrustGrant:`

  - `Status status`

    Status of the trust grant.

    - `ACTIVE("active")`

    - `PENDING("pending")`

    - `REJECTED("rejected")`

# Dreams

## Create a Dream

`BetaDream beta().dreams().create(DreamCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/dreams`

Create a Dream

### Parameters

- `DreamCreateParams params`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

      - `Type type`

        - `MEMORY_STORE("memory_store")`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

        - `SESSIONS("sessions")`

  - `Model model`

    Model identifier and configuration applied to every pipeline stage.

    - `String`

    - `class BetaDreamModelConfigParam:`

      Model identifier and configuration applied to every pipeline stage.

      - `String id`

        Model identifier, e.g. "claude-opus-5". 1-256 characters.

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

  - `Optional<String> instructions`

  - `Optional<BetaOutputBehavior> outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> endedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaDreamError> error`

    Failure detail for a Dream whose `status` is `failed`.

    - `String message`

    - `String type`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

      - `Type type`

        - `MEMORY_STORE("memory_store")`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

        - `SESSIONS("sessions")`

  - `Optional<String> instructions`

  - `BetaDreamModelConfig model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `String id`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `BetaOutputBehavior outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type type`

        - `CREATE_NEW("create_new")`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `String memoryStoreId`

      - `Type type`

        - `UPDATE_EXISTING("update_existing")`

  - `List<BetaDreamOutput> outputs`

    - `String memoryStoreId`

    - `Type type`

      - `MEMORY_STORE("memory_store")`

  - `Optional<String> sessionId`

  - `BetaDreamStatus status`

    Lifecycle status of a Dream.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Type type`

    - `DREAM("dream")`

  - `BetaDreamUsage usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `long cacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `long cacheReadInputTokens`

      Total tokens read from prompt cache.

    - `long inputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `long outputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.dreams.BetaDream;
import com.anthropic.models.beta.dreams.DreamCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        DreamCreateParams params = DreamCreateParams.builder()
            .addMemoryStoreInput("x")
            .model("string")
            .build();
        BetaDream betaDream = client.beta().dreams().create(params);
    }
}
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

`DreamListPage beta().dreams().list(DreamListParamsparams = DreamListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/dreams`

List Dreams

### Parameters

- `DreamListParams params`

  - `Optional<LocalDateTime> createdAtGt`

    Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

  - `Optional<LocalDateTime> createdAtLt`

    Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

  - `Optional<Boolean> includeArchived`

    Query parameter for include_archived

  - `Optional<Long> limit`

    Query parameter for limit

  - `Optional<String> page`

    Query parameter for page

  - `Optional<List<BetaDreamStatus>> statuses`

    Filter by lifecycle status. Repeat the parameter to match any of multiple statuses. Empty applies no status filter.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> endedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaDreamError> error`

    Failure detail for a Dream whose `status` is `failed`.

    - `String message`

    - `String type`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

      - `Type type`

        - `MEMORY_STORE("memory_store")`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

        - `SESSIONS("sessions")`

  - `Optional<String> instructions`

  - `BetaDreamModelConfig model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `String id`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `BetaOutputBehavior outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type type`

        - `CREATE_NEW("create_new")`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `String memoryStoreId`

      - `Type type`

        - `UPDATE_EXISTING("update_existing")`

  - `List<BetaDreamOutput> outputs`

    - `String memoryStoreId`

    - `Type type`

      - `MEMORY_STORE("memory_store")`

  - `Optional<String> sessionId`

  - `BetaDreamStatus status`

    Lifecycle status of a Dream.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Type type`

    - `DREAM("dream")`

  - `BetaDreamUsage usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `long cacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `long cacheReadInputTokens`

      Total tokens read from prompt cache.

    - `long inputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `long outputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.dreams.DreamListPage;
import com.anthropic.models.beta.dreams.DreamListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        DreamListPage page = client.beta().dreams().list();
    }
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

`BetaDream beta().dreams().retrieve(DreamRetrieveParamsparams = DreamRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/dreams/{dream_id}`

Get a Dream

### Parameters

- `DreamRetrieveParams params`

  - `Optional<String> dreamId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> endedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaDreamError> error`

    Failure detail for a Dream whose `status` is `failed`.

    - `String message`

    - `String type`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

      - `Type type`

        - `MEMORY_STORE("memory_store")`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

        - `SESSIONS("sessions")`

  - `Optional<String> instructions`

  - `BetaDreamModelConfig model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `String id`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `BetaOutputBehavior outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type type`

        - `CREATE_NEW("create_new")`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `String memoryStoreId`

      - `Type type`

        - `UPDATE_EXISTING("update_existing")`

  - `List<BetaDreamOutput> outputs`

    - `String memoryStoreId`

    - `Type type`

      - `MEMORY_STORE("memory_store")`

  - `Optional<String> sessionId`

  - `BetaDreamStatus status`

    Lifecycle status of a Dream.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Type type`

    - `DREAM("dream")`

  - `BetaDreamUsage usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `long cacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `long cacheReadInputTokens`

      Total tokens read from prompt cache.

    - `long inputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `long outputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.dreams.BetaDream;
import com.anthropic.models.beta.dreams.DreamRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaDream betaDream = client.beta().dreams().retrieve("dream_id");
    }
}
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

`BetaDream beta().dreams().cancel(DreamCancelParamsparams = DreamCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/dreams/{dream_id}/cancel`

Cancel a Dream

### Parameters

- `DreamCancelParams params`

  - `Optional<String> dreamId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> endedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaDreamError> error`

    Failure detail for a Dream whose `status` is `failed`.

    - `String message`

    - `String type`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

      - `Type type`

        - `MEMORY_STORE("memory_store")`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

        - `SESSIONS("sessions")`

  - `Optional<String> instructions`

  - `BetaDreamModelConfig model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `String id`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `BetaOutputBehavior outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type type`

        - `CREATE_NEW("create_new")`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `String memoryStoreId`

      - `Type type`

        - `UPDATE_EXISTING("update_existing")`

  - `List<BetaDreamOutput> outputs`

    - `String memoryStoreId`

    - `Type type`

      - `MEMORY_STORE("memory_store")`

  - `Optional<String> sessionId`

  - `BetaDreamStatus status`

    Lifecycle status of a Dream.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Type type`

    - `DREAM("dream")`

  - `BetaDreamUsage usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `long cacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `long cacheReadInputTokens`

      Total tokens read from prompt cache.

    - `long inputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `long outputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.dreams.BetaDream;
import com.anthropic.models.beta.dreams.DreamCancelParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaDream betaDream = client.beta().dreams().cancel("dream_id");
    }
}
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

`BetaDream beta().dreams().archive(DreamArchiveParamsparams = DreamArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/dreams/{dream_id}/archive`

Archive a Dream

### Parameters

- `DreamArchiveParams params`

  - `Optional<String> dreamId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> endedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaDreamError> error`

    Failure detail for a Dream whose `status` is `failed`.

    - `String message`

    - `String type`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

      - `Type type`

        - `MEMORY_STORE("memory_store")`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

        - `SESSIONS("sessions")`

  - `Optional<String> instructions`

  - `BetaDreamModelConfig model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `String id`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `BetaOutputBehavior outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type type`

        - `CREATE_NEW("create_new")`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `String memoryStoreId`

      - `Type type`

        - `UPDATE_EXISTING("update_existing")`

  - `List<BetaDreamOutput> outputs`

    - `String memoryStoreId`

    - `Type type`

      - `MEMORY_STORE("memory_store")`

  - `Optional<String> sessionId`

  - `BetaDreamStatus status`

    Lifecycle status of a Dream.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Type type`

    - `DREAM("dream")`

  - `BetaDreamUsage usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `long cacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `long cacheReadInputTokens`

      Total tokens read from prompt cache.

    - `long inputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `long outputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.dreams.BetaDream;
import com.anthropic.models.beta.dreams.DreamArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaDream betaDream = client.beta().dreams().archive("dream_id");
    }
}
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

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> endedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaDreamError> error`

    Failure detail for a Dream whose `status` is `failed`.

    - `String message`

    - `String type`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

      - `Type type`

        - `MEMORY_STORE("memory_store")`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

        - `SESSIONS("sessions")`

  - `Optional<String> instructions`

  - `BetaDreamModelConfig model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `String id`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `BetaOutputBehavior outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type type`

        - `CREATE_NEW("create_new")`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `String memoryStoreId`

      - `Type type`

        - `UPDATE_EXISTING("update_existing")`

  - `List<BetaDreamOutput> outputs`

    - `String memoryStoreId`

    - `Type type`

      - `MEMORY_STORE("memory_store")`

  - `Optional<String> sessionId`

  - `BetaDreamStatus status`

    Lifecycle status of a Dream.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Type type`

    - `DREAM("dream")`

  - `BetaDreamUsage usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `long cacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `long cacheReadInputTokens`

      Total tokens read from prompt cache.

    - `long inputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `long outputTokens`

      Total output tokens generated across every pipeline stage.

### Beta Dream Error

- `class BetaDreamError:`

  Failure detail for a Dream whose `status` is `failed`.

  - `String message`

  - `String type`

### Beta Dream Input

- `class BetaDreamInput: A class that can be one of several variants.union`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `class BetaDreamMemoryStoreInput:`

    An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

    - `String memoryStoreId`

    - `Type type`

      - `MEMORY_STORE("memory_store")`

  - `class BetaDreamSessionsInput:`

    Input session transcripts the dream reads.

    - `List<String> sessionIds`

    - `Type type`

      - `SESSIONS("sessions")`

### Beta Dream Memory Store Input

- `class BetaDreamMemoryStoreInput:`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `String memoryStoreId`

  - `Type type`

    - `MEMORY_STORE("memory_store")`

### Beta Dream Memory Store Output

- `class BetaDreamMemoryStoreOutput:`

  An output memory store the dream writes consolidated memories into.

  - `String memoryStoreId`

  - `Type type`

    - `MEMORY_STORE("memory_store")`

### Beta Dream Model Config

- `class BetaDreamModelConfig:`

  Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

  - `String id`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

  - `Optional<Speed> speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `STANDARD("standard")`

    - `FAST("fast")`

### Beta Dream Model Config Param

- `class BetaDreamModelConfigParam:`

  Model identifier and configuration applied to every pipeline stage.

  - `String id`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

  - `Optional<Speed> speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `STANDARD("standard")`

    - `FAST("fast")`

### Beta Dream Output

- `class BetaDreamOutput:`

  An output memory store the dream writes consolidated memories into.

  - `String memoryStoreId`

  - `Type type`

    - `MEMORY_STORE("memory_store")`

### Beta Dream Sessions Input

- `class BetaDreamSessionsInput:`

  Input session transcripts the dream reads.

  - `List<String> sessionIds`

  - `Type type`

    - `SESSIONS("sessions")`

### Beta Dream Status

- `enum BetaDreamStatus:`

  Lifecycle status of a Dream.

  - `PENDING("pending")`

  - `RUNNING("running")`

  - `COMPLETED("completed")`

  - `FAILED("failed")`

  - `CANCELED("canceled")`

### Beta Dream Usage

- `class BetaDreamUsage:`

  Cumulative token usage for the dream across every pipeline stage.

  - `long cacheCreationInputTokens`

    Total tokens used to create prompt-cache entries (sum of all TTL tiers).

  - `long cacheReadInputTokens`

    Total tokens read from prompt cache.

  - `long inputTokens`

    Total uncached input tokens consumed across every pipeline stage.

  - `long outputTokens`

    Total output tokens generated across every pipeline stage.

### Beta Output Behavior

- `class BetaOutputBehavior: A class that can be one of several variants.union`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `class BetaOutputBehaviorCreateNew:`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `Type type`

      - `CREATE_NEW("create_new")`

  - `class BetaOutputBehaviorUpdateExisting:`

    The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

    - `String memoryStoreId`

    - `Type type`

      - `UPDATE_EXISTING("update_existing")`

### Beta Output Behavior Create New

- `class BetaOutputBehaviorCreateNew:`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `Type type`

    - `CREATE_NEW("create_new")`

### Beta Output Behavior Update Existing

- `class BetaOutputBehaviorUpdateExisting:`

  The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

  - `String memoryStoreId`

  - `Type type`

    - `UPDATE_EXISTING("update_existing")`

# Tunnels

## Create Tunnel

`BetaTunnel beta().tunnels().create(TunnelCreateParamsparams = TunnelCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

### Parameters

- `TunnelCreateParams params`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `Optional<String> displayName`

    Optional human-readable name for the tunnel (1-255 characters).

### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `String id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `String domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonValue; type "tunnel"constant`

    - `TUNNEL("tunnel")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.BetaTunnel;
import com.anthropic.models.beta.tunnels.TunnelCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaTunnel betaTunnel = client.beta().tunnels().create();
    }
}
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

`BetaTunnel beta().tunnels().retrieve(TunnelRetrieveParamsparams = TunnelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

### Parameters

- `TunnelRetrieveParams params`

  - `Optional<String> tunnelId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `String id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `String domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonValue; type "tunnel"constant`

    - `TUNNEL("tunnel")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.BetaTunnel;
import com.anthropic.models.beta.tunnels.TunnelRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaTunnel betaTunnel = client.beta().tunnels().retrieve("tunnel_id");
    }
}
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

`TunnelListPage beta().tunnels().list(TunnelListParamsparams = TunnelListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

### Parameters

- `TunnelListParams params`

  - `Optional<Boolean> includeArchived`

    Whether to include archived tunnels in the results. Defaults to false.

  - `Optional<Long> limit`

    Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

  - `Optional<String> page`

    Opaque pagination cursor from a previous `list_tunnels` response.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `String id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `String domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonValue; type "tunnel"constant`

    - `TUNNEL("tunnel")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.TunnelListPage;
import com.anthropic.models.beta.tunnels.TunnelListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        TunnelListPage page = client.beta().tunnels().list();
    }
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

`BetaTunnel beta().tunnels().archive(TunnelArchiveParamsparams = TunnelArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

### Parameters

- `TunnelArchiveParams params`

  - `Optional<String> tunnelId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `String id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `String domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonValue; type "tunnel"constant`

    - `TUNNEL("tunnel")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.BetaTunnel;
import com.anthropic.models.beta.tunnels.TunnelArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaTunnel betaTunnel = client.beta().tunnels().archive("tunnel_id");
    }
}
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

`BetaTunnelToken beta().tunnels().revealToken(TunnelRevealTokenParamsparams = TunnelRevealTokenParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

### Parameters

- `TunnelRevealTokenParams params`

  - `Optional<String> tunnelId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaTunnelToken:`

  A tunnel's connector token.

  - `String id`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `String tunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `JsonValue; type "tunnel_token"constant`

    - `TUNNEL_TOKEN("tunnel_token")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.BetaTunnelToken;
import com.anthropic.models.beta.tunnels.TunnelRevealTokenParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaTunnelToken betaTunnelToken = client.beta().tunnels().revealToken("tunnel_id");
    }
}
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

`BetaTunnelToken beta().tunnels().rotateToken(TunnelRotateTokenParamsparams = TunnelRotateTokenParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

### Parameters

- `TunnelRotateTokenParams params`

  - `Optional<String> tunnelId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `Optional<String> reason`

    Optional free-text reason for the rotation, recorded for audit.

### Returns

- `class BetaTunnelToken:`

  A tunnel's connector token.

  - `String id`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `String tunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `JsonValue; type "tunnel_token"constant`

    - `TUNNEL_TOKEN("tunnel_token")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.BetaTunnelToken;
import com.anthropic.models.beta.tunnels.TunnelRotateTokenParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaTunnelToken betaTunnelToken = client.beta().tunnels().rotateToken("tunnel_id");
    }
}
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

  - `String id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `String domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonValue; type "tunnel"constant`

    - `TUNNEL("tunnel")`

### Beta Tunnel Token

- `class BetaTunnelToken:`

  A tunnel's connector token.

  - `String id`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `String tunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `JsonValue; type "tunnel_token"constant`

    - `TUNNEL_TOKEN("tunnel_token")`

# Certificates

## Create Tunnel Certificate

`BetaTunnelCertificate beta().tunnels().certificates().create(CertificateCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

### Parameters

- `CertificateCreateParams params`

  - `Optional<String> tunnelId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `String caCertificatePem`

    PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `String id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

  - `String fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `String tunnelId`

    ID of the tunnel the certificate is registered against.

  - `JsonValue; type "tunnel_certificate"constant`

    - `TUNNEL_CERTIFICATE("tunnel_certificate")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.certificates.BetaTunnelCertificate;
import com.anthropic.models.beta.tunnels.certificates.CertificateCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CertificateCreateParams params = CertificateCreateParams.builder()
            .tunnelId("tunnel_id")
            .caCertificatePem("ca_certificate_pem")
            .build();
        BetaTunnelCertificate betaTunnelCertificate = client.beta().tunnels().certificates().create(params);
    }
}
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

`BetaTunnelCertificate beta().tunnels().certificates().retrieve(CertificateRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

### Parameters

- `CertificateRetrieveParams params`

  - `String tunnelId`

  - `Optional<String> certificateId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `String id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

  - `String fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `String tunnelId`

    ID of the tunnel the certificate is registered against.

  - `JsonValue; type "tunnel_certificate"constant`

    - `TUNNEL_CERTIFICATE("tunnel_certificate")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.certificates.BetaTunnelCertificate;
import com.anthropic.models.beta.tunnels.certificates.CertificateRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CertificateRetrieveParams params = CertificateRetrieveParams.builder()
            .tunnelId("tunnel_id")
            .certificateId("certificate_id")
            .build();
        BetaTunnelCertificate betaTunnelCertificate = client.beta().tunnels().certificates().retrieve(params);
    }
}
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

`CertificateListPage beta().tunnels().certificates().list(CertificateListParamsparams = CertificateListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

### Parameters

- `CertificateListParams params`

  - `Optional<String> tunnelId`

  - `Optional<Boolean> includeArchived`

    Whether to include archived certificates in the results. Defaults to false.

  - `Optional<Long> limit`

    Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

  - `Optional<String> page`

    Opaque pagination cursor from a previous `list_tunnel_certificates` response.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `String id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

  - `String fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `String tunnelId`

    ID of the tunnel the certificate is registered against.

  - `JsonValue; type "tunnel_certificate"constant`

    - `TUNNEL_CERTIFICATE("tunnel_certificate")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.certificates.CertificateListPage;
import com.anthropic.models.beta.tunnels.certificates.CertificateListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CertificateListPage page = client.beta().tunnels().certificates().list("tunnel_id");
    }
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

`BetaTunnelCertificate beta().tunnels().certificates().archive(CertificateArchiveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

### Parameters

- `CertificateArchiveParams params`

  - `String tunnelId`

  - `Optional<String> certificateId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `String id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

  - `String fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `String tunnelId`

    ID of the tunnel the certificate is registered against.

  - `JsonValue; type "tunnel_certificate"constant`

    - `TUNNEL_CERTIFICATE("tunnel_certificate")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.certificates.BetaTunnelCertificate;
import com.anthropic.models.beta.tunnels.certificates.CertificateArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CertificateArchiveParams params = CertificateArchiveParams.builder()
            .tunnelId("tunnel_id")
            .certificateId("certificate_id")
            .build();
        BetaTunnelCertificate betaTunnelCertificate = client.beta().tunnels().certificates().archive(params);
    }
}
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

  - `String id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

  - `String fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `String tunnelId`

    ID of the tunnel the certificate is registered against.

  - `JsonValue; type "tunnel_certificate"constant`

    - `TUNNEL_CERTIFICATE("tunnel_certificate")`

# Webhooks

## Domain Types

### Beta Webhook Agent Archived Event Data

- `class BetaWebhookAgentArchivedEventData:`

  - `String id`

    ID of the agent that triggered the event.

  - `String organizationId`

  - `JsonValue; type "agent.archived"constant`

    - `AGENT_ARCHIVED("agent.archived")`

  - `String workspaceId`

### Beta Webhook Agent Created Event Data

- `class BetaWebhookAgentCreatedEventData:`

  - `String id`

    ID of the agent that triggered the event.

  - `String organizationId`

  - `JsonValue; type "agent.created"constant`

    - `AGENT_CREATED("agent.created")`

  - `String workspaceId`

### Beta Webhook Agent Deleted Event Data

- `class BetaWebhookAgentDeletedEventData:`

  - `String id`

    ID of the agent that triggered the event.

  - `String organizationId`

  - `JsonValue; type "agent.deleted"constant`

    - `AGENT_DELETED("agent.deleted")`

  - `String workspaceId`

### Beta Webhook Agent Updated Event Data

- `class BetaWebhookAgentUpdatedEventData:`

  - `String id`

    ID of the agent that triggered the event.

  - `String organizationId`

  - `JsonValue; type "agent.updated"constant`

    - `AGENT_UPDATED("agent.updated")`

  - `String workspaceId`

### Beta Webhook Deployment Archived Event Data

- `class BetaWebhookDeploymentArchivedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment.archived"constant`

    - `DEPLOYMENT_ARCHIVED("deployment.archived")`

  - `String workspaceId`

### Beta Webhook Deployment Created Event Data

- `class BetaWebhookDeploymentCreatedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment.created"constant`

    - `DEPLOYMENT_CREATED("deployment.created")`

  - `String workspaceId`

### Beta Webhook Deployment Deleted Event Data

- `class BetaWebhookDeploymentDeletedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment.deleted"constant`

    - `DEPLOYMENT_DELETED("deployment.deleted")`

  - `String workspaceId`

### Beta Webhook Deployment Paused Event Data

- `class BetaWebhookDeploymentPausedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment.paused"constant`

    - `DEPLOYMENT_PAUSED("deployment.paused")`

  - `String workspaceId`

### Beta Webhook Deployment Run Failed Event Data

- `class BetaWebhookDeploymentRunFailedEventData:`

  - `String id`

    ID of the deployment run that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment_run.failed"constant`

    - `DEPLOYMENT_RUN_FAILED("deployment_run.failed")`

  - `String workspaceId`

### Beta Webhook Deployment Run Started Event Data

- `class BetaWebhookDeploymentRunStartedEventData:`

  - `String id`

    ID of the deployment run that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment_run.started"constant`

    - `DEPLOYMENT_RUN_STARTED("deployment_run.started")`

  - `String workspaceId`

### Beta Webhook Deployment Run Succeeded Event Data

- `class BetaWebhookDeploymentRunSucceededEventData:`

  - `String id`

    ID of the deployment run that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment_run.succeeded"constant`

    - `DEPLOYMENT_RUN_SUCCEEDED("deployment_run.succeeded")`

  - `String workspaceId`

### Beta Webhook Deployment Unpaused Event Data

- `class BetaWebhookDeploymentUnpausedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment.unpaused"constant`

    - `DEPLOYMENT_UNPAUSED("deployment.unpaused")`

  - `String workspaceId`

### Beta Webhook Deployment Updated Event Data

- `class BetaWebhookDeploymentUpdatedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment.updated"constant`

    - `DEPLOYMENT_UPDATED("deployment.updated")`

  - `String workspaceId`

### Beta Webhook Environment Archived Event Data

- `class BetaWebhookEnvironmentArchivedEventData:`

  - `String id`

    ID of the environment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "environment.archived"constant`

    - `ENVIRONMENT_ARCHIVED("environment.archived")`

  - `String workspaceId`

### Beta Webhook Environment Created Event Data

- `class BetaWebhookEnvironmentCreatedEventData:`

  - `String id`

    ID of the environment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "environment.created"constant`

    - `ENVIRONMENT_CREATED("environment.created")`

  - `String workspaceId`

### Beta Webhook Environment Deleted Event Data

- `class BetaWebhookEnvironmentDeletedEventData:`

  - `String id`

    ID of the environment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "environment.deleted"constant`

    - `ENVIRONMENT_DELETED("environment.deleted")`

  - `String workspaceId`

### Beta Webhook Environment Updated Event Data

- `class BetaWebhookEnvironmentUpdatedEventData:`

  - `String id`

    ID of the environment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "environment.updated"constant`

    - `ENVIRONMENT_UPDATED("environment.updated")`

  - `String workspaceId`

### Beta Webhook Event

- `class BetaWebhookEvent:`

  - `String id`

    Unique event identifier for idempotency.

  - `LocalDateTime createdAt`

    RFC 3339 timestamp when the event occurred.

  - `BetaWebhookEventData data`

    - `class BetaWebhookSessionCreatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.created"constant`

        - `SESSION_CREATED("session.created")`

      - `String workspaceId`

    - `class BetaWebhookSessionPendingEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.pending"constant`

        - `SESSION_PENDING("session.pending")`

      - `String workspaceId`

    - `class BetaWebhookSessionRunningEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.running"constant`

        - `SESSION_RUNNING("session.running")`

      - `String workspaceId`

    - `class BetaWebhookSessionIdledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.idled"constant`

        - `SESSION_IDLED("session.idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionRequiresActionEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.requires_action"constant`

        - `SESSION_REQUIRES_ACTION("session.requires_action")`

      - `String workspaceId`

    - `class BetaWebhookSessionArchivedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.archived"constant`

        - `SESSION_ARCHIVED("session.archived")`

      - `String workspaceId`

    - `class BetaWebhookSessionDeletedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.deleted"constant`

        - `SESSION_DELETED("session.deleted")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusRescheduledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_rescheduled"constant`

        - `SESSION_STATUS_RESCHEDULED("session.status_rescheduled")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusRunStartedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_run_started"constant`

        - `SESSION_STATUS_RUN_STARTED("session.status_run_started")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusIdledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_idled"constant`

        - `SESSION_STATUS_IDLED("session.status_idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusTerminatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_terminated"constant`

        - `SESSION_STATUS_TERMINATED("session.status_terminated")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadCreatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `JsonValue; type "session.thread_created"constant`

        - `SESSION_THREAD_CREATED("session.thread_created")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadIdledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `JsonValue; type "session.thread_idled"constant`

        - `SESSION_THREAD_IDLED("session.thread_idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadTerminatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `JsonValue; type "session.thread_terminated"constant`

        - `SESSION_THREAD_TERMINATED("session.thread_terminated")`

      - `String workspaceId`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.outcome_evaluation_ended"constant`

        - `SESSION_OUTCOME_EVALUATION_ENDED("session.outcome_evaluation_ended")`

      - `String workspaceId`

    - `class BetaWebhookVaultCreatedEventData:`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.created"constant`

        - `VAULT_CREATED("vault.created")`

      - `String workspaceId`

    - `class BetaWebhookVaultArchivedEventData:`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.archived"constant`

        - `VAULT_ARCHIVED("vault.archived")`

      - `String workspaceId`

    - `class BetaWebhookVaultDeletedEventData:`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.deleted"constant`

        - `VAULT_DELETED("vault.deleted")`

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialCreatedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.created"constant`

        - `VAULT_CREDENTIAL_CREATED("vault_credential.created")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialArchivedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.archived"constant`

        - `VAULT_CREDENTIAL_ARCHIVED("vault_credential.archived")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialDeletedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.deleted"constant`

        - `VAULT_CREDENTIAL_DELETED("vault_credential.deleted")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.refresh_failed"constant`

        - `VAULT_CREDENTIAL_REFRESH_FAILED("vault_credential.refresh_failed")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookSessionUpdatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.updated"constant`

        - `SESSION_UPDATED("session.updated")`

      - `String workspaceId`

    - `class BetaWebhookAgentCreatedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue; type "agent.created"constant`

        - `AGENT_CREATED("agent.created")`

      - `String workspaceId`

    - `class BetaWebhookAgentArchivedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue; type "agent.archived"constant`

        - `AGENT_ARCHIVED("agent.archived")`

      - `String workspaceId`

    - `class BetaWebhookAgentDeletedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue; type "agent.deleted"constant`

        - `AGENT_DELETED("agent.deleted")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentPausedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.paused"constant`

        - `DEPLOYMENT_PAUSED("deployment.paused")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunFailedEventData:`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment_run.failed"constant`

        - `DEPLOYMENT_RUN_FAILED("deployment_run.failed")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentCreatedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.created"constant`

        - `DEPLOYMENT_CREATED("deployment.created")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentUpdatedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.updated"constant`

        - `DEPLOYMENT_UPDATED("deployment.updated")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentUnpausedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.unpaused"constant`

        - `DEPLOYMENT_UNPAUSED("deployment.unpaused")`

      - `String workspaceId`

    - `class BetaWebhookAgentUpdatedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue; type "agent.updated"constant`

        - `AGENT_UPDATED("agent.updated")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentArchivedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.archived"constant`

        - `DEPLOYMENT_ARCHIVED("deployment.archived")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunStartedEventData:`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment_run.started"constant`

        - `DEPLOYMENT_RUN_STARTED("deployment_run.started")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentDeletedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.deleted"constant`

        - `DEPLOYMENT_DELETED("deployment.deleted")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunSucceededEventData:`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment_run.succeeded"constant`

        - `DEPLOYMENT_RUN_SUCCEEDED("deployment_run.succeeded")`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentCreatedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "environment.created"constant`

        - `ENVIRONMENT_CREATED("environment.created")`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentUpdatedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "environment.updated"constant`

        - `ENVIRONMENT_UPDATED("environment.updated")`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentArchivedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "environment.archived"constant`

        - `ENVIRONMENT_ARCHIVED("environment.archived")`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentDeletedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "environment.deleted"constant`

        - `ENVIRONMENT_DELETED("environment.deleted")`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreCreatedEventData:`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `JsonValue; type "memory_store.created"constant`

        - `MEMORY_STORE_CREATED("memory_store.created")`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreArchivedEventData:`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `JsonValue; type "memory_store.archived"constant`

        - `MEMORY_STORE_ARCHIVED("memory_store.archived")`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreDeletedEventData:`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `JsonValue; type "memory_store.deleted"constant`

        - `MEMORY_STORE_DELETED("memory_store.deleted")`

      - `String workspaceId`

    - `class BetaWebhookSessionBudgetReachedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.budget_reached"constant`

        - `SESSION_BUDGET_REACHED("session.budget_reached")`

      - `String workspaceId`

  - `JsonValue; type "event"constant`

    Object type. Always `event` for webhook payloads.

    - `EVENT("event")`

### Beta Webhook Event Data

- `class BetaWebhookEventData: A class that can be one of several variants.union`

  - `class BetaWebhookSessionCreatedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.created"constant`

      - `SESSION_CREATED("session.created")`

    - `String workspaceId`

  - `class BetaWebhookSessionPendingEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.pending"constant`

      - `SESSION_PENDING("session.pending")`

    - `String workspaceId`

  - `class BetaWebhookSessionRunningEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.running"constant`

      - `SESSION_RUNNING("session.running")`

    - `String workspaceId`

  - `class BetaWebhookSessionIdledEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.idled"constant`

      - `SESSION_IDLED("session.idled")`

    - `String workspaceId`

  - `class BetaWebhookSessionRequiresActionEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.requires_action"constant`

      - `SESSION_REQUIRES_ACTION("session.requires_action")`

    - `String workspaceId`

  - `class BetaWebhookSessionArchivedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.archived"constant`

      - `SESSION_ARCHIVED("session.archived")`

    - `String workspaceId`

  - `class BetaWebhookSessionDeletedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.deleted"constant`

      - `SESSION_DELETED("session.deleted")`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusRescheduledEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.status_rescheduled"constant`

      - `SESSION_STATUS_RESCHEDULED("session.status_rescheduled")`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusRunStartedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.status_run_started"constant`

      - `SESSION_STATUS_RUN_STARTED("session.status_run_started")`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusIdledEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.status_idled"constant`

      - `SESSION_STATUS_IDLED("session.status_idled")`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusTerminatedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.status_terminated"constant`

      - `SESSION_STATUS_TERMINATED("session.status_terminated")`

    - `String workspaceId`

  - `class BetaWebhookSessionThreadCreatedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String sessionThreadId`

      ID of the session thread this event refers to.

    - `JsonValue; type "session.thread_created"constant`

      - `SESSION_THREAD_CREATED("session.thread_created")`

    - `String workspaceId`

  - `class BetaWebhookSessionThreadIdledEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String sessionThreadId`

      ID of the session thread this event refers to.

    - `JsonValue; type "session.thread_idled"constant`

      - `SESSION_THREAD_IDLED("session.thread_idled")`

    - `String workspaceId`

  - `class BetaWebhookSessionThreadTerminatedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String sessionThreadId`

      ID of the session thread this event refers to.

    - `JsonValue; type "session.thread_terminated"constant`

      - `SESSION_THREAD_TERMINATED("session.thread_terminated")`

    - `String workspaceId`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.outcome_evaluation_ended"constant`

      - `SESSION_OUTCOME_EVALUATION_ENDED("session.outcome_evaluation_ended")`

    - `String workspaceId`

  - `class BetaWebhookVaultCreatedEventData:`

    - `String id`

      ID of the vault that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault.created"constant`

      - `VAULT_CREATED("vault.created")`

    - `String workspaceId`

  - `class BetaWebhookVaultArchivedEventData:`

    - `String id`

      ID of the vault that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault.archived"constant`

      - `VAULT_ARCHIVED("vault.archived")`

    - `String workspaceId`

  - `class BetaWebhookVaultDeletedEventData:`

    - `String id`

      ID of the vault that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault.deleted"constant`

      - `VAULT_DELETED("vault.deleted")`

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialCreatedEventData:`

    - `String id`

      ID of the vault credential that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault_credential.created"constant`

      - `VAULT_CREDENTIAL_CREATED("vault_credential.created")`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialArchivedEventData:`

    - `String id`

      ID of the vault credential that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault_credential.archived"constant`

      - `VAULT_CREDENTIAL_ARCHIVED("vault_credential.archived")`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialDeletedEventData:`

    - `String id`

      ID of the vault credential that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault_credential.deleted"constant`

      - `VAULT_CREDENTIAL_DELETED("vault_credential.deleted")`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

    - `String id`

      ID of the vault credential that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault_credential.refresh_failed"constant`

      - `VAULT_CREDENTIAL_REFRESH_FAILED("vault_credential.refresh_failed")`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookSessionUpdatedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.updated"constant`

      - `SESSION_UPDATED("session.updated")`

    - `String workspaceId`

  - `class BetaWebhookAgentCreatedEventData:`

    - `String id`

      ID of the agent that triggered the event.

    - `String organizationId`

    - `JsonValue; type "agent.created"constant`

      - `AGENT_CREATED("agent.created")`

    - `String workspaceId`

  - `class BetaWebhookAgentArchivedEventData:`

    - `String id`

      ID of the agent that triggered the event.

    - `String organizationId`

    - `JsonValue; type "agent.archived"constant`

      - `AGENT_ARCHIVED("agent.archived")`

    - `String workspaceId`

  - `class BetaWebhookAgentDeletedEventData:`

    - `String id`

      ID of the agent that triggered the event.

    - `String organizationId`

    - `JsonValue; type "agent.deleted"constant`

      - `AGENT_DELETED("agent.deleted")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentPausedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment.paused"constant`

      - `DEPLOYMENT_PAUSED("deployment.paused")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentRunFailedEventData:`

    - `String id`

      ID of the deployment run that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment_run.failed"constant`

      - `DEPLOYMENT_RUN_FAILED("deployment_run.failed")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentCreatedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment.created"constant`

      - `DEPLOYMENT_CREATED("deployment.created")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentUpdatedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment.updated"constant`

      - `DEPLOYMENT_UPDATED("deployment.updated")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentUnpausedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment.unpaused"constant`

      - `DEPLOYMENT_UNPAUSED("deployment.unpaused")`

    - `String workspaceId`

  - `class BetaWebhookAgentUpdatedEventData:`

    - `String id`

      ID of the agent that triggered the event.

    - `String organizationId`

    - `JsonValue; type "agent.updated"constant`

      - `AGENT_UPDATED("agent.updated")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentArchivedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment.archived"constant`

      - `DEPLOYMENT_ARCHIVED("deployment.archived")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentRunStartedEventData:`

    - `String id`

      ID of the deployment run that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment_run.started"constant`

      - `DEPLOYMENT_RUN_STARTED("deployment_run.started")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentDeletedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment.deleted"constant`

      - `DEPLOYMENT_DELETED("deployment.deleted")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentRunSucceededEventData:`

    - `String id`

      ID of the deployment run that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment_run.succeeded"constant`

      - `DEPLOYMENT_RUN_SUCCEEDED("deployment_run.succeeded")`

    - `String workspaceId`

  - `class BetaWebhookEnvironmentCreatedEventData:`

    - `String id`

      ID of the environment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "environment.created"constant`

      - `ENVIRONMENT_CREATED("environment.created")`

    - `String workspaceId`

  - `class BetaWebhookEnvironmentUpdatedEventData:`

    - `String id`

      ID of the environment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "environment.updated"constant`

      - `ENVIRONMENT_UPDATED("environment.updated")`

    - `String workspaceId`

  - `class BetaWebhookEnvironmentArchivedEventData:`

    - `String id`

      ID of the environment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "environment.archived"constant`

      - `ENVIRONMENT_ARCHIVED("environment.archived")`

    - `String workspaceId`

  - `class BetaWebhookEnvironmentDeletedEventData:`

    - `String id`

      ID of the environment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "environment.deleted"constant`

      - `ENVIRONMENT_DELETED("environment.deleted")`

    - `String workspaceId`

  - `class BetaWebhookMemoryStoreCreatedEventData:`

    - `String id`

      ID of the memory store that triggered the event.

    - `String organizationId`

    - `JsonValue; type "memory_store.created"constant`

      - `MEMORY_STORE_CREATED("memory_store.created")`

    - `String workspaceId`

  - `class BetaWebhookMemoryStoreArchivedEventData:`

    - `String id`

      ID of the memory store that triggered the event.

    - `String organizationId`

    - `JsonValue; type "memory_store.archived"constant`

      - `MEMORY_STORE_ARCHIVED("memory_store.archived")`

    - `String workspaceId`

  - `class BetaWebhookMemoryStoreDeletedEventData:`

    - `String id`

      ID of the memory store that triggered the event.

    - `String organizationId`

    - `JsonValue; type "memory_store.deleted"constant`

      - `MEMORY_STORE_DELETED("memory_store.deleted")`

    - `String workspaceId`

  - `class BetaWebhookSessionBudgetReachedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.budget_reached"constant`

      - `SESSION_BUDGET_REACHED("session.budget_reached")`

    - `String workspaceId`

### Beta Webhook Memory Store Archived Event Data

- `class BetaWebhookMemoryStoreArchivedEventData:`

  - `String id`

    ID of the memory store that triggered the event.

  - `String organizationId`

  - `JsonValue; type "memory_store.archived"constant`

    - `MEMORY_STORE_ARCHIVED("memory_store.archived")`

  - `String workspaceId`

### Beta Webhook Memory Store Created Event Data

- `class BetaWebhookMemoryStoreCreatedEventData:`

  - `String id`

    ID of the memory store that triggered the event.

  - `String organizationId`

  - `JsonValue; type "memory_store.created"constant`

    - `MEMORY_STORE_CREATED("memory_store.created")`

  - `String workspaceId`

### Beta Webhook Memory Store Deleted Event Data

- `class BetaWebhookMemoryStoreDeletedEventData:`

  - `String id`

    ID of the memory store that triggered the event.

  - `String organizationId`

  - `JsonValue; type "memory_store.deleted"constant`

    - `MEMORY_STORE_DELETED("memory_store.deleted")`

  - `String workspaceId`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.archived"constant`

    - `SESSION_ARCHIVED("session.archived")`

  - `String workspaceId`

### Beta Webhook Session Budget Reached Event Data

- `class BetaWebhookSessionBudgetReachedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.budget_reached"constant`

    - `SESSION_BUDGET_REACHED("session.budget_reached")`

  - `String workspaceId`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.created"constant`

    - `SESSION_CREATED("session.created")`

  - `String workspaceId`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.deleted"constant`

    - `SESSION_DELETED("session.deleted")`

  - `String workspaceId`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.idled"constant`

    - `SESSION_IDLED("session.idled")`

  - `String workspaceId`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.outcome_evaluation_ended"constant`

    - `SESSION_OUTCOME_EVALUATION_ENDED("session.outcome_evaluation_ended")`

  - `String workspaceId`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.pending"constant`

    - `SESSION_PENDING("session.pending")`

  - `String workspaceId`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.requires_action"constant`

    - `SESSION_REQUIRES_ACTION("session.requires_action")`

  - `String workspaceId`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.running"constant`

    - `SESSION_RUNNING("session.running")`

  - `String workspaceId`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.status_idled"constant`

    - `SESSION_STATUS_IDLED("session.status_idled")`

  - `String workspaceId`

### Beta Webhook Session Status Rescheduled Event Data

- `class BetaWebhookSessionStatusRescheduledEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.status_rescheduled"constant`

    - `SESSION_STATUS_RESCHEDULED("session.status_rescheduled")`

  - `String workspaceId`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.status_run_started"constant`

    - `SESSION_STATUS_RUN_STARTED("session.status_run_started")`

  - `String workspaceId`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.status_terminated"constant`

    - `SESSION_STATUS_TERMINATED("session.status_terminated")`

  - `String workspaceId`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String sessionThreadId`

    ID of the session thread this event refers to.

  - `JsonValue; type "session.thread_created"constant`

    - `SESSION_THREAD_CREATED("session.thread_created")`

  - `String workspaceId`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String sessionThreadId`

    ID of the session thread this event refers to.

  - `JsonValue; type "session.thread_idled"constant`

    - `SESSION_THREAD_IDLED("session.thread_idled")`

  - `String workspaceId`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String sessionThreadId`

    ID of the session thread this event refers to.

  - `JsonValue; type "session.thread_terminated"constant`

    - `SESSION_THREAD_TERMINATED("session.thread_terminated")`

  - `String workspaceId`

### Beta Webhook Session Updated Event Data

- `class BetaWebhookSessionUpdatedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.updated"constant`

    - `SESSION_UPDATED("session.updated")`

  - `String workspaceId`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData:`

  - `String id`

    ID of the vault that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault.archived"constant`

    - `VAULT_ARCHIVED("vault.archived")`

  - `String workspaceId`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData:`

  - `String id`

    ID of the vault that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault.created"constant`

    - `VAULT_CREATED("vault.created")`

  - `String workspaceId`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData:`

  - `String id`

    ID of the vault credential that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault_credential.archived"constant`

    - `VAULT_CREDENTIAL_ARCHIVED("vault_credential.archived")`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData:`

  - `String id`

    ID of the vault credential that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault_credential.created"constant`

    - `VAULT_CREDENTIAL_CREATED("vault_credential.created")`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData:`

  - `String id`

    ID of the vault credential that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault_credential.deleted"constant`

    - `VAULT_CREDENTIAL_DELETED("vault_credential.deleted")`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData:`

  - `String id`

    ID of the vault credential that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault_credential.refresh_failed"constant`

    - `VAULT_CREDENTIAL_REFRESH_FAILED("vault_credential.refresh_failed")`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData:`

  - `String id`

    ID of the vault that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault.deleted"constant`

    - `VAULT_DELETED("vault.deleted")`

  - `String workspaceId`

### Unwrap Webhook Event

- `class UnwrapWebhookEvent:`

  - `String id`

    Unique event identifier for idempotency.

  - `LocalDateTime createdAt`

    RFC 3339 timestamp when the event occurred.

  - `BetaWebhookEventData data`

    - `class BetaWebhookSessionCreatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.created"constant`

        - `SESSION_CREATED("session.created")`

      - `String workspaceId`

    - `class BetaWebhookSessionPendingEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.pending"constant`

        - `SESSION_PENDING("session.pending")`

      - `String workspaceId`

    - `class BetaWebhookSessionRunningEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.running"constant`

        - `SESSION_RUNNING("session.running")`

      - `String workspaceId`

    - `class BetaWebhookSessionIdledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.idled"constant`

        - `SESSION_IDLED("session.idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionRequiresActionEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.requires_action"constant`

        - `SESSION_REQUIRES_ACTION("session.requires_action")`

      - `String workspaceId`

    - `class BetaWebhookSessionArchivedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.archived"constant`

        - `SESSION_ARCHIVED("session.archived")`

      - `String workspaceId`

    - `class BetaWebhookSessionDeletedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.deleted"constant`

        - `SESSION_DELETED("session.deleted")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusRescheduledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_rescheduled"constant`

        - `SESSION_STATUS_RESCHEDULED("session.status_rescheduled")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusRunStartedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_run_started"constant`

        - `SESSION_STATUS_RUN_STARTED("session.status_run_started")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusIdledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_idled"constant`

        - `SESSION_STATUS_IDLED("session.status_idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusTerminatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_terminated"constant`

        - `SESSION_STATUS_TERMINATED("session.status_terminated")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadCreatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `JsonValue; type "session.thread_created"constant`

        - `SESSION_THREAD_CREATED("session.thread_created")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadIdledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `JsonValue; type "session.thread_idled"constant`

        - `SESSION_THREAD_IDLED("session.thread_idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadTerminatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `JsonValue; type "session.thread_terminated"constant`

        - `SESSION_THREAD_TERMINATED("session.thread_terminated")`

      - `String workspaceId`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.outcome_evaluation_ended"constant`

        - `SESSION_OUTCOME_EVALUATION_ENDED("session.outcome_evaluation_ended")`

      - `String workspaceId`

    - `class BetaWebhookVaultCreatedEventData:`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.created"constant`

        - `VAULT_CREATED("vault.created")`

      - `String workspaceId`

    - `class BetaWebhookVaultArchivedEventData:`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.archived"constant`

        - `VAULT_ARCHIVED("vault.archived")`

      - `String workspaceId`

    - `class BetaWebhookVaultDeletedEventData:`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.deleted"constant`

        - `VAULT_DELETED("vault.deleted")`

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialCreatedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.created"constant`

        - `VAULT_CREDENTIAL_CREATED("vault_credential.created")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialArchivedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.archived"constant`

        - `VAULT_CREDENTIAL_ARCHIVED("vault_credential.archived")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialDeletedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.deleted"constant`

        - `VAULT_CREDENTIAL_DELETED("vault_credential.deleted")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.refresh_failed"constant`

        - `VAULT_CREDENTIAL_REFRESH_FAILED("vault_credential.refresh_failed")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookSessionUpdatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.updated"constant`

        - `SESSION_UPDATED("session.updated")`

      - `String workspaceId`

    - `class BetaWebhookAgentCreatedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue; type "agent.created"constant`

        - `AGENT_CREATED("agent.created")`

      - `String workspaceId`

    - `class BetaWebhookAgentArchivedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue; type "agent.archived"constant`

        - `AGENT_ARCHIVED("agent.archived")`

      - `String workspaceId`

    - `class BetaWebhookAgentDeletedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue; type "agent.deleted"constant`

        - `AGENT_DELETED("agent.deleted")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentPausedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.paused"constant`

        - `DEPLOYMENT_PAUSED("deployment.paused")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunFailedEventData:`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment_run.failed"constant`

        - `DEPLOYMENT_RUN_FAILED("deployment_run.failed")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentCreatedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.created"constant`

        - `DEPLOYMENT_CREATED("deployment.created")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentUpdatedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.updated"constant`

        - `DEPLOYMENT_UPDATED("deployment.updated")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentUnpausedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.unpaused"constant`

        - `DEPLOYMENT_UNPAUSED("deployment.unpaused")`

      - `String workspaceId`

    - `class BetaWebhookAgentUpdatedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue; type "agent.updated"constant`

        - `AGENT_UPDATED("agent.updated")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentArchivedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.archived"constant`

        - `DEPLOYMENT_ARCHIVED("deployment.archived")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunStartedEventData:`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment_run.started"constant`

        - `DEPLOYMENT_RUN_STARTED("deployment_run.started")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentDeletedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.deleted"constant`

        - `DEPLOYMENT_DELETED("deployment.deleted")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunSucceededEventData:`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment_run.succeeded"constant`

        - `DEPLOYMENT_RUN_SUCCEEDED("deployment_run.succeeded")`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentCreatedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "environment.created"constant`

        - `ENVIRONMENT_CREATED("environment.created")`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentUpdatedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "environment.updated"constant`

        - `ENVIRONMENT_UPDATED("environment.updated")`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentArchivedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "environment.archived"constant`

        - `ENVIRONMENT_ARCHIVED("environment.archived")`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentDeletedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "environment.deleted"constant`

        - `ENVIRONMENT_DELETED("environment.deleted")`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreCreatedEventData:`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `JsonValue; type "memory_store.created"constant`

        - `MEMORY_STORE_CREATED("memory_store.created")`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreArchivedEventData:`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `JsonValue; type "memory_store.archived"constant`

        - `MEMORY_STORE_ARCHIVED("memory_store.archived")`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreDeletedEventData:`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `JsonValue; type "memory_store.deleted"constant`

        - `MEMORY_STORE_DELETED("memory_store.deleted")`

      - `String workspaceId`

    - `class BetaWebhookSessionBudgetReachedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.budget_reached"constant`

        - `SESSION_BUDGET_REACHED("session.budget_reached")`

      - `String workspaceId`

  - `JsonValue; type "event"constant`

    Object type. Always `event` for webhook payloads.

    - `EVENT("event")`
