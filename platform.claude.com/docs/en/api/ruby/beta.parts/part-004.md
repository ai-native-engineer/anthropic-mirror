<!-- source: https://platform.claude.com/docs/en/api/ruby/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/ruby/beta -->

<!-- chunk-start -->

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_store = anthropic.beta.memory_stores.archive("memory_store_id")

puts(beta_managed_agents_memory_store)
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

- `class BetaManagedAgentsDeletedMemoryStore`

  Confirmation that a `memory_store` was deleted.

  - `id: String`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `type: :memory_store_deleted`

    - `:memory_store_deleted`

### Beta Managed Agents Memory Store

- `class BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: String`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `name: String`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: :memory_store`

    - `:memory_store`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `description: String`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

# Memories

## Create a memory

`beta.memory_stores.memories.create(memory_store_id, **kwargs) -> BetaManagedAgentsMemory`

**post** `/v1/memory_stores/{memory_store_id}/memories`

Create a memory

### Parameters

- `memory_store_id: String`

- `content: String`

  UTF-8 text content for the new memory. Maximum 100 kB (102,400 bytes). Required; pass `""` explicitly to create an empty memory.

- `path: String`

  Hierarchical path for the new memory, e.g. `/projects/foo/notes.md`. Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive.

- `view: BetaManagedAgentsMemoryView`

  Query parameter for view

  - `:basic`

  - `:full`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaManagedAgentsMemory`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: String`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: Integer`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `memory_store_id: String`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: String`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: String`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: :memory`

    - `:memory`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `content: String`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory = anthropic.beta.memory_stores.memories.create("memory_store_id", content: "content", path: "xx")

puts(beta_managed_agents_memory)
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

`beta.memory_stores.memories.list(memory_store_id, **kwargs) -> PageCursor<BetaManagedAgentsMemoryListItem>`

**get** `/v1/memory_stores/{memory_store_id}/memories`

List memories

### Parameters

- `memory_store_id: String`

- `depth: Integer`

  `0` (or omitted) returns all descendants below `path_prefix` (recursive). `1` returns immediate children only; deeper entries roll up as `memory_prefix` items. `depth=1` behaves like `ls`; omitting `depth` behaves like `find`.

- `limit: Integer`

  Maximum number of items to return per page. Must be between 1 and 100. Defaults to 20 when omitted. Capped at 20 when `view=full`. Both `memory` and `memory_prefix` items count toward the limit.

- `page: String`

  Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

- `path_prefix: String`

  Optional path prefix filter. Must end with `/` (segment-aligned), e.g., `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

- `view: BetaManagedAgentsMemoryView`

  Which projection of each `memory` to return. Defaults to `basic` (content omitted). `full` populates `content` on each item and caps `limit` at 20; use this as the bulk-read path for export and sync.

  - `:basic`

  - `:full`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `BetaManagedAgentsMemoryListItem = BetaManagedAgentsMemory | BetaManagedAgentsMemoryPrefix`

  One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

  - `class BetaManagedAgentsMemory`

    A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

    - `id: String`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `content_sha256: String`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `content_size_bytes: Integer`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `created_at: Time`

      A timestamp in RFC 3339 format

    - `memory_store_id: String`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `memory_version_id: String`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `path: String`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `type: :memory`

      - `:memory`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

    - `content: String`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `class BetaManagedAgentsMemoryPrefix`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `path: String`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `type: :memory_prefix`

      - `:memory_prefix`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.memory_stores.memories.list("memory_store_id")

puts(page)
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

`beta.memory_stores.memories.retrieve(memory_id, **kwargs) -> BetaManagedAgentsMemory`

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a memory

### Parameters

- `memory_store_id: String`

- `memory_id: String`

- `view: BetaManagedAgentsMemoryView`

  Query parameter for view

  - `:basic`

  - `:full`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaManagedAgentsMemory`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: String`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: Integer`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `memory_store_id: String`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: String`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: String`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: :memory`

    - `:memory`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `content: String`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory = anthropic.beta.memory_stores.memories.retrieve("memory_id", memory_store_id: "memory_store_id")

puts(beta_managed_agents_memory)
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

`beta.memory_stores.memories.update(memory_id, **kwargs) -> BetaManagedAgentsMemory`

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a memory

### Parameters

- `memory_store_id: String`

- `memory_id: String`

- `view: BetaManagedAgentsMemoryView`

  Query parameter for view

  - `:basic`

  - `:full`

- `content: String`

  New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

- `path: String`

  New path for the memory (a rename). Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive. The memory's `id` is preserved across renames. Omit to leave the path unchanged.

- `precondition: BetaManagedAgentsPrecondition`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `type: :content_sha256`

    - `:content_sha256`

  - `content_sha256: String`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaManagedAgentsMemory`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: String`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: Integer`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `memory_store_id: String`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: String`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: String`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: :memory`

    - `:memory`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `content: String`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory = anthropic.beta.memory_stores.memories.update("memory_id", memory_store_id: "memory_store_id")

puts(beta_managed_agents_memory)
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

`beta.memory_stores.memories.delete(memory_id, **kwargs) -> BetaManagedAgentsDeletedMemory`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

### Parameters

- `memory_store_id: String`

- `memory_id: String`

- `expected_content_sha256: String`

  Query parameter for expected_content_sha256

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaManagedAgentsDeletedMemory`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `id: String`

    ID of the deleted memory (a `mem_...` value).

  - `type: :memory_deleted`

    - `:memory_deleted`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deleted_memory = anthropic.beta.memory_stores.memories.delete("memory_id", memory_store_id: "memory_store_id")

puts(beta_managed_agents_deleted_memory)
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

- `class BetaManagedAgentsConflictError`

  - `type: :conflict_error`

    - `:conflict_error`

  - `message: String`

### Beta Managed Agents Content Sha256 Precondition

- `class BetaManagedAgentsContentSha256Precondition`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `type: :content_sha256`

    - `:content_sha256`

  - `content_sha256: String`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

### Beta Managed Agents Deleted Memory

- `class BetaManagedAgentsDeletedMemory`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `id: String`

    ID of the deleted memory (a `mem_...` value).

  - `type: :memory_deleted`

    - `:memory_deleted`

### Beta Managed Agents Error

- `BetaManagedAgentsError = BetaInvalidRequestError | BetaAuthenticationError | BetaBillingError | 9 more`

  - `class BetaInvalidRequestError`

    - `message: String`

    - `type: :invalid_request_error`

      - `:invalid_request_error`

  - `class BetaAuthenticationError`

    - `message: String`

    - `type: :authentication_error`

      - `:authentication_error`

  - `class BetaBillingError`

    - `message: String`

    - `type: :billing_error`

      - `:billing_error`

  - `class BetaPermissionError`

    - `message: String`

    - `type: :permission_error`

      - `:permission_error`

  - `class BetaNotFoundError`

    - `message: String`

    - `type: :not_found_error`

      - `:not_found_error`

  - `class BetaRateLimitError`

    - `message: String`

    - `type: :rate_limit_error`

      - `:rate_limit_error`

  - `class BetaGatewayTimeoutError`

    - `message: String`

    - `type: :timeout_error`

      - `:timeout_error`

  - `class BetaAPIError`

    - `message: String`

    - `type: :api_error`

      - `:api_error`

  - `class BetaOverloadedError`

    - `message: String`

    - `type: :overloaded_error`

      - `:overloaded_error`

  - `class BetaManagedAgentsMemoryPreconditionFailedError`

    - `type: :memory_precondition_failed_error`

      - `:memory_precondition_failed_error`

    - `message: String`

  - `class BetaManagedAgentsMemoryPathConflictError`

    - `type: :memory_path_conflict_error`

      - `:memory_path_conflict_error`

    - `conflicting_memory_id: String`

    - `conflicting_path: String`

    - `message: String`

  - `class BetaManagedAgentsConflictError`

    - `type: :conflict_error`

      - `:conflict_error`

    - `message: String`

### Beta Managed Agents Memory

- `class BetaManagedAgentsMemory`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: String`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: Integer`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `memory_store_id: String`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: String`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: String`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: :memory`

    - `:memory`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `content: String`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Beta Managed Agents Memory List Item

- `BetaManagedAgentsMemoryListItem = BetaManagedAgentsMemory | BetaManagedAgentsMemoryPrefix`

  One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

  - `class BetaManagedAgentsMemory`

    A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

    - `id: String`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `content_sha256: String`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `content_size_bytes: Integer`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `created_at: Time`

      A timestamp in RFC 3339 format

    - `memory_store_id: String`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `memory_version_id: String`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `path: String`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `type: :memory`

      - `:memory`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

    - `content: String`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `class BetaManagedAgentsMemoryPrefix`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `path: String`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `type: :memory_prefix`

      - `:memory_prefix`

### Beta Managed Agents Memory Path Conflict Error

- `class BetaManagedAgentsMemoryPathConflictError`

  - `type: :memory_path_conflict_error`

    - `:memory_path_conflict_error`

  - `conflicting_memory_id: String`

  - `conflicting_path: String`

  - `message: String`

### Beta Managed Agents Memory Precondition Failed Error

- `class BetaManagedAgentsMemoryPreconditionFailedError`

  - `type: :memory_precondition_failed_error`

    - `:memory_precondition_failed_error`

  - `message: String`

### Beta Managed Agents Memory Prefix

