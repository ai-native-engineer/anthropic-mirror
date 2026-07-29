<!-- source: https://platform.claude.com/docs/en/api/python/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/python/beta -->

<!-- chunk-start -->
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Session Resource

`beta.sessions.resources.retrieve(strresource_id, ResourceRetrieveParams**kwargs)  -> ResourceRetrieveResponse`

**get** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

### Parameters

- `session_id: str`

- `resource_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `ResourceRetrieveResponse`

  The requested session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource: …`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

    - `mount_path: str`

    - `type: Literal["github_repository"]`

      - `"github_repository"`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

    - `url: str`

    - `checkout: Optional[Checkout]`

      - `class BetaManagedAgentsBranchCheckout: …`

        - `name: str`

          Branch name to check out.

        - `type: Literal["branch"]`

          - `"branch"`

      - `class BetaManagedAgentsCommitCheckout: …`

        - `sha: str`

          Full commit SHA to check out.

        - `type: Literal["commit"]`

          - `"commit"`

  - `class BetaManagedAgentsFileResource: …`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

    - `file_id: str`

    - `mount_path: str`

    - `type: Literal["file"]`

      - `"file"`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsMemoryStoreResource: …`

    A memory store attached to an agent session.

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: Literal["memory_store"]`

      - `"memory_store"`

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description: Optional[str]`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `mount_path: Optional[str]`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: Optional[str]`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
resource = client.beta.sessions.resources.retrieve(
    resource_id="sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(resource)
```

#### Response

```json
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```

## Update Session Resource

`beta.sessions.resources.update(strresource_id, ResourceUpdateParams**kwargs)  -> ResourceUpdateResponse`

**post** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

### Parameters

- `session_id: str`

- `resource_id: str`

- `authorization_token: str`

  New authorization token for the resource. Currently only `github_repository` resources support token rotation.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `ResourceUpdateResponse`

  The updated session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource: …`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

    - `mount_path: str`

    - `type: Literal["github_repository"]`

      - `"github_repository"`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

    - `url: str`

    - `checkout: Optional[Checkout]`

      - `class BetaManagedAgentsBranchCheckout: …`

        - `name: str`

          Branch name to check out.

        - `type: Literal["branch"]`

          - `"branch"`

      - `class BetaManagedAgentsCommitCheckout: …`

        - `sha: str`

          Full commit SHA to check out.

        - `type: Literal["commit"]`

          - `"commit"`

  - `class BetaManagedAgentsFileResource: …`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

    - `file_id: str`

    - `mount_path: str`

    - `type: Literal["file"]`

      - `"file"`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsMemoryStoreResource: …`

    A memory store attached to an agent session.

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: Literal["memory_store"]`

      - `"memory_store"`

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description: Optional[str]`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `mount_path: Optional[str]`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: Optional[str]`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
resource = client.beta.sessions.resources.update(
    resource_id="sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
    authorization_token="ghp_exampletoken",
)
print(resource)
```

#### Response

```json
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```

## Delete Session Resource

`beta.sessions.resources.delete(strresource_id, ResourceDeleteParams**kwargs)  -> BetaManagedAgentsDeleteSessionResource`

**delete** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

### Parameters

- `session_id: str`

- `resource_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaManagedAgentsDeleteSessionResource: …`

  Confirmation of resource deletion.

  - `id: str`

  - `type: Literal["session_resource_deleted"]`

    - `"session_resource_deleted"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_delete_session_resource = client.beta.sessions.resources.delete(
    resource_id="sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_delete_session_resource.id)
```

#### Response

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "type": "session_resource_deleted"
}
```

## Domain Types

### Beta Managed Agents Delete Session Resource

- `class BetaManagedAgentsDeleteSessionResource: …`

  Confirmation of resource deletion.

  - `id: str`

  - `type: Literal["session_resource_deleted"]`

    - `"session_resource_deleted"`

### Beta Managed Agents File Resource

- `class BetaManagedAgentsFileResource: …`

  - `id: str`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `file_id: str`

  - `mount_path: str`

  - `type: Literal["file"]`

    - `"file"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

### Beta Managed Agents GitHub Repository Resource

- `class BetaManagedAgentsGitHubRepositoryResource: …`

  - `id: str`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `mount_path: str`

  - `type: Literal["github_repository"]`

    - `"github_repository"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `url: str`

  - `checkout: Optional[Checkout]`

    - `class BetaManagedAgentsBranchCheckout: …`

      - `name: str`

        Branch name to check out.

      - `type: Literal["branch"]`

        - `"branch"`

    - `class BetaManagedAgentsCommitCheckout: …`

      - `sha: str`

        Full commit SHA to check out.

      - `type: Literal["commit"]`

        - `"commit"`

### Beta Managed Agents Memory Store Resource

- `class BetaManagedAgentsMemoryStoreResource: …`

  A memory store attached to an agent session.

  - `memory_store_id: str`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `type: Literal["memory_store"]`

    - `"memory_store"`

  - `access: Optional[Literal["read_write", "read_only"]]`

    Access mode for an attached memory store.

    - `"read_write"`

    - `"read_only"`

  - `description: Optional[str]`

    Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

  - `instructions: Optional[str]`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `mount_path: Optional[str]`

    Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

  - `name: Optional[str]`

    Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Beta Managed Agents Session Resource

- `BetaManagedAgentsSessionResource`

  A memory store attached to an agent session.

  - `class BetaManagedAgentsGitHubRepositoryResource: …`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

    - `mount_path: str`

    - `type: Literal["github_repository"]`

      - `"github_repository"`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

    - `url: str`

    - `checkout: Optional[Checkout]`

      - `class BetaManagedAgentsBranchCheckout: …`

        - `name: str`

          Branch name to check out.

        - `type: Literal["branch"]`

          - `"branch"`

      - `class BetaManagedAgentsCommitCheckout: …`

        - `sha: str`

          Full commit SHA to check out.

        - `type: Literal["commit"]`

          - `"commit"`

  - `class BetaManagedAgentsFileResource: …`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

    - `file_id: str`

    - `mount_path: str`

    - `type: Literal["file"]`

      - `"file"`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsMemoryStoreResource: …`

    A memory store attached to an agent session.

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: Literal["memory_store"]`

      - `"memory_store"`

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description: Optional[str]`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `mount_path: Optional[str]`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: Optional[str]`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Resource Retrieve Response

- `ResourceRetrieveResponse`

  The requested session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource: …`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

    - `mount_path: str`

    - `type: Literal["github_repository"]`

      - `"github_repository"`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

    - `url: str`

    - `checkout: Optional[Checkout]`

      - `class BetaManagedAgentsBranchCheckout: …`

        - `name: str`

          Branch name to check out.

        - `type: Literal["branch"]`

          - `"branch"`

      - `class BetaManagedAgentsCommitCheckout: …`

        - `sha: str`

          Full commit SHA to check out.

        - `type: Literal["commit"]`

          - `"commit"`

  - `class BetaManagedAgentsFileResource: …`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

    - `file_id: str`

    - `mount_path: str`

    - `type: Literal["file"]`

      - `"file"`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsMemoryStoreResource: …`

    A memory store attached to an agent session.

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: Literal["memory_store"]`

      - `"memory_store"`

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description: Optional[str]`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `mount_path: Optional[str]`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: Optional[str]`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Resource Update Response

- `ResourceUpdateResponse`

  The updated session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource: …`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

    - `mount_path: str`

    - `type: Literal["github_repository"]`

      - `"github_repository"`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

    - `url: str`

    - `checkout: Optional[Checkout]`

      - `class BetaManagedAgentsBranchCheckout: …`

        - `name: str`

          Branch name to check out.

        - `type: Literal["branch"]`

          - `"branch"`

      - `class BetaManagedAgentsCommitCheckout: …`

        - `sha: str`

          Full commit SHA to check out.

        - `type: Literal["commit"]`

          - `"commit"`

  - `class BetaManagedAgentsFileResource: …`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

    - `file_id: str`

    - `mount_path: str`

    - `type: Literal["file"]`

      - `"file"`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsMemoryStoreResource: …`

    A memory store attached to an agent session.

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: Literal["memory_store"]`

      - `"memory_store"`

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description: Optional[str]`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `mount_path: Optional[str]`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: Optional[str]`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

# Threads

## List Session Threads

`beta.sessions.threads.list(strsession_id, ThreadListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsSessionThread]`

**get** `/v1/sessions/{session_id}/threads`

List Session Threads

### Parameters

- `session_id: str`

- `limit: Optional[int]`

  Maximum results per page. Defaults to 1000.

- `page: Optional[str]`

  Opaque pagination cursor from a previous response's next_page. Forward-only.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaManagedAgentsSessionThread: …`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: str`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

    - `id: str`

    - `description: Optional[str]`

    - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

      - `name: str`

      - `type: Literal["url"]`

        - `"url"`

      - `url: str`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-5", 10 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `"claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `str`

      - `effort: Optional[Effort]`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow: …`

          Low effort. Favors latency over reasoning depth.

          - `type: Literal["low"]`

            - `"low"`

        - `class BetaManagedAgentsEffortMedium: …`

          Medium effort. Balances latency and reasoning depth.

          - `type: Literal["medium"]`

            - `"medium"`

        - `class BetaManagedAgentsEffortHigh: …`

          High effort. Favors reasoning depth.

          - `type: Literal["high"]`

            - `"high"`

        - `class BetaManagedAgentsEffortXhigh: …`

          Extra-high effort. Not all models accept this level.

          - `type: Literal["xhigh"]`

            - `"xhigh"`

        - `class BetaManagedAgentsEffortMax: …`

          Maximum effort. Favors reasoning depth over latency.

          - `type: Literal["max"]`

            - `"max"`

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `name: str`

    - `skills: List[Skill]`

      - `class BetaManagedAgentsAnthropicSkill: …`

        A resolved Anthropic-managed skill.

        - `skill_id: str`

        - `type: Literal["anthropic"]`

          - `"anthropic"`

        - `version: str`

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

        - `skill_id: str`

        - `type: Literal["custom"]`

          - `"custom"`

        - `version: str`

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

        - `configs: List[BetaManagedAgentsAgentToolConfig]`

          - `enabled: bool`

          - `name: Literal["bash", "edit", "read", 5 more]`

            Built-in agent tool identifier.

            - `"bash"`

            - `"edit"`

            - `"read"`

            - `"write"`

            - `"glob"`

            - `"grep"`

            - `"web_fetch"`

            - `"web_search"`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

              - `type: Literal["always_allow"]`

                - `"always_allow"`

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

              - `type: Literal["always_ask"]`

                - `"always_ask"`

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

          Resolved default configuration for agent tools.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `type: Literal["agent_toolset_20260401"]`

          - `"agent_toolset_20260401"`

      - `class BetaManagedAgentsMCPToolset: …`

        - `configs: List[BetaManagedAgentsMCPToolConfig]`

          - `enabled: bool`

          - `name: str`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: str`

        - `type: Literal["mcp_toolset"]`

          - `"mcp_toolset"`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

        - `description: str`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: Literal["object"]`

            - `"object"`

          - `properties: Optional[Dict[str, object]]`

          - `required: Optional[List[str]]`

        - `name: str`

        - `type: Literal["custom"]`

          - `"custom"`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `parent_thread_id: Optional[str]`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: str`

    The session this thread belongs to.

  - `stats: Optional[BetaManagedAgentsSessionThreadStats]`

    Timing statistics for a session thread.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `duration_seconds: Optional[float]`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `startup_seconds: Optional[float]`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: Literal["session_thread"]`

    - `"session_thread"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `usage: Optional[BetaManagedAgentsSessionThreadUsage]`

    Cumulative token usage for a session thread across all turns.

    - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Optional[int]`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: Optional[int]`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: Optional[int]`

      Total tokens read from prompt cache.

    - `input_tokens: Optional[int]`

      Total input tokens consumed across all turns.

    - `output_tokens: Optional[int]`

      Total output tokens generated across all turns.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.sessions.threads.list(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
page = page.data[0]
print(page.id)
```

#### Response

```json
{
  "data": [
    {
      "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
      "agent": {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "description": "A focused research subagent.",
        "mcp_servers": [
          {
            "name": "example-mcp",
            "type": "url",
            "url": "https://example-server.modelcontextprotocol.io/sse"
          }
        ],
        "model": {
          "id": "claude-sonnet-4-6",
          "effort": {
            "type": "low"
          },
          "speed": "standard"
        },
        "name": "Researcher",
        "skills": [
          {
            "skill_id": "xlsx",
            "type": "anthropic",
            "version": "1"
          }
        ],
        "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
        "tools": [
          {
            "configs": [
              {
                "enabled": true,
                "name": "bash",
                "permission_policy": {
                  "type": "always_allow"
                }
              }
            ],
            "default_config": {
              "enabled": true,
              "permission_policy": {
                "type": "always_ask"
              }
            },
            "type": "agent_toolset_20260401"
          }
        ],
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "parent_thread_id": null,
      "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
      "stats": {
        "active_seconds": 0,
        "duration_seconds": 0,
        "startup_seconds": 0
      },
      "status": "idle",
      "type": "session_thread",
      "updated_at": "2026-03-15T10:00:00Z",
      "usage": {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Session Thread

`beta.sessions.threads.retrieve(strthread_id, ThreadRetrieveParams**kwargs)  -> BetaManagedAgentsSessionThread`

**get** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

### Parameters

- `session_id: str`

- `thread_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaManagedAgentsSessionThread: …`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: str`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

    - `id: str`

    - `description: Optional[str]`

    - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

      - `name: str`

      - `type: Literal["url"]`

        - `"url"`

      - `url: str`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-5", 10 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `"claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `str`

      - `effort: Optional[Effort]`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow: …`

          Low effort. Favors latency over reasoning depth.

          - `type: Literal["low"]`

            - `"low"`

        - `class BetaManagedAgentsEffortMedium: …`

          Medium effort. Balances latency and reasoning depth.

          - `type: Literal["medium"]`

            - `"medium"`

        - `class BetaManagedAgentsEffortHigh: …`

          High effort. Favors reasoning depth.

          - `type: Literal["high"]`

            - `"high"`

        - `class BetaManagedAgentsEffortXhigh: …`

          Extra-high effort. Not all models accept this level.

          - `type: Literal["xhigh"]`

            - `"xhigh"`

        - `class BetaManagedAgentsEffortMax: …`

          Maximum effort. Favors reasoning depth over latency.

          - `type: Literal["max"]`

            - `"max"`

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `name: str`

    - `skills: List[Skill]`

      - `class BetaManagedAgentsAnthropicSkill: …`

        A resolved Anthropic-managed skill.

        - `skill_id: str`

        - `type: Literal["anthropic"]`

          - `"anthropic"`

        - `version: str`

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

        - `skill_id: str`

        - `type: Literal["custom"]`

          - `"custom"`

        - `version: str`

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

        - `configs: List[BetaManagedAgentsAgentToolConfig]`

          - `enabled: bool`

          - `name: Literal["bash", "edit", "read", 5 more]`

            Built-in agent tool identifier.

            - `"bash"`

            - `"edit"`

            - `"read"`

            - `"write"`

            - `"glob"`

            - `"grep"`

            - `"web_fetch"`

            - `"web_search"`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

              - `type: Literal["always_allow"]`

                - `"always_allow"`

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

              - `type: Literal["always_ask"]`

                - `"always_ask"`

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

          Resolved default configuration for agent tools.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `type: Literal["agent_toolset_20260401"]`

          - `"agent_toolset_20260401"`

      - `class BetaManagedAgentsMCPToolset: …`

        - `configs: List[BetaManagedAgentsMCPToolConfig]`

          - `enabled: bool`

          - `name: str`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: str`

        - `type: Literal["mcp_toolset"]`

          - `"mcp_toolset"`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

        - `description: str`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: Literal["object"]`

            - `"object"`

          - `properties: Optional[Dict[str, object]]`

          - `required: Optional[List[str]]`

        - `name: str`

        - `type: Literal["custom"]`

          - `"custom"`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `parent_thread_id: Optional[str]`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: str`

    The session this thread belongs to.

  - `stats: Optional[BetaManagedAgentsSessionThreadStats]`

    Timing statistics for a session thread.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `duration_seconds: Optional[float]`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `startup_seconds: Optional[float]`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: Literal["session_thread"]`

    - `"session_thread"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `usage: Optional[BetaManagedAgentsSessionThreadUsage]`

    Cumulative token usage for a session thread across all turns.

    - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Optional[int]`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: Optional[int]`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: Optional[int]`

      Total tokens read from prompt cache.

    - `input_tokens: Optional[int]`

      Total input tokens consumed across all turns.

    - `output_tokens: Optional[int]`

      Total output tokens generated across all turns.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_session_thread = client.beta.sessions.threads.retrieve(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_session_thread.id)
```

#### Response

```json
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "description": "A focused research subagent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "effort": {
        "type": "low"
      },
      "speed": "standard"
    },
    "name": "Researcher",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      }
    ],
    "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            }
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Archive Session Thread

`beta.sessions.threads.archive(strthread_id, ThreadArchiveParams**kwargs)  -> BetaManagedAgentsSessionThread`

**post** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

### Parameters

- `session_id: str`

- `thread_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaManagedAgentsSessionThread: …`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: str`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

    - `id: str`

    - `description: Optional[str]`

    - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

      - `name: str`

      - `type: Literal["url"]`

        - `"url"`

      - `url: str`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-5", 10 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `"claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `str`

      - `effort: Optional[Effort]`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow: …`

          Low effort. Favors latency over reasoning depth.

          - `type: Literal["low"]`

            - `"low"`

        - `class BetaManagedAgentsEffortMedium: …`

          Medium effort. Balances latency and reasoning depth.

          - `type: Literal["medium"]`

            - `"medium"`

        - `class BetaManagedAgentsEffortHigh: …`

          High effort. Favors reasoning depth.

          - `type: Literal["high"]`

            - `"high"`

        - `class BetaManagedAgentsEffortXhigh: …`

          Extra-high effort. Not all models accept this level.

          - `type: Literal["xhigh"]`

            - `"xhigh"`

        - `class BetaManagedAgentsEffortMax: …`

          Maximum effort. Favors reasoning depth over latency.

          - `type: Literal["max"]`

            - `"max"`

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `name: str`

    - `skills: List[Skill]`

      - `class BetaManagedAgentsAnthropicSkill: …`

        A resolved Anthropic-managed skill.

        - `skill_id: str`

        - `type: Literal["anthropic"]`

          - `"anthropic"`

        - `version: str`

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

        - `skill_id: str`

        - `type: Literal["custom"]`

          - `"custom"`

        - `version: str`

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

        - `configs: List[BetaManagedAgentsAgentToolConfig]`

          - `enabled: bool`

          - `name: Literal["bash", "edit", "read", 5 more]`

            Built-in agent tool identifier.

            - `"bash"`

            - `"edit"`

            - `"read"`

            - `"write"`

            - `"glob"`

            - `"grep"`

            - `"web_fetch"`

            - `"web_search"`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

              - `type: Literal["always_allow"]`

                - `"always_allow"`

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

              - `type: Literal["always_ask"]`

                - `"always_ask"`

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

          Resolved default configuration for agent tools.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `type: Literal["agent_toolset_20260401"]`

          - `"agent_toolset_20260401"`

      - `class BetaManagedAgentsMCPToolset: …`

        - `configs: List[BetaManagedAgentsMCPToolConfig]`

          - `enabled: bool`

          - `name: str`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: str`

        - `type: Literal["mcp_toolset"]`

          - `"mcp_toolset"`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

        - `description: str`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: Literal["object"]`

            - `"object"`

          - `properties: Optional[Dict[str, object]]`

          - `required: Optional[List[str]]`

        - `name: str`

        - `type: Literal["custom"]`

          - `"custom"`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `parent_thread_id: Optional[str]`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: str`

    The session this thread belongs to.

  - `stats: Optional[BetaManagedAgentsSessionThreadStats]`

    Timing statistics for a session thread.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `duration_seconds: Optional[float]`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `startup_seconds: Optional[float]`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: Literal["session_thread"]`

    - `"session_thread"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `usage: Optional[BetaManagedAgentsSessionThreadUsage]`

    Cumulative token usage for a session thread across all turns.

    - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Optional[int]`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: Optional[int]`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: Optional[int]`

      Total tokens read from prompt cache.

    - `input_tokens: Optional[int]`

      Total input tokens consumed across all turns.

    - `output_tokens: Optional[int]`

      Total output tokens generated across all turns.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_session_thread = client.beta.sessions.threads.archive(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_session_thread.id)
```

#### Response

```json
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "description": "A focused research subagent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "effort": {
        "type": "low"
      },
      "speed": "standard"
    },
    "name": "Researcher",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      }
    ],
    "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            }
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Domain Types

### Beta Managed Agents Session Thread

- `class BetaManagedAgentsSessionThread: …`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: str`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

    - `id: str`

    - `description: Optional[str]`

    - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

      - `name: str`

      - `type: Literal["url"]`

        - `"url"`

      - `url: str`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-5", 10 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `"claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `str`

      - `effort: Optional[Effort]`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow: …`

          Low effort. Favors latency over reasoning depth.

          - `type: Literal["low"]`

            - `"low"`

        - `class BetaManagedAgentsEffortMedium: …`

          Medium effort. Balances latency and reasoning depth.

          - `type: Literal["medium"]`

            - `"medium"`

        - `class BetaManagedAgentsEffortHigh: …`

          High effort. Favors reasoning depth.

          - `type: Literal["high"]`

            - `"high"`

        - `class BetaManagedAgentsEffortXhigh: …`

          Extra-high effort. Not all models accept this level.

          - `type: Literal["xhigh"]`

            - `"xhigh"`

        - `class BetaManagedAgentsEffortMax: …`

          Maximum effort. Favors reasoning depth over latency.

          - `type: Literal["max"]`

            - `"max"`

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `name: str`

    - `skills: List[Skill]`

      - `class BetaManagedAgentsAnthropicSkill: …`

        A resolved Anthropic-managed skill.

        - `skill_id: str`

        - `type: Literal["anthropic"]`

          - `"anthropic"`

        - `version: str`

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

        - `skill_id: str`

        - `type: Literal["custom"]`

          - `"custom"`

        - `version: str`

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

        - `configs: List[BetaManagedAgentsAgentToolConfig]`

          - `enabled: bool`

          - `name: Literal["bash", "edit", "read", 5 more]`

            Built-in agent tool identifier.

            - `"bash"`

            - `"edit"`

            - `"read"`

            - `"write"`

            - `"glob"`

            - `"grep"`

            - `"web_fetch"`

            - `"web_search"`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

              - `type: Literal["always_allow"]`

                - `"always_allow"`

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

              - `type: Literal["always_ask"]`

                - `"always_ask"`

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

          Resolved default configuration for agent tools.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `type: Literal["agent_toolset_20260401"]`

          - `"agent_toolset_20260401"`

      - `class BetaManagedAgentsMCPToolset: …`

        - `configs: List[BetaManagedAgentsMCPToolConfig]`

          - `enabled: bool`

          - `name: str`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: str`

        - `type: Literal["mcp_toolset"]`

          - `"mcp_toolset"`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

        - `description: str`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: Literal["object"]`

            - `"object"`

          - `properties: Optional[Dict[str, object]]`

          - `required: Optional[List[str]]`

        - `name: str`

        - `type: Literal["custom"]`

          - `"custom"`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `parent_thread_id: Optional[str]`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: str`

    The session this thread belongs to.

  - `stats: Optional[BetaManagedAgentsSessionThreadStats]`

    Timing statistics for a session thread.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `duration_seconds: Optional[float]`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `startup_seconds: Optional[float]`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: Literal["session_thread"]`

    - `"session_thread"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `usage: Optional[BetaManagedAgentsSessionThreadUsage]`

    Cumulative token usage for a session thread across all turns.

    - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Optional[int]`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: Optional[int]`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: Optional[int]`

      Total tokens read from prompt cache.

    - `input_tokens: Optional[int]`

      Total input tokens consumed across all turns.

    - `output_tokens: Optional[int]`

      Total output tokens generated across all turns.

### Beta Managed Agents Session Thread Stats

- `class BetaManagedAgentsSessionThreadStats: …`

  Timing statistics for a session thread.

  - `active_seconds: Optional[float]`

    Cumulative time in seconds the thread spent actively running. Excludes idle time.

  - `duration_seconds: Optional[float]`

    Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

  - `startup_seconds: Optional[float]`

    Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

### Beta Managed Agents Session Thread Status

- `Literal["running", "idle", "rescheduling", "terminated"]`

  SessionThreadStatus enum

  - `"running"`

  - `"idle"`

  - `"rescheduling"`

  - `"terminated"`

### Beta Managed Agents Session Thread Usage

- `class BetaManagedAgentsSessionThreadUsage: …`

  Cumulative token usage for a session thread across all turns.

  - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

    Prompt-cache creation token usage broken down by cache lifetime.

    - `ephemeral_1h_input_tokens: Optional[int]`

      Tokens used to create 1-hour ephemeral cache entries.

    - `ephemeral_5m_input_tokens: Optional[int]`

      Tokens used to create 5-minute ephemeral cache entries.

  - `cache_read_input_tokens: Optional[int]`

    Total tokens read from prompt cache.

  - `input_tokens: Optional[int]`

    Total input tokens consumed across all turns.

  - `output_tokens: Optional[int]`

    Total output tokens generated across all turns.

### Beta Managed Agents Stream Session Thread Events

- `BetaManagedAgentsStreamSessionThreadEvents`

  Server-sent event in a single thread's stream.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: str`

      Unique identifier for this event.

    - `type: Literal["user.interrupt"]`

      - `"user.interrupt"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_confirmation"]`

      - `"user.tool_confirmation"`

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.custom_tool_result"]`

      - `"user.custom_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `source: str`

          The URL source of the search result.

        - `title: str`

          The title of the search result.

        - `type: Literal["search_result"]`

          - `"search_result"`

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.custom_tool_use"]`

      - `"agent.custom_tool_use"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.message"]`

      - `"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thinking"]`

      - `"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_use"]`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_result"]`

      - `"agent.mcp_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.tool_use"]`

      - `"agent.tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: Literal["agent.tool_result"]`

      - `"agent.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_message_received"]`

      - `"agent.thread_message_received"`

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: Literal["agent.thread_message_sent"]`

      - `"agent.thread_message_sent"`

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_context_compacted"]`

      - `"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

              - `"retrying"`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

              - `"exhausted"`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

              - `"terminal"`

        - `type: Literal["unknown_error"]`

          - `"unknown_error"`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_overloaded_error"]`

          - `"model_overloaded_error"`

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_rate_limited_error"]`

          - `"model_rate_limited_error"`

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_request_failed_error"]`

          - `"model_request_failed_error"`

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_connection_failed_error"]`

          - `"mcp_connection_failed_error"`

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_authentication_failed_error"]`

          - `"mcp_authentication_failed_error"`

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["billing_error"]`

          - `"billing_error"`

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["credential_host_unreachable_error"]`

          - `"credential_host_unreachable_error"`

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.error"]`

      - `"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_rescheduled"]`

      - `"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_running"]`

      - `"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

          - `"end_turn"`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: Literal["requires_action"]`

          - `"requires_action"`

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: Literal["retries_exhausted"]`

          - `"retries_exhausted"`

    - `type: Literal["session.status_idle"]`

      - `"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_terminated"]`

      - `"session.status_terminated"`

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

    - `type: Literal["session.thread_created"]`

      - `"session.thread_created"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_start"]`

      - `"span.outcome_evaluation_start"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: Literal["span.outcome_evaluation_end"]`

      - `"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

      - `input_tokens: int`

        Input tokens consumed by this request.

      - `output_tokens: int`

        Output tokens generated by this request.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_start"]`

      - `"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_end"]`

      - `"span.model_request_end"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_ongoing"]`

      - `"span.outcome_evaluation_ongoing"`

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.deleted"]`

      - `"session.deleted"`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

    - `type: Literal["session.thread_status_running"]`

      - `"session.thread_status_running"`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

    - `type: Literal["session.thread_status_idle"]`

      - `"session.thread_status_idle"`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

    - `type: Literal["session.thread_status_terminated"]`

      - `"session.thread_status_terminated"`

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_result"]`

      - `"user.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

    - `type: Literal["session.thread_status_rescheduled"]`

      - `"session.thread_status_rescheduled"`

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.updated"]`

      - `"session.updated"`

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: str`

      - `description: Optional[str]`

      - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

        - `name: str`

        - `type: Literal["url"]`

          - `"url"`

        - `url: str`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-5", 10 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

            - `"claude-sonnet-5"`

              High-performance model for coding and agents

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `"claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `"claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `"claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `"claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `str`

        - `effort: Optional[Effort]`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow: …`

            Low effort. Favors latency over reasoning depth.

            - `type: Literal["low"]`

              - `"low"`

          - `class BetaManagedAgentsEffortMedium: …`

            Medium effort. Balances latency and reasoning depth.

            - `type: Literal["medium"]`

              - `"medium"`

          - `class BetaManagedAgentsEffortHigh: …`

            High effort. Favors reasoning depth.

            - `type: Literal["high"]`

              - `"high"`

          - `class BetaManagedAgentsEffortXhigh: …`

            Extra-high effort. Not all models accept this level.

            - `type: Literal["xhigh"]`

              - `"xhigh"`

          - `class BetaManagedAgentsEffortMax: …`

            Maximum effort. Favors reasoning depth over latency.

            - `type: Literal["max"]`

              - `"max"`

        - `speed: Optional[Literal["standard", "fast"]]`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: List[BetaManagedAgentsSessionThreadAgent]`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `id: str`

          - `description: Optional[str]`

          - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

            - `name: str`

            - `type: Literal["url"]`

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `name: str`

          - `skills: List[Skill]`

            - `class BetaManagedAgentsAnthropicSkill: …`

              A resolved Anthropic-managed skill.

              - `skill_id: str`

              - `type: Literal["anthropic"]`

                - `"anthropic"`

              - `version: str`

            - `class BetaManagedAgentsCustomSkill: …`

              A resolved user-created custom skill.

              - `skill_id: str`

              - `type: Literal["custom"]`

                - `"custom"`

              - `version: str`

          - `system: Optional[str]`

          - `tools: List[Tool]`

            - `class BetaManagedAgentsAgentToolset20260401: …`

              - `configs: List[BetaManagedAgentsAgentToolConfig]`

                - `enabled: bool`

                - `name: Literal["bash", "edit", "read", 5 more]`

                  Built-in agent tool identifier.

                  - `"bash"`

                  - `"edit"`

                  - `"read"`

                  - `"write"`

                  - `"glob"`

                  - `"grep"`

                  - `"web_fetch"`

                  - `"web_search"`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                    - `type: Literal["always_allow"]`

                      - `"always_allow"`

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                    - `type: Literal["always_ask"]`

                      - `"always_ask"`

              - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `type: Literal["agent_toolset_20260401"]`

                - `"agent_toolset_20260401"`

            - `class BetaManagedAgentsMCPToolset: …`

              - `configs: List[BetaManagedAgentsMCPToolConfig]`

                - `enabled: bool`

                - `name: str`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: str`

              - `type: Literal["mcp_toolset"]`

                - `"mcp_toolset"`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                  - `"object"`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

              - `name: str`

              - `type: Literal["custom"]`

                - `"custom"`

          - `type: Literal["agent"]`

            - `"agent"`

          - `version: int`

        - `type: Literal["coordinator"]`

          - `"coordinator"`

      - `name: str`

      - `skills: List[Skill]`

        - `class BetaManagedAgentsAnthropicSkill: …`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `type: Literal["agent"]`

        - `"agent"`

      - `version: int`

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent: …`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview: …`

        - `id: str`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: Literal["agent.message"]`

          - `"agent.message"`

      - `class BetaManagedAgentsAgentThinkingPreview: …`

        - `id: str`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: Literal["agent.thinking"]`

          - `"agent.thinking"`

    - `type: Literal["event_start"]`

      - `"event_start"`

  - `class BetaManagedAgentsDeltaEvent: …`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: Literal["content_delta"]`

        - `"content_delta"`

      - `index: Optional[int]`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `event_id: str`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: Literal["event_delta"]`

      - `"event_delta"`

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

# Events

## List Session Thread Events

`beta.sessions.threads.events.list(strthread_id, EventListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsSessionEvent]`

**get** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

### Parameters

- `session_id: str`

- `thread_id: str`

- `limit: Optional[int]`

  Query parameter for limit

- `page: Optional[str]`

  Query parameter for page

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `BetaManagedAgentsSessionEvent`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: str`

      Unique identifier for this event.

    - `type: Literal["user.interrupt"]`

      - `"user.interrupt"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_confirmation"]`

      - `"user.tool_confirmation"`

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.custom_tool_result"]`

      - `"user.custom_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `source: str`

          The URL source of the search result.

        - `title: str`

          The title of the search result.

        - `type: Literal["search_result"]`

          - `"search_result"`

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.custom_tool_use"]`

      - `"agent.custom_tool_use"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.message"]`

      - `"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thinking"]`

      - `"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_use"]`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_result"]`

      - `"agent.mcp_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.tool_use"]`

      - `"agent.tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: Literal["agent.tool_result"]`

      - `"agent.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_message_received"]`

      - `"agent.thread_message_received"`

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: Literal["agent.thread_message_sent"]`

      - `"agent.thread_message_sent"`

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_context_compacted"]`

      - `"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

              - `"retrying"`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

              - `"exhausted"`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

              - `"terminal"`

        - `type: Literal["unknown_error"]`

          - `"unknown_error"`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_overloaded_error"]`

          - `"model_overloaded_error"`

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_rate_limited_error"]`

          - `"model_rate_limited_error"`

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_request_failed_error"]`

          - `"model_request_failed_error"`

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_connection_failed_error"]`

          - `"mcp_connection_failed_error"`

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_authentication_failed_error"]`

          - `"mcp_authentication_failed_error"`

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["billing_error"]`

          - `"billing_error"`

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["credential_host_unreachable_error"]`

          - `"credential_host_unreachable_error"`

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.error"]`

      - `"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_rescheduled"]`

      - `"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_running"]`

      - `"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

          - `"end_turn"`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: Literal["requires_action"]`

          - `"requires_action"`

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: Literal["retries_exhausted"]`

          - `"retries_exhausted"`

    - `type: Literal["session.status_idle"]`

      - `"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_terminated"]`

      - `"session.status_terminated"`

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

    - `type: Literal["session.thread_created"]`

      - `"session.thread_created"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_start"]`

      - `"span.outcome_evaluation_start"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: Literal["span.outcome_evaluation_end"]`

      - `"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

      - `input_tokens: int`

        Input tokens consumed by this request.

      - `output_tokens: int`

        Output tokens generated by this request.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_start"]`

      - `"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_end"]`

      - `"span.model_request_end"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_ongoing"]`

      - `"span.outcome_evaluation_ongoing"`

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.deleted"]`

      - `"session.deleted"`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

    - `type: Literal["session.thread_status_running"]`

      - `"session.thread_status_running"`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

    - `type: Literal["session.thread_status_idle"]`

      - `"session.thread_status_idle"`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

    - `type: Literal["session.thread_status_terminated"]`

      - `"session.thread_status_terminated"`

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_result"]`

      - `"user.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

    - `type: Literal["session.thread_status_rescheduled"]`

      - `"session.thread_status_rescheduled"`

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.updated"]`

      - `"session.updated"`

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: str`

      - `description: Optional[str]`

      - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

        - `name: str`

        - `type: Literal["url"]`

          - `"url"`

        - `url: str`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-5", 10 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

            - `"claude-sonnet-5"`

              High-performance model for coding and agents

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `"claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `"claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `"claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `"claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `str`

        - `effort: Optional[Effort]`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow: …`

            Low effort. Favors latency over reasoning depth.

            - `type: Literal["low"]`

              - `"low"`

          - `class BetaManagedAgentsEffortMedium: …`

            Medium effort. Balances latency and reasoning depth.

            - `type: Literal["medium"]`

              - `"medium"`

          - `class BetaManagedAgentsEffortHigh: …`

            High effort. Favors reasoning depth.

            - `type: Literal["high"]`

              - `"high"`

          - `class BetaManagedAgentsEffortXhigh: …`

            Extra-high effort. Not all models accept this level.

            - `type: Literal["xhigh"]`

              - `"xhigh"`

          - `class BetaManagedAgentsEffortMax: …`

            Maximum effort. Favors reasoning depth over latency.

            - `type: Literal["max"]`

              - `"max"`

        - `speed: Optional[Literal["standard", "fast"]]`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: List[BetaManagedAgentsSessionThreadAgent]`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `id: str`

          - `description: Optional[str]`

          - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

            - `name: str`

            - `type: Literal["url"]`

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `name: str`

          - `skills: List[Skill]`

            - `class BetaManagedAgentsAnthropicSkill: …`

              A resolved Anthropic-managed skill.

              - `skill_id: str`

              - `type: Literal["anthropic"]`

                - `"anthropic"`

              - `version: str`

            - `class BetaManagedAgentsCustomSkill: …`

              A resolved user-created custom skill.

              - `skill_id: str`

              - `type: Literal["custom"]`

                - `"custom"`

              - `version: str`

          - `system: Optional[str]`

          - `tools: List[Tool]`

            - `class BetaManagedAgentsAgentToolset20260401: …`

              - `configs: List[BetaManagedAgentsAgentToolConfig]`

                - `enabled: bool`

                - `name: Literal["bash", "edit", "read", 5 more]`

                  Built-in agent tool identifier.

                  - `"bash"`

                  - `"edit"`

                  - `"read"`

                  - `"write"`

                  - `"glob"`

                  - `"grep"`

                  - `"web_fetch"`

                  - `"web_search"`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                    - `type: Literal["always_allow"]`

                      - `"always_allow"`

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                    - `type: Literal["always_ask"]`

                      - `"always_ask"`

              - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `type: Literal["agent_toolset_20260401"]`

                - `"agent_toolset_20260401"`

            - `class BetaManagedAgentsMCPToolset: …`

              - `configs: List[BetaManagedAgentsMCPToolConfig]`

                - `enabled: bool`

                - `name: str`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: str`

              - `type: Literal["mcp_toolset"]`

                - `"mcp_toolset"`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                  - `"object"`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

              - `name: str`

              - `type: Literal["custom"]`

                - `"custom"`

          - `type: Literal["agent"]`

            - `"agent"`

          - `version: int`

        - `type: Literal["coordinator"]`

          - `"coordinator"`

      - `name: str`

      - `skills: List[Skill]`

        - `class BetaManagedAgentsAnthropicSkill: …`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `type: Literal["agent"]`

        - `"agent"`

      - `version: int`

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.sessions.threads.events.list(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
page = page.data[0]
print(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "next_page"
}
```

