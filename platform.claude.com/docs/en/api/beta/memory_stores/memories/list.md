<!-- source: https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list -->

# List memories
GET/v1/memory_stores/{memory_store_id}/memories
List memories
##### Path ParametersExpand Collapse 
memory_store_id: string
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#list.memory_store_id)
##### Query ParametersExpand Collapse 
depth: optional number
Query parameter for depth
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#list.depth)
limit: optional number
Query parameter for limit
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#list.limit)
order: optional "asc" or "desc"
Query parameter for order
"asc"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#list.order%5B0%5D)
"desc"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#list.order%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#list.order)
order_by: optional string
Query parameter for order_by
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#list.order_by)
page: optional string
Query parameter for page
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#list.page)
path_prefix: optional string
Optional path prefix filter (raw string-prefix match; include a trailing slash for directory-scoped lists). This value appears in request URLs. Do not include secrets or personally identifiable information.
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#list.path_prefix)
view: optional [BetaManagedAgentsMemoryView](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_memory_view)
Query parameter for view
"basic"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#list.view%5B0%5D)
"full"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#list.view%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#list.view)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#list.betas)
data: optional array of [BetaManagedAgentsMemoryListItem](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_memory_list_item)
One page of results. Each item is either a `memory` object or, when `depth` was set, a `memory_prefix` rollup marker. Items appear in the requested `order_by`/`order`.
BetaManagedAgentsMemory object { id, content_sha256, content_size_bytes, 7 more } 
A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.
Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#beta_managed_agents_memory.id)
content_sha256: string
Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#beta_managed_agents_memory.content_sha256)
content_size_bytes: number
Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#beta_managed_agents_memory.content_size_bytes)
created_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#beta_managed_agents_memory.created_at)
memory_store_id: string
ID of the memory store this memory belongs to (a `memstore_...` value).
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#beta_managed_agents_memory.memory_store_id)
memory_version_id: string
ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list).
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#beta_managed_agents_memory.memory_version_id)
path: string
Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#beta_managed_agents_memory.path)
type: "memory"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#beta_managed_agents_memory.type)
updated_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#beta_managed_agents_memory.updated_at)
content: optional string
The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#beta_managed_agents_memory.content)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#beta_managed_agents_memory)
BetaManagedAgentsMemoryPrefix object { path, type } 
A rolled-up directory marker returned by [List memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.
path: string
The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#beta_managed_agents_memory_prefix.path)
type: "memory_prefix"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#beta_managed_agents_memory_prefix.type)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#beta_managed_agents_memory_prefix)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#list)
next_page: optional string
Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list#list)
List memories
cURL

curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "data": [
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
  ],
  "next_page": "next_page"

  "data": [
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
  ],
  "next_page": "next_page"
