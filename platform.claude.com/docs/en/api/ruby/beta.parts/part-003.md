<!-- source: https://platform.claude.com/docs/en/api/ruby/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/ruby/beta -->

<!-- chunk-start -->

    Who performed this write: one of `session_actor`, `api_actor`, `user_actor`, or `service_account_actor`; `null` when no writer is recorded. Captured at write time and preserved through redaction. A `session_actor` is an agent writing through the store's mounted filesystem at `/mnt/memory/`. The API key that created that session is not recorded on agent writes, so attribution names who made the write, not who is ultimately responsible; look up session provenance via the [Sessions API](https://platform.claude.com/docs/en/api/beta/sessions/retrieve).

    - `class BetaManagedAgentsSessionActor`

      An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

      - `type: :session_actor`

      - `session_id: String`

        ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve) for further provenance.

        minLength: 1

    - `class BetaManagedAgentsAPIActor`

      A direct caller of the public API, identified by the API key that authenticated the request.

      - `type: :api_actor`

      - `api_key_id: String`

        ID of the API key (an `apikey_...` value). This identifies the key, not the secret.

        minLength: 1

    - `class BetaManagedAgentsUserActor`

      A human user, for example acting through the Anthropic Console.

      - `type: :user_actor`

      - `user_id: String`

        ID of the user (a `user_...` value).

        minLength: 1

    - `class BetaManagedAgentsServiceAccountActor`

      A workload authenticated as a service account, for example via Workload Identity Federation.

      - `type: :service_account_actor`

      - `service_account_id: String`

        ID of the service account (a `svac_...` value).

        minLength: 1

  - `path: String`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: Time`

    When this version was redacted, in RFC 3339 format, or `null` if it has not been redacted. When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are all `null`. See [Redact a memory version](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact).

    format: date-time

  - `redacted_by: BetaManagedAgentsActor`

    Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.memory_stores.memory_versions.list("memory_store_id")

puts(page)
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

`beta.memory_stores.memory_versions.retrieve(memory_version_id, **kwargs) -> BetaManagedAgentsMemoryVersion`

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

#### Parameters

- `memory_store_id: String`

  The ID of the memory store that holds the version (`memstore_...`).

- `memory_version_id: String`

  The ID of the memory version to retrieve (`memver_...`).

- `view: BetaManagedAgentsMemoryView`

  Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

  - `:basic`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `:full`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsMemoryVersion`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and are not deleted with the memory; each version is retained for at least the version retention period after it was written, unless the store itself is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `type: :memory_version`

  - `id: String`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: Time`

    When this version was written, in RFC 3339 format.

    format: date-time

  - `memory_id: String`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the memory's retained versions, including the `deleted` row while the lineage is retained.

  - `memory_store_id: String`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation this version records: `created`, `modified`, or `deleted`.

    - `:created`

      The memory was created. The first version in any memory's lineage.

    - `:modified`

      The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`.

    - `:deleted`

      The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash.

  - `content: String`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: Integer`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `created_by: BetaManagedAgentsActor`

    Who performed this write: one of `session_actor`, `api_actor`, `user_actor`, or `service_account_actor`; `null` when no writer is recorded. Captured at write time and preserved through redaction. A `session_actor` is an agent writing through the store's mounted filesystem at `/mnt/memory/`. The API key that created that session is not recorded on agent writes, so attribution names who made the write, not who is ultimately responsible; look up session provenance via the [Sessions API](https://platform.claude.com/docs/en/api/beta/sessions/retrieve).

    - `class BetaManagedAgentsSessionActor`

      An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

      - `type: :session_actor`

      - `session_id: String`

        ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve) for further provenance.

        minLength: 1

    - `class BetaManagedAgentsAPIActor`

      A direct caller of the public API, identified by the API key that authenticated the request.

      - `type: :api_actor`

      - `api_key_id: String`

        ID of the API key (an `apikey_...` value). This identifies the key, not the secret.

        minLength: 1

    - `class BetaManagedAgentsUserActor`

      A human user, for example acting through the Anthropic Console.

      - `type: :user_actor`

      - `user_id: String`

        ID of the user (a `user_...` value).

        minLength: 1

    - `class BetaManagedAgentsServiceAccountActor`

      A workload authenticated as a service account, for example via Workload Identity Federation.

      - `type: :service_account_actor`

      - `service_account_id: String`

        ID of the service account (a `svac_...` value).

        minLength: 1

  - `path: String`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: Time`

    When this version was redacted, in RFC 3339 format, or `null` if it has not been redacted. When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are all `null`. See [Redact a memory version](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact).

    format: date-time

  - `redacted_by: BetaManagedAgentsActor`

    Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_version = anthropic.beta.memory_stores.memory_versions.retrieve(
  "memory_version_id",
  memory_store_id: "memory_store_id"
)

puts(beta_managed_agents_memory_version)
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

`beta.memory_stores.memory_versions.redact(memory_version_id, **kwargs) -> BetaManagedAgentsMemoryVersion`

**POST** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a memory version

#### Parameters

- `memory_store_id: String`

  The ID of the memory store that holds the version (`memstore_...`).

- `memory_version_id: String`

  The ID of the memory version to redact (`memver_...`).

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsMemoryVersion`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and are not deleted with the memory; each version is retained for at least the version retention period after it was written, unless the store itself is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `type: :memory_version`

  - `id: String`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: Time`

    When this version was written, in RFC 3339 format.

    format: date-time

  - `memory_id: String`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the memory's retained versions, including the `deleted` row while the lineage is retained.

  - `memory_store_id: String`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation this version records: `created`, `modified`, or `deleted`.

    - `:created`

      The memory was created. The first version in any memory's lineage.

    - `:modified`

      The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`.

    - `:deleted`

      The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash.

  - `content: String`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: Integer`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `created_by: BetaManagedAgentsActor`

    Who performed this write: one of `session_actor`, `api_actor`, `user_actor`, or `service_account_actor`; `null` when no writer is recorded. Captured at write time and preserved through redaction. A `session_actor` is an agent writing through the store's mounted filesystem at `/mnt/memory/`. The API key that created that session is not recorded on agent writes, so attribution names who made the write, not who is ultimately responsible; look up session provenance via the [Sessions API](https://platform.claude.com/docs/en/api/beta/sessions/retrieve).

    - `class BetaManagedAgentsSessionActor`

      An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

      - `type: :session_actor`

      - `session_id: String`

        ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve) for further provenance.

        minLength: 1

    - `class BetaManagedAgentsAPIActor`

      A direct caller of the public API, identified by the API key that authenticated the request.

      - `type: :api_actor`

      - `api_key_id: String`

        ID of the API key (an `apikey_...` value). This identifies the key, not the secret.

        minLength: 1

    - `class BetaManagedAgentsUserActor`

      A human user, for example acting through the Anthropic Console.

      - `type: :user_actor`

      - `user_id: String`

        ID of the user (a `user_...` value).

        minLength: 1

    - `class BetaManagedAgentsServiceAccountActor`

      A workload authenticated as a service account, for example via Workload Identity Federation.

      - `type: :service_account_actor`

      - `service_account_id: String`

        ID of the service account (a `svac_...` value).

        minLength: 1

  - `path: String`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: Time`

    When this version was redacted, in RFC 3339 format, or `null` if it has not been redacted. When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are all `null`. See [Redact a memory version](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact).

    format: date-time

  - `redacted_by: BetaManagedAgentsActor`

    Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_version = anthropic.beta.memory_stores.memory_versions.redact(
  "memory_version_id",
  memory_store_id: "memory_store_id"
)

puts(beta_managed_agents_memory_version)
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

`beta.files.upload(**kwargs) -> BetaFileMetadata`

**POST** `/v1/files`

Upload File

#### Parameters

- `file: String`

  The file to upload. Only the final path component of the part's `filename` is kept; an absent or empty `filename` is replaced with `unnamed` plus the extension for the file's stored `mime_type`, when known.

  format: binary

- `expires_in_seconds: Integer`

  Seconds from upload until the file expires and its bytes become permanently unavailable. Must be between 3600 (one hour) and 7776000 (ninety days).

  minimum: 3600, maximum: 7776000

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaFileMetadata`

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `filename: String`

    Original filename of the uploaded file.

    minLength: 1, maxLength: 500

  - `mime_type: String`

    MIME type of the file.

    minLength: 1, maxLength: 255

  - `size_bytes: Integer`

    Size of the file in bytes.

    minimum: 0

  - `downloadable: bool`

    Whether the file can be downloaded.

  - `expires_at: Time`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `scope: BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `type: :session`

      The type of scope (e.g., `"session"`).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_file_metadata = anthropic.beta.files.upload(file: StringIO.new("Example data"))

puts(beta_file_metadata)
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

`beta.files.list(**kwargs) -> PageCursor<BetaFileMetadata>`

**GET** `/v1/files`

List Files

#### Parameters

- `ids: Array[String]`

  Restrict the result set to Files whose `id` is in this list. At most 100 entries (after de-duplication). Mutually exclusive with `page` and `limit`. When supplied, the response is always a single page (`next_page` is null). IDs that do not resolve to a visible File — including deleted Files — are silently omitted.

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `page: String`

  Opaque page cursor returned in a prior list response's `next_page`. Prefixed `page_`.

- `scope_id: String`

  Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaFileMetadata`

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `filename: String`

    Original filename of the uploaded file.

    minLength: 1, maxLength: 500

  - `mime_type: String`

    MIME type of the file.

    minLength: 1, maxLength: 255

  - `size_bytes: Integer`

    Size of the file in bytes.

    minimum: 0

  - `downloadable: bool`

    Whether the file can be downloaded.

  - `expires_at: Time`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `scope: BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `type: :session`

      The type of scope (e.g., `"session"`).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.files.list

puts(page)
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

`beta.files.download(file_id, **kwargs) -> StringIO`

**GET** `/v1/files/{file_id}/content`

Download File

#### Parameters

- `file_id: String`

  ID of the File.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `StringIO`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

response = anthropic.beta.files.download("file_id")

puts(response)
```

### Get File Metadata

`beta.files.retrieve_metadata(file_id, **kwargs) -> BetaFileMetadata`

**GET** `/v1/files/{file_id}`

Get File Metadata

#### Parameters

- `file_id: String`

  ID of the File.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaFileMetadata`

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `filename: String`

    Original filename of the uploaded file.

    minLength: 1, maxLength: 500

  - `mime_type: String`

    MIME type of the file.

    minLength: 1, maxLength: 255

  - `size_bytes: Integer`

    Size of the file in bytes.

    minimum: 0

  - `downloadable: bool`

    Whether the file can be downloaded.

  - `expires_at: Time`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `scope: BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `type: :session`

      The type of scope (e.g., `"session"`).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_file_metadata = anthropic.beta.files.retrieve_metadata("file_id")

puts(beta_file_metadata)
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

`beta.files.delete(file_id, **kwargs) -> BetaDeletedFile`

**DELETE** `/v1/files/{file_id}`

Delete File

#### Parameters

- `file_id: String`

  ID of the File.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaDeletedFile`

  - `type: :file_deleted`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

  - `id: String`

    ID of the deleted file.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_deleted_file = anthropic.beta.files.delete("file_id")

puts(beta_deleted_file)
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

`beta.skills.create(**kwargs) -> BetaSkill`

**POST** `/v1/skills`

Create Skill

#### Parameters

- `files: Array[String]`

  Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `display_name: String`

  Human-readable, single-line label for the Skill. Maximum 255 characters.
  Always set: derived from the SKILL.md frontmatter `name` when omitted at
  creation. Not unique.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaSkill`

  - `type: :skill`

    Object type.

    For Skills, this is always `"skill"`.

  - `id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: Time`

    ISO 8601 timestamp of when the skill was created.

    format: date-time

  - `display_name: String`

    Human-readable, single-line label for the Skill. Maximum 255 characters.
    Always set: derived from the SKILL.md frontmatter `name` when omitted at
    creation. Not unique.

  - `latest_version_id: String`

    ID of the newest Skill Version — what `latest` references resolve to. Always set: a Skill holds at least one version.

  - `source: BetaSkillSource`

    Where the Skill comes from.

    Possible values:

    * `"custom"`: authored by the platform user; private to their workspace
    * `"anthropic"`: published by Anthropic; shared and read-only
    * `"anthropic_example"`: Anthropic-published sample Skill
    * `"plugin"`: resolved from an installed plugin

    - `type: :custom | :anthropic | :anthropic_example | :plugin`

      Where the Skill comes from.

      Possible values:

      * `"custom"`: authored by the platform user; private to their workspace
      * `"anthropic"`: published by Anthropic; shared and read-only
      * `"anthropic_example"`: Anthropic-published sample Skill
      * `"plugin"`: resolved from an installed plugin

      - `:custom`

      - `:anthropic`

      - `:anthropic_example`

      - `:plugin`

  - `updated_at: Time`

    ISO 8601 timestamp of when the skill was last updated.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_skill = anthropic.beta.skills.create(files: [StringIO.new("Example data")])

puts(beta_skill)
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

`beta.skills.list(**kwargs) -> PageCursor<BetaSkill>`

**GET** `/v1/skills`

List Skills

#### Parameters

- `limit: Integer`

  Number of results to return per page.

  Ranges from `1` to `1000`. Defaults to `20`.

  minimum: 1, maximum: 1000

- `page: String`

  Pagination token for fetching a specific page of results.

  Pass the value from a previous response's `next_page` field to get the next page of results.

- `source: String`

  Filter skills by source.

  If provided, only skills from the specified source will be returned:

  * `"custom"`: only return user-created skills
  * `"anthropic"`: only return Anthropic-created skills

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaSkill`

  - `type: :skill`

    Object type.

    For Skills, this is always `"skill"`.

  - `id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: Time`

    ISO 8601 timestamp of when the skill was created.

    format: date-time

  - `display_name: String`

    Human-readable, single-line label for the Skill. Maximum 255 characters.
    Always set: derived from the SKILL.md frontmatter `name` when omitted at
    creation. Not unique.

  - `latest_version_id: String`

    ID of the newest Skill Version — what `latest` references resolve to. Always set: a Skill holds at least one version.

  - `source: BetaSkillSource`

    Where the Skill comes from.

    Possible values:

    * `"custom"`: authored by the platform user; private to their workspace
    * `"anthropic"`: published by Anthropic; shared and read-only
    * `"anthropic_example"`: Anthropic-published sample Skill
    * `"plugin"`: resolved from an installed plugin

    - `type: :custom | :anthropic | :anthropic_example | :plugin`

      Where the Skill comes from.

      Possible values:

      * `"custom"`: authored by the platform user; private to their workspace
      * `"anthropic"`: published by Anthropic; shared and read-only
      * `"anthropic_example"`: Anthropic-published sample Skill
      * `"plugin"`: resolved from an installed plugin

      - `:custom`

      - `:anthropic`

      - `:anthropic_example`

      - `:plugin`

  - `updated_at: Time`

    ISO 8601 timestamp of when the skill was last updated.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.skills.list

puts(page)
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

`beta.skills.retrieve(skill_id, **kwargs) -> BetaSkill`

**GET** `/v1/skills/{skill_id}`

Get Skill

#### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaSkill`

  - `type: :skill`

    Object type.

    For Skills, this is always `"skill"`.

  - `id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: Time`

    ISO 8601 timestamp of when the skill was created.

    format: date-time

  - `display_name: String`

    Human-readable, single-line label for the Skill. Maximum 255 characters.
    Always set: derived from the SKILL.md frontmatter `name` when omitted at
    creation. Not unique.

  - `latest_version_id: String`

    ID of the newest Skill Version — what `latest` references resolve to. Always set: a Skill holds at least one version.

  - `source: BetaSkillSource`

    Where the Skill comes from.

    Possible values:

    * `"custom"`: authored by the platform user; private to their workspace
    * `"anthropic"`: published by Anthropic; shared and read-only
    * `"anthropic_example"`: Anthropic-published sample Skill
    * `"plugin"`: resolved from an installed plugin

    - `type: :custom | :anthropic | :anthropic_example | :plugin`

      Where the Skill comes from.

      Possible values:

      * `"custom"`: authored by the platform user; private to their workspace
      * `"anthropic"`: published by Anthropic; shared and read-only
      * `"anthropic_example"`: Anthropic-published sample Skill
      * `"plugin"`: resolved from an installed plugin

      - `:custom`

      - `:anthropic`

      - `:anthropic_example`

      - `:plugin`

  - `updated_at: Time`

    ISO 8601 timestamp of when the skill was last updated.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_skill = anthropic.beta.skills.retrieve("skill_id")

puts(beta_skill)
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

`beta.skills.delete(skill_id, **kwargs) -> BetaDeletedSkill`

**DELETE** `/v1/skills/{skill_id}`

Delete Skill

#### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaDeletedSkill`

  - `type: :skill_deleted`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

  - `id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_deleted_skill = anthropic.beta.skills.delete("skill_id")

puts(beta_deleted_skill)
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

`beta.skills.versions.create(skill_id, **kwargs) -> BetaSkillVersion`

**POST** `/v1/skills/{skill_id}/versions`

Create Skill Version

#### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `files: Array[String]`

  Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaSkillVersion`

  - `type: :skill_version`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `id: String`

    Unique identifier for this Skill Version. The id addresses the version in
    paths and pins it in references.

  - `created_at: Time`

    ISO 8601 timestamp of when the skill was created.

    format: date-time

  - `description: String`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `name: String`

    The Skill's immutable kebab-case slug, set at creation from the first
    upload's SKILL.md frontmatter `name` (or its enclosing directory). Every
    later upload must resolve to the same value. Also the top-level directory
    of the Skill's mounted files and the base name of a downloaded archive.

  - `skill_id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_skill_version = anthropic.beta.skills.versions.create("skill_id", files: [StringIO.new("Example data")])

puts(beta_skill_version)
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

`beta.skills.versions.list(skill_id, **kwargs) -> PageCursor<BetaSkillVersion>`

**GET** `/v1/skills/{skill_id}/versions`

List Skill Versions

#### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `limit: Integer`

  Number of results to return per page.

  Ranges from `1` to `1000`. Defaults to `20`.

  minimum: 1, maximum: 1000

- `page: String`

  Optionally set to the `next_page` token from the previous response.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaSkillVersion`

  - `type: :skill_version`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `id: String`

    Unique identifier for this Skill Version. The id addresses the version in
    paths and pins it in references.

  - `created_at: Time`

    ISO 8601 timestamp of when the skill was created.

    format: date-time

  - `description: String`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `name: String`

    The Skill's immutable kebab-case slug, set at creation from the first
    upload's SKILL.md frontmatter `name` (or its enclosing directory). Every
    later upload must resolve to the same value. Also the top-level directory
    of the Skill's mounted files and the base name of a downloaded archive.

  - `skill_id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.skills.versions.list("skill_id")

puts(page)
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

`beta.skills.versions.download(version, **kwargs) -> StringIO`

**GET** `/v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

#### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: String`

  Identifies the skill version by its version ID.

  Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `StringIO`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

response = anthropic.beta.skills.versions.download("version", skill_id: "skill_id")

puts(response)
```

### Get Skill Version

`beta.skills.versions.retrieve(version, **kwargs) -> BetaSkillVersion`

**GET** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

#### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: String`

  Identifies the skill version: a version ID, or the literal `latest` for the skill's most recent version.

  Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaSkillVersion`

  - `type: :skill_version`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `id: String`

    Unique identifier for this Skill Version. The id addresses the version in
    paths and pins it in references.

  - `created_at: Time`

    ISO 8601 timestamp of when the skill was created.

    format: date-time

  - `description: String`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `name: String`

    The Skill's immutable kebab-case slug, set at creation from the first
    upload's SKILL.md frontmatter `name` (or its enclosing directory). Every
    later upload must resolve to the same value. Also the top-level directory
    of the Skill's mounted files and the base name of a downloaded archive.

  - `skill_id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_skill_version = anthropic.beta.skills.versions.retrieve("version", skill_id: "skill_id")

puts(beta_skill_version)
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

`beta.skills.versions.delete(version, **kwargs) -> BetaDeletedSkillVersion`

**DELETE** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

#### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: String`

  Identifies the skill version by its version ID.

  Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaDeletedSkillVersion`

  - `type: :skill_version_deleted`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

  - `id: String`

    Unique identifier for this Skill Version. The id addresses the version in
    paths and pins it in references.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_deleted_skill_version = anthropic.beta.skills.versions.delete("version", skill_id: "skill_id")

puts(beta_deleted_skill_version)
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

`beta.user_profiles.create(**kwargs) -> BetaUserProfile`

**POST** `/v1/user_profiles`

Create User Profile

#### Parameters

- `access_type: :application | :passthrough`

  How the platform uses the API for this entity. `application` (default): the profile represents an individual end-user of the platform's product. `passthrough`: the profile identifies a company the platform resells Claude access to.

  - `:application`

    The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.

  - `:passthrough`

    The user profile represents a company that the platform resells Claude access to.

- `external_id: String`

  Platform's own identifier for this user. Not enforced unique. Maximum 255 characters. Accepted under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; under `user-profiles-2026-09-04` send `external_user_details.reference_id` instead.

  minLength: 1, maxLength: 255

- `external_user_details: BetaUserProfileExternalUserDetailsParams`

  Details about the entity this profile represents, as the platform states them. Every field is optional. Accepted under the `user-profiles-2026-09-04` beta header only.

  - `account_status: :active | :suspended | :blocked`

    The status of the entity's account on the platform: `active`, `suspended` or `blocked`.

    - `:active`

      The platform has neither restricted nor barred the account of the entity that the user profile represents.

    - `:suspended`

      The platform has restricted the account of the entity that the user profile represents and may restore it.

    - `:blocked`

      The platform has barred the account of the entity that the user profile represents.

  - `country: String`

    The country of the entity (not of the platform), as the platform determines it: an ISO 3166-1 alpha-2 code in upper case, for example `US`. Only the form, two uppercase ASCII letters, is checked.

  - `email_hash: String`

    A hash of the entity's email address, computed by the platform. Anthropic treats it as an opaque string and does not prescribe the hash function. 1 to 255 characters.

    minLength: 1, maxLength: 255

  - `entity_type: :individual | :business | :non_profit | :government`

    What kind of entity the profile represents: `individual`, `business`, `non_profit` or `government`.

    - `:individual`

    - `:business`

    - `:non_profit`

    - `:government`

  - `name_hash: String`

    A hash of the entity's name, computed by the platform. Anthropic treats it as an opaque string and does not prescribe the hash function. 1 to 255 characters.

    minLength: 1, maxLength: 255

  - `onboarded_at: Time`

    When the entity opened its account with the platform, in RFC 3339 format: for an `application` profile, when the end-user signed up; for a `passthrough` profile, when the company became the platform's customer. Must be a complete timestamp no more than 1 minute in the future.

    format: date-time

  - `reference_id: String`

    The platform's own reference for the entity, for example the key of the end-user's row in the platform's database. Not interpreted by Anthropic and not enforced unique. 1 to 255 characters.

    minLength: 1, maxLength: 255

- `external_user_onboarded_at: Time`

  When the entity this profile represents opened its account with the platform, in RFC 3339 format: for an `application` profile, when the end-user signed up; for a `passthrough` profile, when the company became the platform's customer. Must be a complete timestamp no more than 1 minute in the future. Optional. Accepted under the `user-profiles-2026-08-18` beta header; under `user-profiles-2026-09-04` send `external_user_details.onboarded_at` instead.

  format: date-time

- `metadata: Hash[Symbol, String]`

  Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

- `name: String`

  Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a company the platform resells Claude access to (`access_type` `passthrough`), that company's name where known. Maximum 255 characters.

  minLength: 1, maxLength: 255

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaUserProfile`

  A record of an entity that the platform serves through the API, such as an end-user of the platform's product or a company that the platform resells Claude access to.

  A Messages, Message Batches or token counting request can send a profile's `id` in the `anthropic-user-profile-id` header to attribute the request to that entity.

  - `type: :user_profile`

    Object type. Always `user_profile`.

  - `id: String`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: Time`

    When this user profile was created, in RFC 3339 format.

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Hash[Symbol, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: :active | :pending | :rejected`

      Status of the trust grant.

      - `:active`

      - `:pending`

      - `:rejected`

  - `updated_at: Time`

    When this user profile was last modified, in RFC 3339 format. Trust-grant status changes also bump this timestamp.

    format: date-time

  - `access_type: :application | :passthrough`

    How the platform uses the API for this entity: `application` (default) or `passthrough`. Present under the `user-profiles-2026-08-18` and later beta headers.

    - `:application`

      The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.

    - `:passthrough`

      The user profile represents a company that the platform resells Claude access to.

  - `external_id: String`

    Platform's own identifier for this user. Not enforced unique. Present under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; under `user-profiles-2026-09-04` the value is `external_user_details.reference_id`.

  - `external_user_details: BetaUserProfileExternalUserDetails`

    Details about the entity this profile represents, as the platform states them; not verified by Anthropic. Present under the `user-profiles-2026-09-04` beta header, with every field present and `null` until the platform supplies a value; the earlier beta headers serve `reference_id` as the top-level `external_id`, and `user-profiles-2026-08-18` serves `onboarded_at` as `external_user_onboarded_at`.

    - `account_status: :active | :suspended | :blocked`

      The status of the entity's account on the platform: `active`, `suspended` or `blocked`. `null` until the platform supplies one.

      - `:active`

        The platform has neither restricted nor barred the account of the entity that the user profile represents.

      - `:suspended`

        The platform has restricted the account of the entity that the user profile represents and may restore it.

      - `:blocked`

        The platform has barred the account of the entity that the user profile represents.

    - `country: String`

      The country the platform associates with the entity, as an ISO 3166-1 alpha-2 code. `null` until the platform supplies one.

    - `email_hash: String`

      The platform-computed hash of the entity's email address. `null` until the platform supplies one.

    - `entity_type: :individual | :business | :non_profit | :government`

      What kind of entity the profile represents: `individual`, `business`, `non_profit` or `government`. `null` until the platform supplies one.

      - `:individual`

      - `:business`

      - `:non_profit`

      - `:government`

    - `name_hash: String`

      The platform-computed hash of the entity's name. `null` until the platform supplies one.

    - `onboarded_at: Time`

      When the entity opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one.

      format: date-time

    - `reference_id: String`

      The platform's own reference for the entity. `null` until the platform supplies one.

  - `external_user_onboarded_at: Time`

    When the entity this profile represents opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one. Present under the `user-profiles-2026-08-18` beta header; under `user-profiles-2026-09-04` the value is `external_user_details.onboarded_at`.

    format: date-time

  - `name: String`

    Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_user_profile = anthropic.beta.user_profiles.create

puts(beta_user_profile)
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
  "external_user_details": {
    "account_status": "active",
    "country": "country",
    "email_hash": "email_hash",
    "entity_type": "individual",
    "name_hash": "name_hash",
    "onboarded_at": "2019-12-27T18:11:19.117Z",
    "reference_id": "reference_id"
  },
  "external_user_onboarded_at": "2024-11-02T08:15:00Z",
  "name": "Example User"
}
```

### List User Profiles

`beta.user_profiles.list(**kwargs) -> PageCursor<BetaUserProfile>`

**GET** `/v1/user_profiles`

List User Profiles

#### Parameters

- `limit: Integer`

  The maximum number of user profiles to return, from 1 to 100. Defaults to 20.

  format: int32

- `order: :asc | :desc`

  The sort direction, applied to the field that `order_by` selects. Defaults to `desc`.

  - `:asc`

    Oldest first when `order_by` is `created_at`, or names in ascending order when `order_by` is `name`.

  - `:desc`

    Newest first when `order_by` is `created_at`, or names in descending order when `order_by` is `name`. This is the default.

- `order_by: :created_at | :name`

  The field to sort user profiles by, in the direction that `order` sets. Defaults to `created_at`.

  - `:created_at`

    Sort by when each user profile was created. This is the default.

  - `:name`

    Sort by `name`, ignoring the case of ASCII letters. Profiles without a name come last in either direction.

- `page: String`

  The cursor for the page to return, taken from `next_page` in a previous response.

  Leave it out to get the first page.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaUserProfile`

  A record of an entity that the platform serves through the API, such as an end-user of the platform's product or a company that the platform resells Claude access to.

  A Messages, Message Batches or token counting request can send a profile's `id` in the `anthropic-user-profile-id` header to attribute the request to that entity.

  - `type: :user_profile`

    Object type. Always `user_profile`.

  - `id: String`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: Time`

    When this user profile was created, in RFC 3339 format.

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Hash[Symbol, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: :active | :pending | :rejected`

      Status of the trust grant.

      - `:active`

      - `:pending`

      - `:rejected`

  - `updated_at: Time`

    When this user profile was last modified, in RFC 3339 format. Trust-grant status changes also bump this timestamp.

    format: date-time

  - `access_type: :application | :passthrough`

    How the platform uses the API for this entity: `application` (default) or `passthrough`. Present under the `user-profiles-2026-08-18` and later beta headers.

    - `:application`

      The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.

    - `:passthrough`

      The user profile represents a company that the platform resells Claude access to.

  - `external_id: String`

    Platform's own identifier for this user. Not enforced unique. Present under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; under `user-profiles-2026-09-04` the value is `external_user_details.reference_id`.

  - `external_user_details: BetaUserProfileExternalUserDetails`

    Details about the entity this profile represents, as the platform states them; not verified by Anthropic. Present under the `user-profiles-2026-09-04` beta header, with every field present and `null` until the platform supplies a value; the earlier beta headers serve `reference_id` as the top-level `external_id`, and `user-profiles-2026-08-18` serves `onboarded_at` as `external_user_onboarded_at`.

    - `account_status: :active | :suspended | :blocked`

      The status of the entity's account on the platform: `active`, `suspended` or `blocked`. `null` until the platform supplies one.

      - `:active`

        The platform has neither restricted nor barred the account of the entity that the user profile represents.

      - `:suspended`

        The platform has restricted the account of the entity that the user profile represents and may restore it.

      - `:blocked`

        The platform has barred the account of the entity that the user profile represents.

    - `country: String`

      The country the platform associates with the entity, as an ISO 3166-1 alpha-2 code. `null` until the platform supplies one.

    - `email_hash: String`

      The platform-computed hash of the entity's email address. `null` until the platform supplies one.

    - `entity_type: :individual | :business | :non_profit | :government`

      What kind of entity the profile represents: `individual`, `business`, `non_profit` or `government`. `null` until the platform supplies one.

      - `:individual`

      - `:business`

      - `:non_profit`

      - `:government`

    - `name_hash: String`

      The platform-computed hash of the entity's name. `null` until the platform supplies one.

    - `onboarded_at: Time`

      When the entity opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one.

      format: date-time

    - `reference_id: String`

      The platform's own reference for the entity. `null` until the platform supplies one.

  - `external_user_onboarded_at: Time`

    When the entity this profile represents opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one. Present under the `user-profiles-2026-08-18` beta header; under `user-profiles-2026-09-04` the value is `external_user_details.onboarded_at`.

    format: date-time

  - `name: String`

    Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.user_profiles.list

puts(page)
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
      "external_user_details": {
        "account_status": "active",
        "country": "country",
        "email_hash": "email_hash",
        "entity_type": "individual",
        "name_hash": "name_hash",
        "onboarded_at": "2019-12-27T18:11:19.117Z",
        "reference_id": "reference_id"
      },
      "external_user_onboarded_at": "2024-11-02T08:15:00Z",
      "name": "Example User"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Get User Profile

`beta.user_profiles.retrieve(user_profile_id, **kwargs) -> BetaUserProfile`

**GET** `/v1/user_profiles/{user_profile_id}`

Get User Profile

#### Parameters

- `user_profile_id: String`

  The ID of the user profile to get (`uprof_...`).

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaUserProfile`

  A record of an entity that the platform serves through the API, such as an end-user of the platform's product or a company that the platform resells Claude access to.

  A Messages, Message Batches or token counting request can send a profile's `id` in the `anthropic-user-profile-id` header to attribute the request to that entity.

  - `type: :user_profile`

    Object type. Always `user_profile`.

  - `id: String`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: Time`

    When this user profile was created, in RFC 3339 format.

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Hash[Symbol, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: :active | :pending | :rejected`

      Status of the trust grant.

      - `:active`

      - `:pending`

      - `:rejected`

  - `updated_at: Time`

    When this user profile was last modified, in RFC 3339 format. Trust-grant status changes also bump this timestamp.

    format: date-time

  - `access_type: :application | :passthrough`

    How the platform uses the API for this entity: `application` (default) or `passthrough`. Present under the `user-profiles-2026-08-18` and later beta headers.

    - `:application`

      The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.

    - `:passthrough`

      The user profile represents a company that the platform resells Claude access to.

  - `external_id: String`

    Platform's own identifier for this user. Not enforced unique. Present under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; under `user-profiles-2026-09-04` the value is `external_user_details.reference_id`.

  - `external_user_details: BetaUserProfileExternalUserDetails`

    Details about the entity this profile represents, as the platform states them; not verified by Anthropic. Present under the `user-profiles-2026-09-04` beta header, with every field present and `null` until the platform supplies a value; the earlier beta headers serve `reference_id` as the top-level `external_id`, and `user-profiles-2026-08-18` serves `onboarded_at` as `external_user_onboarded_at`.

    - `account_status: :active | :suspended | :blocked`

      The status of the entity's account on the platform: `active`, `suspended` or `blocked`. `null` until the platform supplies one.

      - `:active`

        The platform has neither restricted nor barred the account of the entity that the user profile represents.

      - `:suspended`

        The platform has restricted the account of the entity that the user profile represents and may restore it.

      - `:blocked`

        The platform has barred the account of the entity that the user profile represents.

    - `country: String`

      The country the platform associates with the entity, as an ISO 3166-1 alpha-2 code. `null` until the platform supplies one.

    - `email_hash: String`

      The platform-computed hash of the entity's email address. `null` until the platform supplies one.

    - `entity_type: :individual | :business | :non_profit | :government`

      What kind of entity the profile represents: `individual`, `business`, `non_profit` or `government`. `null` until the platform supplies one.

      - `:individual`

      - `:business`

      - `:non_profit`

      - `:government`

    - `name_hash: String`

      The platform-computed hash of the entity's name. `null` until the platform supplies one.

    - `onboarded_at: Time`

      When the entity opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one.

      format: date-time

    - `reference_id: String`

      The platform's own reference for the entity. `null` until the platform supplies one.

  - `external_user_onboarded_at: Time`

    When the entity this profile represents opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one. Present under the `user-profiles-2026-08-18` beta header; under `user-profiles-2026-09-04` the value is `external_user_details.onboarded_at`.

    format: date-time

  - `name: String`

    Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_user_profile = anthropic.beta.user_profiles.retrieve("uprof_011CZkZCu8hGbp5mYRQgUmz9")

puts(beta_user_profile)
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
  "external_user_details": {
    "account_status": "active",
    "country": "country",
    "email_hash": "email_hash",
    "entity_type": "individual",
    "name_hash": "name_hash",
    "onboarded_at": "2019-12-27T18:11:19.117Z",
    "reference_id": "reference_id"
  },
  "external_user_onboarded_at": "2024-11-02T08:15:00Z",
  "name": "Example User"
}
```

### Update User Profile

`beta.user_profiles.update(user_profile_id, **kwargs) -> BetaUserProfile`

**POST** `/v1/user_profiles/{user_profile_id}`

Update User Profile

#### Parameters

- `user_profile_id: String`

  The ID of the user profile to update (`uprof_...`).

- `access_type: :application | :passthrough`

  If present, replaces the stored access type. Omit to leave unchanged.

  - `:application`

    The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.

  - `:passthrough`

    The user profile represents a company that the platform resells Claude access to.

- `external_id: String`

  If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters. Accepted under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; under `user-profiles-2026-09-04` send `external_user_details.reference_id` instead.

  minLength: 1, maxLength: 255

- `external_user_details: BetaUserProfileExternalUserDetailsParams`

  Details about the entity this profile represents, as the platform states them. Each field sent replaces the stored value; omit a field to leave it unchanged. Once set, a value cannot be cleared and `null` is rejected. Accepted under the `user-profiles-2026-09-04` beta header only.

  - `account_status: :active | :suspended | :blocked`

    The status of the entity's account on the platform: `active`, `suspended` or `blocked`.

    - `:active`

      The platform has neither restricted nor barred the account of the entity that the user profile represents.

    - `:suspended`

      The platform has restricted the account of the entity that the user profile represents and may restore it.

    - `:blocked`

      The platform has barred the account of the entity that the user profile represents.

  - `country: String`

    The country of the entity (not of the platform), as the platform determines it: an ISO 3166-1 alpha-2 code in upper case, for example `US`. Only the form, two uppercase ASCII letters, is checked.

  - `email_hash: String`

    A hash of the entity's email address, computed by the platform. Anthropic treats it as an opaque string and does not prescribe the hash function. 1 to 255 characters.

    minLength: 1, maxLength: 255

  - `entity_type: :individual | :business | :non_profit | :government`

    What kind of entity the profile represents: `individual`, `business`, `non_profit` or `government`.

    - `:individual`

    - `:business`

    - `:non_profit`

    - `:government`

  - `name_hash: String`

    A hash of the entity's name, computed by the platform. Anthropic treats it as an opaque string and does not prescribe the hash function. 1 to 255 characters.

    minLength: 1, maxLength: 255

  - `onboarded_at: Time`

    When the entity opened its account with the platform, in RFC 3339 format: for an `application` profile, when the end-user signed up; for a `passthrough` profile, when the company became the platform's customer. Must be a complete timestamp no more than 1 minute in the future.

    format: date-time

  - `reference_id: String`

    The platform's own reference for the entity, for example the key of the end-user's row in the platform's database. Not interpreted by Anthropic and not enforced unique. 1 to 255 characters.

    minLength: 1, maxLength: 255

- `external_user_onboarded_at: Time`

  If present, replaces the stored account creation time. Omit to leave unchanged; once set, the value cannot be cleared and `null` is rejected. Must be a complete RFC 3339 timestamp no more than 1 minute in the future. Accepted under the `user-profiles-2026-08-18` beta header; under `user-profiles-2026-09-04` send `external_user_details.onboarded_at` instead.

  format: date-time

- `metadata: Hash[Symbol, String]`

  Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

- `name: String`

  If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

  minLength: 1, maxLength: 255

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaUserProfile`

  A record of an entity that the platform serves through the API, such as an end-user of the platform's product or a company that the platform resells Claude access to.

  A Messages, Message Batches or token counting request can send a profile's `id` in the `anthropic-user-profile-id` header to attribute the request to that entity.

  - `type: :user_profile`

    Object type. Always `user_profile`.

  - `id: String`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: Time`

    When this user profile was created, in RFC 3339 format.

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Hash[Symbol, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: :active | :pending | :rejected`

      Status of the trust grant.

      - `:active`

      - `:pending`

      - `:rejected`

  - `updated_at: Time`

    When this user profile was last modified, in RFC 3339 format. Trust-grant status changes also bump this timestamp.

    format: date-time

  - `access_type: :application | :passthrough`

    How the platform uses the API for this entity: `application` (default) or `passthrough`. Present under the `user-profiles-2026-08-18` and later beta headers.

    - `:application`

      The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.

    - `:passthrough`

      The user profile represents a company that the platform resells Claude access to.

  - `external_id: String`

    Platform's own identifier for this user. Not enforced unique. Present under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; under `user-profiles-2026-09-04` the value is `external_user_details.reference_id`.

  - `external_user_details: BetaUserProfileExternalUserDetails`

    Details about the entity this profile represents, as the platform states them; not verified by Anthropic. Present under the `user-profiles-2026-09-04` beta header, with every field present and `null` until the platform supplies a value; the earlier beta headers serve `reference_id` as the top-level `external_id`, and `user-profiles-2026-08-18` serves `onboarded_at` as `external_user_onboarded_at`.

    - `account_status: :active | :suspended | :blocked`

      The status of the entity's account on the platform: `active`, `suspended` or `blocked`. `null` until the platform supplies one.

      - `:active`

        The platform has neither restricted nor barred the account of the entity that the user profile represents.

      - `:suspended`

        The platform has restricted the account of the entity that the user profile represents and may restore it.

      - `:blocked`

        The platform has barred the account of the entity that the user profile represents.

    - `country: String`

      The country the platform associates with the entity, as an ISO 3166-1 alpha-2 code. `null` until the platform supplies one.

    - `email_hash: String`

      The platform-computed hash of the entity's email address. `null` until the platform supplies one.

    - `entity_type: :individual | :business | :non_profit | :government`

      What kind of entity the profile represents: `individual`, `business`, `non_profit` or `government`. `null` until the platform supplies one.

      - `:individual`

      - `:business`

      - `:non_profit`

      - `:government`

    - `name_hash: String`

      The platform-computed hash of the entity's name. `null` until the platform supplies one.

    - `onboarded_at: Time`

      When the entity opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one.

      format: date-time

    - `reference_id: String`

      The platform's own reference for the entity. `null` until the platform supplies one.

  - `external_user_onboarded_at: Time`

    When the entity this profile represents opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one. Present under the `user-profiles-2026-08-18` beta header; under `user-profiles-2026-09-04` the value is `external_user_details.onboarded_at`.

    format: date-time

  - `name: String`

    Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_user_profile = anthropic.beta.user_profiles.update("uprof_011CZkZCu8hGbp5mYRQgUmz9")

puts(beta_user_profile)
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
  "external_user_details": {
    "account_status": "active",
    "country": "country",
    "email_hash": "email_hash",
    "entity_type": "individual",
    "name_hash": "name_hash",
    "onboarded_at": "2019-12-27T18:11:19.117Z",
    "reference_id": "reference_id"
  },
  "external_user_onboarded_at": "2024-11-02T08:15:00Z",
  "name": "Example User"
}
```

### Create Enrollment URL

`beta.user_profiles.create_enrollment_url(user_profile_id, **kwargs) -> BetaUserProfileEnrollmentURL`

**POST** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

#### Parameters

- `user_profile_id: String`

  The ID of the user profile to create an enrollment URL for (`uprof_...`).

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaUserProfileEnrollmentURL`

  A URL to give to the entity that a user profile represents, so that the entity can enroll for a trust grant.

  - `type: :enrollment_url`

    Object type. Always `enrollment_url`.

  - `expires_at: Time`

    When this enrollment URL expires, in RFC 3339 format.

    format: date-time

  - `url: String`

    Enrollment URL to send to the end user. Valid until `expires_at`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_user_profile_enrollment_url = anthropic.beta.user_profiles.create_enrollment_url("uprof_011CZkZCu8hGbp5mYRQgUmz9")

puts(beta_user_profile_enrollment_url)
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

`beta.dreams.create(**kwargs) -> BetaDream`

**POST** `/v1/dreams`

Start an asynchronous job that uses past sessions to produce a reorganized version of a memory store and get back the dream to poll for the result.

By default the dream writes its result to a new memory store and doesn't change the input memory store. The response has `status` set to `pending` and an empty `outputs` array. Poll the dream until `status` is `completed`, `failed`, or `canceled`.

See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#create-a-dream) to learn more about creating dreams.

#### Parameters

- `inputs: Array[BetaDreamInput]`

  The memory store and sessions for the dream to read, as exactly one `memory_store` entry and exactly one `sessions` entry.

  - `class BetaDreamMemoryStoreInput`

    The memory store that a dream reads, given as an entry in `inputs`.

    With `output_behavior` set to `update_existing`, the dream writes its result into this memory store. Otherwise the dream doesn't change it.

    - `type: :memory_store`

    - `memory_store_id: String`

      The ID of the memory store for the dream to read (`memstore_...`).

      The memory store must be in the same workspace as the dream and must not be archived.

      minLength: 1

  - `class BetaDreamSessionsInput`

    The sessions that a dream reads, given as an entry in `inputs`.

    - `type: :sessions`

    - `session_ids: Array[String]`

      The IDs of the sessions whose transcripts the dream reads (`sesn_...`).

      Give 1 to 100 IDs, with no duplicates. Each session must be in the same workspace as the dream. Responses list the IDs in sorted order.

      The [limits table in the Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#limits) lists all the limits on a dream.

- `model: String | BetaDreamModelConfigParam`

  The model that runs a dream, given as a model ID or as an object with `id` and `speed`.

  In the object form, `speed` can only be `standard`.

  The [limits table in the Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#limits) lists the supported models.

  - `String = String`

  - `class BetaDreamModelConfigParam`

    The object form of `model` in a request to create a dream.

    - `id: String`

      The ID of the model to run the dream with.

      The ID can be 1 to 256 characters long.

      The [limits table in the Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#limits) lists the supported models.

      minLength: 1, maxLength: 256

    - `speed: :standard | :fast`

      How fast the model generates output for the dream. Defaults to `standard`.

      Dreams accept only `standard`.

      - `:standard`

      - `:fast`

- `instructions: String`

  Guidance that steers how the dream reads the sessions and organizes the output memory store, from 1 to 4,096 characters.

  See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#steer-with-instructions) for what kinds of instructions work well.

  minLength: 1, maxLength: 4096

- `output_behavior: BetaOutputBehavior`

  Which memory store a dream writes its result to. Defaults to `create_new` when left out of a create request.

  - `class BetaOutputBehaviorCreateNew`

    Write the result to a new memory store that starts as a copy of the input memory store. This is the default.

    The new memory store is in the same workspace as the dream. The dream doesn't change the input memory store.

    - `type: :create_new`

  - `class BetaOutputBehaviorUpdateExisting`

    Write the result into the input memory store instead of a new memory store.

    The credential must be allowed to write memory stores, or the request returns a 403 error. While another `update_existing` dream on the same memory store hasn't fully stopped, the request returns a 409 error.

    - `type: :update_existing`

    - `memory_store_id: String`

      The ID of the memory store for the dream to write its result to (`memstore_...`). It must be the memory store in the `memory_store` entry of `inputs`.

      minLength: 1

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaDream`

  An asynchronous job that reads a memory store and past sessions, then writes a reorganized version of that memory store.

  By default the dream writes its result to a new memory store and doesn't change the input memory store. With `output_behavior` set to `update_existing`, it writes its result into the input memory store instead.

  The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#how-it-works) for what a dream reads and produces.

  - `type: :dream`

  - `id: String`

    The unique ID of the dream (`drm_...`).

  - `archived_at: Time`

    When the dream was archived, in RFC 3339, or `null` if it hasn't been archived.

    format: date-time

  - `created_at: Time`

    When the dream was created, in RFC 3339.

    Lists of dreams are sorted by this time, newest first.

    format: date-time

  - `ended_at: Time`

    When the dream reached `completed`, `failed`, or `canceled`, in RFC 3339, or `null` if it is still `pending` or `running`.

    format: date-time

  - `error: BetaDreamError`

    Why the dream failed, or `null` if `status` isn't `failed`.

    - `type: String`

      A code for why the dream failed, such as `timeout` or `internal_error`.

      The [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#errors) lists common error codes and when they occur.

    - `message: String`

      A human-readable explanation of why the dream failed.

  - `inputs: Array[BetaDreamInput]`

    The sources that the dream reads, from the request that created it.

    - `class BetaDreamMemoryStoreInput`

      The memory store that a dream reads, given as an entry in `inputs`.

      With `output_behavior` set to `update_existing`, the dream writes its result into this memory store. Otherwise the dream doesn't change it.

      - `type: :memory_store`

      - `memory_store_id: String`

        The ID of the memory store for the dream to read (`memstore_...`).

        The memory store must be in the same workspace as the dream and must not be archived.

        minLength: 1

    - `class BetaDreamSessionsInput`

      The sessions that a dream reads, given as an entry in `inputs`.

      - `type: :sessions`

      - `session_ids: Array[String]`

        The IDs of the sessions whose transcripts the dream reads (`sesn_...`).

        Give 1 to 100 IDs, with no duplicates. Each session must be in the same workspace as the dream. Responses list the IDs in sorted order.

        The [limits table in the Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#limits) lists all the limits on a dream.

  - `instructions: String`

    The guidance given when the dream was created, or `null` if none was given.

  - `model: BetaDreamModelConfig`

    The model that runs a dream, from the request that created it.

    The dream uses this model for all of its work. The response always gives the model as an object, even if the request gave only a model ID.

    - `id: String`

      The ID of the model that runs the dream, as given in the request that created it.

      minLength: 1, maxLength: 256

    - `speed: :standard | :fast`

      How fast the model generates output for the dream. Always `standard`.

      - `:standard`

      - `:fast`

  - `output_behavior: BetaOutputBehavior`

    Where the dream writes its result, as set in the request that created the dream. If that request left out `output_behavior`, the dream used the `create_new` behavior.

    - `class BetaOutputBehaviorCreateNew`

      Write the result to a new memory store that starts as a copy of the input memory store. This is the default.

      The new memory store is in the same workspace as the dream. The dream doesn't change the input memory store.

      - `type: :create_new`

    - `class BetaOutputBehaviorUpdateExisting`

      Write the result into the input memory store instead of a new memory store.

      The credential must be allowed to write memory stores, or the request returns a 403 error. While another `update_existing` dream on the same memory store hasn't fully stopped, the request returns a 409 error.

      - `type: :update_existing`

      - `memory_store_id: String`

        The ID of the memory store for the dream to write its result to (`memstore_...`). It must be the memory store in the `memory_store` entry of `inputs`.

        minLength: 1

  - `outputs: Array[BetaDreamOutput]`

    The memory store that holds the dream's result, as a one-item array, or an empty array until the dream records that memory store.

    The array is empty while the dream is `pending` and for a short time after it starts `running`. It can stay empty if the dream fails or is canceled before then. The memory store holds the complete result only once `status` is `completed`.

    See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#use-the-output) for how to review and use the result.

    - `type: :memory_store`

    - `memory_store_id: String`

      The ID of the memory store that the dream writes its result to (`memstore_...`).

      With `output_behavior` set to `create_new`, this is a new memory store. With `update_existing`, it is the input memory store.

  - `session_id: String`

    The ID of the session that runs the dream (`sesn_...`), or `null` if that session hasn't started.

    Stream that session's events to follow what the dream reads and writes.

    See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#watch-the-pipeline-run) for how to watch a running dream.

  - `status: BetaDreamStatus`

    Where a dream is in its lifecycle.

    `completed`, `failed`, and `canceled` are final: once a dream has one of these statuses, its status doesn't change again.

    See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#lifecycle) for what each status means.

    - `:pending`

      The dream is waiting to start and hasn't read its inputs yet.

      `outputs` is empty and every `usage` count is zero.

    - `:running`

      The dream is reading its inputs and writing its result.

      `usage` updates while the dream has this status.

    - `:completed`

      The dream finished and its output memory store holds the complete result.

    - `:failed`

      The dream stopped with an error, which `error` describes.

      If `outputs` references a memory store, that memory store keeps what the dream wrote before it stopped.

    - `:canceled`

      A cancel request stopped the dream before it reached `completed` or `failed`.

      If `outputs` references a memory store, that memory store keeps what the dream wrote. `usage` can keep changing after the cancel.

  - `usage: BetaDreamUsage`

    The dream's token counts, which stop changing once its `status` is `completed` or `failed`. After a cancel, they can keep changing.

    - `cache_creation_input_tokens: Integer`

      The dream's input tokens that were written to the prompt cache, for both the 5-minute and 1-hour cache durations.

      format: int32

    - `cache_read_input_tokens: Integer`

      The dream's input tokens that were read from the prompt cache.

      format: int32

    - `input_tokens: Integer`

      The dream's input tokens that weren't read from or written to the prompt cache.

      format: int32

    - `output_tokens: Integer`

      The tokens that the model generated for the dream.

      format: int32

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_dream = anthropic.beta.dreams.create(inputs: [{memory_store_id: "x", type: :memory_store}], model: "string")

puts(beta_dream)
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

`beta.dreams.list(**kwargs) -> PageCursor<BetaDream>`

**GET** `/v1/dreams`

List the dreams in the workspace, newest first.

Archived dreams are left out unless `include_archived` is `true`.

See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#list-dreams) for how to page through dreams.

#### Parameters

- `created_at_gt: Time`

  Return only dreams created after this time (exclusive), in RFC 3339.

  format: date-time

- `created_at_lt: Time`

  Return only dreams created before this time (exclusive), in RFC 3339.

  format: date-time

- `include_archived: bool`

  Whether to include archived dreams. Defaults to `false`.

- `limit: Integer`

  The maximum number of dreams to return, from 1 to 100. Defaults to 20.

  format: int32

- `page: String`

  The cursor for the page to return, taken from `next_page` in a previous response.

  Leave it out to get the first page.

- `statuses: Array[BetaDreamStatus]`

  Return only dreams that have one of these statuses.

  Repeat the parameter to give more than one status. Leave it out to return dreams of every status.

  - `:pending`

    The dream is waiting to start and hasn't read its inputs yet.

    `outputs` is empty and every `usage` count is zero.

  - `:running`

    The dream is reading its inputs and writing its result.

    `usage` updates while the dream has this status.

  - `:completed`

    The dream finished and its output memory store holds the complete result.

  - `:failed`

    The dream stopped with an error, which `error` describes.

    If `outputs` references a memory store, that memory store keeps what the dream wrote before it stopped.

  - `:canceled`

    A cancel request stopped the dream before it reached `completed` or `failed`.

    If `outputs` references a memory store, that memory store keeps what the dream wrote. `usage` can keep changing after the cancel.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaDream`

  An asynchronous job that reads a memory store and past sessions, then writes a reorganized version of that memory store.

  By default the dream writes its result to a new memory store and doesn't change the input memory store. With `output_behavior` set to `update_existing`, it writes its result into the input memory store instead.

  The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#how-it-works) for what a dream reads and produces.

  - `type: :dream`

  - `id: String`

    The unique ID of the dream (`drm_...`).

  - `archived_at: Time`

    When the dream was archived, in RFC 3339, or `null` if it hasn't been archived.

    format: date-time

  - `created_at: Time`

    When the dream was created, in RFC 3339.

    Lists of dreams are sorted by this time, newest first.

    format: date-time

  - `ended_at: Time`

    When the dream reached `completed`, `failed`, or `canceled`, in RFC 3339, or `null` if it is still `pending` or `running`.

    format: date-time

  - `error: BetaDreamError`

    Why the dream failed, or `null` if `status` isn't `failed`.

    - `type: String`

      A code for why the dream failed, such as `timeout` or `internal_error`.

      The [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#errors) lists common error codes and when they occur.

    - `message: String`

      A human-readable explanation of why the dream failed.

  - `inputs: Array[BetaDreamInput]`

    The sources that the dream reads, from the request that created it.

    - `class BetaDreamMemoryStoreInput`

      The memory store that a dream reads, given as an entry in `inputs`.

      With `output_behavior` set to `update_existing`, the dream writes its result into this memory store. Otherwise the dream doesn't change it.

      - `type: :memory_store`

      - `memory_store_id: String`

        The ID of the memory store for the dream to read (`memstore_...`).

        The memory store must be in the same workspace as the dream and must not be archived.

        minLength: 1

    - `class BetaDreamSessionsInput`

      The sessions that a dream reads, given as an entry in `inputs`.

      - `type: :sessions`

      - `session_ids: Array[String]`

        The IDs of the sessions whose transcripts the dream reads (`sesn_...`).

        Give 1 to 100 IDs, with no duplicates. Each session must be in the same workspace as the dream. Responses list the IDs in sorted order.

        The [limits table in the Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#limits) lists all the limits on a dream.

  - `instructions: String`

    The guidance given when the dream was created, or `null` if none was given.

  - `model: BetaDreamModelConfig`

    The model that runs a dream, from the request that created it.

    The dream uses this model for all of its work. The response always gives the model as an object, even if the request gave only a model ID.

    - `id: String`

      The ID of the model that runs the dream, as given in the request that created it.

      minLength: 1, maxLength: 256

    - `speed: :standard | :fast`

      How fast the model generates output for the dream. Always `standard`.

      - `:standard`

      - `:fast`

  - `output_behavior: BetaOutputBehavior`

    Where the dream writes its result, as set in the request that created the dream. If that request left out `output_behavior`, the dream used the `create_new` behavior.

    - `class BetaOutputBehaviorCreateNew`

      Write the result to a new memory store that starts as a copy of the input memory store. This is the default.

      The new memory store is in the same workspace as the dream. The dream doesn't change the input memory store.

      - `type: :create_new`

    - `class BetaOutputBehaviorUpdateExisting`

      Write the result into the input memory store instead of a new memory store.

      The credential must be allowed to write memory stores, or the request returns a 403 error. While another `update_existing` dream on the same memory store hasn't fully stopped, the request returns a 409 error.

      - `type: :update_existing`

      - `memory_store_id: String`

        The ID of the memory store for the dream to write its result to (`memstore_...`). It must be the memory store in the `memory_store` entry of `inputs`.

        minLength: 1

  - `outputs: Array[BetaDreamOutput]`

    The memory store that holds the dream's result, as a one-item array, or an empty array until the dream records that memory store.

    The array is empty while the dream is `pending` and for a short time after it starts `running`. It can stay empty if the dream fails or is canceled before then. The memory store holds the complete result only once `status` is `completed`.

    See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#use-the-output) for how to review and use the result.

    - `type: :memory_store`

    - `memory_store_id: String`

      The ID of the memory store that the dream writes its result to (`memstore_...`).

      With `output_behavior` set to `create_new`, this is a new memory store. With `update_existing`, it is the input memory store.

  - `session_id: String`

    The ID of the session that runs the dream (`sesn_...`), or `null` if that session hasn't started.

    Stream that session's events to follow what the dream reads and writes.

    See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#watch-the-pipeline-run) for how to watch a running dream.

  - `status: BetaDreamStatus`

    Where a dream is in its lifecycle.

    `completed`, `failed`, and `canceled` are final: once a dream has one of these statuses, its status doesn't change again.

    See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#lifecycle) for what each status means.

    - `:pending`

      The dream is waiting to start and hasn't read its inputs yet.

      `outputs` is empty and every `usage` count is zero.

    - `:running`

      The dream is reading its inputs and writing its result.

      `usage` updates while the dream has this status.

    - `:completed`

      The dream finished and its output memory store holds the complete result.

    - `:failed`

      The dream stopped with an error, which `error` describes.

      If `outputs` references a memory store, that memory store keeps what the dream wrote before it stopped.

    - `:canceled`

      A cancel request stopped the dream before it reached `completed` or `failed`.

      If `outputs` references a memory store, that memory store keeps what the dream wrote. `usage` can keep changing after the cancel.

  - `usage: BetaDreamUsage`

    The dream's token counts, which stop changing once its `status` is `completed` or `failed`. After a cancel, they can keep changing.

    - `cache_creation_input_tokens: Integer`

      The dream's input tokens that were written to the prompt cache, for both the 5-minute and 1-hour cache durations.

      format: int32

    - `cache_read_input_tokens: Integer`

      The dream's input tokens that were read from the prompt cache.

      format: int32

    - `input_tokens: Integer`

      The dream's input tokens that weren't read from or written to the prompt cache.

      format: int32

    - `output_tokens: Integer`

      The tokens that the model generated for the dream.

      format: int32

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.dreams.list

puts(page)
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

`beta.dreams.retrieve(dream_id, **kwargs) -> BetaDream`

**GET** `/v1/dreams/{dream_id}`

Get a dream by ID to check its status, output memory store, and token usage.

Archived dreams are returned too.

See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#track-progress) for how to poll a dream and what each status means.

#### Parameters

- `dream_id: String`

  The ID of the dream to get (`drm_...`).

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaDream`

  An asynchronous job that reads a memory store and past sessions, then writes a reorganized version of that memory store.

  By default the dream writes its result to a new memory store and doesn't change the input memory store. With `output_behavior` set to `update_existing`, it writes its result into the input memory store instead.

  The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#how-it-works) for what a dream reads and produces.

  - `type: :dream`

  - `id: String`

    The unique ID of the dream (`drm_...`).

  - `archived_at: Time`

    When the dream was archived, in RFC 3339, or `null` if it hasn't been archived.

    format: date-time

  - `created_at: Time`

    When the dream was created, in RFC 3339.

    Lists of dreams are sorted by this time, newest first.

    format: date-time

  - `ended_at: Time`

    When the dream reached `completed`, `failed`, or `canceled`, in RFC 3339, or `null` if it is still `pending` or `running`.

    format: date-time

  - `error: BetaDreamError`

    Why the dream failed, or `null` if `status` isn't `failed`.

    - `type: String`

      A code for why the dream failed, such as `timeout` or `internal_error`.

      The [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#errors) lists common error codes and when they occur.

    - `message: String`

      A human-readable explanation of why the dream failed.

  - `inputs: Array[BetaDreamInput]`

    The sources that the dream reads, from the request that created it.

    - `class BetaDreamMemoryStoreInput`

      The memory store that a dream reads, given as an entry in `inputs`.

      With `output_behavior` set to `update_existing`, the dream writes its result into this memory store. Otherwise the dream doesn't change it.

      - `type: :memory_store`

      - `memory_store_id: String`

        The ID of the memory store for the dream to read (`memstore_...`).

        The memory store must be in the same workspace as the dream and must not be archived.

        minLength: 1

    - `class BetaDreamSessionsInput`

      The sessions that a dream reads, given as an entry in `inputs`.

      - `type: :sessions`

      - `session_ids: Array[String]`

        The IDs of the sessions whose transcripts the dream reads (`sesn_...`).

        Give 1 to 100 IDs, with no duplicates. Each session must be in the same workspace as the dream. Responses list the IDs in sorted order.

        The [limits table in the Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#limits) lists all the limits on a dream.

  - `instructions: String`

    The guidance given when the dream was created, or `null` if none was given.

  - `model: BetaDreamModelConfig`

    The model that runs a dream, from the request that created it.

    The dream uses this model for all of its work. The response always gives the model as an object, even if the request gave only a model ID.

    - `id: String`

      The ID of the model that runs the dream, as given in the request that created it.

      minLength: 1, maxLength: 256

    - `speed: :standard | :fast`

      How fast the model generates output for the dream. Always `standard`.

      - `:standard`

      - `:fast`

  - `output_behavior: BetaOutputBehavior`

    Where the dream writes its result, as set in the request that created the dream. If that request left out `output_behavior`, the dream used the `create_new` behavior.

    - `class BetaOutputBehaviorCreateNew`

      Write the result to a new memory store that starts as a copy of the input memory store. This is the default.

      The new memory store is in the same workspace as the dream. The dream doesn't change the input memory store.

      - `type: :create_new`

    - `class BetaOutputBehaviorUpdateExisting`

      Write the result into the input memory store instead of a new memory store.

      The credential must be allowed to write memory stores, or the request returns a 403 error. While another `update_existing` dream on the same memory store hasn't fully stopped, the request returns a 409 error.

      - `type: :update_existing`

      - `memory_store_id: String`

        The ID of the memory store for the dream to write its result to (`memstore_...`). It must be the memory store in the `memory_store` entry of `inputs`.

        minLength: 1

  - `outputs: Array[BetaDreamOutput]`

    The memory store that holds the dream's result, as a one-item array, or an empty array until the dream records that memory store.

    The array is empty while the dream is `pending` and for a short time after it starts `running`. It can stay empty if the dream fails or is canceled before then. The memory store holds the complete result only once `status` is `completed`.

    See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#use-the-output) for how to review and use the result.

    - `type: :memory_store`

    - `memory_store_id: String`

      The ID of the memory store that the dream writes its result to (`memstore_...`).

      With `output_behavior` set to `create_new`, this is a new memory store. With `update_existing`, it is the input memory store.

  - `session_id: String`

    The ID of the session that runs the dream (`sesn_...`), or `null` if that session hasn't started.

    Stream that session's events to follow what the dream reads and writes.

    See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#watch-the-pipeline-run) for how to watch a running dream.

  - `status: BetaDreamStatus`

    Where a dream is in its lifecycle.

    `completed`, `failed`, and `canceled` are final: once a dream has one of these statuses, its status doesn't change again.

    See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#lifecycle) for what each status means.

    - `:pending`

      The dream is waiting to start and hasn't read its inputs yet.

      `outputs` is empty and every `usage` count is zero.

    - `:running`

      The dream is reading its inputs and writing its result.

      `usage` updates while the dream has this status.

    - `:completed`

      The dream finished and its output memory store holds the complete result.

    - `:failed`

      The dream stopped with an error, which `error` describes.

      If `outputs` references a memory store, that memory store keeps what the dream wrote before it stopped.

    - `:canceled`

      A cancel request stopped the dream before it reached `completed` or `failed`.

      If `outputs` references a memory store, that memory store keeps what the dream wrote. `usage` can keep changing after the cancel.

  - `usage: BetaDreamUsage`

    The dream's token counts, which stop changing once its `status` is `completed` or `failed`. After a cancel, they can keep changing.

    - `cache_creation_input_tokens: Integer`

      The dream's input tokens that were written to the prompt cache, for both the 5-minute and 1-hour cache durations.

      format: int32

    - `cache_read_input_tokens: Integer`

      The dream's input tokens that were read from the prompt cache.

      format: int32

    - `input_tokens: Integer`

      The dream's input tokens that weren't read from or written to the prompt cache.

      format: int32

    - `output_tokens: Integer`

      The tokens that the model generated for the dream.

      format: int32

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_dream = anthropic.beta.dreams.retrieve("dream_id")

puts(beta_dream)
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

`beta.dreams.cancel(dream_id, **kwargs) -> BetaDream`

**POST** `/v1/dreams/{dream_id}/cancel`

Stop a `pending` or `running` dream.

The response shows `status` as `canceled`, unless the dream reached `completed` or `failed` first. `usage` can keep changing after the response. Canceling a `canceled` dream returns it unchanged. Canceling a `completed` or `failed` dream returns a 400 error.

See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#cancel-a-dream) to learn more about canceling dreams.

#### Parameters

- `dream_id: String`

  The ID of the dream to cancel (`drm_...`).

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaDream`

  An asynchronous job that reads a memory store and past sessions, then writes a reorganized version of that memory store.

  By default the dream writes its result to a new memory store and doesn't change the input memory store. With `output_behavior` set to `update_existing`, it writes its result into the input memory store instead.

  The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#how-it-works) for what a dream reads and produces.

  - `type: :dream`

  - `id: String`

    The unique ID of the dream (`drm_...`).

  - `archived_at: Time`

    When the dream was archived, in RFC 3339, or `null` if it hasn't been archived.

    format: date-time

  - `created_at: Time`

    When the dream was created, in RFC 3339.

    Lists of dreams are sorted by this time, newest first.

    format: date-time

  - `ended_at: Time`

    When the dream reached `completed`, `failed`, or `canceled`, in RFC 3339, or `null` if it is still `pending` or `running`.

    format: date-time

  - `error: BetaDreamError`

    Why the dream failed, or `null` if `status` isn't `failed`.

    - `type: String`

      A code for why the dream failed, such as `timeout` or `internal_error`.

      The [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#errors) lists common error codes and when they occur.

    - `message: String`

      A human-readable explanation of why the dream failed.

  - `inputs: Array[BetaDreamInput]`

    The sources that the dream reads, from the request that created it.

    - `class BetaDreamMemoryStoreInput`

      The memory store that a dream reads, given as an entry in `inputs`.

      With `output_behavior` set to `update_existing`, the dream writes its result into this memory store. Otherwise the dream doesn't change it.

      - `type: :memory_store`

      - `memory_store_id: String`

        The ID of the memory store for the dream to read (`memstore_...`).

        The memory store must be in the same workspace as the dream and must not be archived.

        minLength: 1

    - `class BetaDreamSessionsInput`

      The sessions that a dream reads, given as an entry in `inputs`.

      - `type: :sessions`

      - `session_ids: Array[String]`

        The IDs of the sessions whose transcripts the dream reads (`sesn_...`).

        Give 1 to 100 IDs, with no duplicates. Each session must be in the same workspace as the dream. Responses list the IDs in sorted order.

        The [limits table in the Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#limits) lists all the limits on a dream.

  - `instructions: String`

    The guidance given when the dream was created, or `null` if none was given.

  - `model: BetaDreamModelConfig`

    The model that runs a dream, from the request that created it.

    The dream uses this model for all of its work. The response always gives the model as an object, even if the request gave only a model ID.

    - `id: String`

      The ID of the model that runs the dream, as given in the request that created it.

      minLength: 1, maxLength: 256

    - `speed: :standard | :fast`

      How fast the model generates output for the dream. Always `standard`.

      - `:standard`

      - `:fast`

  - `output_behavior: BetaOutputBehavior`

    Where the dream writes its result, as set in the request that created the dream. If that request left out `output_behavior`, the dream used the `create_new` behavior.

    - `class BetaOutputBehaviorCreateNew`

      Write the result to a new memory store that starts as a copy of the input memory store. This is the default.

      The new memory store is in the same workspace as the dream. The dream doesn't change the input memory store.

      - `type: :create_new`

    - `class BetaOutputBehaviorUpdateExisting`

      Write the result into the input memory store instead of a new memory store.

      The credential must be allowed to write memory stores, or the request returns a 403 error. While another `update_existing` dream on the same memory store hasn't fully stopped, the request returns a 409 error.

      - `type: :update_existing`

      - `memory_store_id: String`

        The ID of the memory store for the dream to write its result to (`memstore_...`). It must be the memory store in the `memory_store` entry of `inputs`.

        minLength: 1

  - `outputs: Array[BetaDreamOutput]`

    The memory store that holds the dream's result, as a one-item array, or an empty array until the dream records that memory store.

    The array is empty while the dream is `pending` and for a short time after it starts `running`. It can stay empty if the dream fails or is canceled before then. The memory store holds the complete result only once `status` is `completed`.

    See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#use-the-output) for how to review and use the result.

    - `type: :memory_store`

    - `memory_store_id: String`

      The ID of the memory store that the dream writes its result to (`memstore_...`).

      With `output_behavior` set to `create_new`, this is a new memory store. With `update_existing`, it is the input memory store.

  - `session_id: String`

    The ID of the session that runs the dream (`sesn_...`), or `null` if that session hasn't started.

    Stream that session's events to follow what the dream reads and writes.

    See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#watch-the-pipeline-run) for how to watch a running dream.

  - `status: BetaDreamStatus`

    Where a dream is in its lifecycle.

    `completed`, `failed`, and `canceled` are final: once a dream has one of these statuses, its status doesn't change again.

    See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#lifecycle) for what each status means.

    - `:pending`

      The dream is waiting to start and hasn't read its inputs yet.

      `outputs` is empty and every `usage` count is zero.

    - `:running`

      The dream is reading its inputs and writing its result.

      `usage` updates while the dream has this status.

    - `:completed`

      The dream finished and its output memory store holds the complete result.

    - `:failed`

      The dream stopped with an error, which `error` describes.

      If `outputs` references a memory store, that memory store keeps what the dream wrote before it stopped.

    - `:canceled`

      A cancel request stopped the dream before it reached `completed` or `failed`.

      If `outputs` references a memory store, that memory store keeps what the dream wrote. `usage` can keep changing after the cancel.

  - `usage: BetaDreamUsage`

    The dream's token counts, which stop changing once its `status` is `completed` or `failed`. After a cancel, they can keep changing.

    - `cache_creation_input_tokens: Integer`

      The dream's input tokens that were written to the prompt cache, for both the 5-minute and 1-hour cache durations.

      format: int32

    - `cache_read_input_tokens: Integer`

      The dream's input tokens that were read from the prompt cache.

      format: int32

    - `input_tokens: Integer`

      The dream's input tokens that weren't read from or written to the prompt cache.

      format: int32

    - `output_tokens: Integer`

      The tokens that the model generated for the dream.

      format: int32

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_dream = anthropic.beta.dreams.cancel("dream_id")

puts(beta_dream)
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

`beta.dreams.archive(dream_id, **kwargs) -> BetaDream`

**POST** `/v1/dreams/{dream_id}/archive`

Hide a `completed`, `failed`, or `canceled` dream from the default list of dreams.

Archiving a `pending` or `running` dream returns a 400 error, so cancel it first. Archiving an archived dream returns it unchanged. An archived dream can still be fetched by ID. Archiving can't be undone.

See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#archive-a-dream) to learn more about archiving dreams.

#### Parameters

- `dream_id: String`

  The ID of the dream to archive (`drm_...`).

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaDream`

  An asynchronous job that reads a memory store and past sessions, then writes a reorganized version of that memory store.

  By default the dream writes its result to a new memory store and doesn't change the input memory store. With `output_behavior` set to `update_existing`, it writes its result into the input memory store instead.

  The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#how-it-works) for what a dream reads and produces.

  - `type: :dream`

  - `id: String`

    The unique ID of the dream (`drm_...`).

  - `archived_at: Time`

    When the dream was archived, in RFC 3339, or `null` if it hasn't been archived.

    format: date-time

  - `created_at: Time`

    When the dream was created, in RFC 3339.

    Lists of dreams are sorted by this time, newest first.

    format: date-time

  - `ended_at: Time`

    When the dream reached `completed`, `failed`, or `canceled`, in RFC 3339, or `null` if it is still `pending` or `running`.

    format: date-time

  - `error: BetaDreamError`

    Why the dream failed, or `null` if `status` isn't `failed`.

    - `type: String`

      A code for why the dream failed, such as `timeout` or `internal_error`.

      The [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#errors) lists common error codes and when they occur.

    - `message: String`

      A human-readable explanation of why the dream failed.

  - `inputs: Array[BetaDreamInput]`

    The sources that the dream reads, from the request that created it.

    - `class BetaDreamMemoryStoreInput`

      The memory store that a dream reads, given as an entry in `inputs`.

      With `output_behavior` set to `update_existing`, the dream writes its result into this memory store. Otherwise the dream doesn't change it.

      - `type: :memory_store`

      - `memory_store_id: String`

        The ID of the memory store for the dream to read (`memstore_...`).

        The memory store must be in the same workspace as the dream and must not be archived.

        minLength: 1

    - `class BetaDreamSessionsInput`

      The sessions that a dream reads, given as an entry in `inputs`.

      - `type: :sessions`

      - `session_ids: Array[String]`

        The IDs of the sessions whose transcripts the dream reads (`sesn_...`).

        Give 1 to 100 IDs, with no duplicates. Each session must be in the same workspace as the dream. Responses list the IDs in sorted order.

        The [limits table in the Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#limits) lists all the limits on a dream.

  - `instructions: String`

    The guidance given when the dream was created, or `null` if none was given.

  - `model: BetaDreamModelConfig`

    The model that runs a dream, from the request that created it.

    The dream uses this model for all of its work. The response always gives the model as an object, even if the request gave only a model ID.

    - `id: String`

      The ID of the model that runs the dream, as given in the request that created it.

      minLength: 1, maxLength: 256

    - `speed: :standard | :fast`

      How fast the model generates output for the dream. Always `standard`.

      - `:standard`

      - `:fast`

  - `output_behavior: BetaOutputBehavior`

    Where the dream writes its result, as set in the request that created the dream. If that request left out `output_behavior`, the dream used the `create_new` behavior.

    - `class BetaOutputBehaviorCreateNew`

      Write the result to a new memory store that starts as a copy of the input memory store. This is the default.

      The new memory store is in the same workspace as the dream. The dream doesn't change the input memory store.

      - `type: :create_new`

    - `class BetaOutputBehaviorUpdateExisting`

      Write the result into the input memory store instead of a new memory store.

      The credential must be allowed to write memory stores, or the request returns a 403 error. While another `update_existing` dream on the same memory store hasn't fully stopped, the request returns a 409 error.

      - `type: :update_existing`

      - `memory_store_id: String`

        The ID of the memory store for the dream to write its result to (`memstore_...`). It must be the memory store in the `memory_store` entry of `inputs`.

        minLength: 1

  - `outputs: Array[BetaDreamOutput]`

    The memory store that holds the dream's result, as a one-item array, or an empty array until the dream records that memory store.

    The array is empty while the dream is `pending` and for a short time after it starts `running`. It can stay empty if the dream fails or is canceled before then. The memory store holds the complete result only once `status` is `completed`.

    See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#use-the-output) for how to review and use the result.

    - `type: :memory_store`

    - `memory_store_id: String`

      The ID of the memory store that the dream writes its result to (`memstore_...`).

      With `output_behavior` set to `create_new`, this is a new memory store. With `update_existing`, it is the input memory store.

  - `session_id: String`

    The ID of the session that runs the dream (`sesn_...`), or `null` if that session hasn't started.

    Stream that session's events to follow what the dream reads and writes.

    See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#watch-the-pipeline-run) for how to watch a running dream.

  - `status: BetaDreamStatus`

    Where a dream is in its lifecycle.

    `completed`, `failed`, and `canceled` are final: once a dream has one of these statuses, its status doesn't change again.

    See the [Dreams guide](https://platform.claude.com/docs/en/managed-agents/dreams#lifecycle) for what each status means.

    - `:pending`

      The dream is waiting to start and hasn't read its inputs yet.

      `outputs` is empty and every `usage` count is zero.

    - `:running`

      The dream is reading its inputs and writing its result.

      `usage` updates while the dream has this status.

    - `:completed`

      The dream finished and its output memory store holds the complete result.

    - `:failed`

      The dream stopped with an error, which `error` describes.

      If `outputs` references a memory store, that memory store keeps what the dream wrote before it stopped.

    - `:canceled`

      A cancel request stopped the dream before it reached `completed` or `failed`.

      If `outputs` references a memory store, that memory store keeps what the dream wrote. `usage` can keep changing after the cancel.

  - `usage: BetaDreamUsage`

    The dream's token counts, which stop changing once its `status` is `completed` or `failed`. After a cancel, they can keep changing.

    - `cache_creation_input_tokens: Integer`

      The dream's input tokens that were written to the prompt cache, for both the 5-minute and 1-hour cache durations.

      format: int32

    - `cache_read_input_tokens: Integer`

      The dream's input tokens that were read from the prompt cache.

      format: int32

    - `input_tokens: Integer`

      The dream's input tokens that weren't read from or written to the prompt cache.

      format: int32

    - `output_tokens: Integer`

      The tokens that the model generated for the dream.

      format: int32

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_dream = anthropic.beta.dreams.archive("dream_id")

puts(beta_dream)
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

`beta.tunnels.create(**kwargs) -> BetaTunnel`

**POST** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

#### Parameters

- `display_name: String`

  Optional human-readable name for the tunnel (1-255 characters).

  minLength: 1, maxLength: 255

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaTunnel`

  An MCP tunnel.

  - `type: :tunnel`

  - `id: String`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the tunnel was archived. Null if it is not archived.

    format: date-time

  - `created_at: Time`

    RFC 3339 datetime string indicating when the tunnel was created.

    format: date-time

  - `display_name: String`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: String`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel = anthropic.beta.tunnels.create

puts(beta_tunnel)
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

`beta.tunnels.retrieve(tunnel_id, **kwargs) -> BetaTunnel`

**GET** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

#### Parameters

- `tunnel_id: String`

  ID of the tunnel (`tnl_...`).

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaTunnel`

  An MCP tunnel.

  - `type: :tunnel`

  - `id: String`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the tunnel was archived. Null if it is not archived.

    format: date-time

  - `created_at: Time`

    RFC 3339 datetime string indicating when the tunnel was created.

    format: date-time

  - `display_name: String`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: String`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel = anthropic.beta.tunnels.retrieve("tunnel_id")

puts(beta_tunnel)
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

`beta.tunnels.list(**kwargs) -> PageCursor<BetaTunnel>`

**GET** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

#### Parameters

- `include_archived: bool`

  Whether to include archived tunnels in the results. Defaults to false.

- `limit: Integer`

  Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

  format: int32

- `page: String`

  Opaque pagination cursor from a previous `list_tunnels` response.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaTunnel`

  An MCP tunnel.

  - `type: :tunnel`

  - `id: String`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the tunnel was archived. Null if it is not archived.

    format: date-time

  - `created_at: Time`

    RFC 3339 datetime string indicating when the tunnel was created.

    format: date-time

  - `display_name: String`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: String`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.tunnels.list

puts(page)
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

`beta.tunnels.archive(tunnel_id, **kwargs) -> BetaTunnel`

**POST** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

#### Parameters

- `tunnel_id: String`

  ID of the tunnel (`tnl_...`).

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaTunnel`

  An MCP tunnel.

  - `type: :tunnel`

  - `id: String`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the tunnel was archived. Null if it is not archived.

    format: date-time

  - `created_at: Time`

    RFC 3339 datetime string indicating when the tunnel was created.

    format: date-time

  - `display_name: String`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: String`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel = anthropic.beta.tunnels.archive("tunnel_id")

puts(beta_tunnel)
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

`beta.tunnels.reveal_token(tunnel_id, **kwargs) -> BetaTunnelToken`

**POST** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

#### Parameters

- `tunnel_id: String`

  ID of the tunnel (`tnl_...`).

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaTunnelToken`

  A tunnel's connector token.

  - `type: :tunnel_token`

  - `id: String`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: String`

    The connector token used to run the tunnel. Treat as a credential.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel_token = anthropic.beta.tunnels.reveal_token("tunnel_id")

puts(beta_tunnel_token)
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

`beta.tunnels.rotate_token(tunnel_id, **kwargs) -> BetaTunnelToken`

**POST** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

#### Parameters

- `tunnel_id: String`

  ID of the tunnel (`tnl_...`).

- `reason: String`

  Optional free-text reason for the rotation, recorded for audit.

  maxLength: 1024

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaTunnelToken`

  A tunnel's connector token.

  - `type: :tunnel_token`

  - `id: String`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: String`

    The connector token used to run the tunnel. Treat as a credential.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel_token = anthropic.beta.tunnels.rotate_token("tunnel_id")

puts(beta_tunnel_token)
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

`beta.tunnels.certificates.create(tunnel_id, **kwargs) -> BetaTunnelCertificate`

**POST** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

#### Parameters

- `tunnel_id: String`

  ID of the tunnel (`tnl_...`).

- `ca_certificate_pem: String`

  PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

  maxLength: 8192

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `type: :tunnel_certificate`

  - `id: String`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the certificate was archived. Null if it is still in the trusted set.

    format: date-time

  - `created_at: Time`

    RFC 3339 datetime string indicating when the certificate was registered.

    format: date-time

  - `expires_at: Time`

    RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire.

    format: date-time

  - `fingerprint: String`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: String`

    ID of the tunnel the certificate is registered against.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel_certificate = anthropic.beta.tunnels.certificates.create("tunnel_id", ca_certificate_pem: "ca_certificate_pem")

puts(beta_tunnel_certificate)
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

`beta.tunnels.certificates.retrieve(certificate_id, **kwargs) -> BetaTunnelCertificate`

**GET** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

#### Parameters

- `tunnel_id: String`

  ID of the tunnel (`tnl_...`).

- `certificate_id: String`

  ID of the certificate (`tcrt_...`).

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `type: :tunnel_certificate`

  - `id: String`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the certificate was archived. Null if it is still in the trusted set.

    format: date-time

  - `created_at: Time`

    RFC 3339 datetime string indicating when the certificate was registered.

    format: date-time

  - `expires_at: Time`

    RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire.

    format: date-time

  - `fingerprint: String`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: String`

    ID of the tunnel the certificate is registered against.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel_certificate = anthropic.beta.tunnels.certificates.retrieve("certificate_id", tunnel_id: "tunnel_id")

puts(beta_tunnel_certificate)
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

`beta.tunnels.certificates.list(tunnel_id, **kwargs) -> PageCursor<BetaTunnelCertificate>`

**GET** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

#### Parameters

- `tunnel_id: String`

  ID of the tunnel (`tnl_...`).

- `include_archived: bool`

  Whether to include archived certificates in the results. Defaults to false.

- `limit: Integer`

  Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

  format: int32

- `page: String`

  Opaque pagination cursor from a previous `list_tunnel_certificates` response.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `type: :tunnel_certificate`

  - `id: String`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the certificate was archived. Null if it is still in the trusted set.

    format: date-time

  - `created_at: Time`

    RFC 3339 datetime string indicating when the certificate was registered.

    format: date-time

  - `expires_at: Time`

    RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire.

    format: date-time

  - `fingerprint: String`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: String`

    ID of the tunnel the certificate is registered against.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.tunnels.certificates.list("tunnel_id")

puts(page)
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

`beta.tunnels.certificates.archive(certificate_id, **kwargs) -> BetaTunnelCertificate`

**POST** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

#### Parameters

- `tunnel_id: String`

  ID of the tunnel (`tnl_...`).

- `certificate_id: String`

  ID of the certificate to archive (`tcrt_...`).

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

- `workspace_id: String`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `type: :tunnel_certificate`

  - `id: String`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the certificate was archived. Null if it is still in the trusted set.

    format: date-time

  - `created_at: Time`

    RFC 3339 datetime string indicating when the certificate was registered.

    format: date-time

  - `expires_at: Time`

    RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire.

    format: date-time

  - `fingerprint: String`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: String`

    ID of the tunnel the certificate is registered against.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel_certificate = anthropic.beta.tunnels.certificates.archive("certificate_id", tunnel_id: "tunnel_id")

puts(beta_tunnel_certificate)
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

`beta.organization.retrieve() -> BetaOrganization`

**GET** `/v1/organizations/me`

Retrieve information about the organization associated with the authenticated API key.

#### Returns

- `class BetaOrganization`

  - `type: :organization`

    Object type.

    For Organizations, this is always `"organization"`.

  - `id: String`

    ID of the Organization.

    format: uuid

  - `name: String`

    Name of the Organization.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_organization = anthropic.beta.organization.retrieve

puts(beta_organization)
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

`beta.organization.api_keys.list(**kwargs) -> Page<BetaAPIKey>`

**GET** `/v1/organizations/api_keys`

List API Keys

#### Parameters

- `after_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `created_by_user_id: String`

  Filter by the ID of the User who created the object.

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `status: :active | :archived | :expired | :inactive`

  Filter by API key status.

  - `:active`

  - `:archived`

  - `:expired`

  - `:inactive`

- `workspace_id: String`

  Filter by Workspace ID.

#### Returns

- `class BetaAPIKey`

  - `type: :api_key`

    Object type.

    For API Keys, this is always `"api_key"`.

  - `id: String`

    ID of the API key.

  - `created_at: Time`

    RFC 3339 datetime string indicating when the API Key was created.

    format: date-time

  - `created_by: BetaAPIKeyCreatedBy`

    The ID and type of the actor that created the API key, or `null` when the
    creator is not recorded (legacy, workload-identity-federated, or
    system-created keys).

    - `type: :service_account | :user`

      Type of the actor that created the object.

      - `:service_account`

      - `:user`

    - `id: String`

      ID of the actor that created the object.

  - `expires_at: Time`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

    format: date-time

  - `name: String`

    Name of the API key.

  - `partial_key_hint: String`

    Partially redacted hint for the API key.

  - `principal: BetaAPIKeyUserActor | BetaAPIKeyServiceAccountActor`

    The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

    - `class BetaAPIKeyUserActor`

      - `type: :user_actor`

        Principal type. Always `"user_actor"` for a User.

      - `user_id: String`

        ID of the User the API key acts as.

    - `class BetaAPIKeyServiceAccountActor`

      - `type: :service_account_actor`

        Principal type. Always `"service_account_actor"` for a Service Account.

      - `service_account_id: String`

        ID of the Service Account the API key acts as.

  - `scope: BetaAPIKeyOrganizationScope | BetaAPIKeyWorkspaceScope`

    Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

    - `class BetaAPIKeyOrganizationScope`

      - `type: :organization`

        Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

    - `class BetaAPIKeyWorkspaceScope`

      - `type: :workspace`

        Scope type. Always `"workspace"`: the API key belongs to one Workspace.

      - `workspace_id: String`

        ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.

  - `status: :active | :archived | :expired | :inactive`

    Status of the API key.

    - `:active`

    - `:archived`

    - `:expired`

    - `:inactive`

  - `workspace_id: String`

    **Deprecated**: Use `scope` instead. `workspace_id` is `null` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

    Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.api_keys.list

puts(page)
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

`beta.organization.api_keys.retrieve(api_key_id) -> BetaAPIKey`

**GET** `/v1/organizations/api_keys/{api_key_id}`

Retrieve information about a single API key in your organization, looked up by its ID. This Admin API endpoint requires an Admin API key, is intended for programmatic key management, and never returns the key's secret value. To view or create your own API keys, go to [API keys](https://platform.claude.com/settings/keys) in the Claude Console.

#### Parameters

- `api_key_id: String`

  ID of the API key.

#### Returns

- `class BetaAPIKey`

  - `type: :api_key`

    Object type.

    For API Keys, this is always `"api_key"`.

  - `id: String`

    ID of the API key.

  - `created_at: Time`

    RFC 3339 datetime string indicating when the API Key was created.

    format: date-time

  - `created_by: BetaAPIKeyCreatedBy`

    The ID and type of the actor that created the API key, or `null` when the
    creator is not recorded (legacy, workload-identity-federated, or
    system-created keys).

    - `type: :service_account | :user`

      Type of the actor that created the object.

      - `:service_account`

      - `:user`

    - `id: String`

      ID of the actor that created the object.

  - `expires_at: Time`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

    format: date-time

  - `name: String`

    Name of the API key.

  - `partial_key_hint: String`

    Partially redacted hint for the API key.

  - `principal: BetaAPIKeyUserActor | BetaAPIKeyServiceAccountActor`

    The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

    - `class BetaAPIKeyUserActor`

      - `type: :user_actor`

        Principal type. Always `"user_actor"` for a User.

      - `user_id: String`

        ID of the User the API key acts as.

    - `class BetaAPIKeyServiceAccountActor`

      - `type: :service_account_actor`

        Principal type. Always `"service_account_actor"` for a Service Account.

      - `service_account_id: String`

        ID of the Service Account the API key acts as.

  - `scope: BetaAPIKeyOrganizationScope | BetaAPIKeyWorkspaceScope`

    Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

    - `class BetaAPIKeyOrganizationScope`

      - `type: :organization`

        Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

    - `class BetaAPIKeyWorkspaceScope`

      - `type: :workspace`

        Scope type. Always `"workspace"`: the API key belongs to one Workspace.

      - `workspace_id: String`

        ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.

  - `status: :active | :archived | :expired | :inactive`

    Status of the API key.

    - `:active`

    - `:archived`

    - `:expired`

    - `:inactive`

  - `workspace_id: String`

    **Deprecated**: Use `scope` instead. `workspace_id` is `null` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

    Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_api_key = anthropic.beta.organization.api_keys.retrieve("api_key_id")

puts(beta_api_key)
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

`beta.organization.api_keys.update(api_key_id, **kwargs) -> BetaAPIKey`

**POST** `/v1/organizations/api_keys/{api_key_id}`

Update API Key

#### Parameters

- `api_key_id: String`

  ID of the API key.

- `name: String`

  Name of the API key.

  minLength: 1, maxLength: 500

- `status: :active | :archived | :inactive`

  Status of the API key.

  - `:active`

  - `:archived`

  - `:inactive`

#### Returns

- `class BetaAPIKey`

  - `type: :api_key`

    Object type.

    For API Keys, this is always `"api_key"`.

  - `id: String`

    ID of the API key.

  - `created_at: Time`

    RFC 3339 datetime string indicating when the API Key was created.

    format: date-time

  - `created_by: BetaAPIKeyCreatedBy`

    The ID and type of the actor that created the API key, or `null` when the
    creator is not recorded (legacy, workload-identity-federated, or
    system-created keys).

    - `type: :service_account | :user`

      Type of the actor that created the object.

      - `:service_account`

      - `:user`

    - `id: String`

      ID of the actor that created the object.

  - `expires_at: Time`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

    format: date-time

  - `name: String`

    Name of the API key.

  - `partial_key_hint: String`

    Partially redacted hint for the API key.

  - `principal: BetaAPIKeyUserActor | BetaAPIKeyServiceAccountActor`

    The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

    - `class BetaAPIKeyUserActor`

      - `type: :user_actor`

        Principal type. Always `"user_actor"` for a User.

      - `user_id: String`

        ID of the User the API key acts as.

    - `class BetaAPIKeyServiceAccountActor`

      - `type: :service_account_actor`

        Principal type. Always `"service_account_actor"` for a Service Account.

      - `service_account_id: String`

        ID of the Service Account the API key acts as.

  - `scope: BetaAPIKeyOrganizationScope | BetaAPIKeyWorkspaceScope`

    Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

    - `class BetaAPIKeyOrganizationScope`

      - `type: :organization`

        Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

    - `class BetaAPIKeyWorkspaceScope`

      - `type: :workspace`

        Scope type. Always `"workspace"`: the API key belongs to one Workspace.

      - `workspace_id: String`

        ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.

  - `status: :active | :archived | :expired | :inactive`

    Status of the API key.

    - `:active`

    - `:archived`

    - `:expired`

    - `:inactive`

  - `workspace_id: String`

    **Deprecated**: Use `scope` instead. `workspace_id` is `null` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

    Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_api_key = anthropic.beta.organization.api_keys.update("api_key_id")

puts(beta_api_key)
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

`beta.organization.external_keys.create(**kwargs) -> BetaExternalKey`

**POST** `/v1/organizations/external_keys`

Create an external key config owned by the caller's organization.

#### Parameters

- `provider_config: BetaAWSExternalKeyConfig | BetaGCPExternalKeyConfig | BetaAzureExternalKeyConfigParam`

  KMS provider identity and auth coordinates.

  - `class BetaAWSExternalKeyConfig`

    - `type: :aws`

    - `kms_arn: String`

      Full ARN of the AWS KMS key. On Claude Platform on AWS the key must be a single-Region key in your organization's own AWS account; cross-account keys, multi-Region keys, and alias ARNs are rejected.

      maxLength: 2048

    - `region: String`

      AWS region. Derived from `kms_arn` if omitted.

    - `role_arn: String`

      **Deprecated**

      IAM role ARN. Deprecated — Anthropic reaches the KMS key through its own intermediate role (or, on Claude Platform on AWS, with credentials AWS issues for the Workspace); this field is ignored.

  - `class BetaGCPExternalKeyConfig`

    - `type: :gcp`

    - `key_name: String`

      Full resource name of the Cloud KMS key.

  - `class BetaAzureExternalKeyConfigParam`

    Azure Key Vault provider configuration.

    - `type: :azure`

    - `key_name: String`

      Name of the key within the vault.

    - `tenant_id: String`

      Azure AD tenant ID.

    - `vault_uri: String`

      Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

    - `client_id: String`

      Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

- `display_name: String`

  Human-friendly display name.

  minLength: 1, maxLength: 255

- `geo: :us`

  Data residency geo. Only `us` is supported.

#### Returns

- `class BetaExternalKey`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `type: :external_key`

  - `id: String`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `attachment: BetaExternalKeyAttachedAttachment | BetaExternalKeyUnattachedAttachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `class BetaExternalKeyAttachedAttachment`

      - `type: :attached`

    - `class BetaExternalKeyUnattachedAttachment`

      - `type: :unattached`

  - `created_at: Time`

    format: date-time

  - `display_name: String`

    Human-friendly display name. Null if none was set.

  - `geo: String`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: BetaAWSExternalKeyConfig | BetaGCPExternalKeyConfig | BetaAzureExternalKeyConfig`

    KMS provider identity and auth coordinates.

    - `class BetaAWSExternalKeyConfig`

      - `type: :aws`

      - `kms_arn: String`

        Full ARN of the AWS KMS key. On Claude Platform on AWS the key must be a single-Region key in your organization's own AWS account; cross-account keys, multi-Region keys, and alias ARNs are rejected.

        maxLength: 2048

      - `region: String`

        AWS region. Derived from `kms_arn` if omitted.

      - `role_arn: String`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key through its own intermediate role (or, on Claude Platform on AWS, with credentials AWS issues for the Workspace); this field is ignored.

    - `class BetaGCPExternalKeyConfig`

      - `type: :gcp`

      - `key_name: String`

        Full resource name of the Cloud KMS key.

    - `class BetaAzureExternalKeyConfig`

      - `type: :azure`

      - `key_name: String`

        Name of the key within the vault.

      - `tenant_id: String`

        Azure AD tenant ID.

      - `vault_uri: String`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `client_id: String`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `updated_at: Time`

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_external_key = anthropic.beta.organization.external_keys.create(
  provider_config: {kms_arn: "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222", type: :aws}
)

puts(beta_external_key)
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

`beta.organization.external_keys.list(**kwargs) -> PageCursor<BetaExternalKey>`

**GET** `/v1/organizations/external_keys`

List external key configs in the caller's organization.

Results are ordered by creation time (newest first). Use the
`next_page` cursor from the response to fetch subsequent pages.

#### Parameters

- `limit: Integer`

  Number of results per page.

  minimum: 1, maximum: 100

- `page: String`

  Opaque cursor from a previous response's `next_page`.

#### Returns

- `class BetaExternalKey`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `type: :external_key`

  - `id: String`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `attachment: BetaExternalKeyAttachedAttachment | BetaExternalKeyUnattachedAttachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `class BetaExternalKeyAttachedAttachment`

      - `type: :attached`

    - `class BetaExternalKeyUnattachedAttachment`

      - `type: :unattached`

  - `created_at: Time`

    format: date-time

  - `display_name: String`

    Human-friendly display name. Null if none was set.

  - `geo: String`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: BetaAWSExternalKeyConfig | BetaGCPExternalKeyConfig | BetaAzureExternalKeyConfig`

    KMS provider identity and auth coordinates.

    - `class BetaAWSExternalKeyConfig`

      - `type: :aws`

      - `kms_arn: String`

        Full ARN of the AWS KMS key. On Claude Platform on AWS the key must be a single-Region key in your organization's own AWS account; cross-account keys, multi-Region keys, and alias ARNs are rejected.

        maxLength: 2048

      - `region: String`

        AWS region. Derived from `kms_arn` if omitted.

      - `role_arn: String`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key through its own intermediate role (or, on Claude Platform on AWS, with credentials AWS issues for the Workspace); this field is ignored.

    - `class BetaGCPExternalKeyConfig`

      - `type: :gcp`

      - `key_name: String`

        Full resource name of the Cloud KMS key.

    - `class BetaAzureExternalKeyConfig`

      - `type: :azure`

      - `key_name: String`

        Name of the key within the vault.

      - `tenant_id: String`

        Azure AD tenant ID.

      - `vault_uri: String`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `client_id: String`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `updated_at: Time`

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.external_keys.list

puts(page)
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

`beta.organization.external_keys.retrieve(external_key_id) -> BetaExternalKey`

**GET** `/v1/organizations/external_keys/{external_key_id}`

Retrieve a single external key config in the caller's organization by ID.

#### Parameters

- `external_key_id: String`

  ID of the External Key.

  maxLength: 2048

#### Returns

- `class BetaExternalKey`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `type: :external_key`

  - `id: String`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `attachment: BetaExternalKeyAttachedAttachment | BetaExternalKeyUnattachedAttachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `class BetaExternalKeyAttachedAttachment`

      - `type: :attached`

    - `class BetaExternalKeyUnattachedAttachment`

      - `type: :unattached`

  - `created_at: Time`

    format: date-time

  - `display_name: String`

    Human-friendly display name. Null if none was set.

  - `geo: String`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: BetaAWSExternalKeyConfig | BetaGCPExternalKeyConfig | BetaAzureExternalKeyConfig`

    KMS provider identity and auth coordinates.

    - `class BetaAWSExternalKeyConfig`

      - `type: :aws`

      - `kms_arn: String`

        Full ARN of the AWS KMS key. On Claude Platform on AWS the key must be a single-Region key in your organization's own AWS account; cross-account keys, multi-Region keys, and alias ARNs are rejected.

        maxLength: 2048

      - `region: String`

        AWS region. Derived from `kms_arn` if omitted.

      - `role_arn: String`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key through its own intermediate role (or, on Claude Platform on AWS, with credentials AWS issues for the Workspace); this field is ignored.

    - `class BetaGCPExternalKeyConfig`

      - `type: :gcp`

      - `key_name: String`

        Full resource name of the Cloud KMS key.

    - `class BetaAzureExternalKeyConfig`

      - `type: :azure`

      - `key_name: String`

        Name of the key within the vault.

      - `tenant_id: String`

        Azure AD tenant ID.

      - `vault_uri: String`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `client_id: String`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `updated_at: Time`

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_external_key = anthropic.beta.organization.external_keys.retrieve("external_key_id")

puts(beta_external_key)
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

`beta.organization.external_keys.update(external_key_id, **kwargs) -> BetaExternalKey`

**POST** `/v1/organizations/external_keys/{external_key_id}`

Partially update an external key config. Omitted fields are left unchanged.

`display_name` is always editable. `geo` and `provider_config` cannot
be changed once any workspace references this config, because previously
encrypted data requires the original key identity to decrypt.

#### Parameters

- `external_key_id: String`

  ID of the External Key.

  maxLength: 2048

- `display_name: String`

  Human-friendly display name.

  minLength: 1, maxLength: 255

- `geo: :us`

  Data residency geo. Only `us` is supported.

- `provider_config: BetaAWSExternalKeyConfig | BetaGCPExternalKeyConfig | BetaAzureExternalKeyConfigParam`

  KMS provider identity and auth coordinates.

  - `class BetaAWSExternalKeyConfig`

    - `type: :aws`

    - `kms_arn: String`

      Full ARN of the AWS KMS key. On Claude Platform on AWS the key must be a single-Region key in your organization's own AWS account; cross-account keys, multi-Region keys, and alias ARNs are rejected.

      maxLength: 2048

    - `region: String`

      AWS region. Derived from `kms_arn` if omitted.

    - `role_arn: String`

      **Deprecated**

      IAM role ARN. Deprecated — Anthropic reaches the KMS key through its own intermediate role (or, on Claude Platform on AWS, with credentials AWS issues for the Workspace); this field is ignored.

  - `class BetaGCPExternalKeyConfig`

    - `type: :gcp`

    - `key_name: String`

      Full resource name of the Cloud KMS key.

  - `class BetaAzureExternalKeyConfigParam`

    Azure Key Vault provider configuration.

    - `type: :azure`

    - `key_name: String`

      Name of the key within the vault.

    - `tenant_id: String`

      Azure AD tenant ID.

    - `vault_uri: String`

      Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

    - `client_id: String`

      Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

#### Returns

- `class BetaExternalKey`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `type: :external_key`

  - `id: String`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `attachment: BetaExternalKeyAttachedAttachment | BetaExternalKeyUnattachedAttachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `class BetaExternalKeyAttachedAttachment`

      - `type: :attached`

    - `class BetaExternalKeyUnattachedAttachment`

      - `type: :unattached`

  - `created_at: Time`

    format: date-time

  - `display_name: String`

    Human-friendly display name. Null if none was set.

  - `geo: String`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: BetaAWSExternalKeyConfig | BetaGCPExternalKeyConfig | BetaAzureExternalKeyConfig`

    KMS provider identity and auth coordinates.

    - `class BetaAWSExternalKeyConfig`

      - `type: :aws`

      - `kms_arn: String`

        Full ARN of the AWS KMS key. On Claude Platform on AWS the key must be a single-Region key in your organization's own AWS account; cross-account keys, multi-Region keys, and alias ARNs are rejected.

        maxLength: 2048

      - `region: String`

        AWS region. Derived from `kms_arn` if omitted.

      - `role_arn: String`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key through its own intermediate role (or, on Claude Platform on AWS, with credentials AWS issues for the Workspace); this field is ignored.

    - `class BetaGCPExternalKeyConfig`

      - `type: :gcp`

      - `key_name: String`

        Full resource name of the Cloud KMS key.

    - `class BetaAzureExternalKeyConfig`

      - `type: :azure`

      - `key_name: String`

        Name of the key within the vault.

      - `tenant_id: String`

        Azure AD tenant ID.

      - `vault_uri: String`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `client_id: String`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `updated_at: Time`

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_external_key = anthropic.beta.organization.external_keys.update("external_key_id")

puts(beta_external_key)
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

`beta.organization.external_keys.delete(external_key_id) -> ExternalKeyDeleteResponse`

**DELETE** `/v1/organizations/external_keys/{external_key_id}`

Delete an external key config.

The request is rejected if any workspace still references this config.

#### Parameters

- `external_key_id: String`

  ID of the External Key.

  maxLength: 2048

#### Returns

- `class ExternalKeyDeleteResponse`

  - `type: :external_key_deleted`

  - `id: String`

    ID of the deleted External Key.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

external_key = anthropic.beta.organization.external_keys.delete("external_key_id")

puts(external_key)
```

##### Response (200)

```json
{
  "id": "ekey_01AbCdEfGhIjKlMnOpQrStUv",
  "type": "external_key_deleted"
}
```

### Validate External Key

`beta.organization.external_keys.validate(external_key_id) -> ExternalKeyValidateResponse`

**POST** `/v1/organizations/external_keys/{external_key_id}/validate`

Validate an external key config against the customer's KMS.

Anthropic performs an encrypt/decrypt roundtrip against the configured
KMS key and waits up to 30 seconds for the result. The response status is
`success` if the roundtrip succeeded, or `failure` with an error
message if it failed or timed out.

#### Parameters

- `external_key_id: String`

  ID of the External Key.

  maxLength: 2048

#### Returns

- `class ExternalKeyValidateResponse`

  Result of a validation roundtrip against the customer's KMS.

  HTTP 200 for both outcomes — the operation completed; `status` says
  whether the key works.

  - `type: :external_key_validation`

  - `error: String`

    Error message when status is `failure`. Null otherwise.

  - `status: :failure | :success`

    `success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

    - `:failure`

    - `:success`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

response = anthropic.beta.organization.external_keys.validate("external_key_id")

puts(response)
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

`beta.organization.federation.issuers.create(**kwargs) -> BetaFederationIssuer`

**POST** `/v1/organizations/federation_issuers`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

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

- `issuer_url: String`

  The `iss` claim value to match against.

  minLength: 1

- `name: String`

  Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  minLength: 1, maxLength: 255

- `check_jti: bool`

  Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Defaults to true. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

- `jwks: BetaJWKSDiscovery | BetaJWKSExplicitURL | BetaJWKSInline`

  How signing keys are obtained. Defaults to OIDC discovery.

  - `class BetaJWKSDiscovery`

    JWKS via the issuer's OIDC discovery document.

    - `type: :discovery`

    - `ca_cert_pem: String`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      maxLength: 8192

    - `discovery_base: String`

      Set when the discovery URL differs from `issuer_url`.

  - `class BetaJWKSExplicitURL`

    JWKS fetched from a fixed endpoint.

    - `type: :explicit_url`

    - `url: String`

      JWKS endpoint.

      minLength: 1

    - `ca_cert_pem: String`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      maxLength: 8192

  - `class BetaJWKSInline`

    JWKS supplied directly; no network fetch.

    - `type: :inline`

    - `keys: Array[Hash[Symbol, untyped]]`

      Inline JWK objects.

      minItems: 1

- `max_jwt_lifetime_seconds: Integer`

  Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Defaults to 3600 (1h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  minimum: 1, maximum: 176400

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaFederationIssuer`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `type: :federation_issuer`

  - `id: String`

    Tagged ID of the federation issuer.

  - `archived_at: Time`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: bool`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: Time`

    When this issuer was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: String`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: BetaJWKSDiscovery | BetaJWKSExplicitURL | BetaJWKSInline`

    How signing keys are obtained for signature verification.

    - `class BetaJWKSDiscovery`

      JWKS via the issuer's OIDC discovery document.

      - `type: :discovery`

      - `ca_cert_pem: String`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: String`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJWKSExplicitURL`

      JWKS fetched from a fixed endpoint.

      - `type: :explicit_url`

      - `url: String`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: String`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJWKSInline`

      JWKS supplied directly; no network fetch.

      - `type: :inline`

      - `keys: Array[Hash[Symbol, untyped]]`

        Inline JWK objects.

        minItems: 1

  - `jwks_polling_disabled_at: Time`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: Integer`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: String`

    Admin-chosen slug identifier.

  - `poll_status: BetaFederationIssuerPollStatus`

    Live state of Anthropic's JWKS polling for this issuer. Populated on both single-issuer retrieval and list responses, including archived issuers. Typically null for inline-key issuers (no polling), or when poll status is temporarily unavailable or polling has not started yet.

    - `consecutive_failures: Integer`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: Time`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: Time`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `updated_at: Time`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_federation_issuer = anthropic.beta.organization.federation.issuers.create(issuer_url: "x", name: "x")

puts(beta_federation_issuer)
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

`beta.organization.federation.issuers.list(**kwargs) -> PageCursor<BetaFederationIssuer>`

**GET** `/v1/organizations/federation_issuers`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

List federation issuers in your organization.

Archived issuers are excluded unless `include_archived=true`.

#### Parameters

- `include_archived: bool`

  Include archived resources. Defaults to false.

- `limit: Integer`

  Number of results per page.

  minimum: 1, maximum: 100

- `page: String`

  Opaque cursor from a previous response's `next_page`.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaFederationIssuer`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `type: :federation_issuer`

  - `id: String`

    Tagged ID of the federation issuer.

  - `archived_at: Time`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: bool`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: Time`

    When this issuer was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: String`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: BetaJWKSDiscovery | BetaJWKSExplicitURL | BetaJWKSInline`

    How signing keys are obtained for signature verification.

    - `class BetaJWKSDiscovery`

      JWKS via the issuer's OIDC discovery document.

      - `type: :discovery`

      - `ca_cert_pem: String`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: String`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJWKSExplicitURL`

      JWKS fetched from a fixed endpoint.

      - `type: :explicit_url`

      - `url: String`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: String`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJWKSInline`

      JWKS supplied directly; no network fetch.

      - `type: :inline`

      - `keys: Array[Hash[Symbol, untyped]]`

        Inline JWK objects.

        minItems: 1

  - `jwks_polling_disabled_at: Time`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: Integer`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: String`

    Admin-chosen slug identifier.

  - `poll_status: BetaFederationIssuerPollStatus`

    Live state of Anthropic's JWKS polling for this issuer. Populated on both single-issuer retrieval and list responses, including archived issuers. Typically null for inline-key issuers (no polling), or when poll status is temporarily unavailable or polling has not started yet.

    - `consecutive_failures: Integer`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: Time`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: Time`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `updated_at: Time`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.federation.issuers.list

puts(page)
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

`beta.organization.federation.issuers.retrieve(federation_issuer_id, **kwargs) -> BetaFederationIssuer`

**GET** `/v1/organizations/federation_issuers/{federation_issuer_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Retrieve a federation issuer by its ID (`fdis_...`).

#### Parameters

- `federation_issuer_id: String`

  ID of the federation issuer.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaFederationIssuer`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `type: :federation_issuer`

  - `id: String`

    Tagged ID of the federation issuer.

  - `archived_at: Time`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: bool`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: Time`

    When this issuer was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: String`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: BetaJWKSDiscovery | BetaJWKSExplicitURL | BetaJWKSInline`

    How signing keys are obtained for signature verification.

    - `class BetaJWKSDiscovery`

      JWKS via the issuer's OIDC discovery document.

      - `type: :discovery`

      - `ca_cert_pem: String`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: String`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJWKSExplicitURL`

      JWKS fetched from a fixed endpoint.

      - `type: :explicit_url`

      - `url: String`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: String`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJWKSInline`

      JWKS supplied directly; no network fetch.

      - `type: :inline`

      - `keys: Array[Hash[Symbol, untyped]]`

        Inline JWK objects.

        minItems: 1

  - `jwks_polling_disabled_at: Time`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: Integer`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: String`

    Admin-chosen slug identifier.

  - `poll_status: BetaFederationIssuerPollStatus`

    Live state of Anthropic's JWKS polling for this issuer. Populated on both single-issuer retrieval and list responses, including archived issuers. Typically null for inline-key issuers (no polling), or when poll status is temporarily unavailable or polling has not started yet.

    - `consecutive_failures: Integer`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: Time`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: Time`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `updated_at: Time`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_federation_issuer = anthropic.beta.organization.federation.issuers.retrieve("federation_issuer_id")

puts(beta_federation_issuer)
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

`beta.organization.federation.issuers.update(federation_issuer_id, **kwargs) -> BetaFederationIssuer`

**POST** `/v1/organizations/federation_issuers/{federation_issuer_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Partially update a federation issuer.

Setting `jwks` replaces the full JWKS shape at once. Archived issuers
cannot be updated; this returns 400. Create a new issuer instead.

Updating an issuer that backs a rule with a scope outside
`workspace:developer` or `workspace:inference` requires a Console
session.

#### Parameters

- `federation_issuer_id: String`

  ID of the federation issuer to update.

- `check_jti: bool`

  Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

- `issuer_url: String`

  Replaces the `iss` claim value to match against. For discovery-mode issuers without a `discovery_base`, this is also the URL Anthropic fetches the OIDC discovery document and signing keys from, so changing it repoints the JWKS source. Changing the issuer URL to a well-known shared platform is rejected while any live rule under this issuer would not constrain tenant identity.

  minLength: 1

- `jwks: BetaJWKSDiscovery | BetaJWKSExplicitURL | BetaJWKSInline`

  Replaces the entire JWKS configuration.

  - `class BetaJWKSDiscovery`

    JWKS via the issuer's OIDC discovery document.

    - `type: :discovery`

    - `ca_cert_pem: String`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      maxLength: 8192

    - `discovery_base: String`

      Set when the discovery URL differs from `issuer_url`.

  - `class BetaJWKSExplicitURL`

    JWKS fetched from a fixed endpoint.

    - `type: :explicit_url`

    - `url: String`

      JWKS endpoint.

      minLength: 1

    - `ca_cert_pem: String`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      maxLength: 8192

  - `class BetaJWKSInline`

    JWKS supplied directly; no network fetch.

    - `type: :inline`

    - `keys: Array[Hash[Symbol, untyped]]`

      Inline JWK objects.

      minItems: 1

- `jwks_polling_disabled: bool`

  Only `false` is accepted, to re-enable polling after the system pauses it. Polling is paused automatically; sending `true` is rejected.

- `max_jwt_lifetime_seconds: Integer`

  Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  minimum: 1, maximum: 176400

- `name: String`

  Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  minLength: 1, maxLength: 255

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaFederationIssuer`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `type: :federation_issuer`

  - `id: String`

    Tagged ID of the federation issuer.

  - `archived_at: Time`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: bool`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: Time`

    When this issuer was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: String`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: BetaJWKSDiscovery | BetaJWKSExplicitURL | BetaJWKSInline`

    How signing keys are obtained for signature verification.

    - `class BetaJWKSDiscovery`

      JWKS via the issuer's OIDC discovery document.

      - `type: :discovery`

      - `ca_cert_pem: String`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: String`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJWKSExplicitURL`

      JWKS fetched from a fixed endpoint.

      - `type: :explicit_url`

      - `url: String`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: String`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJWKSInline`

      JWKS supplied directly; no network fetch.

      - `type: :inline`

      - `keys: Array[Hash[Symbol, untyped]]`

        Inline JWK objects.

        minItems: 1

  - `jwks_polling_disabled_at: Time`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: Integer`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: String`

    Admin-chosen slug identifier.

  - `poll_status: BetaFederationIssuerPollStatus`

    Live state of Anthropic's JWKS polling for this issuer. Populated on both single-issuer retrieval and list responses, including archived issuers. Typically null for inline-key issuers (no polling), or when poll status is temporarily unavailable or polling has not started yet.

    - `consecutive_failures: Integer`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: Time`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: Time`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `updated_at: Time`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_federation_issuer = anthropic.beta.organization.federation.issuers.update("federation_issuer_id")

puts(beta_federation_issuer)
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

`beta.organization.federation.issuers.archive(federation_issuer_id, **kwargs) -> BetaFederationIssuer`

**POST** `/v1/organizations/federation_issuers/{federation_issuer_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Archive a federation issuer.

Idempotent; re-archiving returns the issuer with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still references the issuer; archive those rules first (a rule's
issuer cannot be changed), or recreate them against another issuer.

#### Parameters

- `federation_issuer_id: String`

  ID of the federation issuer to archive.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaFederationIssuer`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `type: :federation_issuer`

  - `id: String`

    Tagged ID of the federation issuer.

  - `archived_at: Time`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: bool`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: Time`

    When this issuer was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: String`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: BetaJWKSDiscovery | BetaJWKSExplicitURL | BetaJWKSInline`

    How signing keys are obtained for signature verification.

    - `class BetaJWKSDiscovery`

      JWKS via the issuer's OIDC discovery document.

      - `type: :discovery`

      - `ca_cert_pem: String`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: String`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJWKSExplicitURL`

      JWKS fetched from a fixed endpoint.

      - `type: :explicit_url`

      - `url: String`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: String`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJWKSInline`

      JWKS supplied directly; no network fetch.

      - `type: :inline`

      - `keys: Array[Hash[Symbol, untyped]]`

        Inline JWK objects.

        minItems: 1

  - `jwks_polling_disabled_at: Time`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: Integer`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: String`

    Admin-chosen slug identifier.

  - `poll_status: BetaFederationIssuerPollStatus`

    Live state of Anthropic's JWKS polling for this issuer. Populated on both single-issuer retrieval and list responses, including archived issuers. Typically null for inline-key issuers (no polling), or when poll status is temporarily unavailable or polling has not started yet.

    - `consecutive_failures: Integer`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: Time`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: Time`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `updated_at: Time`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_federation_issuer = anthropic.beta.organization.federation.issuers.archive("federation_issuer_id")

puts(beta_federation_issuer)
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

`beta.organization.federation.rules.create(**kwargs) -> BetaFederationRule`

**POST** `/v1/organizations/federation_rules`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

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

- `issuer_id: String`

  Tagged ID of the federation issuer.

- `match: BetaFederationRuleMatch`

  Conditions the verified JWT must satisfy for this rule to apply. At least one of `subject_prefix` (other than a wildcard-only value like `*`), `claims`, or `condition` is required; `audience` alone is not sufficient.

  - `audience: String`

    Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

    maxLength: 1024

  - `claims: Hash[Symbol, String]`

    Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

  - `condition: String`

    CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

    maxLength: 4096

  - `subject_prefix: String`

    Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

    maxLength: 1024

- `name: String`

  Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  minLength: 1, maxLength: 255

- `oauth_scope: String`

  Space-separated OAuth scopes. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

  minLength: 1

- `target: BetaServiceAccountTarget`

  Identity that tokens minted via this rule act as. Currently always a `service_account` target.

  - `type: :service_account`

  - `service_account_id: String`

    Tagged ID of the service account to mint tokens for.

  - `service_account_name: String`

    Service account's display name at read time. Ignored on writes.

- `applies_to_all_workspaces: bool`

  When true, enable this rule for every workspace in the org (including workspaces created later).

- `attributes: Hash[Symbol, String]`

  CEL expressions `{name: expr}` extracting named values from claims. Not yet supported; any non-empty value is rejected with 400.

- `description: String`

  Optional free-text description.

  maxLength: 2000

- `token_lifetime_seconds: Integer`

  Lifetime in seconds for access tokens minted via this rule (60-86400). Defaults to 3600 (1h). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  minimum: 60, maximum: 86400

- `workspace_id: String`

  Tagged ID of the workspace to enable this rule for. Required unless `applies_to_all_workspaces` is true. Additional workspaces can be added via the `/federation_rules/{federation_rule_id}/workspaces` sub-resource.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaFederationRule`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `type: :federation_rule`

  - `id: String`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: bool`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: Time`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: Hash[Symbol, String]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: Time`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: String`

    Optional free-text description.

  - `issuer_id: String`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: String`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: String`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: Hash[Symbol, String]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: String`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: String`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: String`

    Admin-chosen slug identifier.

  - `oauth_scope: String`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `type: :service_account`

    - `service_account_id: String`

      Tagged ID of the service account to mint tokens for.

    - `service_account_name: String`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: Integer`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `updated_at: Time`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: String`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: Array[String]`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_federation_rule = anthropic.beta.organization.federation.rules.create(
  issuer_id: "issuer_id",
  match: {},
  name: "x",
  oauth_scope: "x",
  target: {service_account_id: "svac_01SDCCSbTxrXDpWc1phhtcfK", type: :service_account}
)

puts(beta_federation_rule)
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

`beta.organization.federation.rules.list(**kwargs) -> PageCursor<BetaFederationRule>`

**GET** `/v1/organizations/federation_rules`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

List federation rules in your organization.

Optionally filter by issuer with `issuer_id`. Archived rules are excluded
unless `include_archived=true`.

#### Parameters

- `include_archived: bool`

  Include archived resources. Defaults to false.

- `issuer_id: String`

  Filter to rules referencing this federation issuer.

- `limit: Integer`

  Number of results per page.

  minimum: 1, maximum: 100

- `page: String`

  Opaque cursor from a previous response's `next_page`.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaFederationRule`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `type: :federation_rule`

  - `id: String`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: bool`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: Time`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: Hash[Symbol, String]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: Time`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: String`

    Optional free-text description.

  - `issuer_id: String`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: String`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: String`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: Hash[Symbol, String]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: String`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: String`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: String`

    Admin-chosen slug identifier.

  - `oauth_scope: String`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `type: :service_account`

    - `service_account_id: String`

      Tagged ID of the service account to mint tokens for.

    - `service_account_name: String`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: Integer`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `updated_at: Time`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: String`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: Array[String]`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.federation.rules.list

puts(page)
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

`beta.organization.federation.rules.retrieve(federation_rule_id, **kwargs) -> BetaFederationRule`

**GET** `/v1/organizations/federation_rules/{federation_rule_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Retrieve a federation rule by its ID (`fdrl_...`).

#### Parameters

- `federation_rule_id: String`

  ID of the federation rule.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaFederationRule`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `type: :federation_rule`

  - `id: String`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: bool`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: Time`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: Hash[Symbol, String]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: Time`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: String`

    Optional free-text description.

  - `issuer_id: String`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: String`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: String`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: Hash[Symbol, String]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: String`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: String`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: String`

    Admin-chosen slug identifier.

  - `oauth_scope: String`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `type: :service_account`

    - `service_account_id: String`

      Tagged ID of the service account to mint tokens for.

    - `service_account_name: String`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: Integer`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `updated_at: Time`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: String`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: Array[String]`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_federation_rule = anthropic.beta.organization.federation.rules.retrieve("federation_rule_id")

puts(beta_federation_rule)
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

`beta.organization.federation.rules.update(federation_rule_id, **kwargs) -> BetaFederationRule`

**POST** `/v1/organizations/federation_rules/{federation_rule_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

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

- `federation_rule_id: String`

  ID of the federation rule to update.

- `applies_to_all_workspaces: bool`

  When true, enables this rule for every workspace in the org (including workspaces created later). Setting `false` is rejected with 400 if no workspace would remain enabled; a rule with only a legacy `workspace_id` binding continues to mint.

- `attributes: Hash[Symbol, String]`

  Replaces the CEL expressions `{name: expr}` extracting named values from claims. Send null to clear them. Not yet supported; any non-empty value is rejected with 400.

- `description: String`

  Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

  maxLength: 2000

- `match: BetaFederationRuleMatch`

  Replaces the entire match object. All populated matcher fields must pass.

  - `audience: String`

    Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

    maxLength: 1024

  - `claims: Hash[Symbol, String]`

    Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

  - `condition: String`

    CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

    maxLength: 4096

  - `subject_prefix: String`

    Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

    maxLength: 1024

- `name: String`

  Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  minLength: 1, maxLength: 255

- `oauth_scope: String`

  Replaces the space-separated OAuth scopes granted on minted tokens. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

  minLength: 1

- `target: BetaServiceAccountTarget`

  Replaces the entire target object. Currently always a `service_account` target.

  - `type: :service_account`

  - `service_account_id: String`

    Tagged ID of the service account to mint tokens for.

  - `service_account_name: String`

    Service account's display name at read time. Ignored on writes.

- `token_lifetime_seconds: Integer`

  Replaces the lifetime in seconds for access tokens minted via this rule (60-86400). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  minimum: 60, maximum: 86400

- `workspace_id: String`

  Replaces the existing single workspace enablement (the previous one is removed). Rejected with 400 if the rule is enabled for more than one workspace; use the `/federation_rules/{federation_rule_id}/workspaces` sub-resource instead.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaFederationRule`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `type: :federation_rule`

  - `id: String`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: bool`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: Time`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: Hash[Symbol, String]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: Time`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: String`

    Optional free-text description.

  - `issuer_id: String`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: String`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: String`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: Hash[Symbol, String]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: String`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: String`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: String`

    Admin-chosen slug identifier.

  - `oauth_scope: String`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `type: :service_account`

    - `service_account_id: String`

      Tagged ID of the service account to mint tokens for.

    - `service_account_name: String`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: Integer`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `updated_at: Time`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: String`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: Array[String]`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_federation_rule = anthropic.beta.organization.federation.rules.update("federation_rule_id")

puts(beta_federation_rule)
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

`beta.organization.federation.rules.archive(federation_rule_id, **kwargs) -> BetaFederationRule`

**POST** `/v1/organizations/federation_rules/{federation_rule_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Archive a federation rule.

Token exchange through this rule stops immediately. Idempotent;
re-archiving returns the rule with its original `archived_at`. Archiving
clears the rule's workspace targeting (`workspace_id` and
`workspace_ids` are emptied). Tokens already minted before archive
remain valid until they expire. OAuth callers may only manage rules
whose `oauth_scope` is `workspace:developer` or `workspace:inference`;
other scopes require a Console session.

#### Parameters

- `federation_rule_id: String`

  ID of the federation rule to archive.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaFederationRule`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `type: :federation_rule`

  - `id: String`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: bool`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: Time`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: Hash[Symbol, String]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: Time`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: String`

    Optional free-text description.

  - `issuer_id: String`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: String`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: String`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: Hash[Symbol, String]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: String`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: String`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: String`

    Admin-chosen slug identifier.

  - `oauth_scope: String`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `type: :service_account`

    - `service_account_id: String`

      Tagged ID of the service account to mint tokens for.

    - `service_account_name: String`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: Integer`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `updated_at: Time`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: String`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: Array[String]`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_federation_rule = anthropic.beta.organization.federation.rules.archive("federation_rule_id")

puts(beta_federation_rule)
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

`beta.organization.federation.rules.workspaces.add(federation_rule_id, **kwargs) -> BetaFederationRuleWorkspace`

**POST** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

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

- `federation_rule_id: String`

  ID of the federation rule.

- `workspace_id: String`

  Tagged ID of the workspace to enable this rule for.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaFederationRuleWorkspace`

  - `type: :federation_rule_workspace`

  - `created_at: Time`

    When this workspace was enabled for the rule.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `federation_rule_id: String`

    Tagged ID of the federation rule.

  - `workspace_id: String`

    Tagged ID of the workspace this rule is enabled for.

  - `workspace_name: String`

    Workspace display name. Populated when listing; null in the enable response.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_federation_rule_workspace = anthropic.beta.organization.federation.rules.workspaces.add(
  "federation_rule_id",
  workspace_id: "workspace_id"
)

puts(beta_federation_rule_workspace)
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

`beta.organization.federation.rules.workspaces.list(federation_rule_id, **kwargs) -> PageCursor<BetaFederationRuleWorkspace>`

**GET** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

List workspaces where this federation rule is enabled.

Returns all workspace enablements in a single response; the `limit` and
`page` parameters are accepted but have no effect, and `next_page` is
always `null`. Returns explicit per-workspace enablements only; for
rules with `applies_to_all_workspaces` or a legacy single
`workspace_id`, check those fields on the rule itself.

#### Parameters

- `federation_rule_id: String`

  ID of the federation rule.

- `limit: Integer`

  Number of results per page.

  minimum: 1, maximum: 100

- `page: String`

  Opaque cursor from a previous response's `next_page`.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaFederationRuleWorkspace`

  - `type: :federation_rule_workspace`

  - `created_at: Time`

    When this workspace was enabled for the rule.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `federation_rule_id: String`

    Tagged ID of the federation rule.

  - `workspace_id: String`

    Tagged ID of the workspace this rule is enabled for.

  - `workspace_name: String`

    Workspace display name. Populated when listing; null in the enable response.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.federation.rules.workspaces.list("federation_rule_id")

puts(page)
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

`beta.organization.federation.rules.workspaces.remove(workspace_id, **kwargs) -> WorkspaceRemoveResponse`

**DELETE** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Disable a federation rule for a workspace.

Idempotent; succeeds even if the enablement was already removed. OAuth
callers may only manage rules whose `oauth_scope` is
`workspace:developer` or `workspace:inference`; other scopes require a
Console session.

#### Parameters

- `federation_rule_id: String`

  ID of the federation rule.

- `workspace_id: String`

  ID of the workspace to disable for.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class WorkspaceRemoveResponse`

  - `type: :federation_rule_workspace_deleted`

  - `federation_rule_id: String`

    Tagged ID of the federation rule.

  - `workspace_id: String`

    Tagged ID of the workspace named in the delete request. Removal is idempotent.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

workspace = anthropic.beta.organization.federation.rules.workspaces.remove(
  "workspace_id",
  federation_rule_id: "federation_rule_id"
)

puts(workspace)
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

`beta.organization.invites.create(**kwargs) -> BetaOrganizationInvite`

**POST** `/v1/organizations/invites`

Invite a user to join the organization by email.

On plans that draw members from a finite pool of purchased seats, the invite automatically consumes a seat from the lowest tier with availability; there is no seat-tier parameter. When no seat is free the request fails with a 400 error rather than purchasing a seat.

#### Parameters

- `email: String`

  Email of the User.

  format: email

- `role: :billing | :claude_code_user | :developer | 2 more`

  Role for the invited User.

  The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

  - `:billing`

  - `:claude_code_user`

  - `:developer`

  - `:managed`

  - `:user`

- `rbac_group_ids: Array[String]`

  RBAC group IDs to assign to the User when the Invite is accepted. A non-empty array is accepted only for a Claude Enterprise organization with RBAC groups, and requires the key to carry the `write:rbac_groups` scope.

  maxItems: 100

#### Returns

- `class BetaOrganizationInvite`

  - `type: :invite`

    Object type.

    For Invites, this is always `"invite"`.

  - `id: String`

    ID of the Invite.

  - `accepted_at: Time`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `email: String`

    Email of the User being invited.

  - `expires_at: Time`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `invited_at: Time`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `rbac_group_ids: Array[String]`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `:admin`

    - `:billing`

    - `:claude_code_user`

    - `:developer`

    - `:managed`

    - `:membership_admin`

    - `:owner`

    - `:primary_owner`

    - `:user`

  - `status: :accepted | :deleted | :expired | :pending`

    Status of the Invite.

    - `:accepted`

    - `:deleted`

    - `:expired`

    - `:pending`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_organization_invite = anthropic.beta.organization.invites.create(email: "user@emaildomain.com", role: :user)

puts(beta_organization_invite)
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

`beta.organization.invites.list(**kwargs) -> Page<BetaOrganizationInvite>`

**GET** `/v1/organizations/invites`

List the organization's invites.

#### Parameters

- `after_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `email: String`

  Filter by the email address the Invite was sent to. Matches the same way as the Users list's `email` filter (normalized, case-insensitive).

  format: email

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `roles: Array[String]`

  Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

  Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

- `statuses: Array[:accepted | :expired | :pending]`

  Filter by Invite status. Repeatable; values are OR'ed together. Omit to return `pending`, `accepted`, and `expired` Invites alike.

  - `:accepted`

  - `:expired`

  - `:pending`

#### Returns

- `class BetaOrganizationInvite`

  - `type: :invite`

    Object type.

    For Invites, this is always `"invite"`.

  - `id: String`

    ID of the Invite.

  - `accepted_at: Time`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `email: String`

    Email of the User being invited.

  - `expires_at: Time`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `invited_at: Time`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `rbac_group_ids: Array[String]`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `:admin`

    - `:billing`

    - `:claude_code_user`

    - `:developer`

    - `:managed`

    - `:membership_admin`

    - `:owner`

    - `:primary_owner`

    - `:user`

  - `status: :accepted | :deleted | :expired | :pending`

    Status of the Invite.

    - `:accepted`

    - `:deleted`

    - `:expired`

    - `:pending`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.invites.list

puts(page)
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

`beta.organization.invites.retrieve(invite_id) -> BetaOrganizationInvite`

**GET** `/v1/organizations/invites/{invite_id}`

Retrieve an invite by ID.

#### Parameters

- `invite_id: String`

  ID of the Invite.

#### Returns

- `class BetaOrganizationInvite`

  - `type: :invite`

    Object type.

    For Invites, this is always `"invite"`.

  - `id: String`

    ID of the Invite.

  - `accepted_at: Time`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `email: String`

    Email of the User being invited.

  - `expires_at: Time`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `invited_at: Time`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `rbac_group_ids: Array[String]`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `:admin`

    - `:billing`

    - `:claude_code_user`

    - `:developer`

    - `:managed`

    - `:membership_admin`

    - `:owner`

    - `:primary_owner`

    - `:user`

  - `status: :accepted | :deleted | :expired | :pending`

    Status of the Invite.

    - `:accepted`

    - `:deleted`

    - `:expired`

    - `:pending`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_organization_invite = anthropic.beta.organization.invites.retrieve("invite_id")

puts(beta_organization_invite)
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

`beta.organization.invites.delete(invite_id) -> InviteDeleteResponse`

**DELETE** `/v1/organizations/invites/{invite_id}`

Delete a pending invite.

#### Parameters

- `invite_id: String`

  ID of the Invite.

#### Returns

- `class InviteDeleteResponse`

  - `type: :invite_deleted`

    Deleted object type.

    For Invites, this is always `"invite_deleted"`.

  - `id: String`

    ID of the Invite.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

invite = anthropic.beta.organization.invites.delete("invite_id")

puts(invite)
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

`beta.organization.service_accounts.create(**kwargs) -> BetaServiceAccount`

**POST** `/v1/organizations/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Create a service account.

A service account is a named workload identity that federation rules
target. `organization_role` is `developer` (default) or `admin`; a rule
may only be created or retargeted to grant `org:admin` scope when the
target's `organization_role` is `admin`. Creating an `admin`-role service
account requires an interactive credential (a user OAuth token or a
Console session) — a workload may only create `developer`-role service
accounts.

#### Parameters

- `name: String`

  Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  minLength: 1, maxLength: 255

- `description: String`

  Optional free-text description.

  maxLength: 2000

- `organization_role: :admin | :developer`

  Org-level role. Defaults to `developer`.

  - `:admin`

  - `:developer`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaServiceAccount`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: :service_account`

  - `id: String`

    Tagged ID of the service account.

  - `archived_at: Time`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: Time`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: String`

    Optional free-text description.

  - `name: String`

    Admin-chosen slug identifier.

  - `organization_role: :admin | :developer`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `:admin`

    - `:developer`

  - `updated_at: Time`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_service_account = anthropic.beta.organization.service_accounts.create(name: "ci-deploy-bot")

puts(beta_service_account)
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

`beta.organization.service_accounts.list(**kwargs) -> PageCursor<BetaServiceAccount>`

**GET** `/v1/organizations/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

List service accounts in the caller's organization.

Results are ordered by creation time, newest first. Use `limit` and the
`next_page` cursor to paginate; set `include_archived=true` to include
archived service accounts.

#### Parameters

- `include_archived: bool`

  Include archived resources. Defaults to false.

- `limit: Integer`

  Number of results per page.

  minimum: 1, maximum: 100

- `page: String`

  Opaque cursor from a previous response's `next_page`.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaServiceAccount`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: :service_account`

  - `id: String`

    Tagged ID of the service account.

  - `archived_at: Time`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: Time`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: String`

    Optional free-text description.

  - `name: String`

    Admin-chosen slug identifier.

  - `organization_role: :admin | :developer`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `:admin`

    - `:developer`

  - `updated_at: Time`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.service_accounts.list

puts(page)
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

`beta.organization.service_accounts.retrieve(service_account_id, **kwargs) -> BetaServiceAccount`

**GET** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Retrieve a service account by its ID (`svac_...`).

#### Parameters

- `service_account_id: String`

  ID of the service account.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaServiceAccount`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: :service_account`

  - `id: String`

    Tagged ID of the service account.

  - `archived_at: Time`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: Time`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: String`

    Optional free-text description.

  - `name: String`

    Admin-chosen slug identifier.

  - `organization_role: :admin | :developer`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `:admin`

    - `:developer`

  - `updated_at: Time`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_service_account = anthropic.beta.organization.service_accounts.retrieve("service_account_id")

puts(beta_service_account)
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

`beta.organization.service_accounts.update(service_account_id, **kwargs) -> BetaServiceAccount`

**POST** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Update a service account.

Only `description` and `organization_role` are mutable; `name` cannot be
changed. Archived service accounts cannot be updated; this returns 400.
Setting `organization_role` to `admin` (even when unchanged) requires an
interactive credential (a user OAuth token or a Console session).

#### Parameters

- `service_account_id: String`

  ID of the service account to update.

- `description: String`

  Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

  maxLength: 2000

- `organization_role: :admin | :developer`

  Replaces the org-level role. Omit or send `null` to leave unchanged.

  - `:admin`

  - `:developer`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaServiceAccount`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: :service_account`

  - `id: String`

    Tagged ID of the service account.

  - `archived_at: Time`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: Time`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: String`

    Optional free-text description.

  - `name: String`

    Admin-chosen slug identifier.

  - `organization_role: :admin | :developer`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `:admin`

    - `:developer`

  - `updated_at: Time`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_service_account = anthropic.beta.organization.service_accounts.update("service_account_id")

puts(beta_service_account)
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

`beta.organization.service_accounts.archive(service_account_id, **kwargs) -> BetaServiceAccount`

**POST** `/v1/organizations/service_accounts/{service_account_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Archive a service account.

Idempotent; re-archiving returns the service account with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still targets this service account, same as issuer archival; archive
those rules first or change their target to another service account.

#### Parameters

- `service_account_id: String`

  ID of the service account to archive.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaServiceAccount`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: :service_account`

  - `id: String`

    Tagged ID of the service account.

  - `archived_at: Time`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: Time`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: String`

    Optional free-text description.

  - `name: String`

    Admin-chosen slug identifier.

  - `organization_role: :admin | :developer`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `:admin`

    - `:developer`

  - `updated_at: Time`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_service_account = anthropic.beta.organization.service_accounts.archive("service_account_id")

puts(beta_service_account)
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

`beta.organization.service_accounts.workspaces.add(service_account_id, **kwargs) -> BetaServiceAccountWorkspaceMember`

**POST** `/v1/organizations/service_accounts/{service_account_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Add a service account to a workspace with the given `workspace_role`.

Mirror of `POST /workspaces/{workspace_id}/service_accounts`, addressed
from the service-account side; both create the same membership. If the
service account is already an explicit member of the workspace, its
`workspace_role` is replaced with the value supplied here. Archived
workspaces return 400. Archived service accounts cannot be added and are
rejected.

#### Parameters

- `service_account_id: String`

  ID of the service account.

- `workspace_id: String`

  Tagged workspace ID to add the service account to.

- `workspace_role: BetaNoBillingWorkspaceRole`

  Role to assign to the service account in this workspace.

  - `:workspace_admin`

  - `:workspace_developer`

  - `:workspace_restricted_developer`

  - `:workspace_user`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaServiceAccountWorkspaceMember`

  - `type: :service_account_workspace_member`

  - `created_by_actor_id: String`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: bool`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: String`

    Tagged service account ID (`svac_...`).

  - `workspace_id: String`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_service_account_workspace_member = anthropic.beta.organization.service_accounts.workspaces.add(
  "service_account_id",
  workspace_id: "workspace_id",
  workspace_role: :workspace_admin
)

puts(beta_service_account_workspace_member)
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

`beta.organization.service_accounts.workspaces.list(service_account_id, **kwargs) -> PageCursor<BetaServiceAccountWorkspaceMember>`

**GET** `/v1/organizations/service_accounts/{service_account_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

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

- `service_account_id: String`

  ID of the service account.

- `limit: Integer`

  Number of results per page.

  minimum: 1, maximum: 100

- `page: String`

  Opaque cursor from a previous response's `next_page`.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaServiceAccountWorkspaceMember`

  - `type: :service_account_workspace_member`

  - `created_by_actor_id: String`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: bool`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: String`

    Tagged service account ID (`svac_...`).

  - `workspace_id: String`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.service_accounts.workspaces.list("service_account_id")

puts(page)
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

`beta.organization.service_accounts.workspaces.remove(workspace_id, **kwargs) -> WorkspaceRemoveResponse`

**DELETE** `/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Remove a service account from a workspace.

Mirror of `DELETE /workspaces/{workspace_id}/service_accounts/{service_account_id}`,
addressed from the service-account side. Removal is idempotent (returns
200 even if the membership was already removed). A DELETE against the
implicit default-workspace membership returns 200 but is a no-op and the
membership persists; deleting an explicit default-workspace row reverts
to the implicit `workspace_user` membership. Archived workspaces return
400.

#### Parameters

- `service_account_id: String`

  ID of the service account.

- `workspace_id: String`

  ID of the workspace.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class WorkspaceRemoveResponse`

  - `type: :service_account_workspace_member_deleted`

  - `service_account_id: String`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `workspace_id: String`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

workspace = anthropic.beta.organization.service_accounts.workspaces.remove(
  "workspace_id",
  service_account_id: "service_account_id"
)

puts(workspace)
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

`beta.organization.users.list(**kwargs) -> Page<BetaOrganizationUser>`

**GET** `/v1/organizations/users`

List the organization's members.

#### Parameters

- `after_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `email: String`

  Filter by user email.

  format: email

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `roles: Array[String]`

  Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

  Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

#### Returns

- `class BetaOrganizationUser`

  - `type: :user`

    Object type.

    For Users, this is always `"user"`.

  - `id: String`

    ID of the User.

  - `added_at: Time`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: String`

    Email of the User.

  - `name: String`

    Name of the User.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `:admin`

    - `:billing`

    - `:claude_code_user`

    - `:developer`

    - `:managed`

    - `:membership_admin`

    - `:owner`

    - `:primary_owner`

    - `:user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.users.list

puts(page)
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

`beta.organization.users.retrieve(user_id) -> BetaOrganizationUser`

**GET** `/v1/organizations/users/{user_id}`

Retrieve a member of the organization by user ID.

#### Parameters

- `user_id: String`

  ID of the User.

#### Returns

- `class BetaOrganizationUser`

  - `type: :user`

    Object type.

    For Users, this is always `"user"`.

  - `id: String`

    ID of the User.

  - `added_at: Time`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: String`

    Email of the User.

  - `name: String`

    Name of the User.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `:admin`

    - `:billing`

    - `:claude_code_user`

    - `:developer`

    - `:managed`

    - `:membership_admin`

    - `:owner`

    - `:primary_owner`

    - `:user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_organization_user = anthropic.beta.organization.users.retrieve("user_id")

puts(beta_organization_user)
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

`beta.organization.users.update(user_id, **kwargs) -> BetaOrganizationUser`

**POST** `/v1/organizations/users/{user_id}`

Update a member's organization role.

#### Parameters

- `user_id: String`

  ID of the User.

- `role: :billing | :claude_code_user | :developer | 2 more`

  New role for the User.

  The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

  - `:billing`

  - `:claude_code_user`

  - `:developer`

  - `:managed`

  - `:user`

#### Returns

- `class BetaOrganizationUser`

  - `type: :user`

    Object type.

    For Users, this is always `"user"`.

  - `id: String`

    ID of the User.

  - `added_at: Time`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: String`

    Email of the User.

  - `name: String`

    Name of the User.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `:admin`

    - `:billing`

    - `:claude_code_user`

    - `:developer`

    - `:managed`

    - `:membership_admin`

    - `:owner`

    - `:primary_owner`

    - `:user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_organization_user = anthropic.beta.organization.users.update("user_id", role: :user)

puts(beta_organization_user)
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

`beta.organization.users.remove(user_id) -> UserRemoveResponse`

**DELETE** `/v1/organizations/users/{user_id}`

Remove a member from the organization.

#### Parameters

- `user_id: String`

  ID of the User.

#### Returns

- `class UserRemoveResponse`

  - `type: :user_deleted`

    Deleted object type.

    For Users, this is always `"user_deleted"`.

  - `id: String`

    ID of the User.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

user = anthropic.beta.organization.users.remove("user_id")

puts(user)
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

`beta.organization.workspaces.list(**kwargs) -> Page<BetaWorkspace>`

**GET** `/v1/organizations/workspaces`

List Workspaces

#### Parameters

- `after_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `include_archived: bool`

  Whether to include Workspaces that have been archived in the response

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

#### Returns

- `class BetaWorkspace`

  - `type: :workspace`

    Object type.

    For Workspaces, this is always `"workspace"`.

  - `id: String`

    ID of the Workspace.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: String`

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

  - `created_at: Time`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: Array[BetaAllowedInferenceGeo] | :unrestricted`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = Array[BetaAllowedInferenceGeo]`

        - `:global`

        - `:us`

      - `:unrestricted`

    - `default_inference_geo: :global | :us`

      Default inference geo applied when requests omit the parameter.

      - `:global`

      - `:us`

    - `workspace_geo: :us`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: String`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: String`

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

  - `name: String`

    Name of the Workspace.

  - `tags: Hash[Symbol, String]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.workspaces.list

puts(page)
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
        "default_inference_geo": "global",
        "workspace_geo": "us"
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

`beta.organization.workspaces.create(**kwargs) -> BetaWorkspace`

**POST** `/v1/organizations/workspaces`

Create Workspace

#### Parameters

- `name: String`

  Name of the Workspace.

  minLength: 1, maxLength: 40

- `data_residency: BetaDataResidencyCreateConfig`

  Data residency configuration for the workspace. If omitted, defaults to `workspace_geo: "us"`, `allowed_inference_geos: "unrestricted"`, and `default_inference_geo: "global"`.

  - `allowed_inference_geos: Array[BetaAllowedInferenceGeo] | :unrestricted`

    Permitted inference geo values. Defaults to 'unrestricted' if omitted, which allows all geos. Use the string 'unrestricted' to allow all geos, or a list of specific geos.

    - `Geos = Array[BetaAllowedInferenceGeo]`

      - `:global`

      - `:us`

    - `:unrestricted`

  - `default_inference_geo: :global | :us`

    Default inference geo applied when requests omit the parameter. Defaults to 'global' if omitted. Must be a member of `allowed_inference_geos` unless `allowed_inference_geos` is `"unrestricted"`.

    - `:global`

    - `:us`

  - `workspace_geo: :us`

    Geographic region for workspace data storage. Immutable after creation. Defaults to 'us' if omitted.

- `display_color: String`

  Hex color code representing the Workspace in the Anthropic Console.

  maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

- `external_key_id: String`

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

- `tags: Hash[Symbol, String]`

  User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaWorkspace`

  - `type: :workspace`

    Object type.

    For Workspaces, this is always `"workspace"`.

  - `id: String`

    ID of the Workspace.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: String`

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

  - `created_at: Time`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: Array[BetaAllowedInferenceGeo] | :unrestricted`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = Array[BetaAllowedInferenceGeo]`

        - `:global`

        - `:us`

      - `:unrestricted`

    - `default_inference_geo: :global | :us`

      Default inference geo applied when requests omit the parameter.

      - `:global`

      - `:us`

    - `workspace_geo: :us`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: String`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: String`

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

  - `name: String`

    Name of the Workspace.

  - `tags: Hash[Symbol, String]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_workspace = anthropic.beta.organization.workspaces.create(name: "x")

puts(beta_workspace)
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
    "default_inference_geo": "global",
    "workspace_geo": "us"
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

`beta.organization.workspaces.retrieve(workspace_id) -> BetaWorkspace`

**GET** `/v1/organizations/workspaces/{workspace_id}`

Get Workspace

#### Parameters

- `workspace_id: String`

  ID of the Workspace.

#### Returns

- `class BetaWorkspace`

  - `type: :workspace`

    Object type.

    For Workspaces, this is always `"workspace"`.

  - `id: String`

    ID of the Workspace.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: String`

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

  - `created_at: Time`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: Array[BetaAllowedInferenceGeo] | :unrestricted`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = Array[BetaAllowedInferenceGeo]`

        - `:global`

        - `:us`

      - `:unrestricted`

    - `default_inference_geo: :global | :us`

      Default inference geo applied when requests omit the parameter.

      - `:global`

      - `:us`

    - `workspace_geo: :us`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: String`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: String`

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

  - `name: String`

    Name of the Workspace.

  - `tags: Hash[Symbol, String]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_workspace = anthropic.beta.organization.workspaces.retrieve("workspace_id")

puts(beta_workspace)
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
    "default_inference_geo": "global",
    "workspace_geo": "us"
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

`beta.organization.workspaces.update(workspace_id, **kwargs) -> BetaWorkspace`

**POST** `/v1/organizations/workspaces/{workspace_id}`

Update Workspace

#### Parameters

- `workspace_id: String`

- `data_residency: BetaDataResidencyUpdateConfig`

  Data residency configuration for the workspace.

  - `allowed_inference_geos: Array[BetaAllowedInferenceGeo] | :unrestricted`

    Permitted inference geo values. Use 'unrestricted' to allow all geos, or a list of specific geos.

    - `Geos = Array[BetaAllowedInferenceGeo]`

      - `:global`

      - `:us`

    - `:unrestricted`

  - `default_inference_geo: :global | :us`

    Default inference geo applied when requests omit the parameter. Must be a member of `allowed_inference_geos` unless `allowed_inference_geos` is `"unrestricted"`.

    - `:global`

    - `:us`

- `display_color: String`

  Hex color code representing the Workspace in the Anthropic Console.

  maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

- `external_key_id: String`

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

- `name: String`

  Name of the Workspace.

  minLength: 1, maxLength: 40

- `tags: Hash[Symbol, String]`

  User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Returns

- `class BetaWorkspace`

  - `type: :workspace`

    Object type.

    For Workspaces, this is always `"workspace"`.

  - `id: String`

    ID of the Workspace.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: String`

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

  - `created_at: Time`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: Array[BetaAllowedInferenceGeo] | :unrestricted`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = Array[BetaAllowedInferenceGeo]`

        - `:global`

        - `:us`

      - `:unrestricted`

    - `default_inference_geo: :global | :us`

      Default inference geo applied when requests omit the parameter.

      - `:global`

      - `:us`

    - `workspace_geo: :us`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: String`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: String`

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

  - `name: String`

    Name of the Workspace.

  - `tags: Hash[Symbol, String]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_workspace = anthropic.beta.organization.workspaces.update("workspace_id")

puts(beta_workspace)
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
    "default_inference_geo": "global",
    "workspace_geo": "us"
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

`beta.organization.workspaces.archive(workspace_id) -> BetaWorkspace`

**POST** `/v1/organizations/workspaces/{workspace_id}/archive`

Archive Workspace

#### Parameters

- `workspace_id: String`

#### Returns

- `class BetaWorkspace`

  - `type: :workspace`

    Object type.

    For Workspaces, this is always `"workspace"`.

  - `id: String`

    ID of the Workspace.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: String`

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

  - `created_at: Time`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: Array[BetaAllowedInferenceGeo] | :unrestricted`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = Array[BetaAllowedInferenceGeo]`

        - `:global`

        - `:us`

      - `:unrestricted`

    - `default_inference_geo: :global | :us`

      Default inference geo applied when requests omit the parameter.

      - `:global`

      - `:us`

    - `workspace_geo: :us`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: String`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: String`

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

  - `name: String`

    Name of the Workspace.

  - `tags: Hash[Symbol, String]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_workspace = anthropic.beta.organization.workspaces.archive("workspace_id")

puts(beta_workspace)
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
    "default_inference_geo": "global",
    "workspace_geo": "us"
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

`beta.organization.workspaces.rate_limits.list(workspace_id, **kwargs) -> PageCursor<BetaWorkspaceRateLimit>`

**GET** `/v1/organizations/workspaces/{workspace_id}/rate_limits`

List a workspace's rate limits.

By default, returns only the groups and limiter types that have a
workspace-level override. With `include_inherited=true`, returns every
group with organization-level limits the workspace can see, listing for
each the values it inherits from the organization as well as its own
overrides. Each value's `source` says which it is.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `workspace_id: String`

  The ID of the workspace.

- `group_type: :batch | :files | :model_group | 3 more`

  Filter by group type.

  - `:batch`

  - `:files`

  - `:model_group`

  - `:skills`

  - `:token_count`

  - `:web_search`

- `include_inherited: bool`

  Also list the limiter values the workspace inherits from the organization, including groups with no workspace-level override.

- `limit: Integer`

  Maximum number of items to return per page. Ranges from `1` to `1000`.

  When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

  minimum: 1, maximum: 1000

- `page: String`

  Opaque cursor from a previous response's `next_page`.

#### Returns

- `class BetaWorkspaceRateLimit`

  - `type: :workspace_rate_limit`

    Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

  - `group: BetaOrganizationRateLimitModelGroup | BetaOrganizationRateLimitBatchGroup | BetaOrganizationRateLimitTokenCountGroup | 3 more`

    The rate-limit group this entry's limits apply to. Its `type` equals `group_type`.

    - `class BetaOrganizationRateLimitModelGroup`

      - `type: :model_group`

        Always `model_group`: a family of models.

      - `id: String`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

      - `display_name: String`

        Human-readable name of the model group (for example, `Claude Sonnet 4.x`). For display only; it may change.

    - `class BetaOrganizationRateLimitBatchGroup`

      - `type: :batch`

        Always `batch`: the Message Batches API.

      - `id: String`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `class BetaOrganizationRateLimitTokenCountGroup`

      - `type: :token_count`

        Always `token_count`: the Token Count API.

      - `id: String`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `class BetaOrganizationRateLimitFilesGroup`

      - `type: :files`

        Always `files`: the Files API.

      - `id: String`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `class BetaOrganizationRateLimitSkillsGroup`

      - `type: :skills`

        Always `skills`: the Skills API.

      - `id: String`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `class BetaOrganizationRateLimitWebSearchGroup`

      - `type: :web_search`

        Always `web_search`: the Messages API web search tool.

      - `id: String`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

  - `limits: Array[BetaWorkspaceRateLimitValue]`

    The workspace's limiter values for this group. By default only the limiter types with a workspace-level override are listed. With `include_inherited` set to `true`, the limiter types the workspace inherits from the organization are listed too, each marked by `source`.

    - `type: String`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `org_limit: Integer`

      The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

    - `source: BetaWorkspaceRateLimitWorkspaceSource | BetaWorkspaceRateLimitOrganizationSource`

      Where `value` comes from. `organization` values are listed only when `include_inherited` is `true`, and then `value` equals `org_limit`.

      - `class BetaWorkspaceRateLimitWorkspaceSource`

        - `type: :workspace`

          Always `workspace`: a workspace-level override is stored.

      - `class BetaWorkspaceRateLimitOrganizationSource`

        - `type: :organization`

          Always `organization`: no workspace-level override is stored, so the organization's value applies.

    - `value: Integer`

      The workspace's value for this limiter type: the workspace-level override when `source.type` is `workspace`, otherwise the organization's value.

  - `models: Array[String]`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `rate_limit_id: String`

    The `id` of the organization's RateLimit entry this entry applies to.

  - `workspace_id: String`

    ID of the Workspace this entry applies to.

  - `group_type: :batch | :files | :model_group | 3 more`

    **Deprecated**: Use `group.type` instead. `group_type` is still returned and always equals `group.type`.

    Deprecated: use `group.type` instead. The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`. Always equal to `group.type`.

    - `:batch`

    - `:files`

    - `:model_group`

    - `:skills`

    - `:token_count`

    - `:web_search`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.workspaces.rate_limits.list("workspace_id")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "group": {
        "id": "id",
        "display_name": "display_name",
        "type": "model_group"
      },
      "group_type": "batch",
      "limits": [
        {
          "org_limit": 0,
          "source": {
            "type": "workspace"
          },
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

`beta.organization.workspaces.members.list(workspace_id, **kwargs) -> Page<BetaWorkspaceMember>`

**GET** `/v1/organizations/workspaces/{workspace_id}/members`

List Workspace Members

#### Parameters

- `workspace_id: String`

  ID of the Workspace.

- `after_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

#### Returns

- `class BetaWorkspaceMember`

  - `type: :workspace_member`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `user_id: String`

    ID of the User.

  - `workspace_id: String`

    ID of the Workspace.

  - `workspace_role: BetaWorkspaceRole`

    Role of the Workspace Member.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.workspaces.members.list("workspace_id")

puts(page)
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

`beta.organization.workspaces.members.add(workspace_id, **kwargs) -> BetaWorkspaceMember`

**POST** `/v1/organizations/workspaces/{workspace_id}/members`

Create Workspace Member

#### Parameters

- `workspace_id: String`

  ID of the Workspace.

- `user_id: String`

  ID of the User.

- `workspace_role: BetaNoBillingWorkspaceRole`

  Role of the new Workspace Member. Cannot be `workspace_billing`.

  - `:workspace_admin`

  - `:workspace_developer`

  - `:workspace_restricted_developer`

  - `:workspace_user`

#### Returns

- `class BetaWorkspaceMember`

  - `type: :workspace_member`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `user_id: String`

    ID of the User.

  - `workspace_id: String`

    ID of the Workspace.

  - `workspace_role: BetaWorkspaceRole`

    Role of the Workspace Member.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_workspace_member = anthropic.beta.organization.workspaces.members.add(
  "workspace_id",
  user_id: "user_01WCz1FkmYMm4gnmykNKUu3Q",
  workspace_role: :workspace_admin
)

puts(beta_workspace_member)
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

`beta.organization.workspaces.members.retrieve(user_id, **kwargs) -> BetaWorkspaceMember`

**GET** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Get Workspace Member

#### Parameters

- `workspace_id: String`

  ID of the Workspace.

- `user_id: String`

  ID of the User.

#### Returns

- `class BetaWorkspaceMember`

  - `type: :workspace_member`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `user_id: String`

    ID of the User.

  - `workspace_id: String`

    ID of the Workspace.

  - `workspace_role: BetaWorkspaceRole`

    Role of the Workspace Member.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_workspace_member = anthropic.beta.organization.workspaces.members.retrieve("user_id", workspace_id: "workspace_id")

puts(beta_workspace_member)
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

`beta.organization.workspaces.members.update(user_id, **kwargs) -> BetaWorkspaceMember`

**POST** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Update Workspace Member

#### Parameters

- `workspace_id: String`

  ID of the Workspace.

- `user_id: String`

  ID of the User.

- `workspace_role: BetaWorkspaceRole`

  New workspace role for the User.

  - `:workspace_admin`

  - `:workspace_billing`

  - `:workspace_developer`

  - `:workspace_restricted_developer`

  - `:workspace_user`

#### Returns

- `class BetaWorkspaceMember`

  - `type: :workspace_member`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `user_id: String`

    ID of the User.

  - `workspace_id: String`

    ID of the Workspace.

  - `workspace_role: BetaWorkspaceRole`

    Role of the Workspace Member.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_workspace_member = anthropic.beta.organization.workspaces.members.update(
  "user_id",
  workspace_id: "workspace_id",
  workspace_role: :workspace_admin
)

puts(beta_workspace_member)
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

`beta.organization.workspaces.members.remove(user_id, **kwargs) -> MemberRemoveResponse`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Delete Workspace Member

#### Parameters

- `workspace_id: String`

  ID of the Workspace.

- `user_id: String`

  ID of the User.

#### Returns

- `class MemberRemoveResponse`

  - `type: :workspace_member_deleted`

    Deleted object type.

    For Workspace Members, this is always `"workspace_member_deleted"`.

  - `user_id: String`

    ID of the User.

  - `workspace_id: String`

    ID of the Workspace.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

member = anthropic.beta.organization.workspaces.members.remove("user_id", workspace_id: "workspace_id")

puts(member)
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

`beta.organization.workspaces.service_accounts.list(workspace_id, **kwargs) -> PageCursor<BetaServiceAccountWorkspaceMember>`

**GET** `/v1/organizations/workspaces/{workspace_id}/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

List the service accounts that are members of a workspace.

Each entry includes the service account's `workspace_role`. Use `limit`
and the `next_page` cursor to paginate. Archived workspaces return 400;
use `GET /service_accounts/{id}/workspaces` to audit memberships of an
archived workspace. The implicit default-workspace membership is not
included in this list. Memberships of archived service accounts are
omitted from the results.

#### Parameters

- `workspace_id: String`

  ID of the workspace.

- `limit: Integer`

  Number of results per page.

  minimum: 1, maximum: 100

- `page: String`

  Opaque cursor from a previous response's `next_page`.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaServiceAccountWorkspaceMember`

  - `type: :service_account_workspace_member`

  - `created_by_actor_id: String`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: bool`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: String`

    Tagged service account ID (`svac_...`).

  - `workspace_id: String`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.workspaces.service_accounts.list("workspace_id")

puts(page)
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

`beta.organization.workspaces.service_accounts.add(workspace_id, **kwargs) -> BetaServiceAccountWorkspaceMember`

**POST** `/v1/organizations/workspaces/{workspace_id}/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

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

- `workspace_id: String`

  ID of the workspace.

- `service_account_id: String`

  Tagged service account ID to add.

- `workspace_role: BetaNoBillingWorkspaceRole`

  Role to assign to the service account in this workspace.

  - `:workspace_admin`

  - `:workspace_developer`

  - `:workspace_restricted_developer`

  - `:workspace_user`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaServiceAccountWorkspaceMember`

  - `type: :service_account_workspace_member`

  - `created_by_actor_id: String`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: bool`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: String`

    Tagged service account ID (`svac_...`).

  - `workspace_id: String`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_service_account_workspace_member = anthropic.beta.organization.workspaces.service_accounts.add(
  "workspace_id",
  service_account_id: "service_account_id",
  workspace_role: :workspace_admin
)

puts(beta_service_account_workspace_member)
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

`beta.organization.workspaces.service_accounts.retrieve(service_account_id, **kwargs) -> BetaServiceAccountWorkspaceMember`

**GET** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Retrieve a service account's membership in a workspace.

Returns the membership record, including the service account's
`workspace_role` in this workspace. Archived workspaces return 400. For
the default workspace, returns the implicit (`implicit: true`)
membership when no explicit membership exists; an explicitly added
membership is returned with its assigned role. An archived service
account returns 404.

#### Parameters

- `workspace_id: String`

  ID of the workspace.

- `service_account_id: String`

  ID of the service account.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaServiceAccountWorkspaceMember`

  - `type: :service_account_workspace_member`

  - `created_by_actor_id: String`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: bool`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: String`

    Tagged service account ID (`svac_...`).

  - `workspace_id: String`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_service_account_workspace_member = anthropic.beta.organization.workspaces.service_accounts.retrieve(
  "service_account_id",
  workspace_id: "workspace_id"
)

puts(beta_service_account_workspace_member)
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

`beta.organization.workspaces.service_accounts.update(service_account_id, **kwargs) -> BetaServiceAccountWorkspaceMember`

**POST** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Change a service account's role in a workspace.

The new `workspace_role` replaces the current one. Only explicit
memberships can be updated; to set a role on the implicit
default-workspace membership, add the service account explicitly with
`POST /workspaces/{workspace_id}/service_accounts`. Archived workspaces
return 400. Archived service accounts cannot be updated and are
rejected.

#### Parameters

- `workspace_id: String`

  ID of the workspace.

- `service_account_id: String`

  ID of the service account.

- `workspace_role: BetaNoBillingWorkspaceRole`

  New role for the service account in this workspace.

  - `:workspace_admin`

  - `:workspace_developer`

  - `:workspace_restricted_developer`

  - `:workspace_user`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaServiceAccountWorkspaceMember`

  - `type: :service_account_workspace_member`

  - `created_by_actor_id: String`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: bool`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: String`

    Tagged service account ID (`svac_...`).

  - `workspace_id: String`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_service_account_workspace_member = anthropic.beta.organization.workspaces.service_accounts.update(
  "service_account_id",
  workspace_id: "workspace_id",
  workspace_role: :workspace_admin
)

puts(beta_service_account_workspace_member)
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

`beta.organization.workspaces.service_accounts.remove(service_account_id, **kwargs) -> ServiceAccountRemoveResponse`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Remove a service account from a workspace.

Removal is idempotent (returns 200 even if the membership was already
removed). A DELETE against the implicit default-workspace membership
returns 200 but is a no-op and the membership persists; deleting an
explicit default-workspace row reverts to the implicit `workspace_user`
membership. Archived workspaces return 400.

#### Parameters

- `workspace_id: String`

  ID of the workspace.

- `service_account_id: String`

  ID of the service account.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class ServiceAccountRemoveResponse`

  - `type: :service_account_workspace_member_deleted`

  - `service_account_id: String`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `workspace_id: String`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

service_account = anthropic.beta.organization.workspaces.service_accounts.remove(
  "service_account_id",
  workspace_id: "workspace_id"
)

puts(service_account)
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

`beta.organization.rate_limits.list(**kwargs) -> PageCursor<BetaOrganizationRateLimit>`

**GET** `/v1/organizations/rate_limits`

List Messages API rate limits for your organization.

Each entry corresponds to one rate-limit group (either a model family
or an API-surface category such as the Message Batches API or the web
search tool) and contains the set of limiter values that apply to it.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `group_type: :batch | :files | :model_group | 3 more`

  Filter by group type.

  - `:batch`

  - `:files`

  - `:model_group`

  - `:skills`

  - `:token_count`

  - `:web_search`

- `limit: Integer`

  Maximum number of items to return per page. Ranges from `1` to `1000`.

  When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

  minimum: 1, maximum: 1000

- `model: String`

  Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

- `page: String`

  Opaque cursor from a previous response's `next_page`.

#### Returns

- `class BetaOrganizationRateLimit`

  - `type: :rate_limit`

    Object type. Always `rate_limit` for organization rate-limit entries.

  - `id: String`

    Identifier of this rate-limit entry. It is stable within the organization and differs between organizations; the group's own identifier is `group.id`.

  - `group: BetaOrganizationRateLimitModelGroup | BetaOrganizationRateLimitBatchGroup | BetaOrganizationRateLimitTokenCountGroup | 3 more`

    The rate-limit group this entry's limits apply to. Its `type` equals `group_type`.

    - `class BetaOrganizationRateLimitModelGroup`

      - `type: :model_group`

        Always `model_group`: a family of models.

      - `id: String`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

      - `display_name: String`

        Human-readable name of the model group (for example, `Claude Sonnet 4.x`). For display only; it may change.

    - `class BetaOrganizationRateLimitBatchGroup`

      - `type: :batch`

        Always `batch`: the Message Batches API.

      - `id: String`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `class BetaOrganizationRateLimitTokenCountGroup`

      - `type: :token_count`

        Always `token_count`: the Token Count API.

      - `id: String`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `class BetaOrganizationRateLimitFilesGroup`

      - `type: :files`

        Always `files`: the Files API.

      - `id: String`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `class BetaOrganizationRateLimitSkillsGroup`

      - `type: :skills`

        Always `skills`: the Skills API.

      - `id: String`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `class BetaOrganizationRateLimitWebSearchGroup`

      - `type: :web_search`

        Always `web_search`: the Messages API web search tool.

      - `id: String`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

  - `limits: Array[BetaOrganizationRateLimitValue]`

    The limiter values that apply to this group.

    - `type: String`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `value: Integer`

      The configured limit value for this limiter type.

  - `models: Array[String]`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `group_type: :batch | :files | :model_group | 3 more`

    **Deprecated**: Use `group.type` instead. `group_type` is still returned and always equals `group.type`.

    Deprecated: use `group.type` instead. The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`. Always equal to `group.type`.

    - `:batch`

    - `:files`

    - `:model_group`

    - `:skills`

    - `:token_count`

    - `:web_search`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.rate_limits.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "group": {
        "id": "id",
        "display_name": "display_name",
        "type": "model_group"
      },
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

`beta.organization.compliance_settings.retrieve() -> BetaComplianceSettings`

**GET** `/v1/organizations/compliance_settings`

Retrieve your organization's Compliance Settings.

Compliance Settings is a singleton resource: there is exactly one per
organization, addressed without an identifier. The `state` field reflects
whether the Compliance API is enabled. An organization with a parent
organization reads the state inherited from the parent's configuration.

#### Returns

- `class BetaComplianceSettings`

  - `type: :compliance_settings`

  - `state: BetaComplianceSettingsState`

    Whether the Compliance API is enabled for this organization.

    - `class BetaComplianceSettingsStateEnabled`

      - `type: :enabled`

    - `class BetaComplianceSettingsStateDisabled`

      - `type: :disabled`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_compliance_settings = anthropic.beta.organization.compliance_settings.retrieve

puts(beta_compliance_settings)
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

`beta.organization.compliance_settings.update(**kwargs) -> BetaComplianceSettings`

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

- `state: BetaComplianceSettingsStateParam`

  Desired state. Accepts the string shorthand "enabled" or "disabled" in place of the object form; the response always returns the canonical object form.

  - `class BetaComplianceSettingsStateEnabledParam`

    - `type: :enabled`

  - `class BetaComplianceSettingsStateDisabledParam`

    - `type: :disabled`

#### Returns

- `class BetaComplianceSettings`

  - `type: :compliance_settings`

  - `state: BetaComplianceSettingsState`

    Whether the Compliance API is enabled for this organization.

    - `class BetaComplianceSettingsStateEnabled`

      - `type: :enabled`

    - `class BetaComplianceSettingsStateDisabled`

      - `type: :disabled`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_compliance_settings = anthropic.beta.organization.compliance_settings.update(state: {type: :enabled})

puts(beta_compliance_settings)
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

## Beta › Organization › Analytics › Summaries

### Get Activity Summaries

`beta.organization.analytics.summaries.list(**kwargs) -> PageCursor<BetaAnalyticsSingleDayActivitySummary>`

**GET** `/v1/organizations/analytics/summaries`

Get organization-wide activity summaries for a date range.

Returns one entry per day from `starting_date` (inclusive) to `ending_date`
(exclusive) in `data`, the same `data` / `next_page` envelope as the other
analytics list endpoints; the series is currently returned in full, so
`next_page` is always null (`summaries` is a deprecated alias of `data`).
Data is typically available with a 1-day lag and may be revised by a few
percent over the following days: when `ending_date` is omitted it
defaults to the most recent available day + 1, so the last entry covers
the most recent available day. The series can be scoped to an RBAC group
via `filter[]=rbac_group_id:{id}`. Available to organizations on a Claude
Enterprise plan. Requires an API key with the `read:analytics` scope.

#### Parameters

- `starting_date: Date`

  UTC date in YYYY-MM-DD format. Start of the date range (inclusive). Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: Date`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive). Data is typically available with a 1-day lag, so this can be at most today — which is also the default when omitted, making the last entry cover the most recent available day. Data may be revised by a few percent over the following days. The range may span at most 366 days.

  format: date

- `filter: Array[String]`

  Filters as `dimension:value`. Only `rbac_group_id` is supported (e.g. `filter[]=rbac_group_id:{id}`); repeat the param to OR across groups. Scopes the whole day series to members of the matching group(s), re-aggregated from member-level activity — org-wide seat/invite fields and the adoption rates derived from them are null on scoped rows. `rbac_group_id` accepts the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each UTC day (time-of-usage attribution). At most 100 entries.

  maxItems: 100

- `limit: Integer`

  Number of results per page (1-1000, default 100). The day series (at most 366 entries) is currently returned in full in a single page, so `limit` does not yet shorten it.

  minimum: 1, maximum: 1000

- `page: String`

  Opaque cursor from a previous response's `next_page` field. `next_page` is currently always null, so there is never a cursor to send.

#### Returns

- `class BetaAnalyticsSingleDayActivitySummary`

  Per-day entry in the /summaries response.

  - `assigned_seat_count: Integer`

    Number of seats currently assigned to members. Null when the response is scoped to an RBAC group — seat assignment is org-wide and has no per-group analogue.

  - `cowork_daily_active_user_count: Integer`

    Number of users with Cowork activity on the requested day

  - `cowork_monthly_active_user_count: Integer`

    Number of users with Cowork activity in the 30-day rolling window

  - `cowork_weekly_active_user_count: Integer`

    Number of users with Cowork activity in the 7-day rolling window

  - `daily_active_user_count: Integer`

    Number of users with token consumption on the requested day

  - `daily_adoption_rate: Float`

    Percentage of assigned seats with activity on the requested day (`DAU / assigned_seat_count * 100`). Null when the response is scoped to an RBAC group.

  - `ending_at: Time`

    End of the aggregation period (exclusive), UTC midnight in RFC 3339 format (e.g. `2026-01-16T00:00:00Z`).

    format: date-time

  - `monthly_active_user_count: Integer`

    Number of users with token consumption in the 30-day rolling window

  - `monthly_adoption_rate: Float`

    Percentage of assigned seats with activity in the 30-day rolling window (`MAU / assigned_seat_count * 100`). Null when the response is scoped to an RBAC group.

  - `pending_invite_count: Integer`

    Number of pending invitations to join the organization. Null when the response is scoped to an RBAC group.

  - `starting_at: Time`

    Start of the aggregation period (inclusive), UTC midnight in RFC 3339 format (e.g. `2026-01-15T00:00:00Z`).

    format: date-time

  - `weekly_active_user_count: Integer`

    Number of users with token consumption in the 7-day rolling window

  - `weekly_adoption_rate: Float`

    Percentage of assigned seats with activity in the 7-day rolling window (`WAU / assigned_seat_count * 100`). Null when the response is scoped to an RBAC group.

  - `chat_daily_active_user_count: Integer`

    Number of users with claude.ai (chat) activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `chat_monthly_active_user_count: Integer`

    Number of users with claude.ai (chat) activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `chat_weekly_active_user_count: Integer`

    Number of users with claude.ai (chat) activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_code_daily_active_user_count: Integer`

    Number of users with Claude Code activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_code_monthly_active_user_count: Integer`

    Number of users with Claude Code activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_code_weekly_active_user_count: Integer`

    Number of users with Claude Code activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_design_daily_active_user_count: Integer`

    Number of users with Claude Design activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_design_monthly_active_user_count: Integer`

    Number of users with Claude Design activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_design_weekly_active_user_count: Integer`

    Number of users with Claude Design activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `office_agent_daily_active_user_count: Integer`

    Number of users with Claude in Office activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `office_agent_monthly_active_user_count: Integer`

    Number of users with Claude in Office activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `office_agent_weekly_active_user_count: Integer`

    Number of users with Claude in Office activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `science_daily_active_user_count: Integer`

    Number of users with Claude Science activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `science_entitled_user_count: Integer`

    Number of users with a Claude Science seat entitlement (per-seat RBAC) at the time of the daily snapshot. The funnel top; independent of the org-level Claude Science toggle. Null when the response is scoped to an RBAC group — entitlement is org-wide and has no per-group analogue. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `science_monthly_active_user_count: Integer`

    Number of users with Claude Science activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `science_weekly_active_user_count: Integer`

    Number of users with Claude Science activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.analytics.summaries.list(starting_date: "2019-12-27")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "assigned_seat_count": 0,
      "cowork_daily_active_user_count": 0,
      "cowork_monthly_active_user_count": 0,
      "cowork_weekly_active_user_count": 0,
      "daily_active_user_count": 0,
      "daily_adoption_rate": 0,
      "ending_at": "2019-12-27T18:11:19.117Z",
      "monthly_active_user_count": 0,
      "monthly_adoption_rate": 0,
      "pending_invite_count": 0,
      "starting_at": "2019-12-27T18:11:19.117Z",
      "weekly_active_user_count": 0,
      "weekly_adoption_rate": 0,
      "chat_daily_active_user_count": 0,
      "chat_monthly_active_user_count": 0,
      "chat_weekly_active_user_count": 0,
      "claude_code_daily_active_user_count": 0,
      "claude_code_monthly_active_user_count": 0,
      "claude_code_weekly_active_user_count": 0,
      "claude_design_daily_active_user_count": 0,
      "claude_design_monthly_active_user_count": 0,
      "claude_design_weekly_active_user_count": 0,
      "office_agent_daily_active_user_count": 0,
      "office_agent_monthly_active_user_count": 0,
      "office_agent_weekly_active_user_count": 0,
      "science_daily_active_user_count": 0,
      "science_entitled_user_count": 0,
      "science_monthly_active_user_count": 0,
      "science_weekly_active_user_count": 0
    }
  ],
  "next_page": "next_page",
  "summaries": [
    {
      "assigned_seat_count": 0,
      "cowork_daily_active_user_count": 0,
      "cowork_monthly_active_user_count": 0,
      "cowork_weekly_active_user_count": 0,
      "daily_active_user_count": 0,
      "daily_adoption_rate": 0,
      "ending_at": "2019-12-27T18:11:19.117Z",
      "monthly_active_user_count": 0,
      "monthly_adoption_rate": 0,
      "pending_invite_count": 0,
      "starting_at": "2019-12-27T18:11:19.117Z",
      "weekly_active_user_count": 0,
      "weekly_adoption_rate": 0,
      "chat_daily_active_user_count": 0,
      "chat_monthly_active_user_count": 0,
      "chat_weekly_active_user_count": 0,
      "claude_code_daily_active_user_count": 0,
      "claude_code_monthly_active_user_count": 0,
      "claude_code_weekly_active_user_count": 0,
      "claude_design_daily_active_user_count": 0,
      "claude_design_monthly_active_user_count": 0,
      "claude_design_weekly_active_user_count": 0,
      "office_agent_daily_active_user_count": 0,
      "office_agent_monthly_active_user_count": 0,
      "office_agent_weekly_active_user_count": 0,
      "science_daily_active_user_count": 0,
      "science_entitled_user_count": 0,
      "science_monthly_active_user_count": 0,
      "science_weekly_active_user_count": 0
    }
  ]
}
```

## Beta › Organization › Analytics › Users

### List User Activity

`beta.organization.analytics.users.list(**kwargs) -> PageCursor<BetaAnalyticsUserActivity>`

**GET** `/v1/organizations/analytics/users`

Get per-user activity for a given day, with cursor-based pagination.

Returns activity metrics for each user in the organization, sorted by email
address. Use `group_by[]` for per-RBAC-group aggregates, or `filter[]` to
scope results to specific members, groups, or a chat project. Available
to organizations on a Claude Enterprise plan. Requires an API key with
the `read:analytics` scope.

#### Parameters

- `date: Date`

  UTC date in YYYY-MM-DD format. The day to get user activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: Date`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

  format: date

- `filter: Array[String]`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `project_id`, `rbac_group_id`, `user_id`. Value forms: `project_id` takes a tagged project id (`claude_proj_...`) and scopes each member's row to their claude.ai chat activity within that project (it cannot be combined with `group_by[]` or an `rbac_group_id` filter); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

  maxItems: 100

- `group_by: Array[:rbac_group_id]`

  Dimensions to break results out by (e.g. `group_by[]=rbac_group_id`). Supported on this endpoint: `rbac_group_id`. Rows are already per-member, so the one supported grouping aggregates them per RBAC group instead. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

  maxItems: 100

- `limit: Integer`

  Number of results per page (1-1000, default 100).

  minimum: 1, maximum: 1000

- `order: :asc | :desc`

  Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

  - `:asc`

  - `:desc`

- `order_by: String`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: String`

  Opaque cursor from a previous response's `next_page` field.

- `starting_date: Date`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

#### Returns

- `class BetaAnalyticsUserActivity`

  Per-user activity data for a given day.

  - `chat_metrics: BetaAnalyticsChatMetrics`

    Claude.ai activity metrics for a single user on a given day.

    - `connectors_used_count: Integer`

      Number of MCP connector invocations.

    - `distinct_artifacts_created_count: Integer`

      Number of distinct artifacts created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `distinct_connectors_used_count: Integer`

      Distinct claude.ai connectors this user used. Excludes calls whose connector could not be identified and all calls from organizations with zero data retention. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_conversation_count: Integer`

      Number of distinct conversations the user participated in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_files_uploaded_count: Integer`

      Number of distinct files uploaded. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_projects_created_count: Integer`

      Number of distinct projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `distinct_projects_used_count: Integer`

      Number of distinct projects used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_shared_artifacts_viewed_count: Integer`

      Number of distinct shared artifacts the user viewed. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_skills_used_count: Integer`

      Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `message_count: Integer`

      Number of messages sent

    - `shared_conversations_viewed_count: Integer`

      Number of times the user opened a shared conversation in a project

    - `thinking_message_count: Integer`

      Number of messages that used extended thinking

  - `claude_code_metrics: BetaAnalyticsClaudeCodeMetrics`

    Claude Code activity metrics for a single user on a given day.

    - `core_metrics: BetaAnalyticsCoreCodeMetrics`

      Core Claude Code activity metrics for a single user on a given day.

      - `artifacts_created_count: Integer`

        Number of artifacts created in Claude Code sessions: an artifact counts once, on the day a session first saves it. Counted from 2026-08-17; 0 on earlier days. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `commit_count: Integer`

        Number of commits made via Claude Code

      - `distinct_session_count: Integer`

        Number of distinct Claude Code sessions. On aggregated rows and in date-range mode: summed per-day distinct counts. A session essentially never spans a UTC day, so the sum is in practice the true distinct count.

      - `lines_of_code: BetaAnalyticsLinesOfCode`

        Lines of code added and removed via Claude Code.

        - `added_count: Integer`

          Lines of code added

        - `removed_count: Integer`

          Lines of code removed

      - `pull_request_count: Integer`

        Number of pull requests created via Claude Code

    - `tool_actions: BetaAnalyticsToolActions`

      Per-tool accepted/rejected counts for Claude Code file modification tools.

      - `edit_tool: BetaAnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

        - `accepted_count: Integer`

          Number of tool proposals accepted

        - `rejected_count: Integer`

          Number of tool proposals rejected

      - `multi_edit_tool: BetaAnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

      - `notebook_edit_tool: BetaAnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

      - `write_tool: BetaAnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

  - `cowork_metrics: BetaAnalyticsCoworkMetrics`

    Cowork activity metrics for a single user on a given day.

    - `action_count: Integer`

      Number of tool actions completed in Cowork sessions

    - `artifacts_created_count: Integer`

      Number of artifacts created in Cowork sessions: an artifact counts once, on the day a session first saves it. Counted from 2026-08-17; 0 on earlier days. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `connectors_used_count: Integer`

      Total number of connector invocations in Cowork sessions

    - `dispatch_turn_count: Integer`

      Number of Dispatch (background agent) turns completed

    - `distinct_connectors_used_count: Integer`

      Number of distinct connectors used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_session_count: Integer`

      Number of distinct Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_skills_used_count: Integer`

      Number of distinct skills used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `message_count: Integer`

      Number of messages sent in Cowork sessions

    - `skills_used_count: Integer`

      Total number of skill invocations in Cowork sessions

    - `distinct_plugins_used_count: Integer`

      Number of distinct plugins used in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `edit_tool_count: Integer`

      Number of successful Edit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `file_edit_count: Integer`

      Number of successful file-edit tool calls (Edit, MultiEdit, Write, NotebookEdit) in Cowork sessions. Null, never 0, while the file-edit metrics are not enabled for this organization.

    - `multi_edit_tool_count: Integer`

      Number of successful MultiEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `notebook_edit_tool_count: Integer`

      Number of successful NotebookEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `plugins_used_count: Integer`

      Total number of plugin invocations in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization.

    - `sessions_with_file_edits_count: Integer`

      Number of distinct Cowork sessions with at least one successful file-edit tool call. Null while the file-edit metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `write_tool_count: Integer`

      Number of successful Write tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

  - `design_metrics: BetaAnalyticsDesignMetrics`

    Claude Design activity metrics for a single user on a given day.

    - `distinct_projects_created_count: Integer`

      Number of distinct Claude Design projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `distinct_projects_used_count: Integer`

      Number of distinct Claude Design projects the user worked in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_session_count: Integer`

      Number of distinct Claude Design sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `message_count: Integer`

      Number of messages sent in Claude Design sessions

  - `office_metrics: BetaAnalyticsOfficeMetrics`

    Office Agent activity metrics for a single user on a given day, broken out by Office product.

    - `excel: BetaAnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

      - `connectors_used_count: Integer`

        Number of MCP connector invocations

      - `distinct_connectors_used_count: Integer`

        Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: Integer`

        Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: Integer`

        Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: Integer`

        Number of messages sent

      - `skills_used_count: Integer`

        Number of skill invocations

    - `outlook: BetaAnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

    - `powerpoint: BetaAnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

    - `word: BetaAnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

  - `science_metrics: BetaAnalyticsScienceMetrics`

    Claude Science activity metrics for a single user on a given day.

    - `delegation_count: Integer`

      Number of delegations (handoffs to a specialized agent) in Claude Science sessions

    - `distinct_session_count: Integer`

      Number of distinct Claude Science sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `message_count: Integer`

      Number of messages sent in Claude Science sessions

    - `remote_compute_job_count: Integer`

      Number of remote compute jobs launched from Claude Science sessions

    - `skills_used_count: Integer`

      Total number of skill invocations in Claude Science sessions

  - `web_search_count: Integer`

    Number of web searches performed

  - `distinct_user_count: Integer`

    Number of distinct active users represented by this row. Only set for grouped rollups (`group_by[]`); null for per-user rows. In date-range mode, recomputed as an exact distinct count of the group's active members over the requested window, never a sum of per-day values.

  - `last_activity_date: Date`

    Most recent UTC day (YYYY-MM-DD) on which the user had any counted activity, within the requested window: equal to the requested `date` in single-day mode, and to the latest active day from `starting_date` (inclusive) to `ending_date` (exclusive) in date-range rollup mode — never a day earlier than the window start. On filtered requests (`filter[]`) only days matching the filter count: with `filter[]=rbac_group_id:{id}` it is the last day the user was active while a member of that group, consistent with the row's other metrics. On grouped (`group_by[]`) rows it is the latest day any member of the group was active (the requested `date` in single-day mode). Omitted from the response while last-activity reporting is not enabled for this organization.

    format: date

  - `rbac_group_id: String`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: String`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user: BetaAnalyticsUser`

    The user this row describes. Null on rows aggregated across users.

    - `type: :user`

      Object type. Always `user`.

    - `id: String`

      Tagged user identifier (e.g. `user_...`)

    - `email_address: String`

      Email address of the user

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.analytics.users.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "chat_metrics": {
        "connectors_used_count": 0,
        "distinct_artifacts_created_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_conversation_count": 0,
        "distinct_files_uploaded_count": 0,
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_shared_artifacts_viewed_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "shared_conversations_viewed_count": 0,
        "thinking_message_count": 0
      },
      "claude_code_metrics": {
        "core_metrics": {
          "artifacts_created_count": 0,
          "commit_count": 0,
          "distinct_session_count": 0,
          "lines_of_code": {
            "added_count": 0,
            "removed_count": 0
          },
          "pull_request_count": 0
        },
        "tool_actions": {
          "edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "multi_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "notebook_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "write_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          }
        }
      },
      "cowork_metrics": {
        "action_count": 0,
        "artifacts_created_count": 0,
        "connectors_used_count": 0,
        "dispatch_turn_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_session_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "skills_used_count": 0,
        "distinct_plugins_used_count": 0,
        "edit_tool_count": 0,
        "file_edit_count": 0,
        "multi_edit_tool_count": 0,
        "notebook_edit_tool_count": 0,
        "plugins_used_count": 0,
        "sessions_with_file_edits_count": 0,
        "write_tool_count": 0
      },
      "design_metrics": {
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_session_count": 0,
        "message_count": 0
      },
      "office_metrics": {
        "excel": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "outlook": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "powerpoint": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "word": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        }
      },
      "science_metrics": {
        "delegation_count": 0,
        "distinct_session_count": 0,
        "message_count": 0,
        "remote_compute_job_count": 0,
        "skills_used_count": 0
      },
      "web_search_count": 0,
      "distinct_user_count": 0,
      "last_activity_date": "2019-12-27",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user": {
        "id": "id",
        "email_address": "email_address",
        "type": "user"
      }
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Analytics › Apps › Chat › Projects

### Get Chat Project Usage

`beta.organization.analytics.apps.chat.projects.list(**kwargs) -> PageCursor<BetaAnalyticsProjectActivity>`

**GET** `/v1/organizations/analytics/apps/chat/projects`

Get per-project activity for a given day, with cursor-based pagination.

Returns activity metrics for each project in the organization, sorted by
project ID. Use `group_by[]` to break projects out per member or per RBAC
group, and `filter[]` to scope results; the parameter descriptions list the
supported dimensions. Available to organizations on a Claude Enterprise
plan. Requires an API key with the `read:analytics` scope.

#### Parameters

- `date: Date`

  UTC date in YYYY-MM-DD format. The day to get project activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: Date`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

  format: date

- `filter: Array[String]`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `project_id`, `rbac_group_id`, `user_id`. Value forms: `project_id` takes a tagged project id (`claude_proj_...`); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

  maxItems: 100

- `group_by: Array[:rbac_group_id | :user_id]`

  Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `rbac_group_id`, `user_id`. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

  maxItems: 100

  - `:rbac_group_id`

  - `:user_id`

- `limit: Integer`

  Number of results per page (1-1000, default 100).

  minimum: 1, maximum: 1000

- `order: :asc | :desc`

  Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

  - `:asc`

  - `:desc`

- `order_by: String`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: String`

  Opaque cursor from a previous response's `next_page` field.

- `starting_date: Date`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

#### Returns

- `class BetaAnalyticsProjectActivity`

  Per-project activity data for a given day.

  - `distinct_user_count: Integer`

    Number of distinct users who used the project on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `message_count: Integer`

    Number of messages sent in the project on the requested day

  - `project_id: String`

    Tagged project identifier (e.g. `claude_proj_...`)

  - `project_name: String`

    Name of the project

  - `created_at: Time`

    Project creation timestamp in RFC 3339 format. Null if the project was deleted before attribution was recorded.

    format: date-time

  - `created_by: BetaAnalyticsUser`

    User who created the project. Null if the project was deleted before attribution was recorded, or if the creator's account no longer exists.

    - `type: :user`

      Object type. Always `user`.

    - `id: String`

      Tagged user identifier (e.g. `user_...`)

    - `email_address: String`

      Email address of the user

  - `distinct_conversation_count: Integer`

    Number of distinct conversations in the project. Null on aggregated rows where a distinct count cannot be computed.

  - `product: String`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, or `office_agent` (the canonical Cost & Usage product naming; an `office_agent` row's per-surface breakdown is in its `office_metrics`). On `/plugins` only `cowork` and `claude_code` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, and `cowork` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `rbac_group_id: String`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: String`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: String`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.analytics.apps.chat.projects.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "distinct_user_count": 0,
      "message_count": 0,
      "project_id": "project_id",
      "project_name": "project_name",
      "created_at": "2019-12-27T18:11:19.117Z",
      "created_by": {
        "id": "id",
        "email_address": "email_address",
        "type": "user"
      },
      "distinct_conversation_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Analytics › Connectors

### Get Connector Usage

`beta.organization.analytics.connectors.list(**kwargs) -> PageCursor<BetaAnalyticsConnectorActivity>`

**GET** `/v1/organizations/analytics/connectors`

Get per-connector usage for a given day, with cursor-based pagination.

Returns connector usage metrics for the organization, sorted by connector
name. Connector names are normalized from their various sources — for
example, "Atlassian MCP server" and "mcp-atlassian" both appear as
"atlassian". Use `group_by[]` to break usage out per member, per RBAC
group, or per product surface, and `filter[]` to scope results; the
parameter descriptions list the supported dimensions. Available to
organizations on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

#### Parameters

- `date: Date`

  UTC date in YYYY-MM-DD format. The day to get connector usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: Date`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

  format: date

- `filter: Array[String]`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `connector_name`, `product`, `rbac_group_id`, `user_id`. Value forms: `connector_name` matches case-insensitively, a display name such as 'GitHub MCP' also matches its normalized stored form ('github'), and for rows whose `connector_name` is an opaque connector id the connector's display name (`connector_display_name`) also matches; `product` is one of `chat`, `claude_code`, `cowork`, or `office_agent`; `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

  maxItems: 100

- `group_by: Array[:product | :rbac_group_id | :user_id]`

  Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `product`, `rbac_group_id`, `user_id`. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

  maxItems: 100

  - `:product`

  - `:rbac_group_id`

  - `:user_id`

- `limit: Integer`

  Number of results per page (1-1000, default 100).

  minimum: 1, maximum: 1000

- `order: :asc | :desc`

  Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

  - `:asc`

  - `:desc`

- `order_by: String`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: String`

  Opaque cursor from a previous response's `next_page` field.

- `starting_date: Date`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

#### Returns

- `class BetaAnalyticsConnectorActivity`

  Per-connector activity data for a given day.

  - `chat_metrics: BetaAnalyticsConnectorChatMetrics`

    Claude.ai activity metrics for a single connector on a given day.

    - `distinct_conversation_connector_used_count: Integer`

      Number of distinct conversations in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `claude_code_metrics: BetaAnalyticsConnectorClaudeCodeMetrics`

    Claude Code activity metrics for a single connector on a given day.

    - `distinct_session_connector_used_count: Integer`

      Number of distinct Claude Code sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `connector_name: String`

    Name of the connector. Some rows carry an opaque connector id here instead of a readable name; `connector_display_name` holds the resolved name for those rows.

  - `cowork_metrics: BetaAnalyticsConnectorCoworkMetrics`

    Cowork activity metrics for a single connector on a given day.

    - `distinct_session_connector_used_count: Integer`

      Number of distinct Cowork sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_user_count: Integer`

    Number of distinct users who used the connector on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `office_metrics: BetaAnalyticsConnectorOfficeMetrics`

    Office Agent activity metrics for a single connector on a given day, broken out by Office product.

    - `excel: BetaAnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

      - `distinct_session_connector_used_count: Integer`

        Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `outlook: BetaAnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

    - `powerpoint: BetaAnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

    - `word: BetaAnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

  - `connector_display_name: String`

    Human-readable display name for rows whose `connector_name` is an opaque connector id rather than a readable name, resolved at request time from the organization's connectors (including connectors that have since been removed). `connector_name` remains the row's stable key for sorting and pagination, and `filter[]=connector_name:{value}` also matches these rows by display name. Display names are not unique, and the same connector's claude.ai usage can appear under a separate row with a readable `connector_name`. Null when `connector_name` is already a readable name, when the id cannot be resolved to one of the organization's connectors, or when display-name resolution is not enabled for this organization.

  - `individual_auth_distinct_user_count: Integer`

    Number of distinct users whose use of this connector on the requested day ran on their own individual credential, connected through their own consent flow. Companion bucket to `managed_auth_distinct_user_count`, which carries the measurement, attribution, and null rules. Users whose requests used no stored credential count in neither bucket.

  - `managed_auth_distinct_user_count: Integer`

    Number of distinct users whose use of this connector on the requested day ran on Enterprise Managed Auth (an organization-managed credential provisioned through the organization's identity provider), read from the token record each request used. Null, never 0, when managed-auth reporting is not enabled for the organization, the value cannot be attributed to the row, no credentialed requests and no managed-token mint events (a managed credential being provisioned for a user's use of the connector) were observed that day, or the day predates 2026-07-01, the first day the backing data exists (forward-only data, no backfill). When credentialed requests or mint events were observed and attributed, both managed-auth fields populate, reporting 0 for a bucket with no users; the two counts are independent, not a partition — a user whose requests that day used both kinds of credential counts in both. Mint events carry user but not surface attribution, so they count as observed auth activity on `user_id` and `rbac_group_id` cuts — attributed to the user the credential was provisioned for — but never on a cut that references `product` (group or filter). Date-range rollup mode (`starting_date`/`ending_date`) computes both fields exactly over the window — distinct users with at least one qualifying day — when the whole window starts on or after 2026-07-01, with the null-versus-0 and mint-event rules applying with the window in place of the day; a range starting earlier reports every managed-auth field as null, never a partial-window value.

  - `product: String`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, or `office_agent` (the canonical Cost & Usage product naming; an `office_agent` row's per-surface breakdown is in its `office_metrics`). On `/plugins` only `cowork` and `claude_code` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, and `cowork` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `rbac_group_id: String`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: String`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `read_call_count: Integer`

    Number of connector tool calls on the requested day whose trusted read-only annotation marked them read-only. Call count, not distinct users. Every call recorded on a classified surface lands in exactly one of `read_call_count`, `write_call_count`, or `unclassified_call_count`, so the three sum to the day's classified calls. Classification is forward-only per surface: claude.ai from 2026-06-01, Claude Code from 2026-05-30, Claude in Office from 2026-05-29, Cowork from 2026-06-02 (Cowork clients predating annotation forwarding land in `unclassified_call_count`). Null, never 0, when the value cannot be stated: the read/write split is not enabled for this organization, or the day predates 2026-05-29. For a date-range total, sum the per-day values, but treat a window that extends before 2026-05-29 as null rather than summing only its covered days — date-range rollup mode (`starting_date`/`ending_date`) applies both rules server-side.

  - `unclassified_call_count: Integer`

    Number of connector tool calls on the requested day with no trusted read-only annotation — the annotation is optional in the MCP spec and is discarded when connector access controls are active, so unclassified calls are common. This field shows how much of the day's classified activity the read/write split actually covers. Call count, not distinct users. One of the three call-classification buckets; see `read_call_count` for the per-surface data-start dates, null conditions, and date-range guidance.

  - `user_id: String`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

  - `write_call_count: Integer`

    Number of connector tool calls on the requested day whose trusted read-only annotation marked them not read-only. Call count, not distinct users. One of the three call-classification buckets; see `read_call_count` for the per-surface data-start dates, null conditions, and date-range guidance.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.analytics.connectors.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "chat_metrics": {
        "distinct_conversation_connector_used_count": 0
      },
      "claude_code_metrics": {
        "distinct_session_connector_used_count": 0
      },
      "connector_name": "connector_name",
      "cowork_metrics": {
        "distinct_session_connector_used_count": 0
      },
      "distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_connector_used_count": 0
        },
        "outlook": {
          "distinct_session_connector_used_count": 0
        },
        "powerpoint": {
          "distinct_session_connector_used_count": 0
        },
        "word": {
          "distinct_session_connector_used_count": 0
        }
      },
      "connector_display_name": "connector_display_name",
      "individual_auth_distinct_user_count": 0,
      "managed_auth_distinct_user_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "read_call_count": 0,
      "unclassified_call_count": 0,
      "user_id": "user_id",
      "write_call_count": 0
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Analytics › Plugins

### Get Plugin Usage

`beta.organization.analytics.plugins.list(**kwargs) -> PageCursor<BetaAnalyticsPluginActivity>`

**GET** `/v1/organizations/analytics/plugins`

Get per-plugin install + invocation usage for a given day, with pagination.

Returns plugin usage metrics for the organization across Cowork and Claude
Code, sorted by plugin name. The `plugin_name` value `third-party` is
an aggregate bucket, not a plugin: it collects plugin activity, from
either surface, for which the reporting client did not provide a plugin
name — so an organization's own plugins can contribute both to their own
named rows and to this bucket. Use `group_by[]` to break usage out per
member, per RBAC group, or per product surface (Cowork / Claude Code),
and `filter[]` to scope results; the parameter descriptions list the
supported dimensions. Requires an API key with the
`read:analytics` scope. `starting_date` / `ending_date` select
range-rollup mode like `/skills`.

#### Parameters

- `date: Date`

  UTC date in YYYY-MM-DD format. The day to get plugin usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: Date`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

  format: date

- `filter: Array[String]`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `plugin_name`, `product`, `rbac_group_id`, `user_id`. Value forms: `plugin_name` matches case-insensitively; `product` is `claude_code` or `cowork` (the only surfaces with plugin attribution); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

  maxItems: 100

- `group_by: Array[:product | :rbac_group_id | :user_id]`

  Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `product`, `rbac_group_id`, `user_id`. On this endpoint `product` takes the values `claude_code` or `cowork` only (the surfaces with plugin attribution). Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

  maxItems: 100

  - `:product`

  - `:rbac_group_id`

  - `:user_id`

- `limit: Integer`

  Number of results per page (1-1000, default 100).

  minimum: 1, maximum: 1000

- `order: :asc | :desc`

  Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

  - `:asc`

  - `:desc`

- `order_by: String`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: String`

  Opaque cursor from a previous response's `next_page` field.

- `starting_date: Date`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

#### Returns

- `class BetaAnalyticsPluginActivity`

  Per-plugin install + invocation activity for a given day.

  With `group_by[]=user_id` / `rbac_group_id` / `product` (`cowork` /
  `claude_code` only on this endpoint) each row is one (plugin, user),
  (plugin, group), or (plugin, product) cut: the flat `user_id` /
  `rbac_group_id` / `product` keys carry the cut and the counts are
  scoped to it.

  - `claude_code_metrics: BetaAnalyticsPluginClaudeCodeMetrics`

    Claude Code activity metrics for a single plugin on a given day.

    - `distinct_session_plugin_used_count: Integer`

      Number of distinct Claude Code sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

  - `cowork_metrics: BetaAnalyticsPluginCoworkMetrics`

    Cowork activity metrics for a single plugin on a given day.

    - `distinct_session_plugin_used_count: Integer`

      Number of distinct Cowork sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_user_count: Integer`

    Number of distinct users with recorded install or invocation activity for the plugin on the requested day (install-only users count), or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `install_count: Integer`

    Number of distinct users who installed the plugin on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `invocation_count: Integer`

    Number of plugin invocations on the requested day

  - `plugin_name: String`

    Name of the plugin

  - `plugin_id: String`

    Stable plugin identifier when available (e.g. `serena@claude-plugins-official`). Null for third-party Claude Code plugins (redacted at the source) and Cowork slash commands that carry only a hashed id.

  - `product: String`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, or `office_agent` (the canonical Cost & Usage product naming; an `office_agent` row's per-surface breakdown is in its `office_metrics`). On `/plugins` only `cowork` and `claude_code` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, and `cowork` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `rbac_group_id: String`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: String`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: String`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.analytics.plugins.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "claude_code_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "cowork_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "distinct_user_count": 0,
      "install_count": 0,
      "invocation_count": 0,
      "plugin_name": "plugin_name",
      "plugin_id": "plugin_id",
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Analytics › Skills

### Get Skill Usage

`beta.organization.analytics.skills.list(**kwargs) -> PageCursor<BetaAnalyticsSkillActivity>`

**GET** `/v1/organizations/analytics/skills`

Get per-skill usage for a given day, with cursor-based pagination.

Returns skill usage metrics for the organization, sorted by skill name.
Use `group_by[]` to break usage out per member, per RBAC group, or per
product surface, and `filter[]` to scope results; the parameter
descriptions list the supported dimensions. Available to organizations
on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

#### Parameters

- `date: Date`

  UTC date in YYYY-MM-DD format. The day to get skill usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: Date`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

  format: date

- `filter: Array[String]`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `product`, `rbac_group_id`, `share_status`, `skill_name`, `user_id`. Value forms: `product` is one of `chat`, `claude_code`, `cowork`, or `office_agent`; `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `share_status` is one of `organization`, `private`, or `public`; `skill_name` matches case-insensitively; `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

  maxItems: 100

- `group_by: Array[:product | :rbac_group_id | :user_id]`

  Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `product`, `rbac_group_id`, `user_id`. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

  maxItems: 100

  - `:product`

  - `:rbac_group_id`

  - `:user_id`

- `limit: Integer`

  Number of results per page (1-1000, default 100).

  minimum: 1, maximum: 1000

- `order: :asc | :desc`

  Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

  - `:asc`

  - `:desc`

- `order_by: String`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: String`

  Opaque cursor from a previous response's `next_page` field.

- `starting_date: Date`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

#### Returns

- `class BetaAnalyticsSkillActivity`

  Per-skill activity data for a given day.

  - `chat_metrics: BetaAnalyticsSkillChatMetrics`

    Claude.ai activity metrics for a single skill on a given day.

    - `distinct_conversation_skill_used_count: Integer`

      Number of distinct conversations in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `claude_code_metrics: BetaAnalyticsSkillClaudeCodeMetrics`

    Claude Code activity metrics for a single skill on a given day.

    - `distinct_session_skill_used_count: Integer`

      Number of distinct Claude Code sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `cowork_metrics: BetaAnalyticsSkillCoworkMetrics`

    Cowork activity metrics for a single skill on a given day.

    - `distinct_session_skill_used_count: Integer`

      Number of distinct Cowork sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_user_count: Integer`

    Number of distinct users who used the skill on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted.

  - `office_metrics: BetaAnalyticsSkillOfficeMetrics`

    Office Agent activity metrics for a single skill on a given day, broken out by Office product.

    - `excel: BetaAnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

      - `distinct_session_skill_used_count: Integer`

        Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `outlook: BetaAnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

    - `powerpoint: BetaAnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

    - `word: BetaAnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

  - `skill_name: String`

    Name of the skill

  - `attributed_list_price: String`

    List-price (rate-card) value of the member requests attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD), from Claude Code, Cowork, and Office Agent request-level attribution — the value of requests that involved the skill, not the skill's incremental cost. Unlike `estimated_overage_spend` this reflects usage value regardless of how it was funded — seat-covered usage counts — but it is undiscounted and does not tie to billed spend or the organization's spend reporting. claude.ai chat usage carries no request-level attribution and contributes nothing: the field is null on `chat` product rows and on `office_agent` product cuts dated before 2026-06-18 (the Office Agent attribution data-start), and on ungrouped rows it covers the Claude Code + Cowork + Office Agent share only (null when no attributable usage exists). Also null under the same conditions as `estimated_overage_spend` (spend reporting not enabled for this organization, `office_agent` product cuts before the 2026-06-18 data-start). "0" means attributable usage existed but none was attributed to this skill. Addable across days: date-range rollup mode returns the window's sum. On `group_by[]` and `filter[]` shapes both amounts can total below the ungrouped value for the same skill over the same date or range: spend attributed to a member–skill pair with no counted usage on that day is excluded from those cuts.

  - `currency: String`

    Currency for this row's monetary fields (`estimated_overage_spend` and `attributed_list_price`), as an uppercase ISO-4217 code. Always "USD" when either amount is populated; null whenever both amounts are null.

  - `enable_count: Integer`

    Distinct accounts that enabled this skill on the requested day (claude.ai only — the skill analog of plugin `install_count`). The count is org-wide: null when enable reporting is not enabled for this organization, or when the request scopes to `user_id` / `rbac_group_id` / `product` via `group_by[]` or `filter[]` (an org-wide count would be misleading on per-cut rows). A distinct count, not an event count: summing across days double-counts members who enable the skill on more than one day, so it is also null in date-range rollup mode (`starting_date`/`ending_date`).

  - `estimated_overage_spend: String`

    Estimated overage spend attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD; "1250" is $12.50, fractional cents possible) — an allocation of each member's daily post-discount, pre-credit metered overage spend (the same cost basis as the organization's spend reporting and the Cost & Usage API, so per-skill figures are directly comparable; spend with no skill attribution — including any member-day without skill invocations — is not represented, so skill rows sum to at most those totals) across the skills the member used. Overage only: usage covered by included seat allowances bills nothing and allocates $0 here — see `attributed_list_price` for the funding-independent usage-value companion. Claude Code, Cowork, and Office Agent spend use request-level skill attribution; claude.ai chat spend is approximated proportionally to skill-invoking messages. An estimate, not a billing number — and the cost of the requests/messages that involved the skill, not the skill's incremental cost (the same request would still have cost something without the skill active). "0" means no overage spend was attributed; null when spend reporting is not enabled for this organization, on `office_agent` product cuts dated before 2026-06-18 (the Office Agent attribution data-start). Addable across days: date-range rollup mode (`starting_date`/`ending_date`) returns the window's sum. With `group_by[]=user_id` each row carries the user's own attributed spend. On `group_by[]` and `filter[]` shapes both amounts can total below the ungrouped value for the same skill over the same date or range: spend attributed to a member–skill pair with no counted usage on that day is excluded from those cuts.

  - `invocation_count: Integer`

    Total number of times this skill was invoked on the requested day (the skill analog of plugin `invocation_count`). Unlike `distinct_user_count` — which answers '\# of users' — this is the true '# of uses'. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Null when invocation reporting is not enabled for this organization. Sum across a date range for total uses in the window — date-range rollup mode (`starting_date`/`ending_date`) returns this sum directly.

  - `product: String`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, or `office_agent` (the canonical Cost & Usage product naming; an `office_agent` row's per-surface breakdown is in its `office_metrics`). On `/plugins` only `cowork` and `claude_code` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, and `cowork` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `rbac_group_id: String`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: String`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `share_status: :organization | :private | :public`

    Skill share status (claude.ai only): one of `private`, `organization`, or `public`. Null for skills used only in Claude Code or Office (no per-skill share-status concept) and when share-status reporting is not yet available for the organization. Filterable via `filter[]=share_status:{value}`.

    - `:organization`

    - `:private`

    - `:public`

  - `skill_display_name: String`

    Human-readable display name for rows whose `skill_name` is an opaque skill id (user/organization skill types and plugin-delivered skills, whose user-defined names usage reports generally withhold). Organization-shared skills and skills delivered by the organization's own plugins (its plugin marketplaces and its library) resolve; plugin skill names are shown without their 'plugin:' prefix. The literal 'unknown' bucket row gets a fixed 'Unknown skill' label. For a member's own skill (private or personal-plugin) it is null, except when the skill's owner used it from Claude Code or Cowork in the requested period: then it shows the name that client reported at the time. Apart from that, the names of members' own skills are not disclosed to analytics-key holders. Also null for Anthropic-provided plugin skills (not resolved), for an organization skill or plugin whose name can no longer be found (for example, one since deleted), when `skill_name` is already a display name, or when display-name resolution is not enabled for this organization.

  - `user_id: String`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.analytics.skills.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "chat_metrics": {
        "distinct_conversation_skill_used_count": 0
      },
      "claude_code_metrics": {
        "distinct_session_skill_used_count": 0
      },
      "cowork_metrics": {
        "distinct_session_skill_used_count": 0
      },
      "distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_skill_used_count": 0
        },
        "outlook": {
          "distinct_session_skill_used_count": 0
        },
        "powerpoint": {
          "distinct_session_skill_used_count": 0
        },
        "word": {
          "distinct_session_skill_used_count": 0
        }
      },
      "skill_name": "skill_name",
      "attributed_list_price": "attributed_list_price",
      "currency": "currency",
      "enable_count": 0,
      "estimated_overage_spend": "estimated_overage_spend",
      "invocation_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "share_status": "organization",
      "skill_display_name": "skill_display_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Analytics › Artifacts

### Get Artifact Activity

`beta.organization.analytics.artifacts.list(**kwargs) -> PageCursor<BetaAnalyticsArtifactActivity>`

**GET** `/v1/organizations/analytics/artifacts`

Get artifact-creation activity for a given day, broken out by MIME type.

Returns the full (`artifact_type`, `is_shared`) cube for the organization;
`next_page` is null except for grouped queries, which paginate. The cube
can be broken out per product, per member, or per RBAC group via
`group_by[]`, and scoped via `filter[]`. Requires an API key with the
`read:analytics` scope.

#### Parameters

- `date: Date`

  UTC date in YYYY-MM-DD format. The day to get artifact activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `filter: Array[String]`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `artifact_type`, `is_shared`, `product`, `rbac_group_id`, `user_id`. Value forms: `artifact_type` is a canonical artifact MIME type (e.g. `text/markdown`) or `other`; `is_shared` is `true` or `false`; `product` is `chat`, `claude_code`, or `cowork` (the surfaces that create artifacts); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

  maxItems: 100

- `group_by: Array[:product | :rbac_group_id | :user_id]`

  Dimensions to break results out by: `product`, `user_id` and/or `rbac_group_id`. The ungrouped artifact-type cube is finite and returned in full; grouped queries multiply the cube and paginate via `next_page`. `product` takes the values `chat`, `claude_code`, or `cowork` (the surfaces that create artifacts). `rbac_group_id` attributes a user to every group they held at any point during the requested UTC day, so grouped rows are not an exclusive partition. At most 100 entries.

  maxItems: 100

  - `:product`

  - `:rbac_group_id`

  - `:user_id`

- `limit: Integer`

  Maximum rows to return (1-1000, default 100). The ungrouped artifact-type cube is finite and returned in full; `limit` is the page size only when `group_by[]` multiplies the cube.

  minimum: 1, maximum: 1000

- `page: String`

  Opaque cursor from a previous response's `next_page` field. Only valid with `group_by[]` — the ungrouped cube is never paginated.

#### Returns

- `class BetaAnalyticsArtifactActivity`

  Artifact-creation activity for one (`artifact_type`, `is_shared`) bucket
  on a given day.

  Artifacts form a small finite cube — the canonical MIME type (8 values incl.
  `other`) crossed with shared-vs-private — so the response is the full set of
  non-empty buckets, not a ranked/paginated list. Claude Code and Cowork
  artifacts report under `text/html` and are counted from 2026-08-17
  onward; earlier days contain claude.ai chat artifacts only. With
  `group_by[]=product` / `user_id` / `rbac_group_id` each row is further
  split by the flat group keys and counts are scoped to that cut.

  - `artifact_type: String`

    Canonical artifact MIME type (e.g. `text/markdown`, `application/vnd.ant.react`, `image/svg+xml`), or `other`. Claude Code and Cowork artifacts report as `text/html`.

  - `artifacts_created_count: Integer`

    Number of artifacts created in this bucket on the requested day

  - `distinct_user_count: Integer`

    Number of distinct users who created artifacts in this bucket on the requested day

  - `is_shared: bool`

    Whether the artifacts in this bucket have ever been shared (a Claude Code / Cowork artifact is shared once anyone beyond its creator may open it: named members, the whole organization, or anyone with the link).

  - `published_artifacts_created_count: Integer`

    Number of those artifacts that have been published (for Claude Code / Cowork artifacts: open to anyone with the link); never exceeds `artifacts_created_count`

  - `product: String`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, or `office_agent` (the canonical Cost & Usage product naming; an `office_agent` row's per-surface breakdown is in its `office_metrics`). On `/plugins` only `cowork` and `claude_code` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, and `cowork` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `rbac_group_id: String`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: String`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: String`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.analytics.artifacts.list(date: "2019-12-27")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "artifact_type": "artifact_type",
      "artifacts_created_count": 0,
      "distinct_user_count": 0,
      "is_shared": true,
      "published_artifacts_created_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Analytics › Usage Report

### Get Token Usage Over Time

`beta.organization.analytics.usage_report.list(**kwargs) -> PageCursor<BetaAnalyticsUsageReportTimeBucket>`

**GET** `/v1/organizations/analytics/usage_report`

Get token usage over time across a date range.

Returns token usage bucketed by minute, hour, or day, optionally broken
down by product, model, context window, inference region, or speed.
Available to organizations on a Claude Enterprise plan. Requires an API
key with the `read:analytics` scope.

#### Parameters

- `starting_at: Time`

  Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

  format: date-time

- `bucket_width: :"1d" | :"1h" | :"1m"`

  Time bucket granularity.

  - `:"1d"`

  - `:"1h"`

  - `:"1m"`

- `claude_tag_categories: Array[BetaAnalyticsClaudeTagCategory]`

  Filter to Claude Tag (Claude in Slack) usage in specific spend categories. Usage with no category never matches. `dm` usage is reported under the user's product rather than `claude-tag`, so combining this filter with `products[]=claude-tag` excludes it. Use `group_by[]=claude_tag_category` to break out per-category values.

  maxItems: 100

  - `:dm`

  - `:engaged`

  - `:monitoring`

  - `:proactive`

  - `:scheduled`

- `claude_tag_user_ids: Array[String]`

  Filter to Claude Tag (Claude in Slack) usage attributed to specific Slack users, by Slack user ID (for example `U0123ABCDEF`), not claude.ai user ID. Usage that is not Claude Tag, and Claude Tag usage not attributed to a single user, never matches. Use `group_by[]=claude_tag_user_id` to break out per-user values.

  maxItems: 100

- `context_windows: Array[BetaAnalyticsContextWindow]`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  maxItems: 100

  - `:"0-200k"`

  - `:"200k-1M"`

- `ending_at: Time`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

  format: date-time

- `group_by: Array[:claude_tag_category | :claude_tag_user_id | :context_window | 6 more]`

  Dimensions to break each time bucket out by. Defaults to no grouping (one total per bucket). Each bucket reports at most its top 100 groups; a group beyond that cap has no row in that bucket (there is no remainder row), so grouped buckets are not exhaustive when a dimension has more than 100 distinct values.

  maxItems: 100

  - `:claude_tag_category`

  - `:claude_tag_user_id`

  - `:context_window`

  - `:inference_geo`

  - `:model`

  - `:product`

  - `:rbac_group_id`

  - `:slack_channel_id`

  - `:speed`

- `inference_geos: Array[BetaAnalyticsInferenceGeoFilter]`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  maxItems: 100

  - `:global`

  - `:not_available`

  - `:us`

- `limit: Integer`

  Maximum number of time buckets per page. Defaults and caps vary by `bucket_width` (`1d`: default 7, max 31; `1h`: default 24, max 168; `1m`: default 60, max 256).

  minimum: 1

- `models: Array[String]`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

  maxItems: 100

- `page: String`

  Opaque cursor from a previous response's `next_page` field.

- `products: Array[BetaAnalyticsProductFilter]`

  Product surfaces to include. Defaults to all products. Use `group_by[]=product` to break out per-product values.

  maxItems: 100

  - `:chat`

  - `:"claude-tag"`

  - `:claude_code`

  - `:claude_design`

  - `:claude_in_chrome`

  - `:cowork`

  - `:office_agent`

- `rbac_group_ids: Array[String]`

  Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

  maxItems: 100

- `slack_channel_ids: Array[String]`

  Filter to usage originating from specific Slack channels. Use `group_by[]=slack_channel_id` to break out per-channel values.

  maxItems: 100

- `speeds: Array[:fast | :standard]`

  Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

  maxItems: 100

  - `:fast`

  - `:standard`

- `user_ids: Array[String]`

  Filter to specific users by tagged user ID.

  maxItems: 100

#### Returns

- `class BetaAnalyticsUsageReportTimeBucket`

  - `ending_at: Time`

    End of the time bucket (exclusive) in RFC 3339 format.

    format: date-time

  - `results: Array[BetaAnalyticsUsageBucketedResult]`

    Rows for this time bucket. Empty when the bucket has no data; otherwise a single combined row when `group_by[]` is omitted, or one row per group (subject to the per-bucket group cap described on the `group_by[]` parameter).

    - `cache_creation: BetaCacheCreation`

      The number of input tokens for cache creation.

      - `ephemeral_1h_input_tokens: Integer`

        The number of input tokens used to create the 1 hour cache entry.

        minimum: 0

      - `ephemeral_5m_input_tokens: Integer`

        The number of input tokens used to create the 5 minute cache entry.

        minimum: 0

    - `cache_read_input_tokens: Integer`

      The number of input tokens read from the cache.

    - `claude_tag_category: BetaAnalyticsClaudeTagCategory`

      Claude Tag (Claude in Slack) spend category: `engaged` (a person addressed Claude in a channel or thread), `proactive` (Claude responded without being addressed), `scheduled` (a scheduled routine ran), `monitoring` (Claude watching a channel it was asked to monitor), or `dm` (direct messages with Claude). Populated only when `claude_tag_category` is in `group_by[]`; null for usage that is not Claude Tag. Direct-message usage is billed to the individual user and is reported under that user's product, not under `claude-tag`. New categories may be added over time.

      - `:dm`

      - `:engaged`

      - `:monitoring`

      - `:proactive`

      - `:scheduled`

    - `claude_tag_user_id: String`

      Slack user ID (for example `U0123ABCDEF`) of the member the Claude Tag (Claude in Slack) usage is attributed to, not a claude.ai user ID. Populated only when `claude_tag_user_id` is in `group_by[]`; null for usage that is not Claude Tag and for Claude Tag usage that is not attributed to a single user (for example `monitoring`, and `proactive` usage Claude initiated), so per-user rows can sum to less than the Claude Tag total. Cannot be combined with `group_by[]=rbac_group_id` or the `rbac_group_ids[]` filter.

    - `context_window: BetaAnalyticsContextWindow`

      Context-window pricing tier of the usage or cost. Null unless `context_window` is in `group_by[]`; it can also be null on grouped rows with no context-window tier, such as code execution.

      - `:"0-200k"`

      - `:"200k-1M"`

    - `inference_geo: :global | :us`

      Inference region of the usage or cost. Null unless `inference_geo` is in `group_by[]`; it can also be null on grouped rows where the region is not set (the rows that `inference_geos[]=not_available` matches).

      - `:global`

      - `:us`

    - `model: String`

      Model that produced the usage or cost, as a model name in the form the `models[]` filter accepts (for example, `claude-opus-5`). Null unless `model` is in `group_by[]`; it can also be null on grouped rows whose usage or cost is not attributed to a specific model, such as code execution.

    - `output_tokens: Integer`

      The number of output tokens generated.

    - `product: String`

      Product surface that produced the usage or cost. Null unless product is in `group_by[]`; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include `chat`, `claude_code`, `cowork`, `office_agent`, `claude_in_chrome`, `claude_design`, and `claude-tag`. `claude-tag` is Claude Tag, the Claude product in Slack. Some unattributed usage is reported as "other".

    - `rbac_group_id: String`

      RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has one id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query without `group_by[]`.

    - `requests: Integer`

      Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

    - `server_tool_use: BetaAnalyticsServerToolUse`

      Server-side tool usage metrics.

      - `web_search_requests: Integer`

        The number of web search requests made.

    - `slack_channel_id: String`

      Slack channel the usage originated from. Populated only when `slack_channel_id` is in `group_by[]`; null for usage outside Slack (and for rows recorded before channel attribution was enabled).

    - `speed: :fast | :standard`

      Inference speed mode of the usage or cost: `fast` or `standard`. Null unless `speed` is in `group_by[]`.

      - `:fast`

      - `:standard`

    - `uncached_input_tokens: Integer`

      The number of uncached input tokens processed.

  - `starting_at: Time`

    Start of the time bucket (inclusive) in RFC 3339 format.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.analytics.usage_report.list(starting_at: "2019-12-27T18:11:19.117Z")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "ending_at": "2019-12-27T18:11:19.117Z",
      "results": [
        {
          "cache_creation": {
            "ephemeral_1h_input_tokens": 0,
            "ephemeral_5m_input_tokens": 0
          },
          "cache_read_input_tokens": 0,
          "claude_tag_category": "dm",
          "claude_tag_user_id": "U0123ABCDEF",
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "claude-opus-5",
          "output_tokens": 0,
          "product": "chat",
          "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
          "requests": 0,
          "server_tool_use": {
            "web_search_requests": 10
          },
          "slack_channel_id": "C0123ABCDEF",
          "speed": "fast",
          "uncached_input_tokens": 0
        }
      ],
      "starting_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

## Beta › Organization › Analytics › User Usage Report

### Get Per-User Token Usage

`beta.organization.analytics.user_usage_report.list(**kwargs) -> PageCursor<BetaAnalyticsUsageUsersItem>`

**GET** `/v1/organizations/analytics/user_usage_report`

Get per-user token usage across a date range.

Returns one row per user, ranked by the chosen token metric. Use this to
see which users consume the most tokens. Only usage attributable to a
seat user is included; for organization-wide totals including direct
API-key and automation traffic, use the bucketed
`/v1/organizations/analytics/usage_report` endpoint. Available to
organizations on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

#### Parameters

- `starting_at: Time`

  Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

  format: date-time

- `bucket_width: :"1d" | :"1h" | :"1m"`

  Time-bucket granularity. When set, each row's `starting_at` and `ending_at` are populated and one actor may span several rows (one per time bucket with usage). The time bucket counts toward `limit`, so one page can return multiple rows for the same actor. `ending_at` is required when `bucket_width` is set, and with `bucket_width="1m"` the range may span at most 24 hours. When omitted, each row aggregates the full `[starting_at, ending_at)` range.

  - `:"1d"`

  - `:"1h"`

  - `:"1m"`

- `claude_tag_categories: Array[BetaAnalyticsClaudeTagCategory]`

  Filter to Claude Tag (Claude in Slack) usage in specific spend categories. Usage with no category never matches. `dm` usage is reported under the user's product rather than `claude-tag`, so combining this filter with `products[]=claude-tag` excludes it. Use `group_by[]=claude_tag_category` to break out per-category values.

  maxItems: 100

  - `:dm`

  - `:engaged`

  - `:monitoring`

  - `:proactive`

  - `:scheduled`

- `claude_tag_user_ids: Array[String]`

  Filter to Claude Tag (Claude in Slack) usage attributed to specific Slack users, by Slack user ID (for example `U0123ABCDEF`), not claude.ai user ID. Usage that is not Claude Tag, and Claude Tag usage not attributed to a single user, never matches. Use `group_by[]=claude_tag_user_id` to break out per-user values.

  maxItems: 100

- `context_windows: Array[BetaAnalyticsContextWindow]`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  maxItems: 100

  - `:"0-200k"`

  - `:"200k-1M"`

- `ending_at: Time`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

  format: date-time

- `exclude_deleted_users: bool`

  If true, omit rows for users who are deleted (`deleted: true`). A page may contain fewer than `limit` rows; use `has_more` and `next_page` to paginate as usual.

- `group_by: Array[:claude_tag_category | :claude_tag_user_id | :context_window | 6 more]`

  Break each actor's row out by the given dimensions. Accepts the same values as the bucketed `/usage_report` endpoint. `limit` bounds (actor × time bucket × dimension) rows — with dimensions or `bucket_width` present, one actor may span several rows.

  maxItems: 100

  - `:claude_tag_category`

  - `:claude_tag_user_id`

  - `:context_window`

  - `:inference_geo`

  - `:model`

  - `:product`

  - `:rbac_group_id`

  - `:slack_channel_id`

  - `:speed`

- `inference_geos: Array[BetaAnalyticsInferenceGeoFilter]`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  maxItems: 100

  - `:global`

  - `:not_available`

  - `:us`

- `limit: Integer`

  Number of rows per page (1-1000, default 20). One row per actor unless `group_by[]` or `bucket_width` splits an actor across rows; `cost_type`/`token_type` fan-out rows (cost endpoint only) are the exception — they do not count toward this limit, so `data` can exceed it.

  minimum: 1, maximum: 1000

- `models: Array[String]`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

  maxItems: 100

- `order: :asc | :desc`

  Sort direction. Defaults to `desc`.

  - `:asc`

  - `:desc`

- `order_by: :output_tokens | :requests | :total_tokens | :uncached_input_tokens`

  Metric to rank actors by. Defaults to `total_tokens`.

  - `:output_tokens`

  - `:requests`

  - `:total_tokens`

  - `:uncached_input_tokens`

- `page: String`

  Opaque cursor from a previous response's `next_page` field.

- `products: Array[BetaAnalyticsProductFilter]`

  Product surfaces to include. Defaults to all products.

  maxItems: 100

  - `:chat`

  - `:"claude-tag"`

  - `:claude_code`

  - `:claude_design`

  - `:claude_in_chrome`

  - `:cowork`

  - `:office_agent`

- `rbac_group_ids: Array[String]`

  Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

  maxItems: 100

- `slack_channel_ids: Array[String]`

  Filter to usage originating from specific Slack channels. Use `group_by[]=slack_channel_id` to break out per-channel values.

  maxItems: 100

- `speeds: Array[:fast | :standard]`

  Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

  maxItems: 100

  - `:fast`

  - `:standard`

- `user_ids: Array[String]`

  Filter to specific users by tagged user ID.

  maxItems: 100

#### Returns

- `class BetaAnalyticsUsageUsersItem`

  - `actor: BetaAnalyticsUserActor`

    The user this row's usage or cost is attributed to. Always a `user_actor`.

    - `type: :user_actor`

      Actor type. Always `"user_actor"`.

    - `deleted: bool`

      True when the account has been deleted, or when the user is no longer a member of the organization or its associated organizations (for example, their membership was removed or they were deprovisioned via your identity provider). `email_address` stays populated for removed users and is null when the account has been deleted. `name` follows the rules described on that field. The `user_id` is still populated for reconciliation.

    - `email_address: String`

      The user's email address, including for users who are no longer members of the organization or its associated organizations. Null when the account has been deleted (check `deleted`) and for system-minted service accounts, which have no person's mailbox behind them (check `name`).

    - `name: String`

      The user's full name. Null when the user has not set a name. Returns `"Deleted User"` when the account itself has been deleted, or when the user is no longer a member of the organization or its associated organizations and the organization has chosen to hide the names of removed users. Otherwise, the name stays populated for removed users. Rows for system-minted service accounts render the service name (for example, `"Claude Security"` for usage by Anthropic's security-patching service) or null.

    - `user_id: String`

      Tagged user ID.

  - `cache_creation: BetaCacheCreation`

    The number of input tokens for cache creation.

    - `ephemeral_1h_input_tokens: Integer`

      The number of input tokens used to create the 1 hour cache entry.

      minimum: 0

    - `ephemeral_5m_input_tokens: Integer`

      The number of input tokens used to create the 5 minute cache entry.

      minimum: 0

  - `cache_read_input_tokens: Integer`

    The number of input tokens read from the cache.

  - `claude_tag_category: BetaAnalyticsClaudeTagCategory`

    Claude Tag (Claude in Slack) spend category: `engaged` (a person addressed Claude in a channel or thread), `proactive` (Claude responded without being addressed), `scheduled` (a scheduled routine ran), `monitoring` (Claude watching a channel it was asked to monitor), or `dm` (direct messages with Claude). Populated only when `claude_tag_category` is in `group_by[]`; null for usage that is not Claude Tag. Direct-message usage is billed to the individual user and is reported under that user's product, not under `claude-tag`. New categories may be added over time.

    - `:dm`

    - `:engaged`

    - `:monitoring`

    - `:proactive`

    - `:scheduled`

  - `claude_tag_user_id: String`

    Slack user ID (for example `U0123ABCDEF`) of the member the Claude Tag (Claude in Slack) usage is attributed to, not a claude.ai user ID. Populated only when `claude_tag_user_id` is in `group_by[]`; null for usage that is not Claude Tag and for Claude Tag usage that is not attributed to a single user (for example `monitoring`, and `proactive` usage Claude initiated), so per-user rows can sum to less than the Claude Tag total. Cannot be combined with `group_by[]=rbac_group_id` or the `rbac_group_ids[]` filter.

  - `context_window: BetaAnalyticsContextWindow`

    Context-window pricing tier of the usage or cost. Null unless `context_window` is in `group_by[]`; it can also be null on grouped rows with no context-window tier, such as code execution.

    - `:"0-200k"`

    - `:"200k-1M"`

  - `ending_at: Time`

    End of the row's UTC time bucket (exclusive), as an RFC 3339 timestamp; equal to `starting_at` plus one `bucket_width`. Null unless `bucket_width` is set.

    format: date-time

  - `inference_geo: :global | :us`

    Inference region of the usage or cost. Null unless `inference_geo` is in `group_by[]`; it can also be null on grouped rows where the region is not set (the rows that `inference_geos[]=not_available` matches).

    - `:global`

    - `:us`

  - `model: String`

    Model that produced the usage or cost, as a model name in the form the `models[]` filter accepts (for example, `claude-opus-5`). Null unless `model` is in `group_by[]`; it can also be null on grouped rows whose usage or cost is not attributed to a specific model, such as code execution.

  - `output_tokens: Integer`

    The number of output tokens generated.

  - `product: String`

    Product surface that produced the usage or cost. Null unless product is in `group_by[]`; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include `chat`, `claude_code`, `cowork`, `office_agent`, `claude_in_chrome`, `claude_design`, and `claude-tag`. `claude-tag` is Claude Tag, the Claude product in Slack. Some unattributed usage is reported as "other".

  - `rbac_group_id: String`

    RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has one id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query without `group_by[]`.

  - `requests: Integer`

    Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

  - `server_tool_use: BetaAnalyticsServerToolUse`

    Server-side tool usage metrics.

    - `web_search_requests: Integer`

      The number of web search requests made.

  - `slack_channel_id: String`

    Slack channel the usage originated from. Populated only when `slack_channel_id` is in `group_by[]`; null for usage outside Slack (and for rows recorded before channel attribution was enabled).

  - `speed: :fast | :standard`

    Inference speed mode of the usage or cost: `fast` or `standard`. Null unless `speed` is in `group_by[]`.

    - `:fast`

    - `:standard`

  - `starting_at: Time`

    Start of the row's UTC time bucket (inclusive), as an RFC 3339 timestamp. Null unless `bucket_width` is set; without `bucket_width`, each row aggregates the full requested range.

    format: date-time

  - `total_tokens: Integer`

    Total token count across all token types. This is the value the default `order_by` (`total_tokens`) sorts on.

  - `uncached_input_tokens: Integer`

    The number of uncached input tokens processed.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.analytics.user_usage_report.list(starting_at: "2019-12-27T18:11:19.117Z")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "actor": {
        "deleted": true,
        "email": "jane@example.com",
        "email_address": "jane@example.com",
        "name": "Jane Smith",
        "type": "user_actor",
        "user_id": "user_01AbCdEfGhIjKlMnOpQrSt"
      },
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "cache_read_input_tokens": 3200000,
      "claude_tag_category": "dm",
      "claude_tag_user_id": "U0123ABCDEF",
      "context_window": "0-200k",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "model": "claude-opus-5",
      "output_tokens": 891000,
      "product": "chat",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "requests": 128,
      "server_tool_use": {
        "web_search_requests": 10
      },
      "slack_channel_id": "C0123ABCDEF",
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "total_tokens": 5377000,
      "uncached_input_tokens": 1284500
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

## Beta › Organization › Analytics › Cost Report

### Get Cost Over Time

`beta.organization.analytics.cost_report.list(**kwargs) -> PageCursor<BetaAnalyticsCostReportTimeBucket>`

**GET** `/v1/organizations/analytics/cost_report`

Get cost in USD over time across a date range.

Returns cost bucketed by minute, hour, or day, optionally broken down by
product, model, context window, inference region, speed, cost type, or
token type. Available to organizations on a Claude Enterprise plan.
Requires an API key with the `read:analytics` scope.

#### Parameters

- `starting_at: Time`

  Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

  format: date-time

- `bucket_width: :"1d" | :"1h" | :"1m"`

  Time bucket granularity.

  - `:"1d"`

  - `:"1h"`

  - `:"1m"`

- `claude_tag_categories: Array[BetaAnalyticsClaudeTagCategory]`

  Filter to Claude Tag (Claude in Slack) usage in specific spend categories. Usage with no category never matches. `dm` usage is reported under the user's product rather than `claude-tag`, so combining this filter with `products[]=claude-tag` excludes it. Use `group_by[]=claude_tag_category` to break out per-category values.

  maxItems: 100

  - `:dm`

  - `:engaged`

  - `:monitoring`

  - `:proactive`

  - `:scheduled`

- `claude_tag_user_ids: Array[String]`

  Filter to Claude Tag (Claude in Slack) usage attributed to specific Slack users, by Slack user ID (for example `U0123ABCDEF`), not claude.ai user ID. Usage that is not Claude Tag, and Claude Tag usage not attributed to a single user, never matches. Use `group_by[]=claude_tag_user_id` to break out per-user values.

  maxItems: 100

- `context_windows: Array[BetaAnalyticsContextWindow]`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  maxItems: 100

  - `:"0-200k"`

  - `:"200k-1M"`

- `ending_at: Time`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

  format: date-time

- `group_by: Array[:claude_tag_category | :claude_tag_user_id | :context_window | 8 more]`

  Dimensions to break each time bucket out by. Defaults to no grouping (one total per bucket). Each bucket reports at most its top 100 groups; a group beyond that cap has no row in that bucket (there is no remainder row), so grouped buckets are not exhaustive when a dimension has more than 100 distinct values.

  maxItems: 100

  - `:claude_tag_category`

  - `:claude_tag_user_id`

  - `:context_window`

  - `:cost_type`

  - `:inference_geo`

  - `:model`

  - `:product`

  - `:rbac_group_id`

  - `:slack_channel_id`

  - `:speed`

  - `:token_type`

- `inference_geos: Array[BetaAnalyticsInferenceGeoFilter]`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  maxItems: 100

  - `:global`

  - `:not_available`

  - `:us`

- `limit: Integer`

  Maximum number of time buckets per page. Defaults and caps vary by `bucket_width` (`1d`: default 7, max 31; `1h`: default 24, max 168; `1m`: default 60, max 256).

  minimum: 1

- `models: Array[String]`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

  maxItems: 100

- `page: String`

  Opaque cursor from a previous response's `next_page` field.

- `products: Array[BetaAnalyticsProductFilter]`

  Product surfaces to include. Defaults to all products. Use `group_by[]=product` to break out per-product values.

  maxItems: 100

  - `:chat`

  - `:"claude-tag"`

  - `:claude_code`

  - `:claude_design`

  - `:claude_in_chrome`

  - `:cowork`

  - `:office_agent`

- `rbac_group_ids: Array[String]`

  Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

  maxItems: 100

- `slack_channel_ids: Array[String]`

  Filter to usage originating from specific Slack channels. Use `group_by[]=slack_channel_id` to break out per-channel values.

  maxItems: 100

- `speeds: Array[:fast | :standard]`

  Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

  maxItems: 100

  - `:fast`

  - `:standard`

- `user_ids: Array[String]`

  Filter to specific users by tagged user ID.

  maxItems: 100

#### Returns

- `class BetaAnalyticsCostReportTimeBucket`

  - `ending_at: Time`

    End of the time bucket (exclusive) in RFC 3339 format.

    format: date-time

  - `results: Array[BetaAnalyticsCostBucketedResult]`

    Rows for this time bucket. Empty when the bucket has no data; otherwise a single combined row when `group_by[]` is omitted, or one row per group (subject to the per-bucket group cap described on the `group_by[]` parameter).

    - `amount: String`

      Amount (post-discount, pre-credit) in fractional cents.

    - `claude_tag_category: BetaAnalyticsClaudeTagCategory`

      Claude Tag (Claude in Slack) spend category: `engaged` (a person addressed Claude in a channel or thread), `proactive` (Claude responded without being addressed), `scheduled` (a scheduled routine ran), `monitoring` (Claude watching a channel it was asked to monitor), or `dm` (direct messages with Claude). Populated only when `claude_tag_category` is in `group_by[]`; null for usage that is not Claude Tag. Direct-message usage is billed to the individual user and is reported under that user's product, not under `claude-tag`. New categories may be added over time.

      - `:dm`

      - `:engaged`

      - `:monitoring`

      - `:proactive`

      - `:scheduled`

    - `claude_tag_user_id: String`

      Slack user ID (for example `U0123ABCDEF`) of the member the Claude Tag (Claude in Slack) usage is attributed to, not a claude.ai user ID. Populated only when `claude_tag_user_id` is in `group_by[]`; null for usage that is not Claude Tag and for Claude Tag usage that is not attributed to a single user (for example `monitoring`, and `proactive` usage Claude initiated), so per-user rows can sum to less than the Claude Tag total. Cannot be combined with `group_by[]=rbac_group_id` or the `rbac_group_ids[]` filter.

    - `context_window: BetaAnalyticsContextWindow`

      Context-window pricing tier of the usage or cost. Null unless `context_window` is in `group_by[]`; it can also be null on grouped rows with no context-window tier, such as code execution.

      - `:"0-200k"`

      - `:"200k-1M"`

    - `cost_type: BetaAnalyticsCostType`

      Cost component when `group_by[]=cost_type`; null otherwise (amount is the combined total).

      - `:code_execution`

      - `:tokens`

      - `:web_search`

    - `currency: String`

      Currency code for the cost amount. Currently always `"USD"`.

    - `inference_geo: :global | :us`

      Inference region of the usage or cost. Null unless `inference_geo` is in `group_by[]`; it can also be null on grouped rows where the region is not set (the rows that `inference_geos[]=not_available` matches).

      - `:global`

      - `:us`

    - `list_amount: String`

      List-price amount (pre-discount) in fractional cents.

    - `model: String`

      Model that produced the usage or cost, as a model name in the form the `models[]` filter accepts (for example, `claude-opus-5`). Null unless `model` is in `group_by[]`; it can also be null on grouped rows whose usage or cost is not attributed to a specific model, such as code execution.

    - `product: String`

      Product surface that produced the usage or cost. Null unless product is in `group_by[]`; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include `chat`, `claude_code`, `cowork`, `office_agent`, `claude_in_chrome`, `claude_design`, and `claude-tag`. `claude-tag` is Claude Tag, the Claude product in Slack. Some unattributed usage is reported as "other".

    - `rbac_group_id: String`

      RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has one id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query without `group_by[]`.

    - `requests: Integer`

      Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

    - `slack_channel_id: String`

      Slack channel the usage originated from. Populated only when `slack_channel_id` is in `group_by[]`; null for usage outside Slack (and for rows recorded before channel attribution was enabled).

    - `speed: :fast | :standard`

      Inference speed mode of the usage or cost: `fast` or `standard`. Null unless `speed` is in `group_by[]`.

      - `:fast`

      - `:standard`

    - `token_type: BetaAnalyticsTokenType`

      Token type when `group_by[]=token_type` and `cost_type=tokens`; null otherwise.

      - `:"cache_creation.ephemeral_1h_input_tokens"`

      - `:"cache_creation.ephemeral_5m_input_tokens"`

      - `:cache_read_input_tokens`

      - `:output_tokens`

      - `:uncached_input_tokens`

  - `starting_at: Time`

    Start of the time bucket (inclusive) in RFC 3339 format.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.analytics.cost_report.list(starting_at: "2019-12-27T18:11:19.117Z")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "ending_at": "2019-12-27T18:11:19.117Z",
      "results": [
        {
          "amount": "amount",
          "claude_tag_category": "dm",
          "claude_tag_user_id": "U0123ABCDEF",
          "context_window": "0-200k",
          "cost_type": "code_execution",
          "currency": "USD",
          "inference_geo": "global",
          "list_amount": "list_amount",
          "model": "claude-opus-5",
          "product": "chat",
          "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
          "requests": 0,
          "slack_channel_id": "C0123ABCDEF",
          "speed": "fast",
          "token_type": "cache_creation.ephemeral_1h_input_tokens"
        }
      ],
      "starting_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

## Beta › Organization › Analytics › User Cost Report

### Get Per-User Cost

`beta.organization.analytics.user_cost_report.list(**kwargs) -> PageCursor<BetaAnalyticsCostUsersItem>`

**GET** `/v1/organizations/analytics/user_cost_report`

Get per-user cost in USD across a date range.

Returns one row per user, ranked by spend. Use this to see which users
account for the most cost. Only cost attributable to a seat user is
included; for organization-wide totals including direct API-key and
automation traffic, use the bucketed
`/v1/organizations/analytics/cost_report` endpoint. Available to
organizations on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

#### Parameters

- `starting_at: Time`

  Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

  format: date-time

- `bucket_width: :"1d" | :"1h" | :"1m"`

  Time-bucket granularity. When set, each row's `starting_at` and `ending_at` are populated and one actor may span several rows (one per time bucket with usage). The time bucket counts toward `limit`, so one page can return multiple rows for the same actor. `ending_at` is required when `bucket_width` is set, and with `bucket_width="1m"` the range may span at most 24 hours. When omitted, each row aggregates the full `[starting_at, ending_at)` range.

  - `:"1d"`

  - `:"1h"`

  - `:"1m"`

- `claude_tag_categories: Array[BetaAnalyticsClaudeTagCategory]`

  Filter to Claude Tag (Claude in Slack) usage in specific spend categories. Usage with no category never matches. `dm` usage is reported under the user's product rather than `claude-tag`, so combining this filter with `products[]=claude-tag` excludes it. Use `group_by[]=claude_tag_category` to break out per-category values.

  maxItems: 100

  - `:dm`

  - `:engaged`

  - `:monitoring`

  - `:proactive`

  - `:scheduled`

- `claude_tag_user_ids: Array[String]`

  Filter to Claude Tag (Claude in Slack) usage attributed to specific Slack users, by Slack user ID (for example `U0123ABCDEF`), not claude.ai user ID. Usage that is not Claude Tag, and Claude Tag usage not attributed to a single user, never matches. Use `group_by[]=claude_tag_user_id` to break out per-user values.

  maxItems: 100

- `context_windows: Array[BetaAnalyticsContextWindow]`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  maxItems: 100

  - `:"0-200k"`

  - `:"200k-1M"`

- `ending_at: Time`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

  format: date-time

- `exclude_deleted_users: bool`

  If true, omit rows for users who are deleted (`deleted: true`). A page may contain fewer than `limit` rows; use `has_more` and `next_page` to paginate as usual.

- `group_by: Array[:claude_tag_category | :claude_tag_user_id | :context_window | 8 more]`

  Break each actor's row out by the given dimensions. Accepts the same values as the bucketed `/cost_report` endpoint. The `product`, `model`, `context_window`, `inference_geo`, and `speed` dimensions — and the time bucket, when `bucket_width` is set — count toward `limit`. `cost_type` and `token_type` do not: `cost_type` returns one row per cost component (tokens, web search, code execution); `token_type` returns one row per token type, each with `cost_type: "tokens"`; combining both returns the per-token-type rows plus the web-search and code-execution rows. A page can therefore contain more rows than `limit` when `cost_type` or `token_type` is requested.

  maxItems: 100

  - `:claude_tag_category`

  - `:claude_tag_user_id`

  - `:context_window`

  - `:cost_type`

  - `:inference_geo`

  - `:model`

  - `:product`

  - `:rbac_group_id`

  - `:slack_channel_id`

  - `:speed`

  - `:token_type`

- `inference_geos: Array[BetaAnalyticsInferenceGeoFilter]`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  maxItems: 100

  - `:global`

  - `:not_available`

  - `:us`

- `limit: Integer`

  Number of rows per page (1-1000, default 20). One row per actor unless `group_by[]` or `bucket_width` splits an actor across rows; `cost_type`/`token_type` fan-out rows (cost endpoint only) are the exception — they do not count toward this limit, so `data` can exceed it.

  minimum: 1, maximum: 1000

- `models: Array[String]`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

  maxItems: 100

- `order: :asc | :desc`

  Sort direction. Defaults to `desc`.

  - `:asc`

  - `:desc`

- `order_by: :amount | :list_amount`

  Metric to rank actors by. Defaults to `amount`.

  - `:amount`

  - `:list_amount`

- `page: String`

  Opaque cursor from a previous response's `next_page` field.

- `products: Array[BetaAnalyticsProductFilter]`

  Product surfaces to include. Defaults to all products.

  maxItems: 100

  - `:chat`

  - `:"claude-tag"`

  - `:claude_code`

  - `:claude_design`

  - `:claude_in_chrome`

  - `:cowork`

  - `:office_agent`

- `rbac_group_ids: Array[String]`

  Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

  maxItems: 100

- `slack_channel_ids: Array[String]`

  Filter to usage originating from specific Slack channels. Use `group_by[]=slack_channel_id` to break out per-channel values.

  maxItems: 100

- `speeds: Array[:fast | :standard]`

  Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

  maxItems: 100

  - `:fast`

  - `:standard`

- `user_ids: Array[String]`

  Filter to specific users by tagged user ID.

  maxItems: 100

#### Returns

- `class BetaAnalyticsCostUsersItem`

  - `actor: BetaAnalyticsUserActor`

    The user this row's usage or cost is attributed to. Always a `user_actor`.

    - `type: :user_actor`

      Actor type. Always `"user_actor"`.

    - `deleted: bool`

      True when the account has been deleted, or when the user is no longer a member of the organization or its associated organizations (for example, their membership was removed or they were deprovisioned via your identity provider). `email_address` stays populated for removed users and is null when the account has been deleted. `name` follows the rules described on that field. The `user_id` is still populated for reconciliation.

    - `email_address: String`

      The user's email address, including for users who are no longer members of the organization or its associated organizations. Null when the account has been deleted (check `deleted`) and for system-minted service accounts, which have no person's mailbox behind them (check `name`).

    - `name: String`

      The user's full name. Null when the user has not set a name. Returns `"Deleted User"` when the account itself has been deleted, or when the user is no longer a member of the organization or its associated organizations and the organization has chosen to hide the names of removed users. Otherwise, the name stays populated for removed users. Rows for system-minted service accounts render the service name (for example, `"Claude Security"` for usage by Anthropic's security-patching service) or null.

    - `user_id: String`

      Tagged user ID.

  - `amount: String`

    Amount (post-discount, pre-credit) in fractional cents (minor units).

  - `claude_tag_category: BetaAnalyticsClaudeTagCategory`

    Claude Tag (Claude in Slack) spend category: `engaged` (a person addressed Claude in a channel or thread), `proactive` (Claude responded without being addressed), `scheduled` (a scheduled routine ran), `monitoring` (Claude watching a channel it was asked to monitor), or `dm` (direct messages with Claude). Populated only when `claude_tag_category` is in `group_by[]`; null for usage that is not Claude Tag. Direct-message usage is billed to the individual user and is reported under that user's product, not under `claude-tag`. New categories may be added over time.

    - `:dm`

    - `:engaged`

    - `:monitoring`

    - `:proactive`

    - `:scheduled`

  - `claude_tag_user_id: String`

    Slack user ID (for example `U0123ABCDEF`) of the member the Claude Tag (Claude in Slack) usage is attributed to, not a claude.ai user ID. Populated only when `claude_tag_user_id` is in `group_by[]`; null for usage that is not Claude Tag and for Claude Tag usage that is not attributed to a single user (for example `monitoring`, and `proactive` usage Claude initiated), so per-user rows can sum to less than the Claude Tag total. Cannot be combined with `group_by[]=rbac_group_id` or the `rbac_group_ids[]` filter.

  - `context_window: BetaAnalyticsContextWindow`

    Context-window pricing tier of the usage or cost. Null unless `context_window` is in `group_by[]`; it can also be null on grouped rows with no context-window tier, such as code execution.

    - `:"0-200k"`

    - `:"200k-1M"`

  - `cost_type: BetaAnalyticsCostType`

    Cost component breakdown; null when returning the combined total.

    - `:code_execution`

    - `:tokens`

    - `:web_search`

  - `currency: String`

    Currency code for the cost amount. Currently always `"USD"`.

  - `ending_at: Time`

    End of the row's UTC time bucket (exclusive), as an RFC 3339 timestamp; equal to `starting_at` plus one `bucket_width`. Null unless `bucket_width` is set.

    format: date-time

  - `inference_geo: :global | :us`

    Inference region of the usage or cost. Null unless `inference_geo` is in `group_by[]`; it can also be null on grouped rows where the region is not set (the rows that `inference_geos[]=not_available` matches).

    - `:global`

    - `:us`

  - `list_amount: String`

    List-price amount (pre-discount) in fractional cents.

  - `model: String`

    Model that produced the usage or cost, as a model name in the form the `models[]` filter accepts (for example, `claude-opus-5`). Null unless `model` is in `group_by[]`; it can also be null on grouped rows whose usage or cost is not attributed to a specific model, such as code execution.

  - `product: String`

    Product surface that produced the usage or cost. Null unless product is in `group_by[]`; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include `chat`, `claude_code`, `cowork`, `office_agent`, `claude_in_chrome`, `claude_design`, and `claude-tag`. `claude-tag` is Claude Tag, the Claude product in Slack. Some unattributed usage is reported as "other".

  - `rbac_group_id: String`

    RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has one id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query without `group_by[]`.

  - `requests: Integer`

    Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

  - `slack_channel_id: String`

    Slack channel the usage originated from. Populated only when `slack_channel_id` is in `group_by[]`; null for usage outside Slack (and for rows recorded before channel attribution was enabled).

  - `speed: :fast | :standard`

    Inference speed mode of the usage or cost: `fast` or `standard`. Null unless `speed` is in `group_by[]`.

    - `:fast`

    - `:standard`

  - `starting_at: Time`

    Start of the row's UTC time bucket (inclusive), as an RFC 3339 timestamp. Null unless `bucket_width` is set; without `bucket_width`, each row aggregates the full requested range.

    format: date-time

  - `token_type: BetaAnalyticsTokenType`

    Token type when `cost_type` is `tokens`; null otherwise.

    - `:"cache_creation.ephemeral_1h_input_tokens"`

    - `:"cache_creation.ephemeral_5m_input_tokens"`

    - `:cache_read_input_tokens`

    - `:output_tokens`

    - `:uncached_input_tokens`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.analytics.user_cost_report.list(starting_at: "2019-12-27T18:11:19.117Z")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "actor": {
        "deleted": true,
        "email": "jane@example.com",
        "email_address": "jane@example.com",
        "name": "Jane Smith",
        "type": "user_actor",
        "user_id": "user_01AbCdEfGhIjKlMnOpQrSt"
      },
      "amount": "41280.000000",
      "claude_tag_category": "dm",
      "claude_tag_user_id": "U0123ABCDEF",
      "context_window": "0-200k",
      "cost_type": "code_execution",
      "currency": "USD",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "list_amount": "51600.000000",
      "model": "claude-opus-5",
      "product": "chat",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "requests": 128,
      "slack_channel_id": "C0123ABCDEF",
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "token_type": "cache_creation.ephemeral_1h_input_tokens"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

## Beta › Organization › Spend Limits

### Set Spend Limit

`beta.organization.spend_limits.set(**kwargs) -> BetaSpendLimit`

**POST** `/v1/organizations/spend_limits`

Set a spend limit.

Upsert keyed on (scope, period): setting a limit that already exists
overwrites it in place. A Claude Enterprise organization sets `user`
limits. Its seat-tier, group, and organization-level defaults are configured
in claude.ai. A Claude Console organization sets `organization` and
`workspace` limits, which are monthly and always carry an amount. Setting those
limits is in an early access preview. To request access, contact your
Anthropic account team.

#### Parameters

- `amount: String`

  Limit amount as a non-negative integer decimal string in the minor unit of the organization's billing currency (cents for USD): "50000" is $500.00. `null` sets an explicit no-limit override for this scope and `period` only — each period resolves independently, so caps for other periods still apply.

- `scope: BetaSpendLimitUserScope | BetaSpendLimitOrganizationScope | BetaSpendLimitWorkspaceScope`

  What the limit applies to. Claude Enterprise organizations set `user` limits. Claude Console organizations set `organization` and `workspace` limits. Any other combination returns 400. Setting `organization` and `workspace` limits through the API is in an early access preview. To request access, contact your Anthropic account team.

  - `class BetaSpendLimitUserScope`

    Scope selecting a single member of the organization.

    - `type: :user`

      Scope type. Always `user` for this scope.

    - `user_id: String`

      Tagged ID of the member the spend limit applies to.

  - `class BetaSpendLimitOrganizationScope`

    - `type: :organization`

  - `class BetaSpendLimitWorkspaceScope`

    Scope selecting one workspace of a Claude Console organization.

    - `type: :workspace`

      Scope type. Always `workspace` for this scope.

    - `workspace_id: String`

      Tagged ID of the workspace the spend limit applies to.

- `period: BetaSpendLimitPeriod`

  - `:daily`

  - `:monthly`

  - `:weekly`

#### Returns

- `class BetaSpendLimit`

  A configured spend limit: a cap on metered spend for one scope and period.

  - `type: :spend_limit`

    Object type. Always `spend_limit`.

  - `id: String`

    Unique tagged ID of the spend limit (`spl_...`).

  - `amount: String`

    Limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD): "50000" is $500.00. `null` means no numeric cap is configured at this scope — see the effective report for whether a limit applies.

  - `created_at: Time`

    RFC 3339 datetime at which the spend limit was created.

    format: date-time

  - `currency: String`

    ISO 4217 code of the organization's billing currency; the unit for `amount`.

  - `is_enabled: bool`

    Read-only. `false` when extra usage is switched off for this organization (`organization` limit) or for this member (`user` limit); `amount` is kept and applies again when it's switched back on. Always `true` for other limits.

  - `period: BetaSpendLimitPeriod`

    Length of the window the limit resets over. `amount` caps spend within each period.

    - `:daily`

    - `:monthly`

    - `:weekly`

  - `scope: BetaSpendLimitUserScope | BetaSpendLimitSeatTierScope | BetaSpendLimitRBACGroupScope | 3 more`

    What the limit applies to. A tagged union on `type`; each variant carries the identifier for its scope.

    - `class BetaSpendLimitUserScope`

      Scope selecting a single member of the organization.

      - `type: :user`

        Scope type. Always `user` for this scope.

      - `user_id: String`

        Tagged ID of the member the spend limit applies to.

    - `class BetaSpendLimitSeatTierScope`

      - `type: :seat_tier`

      - `seat_tier: String`

    - `class BetaSpendLimitRBACGroupScope`

      - `type: :rbac_group`

      - `rbac_group_id: String`

    - `class BetaSpendLimitOrganizationServiceScope`

      - `type: :organization_service`

      - `service: String`

    - `class BetaSpendLimitOrganizationScope`

      - `type: :organization`

    - `class BetaSpendLimitWorkspaceScope`

      Scope selecting one workspace of a Claude Console organization.

      - `type: :workspace`

        Scope type. Always `workspace` for this scope.

      - `workspace_id: String`

        Tagged ID of the workspace the spend limit applies to.

  - `updated_at: Time`

    RFC 3339 datetime at which the spend limit was last modified.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_spend_limit = anthropic.beta.organization.spend_limits.set(
  amount: "50000",
  scope: {type: :user, user_id: "user_01WCz1FkmYMm4gnmykNKUu3Q"}
)

puts(beta_spend_limit)
```

##### Response (200)

```json
{
  "id": "id",
  "amount": "50000",
  "created_at": "2019-12-27T18:11:19.117Z",
  "currency": "USD",
  "is_enabled": true,
  "period": "daily",
  "scope": {
    "type": "user",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "type": "spend_limit",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

### Get Spend Limit

`beta.organization.spend_limits.retrieve(spend_limit_id) -> BetaSpendLimit`

**GET** `/v1/organizations/spend_limits/{spend_limit_id}`

Retrieve a spend limit by ID.

#### Parameters

- `spend_limit_id: String`

  ID of the Spend Limit.

#### Returns

- `class BetaSpendLimit`

  A configured spend limit: a cap on metered spend for one scope and period.

  - `type: :spend_limit`

    Object type. Always `spend_limit`.

  - `id: String`

    Unique tagged ID of the spend limit (`spl_...`).

  - `amount: String`

    Limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD): "50000" is $500.00. `null` means no numeric cap is configured at this scope — see the effective report for whether a limit applies.

  - `created_at: Time`

    RFC 3339 datetime at which the spend limit was created.

    format: date-time

  - `currency: String`

    ISO 4217 code of the organization's billing currency; the unit for `amount`.

  - `is_enabled: bool`

    Read-only. `false` when extra usage is switched off for this organization (`organization` limit) or for this member (`user` limit); `amount` is kept and applies again when it's switched back on. Always `true` for other limits.

  - `period: BetaSpendLimitPeriod`

    Length of the window the limit resets over. `amount` caps spend within each period.

    - `:daily`

    - `:monthly`

    - `:weekly`

  - `scope: BetaSpendLimitUserScope | BetaSpendLimitSeatTierScope | BetaSpendLimitRBACGroupScope | 3 more`

    What the limit applies to. A tagged union on `type`; each variant carries the identifier for its scope.

    - `class BetaSpendLimitUserScope`

      Scope selecting a single member of the organization.

      - `type: :user`

        Scope type. Always `user` for this scope.

      - `user_id: String`

        Tagged ID of the member the spend limit applies to.

    - `class BetaSpendLimitSeatTierScope`

      - `type: :seat_tier`

      - `seat_tier: String`

    - `class BetaSpendLimitRBACGroupScope`

      - `type: :rbac_group`

      - `rbac_group_id: String`

    - `class BetaSpendLimitOrganizationServiceScope`

      - `type: :organization_service`

      - `service: String`

    - `class BetaSpendLimitOrganizationScope`

      - `type: :organization`

    - `class BetaSpendLimitWorkspaceScope`

      Scope selecting one workspace of a Claude Console organization.

      - `type: :workspace`

        Scope type. Always `workspace` for this scope.

      - `workspace_id: String`

        Tagged ID of the workspace the spend limit applies to.

  - `updated_at: Time`

    RFC 3339 datetime at which the spend limit was last modified.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_spend_limit = anthropic.beta.organization.spend_limits.retrieve("spend_limit_id")

puts(beta_spend_limit)
```

##### Response (200)

```json
{
  "id": "id",
  "amount": "50000",
  "created_at": "2019-12-27T18:11:19.117Z",
  "currency": "USD",
  "is_enabled": true,
  "period": "daily",
  "scope": {
    "type": "user",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "type": "spend_limit",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

### Delete Spend Limit

`beta.organization.spend_limits.delete(spend_limit_id) -> SpendLimitDeleteResponse`

**DELETE** `/v1/organizations/spend_limits/{spend_limit_id}`

Delete a spend limit.

For a Claude Enterprise organization, this deletes a per-user override, and
the member falls back to any inherited spend limit at that period. Its
seat-tier, group, and organization-level rows cannot be deleted via this
endpoint. A Claude Console organization deletes its organization and
workspace limits. Deleting them through the API is in an early access preview.

#### Parameters

- `spend_limit_id: String`

  ID of the Spend Limit.

#### Returns

- `class SpendLimitDeleteResponse`

  - `type: :spend_limit_deleted`

  - `id: String`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

spend_limit = anthropic.beta.organization.spend_limits.delete("spend_limit_id")

puts(spend_limit)
```

##### Response (200)

```json
{
  "id": "id",
  "type": "spend_limit_deleted"
}
```

### List Spend Limits

`beta.organization.spend_limits.list(**kwargs) -> PageCursor<BetaSpendLimit>`

**GET** `/v1/organizations/spend_limits`

List the organization's spend limits.

A Claude Console organization's limits come in an order that is stable across
pages. A Claude Enterprise organization's are grouped by scope type,
in the order `organization`, `seat_tier`, `rbac_group`,
`organization_service`, `user`; within a type they come in a fixed order that
is not creation order.

#### Parameters

- `limit: Integer`

  Maximum number of limits per page. Defaults to `20`.

  minimum: 1, maximum: 1000

- `page: String`

  Opaque cursor from a previous response's `next_page` field.

- `scope_type: Array[:organization | :organization_service | :rbac_group | 3 more]`

  Return only limits with these scope types. A Claude Console organization has `organization` and `workspace` limits; a Claude Enterprise organization has `organization`, `seat_tier`, `rbac_group`, `organization_service` and `user` limits. Omit for all.

  maxItems: 6

  - `:organization`

  - `:organization_service`

  - `:rbac_group`

  - `:seat_tier`

  - `:user`

  - `:workspace`

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `spend-limit-reads-2026-09-26` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaSpendLimit`

  A configured spend limit: a cap on metered spend for one scope and period.

  - `type: :spend_limit`

    Object type. Always `spend_limit`.

  - `id: String`

    Unique tagged ID of the spend limit (`spl_...`).

  - `amount: String`

    Limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD): "50000" is $500.00. `null` means no numeric cap is configured at this scope — see the effective report for whether a limit applies.

  - `created_at: Time`

    RFC 3339 datetime at which the spend limit was created.

    format: date-time

  - `currency: String`

    ISO 4217 code of the organization's billing currency; the unit for `amount`.

  - `is_enabled: bool`

    Read-only. `false` when extra usage is switched off for this organization (`organization` limit) or for this member (`user` limit); `amount` is kept and applies again when it's switched back on. Always `true` for other limits.

  - `period: BetaSpendLimitPeriod`

    Length of the window the limit resets over. `amount` caps spend within each period.

    - `:daily`

    - `:monthly`

    - `:weekly`

  - `scope: BetaSpendLimitUserScope | BetaSpendLimitSeatTierScope | BetaSpendLimitRBACGroupScope | 3 more`

    What the limit applies to. A tagged union on `type`; each variant carries the identifier for its scope.

    - `class BetaSpendLimitUserScope`

      Scope selecting a single member of the organization.

      - `type: :user`

        Scope type. Always `user` for this scope.

      - `user_id: String`

        Tagged ID of the member the spend limit applies to.

    - `class BetaSpendLimitSeatTierScope`

      - `type: :seat_tier`

      - `seat_tier: String`

    - `class BetaSpendLimitRBACGroupScope`

      - `type: :rbac_group`

      - `rbac_group_id: String`

    - `class BetaSpendLimitOrganizationServiceScope`

      - `type: :organization_service`

      - `service: String`

    - `class BetaSpendLimitOrganizationScope`

      - `type: :organization`

    - `class BetaSpendLimitWorkspaceScope`

      Scope selecting one workspace of a Claude Console organization.

      - `type: :workspace`

        Scope type. Always `workspace` for this scope.

      - `workspace_id: String`

        Tagged ID of the workspace the spend limit applies to.

  - `updated_at: Time`

    RFC 3339 datetime at which the spend limit was last modified.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.spend_limits.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "amount": "50000",
      "created_at": "2019-12-27T18:11:19.117Z",
      "currency": "USD",
      "is_enabled": true,
      "period": "daily",
      "scope": {
        "type": "user",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "type": "spend_limit",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Spend Limits › Effective

### List Effective Spend Limits

`beta.organization.spend_limits.effective.list(**kwargs) -> PageCursor<BetaSpendSummary>`

**GET** `/v1/organizations/spend_limits/effective`

List each member's effective spend limit and period-to-date spend.

Returns one row per (member, period) the member resolves a spend limit
for, with the `source` scope the spend limit was inherited from.
Paginates by member, so a member's periods never split across pages.

#### Parameters

- `limit: Integer`

  Maximum number of members per page. A member's period rows never split across pages, so a page may carry more rows than this. Defaults to `20`.

  minimum: 1, maximum: 1000

- `page: String`

  Opaque cursor from a previous response's `next_page` field.

- `period: Array[:daily | :monthly | :weekly]`

  Restrict the report to these limit periods. Omit to return one row per period each member resolves a spend limit for.

  maxItems: 3

  - `:daily`

  - `:monthly`

  - `:weekly`

- `user_ids: Array[String]`

  Restrict the report to these members, by tagged user ID (`user_...`). At most 100 entries.

  maxItems: 100

#### Returns

- `class BetaSpendSummary`

  Per-member effective-limit report row (`GET /spend_limits/effective`).

  - `actor: BetaSpendLimitUserActor | BetaSpendLimitScopedAPIKeyActor`

    - `class BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `type: :user_actor`

        Actor type. Always `user_actor`.

      - `deleted: bool`

        True only when the underlying account has been deleted.

      - `email_address: String`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `name: String`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `user_id: String`

        Tagged ID of the user.

    - `class BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

      - `type: :scoped_api_key_actor`

      - `scoped_api_key_id: String`

  - `amount: String`

    Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

  - `currency: String`

    ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

  - `period: BetaSpendLimitPeriod`

    Period this row's effective limit and spend are reported for.

    - `:daily`

    - `:monthly`

    - `:weekly`

  - `period_to_date_spend: String`

    The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

  - `scope: BetaSpendLimitUserScope | BetaSpendLimitSeatTierScope | BetaSpendLimitRBACGroupScope | 3 more`

    - `class BetaSpendLimitUserScope`

      Scope selecting a single member of the organization.

      - `type: :user`

        Scope type. Always `user` for this scope.

      - `user_id: String`

        Tagged ID of the member the spend limit applies to.

    - `class BetaSpendLimitSeatTierScope`

      - `type: :seat_tier`

      - `seat_tier: String`

    - `class BetaSpendLimitRBACGroupScope`

      - `type: :rbac_group`

      - `rbac_group_id: String`

    - `class BetaSpendLimitOrganizationServiceScope`

      - `type: :organization_service`

      - `service: String`

    - `class BetaSpendLimitOrganizationScope`

      - `type: :organization`

    - `class BetaSpendLimitWorkspaceScope`

      Scope selecting one workspace of a Claude Console organization.

      - `type: :workspace`

        Scope type. Always `workspace` for this scope.

      - `workspace_id: String`

        Tagged ID of the workspace the spend limit applies to.

  - `source: BetaSpendLimitUserScope | BetaSpendLimitSeatTierScope | BetaSpendLimitRBACGroupScope | 3 more`

    - `class BetaSpendLimitUserScope`

      Scope selecting a single member of the organization.

    - `class BetaSpendLimitSeatTierScope`

    - `class BetaSpendLimitRBACGroupScope`

    - `class BetaSpendLimitOrganizationServiceScope`

    - `class BetaSpendLimitOrganizationScope`

    - `class BetaSpendLimitWorkspaceScope`

      Scope selecting one workspace of a Claude Console organization.

  - `spend_limit_id: String`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.spend_limits.effective.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "amount": "50000",
      "currency": "USD",
      "period": "daily",
      "period_to_date_spend": "12050.5",
      "scope": {
        "type": "user",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "source": {
        "type": "user",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "spend_limit_id": "spend_limit_id"
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Spend Limits › Increase Requests

### List Spend Limit Increase Requests

`beta.organization.spend_limits.increase_requests.list(**kwargs) -> PageCursor<BetaSpendLimitIncreaseRequest>`

**GET** `/v1/organizations/spend_limit_increase_requests`

List spend limit increase requests, most recent first.

Pending requests include a live `spend_summary` for the requester.
Requests whose requester is no longer a member are excluded.

#### Parameters

- `actor_ids: Array[String]`

  Filter by requester, as `user_...` tagged IDs.

- `limit: Integer`

  minimum: 1, maximum: 1000

- `page: String`

  Opaque cursor from a previous response's `next_page`.

- `status: Array[BetaSpendLimitIncreaseRequestStatus]`

  Filter by status. Omit to return all.

  - `:approved`

  - `:denied`

  - `:pending`

#### Returns

- `class BetaSpendLimitIncreaseRequest`

  - `type: :spend_limit_increase_request`

  - `id: String`

  - `actor: BetaSpendLimitUserActor | BetaSpendLimitScopedAPIKeyActor`

    - `class BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `type: :user_actor`

        Actor type. Always `user_actor`.

      - `deleted: bool`

        True only when the underlying account has been deleted.

      - `email_address: String`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `name: String`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `user_id: String`

        Tagged ID of the user.

    - `class BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

      - `type: :scoped_api_key_actor`

      - `scoped_api_key_id: String`

  - `created_at: Time`

    format: date-time

  - `period: BetaSpendLimitPeriod`

    - `:daily`

    - `:monthly`

    - `:weekly`

  - `resolved_at: Time`

    format: date-time

  - `resolved_by: BetaSpendLimitUserActor | BetaSpendLimitScopedAPIKeyActor`

    - `class BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

    - `class BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

  - `spend_summary: BetaSpendSummary`

    Per-member effective-limit report row (`GET /spend_limits/effective`).

    - `actor: BetaSpendLimitUserActor | BetaSpendLimitScopedAPIKeyActor`

      - `class BetaSpendLimitUserActor`

        A user within the organization. `name` and `email_address` are
        null when the underlying account is unavailable or has been deleted;
        `deleted` is true only for deleted accounts.

      - `class BetaSpendLimitScopedAPIKeyActor`

        A scoped Admin API key acting on behalf of the organization.

    - `amount: String`

      Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

    - `currency: String`

      ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

    - `period: BetaSpendLimitPeriod`

      Period this row's effective limit and spend are reported for.

    - `period_to_date_spend: String`

      The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

    - `scope: BetaSpendLimitUserScope | BetaSpendLimitSeatTierScope | BetaSpendLimitRBACGroupScope | 3 more`

      - `class BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

        - `type: :user`

          Scope type. Always `user` for this scope.

        - `user_id: String`

          Tagged ID of the member the spend limit applies to.

      - `class BetaSpendLimitSeatTierScope`

        - `type: :seat_tier`

        - `seat_tier: String`

      - `class BetaSpendLimitRBACGroupScope`

        - `type: :rbac_group`

        - `rbac_group_id: String`

      - `class BetaSpendLimitOrganizationServiceScope`

        - `type: :organization_service`

        - `service: String`

      - `class BetaSpendLimitOrganizationScope`

        - `type: :organization`

      - `class BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

        - `type: :workspace`

          Scope type. Always `workspace` for this scope.

        - `workspace_id: String`

          Tagged ID of the workspace the spend limit applies to.

    - `source: BetaSpendLimitUserScope | BetaSpendLimitSeatTierScope | BetaSpendLimitRBACGroupScope | 3 more`

      - `class BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

      - `class BetaSpendLimitSeatTierScope`

      - `class BetaSpendLimitRBACGroupScope`

      - `class BetaSpendLimitOrganizationServiceScope`

      - `class BetaSpendLimitOrganizationScope`

      - `class BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

    - `spend_limit_id: String`

  - `status: BetaSpendLimitIncreaseRequestStatus`

    - `:approved`

    - `:denied`

    - `:pending`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.spend_limits.increase_requests.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "period": "daily",
      "resolved_at": "2019-12-27T18:11:19.117Z",
      "resolved_by": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "spend_summary": {
        "actor": {
          "deleted": true,
          "email_address": "email_address",
          "name": "name",
          "type": "user_actor",
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        },
        "amount": "50000",
        "currency": "USD",
        "period": "daily",
        "period_to_date_spend": "12050.5",
        "scope": {
          "type": "user",
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        },
        "source": {
          "type": "user",
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        },
        "spend_limit_id": "spend_limit_id"
      },
      "status": "approved",
      "type": "spend_limit_increase_request"
    }
  ],
  "next_page": "next_page"
}
```

### Get Spend Limit Increase Request

`beta.organization.spend_limits.increase_requests.retrieve(spend_limit_increase_request_id) -> BetaSpendLimitIncreaseRequest`

**GET** `/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}`

Retrieve a spend limit increase request.

While `pending`, the response includes a live `spend_summary` for the
requester at the request's period.

#### Parameters

- `spend_limit_increase_request_id: String`

  ID of the spend limit increase request.

#### Returns

- `class BetaSpendLimitIncreaseRequest`

  - `type: :spend_limit_increase_request`

  - `id: String`

  - `actor: BetaSpendLimitUserActor | BetaSpendLimitScopedAPIKeyActor`

    - `class BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `type: :user_actor`

        Actor type. Always `user_actor`.

      - `deleted: bool`

        True only when the underlying account has been deleted.

      - `email_address: String`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `name: String`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `user_id: String`

        Tagged ID of the user.

    - `class BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

      - `type: :scoped_api_key_actor`

      - `scoped_api_key_id: String`

  - `created_at: Time`

    format: date-time

  - `period: BetaSpendLimitPeriod`

    - `:daily`

    - `:monthly`

    - `:weekly`

  - `resolved_at: Time`

    format: date-time

  - `resolved_by: BetaSpendLimitUserActor | BetaSpendLimitScopedAPIKeyActor`

    - `class BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

    - `class BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

  - `spend_summary: BetaSpendSummary`

    Per-member effective-limit report row (`GET /spend_limits/effective`).

    - `actor: BetaSpendLimitUserActor | BetaSpendLimitScopedAPIKeyActor`

      - `class BetaSpendLimitUserActor`

        A user within the organization. `name` and `email_address` are
        null when the underlying account is unavailable or has been deleted;
        `deleted` is true only for deleted accounts.

      - `class BetaSpendLimitScopedAPIKeyActor`

        A scoped Admin API key acting on behalf of the organization.

    - `amount: String`

      Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

    - `currency: String`

      ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

    - `period: BetaSpendLimitPeriod`

      Period this row's effective limit and spend are reported for.

    - `period_to_date_spend: String`

      The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

    - `scope: BetaSpendLimitUserScope | BetaSpendLimitSeatTierScope | BetaSpendLimitRBACGroupScope | 3 more`

      - `class BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

        - `type: :user`

          Scope type. Always `user` for this scope.

        - `user_id: String`

          Tagged ID of the member the spend limit applies to.

      - `class BetaSpendLimitSeatTierScope`

        - `type: :seat_tier`

        - `seat_tier: String`

      - `class BetaSpendLimitRBACGroupScope`

        - `type: :rbac_group`

        - `rbac_group_id: String`

      - `class BetaSpendLimitOrganizationServiceScope`

        - `type: :organization_service`

        - `service: String`

      - `class BetaSpendLimitOrganizationScope`

        - `type: :organization`

      - `class BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

        - `type: :workspace`

          Scope type. Always `workspace` for this scope.

        - `workspace_id: String`

          Tagged ID of the workspace the spend limit applies to.

    - `source: BetaSpendLimitUserScope | BetaSpendLimitSeatTierScope | BetaSpendLimitRBACGroupScope | 3 more`

      - `class BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

      - `class BetaSpendLimitSeatTierScope`

      - `class BetaSpendLimitRBACGroupScope`

      - `class BetaSpendLimitOrganizationServiceScope`

      - `class BetaSpendLimitOrganizationScope`

      - `class BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

    - `spend_limit_id: String`

  - `status: BetaSpendLimitIncreaseRequestStatus`

    - `:approved`

    - `:denied`

    - `:pending`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_spend_limit_increase_request = anthropic.beta.organization.spend_limits.increase_requests.retrieve("spend_limit_increase_request_id")

puts(beta_spend_limit_increase_request)
```

##### Response (200)

```json
{
  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "daily",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "daily",
    "period_to_date_spend": "12050.5",
    "scope": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "source": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "spend_limit_id": "spend_limit_id"
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
}
```

### Approve Spend Limit Increase Request

`beta.organization.spend_limits.increase_requests.approve(spend_limit_increase_request_id, **kwargs) -> IncreaseRequestApproveResponse`

**POST** `/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve`

Approve a pending spend limit increase request.

Writes a per-user spend limit at `amount` for the requester and
transitions the request to `approved`. `period` defaults to the period
the member was blocked on. Anthropic emails the requester unless
`suppress_notification` is set.

#### Parameters

- `spend_limit_increase_request_id: String`

  ID of the spend limit increase request.

- `amount: String`

  New per-user spend limit as a non-negative integer decimal string (minor units).

- `period: BetaSpendLimitPeriod`

  - `:daily`

  - `:monthly`

  - `:weekly`

- `suppress_notification: bool`

#### Returns

- `class IncreaseRequestApproveResponse`

  - `type: :spend_limit_increase_request`

  - `id: String`

  - `actor: BetaSpendLimitUserActor | BetaSpendLimitScopedAPIKeyActor`

    - `class BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `type: :user_actor`

        Actor type. Always `user_actor`.

      - `deleted: bool`

        True only when the underlying account has been deleted.

      - `email_address: String`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `name: String`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `user_id: String`

        Tagged ID of the user.

    - `class BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

      - `type: :scoped_api_key_actor`

      - `scoped_api_key_id: String`

  - `created_at: Time`

    format: date-time

  - `period: BetaSpendLimitPeriod`

    - `:daily`

    - `:monthly`

    - `:weekly`

  - `resolved_at: Time`

    format: date-time

  - `resolved_by: BetaSpendLimitUserActor | BetaSpendLimitScopedAPIKeyActor`

    - `class BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

    - `class BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

  - `spend_limit: BetaSpendLimit`

    A configured spend limit: a cap on metered spend for one scope and period.

    - `type: :spend_limit`

      Object type. Always `spend_limit`.

    - `id: String`

      Unique tagged ID of the spend limit (`spl_...`).

    - `amount: String`

      Limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD): "50000" is $500.00. `null` means no numeric cap is configured at this scope — see the effective report for whether a limit applies.

    - `created_at: Time`

      RFC 3339 datetime at which the spend limit was created.

      format: date-time

    - `currency: String`

      ISO 4217 code of the organization's billing currency; the unit for `amount`.

    - `is_enabled: bool`

      Read-only. `false` when extra usage is switched off for this organization (`organization` limit) or for this member (`user` limit); `amount` is kept and applies again when it's switched back on. Always `true` for other limits.

    - `period: BetaSpendLimitPeriod`

      Length of the window the limit resets over. `amount` caps spend within each period.

    - `scope: BetaSpendLimitUserScope | BetaSpendLimitSeatTierScope | BetaSpendLimitRBACGroupScope | 3 more`

      What the limit applies to. A tagged union on `type`; each variant carries the identifier for its scope.

      - `class BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

        - `type: :user`

          Scope type. Always `user` for this scope.

        - `user_id: String`

          Tagged ID of the member the spend limit applies to.

      - `class BetaSpendLimitSeatTierScope`

        - `type: :seat_tier`

        - `seat_tier: String`

      - `class BetaSpendLimitRBACGroupScope`

        - `type: :rbac_group`

        - `rbac_group_id: String`

      - `class BetaSpendLimitOrganizationServiceScope`

        - `type: :organization_service`

        - `service: String`

      - `class BetaSpendLimitOrganizationScope`

        - `type: :organization`

      - `class BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

        - `type: :workspace`

          Scope type. Always `workspace` for this scope.

        - `workspace_id: String`

          Tagged ID of the workspace the spend limit applies to.

    - `updated_at: Time`

      RFC 3339 datetime at which the spend limit was last modified.

      format: date-time

  - `spend_summary: BetaSpendSummary`

    Per-member effective-limit report row (`GET /spend_limits/effective`).

    - `actor: BetaSpendLimitUserActor | BetaSpendLimitScopedAPIKeyActor`

      - `class BetaSpendLimitUserActor`

        A user within the organization. `name` and `email_address` are
        null when the underlying account is unavailable or has been deleted;
        `deleted` is true only for deleted accounts.

      - `class BetaSpendLimitScopedAPIKeyActor`

        A scoped Admin API key acting on behalf of the organization.

    - `amount: String`

      Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

    - `currency: String`

      ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

    - `period: BetaSpendLimitPeriod`

      Period this row's effective limit and spend are reported for.

    - `period_to_date_spend: String`

      The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

    - `scope: BetaSpendLimitUserScope | BetaSpendLimitSeatTierScope | BetaSpendLimitRBACGroupScope | 3 more`

      - `class BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

      - `class BetaSpendLimitSeatTierScope`

      - `class BetaSpendLimitRBACGroupScope`

      - `class BetaSpendLimitOrganizationServiceScope`

      - `class BetaSpendLimitOrganizationScope`

      - `class BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

    - `source: BetaSpendLimitUserScope | BetaSpendLimitSeatTierScope | BetaSpendLimitRBACGroupScope | 3 more`

      - `class BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

      - `class BetaSpendLimitSeatTierScope`

      - `class BetaSpendLimitRBACGroupScope`

      - `class BetaSpendLimitOrganizationServiceScope`

      - `class BetaSpendLimitOrganizationScope`

      - `class BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

    - `spend_limit_id: String`

  - `status: BetaSpendLimitIncreaseRequestStatus`

    - `:approved`

    - `:denied`

    - `:pending`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

response = anthropic.beta.organization.spend_limits.increase_requests.approve(
  "spend_limit_increase_request_id",
  amount: "50000"
)

puts(response)
```

##### Response (200)

```json
{
  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "daily",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "spend_limit": {
    "id": "id",
    "amount": "50000",
    "created_at": "2019-12-27T18:11:19.117Z",
    "currency": "USD",
    "is_enabled": true,
    "period": "daily",
    "scope": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "type": "spend_limit",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "daily",
    "period_to_date_spend": "12050.5",
    "scope": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "source": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "spend_limit_id": "spend_limit_id"
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
}
```

### Deny Spend Limit Increase Request

`beta.organization.spend_limits.increase_requests.deny(spend_limit_increase_request_id, **kwargs) -> BetaSpendLimitIncreaseRequest`

**POST** `/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny`

Deny a pending spend limit increase request.

Idempotent on `denied`; denying an already-`approved` request returns
400. Anthropic emails the requester unless `suppress_notification` is set.

#### Parameters

- `spend_limit_increase_request_id: String`

  ID of the spend limit increase request.

- `suppress_notification: bool`

#### Returns

- `class BetaSpendLimitIncreaseRequest`

  - `type: :spend_limit_increase_request`

  - `id: String`

  - `actor: BetaSpendLimitUserActor | BetaSpendLimitScopedAPIKeyActor`

    - `class BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `type: :user_actor`

        Actor type. Always `user_actor`.

      - `deleted: bool`

        True only when the underlying account has been deleted.

      - `email_address: String`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `name: String`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `user_id: String`

        Tagged ID of the user.

    - `class BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

      - `type: :scoped_api_key_actor`

      - `scoped_api_key_id: String`

  - `created_at: Time`

    format: date-time

  - `period: BetaSpendLimitPeriod`

    - `:daily`

    - `:monthly`

    - `:weekly`

  - `resolved_at: Time`

    format: date-time

  - `resolved_by: BetaSpendLimitUserActor | BetaSpendLimitScopedAPIKeyActor`

    - `class BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

    - `class BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

  - `spend_summary: BetaSpendSummary`

    Per-member effective-limit report row (`GET /spend_limits/effective`).

    - `actor: BetaSpendLimitUserActor | BetaSpendLimitScopedAPIKeyActor`

      - `class BetaSpendLimitUserActor`

        A user within the organization. `name` and `email_address` are
        null when the underlying account is unavailable or has been deleted;
        `deleted` is true only for deleted accounts.

      - `class BetaSpendLimitScopedAPIKeyActor`

        A scoped Admin API key acting on behalf of the organization.

    - `amount: String`

      Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

    - `currency: String`

      ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

    - `period: BetaSpendLimitPeriod`

      Period this row's effective limit and spend are reported for.

    - `period_to_date_spend: String`

      The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

    - `scope: BetaSpendLimitUserScope | BetaSpendLimitSeatTierScope | BetaSpendLimitRBACGroupScope | 3 more`

      - `class BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

        - `type: :user`

          Scope type. Always `user` for this scope.

        - `user_id: String`

          Tagged ID of the member the spend limit applies to.

      - `class BetaSpendLimitSeatTierScope`

        - `type: :seat_tier`

        - `seat_tier: String`

      - `class BetaSpendLimitRBACGroupScope`

        - `type: :rbac_group`

        - `rbac_group_id: String`

      - `class BetaSpendLimitOrganizationServiceScope`

        - `type: :organization_service`

        - `service: String`

      - `class BetaSpendLimitOrganizationScope`

        - `type: :organization`

      - `class BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

        - `type: :workspace`

          Scope type. Always `workspace` for this scope.

        - `workspace_id: String`

          Tagged ID of the workspace the spend limit applies to.

    - `source: BetaSpendLimitUserScope | BetaSpendLimitSeatTierScope | BetaSpendLimitRBACGroupScope | 3 more`

      - `class BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

      - `class BetaSpendLimitSeatTierScope`

      - `class BetaSpendLimitRBACGroupScope`

      - `class BetaSpendLimitOrganizationServiceScope`

      - `class BetaSpendLimitOrganizationScope`

      - `class BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

    - `spend_limit_id: String`

  - `status: BetaSpendLimitIncreaseRequestStatus`

    - `:approved`

    - `:denied`

    - `:pending`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_spend_limit_increase_request = anthropic.beta.organization.spend_limits.increase_requests.deny("spend_limit_increase_request_id")

puts(beta_spend_limit_increase_request)
```

##### Response (200)

```json
{
  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "daily",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "daily",
    "period_to_date_spend": "12050.5",
    "scope": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "source": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "spend_limit_id": "spend_limit_id"
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
}
```

## Beta › Organization › RBAC Groups

### Create RBAC Group

`beta.organization.rbac_groups.create(**kwargs) -> BetaRBACGroup`

**POST** `/v1/organizations/rbac_groups`

Create an RBAC Group in the Claude Enterprise tenant. Groups created via the API have source type `"direct"`.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `name: String`

  Name of the RBAC Group. Not uniqueness-enforced.

  minLength: 1, maxLength: 255

#### Returns

- `class BetaRBACGroup`

  - `type: :rbac_group`

    Object type.

    For RBAC Groups, this is always `"rbac_group"`.

  - `id: String`

    ID of the RBAC Group.

  - `created_at: Time`

    RFC 3339 timestamp of when the RBAC Group was created.

    format: date-time

  - `name: String`

    Name of the RBAC Group. Not uniqueness-enforced.

  - `role_ids: Array[String]`

    RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

  - `source_type: :direct | :scim`

    How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

    - `:direct`

    - `:scim`

  - `updated_at: Time`

    RFC 3339 timestamp of when the RBAC Group was last updated.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_rbac_group = anthropic.beta.organization.rbac_groups.create(name: "Engineering")

puts(beta_rbac_group)
```

##### Response (200)

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Engineering",
  "role_ids": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "roles": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "source_type": "direct",
  "type": "rbac_group",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### List RBAC Groups

`beta.organization.rbac_groups.list(**kwargs) -> PageCursor<BetaRBACGroup>`

**GET** `/v1/organizations/rbac_groups`

List RBAC Groups in the Claude Enterprise tenant.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `page: String`

  Optionally set to the `next_page` token from the previous response.

#### Returns

- `class BetaRBACGroup`

  - `type: :rbac_group`

    Object type.

    For RBAC Groups, this is always `"rbac_group"`.

  - `id: String`

    ID of the RBAC Group.

  - `created_at: Time`

    RFC 3339 timestamp of when the RBAC Group was created.

    format: date-time

  - `name: String`

    Name of the RBAC Group. Not uniqueness-enforced.

  - `role_ids: Array[String]`

    RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

  - `source_type: :direct | :scim`

    How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

    - `:direct`

    - `:scim`

  - `updated_at: Time`

    RFC 3339 timestamp of when the RBAC Group was last updated.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.rbac_groups.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "name": "Engineering",
      "role_ids": [
        "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
      ],
      "roles": [
        "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
      ],
      "source_type": "direct",
      "type": "rbac_group",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": false,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19ncm91cF8wMSJ9"
}
```

### Get RBAC Group

`beta.organization.rbac_groups.retrieve(rbac_group_id) -> BetaRBACGroup`

**GET** `/v1/organizations/rbac_groups/{rbac_group_id}`

Retrieve an RBAC Group by ID.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `rbac_group_id: String`

  ID of the RBAC Group.

#### Returns

- `class BetaRBACGroup`

  - `type: :rbac_group`

    Object type.

    For RBAC Groups, this is always `"rbac_group"`.

  - `id: String`

    ID of the RBAC Group.

  - `created_at: Time`

    RFC 3339 timestamp of when the RBAC Group was created.

    format: date-time

  - `name: String`

    Name of the RBAC Group. Not uniqueness-enforced.

  - `role_ids: Array[String]`

    RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

  - `source_type: :direct | :scim`

    How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

    - `:direct`

    - `:scim`

  - `updated_at: Time`

    RFC 3339 timestamp of when the RBAC Group was last updated.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_rbac_group = anthropic.beta.organization.rbac_groups.retrieve("rbac_group_id")

puts(beta_rbac_group)
```

##### Response (200)

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Engineering",
  "role_ids": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "roles": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "source_type": "direct",
  "type": "rbac_group",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### Update RBAC Group

`beta.organization.rbac_groups.update(rbac_group_id, **kwargs) -> BetaRBACGroup`

**POST** `/v1/organizations/rbac_groups/{rbac_group_id}`

Update an RBAC Group's name. Groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `rbac_group_id: String`

  ID of the RBAC Group.

- `name: String`

  Name of the RBAC Group. Not uniqueness-enforced.

  minLength: 1, maxLength: 255

#### Returns

- `class BetaRBACGroup`

  - `type: :rbac_group`

    Object type.

    For RBAC Groups, this is always `"rbac_group"`.

  - `id: String`

    ID of the RBAC Group.

  - `created_at: Time`

    RFC 3339 timestamp of when the RBAC Group was created.

    format: date-time

  - `name: String`

    Name of the RBAC Group. Not uniqueness-enforced.

  - `role_ids: Array[String]`

    RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

  - `source_type: :direct | :scim`

    How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

    - `:direct`

    - `:scim`

  - `updated_at: Time`

    RFC 3339 timestamp of when the RBAC Group was last updated.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_rbac_group = anthropic.beta.organization.rbac_groups.update("rbac_group_id")

puts(beta_rbac_group)
```

##### Response (200)

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Engineering",
  "role_ids": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "roles": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "source_type": "direct",
  "type": "rbac_group",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### Delete RBAC Group

`beta.organization.rbac_groups.delete(rbac_group_id) -> RBACGroupDeleteResponse`

**DELETE** `/v1/organizations/rbac_groups/{rbac_group_id}`

Delete an RBAC Group. Groups provisioned by an identity provider (source type `"scim"`) cannot be deleted via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `rbac_group_id: String`

  ID of the RBAC Group.

#### Returns

- `class RBACGroupDeleteResponse`

  - `type: :rbac_group_deleted`

    Deleted object type.

    For RBAC Groups, this is always `"rbac_group_deleted"`.

  - `id: String`

    ID of the RBAC Group.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

rbac_group = anthropic.beta.organization.rbac_groups.delete("rbac_group_id")

puts(rbac_group)
```

##### Response (200)

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_deleted"
}
```

## Beta › Organization › RBAC Groups › Members

### List RBAC Group Members

`beta.organization.rbac_groups.members.list(rbac_group_id, **kwargs) -> PageCursor<BetaRBACGroupMember>`

**GET** `/v1/organizations/rbac_groups/{rbac_group_id}/members`

List members of an RBAC Group.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `rbac_group_id: String`

  ID of the RBAC Group.

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `page: String`

  Optionally set to the `next_page` token from the previous response.

#### Returns

- `class BetaRBACGroupMember`

  - `type: :rbac_group_member`

    Object type.

    For RBAC Group Members, this is always `"rbac_group_member"`.

  - `created_at: Time`

    RFC 3339 timestamp of when the User was added to the RBAC Group.

    format: date-time

  - `email: String`

    Email of the User.

  - `rbac_group_id: String`

    ID of the RBAC Group.

  - `user_id: String`

    ID of the User.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.rbac_groups.members.list("rbac_group_id")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "type": "rbac_group_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    }
  ],
  "has_more": false,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19ncm91cF8wMSJ9"
}
```

### Add RBAC Group Member

`beta.organization.rbac_groups.members.add(rbac_group_id, **kwargs) -> BetaRBACGroupMember`

**POST** `/v1/organizations/rbac_groups/{rbac_group_id}/members`

Add a User to an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `rbac_group_id: String`

  ID of the RBAC Group.

- `user_id: String`

  ID of the User.

#### Returns

- `class BetaRBACGroupMember`

  - `type: :rbac_group_member`

    Object type.

    For RBAC Group Members, this is always `"rbac_group_member"`.

  - `created_at: Time`

    RFC 3339 timestamp of when the User was added to the RBAC Group.

    format: date-time

  - `email: String`

    Email of the User.

  - `rbac_group_id: String`

    ID of the RBAC Group.

  - `user_id: String`

    ID of the User.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_rbac_group_member = anthropic.beta.organization.rbac_groups.members.add(
  "rbac_group_id",
  user_id: "user_01WCz1FkmYMm4gnmykNKUu3Q"
)

puts(beta_rbac_group_member)
```

##### Response (200)

```json
{
  "created_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
}
```

### Remove RBAC Group Member

`beta.organization.rbac_groups.members.remove(user_id, **kwargs) -> MemberRemoveResponse`

**DELETE** `/v1/organizations/rbac_groups/{rbac_group_id}/members/{user_id}`

Remove a User from an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `rbac_group_id: String`

  ID of the RBAC Group.

- `user_id: String`

  ID of the User.

#### Returns

- `class MemberRemoveResponse`

  - `type: :rbac_group_member_deleted`

    Deleted object type. For RBAC Group Members, this is always `"rbac_group_member_deleted"`.

  - `rbac_group_id: String`

    ID of the RBAC Group.

  - `user_id: String`

    ID of the User.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

member = anthropic.beta.organization.rbac_groups.members.remove("user_id", rbac_group_id: "rbac_group_id")

puts(member)
```

##### Response (200)

```json
{
  "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
}
```

## Beta › Organization › RBAC Roles

### List RBAC Roles

`beta.organization.rbac_roles.list(**kwargs) -> PageCursor<BetaRBACRole>`

**GET** `/v1/organizations/rbac_roles`

List RBAC Roles in the organization.

The RBAC Roles API is available to Claude Enterprise organizations only.

#### Parameters

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `page: String`

  Optionally set to the `next_page` token from the previous response.

#### Returns

- `class BetaRBACRole`

  - `type: :rbac_role`

    Object type.

    For RBAC Roles, this is always `"rbac_role"`.

  - `id: String`

    ID of the RBAC Role.

  - `created_at: Time`

    RFC 3339 datetime string indicating when the RBAC Role was created.

    format: date-time

  - `name: String`

    Name of the RBAC Role.

  - `updated_at: Time`

    RFC 3339 datetime string indicating when the RBAC Role was last updated.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.rbac_roles.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "name": "Project Editor",
      "type": "rbac_role",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": true,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19yb2xlXzAxIn0"
}
```

### Get RBAC Role

`beta.organization.rbac_roles.retrieve(rbac_role_id) -> BetaRBACRole`

**GET** `/v1/organizations/rbac_roles/{rbac_role_id}`

Retrieve an RBAC Role by ID.

The RBAC Roles API is available to Claude Enterprise organizations only.

#### Parameters

- `rbac_role_id: String`

  ID of the RBAC Role.

#### Returns

- `class BetaRBACRole`

  - `type: :rbac_role`

    Object type.

    For RBAC Roles, this is always `"rbac_role"`.

  - `id: String`

    ID of the RBAC Role.

  - `created_at: Time`

    RFC 3339 datetime string indicating when the RBAC Role was created.

    format: date-time

  - `name: String`

    Name of the RBAC Role.

  - `updated_at: Time`

    RFC 3339 datetime string indicating when the RBAC Role was last updated.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_rbac_role = anthropic.beta.organization.rbac_roles.retrieve("rbac_role_id")

puts(beta_rbac_role)
```

##### Response (200)

```json
{
  "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Project Editor",
  "type": "rbac_role",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

## Beta › Organization › RBAC Roles › Permissions

### List RBAC Role Permissions

`beta.organization.rbac_roles.permissions.list(rbac_role_id, **kwargs) -> PageCursor<BetaRBACRolePermission>`

**GET** `/v1/organizations/rbac_roles/{rbac_role_id}/permissions`

List the permissions an RBAC Role grants.

The RBAC Roles API is available to Claude Enterprise organizations only.

#### Parameters

- `rbac_role_id: String`

  ID of the RBAC Role.

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `page: String`

  Optionally set to the `next_page` token from the previous response.

#### Returns

- `class BetaRBACRolePermission`

  - `type: :rbac_role_permission`

    Object type.

    For RBAC Role Permissions, this is always `"rbac_role_permission"`.

  - `action: String`

    Action the permission grants on the resource.

    The vocabulary follows the resource: an `organization` grant carries a
    product-feature entitlement (for example `chat`), an admin-panel
    permission entitlement (`permission_*`), or a blanket capability-access
    mode — `capability_access_all` grants every product-feature entitlement,
    and `capability_access_all_ga` grants the generally-available subset as
    it stands at permission-check time; neither mode grants model-access
    entitlements. A consumer enumerating a role's per-feature grants should
    treat a blanket row as granting every product-feature entitlement it
    covers, or it will under-report the role's effective access. A `connector_tool` grant carries
    a tool-access action (`use` or `always_allow`); a `connector_scope` grant
    carries the scope action `grant` (the role may receive the named OAuth
    scope when tokens are minted for the connector); `connector` and
    `all_connectors` grants carry a tool-access action, the scope action, or
    an authentication-method action (`interactive` or `managed`).

  - `resource: BetaRBACOrganizationPermissionResource | BetaRBACConnectorToolPermissionResource | BetaRBACConnectorScopePermissionResource | 2 more`

    What the permission applies to.

    A tagged union: `type` names the kind of resource and determines which
    identifier fields are present.

    - `class BetaRBACOrganizationPermissionResource`

      - `type: :organization`

        Kind of resource the permission applies to.

      - `organization_id: String`

        UUID of the organization the permission applies to.

    - `class BetaRBACConnectorToolPermissionResource`

      - `type: :connector_tool`

        Kind of resource the permission applies to.

      - `connector_id: String`

        ID of the connector the permission applies to.

      - `tool_name: String`

        Published name of the connector tool the permission applies to.

        When the published name contains characters outside `[a-zA-Z0-9_-]` (or
        collides with a reserved form), it is server-encoded into a stable
        `{prefix}_{32-hex}` form — a shortened readable prefix of the name plus
        a hash — from which the published name is not recoverable.

    - `class BetaRBACConnectorScopePermissionResource`

      - `type: :connector_scope`

        Kind of resource the permission applies to.

      - `connector_id: String`

        ID of the connector the permission applies to.

      - `scope: String`

        OAuth scope the permission names — the role may receive this scope when
        tokens are minted for the connector.

        Subject to the same encoding rule as `tool_name`: a scope containing
        characters outside `[a-zA-Z0-9_-]` (or colliding with a reserved form)
        appears server-encoded in a stable `{prefix}_{32-hex}` form. OAuth
        scopes routinely contain `:` and `/`, so most appear encoded.

    - `class BetaRBACConnectorPermissionResource`

      - `type: :connector`

        Kind of resource the permission applies to.

      - `connector_id: String`

        ID of the connector the permission applies to.

    - `class BetaRBACAllConnectorsPermissionResource`

      - `type: :all_connectors`

        Kind of resource the permission applies to.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.rbac_roles.permissions.list("rbac_role_id")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "action": "use",
      "resource": {
        "organization_id": "3c4f5e6d-7a8b-49c0-9d1e-2f3a4b5c6d7e",
        "type": "organization"
      },
      "type": "rbac_role_permission"
    }
  ],
  "has_more": true,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19yb2xlXzAxIn0"
}
```

## Beta › Organization › Plugins

### Create Plugin

`beta.organization.plugins.create(**kwargs) -> BetaPlugin`

**POST** `/v1/organizations/plugins`

Create an organization-owned Plugin and its first version by uploading the
version's files.

The upload is `multipart/form-data`: the version's files (`files`, each part sent
as `files[]`), with an optional `marketplace_id` and `release_notes`. The manifest's `name` becomes the
Plugin's `name`, and `display_name`, `description` and `manifest_version` come
from the manifest too.

`name` may contain lowercase letters (from any alphabet), digits, and hyphens, up
to 64 characters. Uppercase letters, spaces, underscores, and other punctuation are
rejected.

The `name` must be unique within the marketplace: a name already taken
returns a 409 with `error_code` `plugin_name_taken` and, when a Plugin holds it,
that Plugin's ID in `details.plugin_id`. A Plugin going into the organization's
library marketplace is also refused with a 409 when one of its skills has the name of
an organization skill (a skill an administrator uploaded for the whole organization
in claude.ai): `error_code` `skill_name_taken`, with that name in
`details.skill_name`; rename the skill, or remove the organization skill in
claude.ai. A 503 with `error_code`
`registration_pending` means the Plugin and its version were stored (their IDs are
in `details`) but are not yet usable in claude.ai: do not retry the create (the
retry would return `plugin_name_taken`); create a version on the stored Plugin
instead, which completes it.

For a worked example, see [Create a plugin](https://platform.claude.com/docs/en/manage-claude/plugins-api#create-a-plugin)
in the Plugins API guide.

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `files: Array[String]`

  The version's files: one part per file, the part's filename being the file's path within the Plugin (for example `skills/review-pr/SKILL.md`), or a single `.zip` or `.plugin` archive holding them all. On the wire each part is named `files[]`, and a part named plain `files` is not read; with cURL, `-F 'files[]=@SKILL.md;filename=skills/review-pr/SKILL.md'`. The files must include the manifest, `.claude-plugin/plugin.json`.

- `marketplace_id: String`

  ID of the organization-owned plugin marketplace to create the Plugin in (prefixed `marketplace_`). It must be a `manual` marketplace, one whose Plugins are uploaded rather than synchronized from a repository. When omitted, the Plugin is created in the organization's library marketplace, an organization-owned `manual` marketplace created on first use.

- `release_notes: String`

  Release notes stored with the version and shown in its version history in claude.ai; up to 5,000 characters.

  maxLength: 5000

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaPlugin`

  - `type: :plugin`

    Always `plugin`.

  - `id: String`

    The Plugin's ID.

  - `components: Array[BetaPluginComponent]`

    What the served version contains; null when not enumerated.

    - `type: :agent | :cli | :command | 3 more`

      The kind of component.

      - `:agent`

      - `:cli`

      - `:command`

      - `:hook`

      - `:mcp_server`

      - `:skill`

    - `description: String`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: String`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: BetaPluginContentScan`

    The served version's content scan; null when it has not been scanned.

    - `assessment: :fail | :pass | :unknown | :warn`

      The scan's verdict; set only when `status` is `completed`.

      - `:fail`

      - `:pass`

      - `:unknown`

      - `:warn`

    - `reason: String`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: :completed | :errored | :processing`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `:completed`

      - `:errored`

      - `:processing`

  - `created_at: Time`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor | BetaPluginAPIActor`

    Who created the Plugin; null when no creator is recorded.

    - `class BetaPluginUserActor`

      - `type: :user_actor`

        A member of the organization.

      - `email_address: String`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: String`

        The member's User ID.

    - `class BetaPluginAPIActor`

      - `type: :api_actor`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

      - `api_key_id: String`

        The key's ID.

  - `description: String`

    The served version's description.

  - `display_name: String`

    The served version's display name.

  - `latest_version_id: String`

    The newest version.

  - `manifest_version: String`

    The version string the served version's manifest declares.

  - `marketplace_id: String`

    The ID of the plugin marketplace the Plugin lives in.

  - `name: String`

    Lowercase identifier, unique within its plugin marketplace. Fixed for an organization-owned Plugin's lifetime; a member-owned Plugin's changes when its owner renames it in claude.ai, while its `id` stays the same.

  - `organization_installation_preference: :auto_install | :available | :not_available | :required`

    Organization-owned Plugin: the organization-wide installation setting every member gets unless an RBAC Group they belong to holds its own — the Plugin's own setting, or its plugin marketplace's default. Null for a member-owned Plugin, which has shares instead. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `:auto_install`

    - `:available`

    - `:not_available`

    - `:required`

  - `organization_installation_preference_inherited: bool`

    Organization-owned Plugin: true while it has no organization-wide setting of its own and `organization_installation_preference` is its plugin marketplace's default. Null for a member-owned Plugin.

  - `owner: BetaPluginOwnerOrganization | BetaPluginOwnerUser`

    Who owns the Plugin: the organization, or the member whose personal plugin marketplace it lives in.

    - `class BetaPluginOwnerOrganization`

      - `type: :organization`

        The Plugin lives in a plugin marketplace the organization owns.

    - `class BetaPluginOwnerUser`

      - `type: :user`

        The Plugin lives in one member's personal plugin marketplace.

      - `user_id: String`

        The member's User ID.

  - `reach: :contained | :privileged | :remote`

    How far the served version reaches: `remote` when it declares an MCP server or a CLI, `privileged` when it declares a hook, monitor, language server or settings but nothing remote, `contained` otherwise; null when not classifiable.

    - `:contained`

    - `:privileged`

    - `:remote`

  - `served_version_id: String`

    The version claude.ai serves to members.

  - `served_version_pinned: bool`

    False while the served version follows each new version; true once it has been pinned to one.

  - `updated_at: Time`

    RFC 3339. Moves on a new version and on a served-version change; a change to the Plugin's installation settings or shares does not move it.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_plugin = anthropic.beta.organization.plugins.create(files: [StringIO.new("Example data")])

puts(beta_plugin)
```

##### Response (200)

```json
{
  "id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "components": [
    {
      "description": "description",
      "name": "review-pr",
      "type": "skill"
    }
  ],
  "content_scan": {
    "assessment": "warn",
    "reason": "credential-exposure",
    "status": "completed"
  },
  "created_at": "2026-03-14T09:26:53.589793Z",
  "created_by": {
    "email_address": "user@example.com",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "description": "Reviews pull requests against your team's conventions.",
  "display_name": "Code Review Helper",
  "latest_version_id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
  "manifest_version": "1.2.0",
  "marketplace_id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
  "name": "code-review-helper",
  "organization_installation_preference": "available",
  "organization_installation_preference_inherited": true,
  "owner": {
    "type": "organization"
  },
  "reach": "contained",
  "served_version_id": "pluginver_01K9wPcHd4Rm2Tx8Vq6Ln3Sb",
  "served_version_pinned": true,
  "type": "plugin",
  "updated_at": "2026-03-14T09:26:53.589793Z"
}
```

### Get Plugin

`beta.organization.plugins.retrieve(plugin_id, **kwargs) -> BetaPlugin`

**GET** `/v1/organizations/plugins/{plugin_id}`

Retrieve a Plugin by ID.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `plugin_id: String`

  ID of the Plugin (prefixed `plugin_`).

- `organization_id: String`

  For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaPlugin`

  - `type: :plugin`

    Always `plugin`.

  - `id: String`

    The Plugin's ID.

  - `components: Array[BetaPluginComponent]`

    What the served version contains; null when not enumerated.

    - `type: :agent | :cli | :command | 3 more`

      The kind of component.

      - `:agent`

      - `:cli`

      - `:command`

      - `:hook`

      - `:mcp_server`

      - `:skill`

    - `description: String`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: String`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: BetaPluginContentScan`

    The served version's content scan; null when it has not been scanned.

    - `assessment: :fail | :pass | :unknown | :warn`

      The scan's verdict; set only when `status` is `completed`.

      - `:fail`

      - `:pass`

      - `:unknown`

      - `:warn`

    - `reason: String`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: :completed | :errored | :processing`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `:completed`

      - `:errored`

      - `:processing`

  - `created_at: Time`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor | BetaPluginAPIActor`

    Who created the Plugin; null when no creator is recorded.

    - `class BetaPluginUserActor`

      - `type: :user_actor`

        A member of the organization.

      - `email_address: String`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: String`

        The member's User ID.

    - `class BetaPluginAPIActor`

      - `type: :api_actor`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

      - `api_key_id: String`

        The key's ID.

  - `description: String`

    The served version's description.

  - `display_name: String`

    The served version's display name.

  - `latest_version_id: String`

    The newest version.

  - `manifest_version: String`

    The version string the served version's manifest declares.

  - `marketplace_id: String`

    The ID of the plugin marketplace the Plugin lives in.

  - `name: String`

    Lowercase identifier, unique within its plugin marketplace. Fixed for an organization-owned Plugin's lifetime; a member-owned Plugin's changes when its owner renames it in claude.ai, while its `id` stays the same.

  - `organization_installation_preference: :auto_install | :available | :not_available | :required`

    Organization-owned Plugin: the organization-wide installation setting every member gets unless an RBAC Group they belong to holds its own — the Plugin's own setting, or its plugin marketplace's default. Null for a member-owned Plugin, which has shares instead. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `:auto_install`

    - `:available`

    - `:not_available`

    - `:required`

  - `organization_installation_preference_inherited: bool`

    Organization-owned Plugin: true while it has no organization-wide setting of its own and `organization_installation_preference` is its plugin marketplace's default. Null for a member-owned Plugin.

  - `owner: BetaPluginOwnerOrganization | BetaPluginOwnerUser`

    Who owns the Plugin: the organization, or the member whose personal plugin marketplace it lives in.

    - `class BetaPluginOwnerOrganization`

      - `type: :organization`

        The Plugin lives in a plugin marketplace the organization owns.

    - `class BetaPluginOwnerUser`

      - `type: :user`

        The Plugin lives in one member's personal plugin marketplace.

      - `user_id: String`

        The member's User ID.

  - `reach: :contained | :privileged | :remote`

    How far the served version reaches: `remote` when it declares an MCP server or a CLI, `privileged` when it declares a hook, monitor, language server or settings but nothing remote, `contained` otherwise; null when not classifiable.

    - `:contained`

    - `:privileged`

    - `:remote`

  - `served_version_id: String`

    The version claude.ai serves to members.

  - `served_version_pinned: bool`

    False while the served version follows each new version; true once it has been pinned to one.

  - `updated_at: Time`

    RFC 3339. Moves on a new version and on a served-version change; a change to the Plugin's installation settings or shares does not move it.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_plugin = anthropic.beta.organization.plugins.retrieve("plugin_id")

puts(beta_plugin)
```

##### Response (200)

```json
{
  "id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "components": [
    {
      "description": "description",
      "name": "review-pr",
      "type": "skill"
    }
  ],
  "content_scan": {
    "assessment": "warn",
    "reason": "credential-exposure",
    "status": "completed"
  },
  "created_at": "2026-03-14T09:26:53.589793Z",
  "created_by": {
    "email_address": "user@example.com",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "description": "Reviews pull requests against your team's conventions.",
  "display_name": "Code Review Helper",
  "latest_version_id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
  "manifest_version": "1.2.0",
  "marketplace_id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
  "name": "code-review-helper",
  "organization_installation_preference": "available",
  "organization_installation_preference_inherited": true,
  "owner": {
    "type": "organization"
  },
  "reach": "contained",
  "served_version_id": "pluginver_01K9wPcHd4Rm2Tx8Vq6Ln3Sb",
  "served_version_pinned": true,
  "type": "plugin",
  "updated_at": "2026-03-14T09:26:53.589793Z"
}
```

### Update Plugin

`beta.organization.plugins.update(plugin_id, **kwargs) -> BetaPlugin`

**POST** `/v1/organizations/plugins/{plugin_id}`

Change which stored version of an organization-owned Plugin is served to members,
for example to roll back to an earlier one. This pins the served version: later
uploads are stored but no longer change what is served, and pinning cannot currently
be undone, here or in claude.ai.

Pass the version as `served_version_id`: an earlier one to roll back, a later one to
start serving a version that was stored without being served, or the one already
served to pin it without changing what is served. No new version is created.

When the organization has content scanning enabled, a version whose scan is still
running is refused with a 409 (`error_code` `scan_pending`; retry once the scan
finishes) and one whose scan failed, errored or reached no verdict with a 400
(`scan_failed`; a `warn` is accepted). When the Plugin is in the organization's
library marketplace, a version other than the one served is also refused with a 409
when one of its skills has a name that an organization skill (one an administrator
uploaded for the whole organization in claude.ai) has since taken: `error_code`
`skill_name_taken`, with that name in `details.skill_name`. A member-owned Plugin
cannot be updated here (403).

This endpoint does not write installation settings; they are written at
`/v1/organizations/plugins/{plugin_id}/installation_settings/{target}`.

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `plugin_id: String`

  ID of the Plugin (prefixed `plugin_`).

- `served_version_id: String`

  Serve this version of the Plugin (prefixed `pluginver_`) and pin the served version to it; `latest` is not accepted.

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaPlugin`

  - `type: :plugin`

    Always `plugin`.

  - `id: String`

    The Plugin's ID.

  - `components: Array[BetaPluginComponent]`

    What the served version contains; null when not enumerated.

    - `type: :agent | :cli | :command | 3 more`

      The kind of component.

      - `:agent`

      - `:cli`

      - `:command`

      - `:hook`

      - `:mcp_server`

      - `:skill`

    - `description: String`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: String`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: BetaPluginContentScan`

    The served version's content scan; null when it has not been scanned.

    - `assessment: :fail | :pass | :unknown | :warn`

      The scan's verdict; set only when `status` is `completed`.

      - `:fail`

      - `:pass`

      - `:unknown`

      - `:warn`

    - `reason: String`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: :completed | :errored | :processing`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `:completed`

      - `:errored`

      - `:processing`

  - `created_at: Time`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor | BetaPluginAPIActor`

    Who created the Plugin; null when no creator is recorded.

    - `class BetaPluginUserActor`

      - `type: :user_actor`

        A member of the organization.

      - `email_address: String`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: String`

        The member's User ID.

    - `class BetaPluginAPIActor`

      - `type: :api_actor`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

      - `api_key_id: String`

        The key's ID.

  - `description: String`

    The served version's description.

  - `display_name: String`

    The served version's display name.

  - `latest_version_id: String`

    The newest version.

  - `manifest_version: String`

    The version string the served version's manifest declares.

  - `marketplace_id: String`

    The ID of the plugin marketplace the Plugin lives in.

  - `name: String`

    Lowercase identifier, unique within its plugin marketplace. Fixed for an organization-owned Plugin's lifetime; a member-owned Plugin's changes when its owner renames it in claude.ai, while its `id` stays the same.

  - `organization_installation_preference: :auto_install | :available | :not_available | :required`

    Organization-owned Plugin: the organization-wide installation setting every member gets unless an RBAC Group they belong to holds its own — the Plugin's own setting, or its plugin marketplace's default. Null for a member-owned Plugin, which has shares instead. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `:auto_install`

    - `:available`

    - `:not_available`

    - `:required`

  - `organization_installation_preference_inherited: bool`

    Organization-owned Plugin: true while it has no organization-wide setting of its own and `organization_installation_preference` is its plugin marketplace's default. Null for a member-owned Plugin.

  - `owner: BetaPluginOwnerOrganization | BetaPluginOwnerUser`

    Who owns the Plugin: the organization, or the member whose personal plugin marketplace it lives in.

    - `class BetaPluginOwnerOrganization`

      - `type: :organization`

        The Plugin lives in a plugin marketplace the organization owns.

    - `class BetaPluginOwnerUser`

      - `type: :user`

        The Plugin lives in one member's personal plugin marketplace.

      - `user_id: String`

        The member's User ID.

  - `reach: :contained | :privileged | :remote`

    How far the served version reaches: `remote` when it declares an MCP server or a CLI, `privileged` when it declares a hook, monitor, language server or settings but nothing remote, `contained` otherwise; null when not classifiable.

    - `:contained`

    - `:privileged`

    - `:remote`

  - `served_version_id: String`

    The version claude.ai serves to members.

  - `served_version_pinned: bool`

    False while the served version follows each new version; true once it has been pinned to one.

  - `updated_at: Time`

    RFC 3339. Moves on a new version and on a served-version change; a change to the Plugin's installation settings or shares does not move it.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_plugin = anthropic.beta.organization.plugins.update(
  "plugin_id",
  served_version_id: "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8"
)

puts(beta_plugin)
```

##### Response (200)

```json
{
  "id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "components": [
    {
      "description": "description",
      "name": "review-pr",
      "type": "skill"
    }
  ],
  "content_scan": {
    "assessment": "warn",
    "reason": "credential-exposure",
    "status": "completed"
  },
  "created_at": "2026-03-14T09:26:53.589793Z",
  "created_by": {
    "email_address": "user@example.com",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "description": "Reviews pull requests against your team's conventions.",
  "display_name": "Code Review Helper",
  "latest_version_id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
  "manifest_version": "1.2.0",
  "marketplace_id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
  "name": "code-review-helper",
  "organization_installation_preference": "available",
  "organization_installation_preference_inherited": true,
  "owner": {
    "type": "organization"
  },
  "reach": "contained",
  "served_version_id": "pluginver_01K9wPcHd4Rm2Tx8Vq6Ln3Sb",
  "served_version_pinned": true,
  "type": "plugin",
  "updated_at": "2026-03-14T09:26:53.589793Z"
}
```

### List Plugins

`beta.organization.plugins.list(**kwargs) -> PageCursor<BetaPlugin>`

**GET** `/v1/organizations/plugins`

List the Plugins created under the organization, newest first: those in the
organization's own plugin marketplaces and those in members' personal plugin
marketplaces.

Plugins in members' personal marketplaces are listed with the same detail as the
organization's own, and their files can be downloaded through the version archive
endpoint, which records each such download on the Compliance API activity feed.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `created_at_gt: Time`

  RFC 3339 timestamp bound; combine [gte], [gt], [lte], [lt].

  format: date-time

- `created_at_gte: Time`

  RFC 3339 timestamp bound; combine [gte], [gt], [lte], [lt].

  format: date-time

- `created_at_lt: Time`

  RFC 3339 timestamp bound; combine [gte], [gt], [lte], [lt].

  format: date-time

- `created_at_lte: Time`

  RFC 3339 timestamp bound; combine [gte], [gt], [lte], [lt].

  format: date-time

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `100`.

  minimum: 1, maximum: 100

- `marketplace_id: String`

  Only Plugins in this plugin marketplace (prefixed `marketplace_`).

- `organization_id: String`

  For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `owner_type: :organization | :user`

  `organization` for Plugins in the organization's plugin marketplaces, `user` for Plugins in members' personal plugin marketplaces.

  - `:organization`

  - `:user`

- `owner_user_id: String`

  Only Plugins in this member's personal plugin marketplaces (prefixed `user_`); a removed member's ID is accepted.

- `page: String`

  Optionally set to the `next_page` token from the previous response.

  maxLength: 2048

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaPlugin`

  - `type: :plugin`

    Always `plugin`.

  - `id: String`

    The Plugin's ID.

  - `components: Array[BetaPluginComponent]`

    What the served version contains; null when not enumerated.

    - `type: :agent | :cli | :command | 3 more`

      The kind of component.

      - `:agent`

      - `:cli`

      - `:command`

      - `:hook`

      - `:mcp_server`

      - `:skill`

    - `description: String`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: String`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: BetaPluginContentScan`

    The served version's content scan; null when it has not been scanned.

    - `assessment: :fail | :pass | :unknown | :warn`

      The scan's verdict; set only when `status` is `completed`.

      - `:fail`

      - `:pass`

      - `:unknown`

      - `:warn`

    - `reason: String`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: :completed | :errored | :processing`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `:completed`

      - `:errored`

      - `:processing`

  - `created_at: Time`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor | BetaPluginAPIActor`

    Who created the Plugin; null when no creator is recorded.

    - `class BetaPluginUserActor`

      - `type: :user_actor`

        A member of the organization.

      - `email_address: String`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: String`

        The member's User ID.

    - `class BetaPluginAPIActor`

      - `type: :api_actor`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

      - `api_key_id: String`

        The key's ID.

  - `description: String`

    The served version's description.

  - `display_name: String`

    The served version's display name.

  - `latest_version_id: String`

    The newest version.

  - `manifest_version: String`

    The version string the served version's manifest declares.

  - `marketplace_id: String`

    The ID of the plugin marketplace the Plugin lives in.

  - `name: String`

    Lowercase identifier, unique within its plugin marketplace. Fixed for an organization-owned Plugin's lifetime; a member-owned Plugin's changes when its owner renames it in claude.ai, while its `id` stays the same.

  - `organization_installation_preference: :auto_install | :available | :not_available | :required`

    Organization-owned Plugin: the organization-wide installation setting every member gets unless an RBAC Group they belong to holds its own — the Plugin's own setting, or its plugin marketplace's default. Null for a member-owned Plugin, which has shares instead. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `:auto_install`

    - `:available`

    - `:not_available`

    - `:required`

  - `organization_installation_preference_inherited: bool`

    Organization-owned Plugin: true while it has no organization-wide setting of its own and `organization_installation_preference` is its plugin marketplace's default. Null for a member-owned Plugin.

  - `owner: BetaPluginOwnerOrganization | BetaPluginOwnerUser`

    Who owns the Plugin: the organization, or the member whose personal plugin marketplace it lives in.

    - `class BetaPluginOwnerOrganization`

      - `type: :organization`

        The Plugin lives in a plugin marketplace the organization owns.

    - `class BetaPluginOwnerUser`

      - `type: :user`

        The Plugin lives in one member's personal plugin marketplace.

      - `user_id: String`

        The member's User ID.

  - `reach: :contained | :privileged | :remote`

    How far the served version reaches: `remote` when it declares an MCP server or a CLI, `privileged` when it declares a hook, monitor, language server or settings but nothing remote, `contained` otherwise; null when not classifiable.

    - `:contained`

    - `:privileged`

    - `:remote`

  - `served_version_id: String`

    The version claude.ai serves to members.

  - `served_version_pinned: bool`

    False while the served version follows each new version; true once it has been pinned to one.

  - `updated_at: Time`

    RFC 3339. Moves on a new version and on a served-version change; a change to the Plugin's installation settings or shares does not move it.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.plugins.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
      "components": [
        {
          "description": "description",
          "name": "review-pr",
          "type": "skill"
        }
      ],
      "content_scan": {
        "assessment": "warn",
        "reason": "credential-exposure",
        "status": "completed"
      },
      "created_at": "2026-03-14T09:26:53.589793Z",
      "created_by": {
        "email_address": "user@example.com",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "description": "Reviews pull requests against your team's conventions.",
      "display_name": "Code Review Helper",
      "latest_version_id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
      "manifest_version": "1.2.0",
      "marketplace_id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
      "name": "code-review-helper",
      "organization_installation_preference": "available",
      "organization_installation_preference_inherited": true,
      "owner": {
        "type": "organization"
      },
      "reach": "contained",
      "served_version_id": "pluginver_01K9wPcHd4Rm2Tx8Vq6Ln3Sb",
      "served_version_pinned": true,
      "type": "plugin",
      "updated_at": "2026-03-14T09:26:53.589793Z"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
}
```

### Delete Plugin

`beta.organization.plugins.delete(plugin_id, **kwargs) -> BetaDeletedPlugin`

**DELETE** `/v1/organizations/plugins/{plugin_id}`

Permanently delete a Plugin and every version it holds, exactly as when an
administrator deletes it in claude.ai. The Plugin may belong to the organization or
to a member, including a member who has since left the organization.

An organization-owned Plugin's installation settings go with it; a member-owned
Plugin's shares are withdrawn and its owner no longer has it.

To take an organization-owned Plugin out of use reversibly, set its
organization-wide installation setting to `not_available` instead (and
remove or change any group settings, which override it for their members). Only a
Plugin in a `manual` marketplace can be deleted here; one synchronized from a
repository is removed by removing it from the repository (400).

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `plugin_id: String`

  ID of the Plugin (prefixed `plugin_`).

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaDeletedPlugin`

  - `type: :plugin_deleted`

    Always `plugin_deleted`.

  - `id: String`

    The deleted Plugin's ID.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_deleted_plugin = anthropic.beta.organization.plugins.delete("plugin_id")

puts(beta_deleted_plugin)
```

##### Response (200)

```json
{
  "id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "type": "plugin_deleted"
}
```

## Beta › Organization › Plugins › Versions

### Create Plugin Version

`beta.organization.plugins.versions.create(plugin_id, **kwargs) -> BetaPluginVersion`

**POST** `/v1/organizations/plugins/{plugin_id}/versions`

Add a version to an organization-owned Plugin by uploading the new version's
files; it becomes the version served to members unless the Plugin's served version
has been pinned.

The upload is the same `multipart/form-data` as creating a Plugin: the version's
files (`files`, each part sent as `files[]`) and optional `release_notes`. The uploaded manifest's `name`
must equal the Plugin's `name`. Returns the stored version; read the Plugin back to
see which version it serves.

Only a Plugin in a `manual` marketplace takes uploads; a Plugin synchronized from
a repository gets its versions from the repository. When the Plugin is in the
organization's library marketplace, a version that adds a skill with the name of an
organization skill (a skill an administrator uploaded for the whole organization in
claude.ai) is refused with a 409: `error_code` `skill_name_taken`, with that name in
`details.skill_name`. A 503 with `error_code`
`registration_pending` means the version was stored but is not yet usable; a later
version create on the Plugin completes it.

For a worked example, see [Create a version](https://platform.claude.com/docs/en/manage-claude/plugins-api#create-a-version)
in the Plugins API guide.

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `plugin_id: String`

  ID of the Plugin (prefixed `plugin_`).

- `files: Array[String]`

  The version's files: one part per file, the part's filename being the file's path within the Plugin (for example `skills/review-pr/SKILL.md`), or a single `.zip` or `.plugin` archive holding them all. On the wire each part is named `files[]`, and a part named plain `files` is not read; with cURL, `-F 'files[]=@SKILL.md;filename=skills/review-pr/SKILL.md'`. The files must include the manifest, `.claude-plugin/plugin.json`.

- `release_notes: String`

  Release notes stored with the version and shown in its version history in claude.ai; up to 5,000 characters.

  maxLength: 5000

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaPluginVersion`

  - `type: :plugin_version`

    Always `plugin_version`.

  - `id: String`

    The version's ID.

  - `components: Array[BetaPluginComponent]`

    What the version contains; null when not enumerated.

    - `type: :agent | :cli | :command | 3 more`

      The kind of component.

      - `:agent`

      - `:cli`

      - `:command`

      - `:hook`

      - `:mcp_server`

      - `:skill`

    - `description: String`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: String`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: BetaPluginContentScan`

    This version's content scan; null when it has not been scanned.

    - `assessment: :fail | :pass | :unknown | :warn`

      The scan's verdict; set only when `status` is `completed`.

      - `:fail`

      - `:pass`

      - `:unknown`

      - `:warn`

    - `reason: String`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: :completed | :errored | :processing`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `:completed`

      - `:errored`

      - `:processing`

  - `created_at: Time`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor | BetaPluginAPIActor`

    Who uploaded this version; null when not recorded.

    - `class BetaPluginUserActor`

      - `type: :user_actor`

        A member of the organization.

      - `email_address: String`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: String`

        The member's User ID.

    - `class BetaPluginAPIActor`

      - `type: :api_actor`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

      - `api_key_id: String`

        The key's ID.

  - `description: String`

    The manifest's description; null when it declares none.

  - `display_name: String`

    The manifest's display name; null when it declares none.

  - `manifest_version: String`

    The version string the manifest declares; null when it declares none.

  - `plugin_id: String`

    The Plugin's ID.

  - `reach: :contained | :privileged | :remote`

    How far the version reaches: `remote`, `privileged` or `contained`, as on the Plugin; null when not classifiable.

    - `:contained`

    - `:privileged`

    - `:remote`

  - `release_notes: String`

    As supplied with the upload; null when none were supplied.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_plugin_version = anthropic.beta.organization.plugins.versions.create("plugin_id", files: [StringIO.new("Example data")])

puts(beta_plugin_version)
```

##### Response (200)

```json
{
  "id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
  "components": [
    {
      "description": "description",
      "name": "review-pr",
      "type": "skill"
    }
  ],
  "content_scan": {
    "assessment": "warn",
    "reason": "credential-exposure",
    "status": "completed"
  },
  "created_at": "2026-03-14T09:26:53.589793Z",
  "created_by": {
    "email_address": "user@example.com",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "description": "Reviews pull requests against your team's conventions.",
  "display_name": "Code Review Helper",
  "manifest_version": "1.2.0",
  "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "reach": "contained",
  "release_notes": "Adds a review checklist for database migrations.",
  "type": "plugin_version"
}
```

### List Plugin Versions

`beta.organization.plugins.versions.list(plugin_id, **kwargs) -> PageCursor<BetaPluginVersion>`

**GET** `/v1/organizations/plugins/{plugin_id}/versions`

List a Plugin's versions, newest first.

The first item of the first page is the version the Plugin's `latest_version_id`
refers to.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `plugin_id: String`

  ID of the Plugin (prefixed `plugin_`).

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `organization_id: String`

  For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `page: String`

  Optionally set to the `next_page` token from the previous response.

  maxLength: 2048

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaPluginVersion`

  - `type: :plugin_version`

    Always `plugin_version`.

  - `id: String`

    The version's ID.

  - `components: Array[BetaPluginComponent]`

    What the version contains; null when not enumerated.

    - `type: :agent | :cli | :command | 3 more`

      The kind of component.

      - `:agent`

      - `:cli`

      - `:command`

      - `:hook`

      - `:mcp_server`

      - `:skill`

    - `description: String`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: String`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: BetaPluginContentScan`

    This version's content scan; null when it has not been scanned.

    - `assessment: :fail | :pass | :unknown | :warn`

      The scan's verdict; set only when `status` is `completed`.

      - `:fail`

      - `:pass`

      - `:unknown`

      - `:warn`

    - `reason: String`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: :completed | :errored | :processing`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `:completed`

      - `:errored`

      - `:processing`

  - `created_at: Time`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor | BetaPluginAPIActor`

    Who uploaded this version; null when not recorded.

    - `class BetaPluginUserActor`

      - `type: :user_actor`

        A member of the organization.

      - `email_address: String`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: String`

        The member's User ID.

    - `class BetaPluginAPIActor`

      - `type: :api_actor`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

      - `api_key_id: String`

        The key's ID.

  - `description: String`

    The manifest's description; null when it declares none.

  - `display_name: String`

    The manifest's display name; null when it declares none.

  - `manifest_version: String`

    The version string the manifest declares; null when it declares none.

  - `plugin_id: String`

    The Plugin's ID.

  - `reach: :contained | :privileged | :remote`

    How far the version reaches: `remote`, `privileged` or `contained`, as on the Plugin; null when not classifiable.

    - `:contained`

    - `:privileged`

    - `:remote`

  - `release_notes: String`

    As supplied with the upload; null when none were supplied.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.plugins.versions.list("plugin_id")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
      "components": [
        {
          "description": "description",
          "name": "review-pr",
          "type": "skill"
        }
      ],
      "content_scan": {
        "assessment": "warn",
        "reason": "credential-exposure",
        "status": "completed"
      },
      "created_at": "2026-03-14T09:26:53.589793Z",
      "created_by": {
        "email_address": "user@example.com",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "description": "Reviews pull requests against your team's conventions.",
      "display_name": "Code Review Helper",
      "manifest_version": "1.2.0",
      "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
      "reach": "contained",
      "release_notes": "Adds a review checklist for database migrations.",
      "type": "plugin_version"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
}
```

### Get Plugin Version

`beta.organization.plugins.versions.retrieve(version, **kwargs) -> BetaPluginVersion`

**GET** `/v1/organizations/plugins/{plugin_id}/versions/{version}`

Retrieve one version of a Plugin by its ID, or the Plugin's newest version.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `plugin_id: String`

  ID of the Plugin (prefixed `plugin_`).

- `version: String`

  ID of the Plugin Version (prefixed `pluginver_`), or `latest` for the newest one.

- `organization_id: String`

  For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaPluginVersion`

  - `type: :plugin_version`

    Always `plugin_version`.

  - `id: String`

    The version's ID.

  - `components: Array[BetaPluginComponent]`

    What the version contains; null when not enumerated.

    - `type: :agent | :cli | :command | 3 more`

      The kind of component.

      - `:agent`

      - `:cli`

      - `:command`

      - `:hook`

      - `:mcp_server`

      - `:skill`

    - `description: String`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: String`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: BetaPluginContentScan`

    This version's content scan; null when it has not been scanned.

    - `assessment: :fail | :pass | :unknown | :warn`

      The scan's verdict; set only when `status` is `completed`.

      - `:fail`

      - `:pass`

      - `:unknown`

      - `:warn`

    - `reason: String`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: :completed | :errored | :processing`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `:completed`

      - `:errored`

      - `:processing`

  - `created_at: Time`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor | BetaPluginAPIActor`

    Who uploaded this version; null when not recorded.

    - `class BetaPluginUserActor`

      - `type: :user_actor`

        A member of the organization.

      - `email_address: String`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: String`

        The member's User ID.

    - `class BetaPluginAPIActor`

      - `type: :api_actor`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

      - `api_key_id: String`

        The key's ID.

  - `description: String`

    The manifest's description; null when it declares none.

  - `display_name: String`

    The manifest's display name; null when it declares none.

  - `manifest_version: String`

    The version string the manifest declares; null when it declares none.

  - `plugin_id: String`

    The Plugin's ID.

  - `reach: :contained | :privileged | :remote`

    How far the version reaches: `remote`, `privileged` or `contained`, as on the Plugin; null when not classifiable.

    - `:contained`

    - `:privileged`

    - `:remote`

  - `release_notes: String`

    As supplied with the upload; null when none were supplied.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_plugin_version = anthropic.beta.organization.plugins.versions.retrieve("version", plugin_id: "plugin_id")

puts(beta_plugin_version)
```

##### Response (200)

```json
{
  "id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
  "components": [
    {
      "description": "description",
      "name": "review-pr",
      "type": "skill"
    }
  ],
  "content_scan": {
    "assessment": "warn",
    "reason": "credential-exposure",
    "status": "completed"
  },
  "created_at": "2026-03-14T09:26:53.589793Z",
  "created_by": {
    "email_address": "user@example.com",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "description": "Reviews pull requests against your team's conventions.",
  "display_name": "Code Review Helper",
  "manifest_version": "1.2.0",
  "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "reach": "contained",
  "release_notes": "Adds a review checklist for database migrations.",
  "type": "plugin_version"
}
```

### Download Plugin Version Archive

`beta.organization.plugins.versions.download(version, **kwargs) -> StringIO`

**GET** `/v1/organizations/plugins/{plugin_id}/versions/{version}/content`

Download one version's `.zip` archive, exactly as stored. Each download of a
Plugin from a member's personal plugin marketplace is recorded on the Compliance API
activity feed.

The response body is the archive (`Content-Type: application/zip`), sent as an
attachment whose filename is derived from the Plugin's name; name saved files from
the IDs in the request path, since that filename is not unique.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every read scope above (`read:plugins`, `read:org_audit`, and
`read:compliance_org_data`) can download the files of plugins in members' personal
marketplaces, including files that claude.ai's admin settings do not show, and a
`read:org_audit` or `read:compliance_org_data` key created for all of your parent
organization's linked organizations can do this in any organization under it that has
access to this API, by passing `organization_id`. Each such download records a
`claude_plugin_archive_accessed` event on the Compliance API activity feed,
identifying the key, the plugin, the version, and the member. Downloads of
organization-owned plugins are not recorded.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `plugin_id: String`

  ID of the Plugin (prefixed `plugin_`).

- `version: String`

  ID of the Plugin Version (prefixed `pluginver_`). `latest` is not accepted here.

- `organization_id: String`

  For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `StringIO`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

response = anthropic.beta.organization.plugins.versions.download("version", plugin_id: "plugin_id")

puts(response)
```

## Beta › Organization › Plugins › Installation Settings

### List Plugin Installation Settings

`beta.organization.plugins.installation_settings.list(plugin_id, **kwargs) -> PageCursor<BetaPluginInstallationSetting>`

**GET** `/v1/organizations/plugins/{plugin_id}/installation_settings`

List an organization-owned Plugin's installation settings, which say which
members it is for, most recently created first.

The list holds the Plugin's own organization-wide setting (absent while the Plugin
inherits its marketplace's default) and each RBAC Group's own setting. A
member-owned Plugin has shares instead, so this path returns 404 for one.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `plugin_id: String`

  ID of the Plugin (prefixed `plugin_`).

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `100`.

  minimum: 1, maximum: 100

- `organization_id: String`

  For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `page: String`

  Optionally set to the `next_page` token from the previous response.

  maxLength: 2048

- `target_type: :organization | :rbac_group`

  Only settings for this kind of target: `organization` (the organization-wide setting) or `rbac_group` (an RBAC Group's).

  - `:organization`

  - `:rbac_group`

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaPluginInstallationSetting`

  The installation setting an organization-owned Plugin holds for one
  target. It has no ID of its own: it is addressed by the Plugin's ID and the
  target.

  - `type: :plugin_installation_setting`

    Always `plugin_installation_setting`.

  - `created_at: Time`

    When the target was first given a setting for this Plugin.

    format: date-time

  - `installation_preference: :auto_install | :available | :not_available | :required`

    The setting the target holds for this Plugin. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `:auto_install`

    - `:available`

    - `:not_available`

    - `:required`

  - `plugin_id: String`

    The Plugin's ID.

  - `target: BetaPluginTargetOrganization | BetaPluginTargetRBACGroup | BetaPluginTargetOrganizationMember`

    Whose setting this is: `organization` (the Plugin's own organization-wide setting) or `rbac_group` (one RBAC Group's own setting); `organization_member` does not occur here.

    - `class BetaPluginTargetOrganization`

      - `type: :organization`

        Every member of the organization.

    - `class BetaPluginTargetRBACGroup`

      - `type: :rbac_group`

        An RBAC Group.

      - `rbac_group_id: String`

        The RBAC Group's ID.

    - `class BetaPluginTargetOrganizationMember`

      - `type: :organization_member`

        One member of the organization.

      - `user_id: String`

        The member's User ID.

  - `updated_at: Time`

    When its setting last changed.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.plugins.installation_settings.list("plugin_id")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "created_at": "2026-03-14T09:26:53.589793Z",
      "installation_preference": "required",
      "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
      "target": {
        "type": "organization"
      },
      "type": "plugin_installation_setting",
      "updated_at": "2026-03-14T09:26:53.589793Z"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
}
```

### Set Plugin Installation Setting

`beta.organization.plugins.installation_settings.set(target, **kwargs) -> BetaPluginInstallationSetting`

**POST** `/v1/organizations/plugins/{plugin_id}/installation_settings/{target}`

Set or change an organization-owned Plugin's installation setting for the whole
organization or for one RBAC Group.

Writing the value a target already holds of its own changes nothing.

A member-owned Plugin has shares instead of installation settings, so this path
returns 404 for one.

Send a Plugin's installation-setting writes one at a time. If several writes for the
same Plugin arrive at the same time, the server handles them one after another and
can answer some of them with `503` instead of applying them. That `503` carries
`x-should-retry: true`, and the write is safe to repeat: wait a second or two, then
send it again.

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `plugin_id: String`

  ID of the Plugin (prefixed `plugin_`).

- `target: String`

  The target whose setting is written: the literal `organization` for the Plugin's organization-wide setting, or an RBAC Group's ID (prefixed `rbac_group_`) for that group's own setting. Writing the `organization` target stops the Plugin from inheriting its marketplace's default, even when the value written equals that default.

- `installation_preference: :auto_install | :available | :not_available | :required`

  The installation setting the target is to hold for this Plugin: one of `required`, `auto_install`, `available`, `not_available`.

  - `:auto_install`

  - `:available`

  - `:not_available`

  - `:required`

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaPluginInstallationSetting`

  The installation setting an organization-owned Plugin holds for one
  target. It has no ID of its own: it is addressed by the Plugin's ID and the
  target.

  - `type: :plugin_installation_setting`

    Always `plugin_installation_setting`.

  - `created_at: Time`

    When the target was first given a setting for this Plugin.

    format: date-time

  - `installation_preference: :auto_install | :available | :not_available | :required`

    The setting the target holds for this Plugin. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `:auto_install`

    - `:available`

    - `:not_available`

    - `:required`

  - `plugin_id: String`

    The Plugin's ID.

  - `target: BetaPluginTargetOrganization | BetaPluginTargetRBACGroup | BetaPluginTargetOrganizationMember`

    Whose setting this is: `organization` (the Plugin's own organization-wide setting) or `rbac_group` (one RBAC Group's own setting); `organization_member` does not occur here.

    - `class BetaPluginTargetOrganization`

      - `type: :organization`

        Every member of the organization.

    - `class BetaPluginTargetRBACGroup`

      - `type: :rbac_group`

        An RBAC Group.

      - `rbac_group_id: String`

        The RBAC Group's ID.

    - `class BetaPluginTargetOrganizationMember`

      - `type: :organization_member`

        One member of the organization.

      - `user_id: String`

        The member's User ID.

  - `updated_at: Time`

    When its setting last changed.

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_plugin_installation_setting = anthropic.beta.organization.plugins.installation_settings.set(
  "target",
  plugin_id: "plugin_id",
  installation_preference: :required
)

puts(beta_plugin_installation_setting)
```

##### Response (200)

```json
{
  "created_at": "2026-03-14T09:26:53.589793Z",
  "installation_preference": "required",
  "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "target": {
    "type": "organization"
  },
  "type": "plugin_installation_setting",
  "updated_at": "2026-03-14T09:26:53.589793Z"
}
```

### Remove Plugin Installation Setting

`beta.organization.plugins.installation_settings.remove(target, **kwargs) -> BetaDeletedPluginInstallationSetting`

**DELETE** `/v1/organizations/plugins/{plugin_id}/installation_settings/{target}`

Remove an organization-owned Plugin's own installation setting for the whole
organization or for one RBAC Group.

Removing the `organization` target returns the Plugin to its marketplace's default
installation setting and leaves the groups' settings in place. Removing a group's
setting makes the group's members fall back to the Plugin's organization-wide setting
or to the settings of their other groups.

A target that holds no setting of its own returns 404 (a Plugin that already inherits
its marketplace's default holds no `organization` setting), and so does a member-owned
Plugin.

A removal counts as one of the Plugin's installation-setting writes: send all of those
writes one at a time. If several arrive for the same Plugin at the same time, the server
handles them one after another and can answer some of them with `503` and
`x-should-retry: true` instead of applying them; wait a second or two and send the
removal again. A `404` on the repeat means the setting is already gone.

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `plugin_id: String`

  ID of the Plugin (prefixed `plugin_`).

- `target: String`

  The target whose own setting is removed: the literal `organization` for the Plugin's organization-wide setting, or an RBAC Group's ID (prefixed `rbac_group_`) for that group's own setting. Removing the `organization` setting returns the Plugin to its marketplace's default.

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaDeletedPluginInstallationSetting`

  Confirmation that one target's installation setting was removed, naming
  the Plugin and the target in place of an ID.

  - `type: :plugin_installation_setting_deleted`

    Always `plugin_installation_setting_deleted`.

  - `plugin_id: String`

    The Plugin's ID.

  - `target: BetaPluginTargetOrganization | BetaPluginTargetRBACGroup | BetaPluginTargetOrganizationMember`

    Whose setting was removed.

    - `class BetaPluginTargetOrganization`

      - `type: :organization`

        Every member of the organization.

    - `class BetaPluginTargetRBACGroup`

      - `type: :rbac_group`

        An RBAC Group.

      - `rbac_group_id: String`

        The RBAC Group's ID.

    - `class BetaPluginTargetOrganizationMember`

      - `type: :organization_member`

        One member of the organization.

      - `user_id: String`

        The member's User ID.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_deleted_plugin_installation_setting = anthropic.beta.organization.plugins.installation_settings.remove("target", plugin_id: "plugin_id")

puts(beta_deleted_plugin_installation_setting)
```

##### Response (200)

```json
{
  "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "target": {
    "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
    "type": "rbac_group"
  },
  "type": "plugin_installation_setting_deleted"
}
```

## Beta › Organization › Plugins › Shares

### List Plugin Shares

`beta.organization.plugins.shares.list(plugin_id, **kwargs) -> PageCursor<BetaPluginShare>`

**GET** `/v1/organizations/plugins/{plugin_id}/shares`

List the shares the owner of a member-owned Plugin has given — to every member of
the organization, to an RBAC Group, or to one member — most recently granted first.

Shares are read-only in this API: members give and withdraw them in claude.ai, and
who gave a share is recorded on the Compliance API activity feed rather than on the
share. An organization-owned Plugin has installation settings instead, so this path
returns 404 for one.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `plugin_id: String`

  ID of the Plugin (prefixed `plugin_`).

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `100`.

  minimum: 1, maximum: 100

- `organization_id: String`

  For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `page: String`

  Optionally set to the `next_page` token from the previous response.

  maxLength: 2048

- `target_type: :organization | :organization_member | :rbac_group`

  Only shares with this kind of target: `organization` (every member), `rbac_group` (one RBAC Group), or `organization_member` (one member).

  - `:organization`

  - `:organization_member`

  - `:rbac_group`

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaPluginShare`

  One share the owner of a member-owned Plugin has given. Shares are
  read-only in this API and have no ID of their own; who gave a share is
  recorded on the Compliance API activity feed, not here.

  - `type: :plugin_share`

    Always `plugin_share`.

  - `granted_at: Time`

    When the share was given; a share whose role is later changed in claude.ai is re-granted and carries the time of that change.

    format: date-time

  - `plugin_id: String`

    The Plugin's ID.

  - `target: BetaPluginTargetOrganization | BetaPluginTargetRBACGroup | BetaPluginTargetOrganizationMember`

    Who the Plugin is shared with: `organization` (every member), `rbac_group` (one RBAC Group), or `organization_member` (one member).

    - `class BetaPluginTargetOrganization`

      - `type: :organization`

        Every member of the organization.

    - `class BetaPluginTargetRBACGroup`

      - `type: :rbac_group`

        An RBAC Group.

      - `rbac_group_id: String`

        The RBAC Group's ID.

    - `class BetaPluginTargetOrganizationMember`

      - `type: :organization_member`

        One member of the organization.

      - `user_id: String`

        The member's User ID.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.plugins.shares.list("plugin_id")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "granted_at": "2026-03-14T09:26:53.589793Z",
      "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
      "target": {
        "type": "organization"
      },
      "type": "plugin_share"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
}
```

## Beta › Organization › Plugin Marketplaces

### List Plugin Marketplaces

`beta.organization.plugin_marketplaces.list(**kwargs) -> PageCursor<BetaPluginMarketplace>`

**GET** `/v1/organizations/plugin_marketplaces`

List the plugin marketplaces Plugins live in, newest first: the organization's own
and its members' personal ones.

Plugin marketplaces are created, connected to a repository and deleted in
claude.ai, not through this API. The organization's library marketplace, the
organization-owned `manual` marketplace that uploads go to when no marketplace is
named, is created the first time something is put in it and is listed from then on.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `organization_id: String`

  For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `owner_type: :organization | :user`

  `organization` for the organization's plugin marketplaces, `user` for members' personal plugin marketplaces.

  - `:organization`

  - `:user`

- `page: String`

  Optionally set to the `next_page` token from the previous response.

  maxLength: 2048

- `source: :directory | :github | :gitlab | 2 more`

  Only plugin marketplaces with this `source`: `manual` for those whose Plugins are uploaded; `github`, `gitlab` or `public_git` for those synchronized from a Git repository. `directory` (Anthropic's catalog) is never listed here.

  - `:directory`

  - `:github`

  - `:gitlab`

  - `:manual`

  - `:public_git`

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaPluginMarketplace`

  - `type: :plugin_marketplace`

    Always `plugin_marketplace`.

  - `id: String`

    The plugin marketplace's ID, prefixed `marketplace_`.

  - `created_at: Time`

    RFC 3339.

    format: date-time

  - `default_installation_preference: :auto_install | :available | :not_available | :required`

    Organization plugin marketplace: the organization-wide setting every Plugin in it with no setting of its own gets. Null for a member's personal plugin marketplace. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `:auto_install`

    - `:available`

    - `:not_available`

    - `:required`

  - `last_sync_ended_at: Time`

    RFC 3339. When the most recent synchronization attempt to finish did so, whatever its outcome; for a repository plugin marketplace no synchronization has run on yet, when it was created. Null for a plugin marketplace that is not synchronized from a repository.

    format: date-time

  - `last_sync_read_sha: String`

    The commit the last synchronization attempt that reached the repository read, whether or not its content was then accepted (see `sync_status`); an attempt that ends `failed_auth` or `failed_transient` leaves it unchanged. Null until an attempt has first read the repository, and for a plugin marketplace that is not synchronized from a repository.

  - `name: String`

    Fixed for the plugin marketplace's lifetime.

  - `owner: BetaPluginOwnerOrganization | BetaPluginOwnerUser`

    The organization, or the member whose personal plugin marketplace it is.

    - `class BetaPluginOwnerOrganization`

      - `type: :organization`

        The Plugin lives in a plugin marketplace the organization owns.

    - `class BetaPluginOwnerUser`

      - `type: :user`

        The Plugin lives in one member's personal plugin marketplace.

      - `user_id: String`

        The member's User ID.

  - `source: :directory | :github | :gitlab | 2 more`

    Where the plugin marketplace's Plugins come from: `manual` when they are uploaded; `github`, `gitlab` or `public_git` when they are synchronized from the Git repository the owner connected, into which nothing can be uploaded; `directory` is Anthropic's own catalog, which this API does not list. A value this API does not yet name is returned as stored.

    - `:directory`

    - `:github`

    - `:gitlab`

    - `:manual`

    - `:public_git`

  - `sync_status: :failed_auth | :failed_content | :failed_limits | 3 more`

    Outcome of the plugin marketplace's most recent synchronization: one of `success`, `in_progress`, `failed_content`, `failed_transient`, `failed_auth`, `failed_limits`; a value this API does not yet name is returned as stored. Null until a synchronization is first attempted — so always for a `manual` plugin marketplace.

    - `:failed_auth`

    - `:failed_content`

    - `:failed_limits`

    - `:failed_transient`

    - `:in_progress`

    - `:success`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.plugin_marketplaces.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
      "created_at": "2026-03-14T09:26:53.589793Z",
      "default_installation_preference": "available",
      "last_sync_ended_at": "2026-03-14T09:26:53.589793Z",
      "last_sync_read_sha": "9fceb02d0ae598e95dc970b74767f19372d61af8",
      "name": "engineering-tools",
      "owner": {
        "type": "organization"
      },
      "source": "github",
      "sync_status": "success",
      "type": "plugin_marketplace"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
}
```

### Get Plugin Marketplace

`beta.organization.plugin_marketplaces.retrieve(marketplace_id, **kwargs) -> BetaPluginMarketplace`

**GET** `/v1/organizations/plugin_marketplaces/{marketplace_id}`

Retrieve a plugin marketplace by ID.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `marketplace_id: String`

  ID of the plugin marketplace (prefixed `marketplace_`).

- `organization_id: String`

  For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaPluginMarketplace`

  - `type: :plugin_marketplace`

    Always `plugin_marketplace`.

  - `id: String`

    The plugin marketplace's ID, prefixed `marketplace_`.

  - `created_at: Time`

    RFC 3339.

    format: date-time

  - `default_installation_preference: :auto_install | :available | :not_available | :required`

    Organization plugin marketplace: the organization-wide setting every Plugin in it with no setting of its own gets. Null for a member's personal plugin marketplace. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `:auto_install`

    - `:available`

    - `:not_available`

    - `:required`

  - `last_sync_ended_at: Time`

    RFC 3339. When the most recent synchronization attempt to finish did so, whatever its outcome; for a repository plugin marketplace no synchronization has run on yet, when it was created. Null for a plugin marketplace that is not synchronized from a repository.

    format: date-time

  - `last_sync_read_sha: String`

    The commit the last synchronization attempt that reached the repository read, whether or not its content was then accepted (see `sync_status`); an attempt that ends `failed_auth` or `failed_transient` leaves it unchanged. Null until an attempt has first read the repository, and for a plugin marketplace that is not synchronized from a repository.

  - `name: String`

    Fixed for the plugin marketplace's lifetime.

  - `owner: BetaPluginOwnerOrganization | BetaPluginOwnerUser`

    The organization, or the member whose personal plugin marketplace it is.

    - `class BetaPluginOwnerOrganization`

      - `type: :organization`

        The Plugin lives in a plugin marketplace the organization owns.

    - `class BetaPluginOwnerUser`

      - `type: :user`

        The Plugin lives in one member's personal plugin marketplace.

      - `user_id: String`

        The member's User ID.

  - `source: :directory | :github | :gitlab | 2 more`

    Where the plugin marketplace's Plugins come from: `manual` when they are uploaded; `github`, `gitlab` or `public_git` when they are synchronized from the Git repository the owner connected, into which nothing can be uploaded; `directory` is Anthropic's own catalog, which this API does not list. A value this API does not yet name is returned as stored.

    - `:directory`

    - `:github`

    - `:gitlab`

    - `:manual`

    - `:public_git`

  - `sync_status: :failed_auth | :failed_content | :failed_limits | 3 more`

    Outcome of the plugin marketplace's most recent synchronization: one of `success`, `in_progress`, `failed_content`, `failed_transient`, `failed_auth`, `failed_limits`; a value this API does not yet name is returned as stored. Null until a synchronization is first attempted — so always for a `manual` plugin marketplace.

    - `:failed_auth`

    - `:failed_content`

    - `:failed_limits`

    - `:failed_transient`

    - `:in_progress`

    - `:success`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_plugin_marketplace = anthropic.beta.organization.plugin_marketplaces.retrieve("marketplace_id")

puts(beta_plugin_marketplace)
```

##### Response (200)

```json
{
  "id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
  "created_at": "2026-03-14T09:26:53.589793Z",
  "default_installation_preference": "available",
  "last_sync_ended_at": "2026-03-14T09:26:53.589793Z",
  "last_sync_read_sha": "9fceb02d0ae598e95dc970b74767f19372d61af8",
  "name": "engineering-tools",
  "owner": {
    "type": "organization"
  },
  "source": "github",
  "sync_status": "success",
  "type": "plugin_marketplace"
}
```

### Update Plugin Marketplace

`beta.organization.plugin_marketplaces.update(marketplace_id, **kwargs) -> BetaPluginMarketplace`

**POST** `/v1/organizations/plugin_marketplaces/{marketplace_id}`

Set the default installation setting of one of the organization's own plugin
marketplaces. Every Plugin in it without a setting of its own gets this default as
its organization-wide setting, including Plugins added later.

Pass it as `default_installation_preference`. A member's personal marketplace
cannot be updated here (403).

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `marketplace_id: String`

  ID of the plugin marketplace (prefixed `marketplace_`).

- `default_installation_preference: :auto_install | :available | :not_available | :required`

  The organization-wide installation setting every Plugin in the marketplace without one of its own gets: one of `required`, `auto_install`, `available`, `not_available`. Once set it can be changed but not removed.

  - `:auto_install`

  - `:available`

  - `:not_available`

  - `:required`

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaPluginMarketplace`

  - `type: :plugin_marketplace`

    Always `plugin_marketplace`.

  - `id: String`

    The plugin marketplace's ID, prefixed `marketplace_`.

  - `created_at: Time`

    RFC 3339.

    format: date-time

  - `default_installation_preference: :auto_install | :available | :not_available | :required`

    Organization plugin marketplace: the organization-wide setting every Plugin in it with no setting of its own gets. Null for a member's personal plugin marketplace. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `:auto_install`

    - `:available`

    - `:not_available`

    - `:required`

  - `last_sync_ended_at: Time`

    RFC 3339. When the most recent synchronization attempt to finish did so, whatever its outcome; for a repository plugin marketplace no synchronization has run on yet, when it was created. Null for a plugin marketplace that is not synchronized from a repository.

    format: date-time

  - `last_sync_read_sha: String`

    The commit the last synchronization attempt that reached the repository read, whether or not its content was then accepted (see `sync_status`); an attempt that ends `failed_auth` or `failed_transient` leaves it unchanged. Null until an attempt has first read the repository, and for a plugin marketplace that is not synchronized from a repository.

  - `name: String`

    Fixed for the plugin marketplace's lifetime.

  - `owner: BetaPluginOwnerOrganization | BetaPluginOwnerUser`

    The organization, or the member whose personal plugin marketplace it is.

    - `class BetaPluginOwnerOrganization`

      - `type: :organization`

        The Plugin lives in a plugin marketplace the organization owns.

    - `class BetaPluginOwnerUser`

      - `type: :user`

        The Plugin lives in one member's personal plugin marketplace.

      - `user_id: String`

        The member's User ID.

  - `source: :directory | :github | :gitlab | 2 more`

    Where the plugin marketplace's Plugins come from: `manual` when they are uploaded; `github`, `gitlab` or `public_git` when they are synchronized from the Git repository the owner connected, into which nothing can be uploaded; `directory` is Anthropic's own catalog, which this API does not list. A value this API does not yet name is returned as stored.

    - `:directory`

    - `:github`

    - `:gitlab`

    - `:manual`

    - `:public_git`

  - `sync_status: :failed_auth | :failed_content | :failed_limits | 3 more`

    Outcome of the plugin marketplace's most recent synchronization: one of `success`, `in_progress`, `failed_content`, `failed_transient`, `failed_auth`, `failed_limits`; a value this API does not yet name is returned as stored. Null until a synchronization is first attempted — so always for a `manual` plugin marketplace.

    - `:failed_auth`

    - `:failed_content`

    - `:failed_limits`

    - `:failed_transient`

    - `:in_progress`

    - `:success`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_plugin_marketplace = anthropic.beta.organization.plugin_marketplaces.update(
  "marketplace_id",
  default_installation_preference: :available
)

puts(beta_plugin_marketplace)
```

##### Response (200)

```json
{
  "id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
  "created_at": "2026-03-14T09:26:53.589793Z",
  "default_installation_preference": "available",
  "last_sync_ended_at": "2026-03-14T09:26:53.589793Z",
  "last_sync_read_sha": "9fceb02d0ae598e95dc970b74767f19372d61af8",
  "name": "engineering-tools",
  "owner": {
    "type": "organization"
  },
  "source": "github",
  "sync_status": "success",
  "type": "plugin_marketplace"
}
```

### Validate Plugin Marketplace Repository

`beta.organization.plugin_marketplaces.validate_repository(**kwargs) -> BetaPluginMarketplaceValidationReport`

**POST** `/v1/organizations/plugin_marketplaces/validate_repository`

Check whether a plugin marketplace held in a public GitHub repository would
synchronize into claude.ai, without connecting or storing it.

To check a `.zip` of the marketplace directory instead, use Validate Plugin Marketplace Archive.

The report says whether `marketplace.json` is well-formed, which plugins a
synchronization would skip and why, and which plugins would synchronize only in
part, with some files left out. A repository that is missing, private, or has no such branch or commit is reported, not refused: the response is a report with `valid: false`. Plugin sources outside the marketplace
are fetched anonymously from GitHub, so a private one is reported as not found; a
source on any other host is not fetched here, and the report notes that it will be
checked when the marketplace actually synchronizes.

Nothing is recorded on the Compliance API activity feed.

For a worked example, see [Validate marketplace content](https://platform.claude.com/docs/en/manage-claude/plugins-api#validate-marketplace-content)
in the Plugins API guide.

**Accepted credentials:** an Admin API key with the `read:plugins` or `write:plugins` scope; `read:org_audit` and `read:compliance_org_data` do not grant it.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `repository_url: String`

  The `https://` URL of a public repository on github.com that holds the marketplace. Any other host, a URL with credentials in it, or one that does not name a repository is a 400.

  minLength: 1

- `ref: String`

  The branch to validate the tip of, or the full 40-character SHA of the commit to validate. When omitted, the branch a synchronization would read (usually the repository's default branch); if that is not the default branch, the report's `ref` says which branch was read. An empty string, or a value that is neither a branch name nor a 40-character SHA, is a 400.

  minLength: 1

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaPluginMarketplaceValidationReport`

  The outcome of validating plugin marketplace content: a report, not a
  stored object, so nothing in it can be retrieved afterwards.

  - `type: :plugin_marketplace_validation_report`

    Always `plugin_marketplace_validation_report`.

  - `commit_sha: String`

    The full SHA of the commit that was validated: for a repository, the commit that was read; for an uploaded archive, the commit recorded in the archive's comment (as a Git host's download writes it; not verified), else null.

  - `manifest_error: String`

    Set when nothing could be validated: the repository or archive could not be read, or marketplace.json is missing, malformed or over a limit. Null otherwise.

  - `manifest_error_code: String`

    A stable identifier for `manifest_error`; null when that is.

  - `plugin_errors: Array[BetaPluginMarketplaceValidationPluginError]`

    One entry per plugin a synchronization would skip entirely, keyed by the plugin's name in marketplace.json.

    - `error: String`

      Why the plugin would be skipped by a synchronization.

    - `error_code: String`

      A stable identifier for the reason — the value to branch on.

    - `name: String`

      The plugin's name, as its entry in marketplace.json declares it.

  - `plugin_warnings: Array[BetaPluginMarketplaceValidationPluginWarnings]`

    One entry per plugin that would synchronize with some of its contents left out, keyed by the plugin's name in marketplace.json.

    - `name: String`

      The plugin's name, as its entry in marketplace.json declares it.

    - `warnings: Array[BetaPluginMarketplaceValidationPluginWarning]`

      The parts of the plugin a synchronization would leave out.

      - `error_code: String`

        A stable identifier for the kind of warning.

      - `message: String`

        What would be left out, and why.

  - `ref: String`

    For a repository, the branch that was read by name: the one requested, or else the branch a synchronization of this repository is set to read. Null when no branch is named or set and the repository's default branch was read, for a request by commit SHA, and for an uploaded archive.

  - `total_plugin_count: Integer`

    How many plugins marketplace.json declares; 0 when it could not be read.

  - `valid: bool`

    True when marketplace.json is well-formed and no plugin would be skipped; warnings never make it false.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_plugin_marketplace_validation_report = anthropic.beta.organization.plugin_marketplaces.validate_repository(
  repository_url: "https://github.com/example-org/example-marketplace"
)

puts(beta_plugin_marketplace_validation_report)
```

##### Response (200)

```json
{
  "commit_sha": "9fceb02d0ae598e95dc970b74767f19372d61af8",
  "manifest_error": "manifest_error",
  "manifest_error_code": "marketplace_sync_manifest_not_found",
  "plugin_errors": [
    {
      "error": "error",
      "error_code": "marketplace_sync_plugin_missing_manifest",
      "name": "name"
    }
  ],
  "plugin_warnings": [
    {
      "name": "name",
      "warnings": [
        {
          "error_code": "marketplace_sync_zipball_symlink_dangling",
          "message": "message"
        }
      ]
    }
  ],
  "ref": "main",
  "total_plugin_count": 0,
  "type": "plugin_marketplace_validation_report",
  "valid": false
}
```

### Validate Plugin Marketplace Archive

`beta.organization.plugin_marketplaces.validate_archive(**kwargs) -> BetaPluginMarketplaceValidationReport`

**POST** `/v1/organizations/plugin_marketplaces/validate_archive`

Check whether a plugin marketplace, uploaded as a `.zip` of the marketplace
directory, would synchronize into claude.ai, without connecting or storing it.

To check a public GitHub repository instead, use Validate Plugin Marketplace Repository.

The report says whether `marketplace.json` is well-formed, which plugins a
synchronization would skip and why, and which plugins would synchronize only in
part, with some files left out. An archive that cannot be read as a marketplace is reported, not refused: the response is a report with `valid: false`. Plugin sources outside the marketplace
are fetched anonymously from GitHub, so a private one is reported as not found; a
source on any other host is not fetched here, and the report notes that it will be
checked when the marketplace actually synchronizes.

Nothing is recorded on the Compliance API activity feed.

For a worked example, see [Validate marketplace content](https://platform.claude.com/docs/en/manage-claude/plugins-api#validate-marketplace-content)
in the Plugins API guide.

**Accepted credentials:** an Admin API key with the `read:plugins` or `write:plugins` scope; `read:org_audit` and `read:compliance_org_data` do not grant it.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `archive: String`

  A .zip of the marketplace directory (its contents at the root, or wrapped in one folder as a Git host's download produces), sent as a file part with a filename; DEFLATE- or STORE-compressed, at most 32 MB. A part sent without a filename, a second archive part, or any other form field is a 400; a larger archive is a 413.

  format: binary

- `betas: Array[AnthropicBeta]`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

#### Returns

- `class BetaPluginMarketplaceValidationReport`

  The outcome of validating plugin marketplace content: a report, not a
  stored object, so nothing in it can be retrieved afterwards.

  - `type: :plugin_marketplace_validation_report`

    Always `plugin_marketplace_validation_report`.

  - `commit_sha: String`

    The full SHA of the commit that was validated: for a repository, the commit that was read; for an uploaded archive, the commit recorded in the archive's comment (as a Git host's download writes it; not verified), else null.

  - `manifest_error: String`

    Set when nothing could be validated: the repository or archive could not be read, or marketplace.json is missing, malformed or over a limit. Null otherwise.

  - `manifest_error_code: String`

    A stable identifier for `manifest_error`; null when that is.

  - `plugin_errors: Array[BetaPluginMarketplaceValidationPluginError]`

    One entry per plugin a synchronization would skip entirely, keyed by the plugin's name in marketplace.json.

    - `error: String`

      Why the plugin would be skipped by a synchronization.

    - `error_code: String`

      A stable identifier for the reason — the value to branch on.

    - `name: String`

      The plugin's name, as its entry in marketplace.json declares it.

  - `plugin_warnings: Array[BetaPluginMarketplaceValidationPluginWarnings]`

    One entry per plugin that would synchronize with some of its contents left out, keyed by the plugin's name in marketplace.json.

    - `name: String`

      The plugin's name, as its entry in marketplace.json declares it.

    - `warnings: Array[BetaPluginMarketplaceValidationPluginWarning]`

      The parts of the plugin a synchronization would leave out.

      - `error_code: String`

        A stable identifier for the kind of warning.

      - `message: String`

        What would be left out, and why.

  - `ref: String`

    For a repository, the branch that was read by name: the one requested, or else the branch a synchronization of this repository is set to read. Null when no branch is named or set and the repository's default branch was read, for a request by commit SHA, and for an uploaded archive.

  - `total_plugin_count: Integer`

    How many plugins marketplace.json declares; 0 when it could not be read.

  - `valid: bool`

    True when marketplace.json is well-formed and no plugin would be skipped; warnings never make it false.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_plugin_marketplace_validation_report = anthropic.beta.organization.plugin_marketplaces.validate_archive(archive: StringIO.new("Example data"))

puts(beta_plugin_marketplace_validation_report)
```

##### Response (200)

```json
{
  "commit_sha": "9fceb02d0ae598e95dc970b74767f19372d61af8",
  "manifest_error": "manifest_error",
  "manifest_error_code": "marketplace_sync_manifest_not_found",
  "plugin_errors": [
    {
      "error": "error",
      "error_code": "marketplace_sync_plugin_missing_manifest",
      "name": "name"
    }
  ],
  "plugin_warnings": [
    {
      "name": "name",
      "warnings": [
        {
          "error_code": "marketplace_sync_zipball_symlink_dangling",
          "message": "message"
        }
      ]
    }
  ],
  "ref": "main",
  "total_plugin_count": 0,
  "type": "plugin_marketplace_validation_report",
  "valid": false
}
```