## Stream Session Thread Events

`beta.sessions.threads.events.stream(strthread_id, EventStreamParams**kwargs)  -> BetaManagedAgentsStreamSessionThreadEvents`

**get** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

### Parameters

- `session_id: str`

- `thread_id: str`

- `event_deltas: Optional[List[BetaManagedAgentsDeltaType]]`

  When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

  - `"agent.message"`

  - `"agent.thinking"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `BetaManagedAgentsStreamSessionThreadEvents`

  Server-sent event in a single thread's stream.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: str`

      Unique identifier for this event.

    - `type: Literal["user.interrupt"]`

      - `"user.interrupt"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_confirmation"]`

      - `"user.tool_confirmation"`

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.custom_tool_result"]`

      - `"user.custom_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `source: str`

          The URL source of the search result.

        - `title: str`

          The title of the search result.

        - `type: Literal["search_result"]`

          - `"search_result"`

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.custom_tool_use"]`

      - `"agent.custom_tool_use"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.message"]`

      - `"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thinking"]`

      - `"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_use"]`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_result"]`

      - `"agent.mcp_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.tool_use"]`

      - `"agent.tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: Literal["agent.tool_result"]`

      - `"agent.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_message_received"]`

      - `"agent.thread_message_received"`

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: Literal["agent.thread_message_sent"]`

      - `"agent.thread_message_sent"`

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_context_compacted"]`

      - `"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

              - `"retrying"`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

              - `"exhausted"`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

              - `"terminal"`

        - `type: Literal["unknown_error"]`

          - `"unknown_error"`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_overloaded_error"]`

          - `"model_overloaded_error"`

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_rate_limited_error"]`

          - `"model_rate_limited_error"`

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_request_failed_error"]`

          - `"model_request_failed_error"`

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_connection_failed_error"]`

          - `"mcp_connection_failed_error"`

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_authentication_failed_error"]`

          - `"mcp_authentication_failed_error"`

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["billing_error"]`

          - `"billing_error"`

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["credential_host_unreachable_error"]`

          - `"credential_host_unreachable_error"`

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.error"]`

      - `"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_rescheduled"]`

      - `"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_running"]`

      - `"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

          - `"end_turn"`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: Literal["requires_action"]`

          - `"requires_action"`

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: Literal["retries_exhausted"]`

          - `"retries_exhausted"`

    - `type: Literal["session.status_idle"]`

      - `"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_terminated"]`

      - `"session.status_terminated"`

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

    - `type: Literal["session.thread_created"]`

      - `"session.thread_created"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_start"]`

      - `"span.outcome_evaluation_start"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: Literal["span.outcome_evaluation_end"]`

      - `"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

      - `input_tokens: int`

        Input tokens consumed by this request.

      - `output_tokens: int`

        Output tokens generated by this request.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_start"]`

      - `"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_end"]`

      - `"span.model_request_end"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_ongoing"]`

      - `"span.outcome_evaluation_ongoing"`

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.deleted"]`

      - `"session.deleted"`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

    - `type: Literal["session.thread_status_running"]`

      - `"session.thread_status_running"`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

    - `type: Literal["session.thread_status_idle"]`

      - `"session.thread_status_idle"`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

    - `type: Literal["session.thread_status_terminated"]`

      - `"session.thread_status_terminated"`

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_result"]`

      - `"user.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

    - `type: Literal["session.thread_status_rescheduled"]`

      - `"session.thread_status_rescheduled"`

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.updated"]`

      - `"session.updated"`

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: str`

      - `description: Optional[str]`

      - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

        - `name: str`

        - `type: Literal["url"]`

          - `"url"`

        - `url: str`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-5", 10 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

            - `"claude-sonnet-5"`

              High-performance model for coding and agents

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `"claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `"claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `"claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `"claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `str`

        - `effort: Optional[Effort]`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow: …`

            Low effort. Favors latency over reasoning depth.

            - `type: Literal["low"]`

              - `"low"`

          - `class BetaManagedAgentsEffortMedium: …`

            Medium effort. Balances latency and reasoning depth.

            - `type: Literal["medium"]`

              - `"medium"`

          - `class BetaManagedAgentsEffortHigh: …`

            High effort. Favors reasoning depth.

            - `type: Literal["high"]`

              - `"high"`

          - `class BetaManagedAgentsEffortXhigh: …`

            Extra-high effort. Not all models accept this level.

            - `type: Literal["xhigh"]`

              - `"xhigh"`

          - `class BetaManagedAgentsEffortMax: …`

            Maximum effort. Favors reasoning depth over latency.

            - `type: Literal["max"]`

              - `"max"`

        - `speed: Optional[Literal["standard", "fast"]]`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: List[BetaManagedAgentsSessionThreadAgent]`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `id: str`

          - `description: Optional[str]`

          - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

            - `name: str`

            - `type: Literal["url"]`

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `name: str`

          - `skills: List[Skill]`

            - `class BetaManagedAgentsAnthropicSkill: …`

              A resolved Anthropic-managed skill.

              - `skill_id: str`

              - `type: Literal["anthropic"]`

                - `"anthropic"`

              - `version: str`

            - `class BetaManagedAgentsCustomSkill: …`

              A resolved user-created custom skill.

              - `skill_id: str`

              - `type: Literal["custom"]`

                - `"custom"`

              - `version: str`

          - `system: Optional[str]`

          - `tools: List[Tool]`

            - `class BetaManagedAgentsAgentToolset20260401: …`

              - `configs: List[BetaManagedAgentsAgentToolConfig]`

                - `enabled: bool`

                - `name: Literal["bash", "edit", "read", 5 more]`

                  Built-in agent tool identifier.

                  - `"bash"`

                  - `"edit"`

                  - `"read"`

                  - `"write"`

                  - `"glob"`

                  - `"grep"`

                  - `"web_fetch"`

                  - `"web_search"`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                    - `type: Literal["always_allow"]`

                      - `"always_allow"`

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                    - `type: Literal["always_ask"]`

                      - `"always_ask"`

              - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `type: Literal["agent_toolset_20260401"]`

                - `"agent_toolset_20260401"`

            - `class BetaManagedAgentsMCPToolset: …`

              - `configs: List[BetaManagedAgentsMCPToolConfig]`

                - `enabled: bool`

                - `name: str`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: str`

              - `type: Literal["mcp_toolset"]`

                - `"mcp_toolset"`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                  - `"object"`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

              - `name: str`

              - `type: Literal["custom"]`

                - `"custom"`

          - `type: Literal["agent"]`

            - `"agent"`

          - `version: int`

        - `type: Literal["coordinator"]`

          - `"coordinator"`

      - `name: str`

      - `skills: List[Skill]`

        - `class BetaManagedAgentsAnthropicSkill: …`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `type: Literal["agent"]`

        - `"agent"`

      - `version: int`

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent: …`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview: …`

        - `id: str`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: Literal["agent.message"]`

          - `"agent.message"`

      - `class BetaManagedAgentsAgentThinkingPreview: …`

        - `id: str`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: Literal["agent.thinking"]`

          - `"agent.thinking"`

    - `type: Literal["event_start"]`

      - `"event_start"`

  - `class BetaManagedAgentsDeltaEvent: …`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: Literal["content_delta"]`

        - `"content_delta"`

      - `index: Optional[int]`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `event_id: str`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: Literal["event_delta"]`

      - `"event_delta"`

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
for event in client.beta.sessions.threads.events.stream(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
):
  print(event)
```