- `class BetaManagedAgentsMemoryPrefix`

  A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

  - `path: String`

    The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

  - `type: :memory_prefix`

    - `:memory_prefix`

### Beta Managed Agents Memory View

- `BetaManagedAgentsMemoryView = :basic | :full`

  Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

  - `:basic`

  - `:full`

### Beta Managed Agents Precondition

- `class BetaManagedAgentsPrecondition`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `type: :content_sha256`

    - `:content_sha256`

  - `content_sha256: String`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

# Memory Versions

## List memory versions

`beta.memory_stores.memory_versions.list(memory_store_id, **kwargs) -> PageCursor<BetaManagedAgentsMemoryVersion>`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

### Parameters

- `memory_store_id: String`

- `api_key_id: String`

  Query parameter for api_key_id

- `created_at_gte: Time`

  Return versions created at or after this time (inclusive).

- `created_at_lte: Time`

  Return versions created at or before this time (inclusive).

- `limit: Integer`

  Query parameter for limit

- `memory_id: String`

  Query parameter for memory_id

- `operation: BetaManagedAgentsMemoryVersionOperation`

  Query parameter for operation

  - `:created`

  - `:modified`

  - `:deleted`

- `page: String`

  Query parameter for page

- `service_account_id: String`

  Query parameter for service_account_id

- `session_id: String`

  Query parameter for session_id

- `view: BetaManagedAgentsMemoryView`

  Query parameter for view

  - `:basic`

  - `:full`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaManagedAgentsMemoryVersion`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: String`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `memory_id: String`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: String`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `:created`

    - `:modified`

    - `:deleted`

  - `type: :memory_version`

    - `:memory_version`

  - `content: String`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: Integer`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: String`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: :session_actor`

        - `:session_actor`

    - `class BetaManagedAgentsAPIActor`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: String`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: :api_actor`

        - `:api_actor`

    - `class BetaManagedAgentsUserActor`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: :user_actor`

        - `:user_actor`

      - `user_id: String`

        ID of the user who performed the write (a `user_...` value).

    - `class BetaManagedAgentsServiceAccountActor`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `service_account_id: String`

        ID of the service account that performed the write (a `svac_...` value).

      - `type: :service_account_actor`

        - `:service_account_actor`

  - `path: String`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: Time`

    A timestamp in RFC 3339 format

  - `redacted_by: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.memory_stores.memory_versions.list("memory_store_id")

puts(page)
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

`beta.memory_stores.memory_versions.retrieve(memory_version_id, **kwargs) -> BetaManagedAgentsMemoryVersion`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

### Parameters

- `memory_store_id: String`

- `memory_version_id: String`

- `view: BetaManagedAgentsMemoryView`

  Query parameter for view

  - `:basic`

  - `:full`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaManagedAgentsMemoryVersion`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: String`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `memory_id: String`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: String`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `:created`

    - `:modified`

    - `:deleted`

  - `type: :memory_version`

    - `:memory_version`

  - `content: String`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: Integer`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: String`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: :session_actor`

        - `:session_actor`

    - `class BetaManagedAgentsAPIActor`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: String`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: :api_actor`

        - `:api_actor`

    - `class BetaManagedAgentsUserActor`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: :user_actor`

        - `:user_actor`

      - `user_id: String`

        ID of the user who performed the write (a `user_...` value).

    - `class BetaManagedAgentsServiceAccountActor`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `service_account_id: String`

        ID of the service account that performed the write (a `svac_...` value).

      - `type: :service_account_actor`

        - `:service_account_actor`

  - `path: String`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: Time`

    A timestamp in RFC 3339 format

  - `redacted_by: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_version = anthropic.beta.memory_stores.memory_versions.retrieve(
  "memory_version_id",
  memory_store_id: "memory_store_id"
)

puts(beta_managed_agents_memory_version)
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

`beta.memory_stores.memory_versions.redact(memory_version_id, **kwargs) -> BetaManagedAgentsMemoryVersion`

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a memory version

### Parameters

- `memory_store_id: String`

- `memory_version_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaManagedAgentsMemoryVersion`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: String`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `memory_id: String`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: String`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `:created`

    - `:modified`

    - `:deleted`

  - `type: :memory_version`

    - `:memory_version`

  - `content: String`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: Integer`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: String`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: :session_actor`

        - `:session_actor`

    - `class BetaManagedAgentsAPIActor`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: String`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: :api_actor`

        - `:api_actor`

    - `class BetaManagedAgentsUserActor`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: :user_actor`

        - `:user_actor`

      - `user_id: String`

        ID of the user who performed the write (a `user_...` value).

    - `class BetaManagedAgentsServiceAccountActor`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `service_account_id: String`

        ID of the service account that performed the write (a `svac_...` value).

      - `type: :service_account_actor`

        - `:service_account_actor`

  - `path: String`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: Time`

    A timestamp in RFC 3339 format

  - `redacted_by: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_version = anthropic.beta.memory_stores.memory_versions.redact(
  "memory_version_id",
  memory_store_id: "memory_store_id"
)

puts(beta_managed_agents_memory_version)
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

  - `class BetaManagedAgentsSessionActor`

    Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

    - `session_id: String`

      ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

    - `type: :session_actor`

      - `:session_actor`

  - `class BetaManagedAgentsAPIActor`

    Attribution for a write made directly via the public API (outside of any session).

    - `api_key_id: String`

      ID of the API key that performed the write. This identifies the key, not the secret.

    - `type: :api_actor`

      - `:api_actor`

  - `class BetaManagedAgentsUserActor`

    Attribution for a write made by a human user through the Anthropic Console.

    - `type: :user_actor`

      - `:user_actor`

    - `user_id: String`

      ID of the user who performed the write (a `user_...` value).

  - `class BetaManagedAgentsServiceAccountActor`

    Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

    - `service_account_id: String`

      ID of the service account that performed the write (a `svac_...` value).

    - `type: :service_account_actor`

      - `:service_account_actor`

### Beta Managed Agents API Actor

- `class BetaManagedAgentsAPIActor`

  Attribution for a write made directly via the public API (outside of any session).

  - `api_key_id: String`

    ID of the API key that performed the write. This identifies the key, not the secret.

  - `type: :api_actor`

    - `:api_actor`

### Beta Managed Agents Memory Version

- `class BetaManagedAgentsMemoryVersion`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: String`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `memory_id: String`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: String`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `:created`

    - `:modified`

    - `:deleted`

  - `type: :memory_version`

    - `:memory_version`

  - `content: String`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: Integer`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: String`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: :session_actor`

        - `:session_actor`

    - `class BetaManagedAgentsAPIActor`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: String`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: :api_actor`

        - `:api_actor`

    - `class BetaManagedAgentsUserActor`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: :user_actor`

        - `:user_actor`

      - `user_id: String`

        ID of the user who performed the write (a `user_...` value).

    - `class BetaManagedAgentsServiceAccountActor`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `service_account_id: String`

        ID of the service account that performed the write (a `svac_...` value).

      - `type: :service_account_actor`

        - `:service_account_actor`

  - `path: String`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: Time`

    A timestamp in RFC 3339 format

  - `redacted_by: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Beta Managed Agents Memory Version Operation

- `BetaManagedAgentsMemoryVersionOperation = :created | :modified | :deleted`

  The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

  - `:created`

  - `:modified`

  - `:deleted`

### Beta Managed Agents Service Account Actor

- `class BetaManagedAgentsServiceAccountActor`

  Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

  - `service_account_id: String`

    ID of the service account that performed the write (a `svac_...` value).

  - `type: :service_account_actor`

    - `:service_account_actor`

### Beta Managed Agents Session Actor

- `class BetaManagedAgentsSessionActor`

  Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

  - `session_id: String`

    ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

  - `type: :session_actor`

    - `:session_actor`

### Beta Managed Agents User Actor

- `class BetaManagedAgentsUserActor`

  Attribution for a write made by a human user through the Anthropic Console.

  - `type: :user_actor`

    - `:user_actor`

  - `user_id: String`

    ID of the user who performed the write (a `user_...` value).

# Files

## Upload File

`beta.files.upload(**kwargs) -> BetaFileMetadata`

**post** `/v1/files`

Upload File

### Parameters

- `file: String`

  The file to upload

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaFileMetadata`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

  - `filename: String`

    Original filename of the uploaded file.

  - `mime_type: String`

    MIME type of the file.

  - `size_bytes: Integer`

    Size of the file in bytes.

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

    - `:file`

  - `downloadable: bool`

    Whether the file can be downloaded.

  - `scope: BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

    - `type: :session`

      The type of scope (e.g., `"session"`).

      - `:session`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_file_metadata = anthropic.beta.files.upload(file: StringIO.new("Example data"))

puts(beta_file_metadata)
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

`beta.files.list(**kwargs) -> Page<BetaFileMetadata>`

**get** `/v1/files`

List Files

### Parameters

- `after_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `scope_id: String`

  Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaFileMetadata`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

  - `filename: String`

    Original filename of the uploaded file.

  - `mime_type: String`

    MIME type of the file.

  - `size_bytes: Integer`

    Size of the file in bytes.

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

    - `:file`

  - `downloadable: bool`

    Whether the file can be downloaded.

  - `scope: BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

    - `type: :session`

      The type of scope (e.g., `"session"`).

      - `:session`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.files.list

puts(page)
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

`beta.files.download(file_id, **kwargs) -> StringIO`

**get** `/v1/files/{file_id}/content`

Download File

### Parameters

- `file_id: String`

  ID of the File.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `StringIO`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

response = anthropic.beta.files.download("file_id")

puts(response)
```

