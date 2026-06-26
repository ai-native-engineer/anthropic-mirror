<!-- source: https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve -->

# Get Session Resource
GET/v1/sessions/{session_id}/resources/{resource_id}
Get Session Resource
##### Path ParametersExpand Collapse 
session_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#retrieve.session_id)
resource_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#retrieve.resource_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#retrieve.betas)
BetaManagedAgentsGitHubRepositoryResource object { id, created_at, mount_path, 4 more } 
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_github_repository_resource.id)
created_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_github_repository_resource.created_at)
mount_path: string
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_github_repository_resource.mount_path)
type: "github_repository"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_github_repository_resource.type)
updated_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_github_repository_resource.updated_at)
url: string
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_github_repository_resource.url)
checkout: optional [BetaManagedAgentsBranchCheckout](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_branch_checkout) { name, type }  or [BetaManagedAgentsCommitCheckout](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_commit_checkout) { sha, type } 
BetaManagedAgentsBranchCheckout object { name, type } 
name: string
Branch name to check out.
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_branch_checkout.name)
type: "branch"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_branch_checkout.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_branch_checkout)
BetaManagedAgentsCommitCheckout object { sha, type } 
sha: string
Full commit SHA to check out.
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_commit_checkout.sha)
type: "commit"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_commit_checkout.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_commit_checkout)
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_github_repository_resource.checkout)
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_github_repository_resource)
BetaManagedAgentsFileResource object { id, created_at, file_id, 3 more } 
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_file_resource.id)
created_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_file_resource.created_at)
file_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_file_resource.file_id)
mount_path: string
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_file_resource.mount_path)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_file_resource.type)
updated_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_file_resource.updated_at)
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_file_resource)
BetaManagedAgentsMemoryStoreResource object { memory_store_id, type, access, 4 more } 
A memory store attached to an agent session.
memory_store_id: string
The memory store ID (memstore_...). Must belong to the caller's organization and workspace.
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_memory_store_resource.memory_store_id)
type: "memory_store"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_memory_store_resource.type)
access: optional "read_write" or "read_only"
Access mode for an attached memory store.
"read_write"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_memory_store_resource.access%5B0%5D)
"read_only"
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_memory_store_resource.access%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_memory_store_resource.access)
description: optional string
Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_memory_store_resource.description)
instructions: optional string
Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_memory_store_resource.instructions)
mount_path: optional string
Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_memory_store_resource.mount_path)
name: optional string
Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_memory_store_resource.name)
[](https://platform.claude.com/docs/en/api/beta/sessions/resources/retrieve#beta_managed_agents_memory_store_resource)
Get Session Resource
cURL

curl https://api.anthropic.com/v1/sessions/$SESSION_ID/resources/$RESOURCE_ID \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"

  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