#### Response

```json
{
  "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```

# Deployments

## Create Deployment

`beta.deployments.create(DeploymentCreateParams**kwargs)  -> BetaManagedAgentsDeployment`

**post** `/v1/deployments`

Create Deployment

### Parameters

- `agent: Agent`

  Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

  - `str`

  - `class BetaManagedAgentsAgentParams: …`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `id: str`

      The `agent` ID.

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: Optional[int]`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

- `environment_id: str`

  ID of the `environment` defining the container configuration for sessions created from this deployment.

- `initial_events: Iterable[BetaManagedAgentsDeploymentInitialEventParams]`

  Events to send to each session immediately after creation. At least 1, maximum 50.

  - `class BetaManagedAgentsUserMessageEventParams: …`

    Parameters for sending a user message to the session.

    - `content: Iterable[Content]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

  - `class BetaManagedAgentsUserDefineOutcomeEventParams: …`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: str`

      What the agent should produce. This is the task specification.

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubricParams: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

    - `max_iterations: Optional[int]`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsSystemMessageEventParams: …`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

- `name: str`

  Human-readable name for the deployment.

- `description: Optional[str]`

  Description of what the deployment does.

- `metadata: Optional[Dict[str, str]]`

  Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `resources: Optional[Iterable[Resource]]`

  Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

  - `class BetaManagedAgentsGitHubRepositoryResourceParams: …`

    Mount a GitHub repository into the session's container.

    - `authorization_token: str`

      GitHub authorization token used to clone the repository.

    - `type: Literal["github_repository"]`

      - `"github_repository"`

    - `url: str`

      Github URL of the repository

    - `checkout: Optional[Checkout]`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `class BetaManagedAgentsBranchCheckout: …`

        - `name: str`

          Branch name to check out.

        - `type: Literal["branch"]`

          - `"branch"`

      - `class BetaManagedAgentsCommitCheckout: …`

        - `sha: str`

          Full commit SHA to check out.

        - `type: Literal["commit"]`

          - `"commit"`

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `class BetaManagedAgentsFileResourceParams: …`

    Mount a file uploaded via the Files API into the session.

    - `file_id: str`

      ID of a previously uploaded file.

    - `type: Literal["file"]`

      - `"file"`

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `class BetaManagedAgentsMemoryStoreResourceParam: …`

    Parameters for attaching a memory store to an agent session.

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: Literal["memory_store"]`

      - `"memory_store"`

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

- `schedule: Optional[BetaManagedAgentsScheduleParams]`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: str`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `type: Literal["cron"]`

    - `"cron"`

