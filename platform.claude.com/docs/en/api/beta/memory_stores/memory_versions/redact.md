<!-- source: https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact -->

# Redact a memory version
POST/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact
Redact a memory version
##### Path ParametersExpand Collapse 
memory_store_id: string
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#redact.memory_store_id)
memory_version_id: string
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#redact.memory_version_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#redact.betas)
BetaManagedAgentsMemoryVersion object { id, created_at, memory_id, 10 more } 
A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.
Unique identifier for this version (a `memver_...` value).
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.id)
created_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.created_at)
memory_id: string
ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.memory_id)
memory_store_id: string
ID of the memory store this version belongs to (a `memstore_...` value).
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.memory_store_id)
operation: [BetaManagedAgentsMemoryVersionOperation](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_memory_version_operation)
The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.
"created"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.operation%20%2B%20\(resource\)%20beta.memory_stores.memory_versions%5B0%5D)
"modified"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.operation%20%2B%20\(resource\)%20beta.memory_stores.memory_versions%5B1%5D)
"deleted"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.operation%20%2B%20\(resource\)%20beta.memory_stores.memory_versions%5B2%5D)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.operation)
type: "memory_version"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.type)
content: optional string
The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.content)
content_sha256: optional string
Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.content_sha256)
content_size_bytes: optional number
Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.content_size_bytes)
created_by: optional [BetaManagedAgentsActor](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_actor)
Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](https://platform.claude.com/docs/en/api/sessions-retrieve).
BetaManagedAgentsSessionActor object { session_id, type } 
Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.
session_id: string
ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/sessions-retrieve) for further provenance.
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.created_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions.session_id)
type: "session_actor"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.created_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions.type)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.created_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions)
BetaManagedAgentsAPIActor object { api_key_id, type } 
Attribution for a write made directly via the public API (outside of any session).
api_key_id: string
ID of the API key that performed the write. This identifies the key, not the secret.
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.created_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions.api_key_id)
type: "api_actor"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.created_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions.type)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.created_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions)
BetaManagedAgentsUserActor object { type, user_id } 
Attribution for a write made by a human user through the Anthropic Console.
type: "user_actor"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.created_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions.type)
user_id: string
ID of the user who performed the write (a `user_...` value).
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.created_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions.user_id)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.created_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.created_by)
path: optional string
The memory's path at the time of this write. `null` if and only if `redacted_at` is set.
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.path)
redacted_at: optional string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.redacted_at)
redacted_by: optional [BetaManagedAgentsActor](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_actor)
Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](https://platform.claude.com/docs/en/api/sessions-retrieve).
BetaManagedAgentsSessionActor object { session_id, type } 
Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.
session_id: string
ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/sessions-retrieve) for further provenance.
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.redacted_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions.session_id)
type: "session_actor"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.redacted_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions.type)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.redacted_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions)
BetaManagedAgentsAPIActor object { api_key_id, type } 
Attribution for a write made directly via the public API (outside of any session).
api_key_id: string
ID of the API key that performed the write. This identifies the key, not the secret.
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.redacted_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions.api_key_id)
type: "api_actor"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.redacted_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions.type)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.redacted_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions)
BetaManagedAgentsUserActor object { type, user_id } 
Attribution for a write made by a human user through the Anthropic Console.
type: "user_actor"
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.redacted_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions.type)
user_id: string
ID of the user who performed the write (a `user_...` value).
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.redacted_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions.user_id)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.redacted_by%20%2B%20\(resource\)%20beta.memory_stores.memory_versions)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version.redacted_by)
[](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact#beta_managed_agents_memory_version)
Redact a memory version
cURL

curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions/$MEMORY_VERSION_ID/redact \
    -X POST \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

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
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"

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
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