## Get File Metadata

`beta.files.retrieve_metadata(file_id, **kwargs) -> BetaFileMetadata`

**get** `/v1/files/{file_id}`

Get File Metadata

### Parameters

- `file_id: String`

  ID of the File.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaFileMetadata`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

  - `filename: String`

    Original filename of the uploaded file.

  - `mime_type: String`

    MIME type of the file.

  - `size_bytes: Integer`

    Size of the file in bytes.

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

    - `:file`

  - `downloadable: bool`

    Whether the file can be downloaded.

  - `scope: BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

    - `type: :session`

      The type of scope (e.g., `"session"`).

      - `:session`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_file_metadata = anthropic.beta.files.retrieve_metadata("file_id")

puts(beta_file_metadata)
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

`beta.files.delete(file_id, **kwargs) -> BetaDeletedFile`

**delete** `/v1/files/{file_id}`

Delete File

### Parameters

- `file_id: String`

  ID of the File.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaDeletedFile`

  - `id: String`

    ID of the deleted file.

  - `type: :file_deleted`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `:file_deleted`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_deleted_file = anthropic.beta.files.delete("file_id")

puts(beta_deleted_file)
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

- `class BetaDeletedFile`

  - `id: String`

    ID of the deleted file.

  - `type: :file_deleted`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `:file_deleted`

### Beta File Metadata

- `class BetaFileMetadata`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

  - `filename: String`

    Original filename of the uploaded file.

  - `mime_type: String`

    MIME type of the file.

  - `size_bytes: Integer`

    Size of the file in bytes.

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

    - `:file`

  - `downloadable: bool`

    Whether the file can be downloaded.

  - `scope: BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

    - `type: :session`

      The type of scope (e.g., `"session"`).

      - `:session`

### Beta File Scope

- `class BetaFileScope`

  - `id: String`

    The ID of the scoping resource (e.g., the session ID).

  - `type: :session`

    The type of scope (e.g., `"session"`).

    - `:session`

# Skills

## Create Skill

`beta.skills.create(**kwargs) -> SkillCreateResponse`

**post** `/v1/skills`

Create Skill

### Parameters

- `files: Array[String]`

  Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `display_title: String`

  Display title for the skill.

  This is a human-readable label that is not included in the prompt sent to the model.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class SkillCreateResponse`

  - `id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: String`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: String`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: String`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: String`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: String`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

skill = anthropic.beta.skills.create(files: [StringIO.new("Example data")])

puts(skill)
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

`beta.skills.list(**kwargs) -> PageCursor<SkillListResponse>`

**get** `/v1/skills`

List Skills

### Parameters

- `limit: Integer`

  Number of results to return per page.

  Maximum value is 100. Defaults to 20.

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class SkillListResponse`

  - `id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: String`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: String`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: String`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: String`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: String`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.skills.list

puts(page)
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

`beta.skills.retrieve(skill_id, **kwargs) -> SkillRetrieveResponse`

**get** `/v1/skills/{skill_id}`

Get Skill

### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class SkillRetrieveResponse`

  - `id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: String`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: String`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: String`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: String`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: String`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

skill = anthropic.beta.skills.retrieve("skill_id")

puts(skill)
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

`beta.skills.delete(skill_id, **kwargs) -> SkillDeleteResponse`

**delete** `/v1/skills/{skill_id}`

Delete Skill

### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class SkillDeleteResponse`

  - `id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `type: String`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

skill = anthropic.beta.skills.delete("skill_id")

puts(skill)
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

- `class SkillCreateResponse`

  - `id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: String`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: String`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: String`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: String`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: String`

    ISO 8601 timestamp of when the skill was last updated.

### Skill List Response

- `class SkillListResponse`

  - `id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: String`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: String`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: String`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: String`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: String`

    ISO 8601 timestamp of when the skill was last updated.

### Skill Retrieve Response

- `class SkillRetrieveResponse`

  - `id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: String`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: String`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: String`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: String`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: String`

    ISO 8601 timestamp of when the skill was last updated.

### Skill Delete Response

- `class SkillDeleteResponse`

  - `id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `type: String`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

# Versions

## Create Skill Version

`beta.skills.versions.create(skill_id, **kwargs) -> VersionCreateResponse`

**post** `/v1/skills/{skill_id}/versions`

Create Skill Version

### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `files: Array[String]`

  Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class VersionCreateResponse`

  - `id: String`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill version was created.

  - `description: String`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: String`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: String`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: String`

    Identifier for the skill that this version belongs to.

  - `type: String`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: String`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

version = anthropic.beta.skills.versions.create("skill_id", files: [StringIO.new("Example data")])

puts(version)
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

`beta.skills.versions.list(skill_id, **kwargs) -> PageCursor<VersionListResponse>`

**get** `/v1/skills/{skill_id}/versions`

List Skill Versions

### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `page: String`

  Optionally set to the `next_page` token from the previous response.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class VersionListResponse`

  - `id: String`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill version was created.

  - `description: String`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: String`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: String`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: String`

    Identifier for the skill that this version belongs to.

  - `type: String`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: String`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.skills.versions.list("skill_id")

puts(page)
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

`beta.skills.versions.download(version, **kwargs) -> StringIO`

**get** `/v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: String`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `StringIO`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

response = anthropic.beta.skills.versions.download("version", skill_id: "skill_id")