- `vault_ids: Optional[Sequence[str]]`

  Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaManagedAgentsDeployment: …`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

      A user message sent to the session.

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason: …`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

    - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

            - `"environment_archived_error"`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

            - `"agent_archived_error"`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

            - `"environment_not_found_error"`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

            - `"vault_not_found_error"`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

            - `"file_not_found_error"`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

            - `"session_resource_not_found_error"`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

            - `"workspace_archived_error"`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

            - `"organization_disabled_error"`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

            - `"memory_store_archived_error"`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

            - `"skill_not_found_error"`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

            - `"vault_archived_error"`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

            - `"unknown_error"`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

            - `"self_hosted_resources_unsupported_error"`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

            - `"mcp_egress_blocked_error"`

      - `type: Literal["error"]`

        - `"error"`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig: …`

      A file mounted into each session's container.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: Literal["memory_store"]`

        - `"memory_store"`

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: Literal["cron"]`

      - `"cron"`

    - `last_run_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: Literal["deployment"]`

    - `"deployment"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.create(
    agent="string",
    environment_id="x",
    initial_events=[{
        "content": [{
            "text": "Where is my order #1234?",
            "type": "text",
        }],
        "type": "user.message",
    }],
    name="x",
)
print(beta_managed_agents_deployment.id)
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## List Deployments

`beta.deployments.list(DeploymentListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsDeployment]`

**get** `/v1/deployments`

List Deployments

### Parameters

- `agent_id: Optional[str]`

  Filter by agent ID.

- `created_at_gte: Optional[Union[str, datetime]]`

  Return deployments created at or after this time (inclusive).

- `created_at_lte: Optional[Union[str, datetime]]`

  Return deployments created at or before this time (inclusive).

- `include_archived: Optional[bool]`

  When true, includes archived deployments. Default: false (exclude archived).

- `limit: Optional[int]`

  Maximum results per page. Default 20, maximum 100.

- `page: Optional[str]`

  Opaque pagination cursor.

- `status: Optional[BetaManagedAgentsDeploymentStatus]`

  Filter by status: active or paused. Omit for both. To include archived deployments, use include_archived instead; the two cannot be combined.

  - `"active"`

  - `"paused"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaManagedAgentsDeployment: …`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

      A user message sent to the session.

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason: …`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

    - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

            - `"environment_archived_error"`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

            - `"agent_archived_error"`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

            - `"environment_not_found_error"`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

            - `"vault_not_found_error"`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

            - `"file_not_found_error"`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

            - `"session_resource_not_found_error"`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

            - `"workspace_archived_error"`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

            - `"organization_disabled_error"`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

            - `"memory_store_archived_error"`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

            - `"skill_not_found_error"`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

            - `"vault_archived_error"`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

            - `"unknown_error"`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

            - `"self_hosted_resources_unsupported_error"`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

            - `"mcp_egress_blocked_error"`

      - `type: Literal["error"]`

        - `"error"`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig: …`

      A file mounted into each session's container.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: Literal["memory_store"]`

        - `"memory_store"`

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: Literal["cron"]`

      - `"cron"`

    - `last_run_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: Literal["deployment"]`

    - `"deployment"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.deployments.list()
page = page.data[0]
print(page.id)
```

#### Response

```json
{
  "data": [
    {
      "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
      "agent": {
        "id": "agent_011CZkYpogX7uDKUyvBTophP",
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "description": "Compiles yesterday's orders into a report every weekday morning.",
      "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "initial_events": [
        {
          "content": [
            {
              "text": "Compile yesterday's orders into report.md.",
              "type": "text"
            }
          ],
          "type": "user.message"
        }
      ],
      "metadata": {},
      "name": "Daily order report",
      "paused_reason": {
        "type": "manual"
      },
      "resources": [
        {
          "type": "github_repository",
          "url": "url",
          "checkout": {
            "name": "main",
            "type": "branch"
          },
          "mount_path": "mount_path"
        }
      ],
      "schedule": {
        "expression": "0 9 * * 1-5",
        "timezone": "America/Los_Angeles",
        "type": "cron",
        "last_run_at": "2026-03-16T16:00:09Z",
        "upcoming_runs_at": [
          "2026-03-17T16:00:00Z",
          "2026-03-18T16:00:00Z"
        ]
      },
      "status": "active",
      "type": "deployment",
      "updated_at": "2026-03-15T10:00:00Z",
      "vault_ids": [
        "vlt_011CZkZDLs7fYzm1hXNPeRjv"
      ]
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Deployment

`beta.deployments.retrieve(strdeployment_id, DeploymentRetrieveParams**kwargs)  -> BetaManagedAgentsDeployment`

**get** `/v1/deployments/{deployment_id}`

Get Deployment

### Parameters

- `deployment_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaManagedAgentsDeployment: …`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

      A user message sent to the session.

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason: …`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

    - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

            - `"environment_archived_error"`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

            - `"agent_archived_error"`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

            - `"environment_not_found_error"`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

            - `"vault_not_found_error"`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

            - `"file_not_found_error"`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

            - `"session_resource_not_found_error"`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

            - `"workspace_archived_error"`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

            - `"organization_disabled_error"`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

            - `"memory_store_archived_error"`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

            - `"skill_not_found_error"`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

            - `"vault_archived_error"`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

            - `"unknown_error"`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

            - `"self_hosted_resources_unsupported_error"`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

            - `"mcp_egress_blocked_error"`

      - `type: Literal["error"]`

        - `"error"`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig: …`

      A file mounted into each session's container.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: Literal["memory_store"]`

        - `"memory_store"`

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: Literal["cron"]`

      - `"cron"`

    - `last_run_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: Literal["deployment"]`

    - `"deployment"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.retrieve(
    deployment_id="depl_011CZkZcDH3vPqd7xnEfwTai",
)
print(beta_managed_agents_deployment.id)
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Update Deployment

`beta.deployments.update(strdeployment_id, DeploymentUpdateParams**kwargs)  -> BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}`

Update Deployment

### Parameters

- `deployment_id: str`

- `agent: Optional[Agent]`

  Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

  - `str`

  - `class BetaManagedAgentsAgentParams: …`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `id: str`

      The `agent` ID.

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: Optional[int]`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

- `description: Optional[str]`

  Description. Omit to preserve; send empty string or null to clear.

- `environment_id: Optional[str]`

  ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

- `initial_events: Optional[Iterable[BetaManagedAgentsDeploymentInitialEventParams]]`

  Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

  - `class BetaManagedAgentsUserMessageEventParams: …`

    Parameters for sending a user message to the session.

    - `content: Iterable[Content]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

  - `class BetaManagedAgentsUserDefineOutcomeEventParams: …`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: str`

      What the agent should produce. This is the task specification.

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubricParams: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

    - `max_iterations: Optional[int]`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsSystemMessageEventParams: …`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

- `metadata: Optional[Dict[str, Optional[str]]]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `name: Optional[str]`

  Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

- `resources: Optional[Iterable[Resource]]`

  Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

  - `class BetaManagedAgentsGitHubRepositoryResourceParams: …`

    Mount a GitHub repository into the session's container.

    - `authorization_token: str`

      GitHub authorization token used to clone the repository.

    - `type: Literal["github_repository"]`

      - `"github_repository"`

    - `url: str`

      Github URL of the repository

    - `checkout: Optional[Checkout]`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `class BetaManagedAgentsBranchCheckout: …`

        - `name: str`

          Branch name to check out.

        - `type: Literal["branch"]`

          - `"branch"`

      - `class BetaManagedAgentsCommitCheckout: …`

        - `sha: str`

          Full commit SHA to check out.

        - `type: Literal["commit"]`

          - `"commit"`

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `class BetaManagedAgentsFileResourceParams: …`

    Mount a file uploaded via the Files API into the session.

    - `file_id: str`

      ID of a previously uploaded file.

    - `type: Literal["file"]`

      - `"file"`

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `class BetaManagedAgentsMemoryStoreResourceParam: …`

    Parameters for attaching a memory store to an agent session.

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: Literal["memory_store"]`

      - `"memory_store"`

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

- `schedule: Optional[BetaManagedAgentsScheduleParams]`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: str`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `type: Literal["cron"]`

    - `"cron"`

- `vault_ids: Optional[Sequence[str]]`

  Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaManagedAgentsDeployment: …`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

      A user message sent to the session.

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason: …`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

    - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

            - `"environment_archived_error"`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

            - `"agent_archived_error"`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

            - `"environment_not_found_error"`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

            - `"vault_not_found_error"`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

            - `"file_not_found_error"`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

            - `"session_resource_not_found_error"`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

            - `"workspace_archived_error"`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

            - `"organization_disabled_error"`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

            - `"memory_store_archived_error"`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

            - `"skill_not_found_error"`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

            - `"vault_archived_error"`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

            - `"unknown_error"`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

            - `"self_hosted_resources_unsupported_error"`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

            - `"mcp_egress_blocked_error"`

      - `type: Literal["error"]`

        - `"error"`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig: …`

      A file mounted into each session's container.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: Literal["memory_store"]`

        - `"memory_store"`

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: Literal["cron"]`

      - `"cron"`

    - `last_run_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: Literal["deployment"]`

    - `"deployment"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.update(
    deployment_id="depl_011CZkZcDH3vPqd7xnEfwTai",
)
print(beta_managed_agents_deployment.id)
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Archive Deployment

`beta.deployments.archive(strdeployment_id, DeploymentArchiveParams**kwargs)  -> BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}/archive`

Archive Deployment

### Parameters

- `deployment_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaManagedAgentsDeployment: …`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

      A user message sent to the session.

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason: …`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

    - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

            - `"environment_archived_error"`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

            - `"agent_archived_error"`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

            - `"environment_not_found_error"`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

            - `"vault_not_found_error"`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

            - `"file_not_found_error"`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

            - `"session_resource_not_found_error"`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

            - `"workspace_archived_error"`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

            - `"organization_disabled_error"`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

            - `"memory_store_archived_error"`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

            - `"skill_not_found_error"`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

            - `"vault_archived_error"`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

            - `"unknown_error"`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

            - `"self_hosted_resources_unsupported_error"`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

            - `"mcp_egress_blocked_error"`

      - `type: Literal["error"]`

        - `"error"`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig: …`

      A file mounted into each session's container.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: Literal["memory_store"]`

        - `"memory_store"`

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: Literal["cron"]`

      - `"cron"`

    - `last_run_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: Literal["deployment"]`

    - `"deployment"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.archive(
    deployment_id="depl_011CZkZcDH3vPqd7xnEfwTai",
)
print(beta_managed_agents_deployment.id)
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Run Deployment Now

`beta.deployments.run(strdeployment_id, DeploymentRunParams**kwargs)  -> BetaManagedAgentsDeploymentRun`

**post** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

### Parameters

- `deployment_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaManagedAgentsDeploymentRun: …`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: str`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `deployment_id: str`

    ID of the deployment that produced this run.

  - `error: Optional[Error]`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError: …`

      The deployment's environment was archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["environment_archived_error"]`

        - `"environment_archived_error"`

    - `class BetaManagedAgentsAgentArchivedRunError: …`

      The deployment's agent was archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["agent_archived_error"]`

        - `"agent_archived_error"`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError: …`

      The deployment's environment no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["environment_not_found_error"]`

        - `"environment_not_found_error"`

    - `class BetaManagedAgentsVaultNotFoundRunError: …`

      A vault referenced by the deployment no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["vault_not_found_error"]`

        - `"vault_not_found_error"`

    - `class BetaManagedAgentsVaultArchivedRunError: …`

      A vault referenced by the deployment is archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["vault_archived_error"]`

        - `"vault_archived_error"`

    - `class BetaManagedAgentsFileNotFoundRunError: …`

      A file resource referenced by the deployment no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["file_not_found_error"]`

        - `"file_not_found_error"`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError: …`

      A memory store referenced by the deployment is archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["memory_store_archived_error"]`

        - `"memory_store_archived_error"`

    - `class BetaManagedAgentsSkillNotFoundRunError: …`

      A skill referenced by the deployment's agent no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["skill_not_found_error"]`

        - `"skill_not_found_error"`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError: …`

      A referenced resource no longer exists and its kind was not reported.

      - `message: str`

        Human-readable error description.

      - `type: Literal["session_resource_not_found_error"]`

        - `"session_resource_not_found_error"`

    - `class BetaManagedAgentsWorkspaceArchivedRunError: …`

      The deployment's workspace was archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["workspace_archived_error"]`

        - `"workspace_archived_error"`

    - `class BetaManagedAgentsOrganizationDisabledRunError: …`

      The deployment's organization is disabled.

      - `message: str`

        Human-readable error description.

      - `type: Literal["organization_disabled_error"]`

        - `"organization_disabled_error"`

    - `class BetaManagedAgentsSessionRateLimitedRunError: …`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: str`

        Human-readable error description.

      - `type: Literal["session_rate_limited_error"]`

        - `"session_rate_limited_error"`

    - `class BetaManagedAgentsSessionCreationRejectedRunError: …`

      The session create request was rejected with a non-retryable validation error.

      - `message: str`

        Human-readable error description.

      - `type: Literal["session_creation_rejected_error"]`

        - `"session_creation_rejected_error"`

    - `class BetaManagedAgentsUnknownRunError: …`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: str`

        Human-readable error description.

      - `type: Literal["unknown_error"]`

        - `"unknown_error"`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError: …`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: str`

        Human-readable error description.

      - `type: Literal["self_hosted_resources_unsupported_error"]`

        - `"self_hosted_resources_unsupported_error"`

    - `class BetaManagedAgentsMCPEgressBlockedRunError: …`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: str`

        Human-readable error description.

      - `type: Literal["mcp_egress_blocked_error"]`

        - `"mcp_egress_blocked_error"`

  - `session_id: Optional[str]`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext: …`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: datetime`

        A timestamp in RFC 3339 format

      - `type: Literal["schedule"]`

        - `"schedule"`

    - `class BetaManagedAgentsManualTriggerContext: …`

      The run was started manually by creating a session directly against the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

  - `type: Literal["deployment_run"]`

    - `"deployment_run"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deployment_run = client.beta.deployments.run(
    deployment_id="depl_011CZkZcDH3vPqd7xnEfwTai",
)
print(beta_managed_agents_deployment_run.id)
```

#### Response

```json
{
  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "deployment_id": "deployment_id",
  "error": {
    "message": "message",
    "type": "environment_archived_error"
  },
  "session_id": "session_id",
  "trigger_context": {
    "scheduled_at": "2019-12-27T18:11:19.117Z",
    "type": "schedule"
  },
  "type": "deployment_run"
}
```

## Pause Deployment

`beta.deployments.pause(strdeployment_id, DeploymentPauseParams**kwargs)  -> BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}/pause`

Pause Deployment

### Parameters

- `deployment_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaManagedAgentsDeployment: …`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

      A user message sent to the session.

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason: …`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

    - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

            - `"environment_archived_error"`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

            - `"agent_archived_error"`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

            - `"environment_not_found_error"`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

            - `"vault_not_found_error"`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

            - `"file_not_found_error"`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

            - `"session_resource_not_found_error"`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

            - `"workspace_archived_error"`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

            - `"organization_disabled_error"`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

            - `"memory_store_archived_error"`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

            - `"skill_not_found_error"`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

            - `"vault_archived_error"`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

            - `"unknown_error"`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

            - `"self_hosted_resources_unsupported_error"`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

            - `"mcp_egress_blocked_error"`

      - `type: Literal["error"]`

        - `"error"`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig: …`

      A file mounted into each session's container.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: Literal["memory_store"]`

        - `"memory_store"`

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: Literal["cron"]`

      - `"cron"`

    - `last_run_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: Literal["deployment"]`

    - `"deployment"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.pause(
    deployment_id="depl_011CZkZcDH3vPqd7xnEfwTai",
)
print(beta_managed_agents_deployment.id)
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Unpause Deployment

`beta.deployments.unpause(strdeployment_id, DeploymentUnpauseParams**kwargs)  -> BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

### Parameters

- `deployment_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaManagedAgentsDeployment: …`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

      A user message sent to the session.

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason: …`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

    - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

            - `"environment_archived_error"`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

            - `"agent_archived_error"`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

            - `"environment_not_found_error"`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

            - `"vault_not_found_error"`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

            - `"file_not_found_error"`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

            - `"session_resource_not_found_error"`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

            - `"workspace_archived_error"`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

            - `"organization_disabled_error"`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

            - `"memory_store_archived_error"`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

            - `"skill_not_found_error"`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

            - `"vault_archived_error"`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

            - `"unknown_error"`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

            - `"self_hosted_resources_unsupported_error"`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

            - `"mcp_egress_blocked_error"`

      - `type: Literal["error"]`

        - `"error"`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig: …`

      A file mounted into each session's container.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: Literal["memory_store"]`

        - `"memory_store"`

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: Literal["cron"]`

      - `"cron"`

    - `last_run_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: Literal["deployment"]`

    - `"deployment"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.unpause(
    deployment_id="depl_011CZkZcDH3vPqd7xnEfwTai",
)
print(beta_managed_agents_deployment.id)
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Domain Types

### Beta Managed Agents Agent Archived Deployment Paused Reason Error

- `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

  The deployment's agent was archived.

  - `type: Literal["agent_archived_error"]`

    - `"agent_archived_error"`

### Beta Managed Agents Cron Schedule

- `class BetaManagedAgentsCronSchedule: …`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: str`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `type: Literal["cron"]`

    - `"cron"`

  - `last_run_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `upcoming_runs_at: Optional[List[datetime]]`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Cron Schedule Params

- `class BetaManagedAgentsCronScheduleParams: …`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: str`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `type: Literal["cron"]`

    - `"cron"`

### Beta Managed Agents Deployment

- `class BetaManagedAgentsDeployment: …`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

      A user message sent to the session.

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason: …`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

    - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

            - `"environment_archived_error"`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

            - `"agent_archived_error"`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

            - `"environment_not_found_error"`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

            - `"vault_not_found_error"`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

            - `"file_not_found_error"`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

            - `"session_resource_not_found_error"`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

            - `"workspace_archived_error"`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

            - `"organization_disabled_error"`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

            - `"memory_store_archived_error"`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

            - `"skill_not_found_error"`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

            - `"vault_archived_error"`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

            - `"unknown_error"`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

            - `"self_hosted_resources_unsupported_error"`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

            - `"mcp_egress_blocked_error"`

      - `type: Literal["error"]`

        - `"error"`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig: …`

      A file mounted into each session's container.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: Literal["memory_store"]`

        - `"memory_store"`

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: Literal["cron"]`

      - `"cron"`

    - `last_run_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: Literal["deployment"]`

    - `"deployment"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Beta Managed Agents Deployment Initial Event

- `BetaManagedAgentsDeploymentInitialEvent`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

    A user message sent to the session.

    - `content: List[Content]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

  - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

    An outcome the agent should work toward. The agent begins work on receipt.

    - `description: str`

      What the agent should produce. This is the task specification.

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

    - `max_iterations: Optional[int]`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

### Beta Managed Agents Deployment Initial Event Params

- `BetaManagedAgentsDeploymentInitialEventParams`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `class BetaManagedAgentsUserMessageEventParams: …`

    Parameters for sending a user message to the session.

    - `content: Iterable[Content]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

  - `class BetaManagedAgentsUserDefineOutcomeEventParams: …`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: str`

      What the agent should produce. This is the task specification.

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubricParams: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

    - `max_iterations: Optional[int]`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsSystemMessageEventParams: …`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

### Beta Managed Agents Deployment Paused Reason

- `BetaManagedAgentsDeploymentPausedReason`

  Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `class BetaManagedAgentsManualDeploymentPausedReason: …`

    The caller invoked the pause endpoint on the deployment.

    - `type: Literal["manual"]`

      - `"manual"`

  - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

    A scheduled fire recorded a failed run whose error auto-pauses the deployment.

    - `error: BetaManagedAgentsDeploymentPausedReasonError`

      The error that triggered an auto-pause. Matches the failed run's `error.type`.

      - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

        The deployment's environment was archived.

        - `type: Literal["environment_archived_error"]`

          - `"environment_archived_error"`

      - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

        The deployment's agent was archived.

        - `type: Literal["agent_archived_error"]`

          - `"agent_archived_error"`

      - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

        The deployment's environment no longer exists.

        - `type: Literal["environment_not_found_error"]`

          - `"environment_not_found_error"`

      - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

        A vault referenced by the deployment no longer exists.

        - `type: Literal["vault_not_found_error"]`

          - `"vault_not_found_error"`

      - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

        A file resource referenced by the deployment no longer exists.

        - `type: Literal["file_not_found_error"]`

          - `"file_not_found_error"`

      - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

        A referenced resource no longer exists and its kind was not reported.

        - `type: Literal["session_resource_not_found_error"]`

          - `"session_resource_not_found_error"`

      - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

        The deployment's workspace was archived.

        - `type: Literal["workspace_archived_error"]`

          - `"workspace_archived_error"`

      - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

        The deployment's organization is disabled.

        - `type: Literal["organization_disabled_error"]`

          - `"organization_disabled_error"`

      - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

        A memory store referenced by the deployment is archived.

        - `type: Literal["memory_store_archived_error"]`

          - `"memory_store_archived_error"`

      - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

        A skill referenced by the deployment's agent no longer exists.

        - `type: Literal["skill_not_found_error"]`

          - `"skill_not_found_error"`

      - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

        A vault referenced by the deployment is archived.

        - `type: Literal["vault_archived_error"]`

          - `"vault_archived_error"`

      - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

        An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

        - `type: Literal["unknown_error"]`

          - `"unknown_error"`

      - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

        The deployment configures resources, but its environment is self-hosted and cannot mount them.

        - `type: Literal["self_hosted_resources_unsupported_error"]`

          - `"self_hosted_resources_unsupported_error"`

      - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

        An MCP server host used by the deployment's agent is blocked by the environment's network policy.

        - `type: Literal["mcp_egress_blocked_error"]`

          - `"mcp_egress_blocked_error"`

    - `type: Literal["error"]`

      - `"error"`

### Beta Managed Agents Deployment Paused Reason Error

- `BetaManagedAgentsDeploymentPausedReasonError`

  The error that triggered an auto-pause. Matches the failed run's `error.type`.

  - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

    The deployment's environment was archived.

    - `type: Literal["environment_archived_error"]`

      - `"environment_archived_error"`

  - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

    The deployment's agent was archived.

    - `type: Literal["agent_archived_error"]`

      - `"agent_archived_error"`

  - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

    The deployment's environment no longer exists.

    - `type: Literal["environment_not_found_error"]`

      - `"environment_not_found_error"`

  - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

    A vault referenced by the deployment no longer exists.

    - `type: Literal["vault_not_found_error"]`

      - `"vault_not_found_error"`

  - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

    A file resource referenced by the deployment no longer exists.

    - `type: Literal["file_not_found_error"]`

      - `"file_not_found_error"`

  - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

    A referenced resource no longer exists and its kind was not reported.

    - `type: Literal["session_resource_not_found_error"]`

      - `"session_resource_not_found_error"`

  - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

    The deployment's workspace was archived.

    - `type: Literal["workspace_archived_error"]`

      - `"workspace_archived_error"`

  - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

    The deployment's organization is disabled.

    - `type: Literal["organization_disabled_error"]`

      - `"organization_disabled_error"`

  - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

    A memory store referenced by the deployment is archived.

    - `type: Literal["memory_store_archived_error"]`

      - `"memory_store_archived_error"`

  - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

    A skill referenced by the deployment's agent no longer exists.

    - `type: Literal["skill_not_found_error"]`

      - `"skill_not_found_error"`

  - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

    A vault referenced by the deployment is archived.

    - `type: Literal["vault_archived_error"]`

      - `"vault_archived_error"`

  - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

    An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

    - `type: Literal["unknown_error"]`

      - `"unknown_error"`

  - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

    The deployment configures resources, but its environment is self-hosted and cannot mount them.

    - `type: Literal["self_hosted_resources_unsupported_error"]`

      - `"self_hosted_resources_unsupported_error"`

  - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

    An MCP server host used by the deployment's agent is blocked by the environment's network policy.

    - `type: Literal["mcp_egress_blocked_error"]`

      - `"mcp_egress_blocked_error"`

### Beta Managed Agents Deployment Status

- `Literal["active", "paused"]`

  Lifecycle status of a deployment.

  - `"active"`

  - `"paused"`

### Beta Managed Agents Deployment System Message Event

- `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

  Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

  - `content: List[BetaManagedAgentsSystemContentBlock]`

    System content blocks to append. Text-only.

    - `text: str`

      The text content.

    - `type: Literal["text"]`

      - `"text"`

  - `type: Literal["system.message"]`

    - `"system.message"`

### Beta Managed Agents Deployment User Define Outcome Event

- `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

  An outcome the agent should work toward. The agent begins work on receipt.

  - `description: str`

    What the agent should produce. This is the task specification.

  - `rubric: Rubric`

    Rubric for grading the quality of an outcome.

    - `class BetaManagedAgentsFileRubric: …`

      Rubric referenced by a file uploaded via the Files API.

      - `file_id: str`

        ID of the rubric file.

      - `type: Literal["file"]`

        - `"file"`

    - `class BetaManagedAgentsTextRubric: …`

      Rubric content provided inline as text.

      - `content: str`

        Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `type: Literal["text"]`

        - `"text"`

  - `type: Literal["user.define_outcome"]`

    - `"user.define_outcome"`

  - `max_iterations: Optional[int]`

    Eval→revision cycles before giving up. Default 3, max 20.

### Beta Managed Agents Deployment User Message Event

- `class BetaManagedAgentsDeploymentUserMessageEvent: …`

  A user message sent to the session.

  - `content: List[Content]`

    Array of content blocks for the user message.

    - `class BetaManagedAgentsTextBlock: …`

      Regular text content.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `class BetaManagedAgentsImageBlock: …`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource: …`

          Base64-encoded image data.

          - `data: str`

            Base64-encoded image data.

          - `media_type: str`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsURLImageSource: …`

          Image referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource: …`

          Image referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["image"]`

        - `"image"`

    - `class BetaManagedAgentsDocumentBlock: …`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource: …`

          Base64-encoded document data.

          - `data: str`

            Base64-encoded document data.

          - `media_type: str`

            MIME type of the document (e.g., "application/pdf").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsPlainTextDocumentSource: …`

          Plain text document content.

          - `data: str`

            The plain text content.

          - `media_type: Literal["text/plain"]`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsURLDocumentSource: …`

          Document referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource: …`

          Document referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["document"]`

        - `"document"`

      - `context: Optional[str]`

        Additional context about the document for the model.

      - `title: Optional[str]`

        The title of the document.

  - `type: Literal["user.message"]`

    - `"user.message"`

### Beta Managed Agents Environment Archived Deployment Paused Reason Error

- `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

  The deployment's environment was archived.

  - `type: Literal["environment_archived_error"]`

    - `"environment_archived_error"`

### Beta Managed Agents Environment Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

  The deployment's environment no longer exists.

  - `type: Literal["environment_not_found_error"]`

    - `"environment_not_found_error"`

### Beta Managed Agents Error Deployment Paused Reason

- `class BetaManagedAgentsErrorDeploymentPausedReason: …`

  A scheduled fire recorded a failed run whose error auto-pauses the deployment.

  - `error: BetaManagedAgentsDeploymentPausedReasonError`

    The error that triggered an auto-pause. Matches the failed run's `error.type`.

    - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

      The deployment's environment was archived.

      - `type: Literal["environment_archived_error"]`

        - `"environment_archived_error"`

    - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

      The deployment's agent was archived.

      - `type: Literal["agent_archived_error"]`

        - `"agent_archived_error"`

    - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

      The deployment's environment no longer exists.

      - `type: Literal["environment_not_found_error"]`

        - `"environment_not_found_error"`

    - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

      A vault referenced by the deployment no longer exists.

      - `type: Literal["vault_not_found_error"]`

        - `"vault_not_found_error"`

    - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

      A file resource referenced by the deployment no longer exists.

      - `type: Literal["file_not_found_error"]`

        - `"file_not_found_error"`

    - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

      A referenced resource no longer exists and its kind was not reported.

      - `type: Literal["session_resource_not_found_error"]`

        - `"session_resource_not_found_error"`

    - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

      The deployment's workspace was archived.

      - `type: Literal["workspace_archived_error"]`

        - `"workspace_archived_error"`

    - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

      The deployment's organization is disabled.

      - `type: Literal["organization_disabled_error"]`

        - `"organization_disabled_error"`

    - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

      A memory store referenced by the deployment is archived.

      - `type: Literal["memory_store_archived_error"]`

        - `"memory_store_archived_error"`

    - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

      A skill referenced by the deployment's agent no longer exists.

      - `type: Literal["skill_not_found_error"]`

        - `"skill_not_found_error"`

    - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

      A vault referenced by the deployment is archived.

      - `type: Literal["vault_archived_error"]`

        - `"vault_archived_error"`

    - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

      An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

      - `type: Literal["unknown_error"]`

        - `"unknown_error"`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `type: Literal["self_hosted_resources_unsupported_error"]`

        - `"self_hosted_resources_unsupported_error"`

    - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `type: Literal["mcp_egress_blocked_error"]`

        - `"mcp_egress_blocked_error"`

  - `type: Literal["error"]`

    - `"error"`

### Beta Managed Agents File Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

  A file resource referenced by the deployment no longer exists.

  - `type: Literal["file_not_found_error"]`

    - `"file_not_found_error"`

### Beta Managed Agents File Resource Config

- `class BetaManagedAgentsFileResourceConfig: …`

  A file mounted into each session's container.

  - `file_id: str`

    ID of a previously uploaded file.

  - `type: Literal["file"]`

    - `"file"`

  - `mount_path: Optional[str]`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Config

- `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

  A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

  - `type: Literal["github_repository"]`

    - `"github_repository"`

  - `url: str`

    Github URL of the repository

  - `checkout: Optional[Checkout]`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `class BetaManagedAgentsBranchCheckout: …`

      - `name: str`

        Branch name to check out.

      - `type: Literal["branch"]`

        - `"branch"`

    - `class BetaManagedAgentsCommitCheckout: …`

      - `sha: str`

        Full commit SHA to check out.

      - `type: Literal["commit"]`

        - `"commit"`

  - `mount_path: Optional[str]`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Manual Deployment Paused Reason

- `class BetaManagedAgentsManualDeploymentPausedReason: …`

  The caller invoked the pause endpoint on the deployment.

  - `type: Literal["manual"]`

    - `"manual"`

### Beta Managed Agents MCP Egress Blocked Deployment Paused Reason Error

- `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `type: Literal["mcp_egress_blocked_error"]`

    - `"mcp_egress_blocked_error"`

### Beta Managed Agents Memory Store Archived Deployment Paused Reason Error

- `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

  A memory store referenced by the deployment is archived.

  - `type: Literal["memory_store_archived_error"]`

    - `"memory_store_archived_error"`

### Beta Managed Agents Memory Store Resource Config

- `class BetaManagedAgentsMemoryStoreResourceConfig: …`

  A memory store attached to each session created from this deployment.

  - `memory_store_id: str`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `type: Literal["memory_store"]`

    - `"memory_store"`

  - `access: Optional[Literal["read_write", "read_only"]]`

    Access mode for an attached memory store.

    - `"read_write"`

    - `"read_only"`

  - `instructions: Optional[str]`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Organization Disabled Deployment Paused Reason Error

- `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

  The deployment's organization is disabled.

  - `type: Literal["organization_disabled_error"]`

    - `"organization_disabled_error"`

### Beta Managed Agents Schedule

- `class BetaManagedAgentsSchedule: …`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: str`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `type: Literal["cron"]`

    - `"cron"`

  - `last_run_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `upcoming_runs_at: Optional[List[datetime]]`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Schedule Params

- `class BetaManagedAgentsScheduleParams: …`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: str`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `type: Literal["cron"]`

    - `"cron"`

### Beta Managed Agents Self Hosted Resources Unsupported Deployment Paused Reason Error

- `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `type: Literal["self_hosted_resources_unsupported_error"]`

    - `"self_hosted_resources_unsupported_error"`

### Beta Managed Agents Session Resource Config

- `BetaManagedAgentsSessionResourceConfig`

  A configured session resource. Echoes the input minus write-only credentials.

  - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

    A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

    - `type: Literal["github_repository"]`

      - `"github_repository"`

    - `url: str`

      Github URL of the repository

    - `checkout: Optional[Checkout]`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `class BetaManagedAgentsBranchCheckout: …`

        - `name: str`

          Branch name to check out.

        - `type: Literal["branch"]`

          - `"branch"`

      - `class BetaManagedAgentsCommitCheckout: …`

        - `sha: str`

          Full commit SHA to check out.

        - `type: Literal["commit"]`

          - `"commit"`

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `class BetaManagedAgentsFileResourceConfig: …`

    A file mounted into each session's container.

    - `file_id: str`

      ID of a previously uploaded file.

    - `type: Literal["file"]`

      - `"file"`

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

    A memory store attached to each session created from this deployment.

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: Literal["memory_store"]`

      - `"memory_store"`

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Session Resource Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

  A referenced resource no longer exists and its kind was not reported.

  - `type: Literal["session_resource_not_found_error"]`

    - `"session_resource_not_found_error"`

### Beta Managed Agents Skill Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

  A skill referenced by the deployment's agent no longer exists.

  - `type: Literal["skill_not_found_error"]`

    - `"skill_not_found_error"`

### Beta Managed Agents Unknown Deployment Paused Reason Error

- `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

  An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

  - `type: Literal["unknown_error"]`

    - `"unknown_error"`

### Beta Managed Agents Vault Archived Deployment Paused Reason Error

- `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

  A vault referenced by the deployment is archived.

  - `type: Literal["vault_archived_error"]`

    - `"vault_archived_error"`

### Beta Managed Agents Vault Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

  A vault referenced by the deployment no longer exists.

  - `type: Literal["vault_not_found_error"]`

    - `"vault_not_found_error"`

### Beta Managed Agents Workspace Archived Deployment Paused Reason Error

- `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

  The deployment's workspace was archived.

  - `type: Literal["workspace_archived_error"]`

    - `"workspace_archived_error"`

# Deployment Runs

## List Deployment Runs

`beta.deployment_runs.list(DeploymentRunListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsDeploymentRun]`

**get** `/v1/deployment_runs`

List Deployment Runs

### Parameters

- `created_at_gt: Optional[Union[str, datetime]]`

  Return runs created strictly after this time (exclusive).

- `created_at_gte: Optional[Union[str, datetime]]`

  Return runs created at or after this time (inclusive).

- `created_at_lt: Optional[Union[str, datetime]]`

  Return runs created strictly before this time (exclusive).

- `created_at_lte: Optional[Union[str, datetime]]`

  Return runs created at or before this time (inclusive).

- `deployment_id: Optional[str]`

  Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent deployment_id returns 200 with empty data.

- `has_error: Optional[bool]`

  Filter: true for runs with non-null error, false for runs with non-null session_id. Omit for all.

- `limit: Optional[int]`

  Maximum results per page. Default 20, maximum 1000.

- `page: Optional[str]`

  Opaque pagination cursor. Pass next_page from the previous response. Invalid or expired cursors return 400.

- `trigger_type: Optional[BetaManagedAgentsTriggerType]`

  Filter runs by what triggered them. Omit to return all runs.

  - `"schedule"`

  - `"manual"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaManagedAgentsDeploymentRun: …`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: str`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `deployment_id: str`

    ID of the deployment that produced this run.

  - `error: Optional[Error]`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError: …`

      The deployment's environment was archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["environment_archived_error"]`

        - `"environment_archived_error"`

    - `class BetaManagedAgentsAgentArchivedRunError: …`

      The deployment's agent was archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["agent_archived_error"]`

        - `"agent_archived_error"`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError: …`

      The deployment's environment no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["environment_not_found_error"]`

        - `"environment_not_found_error"`

    - `class BetaManagedAgentsVaultNotFoundRunError: …`

      A vault referenced by the deployment no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["vault_not_found_error"]`

        - `"vault_not_found_error"`

    - `class BetaManagedAgentsVaultArchivedRunError: …`

      A vault referenced by the deployment is archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["vault_archived_error"]`

        - `"vault_archived_error"`

    - `class BetaManagedAgentsFileNotFoundRunError: …`

      A file resource referenced by the deployment no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["file_not_found_error"]`

        - `"file_not_found_error"`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError: …`

      A memory store referenced by the deployment is archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["memory_store_archived_error"]`

        - `"memory_store_archived_error"`

    - `class BetaManagedAgentsSkillNotFoundRunError: …`

      A skill referenced by the deployment's agent no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["skill_not_found_error"]`

        - `"skill_not_found_error"`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError: …`

      A referenced resource no longer exists and its kind was not reported.

      - `message: str`

        Human-readable error description.

      - `type: Literal["session_resource_not_found_error"]`

        - `"session_resource_not_found_error"`

    - `class BetaManagedAgentsWorkspaceArchivedRunError: …`

      The deployment's workspace was archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["workspace_archived_error"]`

        - `"workspace_archived_error"`

    - `class BetaManagedAgentsOrganizationDisabledRunError: …`

      The deployment's organization is disabled.

      - `message: str`

        Human-readable error description.

      - `type: Literal["organization_disabled_error"]`

        - `"organization_disabled_error"`

    - `class BetaManagedAgentsSessionRateLimitedRunError: …`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: str`

        Human-readable error description.

      - `type: Literal["session_rate_limited_error"]`

        - `"session_rate_limited_error"`

    - `class BetaManagedAgentsSessionCreationRejectedRunError: …`

      The session create request was rejected with a non-retryable validation error.

      - `message: str`

        Human-readable error description.

      - `type: Literal["session_creation_rejected_error"]`

        - `"session_creation_rejected_error"`

    - `class BetaManagedAgentsUnknownRunError: …`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: str`

        Human-readable error description.

      - `type: Literal["unknown_error"]`

        - `"unknown_error"`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError: …`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: str`

        Human-readable error description.

      - `type: Literal["self_hosted_resources_unsupported_error"]`

        - `"self_hosted_resources_unsupported_error"`

    - `class BetaManagedAgentsMCPEgressBlockedRunError: …`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: str`

        Human-readable error description.

      - `type: Literal["mcp_egress_blocked_error"]`

        - `"mcp_egress_blocked_error"`

  - `session_id: Optional[str]`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext: …`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: datetime`

        A timestamp in RFC 3339 format

      - `type: Literal["schedule"]`

        - `"schedule"`

    - `class BetaManagedAgentsManualTriggerContext: …`

      The run was started manually by creating a session directly against the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

  - `type: Literal["deployment_run"]`

    - `"deployment_run"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.deployment_runs.list()
page = page.data[0]
print(page.id)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "agent": {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "deployment_id": "deployment_id",
      "error": {
        "message": "message",
        "type": "environment_archived_error"
      },
      "session_id": "session_id",
      "trigger_context": {
        "scheduled_at": "2019-12-27T18:11:19.117Z",
        "type": "schedule"
      },
      "type": "deployment_run"
    }
  ],
  "next_page": "next_page"
}
```

## Get Deployment Run

`beta.deployment_runs.retrieve(strdeployment_run_id, DeploymentRunRetrieveParams**kwargs)  -> BetaManagedAgentsDeploymentRun`

**get** `/v1/deployment_runs/{deployment_run_id}`

Get Deployment Run

### Parameters

- `deployment_run_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaManagedAgentsDeploymentRun: …`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: str`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `deployment_id: str`

    ID of the deployment that produced this run.

  - `error: Optional[Error]`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError: …`

      The deployment's environment was archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["environment_archived_error"]`

        - `"environment_archived_error"`

    - `class BetaManagedAgentsAgentArchivedRunError: …`

      The deployment's agent was archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["agent_archived_error"]`

        - `"agent_archived_error"`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError: …`

      The deployment's environment no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["environment_not_found_error"]`

        - `"environment_not_found_error"`

    - `class BetaManagedAgentsVaultNotFoundRunError: …`

      A vault referenced by the deployment no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["vault_not_found_error"]`

        - `"vault_not_found_error"`

    - `class BetaManagedAgentsVaultArchivedRunError: …`

      A vault referenced by the deployment is archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["vault_archived_error"]`

        - `"vault_archived_error"`

    - `class BetaManagedAgentsFileNotFoundRunError: …`

      A file resource referenced by the deployment no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["file_not_found_error"]`

        - `"file_not_found_error"`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError: …`

      A memory store referenced by the deployment is archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["memory_store_archived_error"]`

        - `"memory_store_archived_error"`

    - `class BetaManagedAgentsSkillNotFoundRunError: …`

      A skill referenced by the deployment's agent no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["skill_not_found_error"]`

        - `"skill_not_found_error"`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError: …`

      A referenced resource no longer exists and its kind was not reported.

      - `message: str`

        Human-readable error description.

      - `type: Literal["session_resource_not_found_error"]`

        - `"session_resource_not_found_error"`

    - `class BetaManagedAgentsWorkspaceArchivedRunError: …`

      The deployment's workspace was archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["workspace_archived_error"]`

        - `"workspace_archived_error"`

    - `class BetaManagedAgentsOrganizationDisabledRunError: …`

      The deployment's organization is disabled.

      - `message: str`

        Human-readable error description.

      - `type: Literal["organization_disabled_error"]`

        - `"organization_disabled_error"`

    - `class BetaManagedAgentsSessionRateLimitedRunError: …`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: str`

        Human-readable error description.

      - `type: Literal["session_rate_limited_error"]`

        - `"session_rate_limited_error"`

    - `class BetaManagedAgentsSessionCreationRejectedRunError: …`

      The session create request was rejected with a non-retryable validation error.

      - `message: str`

        Human-readable error description.

      - `type: Literal["session_creation_rejected_error"]`

        - `"session_creation_rejected_error"`

    - `class BetaManagedAgentsUnknownRunError: …`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: str`

        Human-readable error description.

      - `type: Literal["unknown_error"]`

        - `"unknown_error"`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError: …`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: str`

        Human-readable error description.

      - `type: Literal["self_hosted_resources_unsupported_error"]`

        - `"self_hosted_resources_unsupported_error"`

    - `class BetaManagedAgentsMCPEgressBlockedRunError: …`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: str`

        Human-readable error description.

      - `type: Literal["mcp_egress_blocked_error"]`

        - `"mcp_egress_blocked_error"`

  - `session_id: Optional[str]`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext: …`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: datetime`

        A timestamp in RFC 3339 format

      - `type: Literal["schedule"]`

        - `"schedule"`

    - `class BetaManagedAgentsManualTriggerContext: …`

      The run was started manually by creating a session directly against the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

  - `type: Literal["deployment_run"]`

    - `"deployment_run"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deployment_run = client.beta.deployment_runs.retrieve(
    deployment_run_id="deployment_run_id",
)
print(beta_managed_agents_deployment_run.id)
```

#### Response

```json
{
  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "deployment_id": "deployment_id",
  "error": {
    "message": "message",
    "type": "environment_archived_error"
  },
  "session_id": "session_id",
  "trigger_context": {
    "scheduled_at": "2019-12-27T18:11:19.117Z",
    "type": "schedule"
  },
  "type": "deployment_run"
}
```

## Domain Types

### Beta Managed Agents Agent Archived Run Error

- `class BetaManagedAgentsAgentArchivedRunError: …`

  The deployment's agent was archived.

  - `message: str`

    Human-readable error description.

  - `type: Literal["agent_archived_error"]`

    - `"agent_archived_error"`

### Beta Managed Agents Deployment Run

- `class BetaManagedAgentsDeploymentRun: …`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: str`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `deployment_id: str`

    ID of the deployment that produced this run.

  - `error: Optional[Error]`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError: …`

      The deployment's environment was archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["environment_archived_error"]`

        - `"environment_archived_error"`

    - `class BetaManagedAgentsAgentArchivedRunError: …`

      The deployment's agent was archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["agent_archived_error"]`

        - `"agent_archived_error"`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError: …`

      The deployment's environment no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["environment_not_found_error"]`

        - `"environment_not_found_error"`

    - `class BetaManagedAgentsVaultNotFoundRunError: …`

      A vault referenced by the deployment no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["vault_not_found_error"]`

        - `"vault_not_found_error"`

    - `class BetaManagedAgentsVaultArchivedRunError: …`

      A vault referenced by the deployment is archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["vault_archived_error"]`

        - `"vault_archived_error"`

    - `class BetaManagedAgentsFileNotFoundRunError: …`

      A file resource referenced by the deployment no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["file_not_found_error"]`

        - `"file_not_found_error"`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError: …`

      A memory store referenced by the deployment is archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["memory_store_archived_error"]`

        - `"memory_store_archived_error"`

    - `class BetaManagedAgentsSkillNotFoundRunError: …`

      A skill referenced by the deployment's agent no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["skill_not_found_error"]`

        - `"skill_not_found_error"`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError: …`

      A referenced resource no longer exists and its kind was not reported.

      - `message: str`

        Human-readable error description.

      - `type: Literal["session_resource_not_found_error"]`

        - `"session_resource_not_found_error"`

    - `class BetaManagedAgentsWorkspaceArchivedRunError: …`

      The deployment's workspace was archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["workspace_archived_error"]`

        - `"workspace_archived_error"`

    - `class BetaManagedAgentsOrganizationDisabledRunError: …`

      The deployment's organization is disabled.

      - `message: str`

        Human-readable error description.

      - `type: Literal["organization_disabled_error"]`

        - `"organization_disabled_error"`

    - `class BetaManagedAgentsSessionRateLimitedRunError: …`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: str`

        Human-readable error description.

      - `type: Literal["session_rate_limited_error"]`

        - `"session_rate_limited_error"`

    - `class BetaManagedAgentsSessionCreationRejectedRunError: …`

      The session create request was rejected with a non-retryable validation error.

      - `message: str`

        Human-readable error description.

      - `type: Literal["session_creation_rejected_error"]`

        - `"session_creation_rejected_error"`

    - `class BetaManagedAgentsUnknownRunError: …`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: str`

        Human-readable error description.

      - `type: Literal["unknown_error"]`

        - `"unknown_error"`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError: …`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: str`

        Human-readable error description.

      - `type: Literal["self_hosted_resources_unsupported_error"]`

        - `"self_hosted_resources_unsupported_error"`

    - `class BetaManagedAgentsMCPEgressBlockedRunError: …`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: str`

        Human-readable error description.

      - `type: Literal["mcp_egress_blocked_error"]`

        - `"mcp_egress_blocked_error"`

  - `session_id: Optional[str]`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext: …`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: datetime`

        A timestamp in RFC 3339 format

      - `type: Literal["schedule"]`

        - `"schedule"`

    - `class BetaManagedAgentsManualTriggerContext: …`

      The run was started manually by creating a session directly against the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

  - `type: Literal["deployment_run"]`

    - `"deployment_run"`

### Beta Managed Agents Environment Archived Run Error

- `class BetaManagedAgentsEnvironmentArchivedRunError: …`

  The deployment's environment was archived.

  - `message: str`

    Human-readable error description.

  - `type: Literal["environment_archived_error"]`

    - `"environment_archived_error"`

### Beta Managed Agents Environment Not Found Run Error

- `class BetaManagedAgentsEnvironmentNotFoundRunError: …`

  The deployment's environment no longer exists.

  - `message: str`

    Human-readable error description.

  - `type: Literal["environment_not_found_error"]`

    - `"environment_not_found_error"`

### Beta Managed Agents File Not Found Run Error

- `class BetaManagedAgentsFileNotFoundRunError: …`

  A file resource referenced by the deployment no longer exists.

  - `message: str`

    Human-readable error description.

  - `type: Literal["file_not_found_error"]`

    - `"file_not_found_error"`

### Beta Managed Agents Manual Trigger Context

- `class BetaManagedAgentsManualTriggerContext: …`

  The run was started manually by creating a session directly against the deployment.

  - `type: Literal["manual"]`

    - `"manual"`

### Beta Managed Agents MCP Egress Blocked Run Error

- `class BetaManagedAgentsMCPEgressBlockedRunError: …`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `message: str`

    Human-readable error description.

  - `type: Literal["mcp_egress_blocked_error"]`

    - `"mcp_egress_blocked_error"`

### Beta Managed Agents Memory Store Archived Run Error

- `class BetaManagedAgentsMemoryStoreArchivedRunError: …`

  A memory store referenced by the deployment is archived.

  - `message: str`

    Human-readable error description.

  - `type: Literal["memory_store_archived_error"]`

    - `"memory_store_archived_error"`

### Beta Managed Agents Organization Disabled Run Error

- `class BetaManagedAgentsOrganizationDisabledRunError: …`

  The deployment's organization is disabled.

  - `message: str`

    Human-readable error description.

  - `type: Literal["organization_disabled_error"]`

    - `"organization_disabled_error"`

### Beta Managed Agents Schedule Trigger Context

- `class BetaManagedAgentsScheduleTriggerContext: …`

  The run was fired by the deployment's cron schedule.

  - `scheduled_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["schedule"]`

    - `"schedule"`

### Beta Managed Agents Self Hosted Resources Unsupported Run Error

- `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError: …`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `message: str`

    Human-readable error description.

  - `type: Literal["self_hosted_resources_unsupported_error"]`

    - `"self_hosted_resources_unsupported_error"`

### Beta Managed Agents Session Creation Rejected Run Error

- `class BetaManagedAgentsSessionCreationRejectedRunError: …`

  The session create request was rejected with a non-retryable validation error.

  - `message: str`

    Human-readable error description.

  - `type: Literal["session_creation_rejected_error"]`

    - `"session_creation_rejected_error"`

### Beta Managed Agents Session Rate Limited Run Error

- `class BetaManagedAgentsSessionRateLimitedRunError: …`

  Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

  - `message: str`

    Human-readable error description.

  - `type: Literal["session_rate_limited_error"]`

    - `"session_rate_limited_error"`

### Beta Managed Agents Session Resource Not Found Run Error

- `class BetaManagedAgentsSessionResourceNotFoundRunError: …`

  A referenced resource no longer exists and its kind was not reported.

  - `message: str`

    Human-readable error description.

  - `type: Literal["session_resource_not_found_error"]`

    - `"session_resource_not_found_error"`

### Beta Managed Agents Skill Not Found Run Error

- `class BetaManagedAgentsSkillNotFoundRunError: …`

  A skill referenced by the deployment's agent no longer exists.

  - `message: str`

    Human-readable error description.

  - `type: Literal["skill_not_found_error"]`

    - `"skill_not_found_error"`

### Beta Managed Agents Trigger Context

- `BetaManagedAgentsTriggerContext`

  Describes what triggered a deployment run, with trigger-specific metadata.

  - `class BetaManagedAgentsScheduleTriggerContext: …`

    The run was fired by the deployment's cron schedule.

    - `scheduled_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["schedule"]`

      - `"schedule"`

  - `class BetaManagedAgentsManualTriggerContext: …`

    The run was started manually by creating a session directly against the deployment.

    - `type: Literal["manual"]`

      - `"manual"`

### Beta Managed Agents Trigger Type

- `Literal["schedule", "manual"]`

  What triggered a deployment run.

  - `"schedule"`

  - `"manual"`

### Beta Managed Agents Unknown Run Error

- `class BetaManagedAgentsUnknownRunError: …`

  An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

  - `message: str`

    Human-readable error description.

  - `type: Literal["unknown_error"]`

    - `"unknown_error"`

### Beta Managed Agents Vault Archived Run Error

- `class BetaManagedAgentsVaultArchivedRunError: …`

  A vault referenced by the deployment is archived.

  - `message: str`

    Human-readable error description.

  - `type: Literal["vault_archived_error"]`

    - `"vault_archived_error"`

### Beta Managed Agents Vault Not Found Run Error

- `class BetaManagedAgentsVaultNotFoundRunError: …`

  A vault referenced by the deployment no longer exists.

  - `message: str`

    Human-readable error description.

  - `type: Literal["vault_not_found_error"]`

    - `"vault_not_found_error"`

### Beta Managed Agents Workspace Archived Run Error

- `class BetaManagedAgentsWorkspaceArchivedRunError: …`

  The deployment's workspace was archived.

  - `message: str`

    Human-readable error description.

  - `type: Literal["workspace_archived_error"]`

    - `"workspace_archived_error"`

# Vaults

## Create Vault

`beta.vaults.create(VaultCreateParams**kwargs)  -> BetaManagedAgentsVault`

**post** `/v1/vaults`

Create Vault

### Parameters

- `display_name: str`

  Human-readable name for the vault. 1-255 characters.

- `metadata: Optional[Dict[str, str]]`

  Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_credential_validation = client.beta.vaults.credentials.mcp_oauth_validate(
    credential_id="vcrd_011CZkZEMt8gZan2iYOQfSkw",
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

- `session_id: Optional[str]`

  Query parameter for session_id

- `view: Optional[BetaManagedAgentsMemoryView]`

  Query parameter for view

  - `"basic"`

  - `"full"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