puts(response)
```

## Get Skill Version

`beta.skills.versions.retrieve(version, **kwargs) -> VersionRetrieveResponse`

**get** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: String`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class VersionRetrieveResponse`

  - `id: String`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill version was created.

  - `description: String`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: String`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: String`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: String`

    Identifier for the skill that this version belongs to.

  - `type: String`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: String`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

version = anthropic.beta.skills.versions.retrieve("version", skill_id: "skill_id")

puts(version)
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

`beta.skills.versions.delete(version, **kwargs) -> VersionDeleteResponse`

**delete** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: String`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class VersionDeleteResponse`

  - `id: String`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `type: String`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

version = anthropic.beta.skills.versions.delete("version", skill_id: "skill_id")

puts(version)
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

- `class VersionCreateResponse`

  - `id: String`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill version was created.

  - `description: String`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: String`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: String`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: String`

    Identifier for the skill that this version belongs to.

  - `type: String`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: String`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Version List Response

- `class VersionListResponse`

  - `id: String`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill version was created.

  - `description: String`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: String`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: String`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: String`

    Identifier for the skill that this version belongs to.

  - `type: String`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: String`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Version Retrieve Response

- `class VersionRetrieveResponse`

  - `id: String`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill version was created.

  - `description: String`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: String`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: String`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: String`

    Identifier for the skill that this version belongs to.

  - `type: String`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: String`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Version Delete Response

- `class VersionDeleteResponse`

  - `id: String`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `type: String`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

# User Profiles

## Create User Profile

`beta.user_profiles.create(**kwargs) -> BetaUserProfile`

**post** `/v1/user_profiles`

Create User Profile

### Parameters

- `access_type: :application | :passthrough`

  How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

  - `:application`

  - `:passthrough`

- `external_id: String`

  Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

- `metadata: Hash[Symbol, String]`

  Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

- `name: String`

  Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a resold-to company (`relationship` `resold` / `access_type` `passthrough`), that company's name where known. Maximum 255 characters.

- `relationship: :external | :resold | :internal`

  How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

  - `:external`

  - `:resold`

  - `:internal`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaUserProfile`

  - `id: String`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Hash[Symbol, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: :active | :pending | :rejected`

      Status of the trust grant.

      - `:active`

      - `:pending`

      - `:rejected`

  - `type: :user_profile`

    Object type. Always `user_profile`.

    - `:user_profile`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `access_type: :application | :passthrough`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `:application`

    - `:passthrough`

  - `external_id: String`

    Platform's own identifier for this user. Not enforced unique.

  - `name: String`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: :external | :resold | :internal`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `:external`

    - `:resold`

    - `:internal`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_user_profile = anthropic.beta.user_profiles.create

puts(beta_user_profile)
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

`beta.user_profiles.list(**kwargs) -> PageCursor<BetaUserProfile>`

**get** `/v1/user_profiles`

List User Profiles

### Parameters

- `limit: Integer`

  Query parameter for limit

- `order: :asc | :desc`

  Query parameter for order

  - `:asc`

  - `:desc`

- `page: String`

  Query parameter for page

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaUserProfile`

  - `id: String`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Hash[Symbol, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: :active | :pending | :rejected`

      Status of the trust grant.

      - `:active`

      - `:pending`

      - `:rejected`

  - `type: :user_profile`

    Object type. Always `user_profile`.

    - `:user_profile`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `access_type: :application | :passthrough`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `:application`

    - `:passthrough`

  - `external_id: String`

    Platform's own identifier for this user. Not enforced unique.

  - `name: String`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: :external | :resold | :internal`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `:external`

    - `:resold`

    - `:internal`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.user_profiles.list

puts(page)
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

`beta.user_profiles.retrieve(user_profile_id, **kwargs) -> BetaUserProfile`

**get** `/v1/user_profiles/{user_profile_id}`

Get User Profile

### Parameters

- `user_profile_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaUserProfile`

  - `id: String`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Hash[Symbol, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: :active | :pending | :rejected`

      Status of the trust grant.

      - `:active`

      - `:pending`

      - `:rejected`

  - `type: :user_profile`

    Object type. Always `user_profile`.

    - `:user_profile`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `access_type: :application | :passthrough`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `:application`

    - `:passthrough`

  - `external_id: String`

    Platform's own identifier for this user. Not enforced unique.

  - `name: String`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: :external | :resold | :internal`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `:external`

    - `:resold`

    - `:internal`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_user_profile = anthropic.beta.user_profiles.retrieve("uprof_011CZkZCu8hGbp5mYRQgUmz9")

puts(beta_user_profile)
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

`beta.user_profiles.update(user_profile_id, **kwargs) -> BetaUserProfile`

**post** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `user_profile_id: String`

- `access_type: :application | :passthrough`

  How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

  - `:application`

  - `:passthrough`

- `external_id: String`

  If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

- `metadata: Hash[Symbol, String]`

  Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

- `name: String`

  If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

- `relationship: :external | :resold | :internal`

  How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

  - `:external`

  - `:resold`

  - `:internal`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaUserProfile`

  - `id: String`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Hash[Symbol, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: :active | :pending | :rejected`

      Status of the trust grant.

      - `:active`

      - `:pending`

      - `:rejected`

  - `type: :user_profile`

    Object type. Always `user_profile`.

    - `:user_profile`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `access_type: :application | :passthrough`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `:application`

    - `:passthrough`

  - `external_id: String`

    Platform's own identifier for this user. Not enforced unique.

  - `name: String`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: :external | :resold | :internal`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `:external`

    - `:resold`

    - `:internal`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_user_profile = anthropic.beta.user_profiles.update("uprof_011CZkZCu8hGbp5mYRQgUmz9")

puts(beta_user_profile)
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

`beta.user_profiles.create_enrollment_url(user_profile_id, **kwargs) -> BetaUserProfileEnrollmentURL`

**post** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Parameters

- `user_profile_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaUserProfileEnrollmentURL`

  - `expires_at: Time`

    A timestamp in RFC 3339 format

  - `type: :enrollment_url`

    Object type. Always `enrollment_url`.

    - `:enrollment_url`

  - `url: String`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_user_profile_enrollment_url = anthropic.beta.user_profiles.create_enrollment_url("uprof_011CZkZCu8hGbp5mYRQgUmz9")

puts(beta_user_profile_enrollment_url)
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

- `class BetaUserProfile`

  - `id: String`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Hash[Symbol, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: :active | :pending | :rejected`

      Status of the trust grant.

      - `:active`

      - `:pending`

      - `:rejected`

  - `type: :user_profile`

    Object type. Always `user_profile`.

    - `:user_profile`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `access_type: :application | :passthrough`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `:application`

    - `:passthrough`

  - `external_id: String`

    Platform's own identifier for this user. Not enforced unique.

  - `name: String`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: :external | :resold | :internal`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `:external`

    - `:resold`

    - `:internal`

### Beta User Profile Enrollment URL

- `class BetaUserProfileEnrollmentURL`

  - `expires_at: Time`

    A timestamp in RFC 3339 format

  - `type: :enrollment_url`

    Object type. Always `enrollment_url`.

    - `:enrollment_url`

  - `url: String`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Beta User Profile Trust Grant

- `class BetaUserProfileTrustGrant`

  - `status: :active | :pending | :rejected`

    Status of the trust grant.

    - `:active`

    - `:pending`

    - `:rejected`

# Dreams

## Create a Dream

`beta.dreams.create(**kwargs) -> BetaDream`

**post** `/v1/dreams`

Create a Dream

### Parameters

- `inputs: Array[BetaDreamInput]`

  - `class BetaDreamMemoryStoreInput`

    An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

    - `memory_store_id: String`

    - `type: :memory_store`

      - `:memory_store`

  - `class BetaDreamSessionsInput`

    Input session transcripts the dream reads.

    - `session_ids: Array[String]`

    - `type: :sessions`

      - `:sessions`

- `model: String | BetaDreamModelConfigParam`

  Model identifier and configuration applied to every pipeline stage.

  - `String = String`

  - `class BetaDreamModelConfigParam`

    Model identifier and configuration applied to every pipeline stage.

    - `id: String`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

- `instructions: String`

- `output_behavior: BetaOutputBehavior`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `class BetaOutputBehaviorCreateNew`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `type: :create_new`

      - `:create_new`

  - `class BetaOutputBehaviorUpdateExisting`

    The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

    - `memory_store_id: String`

    - `type: :update_existing`

      - `:update_existing`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaDream`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `ended_at: Time`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: String`

    - `type: String`

  - `inputs: Array[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: String`

      - `type: :memory_store`

        - `:memory_store`

    - `class BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array[String]`

      - `type: :sessions`

        - `:sessions`

  - `instructions: String`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: String`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: :create_new`

        - `:create_new`

    - `class BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: String`

      - `type: :update_existing`

        - `:update_existing`

  - `outputs: Array[BetaDreamOutput]`

    - `memory_store_id: String`

    - `type: :memory_store`

      - `:memory_store`

  - `session_id: String`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `:pending`

    - `:running`

    - `:completed`

    - `:failed`

    - `:canceled`

  - `type: :dream`

    - `:dream`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: Integer`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

    - `input_tokens: Integer`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: Integer`

      Total output tokens generated across every pipeline stage.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_dream = anthropic.beta.dreams.create(inputs: [{memory_store_id: "x", type: :memory_store}], model: "string")

puts(beta_dream)
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

`beta.dreams.list(**kwargs) -> PageCursor<BetaDream>`

**get** `/v1/dreams`

List Dreams

### Parameters

- `created_at_gt: Time`

  Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

- `created_at_lt: Time`

  Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

- `include_archived: bool`

  Query parameter for include_archived

- `limit: Integer`

  Query parameter for limit

- `page: String`

  Query parameter for page

- `statuses: Array[BetaDreamStatus]`

  Filter by lifecycle status. Repeat the parameter to match any of multiple statuses. Empty applies no status filter.

  - `:pending`

  - `:running`

  - `:completed`

  - `:failed`

  - `:canceled`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaDream`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `ended_at: Time`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: String`

    - `type: String`

  - `inputs: Array[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: String`

      - `type: :memory_store`

        - `:memory_store`

    - `class BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array[String]`

      - `type: :sessions`

        - `:sessions`

  - `instructions: String`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: String`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: :create_new`

        - `:create_new`

    - `class BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: String`

      - `type: :update_existing`

        - `:update_existing`

  - `outputs: Array[BetaDreamOutput]`

    - `memory_store_id: String`

    - `type: :memory_store`

      - `:memory_store`

  - `session_id: String`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `:pending`

    - `:running`

    - `:completed`

    - `:failed`

    - `:canceled`

  - `type: :dream`

    - `:dream`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: Integer`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

    - `input_tokens: Integer`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: Integer`

      Total output tokens generated across every pipeline stage.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.dreams.list

puts(page)
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

`beta.dreams.retrieve(dream_id, **kwargs) -> BetaDream`

**get** `/v1/dreams/{dream_id}`

Get a Dream

### Parameters

- `dream_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaDream`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `ended_at: Time`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: String`

    - `type: String`

  - `inputs: Array[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: String`

      - `type: :memory_store`

        - `:memory_store`

    - `class BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array[String]`

      - `type: :sessions`

        - `:sessions`

  - `instructions: String`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: String`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: :create_new`

        - `:create_new`

    - `class BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: String`

      - `type: :update_existing`

        - `:update_existing`

  - `outputs: Array[BetaDreamOutput]`

    - `memory_store_id: String`

    - `type: :memory_store`

      - `:memory_store`

  - `session_id: String`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `:pending`

    - `:running`

    - `:completed`

    - `:failed`

    - `:canceled`

  - `type: :dream`

    - `:dream`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: Integer`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

    - `input_tokens: Integer`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: Integer`

      Total output tokens generated across every pipeline stage.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_dream = anthropic.beta.dreams.retrieve("dream_id")

puts(beta_dream)
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

`beta.dreams.cancel(dream_id, **kwargs) -> BetaDream`

**post** `/v1/dreams/{dream_id}/cancel`

Cancel a Dream

### Parameters

- `dream_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaDream`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `ended_at: Time`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: String`

    - `type: String`

  - `inputs: Array[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: String`

      - `type: :memory_store`

        - `:memory_store`

    - `class BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array[String]`

      - `type: :sessions`

        - `:sessions`

  - `instructions: String`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: String`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: :create_new`

        - `:create_new`

    - `class BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: String`

      - `type: :update_existing`

        - `:update_existing`

  - `outputs: Array[BetaDreamOutput]`

    - `memory_store_id: String`

    - `type: :memory_store`

      - `:memory_store`

  - `session_id: String`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `:pending`

    - `:running`

    - `:completed`

    - `:failed`

    - `:canceled`

  - `type: :dream`

    - `:dream`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: Integer`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

    - `input_tokens: Integer`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: Integer`

      Total output tokens generated across every pipeline stage.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_dream = anthropic.beta.dreams.cancel("dream_id")

puts(beta_dream)
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

`beta.dreams.archive(dream_id, **kwargs) -> BetaDream`

**post** `/v1/dreams/{dream_id}/archive`

Archive a Dream

### Parameters

- `dream_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaDream`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `ended_at: Time`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: String`

    - `type: String`

  - `inputs: Array[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: String`

      - `type: :memory_store`

        - `:memory_store`

    - `class BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array[String]`

      - `type: :sessions`

        - `:sessions`

  - `instructions: String`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: String`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: :create_new`

        - `:create_new`

    - `class BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: String`

      - `type: :update_existing`

        - `:update_existing`

  - `outputs: Array[BetaDreamOutput]`

    - `memory_store_id: String`

    - `type: :memory_store`

      - `:memory_store`

  - `session_id: String`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `:pending`

    - `:running`

    - `:completed`

    - `:failed`

    - `:canceled`

  - `type: :dream`

    - `:dream`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: Integer`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

    - `input_tokens: Integer`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: Integer`

      Total output tokens generated across every pipeline stage.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_dream = anthropic.beta.dreams.archive("dream_id")

puts(beta_dream)
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

- `class BetaDream`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `ended_at: Time`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: String`

    - `type: String`

  - `inputs: Array[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: String`

      - `type: :memory_store`

        - `:memory_store`

    - `class BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array[String]`

      - `type: :sessions`

        - `:sessions`

  - `instructions: String`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: String`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: :create_new`

        - `:create_new`

    - `class BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: String`

      - `type: :update_existing`

        - `:update_existing`

  - `outputs: Array[BetaDreamOutput]`

    - `memory_store_id: String`

    - `type: :memory_store`

      - `:memory_store`

  - `session_id: String`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `:pending`

    - `:running`

    - `:completed`

    - `:failed`

    - `:canceled`

  - `type: :dream`

    - `:dream`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: Integer`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

    - `input_tokens: Integer`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: Integer`

      Total output tokens generated across every pipeline stage.

### Beta Dream Error

- `class BetaDreamError`

  Failure detail for a Dream whose `status` is `failed`.

  - `message: String`

  - `type: String`

### Beta Dream Input

- `BetaDreamInput = BetaDreamMemoryStoreInput | BetaDreamSessionsInput`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `class BetaDreamMemoryStoreInput`

    An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

    - `memory_store_id: String`

    - `type: :memory_store`

      - `:memory_store`

  - `class BetaDreamSessionsInput`

    Input session transcripts the dream reads.

    - `session_ids: Array[String]`

    - `type: :sessions`

      - `:sessions`

### Beta Dream Memory Store Input

- `class BetaDreamMemoryStoreInput`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `memory_store_id: String`

  - `type: :memory_store`

    - `:memory_store`

### Beta Dream Memory Store Output

- `class BetaDreamMemoryStoreOutput`

  An output memory store the dream writes consolidated memories into.

  - `memory_store_id: String`

  - `type: :memory_store`

    - `:memory_store`

### Beta Dream Model Config

- `class BetaDreamModelConfig`

  Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

  - `id: String`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

  - `speed: :standard | :fast`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `:standard`

    - `:fast`

### Beta Dream Model Config Param

- `class BetaDreamModelConfigParam`

  Model identifier and configuration applied to every pipeline stage.

  - `id: String`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

  - `speed: :standard | :fast`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `:standard`

    - `:fast`

### Beta Dream Output

- `class BetaDreamOutput`

  An output memory store the dream writes consolidated memories into.

  - `memory_store_id: String`

  - `type: :memory_store`

    - `:memory_store`

### Beta Dream Sessions Input

- `class BetaDreamSessionsInput`

  Input session transcripts the dream reads.

  - `session_ids: Array[String]`

  - `type: :sessions`

    - `:sessions`

### Beta Dream Status

- `BetaDreamStatus = :pending | :running | :completed | 2 more`

  Lifecycle status of a Dream.

  - `:pending`

  - `:running`

  - `:completed`

  - `:failed`

  - `:canceled`

### Beta Dream Usage

- `class BetaDreamUsage`

  Cumulative token usage for the dream across every pipeline stage.

  - `cache_creation_input_tokens: Integer`

    Total tokens used to create prompt-cache entries (sum of all TTL tiers).

  - `cache_read_input_tokens: Integer`

    Total tokens read from prompt cache.

  - `input_tokens: Integer`

    Total uncached input tokens consumed across every pipeline stage.

  - `output_tokens: Integer`

    Total output tokens generated across every pipeline stage.

### Beta Output Behavior

- `BetaOutputBehavior = BetaOutputBehaviorCreateNew | BetaOutputBehaviorUpdateExisting`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `class BetaOutputBehaviorCreateNew`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `type: :create_new`

      - `:create_new`

  - `class BetaOutputBehaviorUpdateExisting`

    The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

    - `memory_store_id: String`

    - `type: :update_existing`

      - `:update_existing`

### Beta Output Behavior Create New

- `class BetaOutputBehaviorCreateNew`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `type: :create_new`

    - `:create_new`

### Beta Output Behavior Update Existing

- `class BetaOutputBehaviorUpdateExisting`

  The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

  - `memory_store_id: String`

  - `type: :update_existing`

    - `:update_existing`

# Tunnels

## Create Tunnel

`beta.tunnels.create(**kwargs) -> BetaTunnel`

**post** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

### Parameters

- `display_name: String`

  Optional human-readable name for the tunnel (1-255 characters).

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaTunnel`

  An MCP tunnel.

  - `id: String`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `display_name: String`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: String`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: :tunnel`

    - `:tunnel`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel = anthropic.beta.tunnels.create

puts(beta_tunnel)
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

`beta.tunnels.retrieve(tunnel_id, **kwargs) -> BetaTunnel`

**get** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

### Parameters

- `tunnel_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaTunnel`

  An MCP tunnel.

  - `id: String`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `display_name: String`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: String`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: :tunnel`

    - `:tunnel`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel = anthropic.beta.tunnels.retrieve("tunnel_id")

puts(beta_tunnel)
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

`beta.tunnels.list(**kwargs) -> PageCursor<BetaTunnel>`

**get** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

### Parameters

- `include_archived: bool`

  Whether to include archived tunnels in the results. Defaults to false.

- `limit: Integer`

  Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

- `page: String`

  Opaque pagination cursor from a previous `list_tunnels` response.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaTunnel`

  An MCP tunnel.

  - `id: String`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `display_name: String`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: String`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: :tunnel`

    - `:tunnel`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.tunnels.list

puts(page)
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

`beta.tunnels.archive(tunnel_id, **kwargs) -> BetaTunnel`

**post** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

### Parameters

- `tunnel_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaTunnel`

  An MCP tunnel.

  - `id: String`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `display_name: String`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: String`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: :tunnel`

    - `:tunnel`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel = anthropic.beta.tunnels.archive("tunnel_id")

puts(beta_tunnel)
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

`beta.tunnels.reveal_token(tunnel_id, **kwargs) -> BetaTunnelToken`

**post** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

### Parameters

- `tunnel_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaTunnelToken`

  A tunnel's connector token.

  - `id: String`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: String`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: :tunnel_token`

    - `:tunnel_token`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel_token = anthropic.beta.tunnels.reveal_token("tunnel_id")

puts(beta_tunnel_token)
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

`beta.tunnels.rotate_token(tunnel_id, **kwargs) -> BetaTunnelToken`

**post** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

### Parameters

- `tunnel_id: String`

- `reason: String`

  Optional free-text reason for the rotation, recorded for audit.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaTunnelToken`

  A tunnel's connector token.

  - `id: String`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: String`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: :tunnel_token`

    - `:tunnel_token`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel_token = anthropic.beta.tunnels.rotate_token("tunnel_id")

puts(beta_tunnel_token)
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

- `class BetaTunnel`

  An MCP tunnel.

  - `id: String`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `display_name: String`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: String`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: :tunnel`

    - `:tunnel`

### Beta Tunnel Token

- `class BetaTunnelToken`

  A tunnel's connector token.

  - `id: String`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: String`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: :tunnel_token`

    - `:tunnel_token`

# Certificates

## Create Tunnel Certificate

`beta.tunnels.certificates.create(tunnel_id, **kwargs) -> BetaTunnelCertificate`

**post** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

### Parameters

- `tunnel_id: String`

- `ca_certificate_pem: String`

  PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: String`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `expires_at: Time`

    A timestamp in RFC 3339 format

  - `fingerprint: String`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: String`

    ID of the tunnel the certificate is registered against.

  - `type: :tunnel_certificate`

    - `:tunnel_certificate`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel_certificate = anthropic.beta.tunnels.certificates.create("tunnel_id", ca_certificate_pem: "ca_certificate_pem")

puts(beta_tunnel_certificate)
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

`beta.tunnels.certificates.retrieve(certificate_id, **kwargs) -> BetaTunnelCertificate`

**get** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

### Parameters

- `tunnel_id: String`

- `certificate_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: String`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `expires_at: Time`

    A timestamp in RFC 3339 format

  - `fingerprint: String`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: String`

    ID of the tunnel the certificate is registered against.

  - `type: :tunnel_certificate`

    - `:tunnel_certificate`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel_certificate = anthropic.beta.tunnels.certificates.retrieve("certificate_id", tunnel_id: "tunnel_id")

puts(beta_tunnel_certificate)
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

`beta.tunnels.certificates.list(tunnel_id, **kwargs) -> PageCursor<BetaTunnelCertificate>`

**get** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

### Parameters

- `tunnel_id: String`

- `include_archived: bool`

  Whether to include archived certificates in the results. Defaults to false.

- `limit: Integer`

  Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

- `page: String`

  Opaque pagination cursor from a previous `list_tunnel_certificates` response.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: String`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `expires_at: Time`

    A timestamp in RFC 3339 format

  - `fingerprint: String`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: String`

    ID of the tunnel the certificate is registered against.

  - `type: :tunnel_certificate`

    - `:tunnel_certificate`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.tunnels.certificates.list("tunnel_id")

puts(page)
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

`beta.tunnels.certificates.archive(certificate_id, **kwargs) -> BetaTunnelCertificate`

**post** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

### Parameters

- `tunnel_id: String`

- `certificate_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

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

### Returns

- `class BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: String`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `expires_at: Time`

    A timestamp in RFC 3339 format

  - `fingerprint: String`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: String`

    ID of the tunnel the certificate is registered against.

  - `type: :tunnel_certificate`

    - `:tunnel_certificate`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel_certificate = anthropic.beta.tunnels.certificates.archive("certificate_id", tunnel_id: "tunnel_id")

puts(beta_tunnel_certificate)
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

- `class BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: String`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `expires_at: Time`

    A timestamp in RFC 3339 format

  - `fingerprint: String`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: String`

    ID of the tunnel the certificate is registered against.

  - `type: :tunnel_certificate`

    - `:tunnel_certificate`

# Webhooks

## Domain Types

### Beta Webhook Agent Archived Event Data

- `class BetaWebhookAgentArchivedEventData`

  - `id: String`

    ID of the agent that triggered the event.

  - `organization_id: String`

  - `type: :"agent.archived"`

    - `:"agent.archived"`

  - `workspace_id: String`

### Beta Webhook Agent Created Event Data

- `class BetaWebhookAgentCreatedEventData`

  - `id: String`

    ID of the agent that triggered the event.

  - `organization_id: String`

  - `type: :"agent.created"`

    - `:"agent.created"`

  - `workspace_id: String`

### Beta Webhook Agent Deleted Event Data

- `class BetaWebhookAgentDeletedEventData`

  - `id: String`

    ID of the agent that triggered the event.

  - `organization_id: String`

  - `type: :"agent.deleted"`

    - `:"agent.deleted"`

  - `workspace_id: String`

### Beta Webhook Agent Updated Event Data

- `class BetaWebhookAgentUpdatedEventData`

  - `id: String`

    ID of the agent that triggered the event.

  - `organization_id: String`

  - `type: :"agent.updated"`

    - `:"agent.updated"`

  - `workspace_id: String`

### Beta Webhook Deployment Archived Event Data

- `class BetaWebhookDeploymentArchivedEventData`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `type: :"deployment.archived"`

    - `:"deployment.archived"`

  - `workspace_id: String`

### Beta Webhook Deployment Created Event Data

- `class BetaWebhookDeploymentCreatedEventData`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `type: :"deployment.created"`

    - `:"deployment.created"`

  - `workspace_id: String`

### Beta Webhook Deployment Deleted Event Data

- `class BetaWebhookDeploymentDeletedEventData`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `type: :"deployment.deleted"`

    - `:"deployment.deleted"`

  - `workspace_id: String`

### Beta Webhook Deployment Paused Event Data

- `class BetaWebhookDeploymentPausedEventData`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `type: :"deployment.paused"`

    - `:"deployment.paused"`

  - `workspace_id: String`

### Beta Webhook Deployment Run Failed Event Data

- `class BetaWebhookDeploymentRunFailedEventData`

  - `id: String`

    ID of the deployment run that triggered the event.

  - `organization_id: String`

  - `type: :"deployment_run.failed"`

    - `:"deployment_run.failed"`

  - `workspace_id: String`

### Beta Webhook Deployment Run Started Event Data

- `class BetaWebhookDeploymentRunStartedEventData`

  - `id: String`

    ID of the deployment run that triggered the event.

  - `organization_id: String`

  - `type: :"deployment_run.started"`

    - `:"deployment_run.started"`

  - `workspace_id: String`

### Beta Webhook Deployment Run Succeeded Event Data

- `class BetaWebhookDeploymentRunSucceededEventData`

  - `id: String`

    ID of the deployment run that triggered the event.

  - `organization_id: String`

  - `type: :"deployment_run.succeeded"`

    - `:"deployment_run.succeeded"`

  - `workspace_id: String`

### Beta Webhook Deployment Unpaused Event Data

- `class BetaWebhookDeploymentUnpausedEventData`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `type: :"deployment.unpaused"`

    - `:"deployment.unpaused"`

  - `workspace_id: String`

### Beta Webhook Deployment Updated Event Data

- `class BetaWebhookDeploymentUpdatedEventData`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `type: :"deployment.updated"`

    - `:"deployment.updated"`

  - `workspace_id: String`

### Beta Webhook Environment Archived Event Data

- `class BetaWebhookEnvironmentArchivedEventData`

  - `id: String`

    ID of the environment that triggered the event.

  - `organization_id: String`

  - `type: :"environment.archived"`

    - `:"environment.archived"`

  - `workspace_id: String`

### Beta Webhook Environment Created Event Data

- `class BetaWebhookEnvironmentCreatedEventData`

  - `id: String`

    ID of the environment that triggered the event.

  - `organization_id: String`

  - `type: :"environment.created"`

    - `:"environment.created"`

  - `workspace_id: String`

### Beta Webhook Environment Deleted Event Data

- `class BetaWebhookEnvironmentDeletedEventData`

  - `id: String`

    ID of the environment that triggered the event.

  - `organization_id: String`

  - `type: :"environment.deleted"`

    - `:"environment.deleted"`

  - `workspace_id: String`

### Beta Webhook Environment Updated Event Data

- `class BetaWebhookEnvironmentUpdatedEventData`

  - `id: String`

    ID of the environment that triggered the event.

  - `organization_id: String`

  - `type: :"environment.updated"`

    - `:"environment.updated"`

  - `workspace_id: String`

### Beta Webhook Event

- `class BetaWebhookEvent`

  - `id: String`

    Unique event identifier for idempotency.

  - `created_at: Time`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `class BetaWebhookSessionCreatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.created"`

        - `:"session.created"`

      - `workspace_id: String`

    - `class BetaWebhookSessionPendingEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.pending"`

        - `:"session.pending"`

      - `workspace_id: String`

    - `class BetaWebhookSessionRunningEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.running"`

        - `:"session.running"`

      - `workspace_id: String`

    - `class BetaWebhookSessionIdledEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.idled"`

        - `:"session.idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionRequiresActionEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.requires_action"`

        - `:"session.requires_action"`

      - `workspace_id: String`

    - `class BetaWebhookSessionArchivedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.archived"`

        - `:"session.archived"`

      - `workspace_id: String`

    - `class BetaWebhookSessionDeletedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.deleted"`

        - `:"session.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusRescheduledEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_rescheduled"`

        - `:"session.status_rescheduled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusRunStartedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_run_started"`

        - `:"session.status_run_started"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusIdledEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_idled"`

        - `:"session.status_idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusTerminatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_terminated"`

        - `:"session.status_terminated"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadCreatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `type: :"session.thread_created"`

        - `:"session.thread_created"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadIdledEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `type: :"session.thread_idled"`

        - `:"session.thread_idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadTerminatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `type: :"session.thread_terminated"`

        - `:"session.thread_terminated"`

      - `workspace_id: String`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.outcome_evaluation_ended"`

        - `:"session.outcome_evaluation_ended"`

      - `workspace_id: String`

    - `class BetaWebhookVaultCreatedEventData`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `type: :"vault.created"`

        - `:"vault.created"`

      - `workspace_id: String`

    - `class BetaWebhookVaultArchivedEventData`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `type: :"vault.archived"`

        - `:"vault.archived"`

      - `workspace_id: String`

    - `class BetaWebhookVaultDeletedEventData`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `type: :"vault.deleted"`

        - `:"vault.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialCreatedEventData`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.created"`

        - `:"vault_credential.created"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialArchivedEventData`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.archived"`

        - `:"vault_credential.archived"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialDeletedEventData`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.deleted"`

        - `:"vault_credential.deleted"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.refresh_failed"`

        - `:"vault_credential.refresh_failed"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookSessionUpdatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.updated"`

        - `:"session.updated"`

      - `workspace_id: String`

    - `class BetaWebhookAgentCreatedEventData`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `type: :"agent.created"`

        - `:"agent.created"`

      - `workspace_id: String`

    - `class BetaWebhookAgentArchivedEventData`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `type: :"agent.archived"`

        - `:"agent.archived"`

      - `workspace_id: String`

    - `class BetaWebhookAgentDeletedEventData`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `type: :"agent.deleted"`

        - `:"agent.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentPausedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.paused"`

        - `:"deployment.paused"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunFailedEventData`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `type: :"deployment_run.failed"`

        - `:"deployment_run.failed"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentCreatedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.created"`

        - `:"deployment.created"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentUpdatedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.updated"`

        - `:"deployment.updated"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentUnpausedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.unpaused"`

        - `:"deployment.unpaused"`

      - `workspace_id: String`

    - `class BetaWebhookAgentUpdatedEventData`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `type: :"agent.updated"`

        - `:"agent.updated"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentArchivedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.archived"`

        - `:"deployment.archived"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunStartedEventData`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `type: :"deployment_run.started"`

        - `:"deployment_run.started"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentDeletedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.deleted"`

        - `:"deployment.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunSucceededEventData`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `type: :"deployment_run.succeeded"`

        - `:"deployment_run.succeeded"`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentCreatedEventData`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `type: :"environment.created"`

        - `:"environment.created"`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentUpdatedEventData`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `type: :"environment.updated"`

        - `:"environment.updated"`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentArchivedEventData`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `type: :"environment.archived"`

        - `:"environment.archived"`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentDeletedEventData`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `type: :"environment.deleted"`

        - `:"environment.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreCreatedEventData`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `type: :"memory_store.created"`

        - `:"memory_store.created"`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreArchivedEventData`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `type: :"memory_store.archived"`

        - `:"memory_store.archived"`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreDeletedEventData`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `type: :"memory_store.deleted"`

        - `:"memory_store.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookSessionBudgetReachedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.budget_reached"`

        - `:"session.budget_reached"`

      - `workspace_id: String`

  - `type: :event`

    Object type. Always `event` for webhook payloads.

    - `:event`

### Beta Webhook Event Data

- `BetaWebhookEventData = BetaWebhookSessionCreatedEventData | BetaWebhookSessionPendingEventData | BetaWebhookSessionRunningEventData | 41 more`

  - `class BetaWebhookSessionCreatedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.created"`

      - `:"session.created"`

    - `workspace_id: String`

  - `class BetaWebhookSessionPendingEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.pending"`

      - `:"session.pending"`

    - `workspace_id: String`

  - `class BetaWebhookSessionRunningEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.running"`

      - `:"session.running"`

    - `workspace_id: String`

  - `class BetaWebhookSessionIdledEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.idled"`

      - `:"session.idled"`

    - `workspace_id: String`

  - `class BetaWebhookSessionRequiresActionEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.requires_action"`

      - `:"session.requires_action"`

    - `workspace_id: String`

  - `class BetaWebhookSessionArchivedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.archived"`

      - `:"session.archived"`

    - `workspace_id: String`

  - `class BetaWebhookSessionDeletedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.deleted"`

      - `:"session.deleted"`

    - `workspace_id: String`

  - `class BetaWebhookSessionStatusRescheduledEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.status_rescheduled"`

      - `:"session.status_rescheduled"`

    - `workspace_id: String`

  - `class BetaWebhookSessionStatusRunStartedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.status_run_started"`

      - `:"session.status_run_started"`

    - `workspace_id: String`

  - `class BetaWebhookSessionStatusIdledEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.status_idled"`

      - `:"session.status_idled"`

    - `workspace_id: String`

  - `class BetaWebhookSessionStatusTerminatedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.status_terminated"`

      - `:"session.status_terminated"`

    - `workspace_id: String`

  - `class BetaWebhookSessionThreadCreatedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `session_thread_id: String`

      ID of the session thread this event refers to.

    - `type: :"session.thread_created"`

      - `:"session.thread_created"`

    - `workspace_id: String`

  - `class BetaWebhookSessionThreadIdledEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `session_thread_id: String`

      ID of the session thread this event refers to.

    - `type: :"session.thread_idled"`

      - `:"session.thread_idled"`

    - `workspace_id: String`

  - `class BetaWebhookSessionThreadTerminatedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `session_thread_id: String`

      ID of the session thread this event refers to.

    - `type: :"session.thread_terminated"`

      - `:"session.thread_terminated"`

    - `workspace_id: String`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.outcome_evaluation_ended"`

      - `:"session.outcome_evaluation_ended"`

    - `workspace_id: String`

  - `class BetaWebhookVaultCreatedEventData`

    - `id: String`

      ID of the vault that triggered the event.

    - `organization_id: String`

    - `type: :"vault.created"`

      - `:"vault.created"`

    - `workspace_id: String`

  - `class BetaWebhookVaultArchivedEventData`

    - `id: String`

      ID of the vault that triggered the event.

    - `organization_id: String`

    - `type: :"vault.archived"`

      - `:"vault.archived"`

    - `workspace_id: String`

  - `class BetaWebhookVaultDeletedEventData`

    - `id: String`

      ID of the vault that triggered the event.

    - `organization_id: String`

    - `type: :"vault.deleted"`

      - `:"vault.deleted"`

    - `workspace_id: String`

  - `class BetaWebhookVaultCredentialCreatedEventData`

    - `id: String`

      ID of the vault credential that triggered the event.

    - `organization_id: String`

    - `type: :"vault_credential.created"`

      - `:"vault_credential.created"`

    - `vault_id: String`

      ID of the vault that owns this credential.

    - `workspace_id: String`

  - `class BetaWebhookVaultCredentialArchivedEventData`

    - `id: String`

      ID of the vault credential that triggered the event.

    - `organization_id: String`

    - `type: :"vault_credential.archived"`

      - `:"vault_credential.archived"`

    - `vault_id: String`

      ID of the vault that owns this credential.

    - `workspace_id: String`

  - `class BetaWebhookVaultCredentialDeletedEventData`

    - `id: String`

      ID of the vault credential that triggered the event.

    - `organization_id: String`

    - `type: :"vault_credential.deleted"`

      - `:"vault_credential.deleted"`

    - `vault_id: String`

      ID of the vault that owns this credential.

    - `workspace_id: String`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData`

    - `id: String`

      ID of the vault credential that triggered the event.

    - `organization_id: String`

    - `type: :"vault_credential.refresh_failed"`

      - `:"vault_credential.refresh_failed"`

    - `vault_id: String`

      ID of the vault that owns this credential.

    - `workspace_id: String`

  - `class BetaWebhookSessionUpdatedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.updated"`

      - `:"session.updated"`

    - `workspace_id: String`

  - `class BetaWebhookAgentCreatedEventData`

    - `id: String`

      ID of the agent that triggered the event.

    - `organization_id: String`

    - `type: :"agent.created"`

      - `:"agent.created"`

    - `workspace_id: String`

  - `class BetaWebhookAgentArchivedEventData`

    - `id: String`

      ID of the agent that triggered the event.

    - `organization_id: String`

    - `type: :"agent.archived"`

      - `:"agent.archived"`

    - `workspace_id: String`

  - `class BetaWebhookAgentDeletedEventData`

    - `id: String`

      ID of the agent that triggered the event.

    - `organization_id: String`

    - `type: :"agent.deleted"`

      - `:"agent.deleted"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentPausedEventData`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `type: :"deployment.paused"`

      - `:"deployment.paused"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentRunFailedEventData`

    - `id: String`

      ID of the deployment run that triggered the event.

    - `organization_id: String`

    - `type: :"deployment_run.failed"`

      - `:"deployment_run.failed"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentCreatedEventData`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `type: :"deployment.created"`

      - `:"deployment.created"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentUpdatedEventData`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `type: :"deployment.updated"`

      - `:"deployment.updated"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentUnpausedEventData`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `type: :"deployment.unpaused"`

      - `:"deployment.unpaused"`

    - `workspace_id: String`

  - `class BetaWebhookAgentUpdatedEventData`

    - `id: String`

      ID of the agent that triggered the event.

    - `organization_id: String`

    - `type: :"agent.updated"`

      - `:"agent.updated"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentArchivedEventData`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `type: :"deployment.archived"`

      - `:"deployment.archived"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentRunStartedEventData`

    - `id: String`

      ID of the deployment run that triggered the event.

    - `organization_id: String`

    - `type: :"deployment_run.started"`

      - `:"deployment_run.started"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentDeletedEventData`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `type: :"deployment.deleted"`

      - `:"deployment.deleted"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentRunSucceededEventData`

    - `id: String`

      ID of the deployment run that triggered the event.

    - `organization_id: String`

    - `type: :"deployment_run.succeeded"`

      - `:"deployment_run.succeeded"`

    - `workspace_id: String`

  - `class BetaWebhookEnvironmentCreatedEventData`

    - `id: String`

      ID of the environment that triggered the event.

    - `organization_id: String`

    - `type: :"environment.created"`

      - `:"environment.created"`

    - `workspace_id: String`

  - `class BetaWebhookEnvironmentUpdatedEventData`

    - `id: String`

      ID of the environment that triggered the event.

    - `organization_id: String`

    - `type: :"environment.updated"`

      - `:"environment.updated"`

    - `workspace_id: String`

  - `class BetaWebhookEnvironmentArchivedEventData`

    - `id: String`

      ID of the environment that triggered the event.

    - `organization_id: String`

    - `type: :"environment.archived"`

      - `:"environment.archived"`

    - `workspace_id: String`

  - `class BetaWebhookEnvironmentDeletedEventData`

    - `id: String`

      ID of the environment that triggered the event.

    - `organization_id: String`

    - `type: :"environment.deleted"`

      - `:"environment.deleted"`

    - `workspace_id: String`

  - `class BetaWebhookMemoryStoreCreatedEventData`

    - `id: String`

      ID of the memory store that triggered the event.

    - `organization_id: String`

    - `type: :"memory_store.created"`

      - `:"memory_store.created"`

    - `workspace_id: String`

  - `class BetaWebhookMemoryStoreArchivedEventData`

    - `id: String`

      ID of the memory store that triggered the event.

    - `organization_id: String`

    - `type: :"memory_store.archived"`

      - `:"memory_store.archived"`

    - `workspace_id: String`

  - `class BetaWebhookMemoryStoreDeletedEventData`

    - `id: String`

      ID of the memory store that triggered the event.

    - `organization_id: String`

    - `type: :"memory_store.deleted"`

      - `:"memory_store.deleted"`

    - `workspace_id: String`

  - `class BetaWebhookSessionBudgetReachedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.budget_reached"`

      - `:"session.budget_reached"`

    - `workspace_id: String`

### Beta Webhook Memory Store Archived Event Data

- `class BetaWebhookMemoryStoreArchivedEventData`

  - `id: String`

    ID of the memory store that triggered the event.

  - `organization_id: String`

  - `type: :"memory_store.archived"`

    - `:"memory_store.archived"`

  - `workspace_id: String`

### Beta Webhook Memory Store Created Event Data

- `class BetaWebhookMemoryStoreCreatedEventData`

  - `id: String`

    ID of the memory store that triggered the event.

  - `organization_id: String`

  - `type: :"memory_store.created"`

    - `:"memory_store.created"`

  - `workspace_id: String`

### Beta Webhook Memory Store Deleted Event Data

- `class BetaWebhookMemoryStoreDeletedEventData`

  - `id: String`

    ID of the memory store that triggered the event.

  - `organization_id: String`

  - `type: :"memory_store.deleted"`

    - `:"memory_store.deleted"`

  - `workspace_id: String`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.archived"`

    - `:"session.archived"`

  - `workspace_id: String`

### Beta Webhook Session Budget Reached Event Data

- `class BetaWebhookSessionBudgetReachedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.budget_reached"`

    - `:"session.budget_reached"`

  - `workspace_id: String`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.created"`

    - `:"session.created"`

  - `workspace_id: String`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.deleted"`

    - `:"session.deleted"`

  - `workspace_id: String`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.idled"`

    - `:"session.idled"`

  - `workspace_id: String`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.outcome_evaluation_ended"`

    - `:"session.outcome_evaluation_ended"`

  - `workspace_id: String`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.pending"`

    - `:"session.pending"`

  - `workspace_id: String`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.requires_action"`

    - `:"session.requires_action"`

  - `workspace_id: String`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.running"`

    - `:"session.running"`

  - `workspace_id: String`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.status_idled"`

    - `:"session.status_idled"`

  - `workspace_id: String`

### Beta Webhook Session Status Rescheduled Event Data

- `class BetaWebhookSessionStatusRescheduledEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.status_rescheduled"`

    - `:"session.status_rescheduled"`

  - `workspace_id: String`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.status_run_started"`

    - `:"session.status_run_started"`

  - `workspace_id: String`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.status_terminated"`

    - `:"session.status_terminated"`

  - `workspace_id: String`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `session_thread_id: String`

    ID of the session thread this event refers to.

  - `type: :"session.thread_created"`

    - `:"session.thread_created"`

  - `workspace_id: String`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `session_thread_id: String`

    ID of the session thread this event refers to.

  - `type: :"session.thread_idled"`

    - `:"session.thread_idled"`

  - `workspace_id: String`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `session_thread_id: String`

    ID of the session thread this event refers to.

  - `type: :"session.thread_terminated"`

    - `:"session.thread_terminated"`

  - `workspace_id: String`

### Beta Webhook Session Updated Event Data

- `class BetaWebhookSessionUpdatedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.updated"`

    - `:"session.updated"`

  - `workspace_id: String`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData`

  - `id: String`

    ID of the vault that triggered the event.

  - `organization_id: String`

  - `type: :"vault.archived"`

    - `:"vault.archived"`

  - `workspace_id: String`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData`

  - `id: String`

    ID of the vault that triggered the event.

  - `organization_id: String`

  - `type: :"vault.created"`

    - `:"vault.created"`

  - `workspace_id: String`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData`

  - `id: String`

    ID of the vault credential that triggered the event.

  - `organization_id: String`

  - `type: :"vault_credential.archived"`

    - `:"vault_credential.archived"`

  - `vault_id: String`

    ID of the vault that owns this credential.

  - `workspace_id: String`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData`

  - `id: String`

    ID of the vault credential that triggered the event.

  - `organization_id: String`

  - `type: :"vault_credential.created"`

    - `:"vault_credential.created"`

  - `vault_id: String`

    ID of the vault that owns this credential.

  - `workspace_id: String`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData`

  - `id: String`

    ID of the vault credential that triggered the event.

  - `organization_id: String`

  - `type: :"vault_credential.deleted"`

    - `:"vault_credential.deleted"`

  - `vault_id: String`

    ID of the vault that owns this credential.

  - `workspace_id: String`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData`

  - `id: String`

    ID of the vault credential that triggered the event.

  - `organization_id: String`

  - `type: :"vault_credential.refresh_failed"`

    - `:"vault_credential.refresh_failed"`

  - `vault_id: String`

    ID of the vault that owns this credential.

  - `workspace_id: String`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData`

  - `id: String`

    ID of the vault that triggered the event.

  - `organization_id: String`

  - `type: :"vault.deleted"`

    - `:"vault.deleted"`

  - `workspace_id: String`

### Unwrap Webhook Event

- `class UnwrapWebhookEvent`

  - `id: String`

    Unique event identifier for idempotency.

  - `created_at: Time`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `class BetaWebhookSessionCreatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.created"`

        - `:"session.created"`

      - `workspace_id: String`

    - `class BetaWebhookSessionPendingEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.pending"`

        - `:"session.pending"`

      - `workspace_id: String`

    - `class BetaWebhookSessionRunningEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.running"`

        - `:"session.running"`

      - `workspace_id: String`

    - `class BetaWebhookSessionIdledEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.idled"`

        - `:"session.idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionRequiresActionEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.requires_action"`

        - `:"session.requires_action"`

      - `workspace_id: String`

    - `class BetaWebhookSessionArchivedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.archived"`

        - `:"session.archived"`

      - `workspace_id: String`

    - `class BetaWebhookSessionDeletedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.deleted"`

        - `:"session.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusRescheduledEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_rescheduled"`

        - `:"session.status_rescheduled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusRunStartedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_run_started"`

        - `:"session.status_run_started"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusIdledEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_idled"`

        - `:"session.status_idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusTerminatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_terminated"`

        - `:"session.status_terminated"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadCreatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `type: :"session.thread_created"`

        - `:"session.thread_created"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadIdledEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `type: :"session.thread_idled"`

        - `:"session.thread_idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadTerminatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `type: :"session.thread_terminated"`

        - `:"session.thread_terminated"`

      - `workspace_id: String`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.outcome_evaluation_ended"`

        - `:"session.outcome_evaluation_ended"`

      - `workspace_id: String`

    - `class BetaWebhookVaultCreatedEventData`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `type: :"vault.created"`

        - `:"vault.created"`

      - `workspace_id: String`

    - `class BetaWebhookVaultArchivedEventData`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `type: :"vault.archived"`

        - `:"vault.archived"`

      - `workspace_id: String`

    - `class BetaWebhookVaultDeletedEventData`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `type: :"vault.deleted"`

        - `:"vault.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialCreatedEventData`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.created"`

        - `:"vault_credential.created"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialArchivedEventData`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.archived"`

        - `:"vault_credential.archived"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialDeletedEventData`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.deleted"`

        - `:"vault_credential.deleted"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.refresh_failed"`

        - `:"vault_credential.refresh_failed"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookSessionUpdatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.updated"`

        - `:"session.updated"`

      - `workspace_id: String`

    - `class BetaWebhookAgentCreatedEventData`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `type: :"agent.created"`

        - `:"agent.created"`

      - `workspace_id: String`

    - `class BetaWebhookAgentArchivedEventData`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `type: :"agent.archived"`

        - `:"agent.archived"`

      - `workspace_id: String`

    - `class BetaWebhookAgentDeletedEventData`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `type: :"agent.deleted"`

        - `:"agent.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentPausedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.paused"`

        - `:"deployment.paused"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunFailedEventData`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `type: :"deployment_run.failed"`

        - `:"deployment_run.failed"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentCreatedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.created"`

        - `:"deployment.created"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentUpdatedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.updated"`

        - `:"deployment.updated"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentUnpausedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.unpaused"`

        - `:"deployment.unpaused"`

      - `workspace_id: String`

    - `class BetaWebhookAgentUpdatedEventData`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `type: :"agent.updated"`

        - `:"agent.updated"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentArchivedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.archived"`

        - `:"deployment.archived"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunStartedEventData`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `type: :"deployment_run.started"`

        - `:"deployment_run.started"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentDeletedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.deleted"`

        - `:"deployment.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunSucceededEventData`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `type: :"deployment_run.succeeded"`

        - `:"deployment_run.succeeded"`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentCreatedEventData`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `type: :"environment.created"`

        - `:"environment.created"`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentUpdatedEventData`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `type: :"environment.updated"`

        - `:"environment.updated"`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentArchivedEventData`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `type: :"environment.archived"`

        - `:"environment.archived"`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentDeletedEventData`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `type: :"environment.deleted"`

        - `:"environment.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreCreatedEventData`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `type: :"memory_store.created"`

        - `:"memory_store.created"`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreArchivedEventData`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `type: :"memory_store.archived"`

        - `:"memory_store.archived"`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreDeletedEventData`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `type: :"memory_store.deleted"`

        - `:"memory_store.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookSessionBudgetReachedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.budget_reached"`

        - `:"session.budget_reached"`

      - `workspace_id: String`

  - `type: :event`

    Object type. Always `event` for webhook payloads.

    - `:event`