`beta.files.upload(FileUploadParams**kwargs)  -> FileMetadata`

**post** `/v1/files`

Upload File

### Parameters

- `file: FileTypes`

  The file to upload

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class FileMetadata: …`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
file_metadata = client.beta.files.upload(
    file=b"Example data",
)
print(file_metadata.id)
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

`beta.files.list(FileListParams**kwargs)  -> SyncPage[FileMetadata]`

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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class FileMetadata: …`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `BinaryResponseContent`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
response = client.beta.files.download(
    file_id="file_id",
)
print(response)
content = response.read()
print(content)
```

## Get File Metadata

`beta.files.retrieve_metadata(strfile_id, FileRetrieveMetadataParams**kwargs)  -> FileMetadata`

**get** `/v1/files/{file_id}`

Get File Metadata

### Parameters

- `file_id: str`

  ID of the File.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class FileMetadata: …`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
file_metadata = client.beta.files.retrieve_metadata(
    file_id="file_id",
)
print(file_metadata.id)
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

`beta.files.delete(strfile_id, FileDeleteParams**kwargs)  -> DeletedFile`

**delete** `/v1/files/{file_id}`

Delete File

### Parameters

- `file_id: str`

  ID of the File.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class DeletedFile: …`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
deleted_file = client.beta.files.delete(
    file_id="file_id",
)
print(deleted_file.id)
```

#### Response

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```

## Domain Types

### Beta File Scope

- `class BetaFileScope: …`

  - `id: str`

    The ID of the scoping resource (e.g., the session ID).

  - `type: Literal["session"]`

    The type of scope (e.g., `"session"`).

    - `"session"`

### Deleted File

- `class DeletedFile: …`

  - `id: str`

    ID of the deleted file.

  - `type: Optional[Literal["file_deleted"]]`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"`

### File Metadata

- `class FileMetadata: …`

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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `BinaryResponseContent`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

- `external_id: Optional[str]`

  Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

- `metadata: Optional[Dict[str, str]]`

  Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

- `name: Optional[str]`

  Display name of the entity this profile represents. Required when relationship is `resold` (the resold-to company's name); optional otherwise. Maximum 255 characters.

- `relationship: Optional[Literal["external", "resold", "internal"]]`

  How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

  - `"external"`

  - `"resold"`

  - `"internal"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaUserProfile: …`

  - `id: str`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `relationship: Literal["external", "resold", "internal"]`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

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

  - `external_id: Optional[str]`

    Platform's own identifier for this user. Not enforced unique.

  - `name: Optional[str]`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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
  "relationship": "external",
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "external_id": "user_12345",
  "name": "Example User"
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaUserProfile: …`

  - `id: str`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `relationship: Literal["external", "resold", "internal"]`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

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

  - `external_id: Optional[str]`

    Platform's own identifier for this user. Not enforced unique.

  - `name: Optional[str]`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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
      "relationship": "external",
      "trust_grants": {
        "cyber": {
          "status": "active"
        }
      },
      "type": "user_profile",
      "updated_at": "2026-03-15T10:00:00Z",
      "external_id": "user_12345",
      "name": "Example User"
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaUserProfile: …`

  - `id: str`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `relationship: Literal["external", "resold", "internal"]`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

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

  - `external_id: Optional[str]`

    Platform's own identifier for this user. Not enforced unique.

  - `name: Optional[str]`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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
  "relationship": "external",
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "external_id": "user_12345",
  "name": "Example User"
}
```

## Update User Profile

`beta.user_profiles.update(struser_profile_id, UserProfileUpdateParams**kwargs)  -> BetaUserProfile`

**post** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `user_profile_id: str`

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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaUserProfile: …`

  - `id: str`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `relationship: Literal["external", "resold", "internal"]`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

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

  - `external_id: Optional[str]`

    Platform's own identifier for this user. Not enforced unique.

  - `name: Optional[str]`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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
  "relationship": "external",
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "external_id": "user_12345",
  "name": "Example User"
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `relationship: Literal["external", "resold", "internal"]`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

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

  - `external_id: Optional[str]`

    Platform's own identifier for this user. Not enforced unique.

  - `name: Optional[str]`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

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

    An input memory store the dream reads from. The dream never mutates this store.

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

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

- `instructions: Optional[str]`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaDream: …`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

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

      An input memory store the dream reads from. The dream never mutates this store.

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

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_dream = client.beta.dreams.create(
    inputs=[{
        "memory_store_id": "x",
        "type": "memory_store",
    }],
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaDream: …`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

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

      An input memory store the dream reads from. The dream never mutates this store.

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

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaDream: …`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

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

      An input memory store the dream reads from. The dream never mutates this store.

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

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaDream: …`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

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

      An input memory store the dream reads from. The dream never mutates this store.

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

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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

### Returns

- `class BetaDream: …`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

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

      An input memory store the dream reads from. The dream never mutates this store.

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

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

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

      An input memory store the dream reads from. The dream never mutates this store.

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

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

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

  An input memory store the dream reads from. The dream never mutates this store.

  - `class BetaDreamMemoryStoreInput: …`

    An input memory store the dream reads from. The dream never mutates this store.

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

  An input memory store the dream reads from. The dream never mutates this store.

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

    Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

  - `speed: Optional[Literal["standard", "fast"]]`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Dream Model Config Param

- `class BetaDreamModelConfigParam: …`

  Model identifier and configuration applied to every pipeline stage.

  - `id: str`

    Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 29 more]`

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
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
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

  - `type: Literal["event"]`

    Object type. Always `event` for webhook payloads.

    - `"event"`
