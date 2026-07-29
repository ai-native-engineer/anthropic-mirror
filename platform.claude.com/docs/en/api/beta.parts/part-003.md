<!-- source: https://platform.claude.com/docs/en/api/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/beta -->

<!-- chunk-start -->

        - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsURLImageSource object { type, url }`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `BetaManagedAgentsFileImageSource object { file_id, type }`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsURLDocumentSource object { type, url }`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "document"`

        - `"document"`

      - `context: optional string`

        Additional context about the document for the model.

      - `title: optional string`

        The title of the document.

  - `type: "user.message"`

    - `"user.message"`

  - `processed_at: optional string`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Message Event Params

- `BetaManagedAgentsUserMessageEventParams object { content, type }`

  Parameters for sending a user message to the session.

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

    Array of content blocks for the user message.

    - `BetaManagedAgentsTextBlock object { text, type }`

      Regular text content.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `BetaManagedAgentsImageBlock object { source, type }`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsURLImageSource object { type, url }`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `BetaManagedAgentsFileImageSource object { file_id, type }`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsURLDocumentSource object { type, url }`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "document"`

        - `"document"`

      - `context: optional string`

        Additional context about the document for the model.

      - `title: optional string`

        The title of the document.

  - `type: "user.message"`

    - `"user.message"`

### Beta Managed Agents User Tool Confirmation Event

- `BetaManagedAgentsUserToolConfirmationEvent object { id, result, tool_use_id, 4 more }`

  A tool confirmation event that approves or denies a pending tool execution.

  - `id: string`

    Unique identifier for this event.

  - `result: "allow" or "deny"`

    UserToolConfirmationResult enum

    - `"allow"`

    - `"deny"`

  - `tool_use_id: string`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: "user.tool_confirmation"`

    - `"user.tool_confirmation"`

  - `deny_message: optional string`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `processed_at: optional string`

    A timestamp in RFC 3339 format

  - `session_thread_id: optional string`

    When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

### Beta Managed Agents User Tool Confirmation Event Params

- `BetaManagedAgentsUserToolConfirmationEventParams object { result, tool_use_id, type, deny_message }`

  Parameters for confirming or denying a tool execution request.

  - `result: "allow" or "deny"`

    UserToolConfirmationResult enum

    - `"allow"`

    - `"deny"`

  - `tool_use_id: string`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: "user.tool_confirmation"`

    - `"user.tool_confirmation"`

  - `deny_message: optional string`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

### Beta Managed Agents User Tool Result Event Params

- `BetaManagedAgentsUserToolResultEventParams object { tool_use_id, type, content, is_error }`

  Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

  - `tool_use_id: string`

    The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: "user.tool_result"`

    - `"user.tool_result"`

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

    The result content returned by the tool.

    - `BetaManagedAgentsTextBlock object { text, type }`

      Regular text content.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `BetaManagedAgentsImageBlock object { source, type }`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsURLImageSource object { type, url }`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `BetaManagedAgentsFileImageSource object { file_id, type }`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsURLDocumentSource object { type, url }`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "document"`

        - `"document"`

      - `context: optional string`

        Additional context about the document for the model.

      - `title: optional string`

        The title of the document.

    - `BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }`

      A block containing a web search result.

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for a search result.

        - `enabled: boolean`

          Whether citations are enabled for this search result.

      - `content: array of BetaManagedAgentsSearchResultContent`

        Array of text content blocks from the search result.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `source: string`

        The URL source of the search result.

      - `title: string`

        The title of the search result.

      - `type: "search_result"`

        - `"search_result"`

  - `is_error: optional boolean`

    Whether the tool execution resulted in an error.

# Resources

## Add Session Resource

**post** `/v1/sessions/{session_id}/resources`

Add Session Resource

### Path Parameters

- `session_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `file_id: string`

  ID of a previously uploaded file.

- `type: "file"`

  - `"file"`

- `mount_path: optional string`

  Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Returns

- `BetaManagedAgentsFileResource object { id, created_at, file_id, 3 more }`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `file_id: string`

  - `mount_path: string`

  - `type: "file"`

    - `"file"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/resources \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
          "type": "file",
          "mount_path": "/uploads/receipt.pdf"
        }'
```

#### Response

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "created_at": "2026-03-15T10:00:00Z",
  "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "mount_path": "/uploads/receipt.pdf",
  "type": "file",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## List Session Resources

**get** `/v1/sessions/{session_id}/resources`

List Session Resources

### Path Parameters

- `session_id: string`

### Query Parameters

- `limit: optional number`

  Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `data: array of BetaManagedAgentsSessionResource`

  Resources for the session, ordered by `created_at`.

  - `BetaManagedAgentsGitHubRepositoryResource object { id, created_at, mount_path, 4 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `mount_path: string`

    - `type: "github_repository"`

      - `"github_repository"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `url: string`

    - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

      - `BetaManagedAgentsBranchCheckout object { name, type }`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `BetaManagedAgentsCommitCheckout object { sha, type }`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

  - `BetaManagedAgentsFileResource object { id, created_at, file_id, 3 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `file_id: string`

    - `mount_path: string`

    - `type: "file"`

      - `"file"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

  - `BetaManagedAgentsMemoryStoreResource object { memory_store_id, type, access, 4 more }`

    A memory store attached to an agent session.

    - `memory_store_id: string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: "memory_store"`

      - `"memory_store"`

    - `access: optional "read_write" or "read_only"`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description: optional string`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: optional string`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `mount_path: optional string`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: optional string`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

- `next_page: optional string`

  Opaque cursor for the next page. Null when no more results.

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/resources \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Session Resource

**get** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

### Path Parameters

- `session_id: string`

- `resource_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsGitHubRepositoryResource object { id, created_at, mount_path, 4 more }`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `mount_path: string`

  - `type: "github_repository"`

    - `"github_repository"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `url: string`

  - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

    - `BetaManagedAgentsBranchCheckout object { name, type }`

      - `name: string`

        Branch name to check out.

      - `type: "branch"`

        - `"branch"`

    - `BetaManagedAgentsCommitCheckout object { sha, type }`

      - `sha: string`

        Full commit SHA to check out.

      - `type: "commit"`

        - `"commit"`

- `BetaManagedAgentsFileResource object { id, created_at, file_id, 3 more }`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `file_id: string`

  - `mount_path: string`

  - `type: "file"`

    - `"file"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

- `BetaManagedAgentsMemoryStoreResource object { memory_store_id, type, access, 4 more }`

  A memory store attached to an agent session.

  - `memory_store_id: string`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `type: "memory_store"`

    - `"memory_store"`

  - `access: optional "read_write" or "read_only"`

    Access mode for an attached memory store.

    - `"read_write"`

    - `"read_only"`

  - `description: optional string`

    Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

  - `instructions: optional string`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `mount_path: optional string`

    Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

  - `name: optional string`

    Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/resources/$RESOURCE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

### Path Parameters

- `session_id: string`

- `resource_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `authorization_token: string`

  New authorization token for the resource. Currently only `github_repository` resources support token rotation.

### Returns

- `BetaManagedAgentsGitHubRepositoryResource object { id, created_at, mount_path, 4 more }`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `mount_path: string`

  - `type: "github_repository"`

    - `"github_repository"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `url: string`

  - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

    - `BetaManagedAgentsBranchCheckout object { name, type }`

      - `name: string`

        Branch name to check out.

      - `type: "branch"`

        - `"branch"`

    - `BetaManagedAgentsCommitCheckout object { sha, type }`

      - `sha: string`

        Full commit SHA to check out.

      - `type: "commit"`

        - `"commit"`

- `BetaManagedAgentsFileResource object { id, created_at, file_id, 3 more }`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `file_id: string`

  - `mount_path: string`

  - `type: "file"`

    - `"file"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

- `BetaManagedAgentsMemoryStoreResource object { memory_store_id, type, access, 4 more }`

  A memory store attached to an agent session.

  - `memory_store_id: string`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `type: "memory_store"`

    - `"memory_store"`

  - `access: optional "read_write" or "read_only"`

    Access mode for an attached memory store.

    - `"read_write"`

    - `"read_only"`

  - `description: optional string`

    Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

  - `instructions: optional string`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `mount_path: optional string`

    Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

  - `name: optional string`

    Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/resources/$RESOURCE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "authorization_token": "ghp_exampletoken"
        }'
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

**delete** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

### Path Parameters

- `session_id: string`

- `resource_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsDeleteSessionResource object { id, type }`

  Confirmation of resource deletion.

  - `id: string`

  - `type: "session_resource_deleted"`

    - `"session_resource_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/resources/$RESOURCE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `BetaManagedAgentsDeleteSessionResource object { id, type }`

  Confirmation of resource deletion.

  - `id: string`

  - `type: "session_resource_deleted"`

    - `"session_resource_deleted"`

### Beta Managed Agents File Resource

- `BetaManagedAgentsFileResource object { id, created_at, file_id, 3 more }`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `file_id: string`

  - `mount_path: string`

  - `type: "file"`

    - `"file"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Beta Managed Agents GitHub Repository Resource

- `BetaManagedAgentsGitHubRepositoryResource object { id, created_at, mount_path, 4 more }`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `mount_path: string`

  - `type: "github_repository"`

    - `"github_repository"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `url: string`

  - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

    - `BetaManagedAgentsBranchCheckout object { name, type }`

      - `name: string`

        Branch name to check out.

      - `type: "branch"`

        - `"branch"`

    - `BetaManagedAgentsCommitCheckout object { sha, type }`

      - `sha: string`

        Full commit SHA to check out.

      - `type: "commit"`

        - `"commit"`

### Beta Managed Agents Memory Store Resource

- `BetaManagedAgentsMemoryStoreResource object { memory_store_id, type, access, 4 more }`

  A memory store attached to an agent session.

  - `memory_store_id: string`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `type: "memory_store"`

    - `"memory_store"`

  - `access: optional "read_write" or "read_only"`

    Access mode for an attached memory store.

    - `"read_write"`

    - `"read_only"`

  - `description: optional string`

    Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

  - `instructions: optional string`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `mount_path: optional string`

    Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

  - `name: optional string`

    Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Beta Managed Agents Session Resource

- `BetaManagedAgentsSessionResource = BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource or BetaManagedAgentsMemoryStoreResource`

  A memory store attached to an agent session.

  - `BetaManagedAgentsGitHubRepositoryResource object { id, created_at, mount_path, 4 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `mount_path: string`

    - `type: "github_repository"`

      - `"github_repository"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `url: string`

    - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

      - `BetaManagedAgentsBranchCheckout object { name, type }`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `BetaManagedAgentsCommitCheckout object { sha, type }`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

  - `BetaManagedAgentsFileResource object { id, created_at, file_id, 3 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `file_id: string`

    - `mount_path: string`

    - `type: "file"`

      - `"file"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

  - `BetaManagedAgentsMemoryStoreResource object { memory_store_id, type, access, 4 more }`

    A memory store attached to an agent session.

    - `memory_store_id: string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: "memory_store"`

      - `"memory_store"`

    - `access: optional "read_write" or "read_only"`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description: optional string`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: optional string`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `mount_path: optional string`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: optional string`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Resource Retrieve Response

- `ResourceRetrieveResponse = BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource or BetaManagedAgentsMemoryStoreResource`

  The requested session resource.

  - `BetaManagedAgentsGitHubRepositoryResource object { id, created_at, mount_path, 4 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `mount_path: string`

    - `type: "github_repository"`

      - `"github_repository"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `url: string`

    - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

      - `BetaManagedAgentsBranchCheckout object { name, type }`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `BetaManagedAgentsCommitCheckout object { sha, type }`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

  - `BetaManagedAgentsFileResource object { id, created_at, file_id, 3 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `file_id: string`

    - `mount_path: string`

    - `type: "file"`

      - `"file"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

  - `BetaManagedAgentsMemoryStoreResource object { memory_store_id, type, access, 4 more }`

    A memory store attached to an agent session.

    - `memory_store_id: string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: "memory_store"`

      - `"memory_store"`

    - `access: optional "read_write" or "read_only"`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description: optional string`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: optional string`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `mount_path: optional string`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: optional string`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Resource Update Response

- `ResourceUpdateResponse = BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource or BetaManagedAgentsMemoryStoreResource`

  The updated session resource.

  - `BetaManagedAgentsGitHubRepositoryResource object { id, created_at, mount_path, 4 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `mount_path: string`

    - `type: "github_repository"`

      - `"github_repository"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `url: string`

    - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

      - `BetaManagedAgentsBranchCheckout object { name, type }`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `BetaManagedAgentsCommitCheckout object { sha, type }`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

  - `BetaManagedAgentsFileResource object { id, created_at, file_id, 3 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `file_id: string`

    - `mount_path: string`

    - `type: "file"`

      - `"file"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

  - `BetaManagedAgentsMemoryStoreResource object { memory_store_id, type, access, 4 more }`

    A memory store attached to an agent session.

    - `memory_store_id: string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: "memory_store"`

      - `"memory_store"`

    - `access: optional "read_write" or "read_only"`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description: optional string`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: optional string`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `mount_path: optional string`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: optional string`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

# Threads

## List Session Threads

**get** `/v1/sessions/{session_id}/threads`

List Session Threads

### Path Parameters

- `session_id: string`

### Query Parameters

- `limit: optional number`

  Maximum results per page. Defaults to 1000.

- `page: optional string`

  Opaque pagination cursor from a previous response's next_page. Forward-only.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `data: optional array of BetaManagedAgentsSessionThread`

  Threads in the session, primary first then children in spawn order.

  - `id: string`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

    - `id: string`

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

        - `"url"`

      - `url: string`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

        - `string`

      - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `BetaManagedAgentsEffortLow object { type }`

          Low effort. Favors latency over reasoning depth.

          - `type: "low"`

            - `"low"`

        - `BetaManagedAgentsEffortMedium object { type }`

          Medium effort. Balances latency and reasoning depth.

          - `type: "medium"`

            - `"medium"`

        - `BetaManagedAgentsEffortHigh object { type }`

          High effort. Favors reasoning depth.

          - `type: "high"`

            - `"high"`

        - `BetaManagedAgentsEffortXhigh object { type }`

          Extra-high effort. Not all models accept this level.

          - `type: "xhigh"`

            - `"xhigh"`

        - `BetaManagedAgentsEffortMax object { type }`

          Maximum effort. Favors reasoning depth over latency.

          - `type: "max"`

            - `"max"`

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

        A resolved Anthropic-managed skill.

        - `skill_id: string`

        - `type: "anthropic"`

          - `"anthropic"`

        - `version: string`

      - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

        A resolved user-created custom skill.

        - `skill_id: string`

        - `type: "custom"`

          - `"custom"`

        - `version: string`

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

        - `configs: array of BetaManagedAgentsAgentToolConfig`

          - `enabled: boolean`

          - `name: "bash" or "edit" or "read" or 5 more`

            Built-in agent tool identifier.

            - `"bash"`

            - `"edit"`

            - `"read"`

            - `"write"`

            - `"glob"`

            - `"grep"`

            - `"web_fetch"`

            - `"web_search"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

          Resolved default configuration for agent tools.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy object { type }`

              Tool calls require user confirmation before execution.

        - `type: "agent_toolset_20260401"`

          - `"agent_toolset_20260401"`

      - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

        - `configs: array of BetaManagedAgentsMCPToolConfig`

          - `enabled: boolean`

          - `name: string`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy object { type }`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy object { type }`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: string`

        - `type: "mcp_toolset"`

          - `"mcp_toolset"`

      - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

        A custom tool as returned in API responses.

        - `description: string`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: "object"`

            - `"object"`

          - `properties: optional map[unknown]`

          - `required: optional array of string`

        - `name: string`

        - `type: "custom"`

          - `"custom"`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `parent_thread_id: string`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: string`

    The session this thread belongs to.

  - `stats: BetaManagedAgentsSessionThreadStats`

    Timing statistics for a session thread.

    - `active_seconds: optional number`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `duration_seconds: optional number`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `startup_seconds: optional number`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: "session_thread"`

    - `"session_thread"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `usage: BetaManagedAgentsSessionThreadUsage`

    Cumulative token usage for a session thread across all turns.

    - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: optional number`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: optional number`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: optional number`

      Total tokens read from prompt cache.

    - `input_tokens: optional number`

      Total input tokens consumed across all turns.

    - `output_tokens: optional number`

      Total output tokens generated across all turns.

- `next_page: optional string`

  Opaque cursor for the next page. Null when no more results.

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/threads \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

### Path Parameters

- `session_id: string`

- `thread_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsSessionThread object { id, agent, archived_at, 8 more }`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: string`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

    - `id: string`

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

        - `"url"`

      - `url: string`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

        - `string`

      - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `BetaManagedAgentsEffortLow object { type }`

          Low effort. Favors latency over reasoning depth.

          - `type: "low"`

            - `"low"`

        - `BetaManagedAgentsEffortMedium object { type }`

          Medium effort. Balances latency and reasoning depth.

          - `type: "medium"`

            - `"medium"`

        - `BetaManagedAgentsEffortHigh object { type }`

          High effort. Favors reasoning depth.

          - `type: "high"`

            - `"high"`

        - `BetaManagedAgentsEffortXhigh object { type }`

          Extra-high effort. Not all models accept this level.

          - `type: "xhigh"`

            - `"xhigh"`

        - `BetaManagedAgentsEffortMax object { type }`

          Maximum effort. Favors reasoning depth over latency.

          - `type: "max"`

            - `"max"`

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

        A resolved Anthropic-managed skill.

        - `skill_id: string`

        - `type: "anthropic"`

          - `"anthropic"`

        - `version: string`

      - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

        A resolved user-created custom skill.

        - `skill_id: string`

        - `type: "custom"`

          - `"custom"`

        - `version: string`

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

        - `configs: array of BetaManagedAgentsAgentToolConfig`

          - `enabled: boolean`

          - `name: "bash" or "edit" or "read" or 5 more`

            Built-in agent tool identifier.

            - `"bash"`

            - `"edit"`

            - `"read"`

            - `"write"`

            - `"glob"`

            - `"grep"`

            - `"web_fetch"`

            - `"web_search"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

          Resolved default configuration for agent tools.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy object { type }`

              Tool calls require user confirmation before execution.

        - `type: "agent_toolset_20260401"`

          - `"agent_toolset_20260401"`

      - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

        - `configs: array of BetaManagedAgentsMCPToolConfig`

          - `enabled: boolean`

          - `name: string`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy object { type }`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy object { type }`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: string`

        - `type: "mcp_toolset"`

          - `"mcp_toolset"`

      - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

        A custom tool as returned in API responses.

        - `description: string`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: "object"`

            - `"object"`

          - `properties: optional map[unknown]`

          - `required: optional array of string`

        - `name: string`

        - `type: "custom"`

          - `"custom"`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `parent_thread_id: string`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: string`

    The session this thread belongs to.

  - `stats: BetaManagedAgentsSessionThreadStats`

    Timing statistics for a session thread.

    - `active_seconds: optional number`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `duration_seconds: optional number`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `startup_seconds: optional number`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: "session_thread"`

    - `"session_thread"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `usage: BetaManagedAgentsSessionThreadUsage`

    Cumulative token usage for a session thread across all turns.

    - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: optional number`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: optional number`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: optional number`

      Total tokens read from prompt cache.

    - `input_tokens: optional number`

      Total input tokens consumed across all turns.

    - `output_tokens: optional number`

      Total output tokens generated across all turns.

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

### Path Parameters

- `session_id: string`

- `thread_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsSessionThread object { id, agent, archived_at, 8 more }`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: string`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

    - `id: string`

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

        - `"url"`

      - `url: string`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

        - `string`

      - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `BetaManagedAgentsEffortLow object { type }`

          Low effort. Favors latency over reasoning depth.

          - `type: "low"`

            - `"low"`

        - `BetaManagedAgentsEffortMedium object { type }`

          Medium effort. Balances latency and reasoning depth.

          - `type: "medium"`

            - `"medium"`

        - `BetaManagedAgentsEffortHigh object { type }`

          High effort. Favors reasoning depth.

          - `type: "high"`

            - `"high"`

        - `BetaManagedAgentsEffortXhigh object { type }`

          Extra-high effort. Not all models accept this level.

          - `type: "xhigh"`

            - `"xhigh"`

        - `BetaManagedAgentsEffortMax object { type }`

          Maximum effort. Favors reasoning depth over latency.

          - `type: "max"`

            - `"max"`

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

        A resolved Anthropic-managed skill.

        - `skill_id: string`

        - `type: "anthropic"`

          - `"anthropic"`

        - `version: string`

      - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

        A resolved user-created custom skill.

        - `skill_id: string`

        - `type: "custom"`

          - `"custom"`

        - `version: string`

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

        - `configs: array of BetaManagedAgentsAgentToolConfig`

          - `enabled: boolean`

          - `name: "bash" or "edit" or "read" or 5 more`

            Built-in agent tool identifier.

            - `"bash"`

            - `"edit"`

            - `"read"`

            - `"write"`

            - `"glob"`

            - `"grep"`

            - `"web_fetch"`

            - `"web_search"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

          Resolved default configuration for agent tools.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy object { type }`

              Tool calls require user confirmation before execution.

        - `type: "agent_toolset_20260401"`

          - `"agent_toolset_20260401"`

      - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

        - `configs: array of BetaManagedAgentsMCPToolConfig`

          - `enabled: boolean`

          - `name: string`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy object { type }`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy object { type }`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: string`

        - `type: "mcp_toolset"`

          - `"mcp_toolset"`

      - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

        A custom tool as returned in API responses.

        - `description: string`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: "object"`

            - `"object"`

          - `properties: optional map[unknown]`

          - `required: optional array of string`

        - `name: string`

        - `type: "custom"`

          - `"custom"`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `parent_thread_id: string`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: string`

    The session this thread belongs to.

  - `stats: BetaManagedAgentsSessionThreadStats`

    Timing statistics for a session thread.

    - `active_seconds: optional number`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `duration_seconds: optional number`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `startup_seconds: optional number`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: "session_thread"`

    - `"session_thread"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `usage: BetaManagedAgentsSessionThreadUsage`

    Cumulative token usage for a session thread across all turns.

    - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: optional number`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: optional number`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: optional number`

      Total tokens read from prompt cache.

    - `input_tokens: optional number`

      Total input tokens consumed across all turns.

    - `output_tokens: optional number`

      Total output tokens generated across all turns.

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `BetaManagedAgentsSessionThread object { id, agent, archived_at, 8 more }`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: string`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

    - `id: string`

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

        - `"url"`

      - `url: string`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

        - `string`

      - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `BetaManagedAgentsEffortLow object { type }`

          Low effort. Favors latency over reasoning depth.

          - `type: "low"`

            - `"low"`

        - `BetaManagedAgentsEffortMedium object { type }`

          Medium effort. Balances latency and reasoning depth.

          - `type: "medium"`

            - `"medium"`

        - `BetaManagedAgentsEffortHigh object { type }`

          High effort. Favors reasoning depth.

          - `type: "high"`

            - `"high"`

        - `BetaManagedAgentsEffortXhigh object { type }`

          Extra-high effort. Not all models accept this level.

          - `type: "xhigh"`

            - `"xhigh"`

        - `BetaManagedAgentsEffortMax object { type }`

          Maximum effort. Favors reasoning depth over latency.

          - `type: "max"`

            - `"max"`

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

        A resolved Anthropic-managed skill.

        - `skill_id: string`

        - `type: "anthropic"`

          - `"anthropic"`

        - `version: string`

      - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

        A resolved user-created custom skill.

        - `skill_id: string`

        - `type: "custom"`

          - `"custom"`

        - `version: string`

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

        - `configs: array of BetaManagedAgentsAgentToolConfig`

          - `enabled: boolean`

          - `name: "bash" or "edit" or "read" or 5 more`

            Built-in agent tool identifier.

            - `"bash"`

            - `"edit"`

            - `"read"`

            - `"write"`

            - `"glob"`

            - `"grep"`

            - `"web_fetch"`

            - `"web_search"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

          Resolved default configuration for agent tools.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy object { type }`

              Tool calls require user confirmation before execution.

        - `type: "agent_toolset_20260401"`

          - `"agent_toolset_20260401"`

      - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

        - `configs: array of BetaManagedAgentsMCPToolConfig`

          - `enabled: boolean`

          - `name: string`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy object { type }`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy object { type }`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: string`

        - `type: "mcp_toolset"`

          - `"mcp_toolset"`

      - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

        A custom tool as returned in API responses.

        - `description: string`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: "object"`

            - `"object"`

          - `properties: optional map[unknown]`

          - `required: optional array of string`

        - `name: string`

        - `type: "custom"`

          - `"custom"`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `parent_thread_id: string`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: string`

    The session this thread belongs to.

  - `stats: BetaManagedAgentsSessionThreadStats`

    Timing statistics for a session thread.

    - `active_seconds: optional number`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `duration_seconds: optional number`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `startup_seconds: optional number`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: "session_thread"`

    - `"session_thread"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `usage: BetaManagedAgentsSessionThreadUsage`

    Cumulative token usage for a session thread across all turns.

    - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: optional number`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: optional number`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: optional number`

      Total tokens read from prompt cache.

    - `input_tokens: optional number`

      Total input tokens consumed across all turns.

    - `output_tokens: optional number`

      Total output tokens generated across all turns.

### Beta Managed Agents Session Thread Stats

- `BetaManagedAgentsSessionThreadStats object { active_seconds, duration_seconds, startup_seconds }`

  Timing statistics for a session thread.

  - `active_seconds: optional number`

    Cumulative time in seconds the thread spent actively running. Excludes idle time.

  - `duration_seconds: optional number`

    Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

  - `startup_seconds: optional number`

    Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

### Beta Managed Agents Session Thread Status

- `BetaManagedAgentsSessionThreadStatus = "running" or "idle" or "rescheduling" or "terminated"`

  SessionThreadStatus enum

  - `"running"`

  - `"idle"`

  - `"rescheduling"`

  - `"terminated"`

### Beta Managed Agents Session Thread Usage

- `BetaManagedAgentsSessionThreadUsage object { cache_creation, cache_read_input_tokens, input_tokens, output_tokens }`

  Cumulative token usage for a session thread across all turns.

  - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

    Prompt-cache creation token usage broken down by cache lifetime.

    - `ephemeral_1h_input_tokens: optional number`

      Tokens used to create 1-hour ephemeral cache entries.

    - `ephemeral_5m_input_tokens: optional number`

      Tokens used to create 5-minute ephemeral cache entries.

  - `cache_read_input_tokens: optional number`

    Total tokens read from prompt cache.

  - `input_tokens: optional number`

    Total input tokens consumed across all turns.

  - `output_tokens: optional number`

    Total output tokens generated across all turns.

### Beta Managed Agents Stream Session Thread Events

- `BetaManagedAgentsStreamSessionThreadEvents = BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 33 more`

  Server-sent event in a single thread's stream.

  - `BetaManagedAgentsUserMessageEvent object { id, content, type, processed_at }`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `type: "user.message"`

      - `"user.message"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `BetaManagedAgentsUserInterruptEvent object { id, type, processed_at, session_thread_id }`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

      - `"user.interrupt"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

    - `session_thread_id: optional string`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEvent object { id, result, tool_use_id, 4 more }`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_confirmation"`

      - `"user.tool_confirmation"`

    - `deny_message: optional string`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

    - `session_thread_id: optional string`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `BetaManagedAgentsUserCustomToolResultEvent object { id, custom_tool_use_id, type, 4 more }`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

      - `"user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `source: string`

          The URL source of the search result.

        - `title: string`

          The title of the search result.

        - `type: "search_result"`

          - `"search_result"`

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

    - `session_thread_id: optional string`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsAgentCustomToolUseEvent object { id, input, name, 3 more }`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.custom_tool_use"`

      - `"agent.custom_tool_use"`

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `BetaManagedAgentsAgentMessageEvent object { id, content, processed_at, type }`

    An agent response event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock`

      Array of text blocks comprising the agent response.

      - `text: string`

        The text content.

      - `type: "text"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.message"`

      - `"agent.message"`

  - `BetaManagedAgentsAgentThinkingEvent object { id, processed_at, type }`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thinking"`

      - `"agent.thinking"`

  - `BetaManagedAgentsAgentMCPToolUseEvent object { id, input, mcp_server_name, 5 more }`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.mcp_tool_use"`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentMCPToolResultEvent object { id, mcp_tool_use_id, processed_at, 3 more }`

    Event representing the result of an MCP tool execution.

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.mcp_tool_result"`

      - `"agent.mcp_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentToolUseEvent object { id, input, name, 4 more }`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.tool_use"`

      - `"agent.tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentToolResultEvent object { id, processed_at, tool_use_id, 3 more }`

    Event representing the result of an agent tool execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: "agent.tool_result"`

      - `"agent.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentThreadMessageReceivedEvent object { id, content, from_session_thread_id, 3 more }`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Message content blocks.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `from_session_thread_id: string`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thread_message_received"`

      - `"agent.thread_message_received"`

    - `from_agent_name: optional string`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `BetaManagedAgentsAgentThreadMessageSentEvent object { id, content, processed_at, 3 more }`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Message content blocks.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: "agent.thread_message_sent"`

      - `"agent.thread_message_sent"`

    - `to_agent_name: optional string`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `BetaManagedAgentsAgentThreadContextCompactedEvent object { id, processed_at, type }`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thread_context_compacted"`

      - `"agent.thread_context_compacted"`

  - `BetaManagedAgentsSessionErrorEvent object { id, error, processed_at, type }`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 5 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `BetaManagedAgentsUnknownError object { message, retry_status, type }`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "unknown_error"`

          - `"unknown_error"`

      - `BetaManagedAgentsModelOverloadedError object { message, retry_status, type }`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_overloaded_error"`

          - `"model_overloaded_error"`

      - `BetaManagedAgentsModelRateLimitedError object { message, retry_status, type }`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_rate_limited_error"`

          - `"model_rate_limited_error"`

      - `BetaManagedAgentsModelRequestFailedError object { message, retry_status, type }`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_request_failed_error"`

          - `"model_request_failed_error"`

      - `BetaManagedAgentsMCPConnectionFailedError object { mcp_server_name, message, retry_status, type }`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_connection_failed_error"`

          - `"mcp_connection_failed_error"`

      - `BetaManagedAgentsMCPAuthenticationFailedError object { mcp_server_name, message, retry_status, type }`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_authentication_failed_error"`

          - `"mcp_authentication_failed_error"`

      - `BetaManagedAgentsBillingError object { message, retry_status, type }`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "billing_error"`

          - `"billing_error"`

      - `BetaManagedAgentsCredentialHostUnreachableError object { credential_id, message, retry_status, 2 more }`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "credential_host_unreachable_error"`

          - `"credential_host_unreachable_error"`

        - `vault_id: string`

          ID of the vault containing the affected credential.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.error"`

      - `"session.error"`

  - `BetaManagedAgentsSessionStatusRescheduledEvent object { id, processed_at, type }`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_rescheduled"`

      - `"session.status_rescheduled"`

  - `BetaManagedAgentsSessionStatusRunningEvent object { id, processed_at, type }`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_running"`

      - `"session.status_running"`

  - `BetaManagedAgentsSessionStatusIdleEvent object { id, processed_at, stop_reason, type }`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn object { type }`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

          - `"end_turn"`

      - `BetaManagedAgentsSessionRequiresAction object { event_ids, type }`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

          - `"requires_action"`

      - `BetaManagedAgentsSessionRetriesExhausted object { type }`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

          - `"retries_exhausted"`

    - `type: "session.status_idle"`

      - `"session.status_idle"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent object { id, processed_at, type }`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_terminated"`

      - `"session.status_terminated"`

  - `BetaManagedAgentsSessionThreadCreatedEvent object { id, agent_name, processed_at, 2 more }`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

    - `type: "session.thread_created"`

      - `"session.thread_created"`

  - `BetaManagedAgentsSpanOutcomeEvaluationStartEvent object { id, iteration, outcome_id, 2 more }`

    Emitted when an outcome evaluation cycle begins.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.outcome_evaluation_start"`

      - `"span.outcome_evaluation_start"`

  - `BetaManagedAgentsSpanOutcomeEvaluationEndEvent object { id, explanation, iteration, 6 more }`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: string`

      Unique identifier for this event.

    - `explanation: string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_evaluation_start_id: string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `result: string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: "span.outcome_evaluation_end"`

      - `"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

      - `input_tokens: number`

        Input tokens consumed by this request.

      - `output_tokens: number`

        Output tokens generated by this request.

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `BetaManagedAgentsSpanModelRequestStartEvent object { id, processed_at, type }`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_start"`

      - `"span.model_request_start"`

  - `BetaManagedAgentsSpanModelRequestEndEvent object { id, is_error, model_request_start_id, 3 more }`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_end"`

      - `"span.model_request_end"`

  - `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object { id, iteration, outcome_id, 2 more }`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.outcome_evaluation_ongoing"`

      - `"span.outcome_evaluation_ongoing"`

  - `BetaManagedAgentsUserDefineOutcomeEvent object { id, description, max_iterations, 4 more }`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: string`

      Unique identifier for this event.

    - `description: string`

      What the agent should produce. Copied from the input event.

    - `max_iterations: number`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `outcome_id: string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubric object { file_id, type }`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

          - `"file"`

      - `BetaManagedAgentsTextRubric object { content, type }`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: "text"`

          - `"text"`

    - `type: "user.define_outcome"`

      - `"user.define_outcome"`

  - `BetaManagedAgentsSessionDeletedEvent object { id, processed_at, type }`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.deleted"`

      - `"session.deleted"`

  - `BetaManagedAgentsSessionThreadStatusRunningEvent object { id, agent_name, processed_at, 2 more }`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

    - `type: "session.thread_status_running"`

      - `"session.thread_status_running"`

  - `BetaManagedAgentsSessionThreadStatusIdleEvent object { id, agent_name, processed_at, 3 more }`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn object { type }`

        The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionRequiresAction object { event_ids, type }`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `BetaManagedAgentsSessionRetriesExhausted object { type }`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

    - `type: "session.thread_status_idle"`

      - `"session.thread_status_idle"`

  - `BetaManagedAgentsSessionThreadStatusTerminatedEvent object { id, agent_name, processed_at, 2 more }`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

    - `type: "session.thread_status_terminated"`

      - `"session.thread_status_terminated"`

  - `BetaManagedAgentsUserToolResultEvent object { id, tool_use_id, type, 4 more }`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_result"`

      - `"user.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

    - `session_thread_id: optional string`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsSessionThreadStatusRescheduledEvent object { id, agent_name, processed_at, 2 more }`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

    - `type: "session.thread_status_rescheduled"`

      - `"session.thread_status_rescheduled"`

  - `BetaManagedAgentsSessionUpdatedEvent object { id, processed_at, type, 3 more }`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.updated"`

      - `"session.updated"`

    - `agent: optional BetaManagedAgentsSessionAgent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: string`

      - `description: string`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `name: string`

        - `type: "url"`

          - `"url"`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

          - `string`

        - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `BetaManagedAgentsEffortLow object { type }`

            Low effort. Favors latency over reasoning depth.

            - `type: "low"`

              - `"low"`

          - `BetaManagedAgentsEffortMedium object { type }`

            Medium effort. Balances latency and reasoning depth.

            - `type: "medium"`

              - `"medium"`

          - `BetaManagedAgentsEffortHigh object { type }`

            High effort. Favors reasoning depth.

            - `type: "high"`

              - `"high"`

          - `BetaManagedAgentsEffortXhigh object { type }`

            Extra-high effort. Not all models accept this level.

            - `type: "xhigh"`

              - `"xhigh"`

          - `BetaManagedAgentsEffortMax object { type }`

            Maximum effort. Favors reasoning depth over latency.

            - `type: "max"`

              - `"max"`

        - `speed: optional "standard" or "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: array of BetaManagedAgentsSessionThreadAgent`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `id: string`

          - `description: string`

          - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

            - `name: string`

            - `type: "url"`

            - `url: string`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `name: string`

          - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

            - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

              A resolved Anthropic-managed skill.

              - `skill_id: string`

              - `type: "anthropic"`

                - `"anthropic"`

              - `version: string`

            - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

              A resolved user-created custom skill.

              - `skill_id: string`

              - `type: "custom"`

                - `"custom"`

              - `version: string`

          - `system: string`

          - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

            - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

              - `configs: array of BetaManagedAgentsAgentToolConfig`

                - `enabled: boolean`

                - `name: "bash" or "edit" or "read" or 5 more`

                  Built-in agent tool identifier.

                  - `"bash"`

                  - `"edit"`

                  - `"read"`

                  - `"write"`

                  - `"glob"`

                  - `"grep"`

                  - `"web_fetch"`

                  - `"web_search"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

                    Tool calls are automatically approved without user confirmation.

                    - `type: "always_allow"`

                      - `"always_allow"`

                  - `BetaManagedAgentsAlwaysAskPolicy object { type }`

                    Tool calls require user confirmation before execution.

                    - `type: "always_ask"`

                      - `"always_ask"`

              - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `enabled: boolean`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

                    Tool calls are automatically approved without user confirmation.

                  - `BetaManagedAgentsAlwaysAskPolicy object { type }`

                    Tool calls require user confirmation before execution.

              - `type: "agent_toolset_20260401"`

                - `"agent_toolset_20260401"`

            - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

              - `configs: array of BetaManagedAgentsMCPToolConfig`

                - `enabled: boolean`

                - `name: string`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

                    Tool calls are automatically approved without user confirmation.

                  - `BetaManagedAgentsAlwaysAskPolicy object { type }`

                    Tool calls require user confirmation before execution.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: boolean`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

                    Tool calls are automatically approved without user confirmation.

                  - `BetaManagedAgentsAlwaysAskPolicy object { type }`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: string`

              - `type: "mcp_toolset"`

                - `"mcp_toolset"`

            - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

              A custom tool as returned in API responses.

              - `description: string`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: "object"`

                  - `"object"`

                - `properties: optional map[unknown]`

                - `required: optional array of string`

              - `name: string`

              - `type: "custom"`

                - `"custom"`

          - `type: "agent"`

            - `"agent"`

          - `version: number`

        - `type: "coordinator"`

          - `"coordinator"`

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

          A resolved Anthropic-managed skill.

        - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

          A resolved user-created custom skill.

      - `system: string`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

        - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

        - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

          A custom tool as returned in API responses.

      - `type: "agent"`

        - `"agent"`

      - `version: number`

    - `metadata: optional map[string]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: optional string`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsStartEvent object { event, type }`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `BetaManagedAgentsAgentMessagePreview object { id, type }`

        - `id: string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: "agent.message"`

          - `"agent.message"`

      - `BetaManagedAgentsAgentThinkingPreview object { id, type }`

        - `id: string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: "agent.thinking"`

          - `"agent.thinking"`

    - `type: "event_start"`

      - `"event_start"`

  - `BetaManagedAgentsDeltaEvent object { delta, event_id, type }`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: "content_delta"`

        - `"content_delta"`

      - `index: optional number`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `event_id: string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: "event_delta"`

      - `"event_delta"`

  - `BetaManagedAgentsSystemMessageEvent object { id, content, type, processed_at }`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `type: "system.message"`

      - `"system.message"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

# Events

## List Session Thread Events

**get** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

### Path Parameters

- `session_id: string`

- `thread_id: string`

### Query Parameters

- `limit: optional number`

  Query parameter for limit

- `page: optional string`

  Query parameter for page

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `data: optional array of BetaManagedAgentsSessionEvent`

  Events for the thread, ordered by `processed_at`.

  - `BetaManagedAgentsUserMessageEvent object { id, content, type, processed_at }`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `type: "user.message"`

      - `"user.message"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `BetaManagedAgentsUserInterruptEvent object { id, type, processed_at, session_thread_id }`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

      - `"user.interrupt"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

    - `session_thread_id: optional string`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEvent object { id, result, tool_use_id, 4 more }`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_confirmation"`

      - `"user.tool_confirmation"`

    - `deny_message: optional string`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

    - `session_thread_id: optional string`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `BetaManagedAgentsUserCustomToolResultEvent object { id, custom_tool_use_id, type, 4 more }`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

      - `"user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `source: string`

          The URL source of the search result.

        - `title: string`

          The title of the search result.

        - `type: "search_result"`

          - `"search_result"`

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

    - `session_thread_id: optional string`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsAgentCustomToolUseEvent object { id, input, name, 3 more }`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.custom_tool_use"`

      - `"agent.custom_tool_use"`

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `BetaManagedAgentsAgentMessageEvent object { id, content, processed_at, type }`

    An agent response event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock`

      Array of text blocks comprising the agent response.

      - `text: string`

        The text content.

      - `type: "text"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.message"`

      - `"agent.message"`

  - `BetaManagedAgentsAgentThinkingEvent object { id, processed_at, type }`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thinking"`

      - `"agent.thinking"`

  - `BetaManagedAgentsAgentMCPToolUseEvent object { id, input, mcp_server_name, 5 more }`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.mcp_tool_use"`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentMCPToolResultEvent object { id, mcp_tool_use_id, processed_at, 3 more }`

    Event representing the result of an MCP tool execution.

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.mcp_tool_result"`

      - `"agent.mcp_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentToolUseEvent object { id, input, name, 4 more }`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.tool_use"`

      - `"agent.tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentToolResultEvent object { id, processed_at, tool_use_id, 3 more }`

    Event representing the result of an agent tool execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: "agent.tool_result"`

      - `"agent.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentThreadMessageReceivedEvent object { id, content, from_session_thread_id, 3 more }`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Message content blocks.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `from_session_thread_id: string`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thread_message_received"`

      - `"agent.thread_message_received"`

    - `from_agent_name: optional string`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `BetaManagedAgentsAgentThreadMessageSentEvent object { id, content, processed_at, 3 more }`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Message content blocks.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: "agent.thread_message_sent"`

      - `"agent.thread_message_sent"`

    - `to_agent_name: optional string`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `BetaManagedAgentsAgentThreadContextCompactedEvent object { id, processed_at, type }`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thread_context_compacted"`

      - `"agent.thread_context_compacted"`

  - `BetaManagedAgentsSessionErrorEvent object { id, error, processed_at, type }`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 5 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `BetaManagedAgentsUnknownError object { message, retry_status, type }`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "unknown_error"`

          - `"unknown_error"`

      - `BetaManagedAgentsModelOverloadedError object { message, retry_status, type }`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_overloaded_error"`

          - `"model_overloaded_error"`

      - `BetaManagedAgentsModelRateLimitedError object { message, retry_status, type }`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_rate_limited_error"`

          - `"model_rate_limited_error"`

      - `BetaManagedAgentsModelRequestFailedError object { message, retry_status, type }`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_request_failed_error"`

          - `"model_request_failed_error"`

      - `BetaManagedAgentsMCPConnectionFailedError object { mcp_server_name, message, retry_status, type }`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_connection_failed_error"`

          - `"mcp_connection_failed_error"`

      - `BetaManagedAgentsMCPAuthenticationFailedError object { mcp_server_name, message, retry_status, type }`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_authentication_failed_error"`

          - `"mcp_authentication_failed_error"`

      - `BetaManagedAgentsBillingError object { message, retry_status, type }`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "billing_error"`

          - `"billing_error"`

      - `BetaManagedAgentsCredentialHostUnreachableError object { credential_id, message, retry_status, 2 more }`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "credential_host_unreachable_error"`

          - `"credential_host_unreachable_error"`

        - `vault_id: string`

          ID of the vault containing the affected credential.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.error"`

      - `"session.error"`

  - `BetaManagedAgentsSessionStatusRescheduledEvent object { id, processed_at, type }`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_rescheduled"`

      - `"session.status_rescheduled"`

  - `BetaManagedAgentsSessionStatusRunningEvent object { id, processed_at, type }`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_running"`

      - `"session.status_running"`

  - `BetaManagedAgentsSessionStatusIdleEvent object { id, processed_at, stop_reason, type }`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn object { type }`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

          - `"end_turn"`

      - `BetaManagedAgentsSessionRequiresAction object { event_ids, type }`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

          - `"requires_action"`

      - `BetaManagedAgentsSessionRetriesExhausted object { type }`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

          - `"retries_exhausted"`

    - `type: "session.status_idle"`

      - `"session.status_idle"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent object { id, processed_at, type }`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_terminated"`

      - `"session.status_terminated"`

  - `BetaManagedAgentsSessionThreadCreatedEvent object { id, agent_name, processed_at, 2 more }`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

    - `type: "session.thread_created"`

      - `"session.thread_created"`

  - `BetaManagedAgentsSpanOutcomeEvaluationStartEvent object { id, iteration, outcome_id, 2 more }`

    Emitted when an outcome evaluation cycle begins.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.outcome_evaluation_start"`

      - `"span.outcome_evaluation_start"`

  - `BetaManagedAgentsSpanOutcomeEvaluationEndEvent object { id, explanation, iteration, 6 more }`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: string`

      Unique identifier for this event.

    - `explanation: string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_evaluation_start_id: string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `result: string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: "span.outcome_evaluation_end"`

      - `"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

      - `input_tokens: number`

        Input tokens consumed by this request.

      - `output_tokens: number`

        Output tokens generated by this request.

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `BetaManagedAgentsSpanModelRequestStartEvent object { id, processed_at, type }`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_start"`

      - `"span.model_request_start"`

  - `BetaManagedAgentsSpanModelRequestEndEvent object { id, is_error, model_request_start_id, 3 more }`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_end"`

      - `"span.model_request_end"`

  - `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object { id, iteration, outcome_id, 2 more }`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.outcome_evaluation_ongoing"`

      - `"span.outcome_evaluation_ongoing"`

  - `BetaManagedAgentsUserDefineOutcomeEvent object { id, description, max_iterations, 4 more }`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: string`

      Unique identifier for this event.

    - `description: string`

      What the agent should produce. Copied from the input event.

    - `max_iterations: number`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `outcome_id: string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubric object { file_id, type }`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

          - `"file"`

      - `BetaManagedAgentsTextRubric object { content, type }`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: "text"`

          - `"text"`

    - `type: "user.define_outcome"`

      - `"user.define_outcome"`

  - `BetaManagedAgentsSessionDeletedEvent object { id, processed_at, type }`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.deleted"`

      - `"session.deleted"`

  - `BetaManagedAgentsSessionThreadStatusRunningEvent object { id, agent_name, processed_at, 2 more }`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

    - `type: "session.thread_status_running"`

      - `"session.thread_status_running"`

  - `BetaManagedAgentsSessionThreadStatusIdleEvent object { id, agent_name, processed_at, 3 more }`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn object { type }`

        The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionRequiresAction object { event_ids, type }`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `BetaManagedAgentsSessionRetriesExhausted object { type }`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

    - `type: "session.thread_status_idle"`

      - `"session.thread_status_idle"`

  - `BetaManagedAgentsSessionThreadStatusTerminatedEvent object { id, agent_name, processed_at, 2 more }`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

    - `type: "session.thread_status_terminated"`

      - `"session.thread_status_terminated"`

  - `BetaManagedAgentsUserToolResultEvent object { id, tool_use_id, type, 4 more }`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_result"`

      - `"user.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

    - `session_thread_id: optional string`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsSessionThreadStatusRescheduledEvent object { id, agent_name, processed_at, 2 more }`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

    - `type: "session.thread_status_rescheduled"`

      - `"session.thread_status_rescheduled"`

  - `BetaManagedAgentsSessionUpdatedEvent object { id, processed_at, type, 3 more }`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.updated"`

      - `"session.updated"`

    - `agent: optional BetaManagedAgentsSessionAgent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: string`

      - `description: string`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `name: string`

        - `type: "url"`

          - `"url"`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

          - `string`

        - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `BetaManagedAgentsEffortLow object { type }`

            Low effort. Favors latency over reasoning depth.

            - `type: "low"`

              - `"low"`

          - `BetaManagedAgentsEffortMedium object { type }`

            Medium effort. Balances latency and reasoning depth.

            - `type: "medium"`

              - `"medium"`

          - `BetaManagedAgentsEffortHigh object { type }`

            High effort. Favors reasoning depth.

            - `type: "high"`

              - `"high"`

          - `BetaManagedAgentsEffortXhigh object { type }`

            Extra-high effort. Not all models accept this level.

            - `type: "xhigh"`

              - `"xhigh"`

          - `BetaManagedAgentsEffortMax object { type }`

            Maximum effort. Favors reasoning depth over latency.

            - `type: "max"`

              - `"max"`

        - `speed: optional "standard" or "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: array of BetaManagedAgentsSessionThreadAgent`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `id: string`

          - `description: string`

          - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

            - `name: string`

            - `type: "url"`

            - `url: string`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `name: string`

          - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

            - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

              A resolved Anthropic-managed skill.

              - `skill_id: string`

              - `type: "anthropic"`

                - `"anthropic"`

              - `version: string`

            - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

              A resolved user-created custom skill.

              - `skill_id: string`

              - `type: "custom"`

                - `"custom"`

              - `version: string`

          - `system: string`

          - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

            - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

              - `configs: array of BetaManagedAgentsAgentToolConfig`

                - `enabled: boolean`

                - `name: "bash" or "edit" or "read" or 5 more`

                  Built-in agent tool identifier.

                  - `"bash"`

                  - `"edit"`

                  - `"read"`

                  - `"write"`

                  - `"glob"`

                  - `"grep"`

                  - `"web_fetch"`

                  - `"web_search"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

                    Tool calls are automatically approved without user confirmation.

                    - `type: "always_allow"`

                      - `"always_allow"`

                  - `BetaManagedAgentsAlwaysAskPolicy object { type }`

                    Tool calls require user confirmation before execution.

                    - `type: "always_ask"`

                      - `"always_ask"`

              - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `enabled: boolean`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

                    Tool calls are automatically approved without user confirmation.

                  - `BetaManagedAgentsAlwaysAskPolicy object { type }`

                    Tool calls require user confirmation before execution.

              - `type: "agent_toolset_20260401"`

                - `"agent_toolset_20260401"`

            - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

              - `configs: array of BetaManagedAgentsMCPToolConfig`

                - `enabled: boolean`

                - `name: string`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

                    Tool calls are automatically approved without user confirmation.

                  - `BetaManagedAgentsAlwaysAskPolicy object { type }`

                    Tool calls require user confirmation before execution.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: boolean`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

                    Tool calls are automatically approved without user confirmation.

                  - `BetaManagedAgentsAlwaysAskPolicy object { type }`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: string`

              - `type: "mcp_toolset"`

                - `"mcp_toolset"`

            - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

              A custom tool as returned in API responses.

              - `description: string`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: "object"`

                  - `"object"`

                - `properties: optional map[unknown]`

                - `required: optional array of string`

              - `name: string`

              - `type: "custom"`

                - `"custom"`

          - `type: "agent"`

            - `"agent"`

          - `version: number`

        - `type: "coordinator"`

          - `"coordinator"`

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

          A resolved Anthropic-managed skill.

        - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

          A resolved user-created custom skill.

      - `system: string`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

        - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

        - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

          A custom tool as returned in API responses.

      - `type: "agent"`

        - `"agent"`

      - `version: number`

    - `metadata: optional map[string]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: optional string`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsSystemMessageEvent object { id, content, type, processed_at }`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `type: "system.message"`

      - `"system.message"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

- `next_page: optional string`

  Opaque cursor for the next page. Null when no more results.

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID/events \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

### Path Parameters

- `session_id: string`

- `thread_id: string`

### Query Parameters

- `event_deltas: optional array of BetaManagedAgentsDeltaType`

  When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

  - `"agent.message"`

  - `"agent.thinking"`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsStreamSessionThreadEvents = BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 33 more`

  Server-sent event in a single thread's stream.

  - `BetaManagedAgentsUserMessageEvent object { id, content, type, processed_at }`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `type: "user.message"`

      - `"user.message"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `BetaManagedAgentsUserInterruptEvent object { id, type, processed_at, session_thread_id }`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

      - `"user.interrupt"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

    - `session_thread_id: optional string`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEvent object { id, result, tool_use_id, 4 more }`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_confirmation"`

      - `"user.tool_confirmation"`

    - `deny_message: optional string`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

    - `session_thread_id: optional string`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `BetaManagedAgentsUserCustomToolResultEvent object { id, custom_tool_use_id, type, 4 more }`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

      - `"user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `source: string`

          The URL source of the search result.

        - `title: string`

          The title of the search result.

        - `type: "search_result"`

          - `"search_result"`

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

    - `session_thread_id: optional string`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsAgentCustomToolUseEvent object { id, input, name, 3 more }`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.custom_tool_use"`

      - `"agent.custom_tool_use"`

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `BetaManagedAgentsAgentMessageEvent object { id, content, processed_at, type }`

    An agent response event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock`

      Array of text blocks comprising the agent response.

      - `text: string`

        The text content.

      - `type: "text"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.message"`

      - `"agent.message"`

  - `BetaManagedAgentsAgentThinkingEvent object { id, processed_at, type }`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thinking"`

      - `"agent.thinking"`

  - `BetaManagedAgentsAgentMCPToolUseEvent object { id, input, mcp_server_name, 5 more }`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.mcp_tool_use"`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentMCPToolResultEvent object { id, mcp_tool_use_id, processed_at, 3 more }`

    Event representing the result of an MCP tool execution.

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.mcp_tool_result"`

      - `"agent.mcp_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentToolUseEvent object { id, input, name, 4 more }`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.tool_use"`

      - `"agent.tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentToolResultEvent object { id, processed_at, tool_use_id, 3 more }`

    Event representing the result of an agent tool execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: "agent.tool_result"`

      - `"agent.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentThreadMessageReceivedEvent object { id, content, from_session_thread_id, 3 more }`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Message content blocks.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `from_session_thread_id: string`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thread_message_received"`

      - `"agent.thread_message_received"`

    - `from_agent_name: optional string`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `BetaManagedAgentsAgentThreadMessageSentEvent object { id, content, processed_at, 3 more }`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Message content blocks.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: "agent.thread_message_sent"`

      - `"agent.thread_message_sent"`

    - `to_agent_name: optional string`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `BetaManagedAgentsAgentThreadContextCompactedEvent object { id, processed_at, type }`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thread_context_compacted"`

      - `"agent.thread_context_compacted"`

  - `BetaManagedAgentsSessionErrorEvent object { id, error, processed_at, type }`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 5 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `BetaManagedAgentsUnknownError object { message, retry_status, type }`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "unknown_error"`

          - `"unknown_error"`

      - `BetaManagedAgentsModelOverloadedError object { message, retry_status, type }`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_overloaded_error"`

          - `"model_overloaded_error"`

      - `BetaManagedAgentsModelRateLimitedError object { message, retry_status, type }`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_rate_limited_error"`

          - `"model_rate_limited_error"`

      - `BetaManagedAgentsModelRequestFailedError object { message, retry_status, type }`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_request_failed_error"`

          - `"model_request_failed_error"`

      - `BetaManagedAgentsMCPConnectionFailedError object { mcp_server_name, message, retry_status, type }`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_connection_failed_error"`

          - `"mcp_connection_failed_error"`

      - `BetaManagedAgentsMCPAuthenticationFailedError object { mcp_server_name, message, retry_status, type }`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_authentication_failed_error"`

          - `"mcp_authentication_failed_error"`

      - `BetaManagedAgentsBillingError object { message, retry_status, type }`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "billing_error"`

          - `"billing_error"`

      - `BetaManagedAgentsCredentialHostUnreachableError object { credential_id, message, retry_status, 2 more }`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "credential_host_unreachable_error"`

          - `"credential_host_unreachable_error"`

        - `vault_id: string`

          ID of the vault containing the affected credential.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.error"`

      - `"session.error"`

  - `BetaManagedAgentsSessionStatusRescheduledEvent object { id, processed_at, type }`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_rescheduled"`

      - `"session.status_rescheduled"`

  - `BetaManagedAgentsSessionStatusRunningEvent object { id, processed_at, type }`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_running"`

      - `"session.status_running"`

  - `BetaManagedAgentsSessionStatusIdleEvent object { id, processed_at, stop_reason, type }`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn object { type }`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

          - `"end_turn"`

      - `BetaManagedAgentsSessionRequiresAction object { event_ids, type }`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

          - `"requires_action"`

      - `BetaManagedAgentsSessionRetriesExhausted object { type }`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

          - `"retries_exhausted"`

    - `type: "session.status_idle"`

      - `"session.status_idle"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent object { id, processed_at, type }`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_terminated"`

      - `"session.status_terminated"`

  - `BetaManagedAgentsSessionThreadCreatedEvent object { id, agent_name, processed_at, 2 more }`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

    - `type: "session.thread_created"`

      - `"session.thread_created"`

  - `BetaManagedAgentsSpanOutcomeEvaluationStartEvent object { id, iteration, outcome_id, 2 more }`

    Emitted when an outcome evaluation cycle begins.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.outcome_evaluation_start"`

      - `"span.outcome_evaluation_start"`

  - `BetaManagedAgentsSpanOutcomeEvaluationEndEvent object { id, explanation, iteration, 6 more }`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: string`

      Unique identifier for this event.

    - `explanation: string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_evaluation_start_id: string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `result: string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: "span.outcome_evaluation_end"`

      - `"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

      - `input_tokens: number`

        Input tokens consumed by this request.

      - `output_tokens: number`

        Output tokens generated by this request.

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `BetaManagedAgentsSpanModelRequestStartEvent object { id, processed_at, type }`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_start"`

      - `"span.model_request_start"`

  - `BetaManagedAgentsSpanModelRequestEndEvent object { id, is_error, model_request_start_id, 3 more }`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_end"`

      - `"span.model_request_end"`

  - `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object { id, iteration, outcome_id, 2 more }`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.outcome_evaluation_ongoing"`

      - `"span.outcome_evaluation_ongoing"`

  - `BetaManagedAgentsUserDefineOutcomeEvent object { id, description, max_iterations, 4 more }`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: string`

      Unique identifier for this event.

    - `description: string`

      What the agent should produce. Copied from the input event.

    - `max_iterations: number`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `outcome_id: string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubric object { file_id, type }`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

          - `"file"`

      - `BetaManagedAgentsTextRubric object { content, type }`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: "text"`

          - `"text"`

    - `type: "user.define_outcome"`

      - `"user.define_outcome"`

  - `BetaManagedAgentsSessionDeletedEvent object { id, processed_at, type }`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.deleted"`

      - `"session.deleted"`

  - `BetaManagedAgentsSessionThreadStatusRunningEvent object { id, agent_name, processed_at, 2 more }`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

    - `type: "session.thread_status_running"`

      - `"session.thread_status_running"`

  - `BetaManagedAgentsSessionThreadStatusIdleEvent object { id, agent_name, processed_at, 3 more }`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn object { type }`

        The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionRequiresAction object { event_ids, type }`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `BetaManagedAgentsSessionRetriesExhausted object { type }`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

    - `type: "session.thread_status_idle"`

      - `"session.thread_status_idle"`

  - `BetaManagedAgentsSessionThreadStatusTerminatedEvent object { id, agent_name, processed_at, 2 more }`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

    - `type: "session.thread_status_terminated"`

      - `"session.thread_status_terminated"`

  - `BetaManagedAgentsUserToolResultEvent object { id, tool_use_id, type, 4 more }`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_result"`

      - `"user.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

    - `session_thread_id: optional string`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsSessionThreadStatusRescheduledEvent object { id, agent_name, processed_at, 2 more }`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

    - `type: "session.thread_status_rescheduled"`

      - `"session.thread_status_rescheduled"`

  - `BetaManagedAgentsSessionUpdatedEvent object { id, processed_at, type, 3 more }`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.updated"`

      - `"session.updated"`

    - `agent: optional BetaManagedAgentsSessionAgent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: string`

      - `description: string`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `name: string`

        - `type: "url"`

          - `"url"`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

          - `string`

        - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `BetaManagedAgentsEffortLow object { type }`

            Low effort. Favors latency over reasoning depth.

            - `type: "low"`

              - `"low"`

          - `BetaManagedAgentsEffortMedium object { type }`

            Medium effort. Balances latency and reasoning depth.

            - `type: "medium"`

              - `"medium"`

          - `BetaManagedAgentsEffortHigh object { type }`

            High effort. Favors reasoning depth.

            - `type: "high"`

              - `"high"`

          - `BetaManagedAgentsEffortXhigh object { type }`

            Extra-high effort. Not all models accept this level.

            - `type: "xhigh"`

              - `"xhigh"`

          - `BetaManagedAgentsEffortMax object { type }`

            Maximum effort. Favors reasoning depth over latency.

            - `type: "max"`

              - `"max"`

        - `speed: optional "standard" or "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: array of BetaManagedAgentsSessionThreadAgent`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `id: string`

          - `description: string`

          - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

            - `name: string`

            - `type: "url"`

            - `url: string`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `name: string`

          - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

            - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

              A resolved Anthropic-managed skill.

              - `skill_id: string`

              - `type: "anthropic"`

                - `"anthropic"`

              - `version: string`

            - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

              A resolved user-created custom skill.

              - `skill_id: string`

              - `type: "custom"`

                - `"custom"`

              - `version: string`

          - `system: string`

          - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

            - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

              - `configs: array of BetaManagedAgentsAgentToolConfig`

                - `enabled: boolean`

                - `name: "bash" or "edit" or "read" or 5 more`

                  Built-in agent tool identifier.

                  - `"bash"`

                  - `"edit"`

                  - `"read"`

                  - `"write"`

                  - `"glob"`

                  - `"grep"`

                  - `"web_fetch"`

                  - `"web_search"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

                    Tool calls are automatically approved without user confirmation.

                    - `type: "always_allow"`

                      - `"always_allow"`

                  - `BetaManagedAgentsAlwaysAskPolicy object { type }`

                    Tool calls require user confirmation before execution.

                    - `type: "always_ask"`

                      - `"always_ask"`

              - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `enabled: boolean`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

                    Tool calls are automatically approved without user confirmation.

                  - `BetaManagedAgentsAlwaysAskPolicy object { type }`

                    Tool calls require user confirmation before execution.

              - `type: "agent_toolset_20260401"`

                - `"agent_toolset_20260401"`

            - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

              - `configs: array of BetaManagedAgentsMCPToolConfig`

                - `enabled: boolean`

                - `name: string`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

                    Tool calls are automatically approved without user confirmation.

                  - `BetaManagedAgentsAlwaysAskPolicy object { type }`

                    Tool calls require user confirmation before execution.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: boolean`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

                    Tool calls are automatically approved without user confirmation.

                  - `BetaManagedAgentsAlwaysAskPolicy object { type }`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: string`

              - `type: "mcp_toolset"`

                - `"mcp_toolset"`

            - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

              A custom tool as returned in API responses.

              - `description: string`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: "object"`

                  - `"object"`

                - `properties: optional map[unknown]`

                - `required: optional array of string`

              - `name: string`

              - `type: "custom"`

                - `"custom"`

          - `type: "agent"`

            - `"agent"`

          - `version: number`

        - `type: "coordinator"`

          - `"coordinator"`

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

          A resolved Anthropic-managed skill.

        - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

          A resolved user-created custom skill.

      - `system: string`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

        - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

        - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

          A custom tool as returned in API responses.

      - `type: "agent"`

        - `"agent"`

      - `version: number`

    - `metadata: optional map[string]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: optional string`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsStartEvent object { event, type }`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `BetaManagedAgentsAgentMessagePreview object { id, type }`

        - `id: string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: "agent.message"`

          - `"agent.message"`

      - `BetaManagedAgentsAgentThinkingPreview object { id, type }`

        - `id: string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: "agent.thinking"`

          - `"agent.thinking"`

    - `type: "event_start"`

      - `"event_start"`

  - `BetaManagedAgentsDeltaEvent object { delta, event_id, type }`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: "content_delta"`

        - `"content_delta"`

      - `index: optional number`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `event_id: string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: "event_delta"`

      - `"event_delta"`

  - `BetaManagedAgentsSystemMessageEvent object { id, content, type, processed_at }`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `type: "system.message"`

      - `"system.message"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID/stream \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/deployments`

Create Deployment

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `agent: string or BetaManagedAgentsAgentParams`

  Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

  - `string`

  - `BetaManagedAgentsAgentParams object { id, type, version }`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `id: string`

      The `agent` ID.

    - `type: "agent"`

      - `"agent"`

    - `version: optional number`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

- `environment_id: string`

  ID of the `environment` defining the container configuration for sessions created from this deployment.

- `initial_events: array of BetaManagedAgentsDeploymentInitialEventParams`

  Events to send to each session immediately after creation. At least 1, maximum 50.

  - `BetaManagedAgentsUserMessageEventParams object { content, type }`

    Parameters for sending a user message to the session.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks for the user message.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `type: "user.message"`

      - `"user.message"`

  - `BetaManagedAgentsUserDefineOutcomeEventParams object { description, rubric, type, max_iterations }`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: string`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubricParams or BetaManagedAgentsTextRubricParams`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubricParams object { file_id, type }`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

          - `"file"`

      - `BetaManagedAgentsTextRubricParams object { content, type }`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `type: "text"`

          - `"text"`

    - `type: "user.define_outcome"`

      - `"user.define_outcome"`

    - `max_iterations: optional number`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `BetaManagedAgentsSystemMessageEventParams object { content, type }`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `type: "system.message"`

      - `"system.message"`

- `name: string`

  Human-readable name for the deployment.

- `description: optional string`

  Description of what the deployment does.

- `metadata: optional map[string]`

  Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `resources: optional array of BetaManagedAgentsGitHubRepositoryResourceParams or BetaManagedAgentsFileResourceParams or BetaManagedAgentsMemoryStoreResourceParam`

  Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

  - `BetaManagedAgentsGitHubRepositoryResourceParams object { authorization_token, type, url, 2 more }`

    Mount a GitHub repository into the session's container.

    - `authorization_token: string`

      GitHub authorization token used to clone the repository.

    - `type: "github_repository"`

      - `"github_repository"`

    - `url: string`

      Github URL of the repository

    - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `BetaManagedAgentsBranchCheckout object { name, type }`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `BetaManagedAgentsCommitCheckout object { sha, type }`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

    - `mount_path: optional string`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `BetaManagedAgentsFileResourceParams object { file_id, type, mount_path }`

    Mount a file uploaded via the Files API into the session.

    - `file_id: string`

      ID of a previously uploaded file.

    - `type: "file"`

      - `"file"`

    - `mount_path: optional string`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `BetaManagedAgentsMemoryStoreResourceParam object { memory_store_id, type, access, instructions }`

    Parameters for attaching a memory store to an agent session.

    - `memory_store_id: string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: "memory_store"`

      - `"memory_store"`

    - `access: optional "read_write" or "read_only"`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `instructions: optional string`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

- `schedule: optional BetaManagedAgentsScheduleParams`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: string`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `type: "cron"`

    - `"cron"`

- `vault_ids: optional array of string`

  Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

### Returns

- `BetaManagedAgentsDeployment object { id, agent, archived_at, 13 more }`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent object { content, type }`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent object { description, rubric, type, max_iterations }`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric object { file_id, type }`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubric object { content, type }`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsDeploymentSystemMessageEvent object { content, type }`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `BetaManagedAgentsManualDeploymentPausedReason object { type }`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason object { error, type }`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type }`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type }`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type }`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type }`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type }`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type }`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type }`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type }`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type }`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError object { type }`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type }`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type }`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig object { type, url, checkout, mount_path }`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig object { file_id, type, mount_path }`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig object { memory_store_id, type, access, instructions }`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```http
curl https://api.anthropic.com/v1/deployments \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "agent": "string",
          "environment_id": "x",
          "initial_events": [
            {
              "content": [
                {
                  "text": "Where is my order #1234?",
                  "type": "text"
                }
              ],
              "type": "user.message"
            }
          ],
          "name": "x"
        }'
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

**get** `/v1/deployments`

List Deployments

### Query Parameters

- `agent_id: optional string`

  Filter by agent ID.

- `"created_at[gte]": optional string`

  Return deployments created at or after this time (inclusive).

- `"created_at[lte]": optional string`

  Return deployments created at or before this time (inclusive).

- `include_archived: optional boolean`

  When true, includes archived deployments. Default: false (exclude archived).

- `limit: optional number`

  Maximum results per page. Default 20, maximum 100.

- `page: optional string`

  Opaque pagination cursor.

- `status: optional BetaManagedAgentsDeploymentStatus`

  Filter by status: active or paused. Omit for both. To include archived deployments, use include_archived instead; the two cannot be combined.

  - `"active"`

  - `"paused"`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `data: array of BetaManagedAgentsDeployment`

  List of deployments.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent object { content, type }`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent object { description, rubric, type, max_iterations }`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric object { file_id, type }`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubric object { content, type }`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsDeploymentSystemMessageEvent object { content, type }`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `BetaManagedAgentsManualDeploymentPausedReason object { type }`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason object { error, type }`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type }`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type }`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type }`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type }`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type }`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type }`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type }`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type }`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type }`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError object { type }`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type }`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type }`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig object { type, url, checkout, mount_path }`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig object { file_id, type, mount_path }`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig object { memory_store_id, type, access, instructions }`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

- `next_page: optional string`

  Opaque cursor for the next page. Null when no more results.

### Example

```http
curl https://api.anthropic.com/v1/deployments \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/deployments/{deployment_id}`

Get Deployment

### Path Parameters

- `deployment_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsDeployment object { id, agent, archived_at, 13 more }`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent object { content, type }`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent object { description, rubric, type, max_iterations }`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric object { file_id, type }`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubric object { content, type }`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsDeploymentSystemMessageEvent object { content, type }`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `BetaManagedAgentsManualDeploymentPausedReason object { type }`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason object { error, type }`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type }`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type }`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type }`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type }`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type }`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type }`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type }`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type }`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type }`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError object { type }`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type }`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type }`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig object { type, url, checkout, mount_path }`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig object { file_id, type, mount_path }`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig object { memory_store_id, type, access, instructions }`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```http
curl https://api.anthropic.com/v1/deployments/$DEPLOYMENT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/deployments/{deployment_id}`

Update Deployment

### Path Parameters

- `deployment_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `agent: optional string or BetaManagedAgentsAgentParams`

  Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

  - `string`

  - `BetaManagedAgentsAgentParams object { id, type, version }`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `id: string`

      The `agent` ID.

    - `type: "agent"`

      - `"agent"`

    - `version: optional number`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

- `description: optional string`

  Description. Omit to preserve; send empty string or null to clear.

- `environment_id: optional string`

  ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

- `initial_events: optional array of BetaManagedAgentsDeploymentInitialEventParams`

  Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

  - `BetaManagedAgentsUserMessageEventParams object { content, type }`

    Parameters for sending a user message to the session.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks for the user message.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `type: "user.message"`

      - `"user.message"`

  - `BetaManagedAgentsUserDefineOutcomeEventParams object { description, rubric, type, max_iterations }`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: string`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubricParams or BetaManagedAgentsTextRubricParams`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubricParams object { file_id, type }`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

          - `"file"`

      - `BetaManagedAgentsTextRubricParams object { content, type }`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `type: "text"`

          - `"text"`

    - `type: "user.define_outcome"`

      - `"user.define_outcome"`

    - `max_iterations: optional number`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `BetaManagedAgentsSystemMessageEventParams object { content, type }`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `type: "system.message"`

      - `"system.message"`

- `metadata: optional map[string]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `name: optional string`

  Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

- `resources: optional array of BetaManagedAgentsGitHubRepositoryResourceParams or BetaManagedAgentsFileResourceParams or BetaManagedAgentsMemoryStoreResourceParam`

  Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

  - `BetaManagedAgentsGitHubRepositoryResourceParams object { authorization_token, type, url, 2 more }`

    Mount a GitHub repository into the session's container.

    - `authorization_token: string`

      GitHub authorization token used to clone the repository.

    - `type: "github_repository"`

      - `"github_repository"`

    - `url: string`

      Github URL of the repository

    - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `BetaManagedAgentsBranchCheckout object { name, type }`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `BetaManagedAgentsCommitCheckout object { sha, type }`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

    - `mount_path: optional string`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `BetaManagedAgentsFileResourceParams object { file_id, type, mount_path }`

    Mount a file uploaded via the Files API into the session.

    - `file_id: string`

      ID of a previously uploaded file.

    - `type: "file"`

      - `"file"`

    - `mount_path: optional string`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `BetaManagedAgentsMemoryStoreResourceParam object { memory_store_id, type, access, instructions }`

    Parameters for attaching a memory store to an agent session.

    - `memory_store_id: string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: "memory_store"`

      - `"memory_store"`

    - `access: optional "read_write" or "read_only"`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `instructions: optional string`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

- `schedule: optional BetaManagedAgentsScheduleParams`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: string`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `type: "cron"`

    - `"cron"`

- `vault_ids: optional array of string`

  Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

### Returns

- `BetaManagedAgentsDeployment object { id, agent, archived_at, 13 more }`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent object { content, type }`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent object { description, rubric, type, max_iterations }`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric object { file_id, type }`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubric object { content, type }`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsDeploymentSystemMessageEvent object { content, type }`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `BetaManagedAgentsManualDeploymentPausedReason object { type }`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason object { error, type }`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type }`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type }`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type }`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type }`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type }`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type }`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type }`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type }`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type }`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError object { type }`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type }`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type }`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig object { type, url, checkout, mount_path }`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig object { file_id, type, mount_path }`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig object { memory_store_id, type, access, instructions }`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```http
curl https://api.anthropic.com/v1/deployments/$DEPLOYMENT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
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

**post** `/v1/deployments/{deployment_id}/archive`

Archive Deployment

### Path Parameters

- `deployment_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsDeployment object { id, agent, archived_at, 13 more }`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent object { content, type }`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent object { description, rubric, type, max_iterations }`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric object { file_id, type }`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubric object { content, type }`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsDeploymentSystemMessageEvent object { content, type }`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `BetaManagedAgentsManualDeploymentPausedReason object { type }`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason object { error, type }`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type }`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type }`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type }`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type }`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type }`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type }`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type }`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type }`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type }`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError object { type }`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type }`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type }`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig object { type, url, checkout, mount_path }`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig object { file_id, type, mount_path }`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig object { memory_store_id, type, access, instructions }`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```http
curl https://api.anthropic.com/v1/deployments/$DEPLOYMENT_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

### Path Parameters

- `deployment_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsDeploymentRun object { id, agent, created_at, 5 more }`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: string`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `deployment_id: string`

    ID of the deployment that produced this run.

  - `error: BetaManagedAgentsEnvironmentArchivedRunError or BetaManagedAgentsAgentArchivedRunError or BetaManagedAgentsEnvironmentNotFoundRunError or 13 more`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `BetaManagedAgentsEnvironmentArchivedRunError object { message, type }`

      The deployment's environment was archived.

      - `message: string`

        Human-readable error description.

      - `type: "environment_archived_error"`

        - `"environment_archived_error"`

    - `BetaManagedAgentsAgentArchivedRunError object { message, type }`

      The deployment's agent was archived.

      - `message: string`

        Human-readable error description.

      - `type: "agent_archived_error"`

        - `"agent_archived_error"`

    - `BetaManagedAgentsEnvironmentNotFoundRunError object { message, type }`

      The deployment's environment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "environment_not_found_error"`

        - `"environment_not_found_error"`

    - `BetaManagedAgentsVaultNotFoundRunError object { message, type }`

      A vault referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "vault_not_found_error"`

        - `"vault_not_found_error"`

    - `BetaManagedAgentsVaultArchivedRunError object { message, type }`

      A vault referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "vault_archived_error"`

        - `"vault_archived_error"`

    - `BetaManagedAgentsFileNotFoundRunError object { message, type }`

      A file resource referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "file_not_found_error"`

        - `"file_not_found_error"`

    - `BetaManagedAgentsMemoryStoreArchivedRunError object { message, type }`

      A memory store referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "memory_store_archived_error"`

        - `"memory_store_archived_error"`

    - `BetaManagedAgentsSkillNotFoundRunError object { message, type }`

      A skill referenced by the deployment's agent no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "skill_not_found_error"`

        - `"skill_not_found_error"`

    - `BetaManagedAgentsSessionResourceNotFoundRunError object { message, type }`

      A referenced resource no longer exists and its kind was not reported.

      - `message: string`

        Human-readable error description.

      - `type: "session_resource_not_found_error"`

        - `"session_resource_not_found_error"`

    - `BetaManagedAgentsWorkspaceArchivedRunError object { message, type }`

      The deployment's workspace was archived.

      - `message: string`

        Human-readable error description.

      - `type: "workspace_archived_error"`

        - `"workspace_archived_error"`

    - `BetaManagedAgentsOrganizationDisabledRunError object { message, type }`

      The deployment's organization is disabled.

      - `message: string`

        Human-readable error description.

      - `type: "organization_disabled_error"`

        - `"organization_disabled_error"`

    - `BetaManagedAgentsSessionRateLimitedRunError object { message, type }`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: string`

        Human-readable error description.

      - `type: "session_rate_limited_error"`

        - `"session_rate_limited_error"`

    - `BetaManagedAgentsSessionCreationRejectedRunError object { message, type }`

      The session create request was rejected with a non-retryable validation error.

      - `message: string`

        Human-readable error description.

      - `type: "session_creation_rejected_error"`

        - `"session_creation_rejected_error"`

    - `BetaManagedAgentsUnknownRunError object { message, type }`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: string`

        Human-readable error description.

      - `type: "unknown_error"`

        - `"unknown_error"`

    - `BetaManagedAgentsSelfHostedResourcesUnsupportedRunError object { message, type }`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: string`

        Human-readable error description.

      - `type: "self_hosted_resources_unsupported_error"`

        - `"self_hosted_resources_unsupported_error"`

    - `BetaManagedAgentsMCPEgressBlockedRunError object { message, type }`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: string`

        Human-readable error description.

      - `type: "mcp_egress_blocked_error"`

        - `"mcp_egress_blocked_error"`

  - `session_id: string`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `BetaManagedAgentsScheduleTriggerContext object { scheduled_at, type }`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: string`

        A timestamp in RFC 3339 format

      - `type: "schedule"`

        - `"schedule"`

    - `BetaManagedAgentsManualTriggerContext object { type }`

      The run was started manually by creating a session directly against the deployment.

      - `type: "manual"`

        - `"manual"`

  - `type: "deployment_run"`

    - `"deployment_run"`

### Example

```http
curl https://api.anthropic.com/v1/deployments/$DEPLOYMENT_ID/run \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/deployments/{deployment_id}/pause`

Pause Deployment

### Path Parameters

- `deployment_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsDeployment object { id, agent, archived_at, 13 more }`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent object { content, type }`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent object { description, rubric, type, max_iterations }`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric object { file_id, type }`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubric object { content, type }`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsDeploymentSystemMessageEvent object { content, type }`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `BetaManagedAgentsManualDeploymentPausedReason object { type }`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason object { error, type }`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type }`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type }`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type }`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type }`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type }`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type }`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type }`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type }`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type }`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError object { type }`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type }`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type }`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig object { type, url, checkout, mount_path }`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig object { file_id, type, mount_path }`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig object { memory_store_id, type, access, instructions }`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```http
curl https://api.anthropic.com/v1/deployments/$DEPLOYMENT_ID/pause \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

### Path Parameters

- `deployment_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsDeployment object { id, agent, archived_at, 13 more }`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent object { content, type }`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent object { description, rubric, type, max_iterations }`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric object { file_id, type }`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubric object { content, type }`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsDeploymentSystemMessageEvent object { content, type }`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `BetaManagedAgentsManualDeploymentPausedReason object { type }`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason object { error, type }`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type }`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type }`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type }`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type }`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type }`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type }`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type }`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type }`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type }`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError object { type }`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type }`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type }`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig object { type, url, checkout, mount_path }`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig object { file_id, type, mount_path }`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig object { memory_store_id, type, access, instructions }`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```http
curl https://api.anthropic.com/v1/deployments/$DEPLOYMENT_ID/unpause \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type }`

  The deployment's agent was archived.

  - `type: "agent_archived_error"`

    - `"agent_archived_error"`

### Beta Managed Agents Cron Schedule

- `BetaManagedAgentsCronSchedule object { expression, timezone, type, 2 more }`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: string`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `type: "cron"`

    - `"cron"`

  - `last_run_at: optional string`

    A timestamp in RFC 3339 format

  - `upcoming_runs_at: optional array of string`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Cron Schedule Params

- `BetaManagedAgentsCronScheduleParams object { expression, timezone, type }`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: string`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `type: "cron"`

    - `"cron"`

### Beta Managed Agents Deployment

- `BetaManagedAgentsDeployment object { id, agent, archived_at, 13 more }`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent object { content, type }`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent object { description, rubric, type, max_iterations }`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric object { file_id, type }`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubric object { content, type }`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsDeploymentSystemMessageEvent object { content, type }`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `BetaManagedAgentsManualDeploymentPausedReason object { type }`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason object { error, type }`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type }`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type }`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type }`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type }`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type }`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type }`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type }`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type }`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type }`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError object { type }`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type }`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type }`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig object { type, url, checkout, mount_path }`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig object { file_id, type, mount_path }`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig object { memory_store_id, type, access, instructions }`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Beta Managed Agents Deployment Initial Event

- `BetaManagedAgentsDeploymentInitialEvent = BetaManagedAgentsDeploymentUserMessageEvent or BetaManagedAgentsDeploymentUserDefineOutcomeEvent or BetaManagedAgentsDeploymentSystemMessageEvent`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `BetaManagedAgentsDeploymentUserMessageEvent object { content, type }`

    A user message sent to the session.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks for the user message.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `type: "user.message"`

      - `"user.message"`

  - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent object { description, rubric, type, max_iterations }`

    An outcome the agent should work toward. The agent begins work on receipt.

    - `description: string`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubric object { file_id, type }`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

          - `"file"`

      - `BetaManagedAgentsTextRubric object { content, type }`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: "text"`

          - `"text"`

    - `type: "user.define_outcome"`

      - `"user.define_outcome"`

    - `max_iterations: optional number`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `BetaManagedAgentsDeploymentSystemMessageEvent object { content, type }`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `type: "system.message"`

      - `"system.message"`

### Beta Managed Agents Deployment Initial Event Params

- `BetaManagedAgentsDeploymentInitialEventParams = BetaManagedAgentsUserMessageEventParams or BetaManagedAgentsUserDefineOutcomeEventParams or BetaManagedAgentsSystemMessageEventParams`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `BetaManagedAgentsUserMessageEventParams object { content, type }`

    Parameters for sending a user message to the session.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks for the user message.

      - `BetaManagedAgentsTextBlock object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `type: "user.message"`

      - `"user.message"`

  - `BetaManagedAgentsUserDefineOutcomeEventParams object { description, rubric, type, max_iterations }`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: string`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubricParams or BetaManagedAgentsTextRubricParams`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubricParams object { file_id, type }`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

          - `"file"`

      - `BetaManagedAgentsTextRubricParams object { content, type }`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `type: "text"`

          - `"text"`

    - `type: "user.define_outcome"`

      - `"user.define_outcome"`

    - `max_iterations: optional number`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `BetaManagedAgentsSystemMessageEventParams object { content, type }`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `type: "system.message"`

      - `"system.message"`

### Beta Managed Agents Deployment Paused Reason

- `BetaManagedAgentsDeploymentPausedReason = BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

  Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `BetaManagedAgentsManualDeploymentPausedReason object { type }`

    The caller invoked the pause endpoint on the deployment.

    - `type: "manual"`

      - `"manual"`

  - `BetaManagedAgentsErrorDeploymentPausedReason object { error, type }`

    A scheduled fire recorded a failed run whose error auto-pauses the deployment.

    - `error: BetaManagedAgentsDeploymentPausedReasonError`

      The error that triggered an auto-pause. Matches the failed run's `error.type`.

      - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type }`

        The deployment's environment was archived.

        - `type: "environment_archived_error"`

          - `"environment_archived_error"`

      - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type }`

        The deployment's agent was archived.

        - `type: "agent_archived_error"`

          - `"agent_archived_error"`

      - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type }`

        The deployment's environment no longer exists.

        - `type: "environment_not_found_error"`

          - `"environment_not_found_error"`

      - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type }`

        A vault referenced by the deployment no longer exists.

        - `type: "vault_not_found_error"`

          - `"vault_not_found_error"`

      - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type }`

        A file resource referenced by the deployment no longer exists.

        - `type: "file_not_found_error"`

          - `"file_not_found_error"`

      - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type }`

        A referenced resource no longer exists and its kind was not reported.

        - `type: "session_resource_not_found_error"`

          - `"session_resource_not_found_error"`

      - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type }`

        The deployment's workspace was archived.

        - `type: "workspace_archived_error"`

          - `"workspace_archived_error"`

      - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type }`

        The deployment's organization is disabled.

        - `type: "organization_disabled_error"`

          - `"organization_disabled_error"`

      - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type }`

        A memory store referenced by the deployment is archived.

        - `type: "memory_store_archived_error"`

          - `"memory_store_archived_error"`

      - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type }`

        A skill referenced by the deployment's agent no longer exists.

        - `type: "skill_not_found_error"`

          - `"skill_not_found_error"`

      - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type }`

        A vault referenced by the deployment is archived.

        - `type: "vault_archived_error"`

          - `"vault_archived_error"`

      - `BetaManagedAgentsUnknownDeploymentPausedReasonError object { type }`

        An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

        - `type: "unknown_error"`

          - `"unknown_error"`

      - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type }`

        The deployment configures resources, but its environment is self-hosted and cannot mount them.

        - `type: "self_hosted_resources_unsupported_error"`

          - `"self_hosted_resources_unsupported_error"`

      - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type }`

        An MCP server host used by the deployment's agent is blocked by the environment's network policy.

        - `type: "mcp_egress_blocked_error"`

          - `"mcp_egress_blocked_error"`

    - `type: "error"`

      - `"error"`

### Beta Managed Agents Deployment Paused Reason Error

- `BetaManagedAgentsDeploymentPausedReasonError = BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

  The error that triggered an auto-pause. Matches the failed run's `error.type`.

  - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type }`

    The deployment's environment was archived.

    - `type: "environment_archived_error"`

      - `"environment_archived_error"`

  - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type }`

    The deployment's agent was archived.

    - `type: "agent_archived_error"`

      - `"agent_archived_error"`

  - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type }`

    The deployment's environment no longer exists.

    - `type: "environment_not_found_error"`

      - `"environment_not_found_error"`

  - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type }`

    A vault referenced by the deployment no longer exists.

    - `type: "vault_not_found_error"`

      - `"vault_not_found_error"`

  - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type }`

    A file resource referenced by the deployment no longer exists.

    - `type: "file_not_found_error"`

      - `"file_not_found_error"`

  - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type }`

    A referenced resource no longer exists and its kind was not reported.

    - `type: "session_resource_not_found_error"`

      - `"session_resource_not_found_error"`

  - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type }`

    The deployment's workspace was archived.

    - `type: "workspace_archived_error"`

      - `"workspace_archived_error"`

  - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type }`

    The deployment's organization is disabled.

    - `type: "organization_disabled_error"`

      - `"organization_disabled_error"`

  - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type }`

    A memory store referenced by the deployment is archived.

    - `type: "memory_store_archived_error"`

      - `"memory_store_archived_error"`

  - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type }`

    A skill referenced by the deployment's agent no longer exists.

    - `type: "skill_not_found_error"`

      - `"skill_not_found_error"`

  - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type }`

    A vault referenced by the deployment is archived.

    - `type: "vault_archived_error"`

      - `"vault_archived_error"`

  - `BetaManagedAgentsUnknownDeploymentPausedReasonError object { type }`

    An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

    - `type: "unknown_error"`

      - `"unknown_error"`

  - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type }`

    The deployment configures resources, but its environment is self-hosted and cannot mount them.

    - `type: "self_hosted_resources_unsupported_error"`

      - `"self_hosted_resources_unsupported_error"`

  - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type }`

    An MCP server host used by the deployment's agent is blocked by the environment's network policy.

    - `type: "mcp_egress_blocked_error"`

      - `"mcp_egress_blocked_error"`

### Beta Managed Agents Deployment Status

- `BetaManagedAgentsDeploymentStatus = "active" or "paused"`

  Lifecycle status of a deployment.

  - `"active"`

  - `"paused"`

### Beta Managed Agents Deployment System Message Event

- `BetaManagedAgentsDeploymentSystemMessageEvent object { content, type }`

  Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

  - `content: array of BetaManagedAgentsSystemContentBlock`

    System content blocks to append. Text-only.

    - `text: string`

      The text content.

    - `type: "text"`

      - `"text"`

  - `type: "system.message"`

    - `"system.message"`

### Beta Managed Agents Deployment User Define Outcome Event

- `BetaManagedAgentsDeploymentUserDefineOutcomeEvent object { description, rubric, type, max_iterations }`

  An outcome the agent should work toward. The agent begins work on receipt.

  - `description: string`

    What the agent should produce. This is the task specification.

  - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

    Rubric for grading the quality of an outcome.

    - `BetaManagedAgentsFileRubric object { file_id, type }`

      Rubric referenced by a file uploaded via the Files API.

      - `file_id: string`

        ID of the rubric file.

      - `type: "file"`

        - `"file"`

    - `BetaManagedAgentsTextRubric object { content, type }`

      Rubric content provided inline as text.

      - `content: string`

        Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `type: "text"`

        - `"text"`

  - `type: "user.define_outcome"`

    - `"user.define_outcome"`

  - `max_iterations: optional number`

    Eval→revision cycles before giving up. Default 3, max 20.

### Beta Managed Agents Deployment User Message Event

- `BetaManagedAgentsDeploymentUserMessageEvent object { content, type }`

  A user message sent to the session.

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

    Array of content blocks for the user message.

    - `BetaManagedAgentsTextBlock object { text, type }`

      Regular text content.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `BetaManagedAgentsImageBlock object { source, type }`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsURLImageSource object { type, url }`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `BetaManagedAgentsFileImageSource object { file_id, type }`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsURLDocumentSource object { type, url }`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "document"`

        - `"document"`

      - `context: optional string`

        Additional context about the document for the model.

      - `title: optional string`

        The title of the document.

  - `type: "user.message"`

    - `"user.message"`

### Beta Managed Agents Environment Archived Deployment Paused Reason Error

- `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type }`

  The deployment's environment was archived.

  - `type: "environment_archived_error"`

    - `"environment_archived_error"`

### Beta Managed Agents Environment Not Found Deployment Paused Reason Error

- `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type }`

  The deployment's environment no longer exists.

  - `type: "environment_not_found_error"`

    - `"environment_not_found_error"`

### Beta Managed Agents Error Deployment Paused Reason

- `BetaManagedAgentsErrorDeploymentPausedReason object { error, type }`

  A scheduled fire recorded a failed run whose error auto-pauses the deployment.

  - `error: BetaManagedAgentsDeploymentPausedReasonError`

    The error that triggered an auto-pause. Matches the failed run's `error.type`.

    - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type }`

      The deployment's environment was archived.

      - `type: "environment_archived_error"`

        - `"environment_archived_error"`

    - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type }`

      The deployment's agent was archived.

      - `type: "agent_archived_error"`

        - `"agent_archived_error"`

    - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type }`

      The deployment's environment no longer exists.

      - `type: "environment_not_found_error"`

        - `"environment_not_found_error"`

    - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type }`

      A vault referenced by the deployment no longer exists.

      - `type: "vault_not_found_error"`

        - `"vault_not_found_error"`

    - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type }`

      A file resource referenced by the deployment no longer exists.

      - `type: "file_not_found_error"`

        - `"file_not_found_error"`

    - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type }`

      A referenced resource no longer exists and its kind was not reported.

      - `type: "session_resource_not_found_error"`

        - `"session_resource_not_found_error"`

    - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type }`

      The deployment's workspace was archived.

      - `type: "workspace_archived_error"`

        - `"workspace_archived_error"`

    - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type }`

      The deployment's organization is disabled.

      - `type: "organization_disabled_error"`

        - `"organization_disabled_error"`

    - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type }`

      A memory store referenced by the deployment is archived.

      - `type: "memory_store_archived_error"`

        - `"memory_store_archived_error"`

    - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type }`

      A skill referenced by the deployment's agent no longer exists.

      - `type: "skill_not_found_error"`

        - `"skill_not_found_error"`

    - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type }`

      A vault referenced by the deployment is archived.

      - `type: "vault_archived_error"`

        - `"vault_archived_error"`

    - `BetaManagedAgentsUnknownDeploymentPausedReasonError object { type }`

      An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

      - `type: "unknown_error"`

        - `"unknown_error"`

    - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type }`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `type: "self_hosted_resources_unsupported_error"`

        - `"self_hosted_resources_unsupported_error"`

    - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type }`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `type: "mcp_egress_blocked_error"`

        - `"mcp_egress_blocked_error"`

  - `type: "error"`

    - `"error"`

### Beta Managed Agents File Not Found Deployment Paused Reason Error

- `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type }`

  A file resource referenced by the deployment no longer exists.

  - `type: "file_not_found_error"`

    - `"file_not_found_error"`

### Beta Managed Agents File Resource Config

- `BetaManagedAgentsFileResourceConfig object { file_id, type, mount_path }`

  A file mounted into each session's container.

  - `file_id: string`

    ID of a previously uploaded file.

  - `type: "file"`

    - `"file"`

  - `mount_path: optional string`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Config

- `BetaManagedAgentsGitHubRepositoryResourceConfig object { type, url, checkout, mount_path }`

  A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

  - `type: "github_repository"`

    - `"github_repository"`

  - `url: string`

    Github URL of the repository

  - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `BetaManagedAgentsBranchCheckout object { name, type }`

      - `name: string`

        Branch name to check out.

      - `type: "branch"`

        - `"branch"`

    - `BetaManagedAgentsCommitCheckout object { sha, type }`

      - `sha: string`

        Full commit SHA to check out.

      - `type: "commit"`

        - `"commit"`

  - `mount_path: optional string`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Manual Deployment Paused Reason

- `BetaManagedAgentsManualDeploymentPausedReason object { type }`

  The caller invoked the pause endpoint on the deployment.

  - `type: "manual"`

    - `"manual"`

### Beta Managed Agents MCP Egress Blocked Deployment Paused Reason Error

- `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type }`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `type: "mcp_egress_blocked_error"`

    - `"mcp_egress_blocked_error"`

### Beta Managed Agents Memory Store Archived Deployment Paused Reason Error

- `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type }`

  A memory store referenced by the deployment is archived.

  - `type: "memory_store_archived_error"`

    - `"memory_store_archived_error"`

### Beta Managed Agents Memory Store Resource Config

- `BetaManagedAgentsMemoryStoreResourceConfig object { memory_store_id, type, access, instructions }`

  A memory store attached to each session created from this deployment.

  - `memory_store_id: string`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `type: "memory_store"`

    - `"memory_store"`

  - `access: optional "read_write" or "read_only"`

    Access mode for an attached memory store.

    - `"read_write"`

    - `"read_only"`

  - `instructions: optional string`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Organization Disabled Deployment Paused Reason Error

- `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type }`

  The deployment's organization is disabled.

  - `type: "organization_disabled_error"`

    - `"organization_disabled_error"`

### Beta Managed Agents Schedule

- `BetaManagedAgentsSchedule object { expression, timezone, type, 2 more }`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: string`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `type: "cron"`

    - `"cron"`

  - `last_run_at: optional string`

    A timestamp in RFC 3339 format

  - `upcoming_runs_at: optional array of string`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Schedule Params

- `BetaManagedAgentsScheduleParams object { expression, timezone, type }`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: string`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `type: "cron"`

    - `"cron"`

### Beta Managed Agents Self Hosted Resources Unsupported Deployment Paused Reason Error

- `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type }`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `type: "self_hosted_resources_unsupported_error"`

    - `"self_hosted_resources_unsupported_error"`

### Beta Managed Agents Session Resource Config

- `BetaManagedAgentsSessionResourceConfig = BetaManagedAgentsGitHubRepositoryResourceConfig or BetaManagedAgentsFileResourceConfig or BetaManagedAgentsMemoryStoreResourceConfig`

  A configured session resource. Echoes the input minus write-only credentials.

  - `BetaManagedAgentsGitHubRepositoryResourceConfig object { type, url, checkout, mount_path }`

    A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

    - `type: "github_repository"`

      - `"github_repository"`

    - `url: string`

      Github URL of the repository

    - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `BetaManagedAgentsBranchCheckout object { name, type }`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `BetaManagedAgentsCommitCheckout object { sha, type }`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

    - `mount_path: optional string`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `BetaManagedAgentsFileResourceConfig object { file_id, type, mount_path }`

    A file mounted into each session's container.

    - `file_id: string`

      ID of a previously uploaded file.

    - `type: "file"`

      - `"file"`

    - `mount_path: optional string`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `BetaManagedAgentsMemoryStoreResourceConfig object { memory_store_id, type, access, instructions }`

    A memory store attached to each session created from this deployment.

    - `memory_store_id: string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: "memory_store"`

      - `"memory_store"`

    - `access: optional "read_write" or "read_only"`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `instructions: optional string`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Session Resource Not Found Deployment Paused Reason Error

- `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type }`

  A referenced resource no longer exists and its kind was not reported.

  - `type: "session_resource_not_found_error"`

    - `"session_resource_not_found_error"`

### Beta Managed Agents Skill Not Found Deployment Paused Reason Error

- `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type }`

  A skill referenced by the deployment's agent no longer exists.

  - `type: "skill_not_found_error"`

    - `"skill_not_found_error"`

### Beta Managed Agents Unknown Deployment Paused Reason Error

- `BetaManagedAgentsUnknownDeploymentPausedReasonError object { type }`

  An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

  - `type: "unknown_error"`

    - `"unknown_error"`

### Beta Managed Agents Vault Archived Deployment Paused Reason Error

- `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type }`

  A vault referenced by the deployment is archived.

  - `type: "vault_archived_error"`

    - `"vault_archived_error"`

### Beta Managed Agents Vault Not Found Deployment Paused Reason Error

- `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type }`

  A vault referenced by the deployment no longer exists.

  - `type: "vault_not_found_error"`

    - `"vault_not_found_error"`

### Beta Managed Agents Workspace Archived Deployment Paused Reason Error

- `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type }`

  The deployment's workspace was archived.

  - `type: "workspace_archived_error"`

    - `"workspace_archived_error"`

# Deployment Runs

## List Deployment Runs

**get** `/v1/deployment_runs`

List Deployment Runs

### Query Parameters

- `"created_at[gt]": optional string`

  Return runs created strictly after this time (exclusive).

- `"created_at[gte]": optional string`

  Return runs created at or after this time (inclusive).

- `"created_at[lt]": optional string`

  Return runs created strictly before this time (exclusive).

- `"created_at[lte]": optional string`

  Return runs created at or before this time (inclusive).

- `deployment_id: optional string`

  Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent deployment_id returns 200 with empty data.

- `has_error: optional boolean`

  Filter: true for runs with non-null error, false for runs with non-null session_id. Omit for all.

- `limit: optional number`

  Maximum results per page. Default 20, maximum 1000.

- `page: optional string`

  Opaque pagination cursor. Pass next_page from the previous response. Invalid or expired cursors return 400.

- `trigger_type: optional BetaManagedAgentsTriggerType`

  Filter runs by what triggered them. Omit to return all runs.

  - `"schedule"`

  - `"manual"`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `data: array of BetaManagedAgentsDeploymentRun`

  List of deployment runs.

  - `id: string`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `deployment_id: string`

    ID of the deployment that produced this run.

  - `error: BetaManagedAgentsEnvironmentArchivedRunError or BetaManagedAgentsAgentArchivedRunError or BetaManagedAgentsEnvironmentNotFoundRunError or 13 more`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `BetaManagedAgentsEnvironmentArchivedRunError object { message, type }`

      The deployment's environment was archived.

      - `message: string`

        Human-readable error description.

      - `type: "environment_archived_error"`

        - `"environment_archived_error"`

    - `BetaManagedAgentsAgentArchivedRunError object { message, type }`

      The deployment's agent was archived.

      - `message: string`

        Human-readable error description.

      - `type: "agent_archived_error"`

        - `"agent_archived_error"`

    - `BetaManagedAgentsEnvironmentNotFoundRunError object { message, type }`

      The deployment's environment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "environment_not_found_error"`

        - `"environment_not_found_error"`

    - `BetaManagedAgentsVaultNotFoundRunError object { message, type }`

      A vault referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "vault_not_found_error"`

        - `"vault_not_found_error"`

    - `BetaManagedAgentsVaultArchivedRunError object { message, type }`

      A vault referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "vault_archived_error"`

        - `"vault_archived_error"`

    - `BetaManagedAgentsFileNotFoundRunError object { message, type }`

      A file resource referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "file_not_found_error"`

        - `"file_not_found_error"`

    - `BetaManagedAgentsMemoryStoreArchivedRunError object { message, type }`

      A memory store referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "memory_store_archived_error"`

        - `"memory_store_archived_error"`

    - `BetaManagedAgentsSkillNotFoundRunError object { message, type }`

      A skill referenced by the deployment's agent no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "skill_not_found_error"`

        - `"skill_not_found_error"`

    - `BetaManagedAgentsSessionResourceNotFoundRunError object { message, type }`

      A referenced resource no longer exists and its kind was not reported.

      - `message: string`

        Human-readable error description.

      - `type: "session_resource_not_found_error"`

        - `"session_resource_not_found_error"`

    - `BetaManagedAgentsWorkspaceArchivedRunError object { message, type }`

      The deployment's workspace was archived.

      - `message: string`

        Human-readable error description.

      - `type: "workspace_archived_error"`

        - `"workspace_archived_error"`

    - `BetaManagedAgentsOrganizationDisabledRunError object { message, type }`

      The deployment's organization is disabled.

      - `message: string`

        Human-readable error description.

      - `type: "organization_disabled_error"`

        - `"organization_disabled_error"`

    - `BetaManagedAgentsSessionRateLimitedRunError object { message, type }`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: string`

        Human-readable error description.

      - `type: "session_rate_limited_error"`

        - `"session_rate_limited_error"`

    - `BetaManagedAgentsSessionCreationRejectedRunError object { message, type }`

      The session create request was rejected with a non-retryable validation error.

      - `message: string`

        Human-readable error description.

      - `type: "session_creation_rejected_error"`

        - `"session_creation_rejected_error"`

    - `BetaManagedAgentsUnknownRunError object { message, type }`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: string`

        Human-readable error description.

      - `type: "unknown_error"`

        - `"unknown_error"`

    - `BetaManagedAgentsSelfHostedResourcesUnsupportedRunError object { message, type }`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: string`

        Human-readable error description.

      - `type: "self_hosted_resources_unsupported_error"`

        - `"self_hosted_resources_unsupported_error"`

    - `BetaManagedAgentsMCPEgressBlockedRunError object { message, type }`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: string`

        Human-readable error description.

      - `type: "mcp_egress_blocked_error"`

        - `"mcp_egress_blocked_error"`

  - `session_id: string`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `BetaManagedAgentsScheduleTriggerContext object { scheduled_at, type }`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: string`

        A timestamp in RFC 3339 format

      - `type: "schedule"`

        - `"schedule"`

    - `BetaManagedAgentsManualTriggerContext object { type }`

      The run was started manually by creating a session directly against the deployment.

      - `type: "manual"`

        - `"manual"`

  - `type: "deployment_run"`

    - `"deployment_run"`

- `next_page: optional string`

  Opaque cursor for the next page. Null when no more results.

### Example

```http
curl https://api.anthropic.com/v1/deployment_runs \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/deployment_runs/{deployment_run_id}`

Get Deployment Run

### Path Parameters

- `deployment_run_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsDeploymentRun object { id, agent, created_at, 5 more }`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: string`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `deployment_id: string`

    ID of the deployment that produced this run.

  - `error: BetaManagedAgentsEnvironmentArchivedRunError or BetaManagedAgentsAgentArchivedRunError or BetaManagedAgentsEnvironmentNotFoundRunError or 13 more`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `BetaManagedAgentsEnvironmentArchivedRunError object { message, type }`

      The deployment's environment was archived.

      - `message: string`

        Human-readable error description.

      - `type: "environment_archived_error"`

        - `"environment_archived_error"`

    - `BetaManagedAgentsAgentArchivedRunError object { message, type }`

      The deployment's agent was archived.

      - `message: string`

        Human-readable error description.

      - `type: "agent_archived_error"`

        - `"agent_archived_error"`

    - `BetaManagedAgentsEnvironmentNotFoundRunError object { message, type }`

      The deployment's environment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "environment_not_found_error"`

        - `"environment_not_found_error"`

    - `BetaManagedAgentsVaultNotFoundRunError object { message, type }`

      A vault referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "vault_not_found_error"`

        - `"vault_not_found_error"`

    - `BetaManagedAgentsVaultArchivedRunError object { message, type }`

      A vault referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "vault_archived_error"`

        - `"vault_archived_error"`

    - `BetaManagedAgentsFileNotFoundRunError object { message, type }`

      A file resource referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "file_not_found_error"`

        - `"file_not_found_error"`

    - `BetaManagedAgentsMemoryStoreArchivedRunError object { message, type }`

      A memory store referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "memory_store_archived_error"`

        - `"memory_store_archived_error"`

    - `BetaManagedAgentsSkillNotFoundRunError object { message, type }`

      A skill referenced by the deployment's agent no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "skill_not_found_error"`

        - `"skill_not_found_error"`

    - `BetaManagedAgentsSessionResourceNotFoundRunError object { message, type }`

      A referenced resource no longer exists and its kind was not reported.

      - `message: string`

        Human-readable error description.

      - `type: "session_resource_not_found_error"`

        - `"session_resource_not_found_error"`

    - `BetaManagedAgentsWorkspaceArchivedRunError object { message, type }`

      The deployment's workspace was archived.

      - `message: string`

        Human-readable error description.

      - `type: "workspace_archived_error"`

        - `"workspace_archived_error"`

    - `BetaManagedAgentsOrganizationDisabledRunError object { message, type }`

      The deployment's organization is disabled.

      - `message: string`

        Human-readable error description.

      - `type: "organization_disabled_error"`

        - `"organization_disabled_error"`

    - `BetaManagedAgentsSessionRateLimitedRunError object { message, type }`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: string`

        Human-readable error description.

      - `type: "session_rate_limited_error"`

        - `"session_rate_limited_error"`

    - `BetaManagedAgentsSessionCreationRejectedRunError object { message, type }`

      The session create request was rejected with a non-retryable validation error.

      - `message: string`

        Human-readable error description.

      - `type: "session_creation_rejected_error"`

        - `"session_creation_rejected_error"`

    - `BetaManagedAgentsUnknownRunError object { message, type }`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: string`

        Human-readable error description.

      - `type: "unknown_error"`

        - `"unknown_error"`

    - `BetaManagedAgentsSelfHostedResourcesUnsupportedRunError object { message, type }`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: string`

        Human-readable error description.

      - `type: "self_hosted_resources_unsupported_error"`

        - `"self_hosted_resources_unsupported_error"`

    - `BetaManagedAgentsMCPEgressBlockedRunError object { message, type }`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: string`

        Human-readable error description.

      - `type: "mcp_egress_blocked_error"`

        - `"mcp_egress_blocked_error"`

  - `session_id: string`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `BetaManagedAgentsScheduleTriggerContext object { scheduled_at, type }`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: string`

        A timestamp in RFC 3339 format

      - `type: "schedule"`

        - `"schedule"`

    - `BetaManagedAgentsManualTriggerContext object { type }`

      The run was started manually by creating a session directly against the deployment.

      - `type: "manual"`

        - `"manual"`

  - `type: "deployment_run"`

    - `"deployment_run"`

### Example

```http
curl https://api.anthropic.com/v1/deployment_runs/$DEPLOYMENT_RUN_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `BetaManagedAgentsAgentArchivedRunError object { message, type }`

  The deployment's agent was archived.

  - `message: string`

    Human-readable error description.

  - `type: "agent_archived_error"`

    - `"agent_archived_error"`

### Beta Managed Agents Deployment Run

- `BetaManagedAgentsDeploymentRun object { id, agent, created_at, 5 more }`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: string`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `deployment_id: string`

    ID of the deployment that produced this run.

  - `error: BetaManagedAgentsEnvironmentArchivedRunError or BetaManagedAgentsAgentArchivedRunError or BetaManagedAgentsEnvironmentNotFoundRunError or 13 more`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `BetaManagedAgentsEnvironmentArchivedRunError object { message, type }`

      The deployment's environment was archived.

      - `message: string`

        Human-readable error description.

      - `type: "environment_archived_error"`

        - `"environment_archived_error"`

    - `BetaManagedAgentsAgentArchivedRunError object { message, type }`

      The deployment's agent was archived.

      - `message: string`

        Human-readable error description.

      - `type: "agent_archived_error"`

        - `"agent_archived_error"`

    - `BetaManagedAgentsEnvironmentNotFoundRunError object { message, type }`

      The deployment's environment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "environment_not_found_error"`

        - `"environment_not_found_error"`

    - `BetaManagedAgentsVaultNotFoundRunError object { message, type }`

      A vault referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "vault_not_found_error"`

        - `"vault_not_found_error"`

    - `BetaManagedAgentsVaultArchivedRunError object { message, type }`

      A vault referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "vault_archived_error"`

        - `"vault_archived_error"`

    - `BetaManagedAgentsFileNotFoundRunError object { message, type }`

      A file resource referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "file_not_found_error"`

        - `"file_not_found_error"`

    - `BetaManagedAgentsMemoryStoreArchivedRunError object { message, type }`

      A memory store referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "memory_store_archived_error"`

        - `"memory_store_archived_error"`

    - `BetaManagedAgentsSkillNotFoundRunError object { message, type }`

      A skill referenced by the deployment's agent no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "skill_not_found_error"`

        - `"skill_not_found_error"`

    - `BetaManagedAgentsSessionResourceNotFoundRunError object { message, type }`

      A referenced resource no longer exists and its kind was not reported.

      - `message: string`

        Human-readable error description.

      - `type: "session_resource_not_found_error"`

        - `"session_resource_not_found_error"`

    - `BetaManagedAgentsWorkspaceArchivedRunError object { message, type }`

      The deployment's workspace was archived.

      - `message: string`

        Human-readable error description.

      - `type: "workspace_archived_error"`

        - `"workspace_archived_error"`

    - `BetaManagedAgentsOrganizationDisabledRunError object { message, type }`

      The deployment's organization is disabled.

      - `message: string`

        Human-readable error description.

      - `type: "organization_disabled_error"`

        - `"organization_disabled_error"`

    - `BetaManagedAgentsSessionRateLimitedRunError object { message, type }`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: string`

        Human-readable error description.

      - `type: "session_rate_limited_error"`

        - `"session_rate_limited_error"`

    - `BetaManagedAgentsSessionCreationRejectedRunError object { message, type }`

      The session create request was rejected with a non-retryable validation error.

      - `message: string`

        Human-readable error description.

      - `type: "session_creation_rejected_error"`

        - `"session_creation_rejected_error"`

    - `BetaManagedAgentsUnknownRunError object { message, type }`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: string`

        Human-readable error description.

      - `type: "unknown_error"`

        - `"unknown_error"`

    - `BetaManagedAgentsSelfHostedResourcesUnsupportedRunError object { message, type }`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: string`

        Human-readable error description.

      - `type: "self_hosted_resources_unsupported_error"`

        - `"self_hosted_resources_unsupported_error"`

    - `BetaManagedAgentsMCPEgressBlockedRunError object { message, type }`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: string`

        Human-readable error description.

      - `type: "mcp_egress_blocked_error"`

        - `"mcp_egress_blocked_error"`

  - `session_id: string`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `BetaManagedAgentsScheduleTriggerContext object { scheduled_at, type }`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: string`

        A timestamp in RFC 3339 format

      - `type: "schedule"`

        - `"schedule"`

    - `BetaManagedAgentsManualTriggerContext object { type }`

      The run was started manually by creating a session directly against the deployment.

      - `type: "manual"`

        - `"manual"`

  - `type: "deployment_run"`

    - `"deployment_run"`

### Beta Managed Agents Environment Archived Run Error

- `BetaManagedAgentsEnvironmentArchivedRunError object { message, type }`

  The deployment's environment was archived.

  - `message: string`

    Human-readable error description.

  - `type: "environment_archived_error"`

    - `"environment_archived_error"`

### Beta Managed Agents Environment Not Found Run Error

- `BetaManagedAgentsEnvironmentNotFoundRunError object { message, type }`

  The deployment's environment no longer exists.

  - `message: string`

    Human-readable error description.

  - `type: "environment_not_found_error"`

    - `"environment_not_found_error"`

### Beta Managed Agents File Not Found Run Error

- `BetaManagedAgentsFileNotFoundRunError object { message, type }`

  A file resource referenced by the deployment no longer exists.

  - `message: string`

    Human-readable error description.

  - `type: "file_not_found_error"`

    - `"file_not_found_error"`

### Beta Managed Agents Manual Trigger Context

- `BetaManagedAgentsManualTriggerContext object { type }`

  The run was started manually by creating a session directly against the deployment.

  - `type: "manual"`

    - `"manual"`

### Beta Managed Agents MCP Egress Blocked Run Error

- `BetaManagedAgentsMCPEgressBlockedRunError object { message, type }`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `message: string`

    Human-readable error description.

  - `type: "mcp_egress_blocked_error"`

    - `"mcp_egress_blocked_error"`

### Beta Managed Agents Memory Store Archived Run Error

- `BetaManagedAgentsMemoryStoreArchivedRunError object { message, type }`

  A memory store referenced by the deployment is archived.

  - `message: string`

    Human-readable error description.

  - `type: "memory_store_archived_error"`

    - `"memory_store_archived_error"`

### Beta Managed Agents Organization Disabled Run Error

- `BetaManagedAgentsOrganizationDisabledRunError object { message, type }`

  The deployment's organization is disabled.

  - `message: string`

    Human-readable error description.

  - `type: "organization_disabled_error"`

    - `"organization_disabled_error"`

### Beta Managed Agents Schedule Trigger Context

- `BetaManagedAgentsScheduleTriggerContext object { scheduled_at, type }`

  The run was fired by the deployment's cron schedule.

  - `scheduled_at: string`

    A timestamp in RFC 3339 format

  - `type: "schedule"`

    - `"schedule"`

### Beta Managed Agents Self Hosted Resources Unsupported Run Error

- `BetaManagedAgentsSelfHostedResourcesUnsupportedRunError object { message, type }`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `message: string`

    Human-readable error description.

  - `type: "self_hosted_resources_unsupported_error"`

    - `"self_hosted_resources_unsupported_error"`

### Beta Managed Agents Session Creation Rejected Run Error

- `BetaManagedAgentsSessionCreationRejectedRunError object { message, type }`

  The session create request was rejected with a non-retryable validation error.

  - `message: string`

    Human-readable error description.

  - `type: "session_creation_rejected_error"`

    - `"session_creation_rejected_error"`

### Beta Managed Agents Session Rate Limited Run Error

- `BetaManagedAgentsSessionRateLimitedRunError object { message, type }`

  Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

  - `message: string`

    Human-readable error description.

  - `type: "session_rate_limited_error"`

    - `"session_rate_limited_error"`

### Beta Managed Agents Session Resource Not Found Run Error

- `BetaManagedAgentsSessionResourceNotFoundRunError object { message, type }`

  A referenced resource no longer exists and its kind was not reported.

  - `message: string`

    Human-readable error description.

  - `type: "session_resource_not_found_error"`

    - `"session_resource_not_found_error"`

### Beta Managed Agents Skill Not Found Run Error

- `BetaManagedAgentsSkillNotFoundRunError object { message, type }`

  A skill referenced by the deployment's agent no longer exists.

  - `message: string`

    Human-readable error description.

  - `type: "skill_not_found_error"`

    - `"skill_not_found_error"`

### Beta Managed Agents Trigger Context

- `BetaManagedAgentsTriggerContext = BetaManagedAgentsScheduleTriggerContext or BetaManagedAgentsManualTriggerContext`

  Describes what triggered a deployment run, with trigger-specific metadata.

  - `BetaManagedAgentsScheduleTriggerContext object { scheduled_at, type }`

    The run was fired by the deployment's cron schedule.

    - `scheduled_at: string`

      A timestamp in RFC 3339 format

    - `type: "schedule"`

      - `"schedule"`

  - `BetaManagedAgentsManualTriggerContext object { type }`

    The run was started manually by creating a session directly against the deployment.

    - `type: "manual"`

      - `"manual"`

### Beta Managed Agents Trigger Type

- `BetaManagedAgentsTriggerType = "schedule" or "manual"`

  What triggered a deployment run.

  - `"schedule"`

  - `"manual"`

### Beta Managed Agents Unknown Run Error

- `BetaManagedAgentsUnknownRunError object { message, type }`

  An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

  - `message: string`

    Human-readable error description.

  - `type: "unknown_error"`

    - `"unknown_error"`

### Beta Managed Agents Vault Archived Run Error

- `BetaManagedAgentsVaultArchivedRunError object { message, type }`

  A vault referenced by the deployment is archived.

  - `message: string`

    Human-readable error description.

  - `type: "vault_archived_error"`

    - `"vault_archived_error"`

### Beta Managed Agents Vault Not Found Run Error

- `BetaManagedAgentsVaultNotFoundRunError object { message, type }`

  A vault referenced by the deployment no longer exists.

  - `message: string`

    Human-readable error description.

  - `type: "vault_not_found_error"`

    - `"vault_not_found_error"`

### Beta Managed Agents Workspace Archived Run Error

- `BetaManagedAgentsWorkspaceArchivedRunError object { message, type }`

  The deployment's workspace was archived.

  - `message: string`

    Human-readable error description.

  - `type: "workspace_archived_error"`

    - `"workspace_archived_error"`

# Vaults

## Create Vault

**post** `/v1/vaults`

Create Vault

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `display_name: string`

  Human-readable name for the vault. 1-255 characters.

- `metadata: optional map[string]`

  Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

### Returns

- `BetaManagedAgentsVault object { id, archived_at, created_at, 4 more }`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```http
curl https://api.anthropic.com/v1/vaults \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "display_name": "Example vault",
          "metadata": {
            "environment": "production"
          }
        }'
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

**get** `/v1/vaults`

List Vaults

### Query Parameters

- `include_archived: optional boolean`

  Whether to include archived vaults in the results.

- `limit: optional number`

  Maximum number of vaults to return per page. Defaults to 20, maximum 100.

- `page: optional string`

  Opaque pagination token from a previous `list_vaults` response.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `data: optional array of BetaManagedAgentsVault`

  List of vaults.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

- `next_page: optional string`

  Pagination token for the next page, or null if no more results.

### Example

```http
curl https://api.anthropic.com/v1/vaults \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/vaults/{vault_id}`

Get Vault

### Path Parameters

- `vault_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsVault object { id, archived_at, created_at, 4 more }`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/vaults/{vault_id}`

Update Vault

### Path Parameters

- `vault_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `display_name: optional string`

  Updated human-readable name for the vault. 1-255 characters.

- `metadata: optional map[string]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

### Returns

- `BetaManagedAgentsVault object { id, archived_at, created_at, 4 more }`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "display_name": "Example vault",
          "metadata": {
            "environment": "production"
          }
        }'
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

**delete** `/v1/vaults/{vault_id}`

Delete Vault

### Path Parameters

- `vault_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsDeletedVault object { id, type }`

  Confirmation of a deleted vault.

  - `id: string`

    Unique identifier of the deleted vault.

  - `type: "vault_deleted"`

    - `"vault_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

## Archive Vault

**post** `/v1/vaults/{vault_id}/archive`

Archive Vault

### Path Parameters

- `vault_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsVault object { id, archived_at, created_at, 4 more }`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `BetaManagedAgentsDeletedVault object { id, type }`

  Confirmation of a deleted vault.

  - `id: string`

    Unique identifier of the deleted vault.

  - `type: "vault_deleted"`

    - `"vault_deleted"`

### Beta Managed Agents Vault

- `BetaManagedAgentsVault object { id, archived_at, created_at, 4 more }`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

# Credentials

## Create Credential

**post** `/v1/vaults/{vault_id}/credentials`

Create Credential

### Path Parameters

- `vault_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `auth: BetaManagedAgentsMCPOAuthCreateParams or BetaManagedAgentsStaticBearerCreateParams or BetaManagedAgentsEnvironmentVariableCreateParams`

  Authentication details for creating a credential.

  - `BetaManagedAgentsMCPOAuthCreateParams object { access_token, mcp_server_url, type, 2 more }`

    Parameters for creating an MCP OAuth credential.

    - `access_token: string`

      OAuth access token.

    - `mcp_server_url: string`

      URL of the MCP server this credential authenticates against.

    - `type: "mcp_oauth"`

      - `"mcp_oauth"`

    - `expires_at: optional string`

      A timestamp in RFC 3339 format

    - `refresh: optional BetaManagedAgentsMCPOAuthRefreshParams`

      OAuth refresh token parameters for creating a credential with refresh support.

      - `client_id: string`

        OAuth client ID.

      - `refresh_token: string`

        OAuth refresh token.

      - `token_endpoint: string`

        Token endpoint URL used to refresh the access token.

      - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam or BetaManagedAgentsTokenEndpointAuthBasicParam or BetaManagedAgentsTokenEndpointAuthPostParam`

        Token endpoint requires no client authentication.

        - `BetaManagedAgentsTokenEndpointAuthNoneParam object { type }`

          Token endpoint requires no client authentication.

          - `type: "none"`

            - `"none"`

        - `BetaManagedAgentsTokenEndpointAuthBasicParam object { client_secret, type }`

          Token endpoint uses HTTP Basic authentication with client credentials.

          - `client_secret: string`

            OAuth client secret.

          - `type: "client_secret_basic"`

            - `"client_secret_basic"`

        - `BetaManagedAgentsTokenEndpointAuthPostParam object { client_secret, type }`

          Token endpoint uses POST body authentication with client credentials.

          - `client_secret: string`

            OAuth client secret.

          - `type: "client_secret_post"`

            - `"client_secret_post"`

      - `resource: optional string`

        OAuth resource indicator.

      - `scope: optional string`

        OAuth scope for the refresh request.

  - `BetaManagedAgentsStaticBearerCreateParams object { token, mcp_server_url, type }`

    Parameters for creating a static bearer token credential.

    - `token: string`

      Static bearer token value.

    - `mcp_server_url: string`

      URL of the MCP server this credential authenticates against.

    - `type: "static_bearer"`

      - `"static_bearer"`

  - `BetaManagedAgentsEnvironmentVariableCreateParams object { networking, secret_name, secret_value, 2 more }`

    Parameters for creating an environment variable credential.

    - `networking: BetaManagedAgentsCredentialNetworkingParams`

      Outbound hosts the secret value is substituted on.

      - `BetaManagedAgentsUnrestrictedCredentialNetworkingParams object { type }`

        Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

        - `type: "unrestricted"`

          - `"unrestricted"`

      - `BetaManagedAgentsLimitedCredentialNetworkingParams object { allowed_hosts, type }`

        Substitute the secret only on requests to the listed hosts.

        - `allowed_hosts: array of string`

          Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

        - `type: "limited"`

          - `"limited"`

    - `secret_name: string`

      Name of the environment variable. Immutable after create.

    - `secret_value: string`

      Secret value. Write-only; never returned in responses.

    - `type: "environment_variable"`

      - `"environment_variable"`

    - `injection_location: optional BetaManagedAgentsInjectionLocationParams`

      Where in the outbound request the secret value may be substituted.

      - `body: optional boolean`

        Substitute when the placeholder appears in the request body.

      - `header: optional boolean`

        Substitute when the placeholder appears in a request header value.

- `display_name: optional string`

  Human-readable name for the credential. Up to 255 characters.

- `metadata: optional map[string]`

  Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

### Returns

- `BetaManagedAgentsCredential object { id, archived_at, auth, 6 more }`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `BetaManagedAgentsMCPOAuthAuthResponse object { mcp_server_url, type, expires_at, refresh }`

      OAuth credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "mcp_oauth"`

        - `"mcp_oauth"`

      - `expires_at: optional string`

        A timestamp in RFC 3339 format

      - `refresh: optional BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: string`

          OAuth client ID.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `BetaManagedAgentsTokenEndpointAuthNoneResponse object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `BetaManagedAgentsTokenEndpointAuthBasicResponse object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `BetaManagedAgentsTokenEndpointAuthPostResponse object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `BetaManagedAgentsStaticBearerAuthResponse object { mcp_server_url, type }`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "static_bearer"`

        - `"static_bearer"`

    - `BetaManagedAgentsEnvironmentVariableAuthResponse object { injection_location, networking, secret_name, type }`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `BetaManagedAgentsUnrestrictedCredentialNetworkingResponse object { type }`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

            - `"unrestricted"`

        - `BetaManagedAgentsLimitedCredentialNetworkingResponse object { allowed_hosts, type }`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: array of string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: "limited"`

            - `"limited"`

      - `secret_name: string`

        Name of the environment variable.

      - `type: "environment_variable"`

        - `"environment_variable"`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the credential.

  - `type: "vault_credential"`

    - `"vault_credential"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name: optional string`

    Human-readable name for the credential.

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "auth": {
            "token": "bearer_exampletoken",
            "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
            "type": "static_bearer"
          },
          "display_name": "Example credential",
          "metadata": {
            "environment": "production"
          }
        }'
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

**get** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Path Parameters

- `vault_id: string`

### Query Parameters

- `include_archived: optional boolean`

  Whether to include archived credentials in the results.

- `limit: optional number`

  Maximum number of credentials to return per page. Defaults to 20, maximum 100.

- `page: optional string`

  Opaque pagination token from a previous `list_credentials` response.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `data: optional array of BetaManagedAgentsCredential`

  List of credentials.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `BetaManagedAgentsMCPOAuthAuthResponse object { mcp_server_url, type, expires_at, refresh }`

      OAuth credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "mcp_oauth"`

        - `"mcp_oauth"`

      - `expires_at: optional string`

        A timestamp in RFC 3339 format

      - `refresh: optional BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: string`

          OAuth client ID.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `BetaManagedAgentsTokenEndpointAuthNoneResponse object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `BetaManagedAgentsTokenEndpointAuthBasicResponse object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `BetaManagedAgentsTokenEndpointAuthPostResponse object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `BetaManagedAgentsStaticBearerAuthResponse object { mcp_server_url, type }`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "static_bearer"`

        - `"static_bearer"`

    - `BetaManagedAgentsEnvironmentVariableAuthResponse object { injection_location, networking, secret_name, type }`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `BetaManagedAgentsUnrestrictedCredentialNetworkingResponse object { type }`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

            - `"unrestricted"`

        - `BetaManagedAgentsLimitedCredentialNetworkingResponse object { allowed_hosts, type }`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: array of string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: "limited"`

            - `"limited"`

      - `secret_name: string`

        Name of the environment variable.

      - `type: "environment_variable"`

        - `"environment_variable"`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the credential.

  - `type: "vault_credential"`

    - `"vault_credential"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name: optional string`

    Human-readable name for the credential.

- `next_page: optional string`

  Pagination token for the next page, or null if no more results.

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

### Path Parameters

- `vault_id: string`

- `credential_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsCredential object { id, archived_at, auth, 6 more }`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `BetaManagedAgentsMCPOAuthAuthResponse object { mcp_server_url, type, expires_at, refresh }`

      OAuth credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "mcp_oauth"`

        - `"mcp_oauth"`

      - `expires_at: optional string`

        A timestamp in RFC 3339 format

      - `refresh: optional BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: string`

          OAuth client ID.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `BetaManagedAgentsTokenEndpointAuthNoneResponse object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `BetaManagedAgentsTokenEndpointAuthBasicResponse object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `BetaManagedAgentsTokenEndpointAuthPostResponse object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `BetaManagedAgentsStaticBearerAuthResponse object { mcp_server_url, type }`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "static_bearer"`

        - `"static_bearer"`

    - `BetaManagedAgentsEnvironmentVariableAuthResponse object { injection_location, networking, secret_name, type }`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `BetaManagedAgentsUnrestrictedCredentialNetworkingResponse object { type }`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

            - `"unrestricted"`

        - `BetaManagedAgentsLimitedCredentialNetworkingResponse object { allowed_hosts, type }`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: array of string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: "limited"`

            - `"limited"`

      - `secret_name: string`

        Name of the environment variable.

      - `type: "environment_variable"`

        - `"environment_variable"`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the credential.

  - `type: "vault_credential"`

    - `"vault_credential"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name: optional string`

    Human-readable name for the credential.

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Path Parameters

- `vault_id: string`

- `credential_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `auth: optional BetaManagedAgentsMCPOAuthUpdateParams or BetaManagedAgentsStaticBearerUpdateParams or BetaManagedAgentsEnvironmentVariableUpdateParams`

  Updated authentication details for a credential.

  - `BetaManagedAgentsMCPOAuthUpdateParams object { type, access_token, expires_at, refresh }`

    Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

    - `type: "mcp_oauth"`

      - `"mcp_oauth"`

    - `access_token: optional string`

      Updated OAuth access token.

    - `expires_at: optional string`

      A timestamp in RFC 3339 format

    - `refresh: optional BetaManagedAgentsMCPOAuthRefreshUpdateParams`

      Parameters for updating OAuth refresh token configuration.

      - `refresh_token: optional string`

        Updated OAuth refresh token.

      - `scope: optional string`

        Updated OAuth scope for the refresh request.

      - `token_endpoint_auth: optional BetaManagedAgentsTokenEndpointAuthBasicUpdateParam or BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `BetaManagedAgentsTokenEndpointAuthBasicUpdateParam object { type, client_secret }`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `type: "client_secret_basic"`

            - `"client_secret_basic"`

          - `client_secret: optional string`

            Updated OAuth client secret.

        - `BetaManagedAgentsTokenEndpointAuthPostUpdateParam object { type, client_secret }`

          Updated POST body authentication parameters for the token endpoint.

          - `type: "client_secret_post"`

            - `"client_secret_post"`

          - `client_secret: optional string`

            Updated OAuth client secret.

  - `BetaManagedAgentsStaticBearerUpdateParams object { type, token }`

    Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

    - `type: "static_bearer"`

      - `"static_bearer"`

    - `token: optional string`

      Updated static bearer token value.

  - `BetaManagedAgentsEnvironmentVariableUpdateParams object { type, injection_location, networking, secret_value }`

    Parameters for updating an environment variable credential. `secret_name` is immutable.

    - `type: "environment_variable"`

      - `"environment_variable"`

    - `injection_location: optional BetaManagedAgentsInjectionLocationUpdateParams`

      Updated injection location.

      - `body: optional boolean`

        Substitute when the placeholder appears in the request body.

      - `header: optional boolean`

        Substitute when the placeholder appears in a request header value.

    - `networking: optional BetaManagedAgentsCredentialNetworkingParams`

      Updated networking scope. Full replacement.

      - `BetaManagedAgentsUnrestrictedCredentialNetworkingParams object { type }`

        Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

        - `type: "unrestricted"`

          - `"unrestricted"`

      - `BetaManagedAgentsLimitedCredentialNetworkingParams object { allowed_hosts, type }`

        Substitute the secret only on requests to the listed hosts.

        - `allowed_hosts: array of string`

          Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

        - `type: "limited"`

          - `"limited"`

    - `secret_value: optional string`

      Updated secret value.

- `display_name: optional string`

  Updated human-readable name for the credential. 1-255 characters.

- `metadata: optional map[string]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

### Returns

- `BetaManagedAgentsCredential object { id, archived_at, auth, 6 more }`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `BetaManagedAgentsMCPOAuthAuthResponse object { mcp_server_url, type, expires_at, refresh }`

      OAuth credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "mcp_oauth"`

        - `"mcp_oauth"`

      - `expires_at: optional string`

        A timestamp in RFC 3339 format

      - `refresh: optional BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: string`

          OAuth client ID.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `BetaManagedAgentsTokenEndpointAuthNoneResponse object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `BetaManagedAgentsTokenEndpointAuthBasicResponse object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `BetaManagedAgentsTokenEndpointAuthPostResponse object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `BetaManagedAgentsStaticBearerAuthResponse object { mcp_server_url, type }`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "static_bearer"`

        - `"static_bearer"`

    - `BetaManagedAgentsEnvironmentVariableAuthResponse object { injection_location, networking, secret_name, type }`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `BetaManagedAgentsUnrestrictedCredentialNetworkingResponse object { type }`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

            - `"unrestricted"`

        - `BetaManagedAgentsLimitedCredentialNetworkingResponse object { allowed_hosts, type }`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: array of string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: "limited"`

            - `"limited"`

      - `secret_name: string`

        Name of the environment variable.

      - `type: "environment_variable"`

        - `"environment_variable"`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the credential.

  - `type: "vault_credential"`

    - `"vault_credential"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name: optional string`

    Human-readable name for the credential.

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "display_name": "Example credential",
          "metadata": {
            "environment": "production"
          }
        }'
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

**delete** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

### Path Parameters

- `vault_id: string`

- `credential_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsDeletedCredential object { id, type }`

  Confirmation of a deleted credential.

  - `id: string`

    Unique identifier of the deleted credential.

  - `type: "vault_credential_deleted"`

    - `"vault_credential_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

## Archive Credential

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

### Path Parameters

- `vault_id: string`

- `credential_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsCredential object { id, archived_at, auth, 6 more }`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `BetaManagedAgentsMCPOAuthAuthResponse object { mcp_server_url, type, expires_at, refresh }`

      OAuth credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "mcp_oauth"`

        - `"mcp_oauth"`

      - `expires_at: optional string`

        A timestamp in RFC 3339 format

      - `refresh: optional BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: string`

          OAuth client ID.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `BetaManagedAgentsTokenEndpointAuthNoneResponse object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `BetaManagedAgentsTokenEndpointAuthBasicResponse object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `BetaManagedAgentsTokenEndpointAuthPostResponse object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `BetaManagedAgentsStaticBearerAuthResponse object { mcp_server_url, type }`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "static_bearer"`

        - `"static_bearer"`

    - `BetaManagedAgentsEnvironmentVariableAuthResponse object { injection_location, networking, secret_name, type }`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `BetaManagedAgentsUnrestrictedCredentialNetworkingResponse object { type }`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

            - `"unrestricted"`

        - `BetaManagedAgentsLimitedCredentialNetworkingResponse object { allowed_hosts, type }`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: array of string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: "limited"`

            - `"limited"`

      - `secret_name: string`

        Name of the environment variable.

      - `type: "environment_variable"`

        - `"environment_variable"`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the credential.

  - `type: "vault_credential"`

    - `"vault_credential"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name: optional string`

    Human-readable name for the credential.

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

### Path Parameters

- `vault_id: string`

- `credential_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsCredentialValidation object { credential_id, has_refresh_token, mcp_probe, 5 more }`

  Result of live-probing a credential against its configured MCP server.

  - `credential_id: string`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: boolean`

    Whether the credential has a refresh token configured.

  - `mcp_probe: BetaManagedAgentsMCPProbe`

    The failing step of an MCP validation probe.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

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

  - `refresh: BetaManagedAgentsRefreshObject`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

    - `status: "succeeded" or "failed" or "connect_error" or "no_refresh_token"`

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

  - `type: "vault_credential_validation"`

    - `"vault_credential_validation"`

  - `validated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault containing the credential.

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID/mcp_oauth_validate \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `BetaManagedAgentsCredential object { id, archived_at, auth, 6 more }`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `BetaManagedAgentsMCPOAuthAuthResponse object { mcp_server_url, type, expires_at, refresh }`

      OAuth credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "mcp_oauth"`

        - `"mcp_oauth"`

      - `expires_at: optional string`

        A timestamp in RFC 3339 format

      - `refresh: optional BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: string`

          OAuth client ID.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `BetaManagedAgentsTokenEndpointAuthNoneResponse object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `BetaManagedAgentsTokenEndpointAuthBasicResponse object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `BetaManagedAgentsTokenEndpointAuthPostResponse object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `BetaManagedAgentsStaticBearerAuthResponse object { mcp_server_url, type }`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "static_bearer"`

        - `"static_bearer"`

    - `BetaManagedAgentsEnvironmentVariableAuthResponse object { injection_location, networking, secret_name, type }`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `BetaManagedAgentsUnrestrictedCredentialNetworkingResponse object { type }`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

            - `"unrestricted"`

        - `BetaManagedAgentsLimitedCredentialNetworkingResponse object { allowed_hosts, type }`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: array of string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: "limited"`

            - `"limited"`

      - `secret_name: string`

        Name of the environment variable.

      - `type: "environment_variable"`

        - `"environment_variable"`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the credential.

  - `type: "vault_credential"`

    - `"vault_credential"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name: optional string`

    Human-readable name for the credential.

### Beta Managed Agents Credential Networking Params

- `BetaManagedAgentsCredentialNetworkingParams = BetaManagedAgentsUnrestrictedCredentialNetworkingParams or BetaManagedAgentsLimitedCredentialNetworkingParams`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `BetaManagedAgentsUnrestrictedCredentialNetworkingParams object { type }`

    Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

    - `type: "unrestricted"`

      - `"unrestricted"`

  - `BetaManagedAgentsLimitedCredentialNetworkingParams object { allowed_hosts, type }`

    Substitute the secret only on requests to the listed hosts.

    - `allowed_hosts: array of string`

      Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

    - `type: "limited"`

      - `"limited"`

### Beta Managed Agents Credential Validation

- `BetaManagedAgentsCredentialValidation object { credential_id, has_refresh_token, mcp_probe, 5 more }`

  Result of live-probing a credential against its configured MCP server.

  - `credential_id: string`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: boolean`

    Whether the credential has a refresh token configured.

  - `mcp_probe: BetaManagedAgentsMCPProbe`

    The failing step of an MCP validation probe.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

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

  - `refresh: BetaManagedAgentsRefreshObject`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

    - `status: "succeeded" or "failed" or "connect_error" or "no_refresh_token"`

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

  - `type: "vault_credential_validation"`

    - `"vault_credential_validation"`

  - `validated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault containing the credential.

### Beta Managed Agents Credential Validation Status

- `BetaManagedAgentsCredentialValidationStatus = "valid" or "invalid" or "unknown"`

  Overall verdict of a credential validation probe.

  - `"valid"`

  - `"invalid"`

  - `"unknown"`

### Beta Managed Agents Deleted Credential

- `BetaManagedAgentsDeletedCredential object { id, type }`

  Confirmation of a deleted credential.

  - `id: string`

    Unique identifier of the deleted credential.

  - `type: "vault_credential_deleted"`

    - `"vault_credential_deleted"`

### Beta Managed Agents Environment Variable Auth Response

- `BetaManagedAgentsEnvironmentVariableAuthResponse object { injection_location, networking, secret_name, type }`

  Environment variable credential details. The secret value is never returned.

  - `injection_location: BetaManagedAgentsInjectionLocationResponse`

    Where in the outbound request the secret value is substituted.

    - `body: boolean`

      Whether the placeholder is substituted in the request body.

    - `header: boolean`

      Whether the placeholder is substituted in request header values.

  - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

    Outbound hosts the secret value is substituted on.

    - `BetaManagedAgentsUnrestrictedCredentialNetworkingResponse object { type }`

      The secret is substituted on any host the session's Environment network policy permits egress to.

      - `type: "unrestricted"`

        - `"unrestricted"`

    - `BetaManagedAgentsLimitedCredentialNetworkingResponse object { allowed_hosts, type }`

      The secret is substituted only on requests to the listed hosts.

      - `allowed_hosts: array of string`

        Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

      - `type: "limited"`

        - `"limited"`

  - `secret_name: string`

    Name of the environment variable.

  - `type: "environment_variable"`

    - `"environment_variable"`

### Beta Managed Agents Environment Variable Create Params

- `BetaManagedAgentsEnvironmentVariableCreateParams object { networking, secret_name, secret_value, 2 more }`

  Parameters for creating an environment variable credential.

  - `networking: BetaManagedAgentsCredentialNetworkingParams`

    Outbound hosts the secret value is substituted on.

    - `BetaManagedAgentsUnrestrictedCredentialNetworkingParams object { type }`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `type: "unrestricted"`

        - `"unrestricted"`

    - `BetaManagedAgentsLimitedCredentialNetworkingParams object { allowed_hosts, type }`

      Substitute the secret only on requests to the listed hosts.

      - `allowed_hosts: array of string`

        Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

      - `type: "limited"`

        - `"limited"`

  - `secret_name: string`

    Name of the environment variable. Immutable after create.

  - `secret_value: string`

    Secret value. Write-only; never returned in responses.

  - `type: "environment_variable"`

    - `"environment_variable"`

  - `injection_location: optional BetaManagedAgentsInjectionLocationParams`

    Where in the outbound request the secret value may be substituted.

    - `body: optional boolean`

      Substitute when the placeholder appears in the request body.

    - `header: optional boolean`

      Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Environment Variable Update Params

- `BetaManagedAgentsEnvironmentVariableUpdateParams object { type, injection_location, networking, secret_value }`

  Parameters for updating an environment variable credential. `secret_name` is immutable.

  - `type: "environment_variable"`

    - `"environment_variable"`

  - `injection_location: optional BetaManagedAgentsInjectionLocationUpdateParams`

    Updated injection location.

    - `body: optional boolean`

      Substitute when the placeholder appears in the request body.

    - `header: optional boolean`

      Substitute when the placeholder appears in a request header value.

  - `networking: optional BetaManagedAgentsCredentialNetworkingParams`

    Updated networking scope. Full replacement.

    - `BetaManagedAgentsUnrestrictedCredentialNetworkingParams object { type }`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `type: "unrestricted"`

        - `"unrestricted"`

    - `BetaManagedAgentsLimitedCredentialNetworkingParams object { allowed_hosts, type }`

      Substitute the secret only on requests to the listed hosts.

      - `allowed_hosts: array of string`

        Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

      - `type: "limited"`

        - `"limited"`

  - `secret_value: optional string`

    Updated secret value.

### Beta Managed Agents Injection Location Params

- `BetaManagedAgentsInjectionLocationParams object { body, header }`

  Where in the outbound request the secret value may be substituted.

  - `body: optional boolean`

    Substitute when the placeholder appears in the request body.

  - `header: optional boolean`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Injection Location Response

- `BetaManagedAgentsInjectionLocationResponse object { body, header }`

  Where in the outbound request the secret value is substituted.

  - `body: boolean`

    Whether the placeholder is substituted in the request body.

  - `header: boolean`

    Whether the placeholder is substituted in request header values.

### Beta Managed Agents Injection Location Update Params

- `BetaManagedAgentsInjectionLocationUpdateParams object { body, header }`

  Updated injection location.

  - `body: optional boolean`

    Substitute when the placeholder appears in the request body.

  - `header: optional boolean`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Limited Credential Networking Params

- `BetaManagedAgentsLimitedCredentialNetworkingParams object { allowed_hosts, type }`

  Substitute the secret only on requests to the listed hosts.

  - `allowed_hosts: array of string`

    Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

  - `type: "limited"`

    - `"limited"`

### Beta Managed Agents Limited Credential Networking Response

- `BetaManagedAgentsLimitedCredentialNetworkingResponse object { allowed_hosts, type }`

  The secret is substituted only on requests to the listed hosts.

  - `allowed_hosts: array of string`

    Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

  - `type: "limited"`

    - `"limited"`

### Beta Managed Agents MCP OAuth Auth Response

- `BetaManagedAgentsMCPOAuthAuthResponse object { mcp_server_url, type, expires_at, refresh }`

  OAuth credential details for an MCP server.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "mcp_oauth"`

    - `"mcp_oauth"`

  - `expires_at: optional string`

    A timestamp in RFC 3339 format

  - `refresh: optional BetaManagedAgentsMCPOAuthRefreshResponse`

    OAuth refresh token configuration returned in credential responses.

    - `client_id: string`

      OAuth client ID.

    - `token_endpoint: string`

      Token endpoint URL used to refresh the access token.

    - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

      Token endpoint requires no client authentication.

      - `BetaManagedAgentsTokenEndpointAuthNoneResponse object { type }`

        Token endpoint requires no client authentication.

        - `type: "none"`

          - `"none"`

      - `BetaManagedAgentsTokenEndpointAuthBasicResponse object { type }`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `type: "client_secret_basic"`

          - `"client_secret_basic"`

      - `BetaManagedAgentsTokenEndpointAuthPostResponse object { type }`

        Token endpoint uses POST body authentication with client credentials.

        - `type: "client_secret_post"`

          - `"client_secret_post"`

    - `resource: optional string`

      OAuth resource indicator.

    - `scope: optional string`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Create Params

- `BetaManagedAgentsMCPOAuthCreateParams object { access_token, mcp_server_url, type, 2 more }`

  Parameters for creating an MCP OAuth credential.

  - `access_token: string`

    OAuth access token.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "mcp_oauth"`

    - `"mcp_oauth"`

  - `expires_at: optional string`

    A timestamp in RFC 3339 format

  - `refresh: optional BetaManagedAgentsMCPOAuthRefreshParams`

    OAuth refresh token parameters for creating a credential with refresh support.

    - `client_id: string`

      OAuth client ID.

    - `refresh_token: string`

      OAuth refresh token.

    - `token_endpoint: string`

      Token endpoint URL used to refresh the access token.

    - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam or BetaManagedAgentsTokenEndpointAuthBasicParam or BetaManagedAgentsTokenEndpointAuthPostParam`

      Token endpoint requires no client authentication.

      - `BetaManagedAgentsTokenEndpointAuthNoneParam object { type }`

        Token endpoint requires no client authentication.

        - `type: "none"`

          - `"none"`

      - `BetaManagedAgentsTokenEndpointAuthBasicParam object { client_secret, type }`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `client_secret: string`

          OAuth client secret.

        - `type: "client_secret_basic"`

          - `"client_secret_basic"`

      - `BetaManagedAgentsTokenEndpointAuthPostParam object { client_secret, type }`

        Token endpoint uses POST body authentication with client credentials.

        - `client_secret: string`

          OAuth client secret.

        - `type: "client_secret_post"`

          - `"client_secret_post"`

    - `resource: optional string`

      OAuth resource indicator.

    - `scope: optional string`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Params

- `BetaManagedAgentsMCPOAuthRefreshParams object { client_id, refresh_token, token_endpoint, 3 more }`

  OAuth refresh token parameters for creating a credential with refresh support.

  - `client_id: string`

    OAuth client ID.

  - `refresh_token: string`

    OAuth refresh token.

  - `token_endpoint: string`

    Token endpoint URL used to refresh the access token.

  - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam or BetaManagedAgentsTokenEndpointAuthBasicParam or BetaManagedAgentsTokenEndpointAuthPostParam`

    Token endpoint requires no client authentication.

    - `BetaManagedAgentsTokenEndpointAuthNoneParam object { type }`

      Token endpoint requires no client authentication.

      - `type: "none"`

        - `"none"`

    - `BetaManagedAgentsTokenEndpointAuthBasicParam object { client_secret, type }`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `client_secret: string`

        OAuth client secret.

      - `type: "client_secret_basic"`

        - `"client_secret_basic"`

    - `BetaManagedAgentsTokenEndpointAuthPostParam object { client_secret, type }`

      Token endpoint uses POST body authentication with client credentials.

      - `client_secret: string`

        OAuth client secret.

      - `type: "client_secret_post"`

        - `"client_secret_post"`

  - `resource: optional string`

    OAuth resource indicator.

  - `scope: optional string`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Response

- `BetaManagedAgentsMCPOAuthRefreshResponse object { client_id, token_endpoint, token_endpoint_auth, 2 more }`

  OAuth refresh token configuration returned in credential responses.

  - `client_id: string`

    OAuth client ID.

  - `token_endpoint: string`

    Token endpoint URL used to refresh the access token.

  - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

    Token endpoint requires no client authentication.

    - `BetaManagedAgentsTokenEndpointAuthNoneResponse object { type }`

      Token endpoint requires no client authentication.

      - `type: "none"`

        - `"none"`

    - `BetaManagedAgentsTokenEndpointAuthBasicResponse object { type }`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `type: "client_secret_basic"`

        - `"client_secret_basic"`

    - `BetaManagedAgentsTokenEndpointAuthPostResponse object { type }`

      Token endpoint uses POST body authentication with client credentials.

      - `type: "client_secret_post"`

        - `"client_secret_post"`

  - `resource: optional string`

    OAuth resource indicator.

  - `scope: optional string`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Update Params

- `BetaManagedAgentsMCPOAuthRefreshUpdateParams object { refresh_token, scope, token_endpoint_auth }`

  Parameters for updating OAuth refresh token configuration.

  - `refresh_token: optional string`

    Updated OAuth refresh token.

  - `scope: optional string`

    Updated OAuth scope for the refresh request.

  - `token_endpoint_auth: optional BetaManagedAgentsTokenEndpointAuthBasicUpdateParam or BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

    Updated HTTP Basic authentication parameters for the token endpoint.

    - `BetaManagedAgentsTokenEndpointAuthBasicUpdateParam object { type, client_secret }`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `type: "client_secret_basic"`

        - `"client_secret_basic"`

      - `client_secret: optional string`

        Updated OAuth client secret.

    - `BetaManagedAgentsTokenEndpointAuthPostUpdateParam object { type, client_secret }`

      Updated POST body authentication parameters for the token endpoint.

      - `type: "client_secret_post"`

        - `"client_secret_post"`

      - `client_secret: optional string`

        Updated OAuth client secret.

### Beta Managed Agents MCP OAuth Update Params

- `BetaManagedAgentsMCPOAuthUpdateParams object { type, access_token, expires_at, refresh }`

  Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

  - `type: "mcp_oauth"`

    - `"mcp_oauth"`

  - `access_token: optional string`

    Updated OAuth access token.

  - `expires_at: optional string`

    A timestamp in RFC 3339 format

  - `refresh: optional BetaManagedAgentsMCPOAuthRefreshUpdateParams`

    Parameters for updating OAuth refresh token configuration.

    - `refresh_token: optional string`

      Updated OAuth refresh token.

    - `scope: optional string`

      Updated OAuth scope for the refresh request.

    - `token_endpoint_auth: optional BetaManagedAgentsTokenEndpointAuthBasicUpdateParam or BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `BetaManagedAgentsTokenEndpointAuthBasicUpdateParam object { type, client_secret }`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `type: "client_secret_basic"`

          - `"client_secret_basic"`

        - `client_secret: optional string`

          Updated OAuth client secret.

      - `BetaManagedAgentsTokenEndpointAuthPostUpdateParam object { type, client_secret }`

        Updated POST body authentication parameters for the token endpoint.

        - `type: "client_secret_post"`

          - `"client_secret_post"`

        - `client_secret: optional string`

          Updated OAuth client secret.

### Beta Managed Agents MCP Probe

- `BetaManagedAgentsMCPProbe object { http_response, method }`

  The failing step of an MCP validation probe.

  - `http_response: BetaManagedAgentsRefreshHTTPResponse`

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

- `BetaManagedAgentsRefreshHTTPResponse object { body, body_truncated, content_type, status_code }`

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

- `BetaManagedAgentsRefreshObject object { http_response, status }`

  Outcome of a refresh-token exchange attempted during credential validation.

  - `http_response: BetaManagedAgentsRefreshHTTPResponse`

    An HTTP response captured during a credential validation probe.

    - `body: string`

      Response body. May be truncated and has sensitive values scrubbed.

    - `body_truncated: boolean`

      Whether `body` was truncated.

    - `content_type: string`

      Value of the `Content-Type` response header.

    - `status_code: number`

      HTTP status code.

  - `status: "succeeded" or "failed" or "connect_error" or "no_refresh_token"`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `"succeeded"`

    - `"failed"`

    - `"connect_error"`

    - `"no_refresh_token"`

### Beta Managed Agents Static Bearer Auth Response

- `BetaManagedAgentsStaticBearerAuthResponse object { mcp_server_url, type }`

  Static bearer token credential details for an MCP server.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "static_bearer"`

    - `"static_bearer"`

### Beta Managed Agents Static Bearer Create Params

- `BetaManagedAgentsStaticBearerCreateParams object { token, mcp_server_url, type }`

  Parameters for creating a static bearer token credential.

  - `token: string`

    Static bearer token value.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "static_bearer"`

    - `"static_bearer"`

### Beta Managed Agents Static Bearer Update Params

- `BetaManagedAgentsStaticBearerUpdateParams object { type, token }`

  Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

  - `type: "static_bearer"`

    - `"static_bearer"`

  - `token: optional string`

    Updated static bearer token value.

### Beta Managed Agents Token Endpoint Auth Basic Param

- `BetaManagedAgentsTokenEndpointAuthBasicParam object { client_secret, type }`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `client_secret: string`

    OAuth client secret.

  - `type: "client_secret_basic"`

    - `"client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Response

- `BetaManagedAgentsTokenEndpointAuthBasicResponse object { type }`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `type: "client_secret_basic"`

    - `"client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `BetaManagedAgentsTokenEndpointAuthBasicUpdateParam object { type, client_secret }`

  Updated HTTP Basic authentication parameters for the token endpoint.

  - `type: "client_secret_basic"`

    - `"client_secret_basic"`

  - `client_secret: optional string`

    Updated OAuth client secret.

### Beta Managed Agents Token Endpoint Auth None Param

- `BetaManagedAgentsTokenEndpointAuthNoneParam object { type }`

  Token endpoint requires no client authentication.

  - `type: "none"`

    - `"none"`

### Beta Managed Agents Token Endpoint Auth None Response

- `BetaManagedAgentsTokenEndpointAuthNoneResponse object { type }`

  Token endpoint requires no client authentication.

  - `type: "none"`

    - `"none"`

### Beta Managed Agents Token Endpoint Auth Post Param

- `BetaManagedAgentsTokenEndpointAuthPostParam object { client_secret, type }`

  Token endpoint uses POST body authentication with client credentials.

  - `client_secret: string`

    OAuth client secret.

  - `type: "client_secret_post"`

    - `"client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Response

- `BetaManagedAgentsTokenEndpointAuthPostResponse object { type }`

  Token endpoint uses POST body authentication with client credentials.

  - `type: "client_secret_post"`

    - `"client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `BetaManagedAgentsTokenEndpointAuthPostUpdateParam object { type, client_secret }`

  Updated POST body authentication parameters for the token endpoint.

  - `type: "client_secret_post"`

    - `"client_secret_post"`

  - `client_secret: optional string`

    Updated OAuth client secret.

### Beta Managed Agents Unrestricted Credential Networking Params

- `BetaManagedAgentsUnrestrictedCredentialNetworkingParams object { type }`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `type: "unrestricted"`

    - `"unrestricted"`

### Beta Managed Agents Unrestricted Credential Networking Response

- `BetaManagedAgentsUnrestrictedCredentialNetworkingResponse object { type }`

  The secret is substituted on any host the session's Environment network policy permits egress to.

  - `type: "unrestricted"`

    - `"unrestricted"`

# Memory Stores

## Create a memory store

**post** `/v1/memory_stores`

Create a memory store

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `name: string`

  Human-readable name for the store. Required; 1–255 characters; no control characters. The mount-path slug under `/mnt/memory/` is derived from this name (lowercased, non-alphanumeric runs collapsed to a hyphen). Names need not be unique within a workspace.

- `description: optional string`

  Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent.

- `metadata: optional map[string]`

  Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Not visible to the agent.

### Returns

- `BetaManagedAgentsMemoryStore object { id, created_at, name, 5 more }`

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

  - `archived_at: optional string`

    A timestamp in RFC 3339 format

  - `description: optional string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: optional map[string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```http
curl https://api.anthropic.com/v1/memory_stores \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "name": "x"
        }'
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

**get** `/v1/memory_stores`

List memory stores

### Query Parameters

- `"created_at[gte]": optional string`

  Return only stores whose `created_at` is at or after this time (inclusive). Sent on the wire as `created_at[gte]`.

- `"created_at[lte]": optional string`

  Return only stores whose `created_at` is at or before this time (inclusive). Sent on the wire as `created_at[lte]`.

- `include_archived: optional boolean`

  When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

- `limit: optional number`

  Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

- `page: optional string`

  Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `data: optional array of BetaManagedAgentsMemoryStore`

  Memory stores on this page, newest first. Empty when there are no stores matching the filters.

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

  - `archived_at: optional string`

    A timestamp in RFC 3339 format

  - `description: optional string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: optional map[string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

- `next_page: optional string`

  Opaque cursor for the next page (a `page_...` value). Pass as `page` on the next request. `null` when there are no more results.

### Example

```http
curl https://api.anthropic.com/v1/memory_stores \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/memory_stores/{memory_store_id}`

Retrieve a memory store

### Path Parameters

- `memory_store_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsMemoryStore object { id, created_at, name, 5 more }`

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

  - `archived_at: optional string`

    A timestamp in RFC 3339 format

  - `description: optional string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: optional map[string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/memory_stores/{memory_store_id}`

Update a memory store

### Path Parameters

- `memory_store_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `description: optional string`

  New description for the store, up to 1024 characters. Pass an empty string to clear it.

- `metadata: optional map[string]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `name: optional string`

  New human-readable name for the store. 1–255 characters; no control characters. Renaming changes the slug used for the store's `mount_path` in sessions created after the update.

### Returns

- `BetaManagedAgentsMemoryStore object { id, created_at, name, 5 more }`

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

  - `archived_at: optional string`

    A timestamp in RFC 3339 format

  - `description: optional string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: optional map[string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
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

**delete** `/v1/memory_stores/{memory_store_id}`

Delete a memory store

### Path Parameters

- `memory_store_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsDeletedMemoryStore object { id, type }`

  Confirmation that a `memory_store` was deleted.

  - `id: string`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `type: "memory_store_deleted"`

    - `"memory_store_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

## Archive a memory store

**post** `/v1/memory_stores/{memory_store_id}/archive`

Archive a memory store

### Path Parameters

- `memory_store_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsMemoryStore object { id, created_at, name, 5 more }`

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

  - `archived_at: optional string`

    A timestamp in RFC 3339 format

  - `description: optional string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: optional map[string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `BetaManagedAgentsDeletedMemoryStore object { id, type }`

  Confirmation that a `memory_store` was deleted.

  - `id: string`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `type: "memory_store_deleted"`

    - `"memory_store_deleted"`

### Beta Managed Agents Memory Store

- `BetaManagedAgentsMemoryStore object { id, created_at, name, 5 more }`

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

  - `archived_at: optional string`

    A timestamp in RFC 3339 format

  - `description: optional string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: optional map[string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

# Memories

## Create a memory

**post** `/v1/memory_stores/{memory_store_id}/memories`

Create a memory

### Path Parameters

- `memory_store_id: string`

### Query Parameters

- `view: optional BetaManagedAgentsMemoryView`

  Query parameter for view

  - `"basic"`

  - `"full"`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `content: string`

  UTF-8 text content for the new memory. Maximum 100 kB (102,400 bytes). Required; pass `""` explicitly to create an empty memory.

- `path: string`

  Hierarchical path for the new memory, e.g. `/projects/foo/notes.md`. Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive.

### Returns

- `BetaManagedAgentsMemory object { id, content_sha256, content_size_bytes, 7 more }`

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

  - `content: optional string`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "content": "content",
          "path": "xx"
        }'
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

**get** `/v1/memory_stores/{memory_store_id}/memories`

List memories

### Path Parameters

- `memory_store_id: string`

### Query Parameters

- `depth: optional number`

  `0` (or omitted) returns all descendants below `path_prefix` (recursive). `1` returns immediate children only; deeper entries roll up as `memory_prefix` items. `depth=1` behaves like `ls`; omitting `depth` behaves like `find`.

- `limit: optional number`

  Maximum number of items to return per page. Must be between 1 and 100. Defaults to 20 when omitted. Capped at 20 when `view=full`. Both `memory` and `memory_prefix` items count toward the limit.

- `page: optional string`

  Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

- `path_prefix: optional string`

  Optional path prefix filter. Must end with `/` (segment-aligned), e.g., `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

- `view: optional BetaManagedAgentsMemoryView`

  Which projection of each `memory` to return. Defaults to `basic` (content omitted). `full` populates `content` on each item and caps `limit` at 20; use this as the bulk-read path for export and sync.

  - `"basic"`

  - `"full"`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `data: optional array of BetaManagedAgentsMemoryListItem`

  One page of results. Each item is either a `memory` object or, when `depth` was set, a `memory_prefix` rollup marker. Items are returned in a stable, server-defined order.

  - `BetaManagedAgentsMemory object { id, content_sha256, content_size_bytes, 7 more }`

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

    - `content: optional string`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `BetaManagedAgentsMemoryPrefix object { path, type }`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `path: string`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `type: "memory_prefix"`

      - `"memory_prefix"`

- `next_page: optional string`

  Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a memory

### Path Parameters

- `memory_store_id: string`

- `memory_id: string`

### Query Parameters

- `view: optional BetaManagedAgentsMemoryView`

  Query parameter for view

  - `"basic"`

  - `"full"`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsMemory object { id, content_sha256, content_size_bytes, 7 more }`

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

  - `content: optional string`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories/$MEMORY_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a memory

### Path Parameters

- `memory_store_id: string`

- `memory_id: string`

### Query Parameters

- `view: optional BetaManagedAgentsMemoryView`

  Query parameter for view

  - `"basic"`

  - `"full"`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `content: optional string`

  New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

- `path: optional string`

  New path for the memory (a rename). Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive. The memory's `id` is preserved across renames. Omit to leave the path unchanged.

- `precondition: optional BetaManagedAgentsPrecondition`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `type: "content_sha256"`

    - `"content_sha256"`

  - `content_sha256: optional string`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

### Returns

- `BetaManagedAgentsMemory object { id, content_sha256, content_size_bytes, 7 more }`

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

  - `content: optional string`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories/$MEMORY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
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

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

### Path Parameters

- `memory_store_id: string`

- `memory_id: string`

### Query Parameters

- `expected_content_sha256: optional string`

  Query parameter for expected_content_sha256

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsDeletedMemory object { id, type }`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `id: string`

    ID of the deleted memory (a `mem_...` value).

  - `type: "memory_deleted"`

    - `"memory_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories/$MEMORY_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `BetaManagedAgentsConflictError object { type, message }`

  - `type: "conflict_error"`

    - `"conflict_error"`

  - `message: optional string`

### Beta Managed Agents Content Sha256 Precondition

- `BetaManagedAgentsContentSha256Precondition object { type, content_sha256 }`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `type: "content_sha256"`

    - `"content_sha256"`

  - `content_sha256: optional string`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

### Beta Managed Agents Deleted Memory

- `BetaManagedAgentsDeletedMemory object { id, type }`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `id: string`

    ID of the deleted memory (a `mem_...` value).

  - `type: "memory_deleted"`

    - `"memory_deleted"`

### Beta Managed Agents Error

- `BetaManagedAgentsError = BetaInvalidRequestError or BetaAuthenticationError or BetaBillingError or 9 more`

  - `BetaInvalidRequestError object { message, type }`

    - `message: string`

    - `type: "invalid_request_error"`

      - `"invalid_request_error"`

  - `BetaAuthenticationError object { message, type }`

    - `message: string`

    - `type: "authentication_error"`

      - `"authentication_error"`

  - `BetaBillingError object { message, type }`

    - `message: string`

    - `type: "billing_error"`

      - `"billing_error"`

  - `BetaPermissionError object { message, type }`

    - `message: string`

    - `type: "permission_error"`

      - `"permission_error"`

  - `BetaNotFoundError object { message, type }`

    - `message: string`

    - `type: "not_found_error"`

      - `"not_found_error"`

  - `BetaRateLimitError object { message, type }`

    - `message: string`

    - `type: "rate_limit_error"`

      - `"rate_limit_error"`

  - `BetaGatewayTimeoutError object { message, type }`

    - `message: string`

    - `type: "timeout_error"`

      - `"timeout_error"`

  - `BetaAPIError object { message, type }`

    - `message: string`

    - `type: "api_error"`

      - `"api_error"`

  - `BetaOverloadedError object { message, type }`

    - `message: string`

    - `type: "overloaded_error"`

      - `"overloaded_error"`

  - `BetaManagedAgentsMemoryPreconditionFailedError object { type, message }`

    - `type: "memory_precondition_failed_error"`

      - `"memory_precondition_failed_error"`

    - `message: optional string`

  - `BetaManagedAgentsMemoryPathConflictError object { type, conflicting_memory_id, conflicting_path, message }`

    - `type: "memory_path_conflict_error"`

      - `"memory_path_conflict_error"`

    - `conflicting_memory_id: optional string`

    - `conflicting_path: optional string`

    - `message: optional string`

  - `BetaManagedAgentsConflictError object { type, message }`

    - `type: "conflict_error"`

      - `"conflict_error"`

    - `message: optional string`

### Beta Managed Agents Memory

- `BetaManagedAgentsMemory object { id, content_sha256, content_size_bytes, 7 more }`

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

  - `content: optional string`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Beta Managed Agents Memory List Item

- `BetaManagedAgentsMemoryListItem = BetaManagedAgentsMemory or BetaManagedAgentsMemoryPrefix`

  One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

  - `BetaManagedAgentsMemory object { id, content_sha256, content_size_bytes, 7 more }`

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

    - `content: optional string`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `BetaManagedAgentsMemoryPrefix object { path, type }`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `path: string`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `type: "memory_prefix"`

      - `"memory_prefix"`

### Beta Managed Agents Memory Path Conflict Error

- `BetaManagedAgentsMemoryPathConflictError object { type, conflicting_memory_id, conflicting_path, message }`

  - `type: "memory_path_conflict_error"`

    - `"memory_path_conflict_error"`

  - `conflicting_memory_id: optional string`

  - `conflicting_path: optional string`

  - `message: optional string`

### Beta Managed Agents Memory Precondition Failed Error

- `BetaManagedAgentsMemoryPreconditionFailedError object { type, message }`

  - `type: "memory_precondition_failed_error"`

    - `"memory_precondition_failed_error"`

  - `message: optional string`

### Beta Managed Agents Memory Prefix

- `BetaManagedAgentsMemoryPrefix object { path, type }`

  A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

  - `path: string`

    The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

  - `type: "memory_prefix"`

    - `"memory_prefix"`

### Beta Managed Agents Memory View

- `BetaManagedAgentsMemoryView = "basic" or "full"`

  Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

  - `"basic"`

  - `"full"`

### Beta Managed Agents Precondition

- `BetaManagedAgentsPrecondition object { type, content_sha256 }`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `type: "content_sha256"`

    - `"content_sha256"`

  - `content_sha256: optional string`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

# Memory Versions

## List memory versions

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

### Path Parameters

- `memory_store_id: string`

### Query Parameters

- `api_key_id: optional string`

  Query parameter for api_key_id

- `"created_at[gte]": optional string`

  Return versions created at or after this time (inclusive).

- `"created_at[lte]": optional string`

  Return versions created at or before this time (inclusive).

- `limit: optional number`

  Query parameter for limit

- `memory_id: optional string`

  Query parameter for memory_id

- `operation: optional BetaManagedAgentsMemoryVersionOperation`

  Query parameter for operation

  - `"created"`

  - `"modified"`

  - `"deleted"`

- `page: optional string`

  Query parameter for page

- `session_id: optional string`

  Query parameter for session_id

- `view: optional BetaManagedAgentsMemoryView`

  Query parameter for view

  - `"basic"`

  - `"full"`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `data: optional array of BetaManagedAgentsMemoryVersion`

  One page of `memory_version` objects, ordered by `created_at` descending (newest first), with `id` as tiebreak.

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

  - `content: optional string`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: optional string`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: optional number`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by: optional BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `BetaManagedAgentsSessionActor object { session_id, type }`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor object { api_key_id, type }`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor object { type, user_id }`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

        ID of the user who performed the write (a `user_...` value).

  - `path: optional string`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

  - `redacted_by: optional BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

- `next_page: optional string`

  Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

### Path Parameters

- `memory_store_id: string`

- `memory_version_id: string`

### Query Parameters

- `view: optional BetaManagedAgentsMemoryView`

  Query parameter for view

  - `"basic"`

  - `"full"`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsMemoryVersion object { id, created_at, memory_id, 10 more }`

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

  - `content: optional string`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: optional string`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: optional number`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by: optional BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `BetaManagedAgentsSessionActor object { session_id, type }`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor object { api_key_id, type }`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor object { type, user_id }`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

        ID of the user who performed the write (a `user_...` value).

  - `path: optional string`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

  - `redacted_by: optional BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions/$MEMORY_VERSION_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a memory version

### Path Parameters

- `memory_store_id: string`

- `memory_version_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaManagedAgentsMemoryVersion object { id, created_at, memory_id, 10 more }`

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

  - `content: optional string`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: optional string`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: optional number`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by: optional BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `BetaManagedAgentsSessionActor object { session_id, type }`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor object { api_key_id, type }`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor object { type, user_id }`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

        ID of the user who performed the write (a `user_...` value).

  - `path: optional string`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

  - `redacted_by: optional BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions/$MEMORY_VERSION_ID/redact \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `BetaManagedAgentsActor = BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

  Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

  - `BetaManagedAgentsSessionActor object { session_id, type }`

    Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

    - `session_id: string`

      ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

    - `type: "session_actor"`

      - `"session_actor"`

  - `BetaManagedAgentsAPIActor object { api_key_id, type }`

    Attribution for a write made directly via the public API (outside of any session).

    - `api_key_id: string`

      ID of the API key that performed the write. This identifies the key, not the secret.

    - `type: "api_actor"`

      - `"api_actor"`

  - `BetaManagedAgentsUserActor object { type, user_id }`

    Attribution for a write made by a human user through the Anthropic Console.

    - `type: "user_actor"`

      - `"user_actor"`

    - `user_id: string`

      ID of the user who performed the write (a `user_...` value).

### Beta Managed Agents API Actor

- `BetaManagedAgentsAPIActor object { api_key_id, type }`

  Attribution for a write made directly via the public API (outside of any session).

  - `api_key_id: string`

    ID of the API key that performed the write. This identifies the key, not the secret.

  - `type: "api_actor"`

    - `"api_actor"`

### Beta Managed Agents Memory Version

- `BetaManagedAgentsMemoryVersion object { id, created_at, memory_id, 10 more }`

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

  - `content: optional string`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: optional string`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: optional number`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by: optional BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `BetaManagedAgentsSessionActor object { session_id, type }`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor object { api_key_id, type }`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor object { type, user_id }`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

        ID of the user who performed the write (a `user_...` value).

  - `path: optional string`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

  - `redacted_by: optional BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Beta Managed Agents Memory Version Operation

- `BetaManagedAgentsMemoryVersionOperation = "created" or "modified" or "deleted"`

  The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

  - `"created"`

  - `"modified"`

  - `"deleted"`

### Beta Managed Agents Session Actor

- `BetaManagedAgentsSessionActor object { session_id, type }`

  Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

  - `session_id: string`

    ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

  - `type: "session_actor"`

    - `"session_actor"`

### Beta Managed Agents User Actor

- `BetaManagedAgentsUserActor object { type, user_id }`

  Attribution for a write made by a human user through the Anthropic Console.

  - `type: "user_actor"`

    - `"user_actor"`

  - `user_id: string`

    ID of the user who performed the write (a `user_...` value).

# Files

## Upload File

**post** `/v1/files`

Upload File

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `FileMetadata object { id, created_at, filename, 5 more }`

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

  - `downloadable: optional boolean`

    Whether the file can be downloaded.

  - `scope: optional BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

      - `"session"`

### Example

```http
curl https://api.anthropic.com/v1/files \
    -H 'Content-Type: multipart/form-data' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: files-api-2025-04-14' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -F 'file=@/path/to/file'
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

**get** `/v1/files`

List Files

### Query Parameters

- `after_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `scope_id: optional string`

  Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `data: array of FileMetadata`

  List of file metadata objects.

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

  - `downloadable: optional boolean`

    Whether the file can be downloaded.

  - `scope: optional BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

      - `"session"`

- `first_id: optional string`

  ID of the first file in this page of results.

- `has_more: optional boolean`

  Whether there are more results available.

- `last_id: optional string`

  ID of the last file in this page of results.

### Example

```http
curl https://api.anthropic.com/v1/files \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: files-api-2025-04-14' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/files/{file_id}/content`

Download File

### Path Parameters

- `file_id: string`

  ID of the File.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Example

```http
curl https://api.anthropic.com/v1/files/$FILE_ID/content \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: files-api-2025-04-14' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Get File Metadata

**get** `/v1/files/{file_id}`

Get File Metadata

### Path Parameters

- `file_id: string`

  ID of the File.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `FileMetadata object { id, created_at, filename, 5 more }`

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

  - `downloadable: optional boolean`

    Whether the file can be downloaded.

  - `scope: optional BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

      - `"session"`

### Example

```http
curl https://api.anthropic.com/v1/files/$FILE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: files-api-2025-04-14' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**delete** `/v1/files/{file_id}`

Delete File

### Path Parameters

- `file_id: string`

  ID of the File.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `DeletedFile object { id, type }`

  - `id: string`

    ID of the deleted file.

  - `type: optional "file_deleted"`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/files/$FILE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: files-api-2025-04-14' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `BetaFileScope object { id, type }`

  - `id: string`

    The ID of the scoping resource (e.g., the session ID).

  - `type: "session"`

    The type of scope (e.g., `"session"`).

    - `"session"`

### Deleted File

- `DeletedFile object { id, type }`

  - `id: string`

    ID of the deleted file.

  - `type: optional "file_deleted"`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"`

### File Metadata

- `FileMetadata object { id, created_at, filename, 5 more }`

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

  - `downloadable: optional boolean`

    Whether the file can be downloaded.

  - `scope: optional BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

      - `"session"`

# Skills

## Create Skill

**post** `/v1/skills`

Create Skill

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `created_at: string`

  ISO 8601 timestamp of when the skill was created.

- `display_title: string`

  Display title for the skill.

  This is a human-readable label that is not included in the prompt sent to the model.

- `latest_version: string`

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

```http
curl https://api.anthropic.com/v1/skills \
    -H 'Content-Type: multipart/form-data' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: skills-2025-10-02' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -F files='["Example data"]'
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

**get** `/v1/skills`

List Skills

### Query Parameters

- `limit: optional number`

  Number of results to return per page.

  Maximum value is 100. Defaults to 20.

- `page: optional string`

  Pagination token for fetching a specific page of results.

  Pass the value from a previous response's `next_page` field to get the next page of results.

- `source: optional string`

  Filter skills by source.

  If provided, only skills from the specified source will be returned:

  * `"custom"`: only return user-created skills
  * `"anthropic"`: only return Anthropic-created skills

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `data: array of object { id, created_at, display_title, 4 more }`

  List of skills.

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: string`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: string`

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

- `has_more: boolean`

  Whether there are more results available.

  If `true`, there are additional results that can be fetched using the `next_page` token.

- `next_page: string`

  Token for fetching the next page of results.

  If `null`, there are no more results available. Pass this value to the `page_token` parameter in the next request to get the next page.

### Example

```http
curl https://api.anthropic.com/v1/skills \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: skills-2025-10-02' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/skills/{skill_id}`

Get Skill

### Path Parameters

- `skill_id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `created_at: string`

  ISO 8601 timestamp of when the skill was created.

- `display_title: string`

  Display title for the skill.

  This is a human-readable label that is not included in the prompt sent to the model.

- `latest_version: string`

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

```http
curl https://api.anthropic.com/v1/skills/$SKILL_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: skills-2025-10-02' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**delete** `/v1/skills/{skill_id}`

Delete Skill

### Path Parameters

- `skill_id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `type: string`

  Deleted object type.

  For Skills, this is always `"skill_deleted"`.

### Example

```http
curl https://api.anthropic.com/v1/skills/$SKILL_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: skills-2025-10-02' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `SkillCreateResponse object { id, created_at, display_title, 4 more }`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: string`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: string`

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

- `SkillListResponse object { id, created_at, display_title, 4 more }`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: string`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: string`

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

- `SkillRetrieveResponse object { id, created_at, display_title, 4 more }`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: string`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: string`

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

- `SkillDeleteResponse object { id, type }`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `type: string`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

# Versions

## Create Skill Version

**post** `/v1/skills/{skill_id}/versions`

Create Skill Version

### Path Parameters

- `skill_id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

```http
curl https://api.anthropic.com/v1/skills/$SKILL_ID/versions \
    -H 'Content-Type: multipart/form-data' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: skills-2025-10-02' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -F files='["Example data"]'
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

**get** `/v1/skills/{skill_id}/versions`

List Skill Versions

### Path Parameters

- `skill_id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

### Query Parameters

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `data: array of object { id, created_at, description, 5 more }`

  List of skill versions.

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

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `next_page: string`

  Token to provide in as `page` in the subsequent request to retrieve the next page of data.

### Example

```http
curl https://api.anthropic.com/v1/skills/$SKILL_ID/versions \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: skills-2025-10-02' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

### Path Parameters

- `skill_id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: string`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Example

```http
curl https://api.anthropic.com/v1/skills/$SKILL_ID/versions/$VERSION/content \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: skills-2025-10-02' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Get Skill Version

**get** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

### Path Parameters

- `skill_id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: string`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

```http
curl https://api.anthropic.com/v1/skills/$SKILL_ID/versions/$VERSION \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: skills-2025-10-02' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**delete** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

### Path Parameters

- `skill_id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: string`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `id: string`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `type: string`

  Deleted object type.

  For Skill Versions, this is always `"skill_version_deleted"`.

### Example

```http
curl https://api.anthropic.com/v1/skills/$SKILL_ID/versions/$VERSION \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: skills-2025-10-02' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `VersionCreateResponse object { id, created_at, description, 5 more }`

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

- `VersionListResponse object { id, created_at, description, 5 more }`

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

- `VersionRetrieveResponse object { id, created_at, description, 5 more }`

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

- `VersionDeleteResponse object { id, type }`

  - `id: string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `type: string`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

# User Profiles

## Create User Profile

**post** `/v1/user_profiles`

Create User Profile

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `external_id: optional string`

  Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

- `metadata: optional map[string]`

  Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

- `name: optional string`

  Display name of the entity this profile represents. Required when relationship is `resold` (the resold-to company's name); optional otherwise. Maximum 255 characters.

- `relationship: optional "external" or "resold" or "internal"`

  How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

  - `"external"`

  - `"resold"`

  - `"internal"`

### Returns

- `BetaUserProfile object { id, created_at, metadata, 6 more }`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `relationship: "external" or "resold" or "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

  - `trust_grants: map[BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" or "pending" or "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `external_id: optional string`

    Platform's own identifier for this user. Not enforced unique.

  - `name: optional string`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```http
curl https://api.anthropic.com/v1/user_profiles \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: user-profiles-2026-03-24' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "external_id": "user_12345",
          "metadata": {}
        }'
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

**get** `/v1/user_profiles`

List User Profiles

### Query Parameters

- `limit: optional number`

  Query parameter for limit

- `order: optional "asc" or "desc"`

  Query parameter for order

  - `"asc"`

  - `"desc"`

- `page: optional string`

  Query parameter for page

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `data: array of BetaUserProfile`

  User profiles on this page.

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `relationship: "external" or "resold" or "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

  - `trust_grants: map[BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" or "pending" or "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `external_id: optional string`

    Platform's own identifier for this user. Not enforced unique.

  - `name: optional string`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

- `next_page: string`

  Cursor for the next page, or `null` when there are no more results.

### Example

```http
curl https://api.anthropic.com/v1/user_profiles \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: user-profiles-2026-03-24' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/user_profiles/{user_profile_id}`

Get User Profile

### Path Parameters

- `user_profile_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaUserProfile object { id, created_at, metadata, 6 more }`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `relationship: "external" or "resold" or "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

  - `trust_grants: map[BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" or "pending" or "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `external_id: optional string`

    Platform's own identifier for this user. Not enforced unique.

  - `name: optional string`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```http
curl https://api.anthropic.com/v1/user_profiles/$USER_PROFILE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: user-profiles-2026-03-24' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Path Parameters

- `user_profile_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `external_id: optional string`

  If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

- `metadata: optional map[string]`

  Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

- `name: optional string`

  If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

- `relationship: optional "external" or "resold" or "internal"`

  How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

  - `"external"`

  - `"resold"`

  - `"internal"`

### Returns

- `BetaUserProfile object { id, created_at, metadata, 6 more }`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `relationship: "external" or "resold" or "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

  - `trust_grants: map[BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" or "pending" or "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `external_id: optional string`

    Platform's own identifier for this user. Not enforced unique.

  - `name: optional string`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```http
curl https://api.anthropic.com/v1/user_profiles/$USER_PROFILE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: user-profiles-2026-03-24' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "external_id": "user_12345"
        }'
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

**post** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Path Parameters

- `user_profile_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaUserProfileEnrollmentURL object { expires_at, type, url }`

  - `expires_at: string`

    A timestamp in RFC 3339 format

  - `type: "enrollment_url"`

    Object type. Always `enrollment_url`.

    - `"enrollment_url"`

  - `url: string`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

```http
curl https://api.anthropic.com/v1/user_profiles/$USER_PROFILE_ID/enrollment_url \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: user-profiles-2026-03-24' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `BetaUserProfile object { id, created_at, metadata, 6 more }`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `relationship: "external" or "resold" or "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

  - `trust_grants: map[BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" or "pending" or "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `external_id: optional string`

    Platform's own identifier for this user. Not enforced unique.

  - `name: optional string`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Beta User Profile Enrollment URL

- `BetaUserProfileEnrollmentURL object { expires_at, type, url }`

  - `expires_at: string`

    A timestamp in RFC 3339 format

  - `type: "enrollment_url"`

    Object type. Always `enrollment_url`.

    - `"enrollment_url"`

  - `url: string`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Beta User Profile Trust Grant

- `BetaUserProfileTrustGrant object { status }`

  - `status: "active" or "pending" or "rejected"`

    Status of the trust grant.

    - `"active"`

    - `"pending"`

    - `"rejected"`

# Dreams

## Create a Dream

**post** `/v1/dreams`

Create a Dream

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `inputs: array of BetaDreamInput`

  - `BetaDreamMemoryStoreInput object { memory_store_id, type }`

    An input memory store the dream reads from. The dream never mutates this store.

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `BetaDreamSessionsInput object { session_ids, type }`

    Input session transcripts the dream reads.

    - `session_ids: array of string`

    - `type: "sessions"`

      - `"sessions"`

- `model: string or BetaDreamModelConfigParam`

  Model identifier and configuration applied to every pipeline stage.

  - `string`

  - `BetaDreamModelConfigParam object { id, speed }`

    Model identifier and configuration applied to every pipeline stage.

    - `id: string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

- `instructions: optional string`

### Returns

- `BetaDream object { id, archived_at, created_at, 10 more }`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `ended_at: string`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `BetaDreamMemoryStoreInput object { memory_store_id, type }`

      An input memory store the dream reads from. The dream never mutates this store.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `BetaDreamSessionsInput object { session_ids, type }`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

        - `"sessions"`

  - `instructions: string`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `session_id: string`

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

```http
curl https://api.anthropic.com/v1/dreams \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: dreaming-2026-04-21' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "inputs": [
            {
              "memory_store_id": "x",
              "type": "memory_store"
            }
          ],
          "model": "string"
        }'
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

**get** `/v1/dreams`

List Dreams

### Query Parameters

- `"created_at[gt]": optional string`

  Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

- `"created_at[lt]": optional string`

  Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

- `include_archived: optional boolean`

  Query parameter for include_archived

- `limit: optional number`

  Query parameter for limit

- `page: optional string`

  Query parameter for page

- `statuses: optional array of BetaDreamStatus`

  Filter by lifecycle status. Repeat the parameter to match any of multiple statuses. Empty applies no status filter.

  - `"pending"`

  - `"running"`

  - `"completed"`

  - `"failed"`

  - `"canceled"`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `data: array of BetaDream`

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `ended_at: string`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `BetaDreamMemoryStoreInput object { memory_store_id, type }`

      An input memory store the dream reads from. The dream never mutates this store.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `BetaDreamSessionsInput object { session_ids, type }`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

        - `"sessions"`

  - `instructions: string`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `session_id: string`

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

- `next_page: string`

### Example

```http
curl https://api.anthropic.com/v1/dreams \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: dreaming-2026-04-21' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/dreams/{dream_id}`

Get a Dream

### Path Parameters

- `dream_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaDream object { id, archived_at, created_at, 10 more }`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `ended_at: string`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `BetaDreamMemoryStoreInput object { memory_store_id, type }`

      An input memory store the dream reads from. The dream never mutates this store.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `BetaDreamSessionsInput object { session_ids, type }`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

        - `"sessions"`

  - `instructions: string`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `session_id: string`

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

```http
curl https://api.anthropic.com/v1/dreams/$DREAM_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: dreaming-2026-04-21' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/dreams/{dream_id}/cancel`

Cancel a Dream

### Path Parameters

- `dream_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaDream object { id, archived_at, created_at, 10 more }`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `ended_at: string`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `BetaDreamMemoryStoreInput object { memory_store_id, type }`

      An input memory store the dream reads from. The dream never mutates this store.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `BetaDreamSessionsInput object { session_ids, type }`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

        - `"sessions"`

  - `instructions: string`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `session_id: string`

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

```http
curl https://api.anthropic.com/v1/dreams/$DREAM_ID/cancel \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: dreaming-2026-04-21' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/dreams/{dream_id}/archive`

Archive a Dream

### Path Parameters

- `dream_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaDream object { id, archived_at, created_at, 10 more }`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `ended_at: string`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `BetaDreamMemoryStoreInput object { memory_store_id, type }`

      An input memory store the dream reads from. The dream never mutates this store.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `BetaDreamSessionsInput object { session_ids, type }`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

        - `"sessions"`

  - `instructions: string`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `session_id: string`

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

```http
curl https://api.anthropic.com/v1/dreams/$DREAM_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: dreaming-2026-04-21' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `BetaDream object { id, archived_at, created_at, 10 more }`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `ended_at: string`

    A timestamp in RFC 3339 format

  - `error: BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `BetaDreamMemoryStoreInput object { memory_store_id, type }`

      An input memory store the dream reads from. The dream never mutates this store.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `BetaDreamSessionsInput object { session_ids, type }`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

        - `"sessions"`

  - `instructions: string`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `session_id: string`

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

- `BetaDreamError object { message, type }`

  Failure detail for a Dream whose `status` is `failed`.

  - `message: string`

  - `type: string`

### Beta Dream Input

- `BetaDreamInput = BetaDreamMemoryStoreInput or BetaDreamSessionsInput`

  An input memory store the dream reads from. The dream never mutates this store.

  - `BetaDreamMemoryStoreInput object { memory_store_id, type }`

    An input memory store the dream reads from. The dream never mutates this store.

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `BetaDreamSessionsInput object { session_ids, type }`

    Input session transcripts the dream reads.

    - `session_ids: array of string`

    - `type: "sessions"`

      - `"sessions"`

### Beta Dream Memory Store Input

- `BetaDreamMemoryStoreInput object { memory_store_id, type }`

  An input memory store the dream reads from. The dream never mutates this store.

  - `memory_store_id: string`

  - `type: "memory_store"`

    - `"memory_store"`

### Beta Dream Memory Store Output

- `BetaDreamMemoryStoreOutput object { memory_store_id, type }`

  An output memory store the dream writes consolidated memories into.

  - `memory_store_id: string`

  - `type: "memory_store"`

    - `"memory_store"`

### Beta Dream Model Config

- `BetaDreamModelConfig object { id, speed }`

  Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

  - `id: string`

    Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

  - `speed: optional "standard" or "fast"`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Dream Model Config Param

- `BetaDreamModelConfigParam object { id, speed }`

  Model identifier and configuration applied to every pipeline stage.

  - `id: string`

    Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

  - `speed: optional "standard" or "fast"`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Dream Output

- `BetaDreamOutput object { memory_store_id, type }`

  An output memory store the dream writes consolidated memories into.

  - `memory_store_id: string`

  - `type: "memory_store"`

    - `"memory_store"`

### Beta Dream Sessions Input

- `BetaDreamSessionsInput object { session_ids, type }`

  Input session transcripts the dream reads.

  - `session_ids: array of string`

  - `type: "sessions"`

    - `"sessions"`

### Beta Dream Status

- `BetaDreamStatus = "pending" or "running" or "completed" or 2 more`

  Lifecycle status of a Dream.

  - `"pending"`

  - `"running"`

  - `"completed"`

  - `"failed"`

  - `"canceled"`

### Beta Dream Usage

- `BetaDreamUsage object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, output_tokens }`

  Cumulative token usage for the dream across every pipeline stage.

  - `cache_creation_input_tokens: number`

    Total tokens used to create prompt-cache entries (sum of all TTL tiers).

  - `cache_read_input_tokens: number`

    Total tokens read from prompt cache.

  - `input_tokens: number`

    Total uncached input tokens consumed across every pipeline stage.

  - `output_tokens: number`

    Total output tokens generated across every pipeline stage.

# Tunnels

## Create Tunnel

**post** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `display_name: optional string`

  Optional human-readable name for the tunnel (1-255 characters).

### Returns

- `BetaTunnel object { id, archived_at, created_at, 3 more }`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

    - `"tunnel"`

### Example

```http
curl https://api.anthropic.com/v1/tunnels \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: mcp-tunnels-2026-06-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
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

**get** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

### Path Parameters

- `tunnel_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaTunnel object { id, archived_at, created_at, 3 more }`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

    - `"tunnel"`

### Example

```http
curl https://api.anthropic.com/v1/tunnels/$TUNNEL_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: mcp-tunnels-2026-06-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

### Query Parameters

- `include_archived: optional boolean`

  Whether to include archived tunnels in the results. Defaults to false.

- `limit: optional number`

  Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

- `page: optional string`

  Opaque pagination cursor from a previous `list_tunnels` response.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `data: array of BetaTunnel`

  List of tunnels, ordered by created_at descending.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

    - `"tunnel"`

- `next_page: string`

  Pagination cursor for the next page, or null if no more results.

### Example

```http
curl https://api.anthropic.com/v1/tunnels \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: mcp-tunnels-2026-06-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

### Path Parameters

- `tunnel_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaTunnel object { id, archived_at, created_at, 3 more }`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

    - `"tunnel"`

### Example

```http
curl https://api.anthropic.com/v1/tunnels/$TUNNEL_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: mcp-tunnels-2026-06-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

### Path Parameters

- `tunnel_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaTunnelToken object { id, tunnel_token, type }`

  A tunnel's connector token.

  - `id: string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: string`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: "tunnel_token"`

    - `"tunnel_token"`

### Example

```http
curl https://api.anthropic.com/v1/tunnels/$TUNNEL_ID/reveal_token \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: mcp-tunnels-2026-06-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

### Path Parameters

- `tunnel_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `reason: optional string`

  Optional free-text reason for the rotation, recorded for audit.

### Returns

- `BetaTunnelToken object { id, tunnel_token, type }`

  A tunnel's connector token.

  - `id: string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: string`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: "tunnel_token"`

    - `"tunnel_token"`

### Example

```http
curl https://api.anthropic.com/v1/tunnels/$TUNNEL_ID/rotate_token \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: mcp-tunnels-2026-06-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
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

- `BetaTunnel object { id, archived_at, created_at, 3 more }`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

    - `"tunnel"`

### Beta Tunnel Token

- `BetaTunnelToken object { id, tunnel_token, type }`

  A tunnel's connector token.

  - `id: string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: string`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: "tunnel_token"`

    - `"tunnel_token"`

# Certificates

## Create Tunnel Certificate

**post** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

### Path Parameters

- `tunnel_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

### Body Parameters

- `ca_certificate_pem: string`

  PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

### Returns

- `BetaTunnelCertificate object { id, archived_at, created_at, 4 more }`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

    - `"tunnel_certificate"`

### Example

```http
curl https://api.anthropic.com/v1/tunnels/$TUNNEL_ID/certificates \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: mcp-tunnels-2026-06-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "ca_certificate_pem": "ca_certificate_pem"
        }'
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

**get** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

### Path Parameters

- `tunnel_id: string`

- `certificate_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaTunnelCertificate object { id, archived_at, created_at, 4 more }`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

    - `"tunnel_certificate"`

### Example

```http
curl https://api.anthropic.com/v1/tunnels/$TUNNEL_ID/certificates/$CERTIFICATE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: mcp-tunnels-2026-06-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

### Path Parameters

- `tunnel_id: string`

### Query Parameters

- `include_archived: optional boolean`

  Whether to include archived certificates in the results. Defaults to false.

- `limit: optional number`

  Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

- `page: optional string`

  Opaque pagination cursor from a previous `list_tunnel_certificates` response.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `data: array of BetaTunnelCertificate`

  List of certificates, ordered by created_at descending.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

    - `"tunnel_certificate"`

- `next_page: string`

  Pagination cursor for the next page, or null if no more results.

### Example

```http
curl https://api.anthropic.com/v1/tunnels/$TUNNEL_ID/certificates \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: mcp-tunnels-2026-06-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

### Path Parameters

- `tunnel_id: string`

- `certificate_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more`

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

- `BetaTunnelCertificate object { id, archived_at, created_at, 4 more }`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

    - `"tunnel_certificate"`

### Example

```http
curl https://api.anthropic.com/v1/tunnels/$TUNNEL_ID/certificates/$CERTIFICATE_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: mcp-tunnels-2026-06-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `BetaTunnelCertificate object { id, archived_at, created_at, 4 more }`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string`

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

- `BetaWebhookAgentArchivedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.archived"`

    - `"agent.archived"`

  - `workspace_id: string`

### Beta Webhook Agent Created Event Data

- `BetaWebhookAgentCreatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.created"`

    - `"agent.created"`

  - `workspace_id: string`

### Beta Webhook Agent Deleted Event Data

- `BetaWebhookAgentDeletedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.deleted"`

    - `"agent.deleted"`

  - `workspace_id: string`

### Beta Webhook Agent Updated Event Data

- `BetaWebhookAgentUpdatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.updated"`

    - `"agent.updated"`

  - `workspace_id: string`

### Beta Webhook Deployment Archived Event Data

- `BetaWebhookDeploymentArchivedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.archived"`

    - `"deployment.archived"`

  - `workspace_id: string`

### Beta Webhook Deployment Created Event Data

- `BetaWebhookDeploymentCreatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.created"`

    - `"deployment.created"`

  - `workspace_id: string`

### Beta Webhook Deployment Deleted Event Data

- `BetaWebhookDeploymentDeletedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.deleted"`

    - `"deployment.deleted"`

  - `workspace_id: string`

### Beta Webhook Deployment Paused Event Data

- `BetaWebhookDeploymentPausedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.paused"`

    - `"deployment.paused"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Failed Event Data

- `BetaWebhookDeploymentRunFailedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.failed"`

    - `"deployment_run.failed"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Started Event Data

- `BetaWebhookDeploymentRunStartedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.started"`

    - `"deployment_run.started"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Succeeded Event Data

- `BetaWebhookDeploymentRunSucceededEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.succeeded"`

    - `"deployment_run.succeeded"`

  - `workspace_id: string`

### Beta Webhook Deployment Unpaused Event Data

- `BetaWebhookDeploymentUnpausedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.unpaused"`

    - `"deployment.unpaused"`

  - `workspace_id: string`

### Beta Webhook Deployment Updated Event Data

- `BetaWebhookDeploymentUpdatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.updated"`

    - `"deployment.updated"`

  - `workspace_id: string`

### Beta Webhook Environment Archived Event Data

- `BetaWebhookEnvironmentArchivedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.archived"`

    - `"environment.archived"`

  - `workspace_id: string`

### Beta Webhook Environment Created Event Data

- `BetaWebhookEnvironmentCreatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.created"`

    - `"environment.created"`

  - `workspace_id: string`

### Beta Webhook Environment Deleted Event Data

- `BetaWebhookEnvironmentDeletedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.deleted"`

    - `"environment.deleted"`

  - `workspace_id: string`

### Beta Webhook Environment Updated Event Data

- `BetaWebhookEnvironmentUpdatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.updated"`

    - `"environment.updated"`

  - `workspace_id: string`

### Beta Webhook Event

- `BetaWebhookEvent object { id, created_at, data, type }`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `BetaWebhookSessionCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

        - `"session.created"`

      - `workspace_id: string`

    - `BetaWebhookSessionPendingEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

        - `"session.pending"`

      - `workspace_id: string`

    - `BetaWebhookSessionRunningEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

        - `"session.running"`

      - `workspace_id: string`

    - `BetaWebhookSessionIdledEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

        - `"session.idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionRequiresActionEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

        - `"session.requires_action"`

      - `workspace_id: string`

    - `BetaWebhookSessionArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

        - `"session.archived"`

      - `workspace_id: string`

    - `BetaWebhookSessionDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

        - `"session.deleted"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRescheduledEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_rescheduled"`

        - `"session.status_rescheduled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRunStartedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

        - `"session.status_run_started"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusIdledEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

        - `"session.status_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusTerminatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

        - `"session.status_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadCreatedEventData object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_created"`

        - `"session.thread_created"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadIdledEventData object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_idled"`

        - `"session.thread_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadTerminatedEventData object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_terminated"`

        - `"session.thread_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `BetaWebhookVaultCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

        - `"vault.created"`

      - `workspace_id: string`

    - `BetaWebhookVaultArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

        - `"vault.archived"`

      - `workspace_id: string`

    - `BetaWebhookVaultDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

        - `"vault.deleted"`

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialCreatedEventData object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

        - `"vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialArchivedEventData object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

        - `"vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialDeletedEventData object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

        - `"vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.refresh_failed"`

        - `"vault_credential.refresh_failed"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookSessionUpdatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.updated"`

        - `"session.updated"`

      - `workspace_id: string`

    - `BetaWebhookAgentCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.created"`

        - `"agent.created"`

      - `workspace_id: string`

    - `BetaWebhookAgentArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.archived"`

        - `"agent.archived"`

      - `workspace_id: string`

    - `BetaWebhookAgentDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.deleted"`

        - `"agent.deleted"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentPausedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.paused"`

        - `"deployment.paused"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunFailedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.failed"`

        - `"deployment_run.failed"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.created"`

        - `"deployment.created"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUpdatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.updated"`

        - `"deployment.updated"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUnpausedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.unpaused"`

        - `"deployment.unpaused"`

      - `workspace_id: string`

    - `BetaWebhookAgentUpdatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.updated"`

        - `"agent.updated"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.archived"`

        - `"deployment.archived"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunStartedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.started"`

        - `"deployment_run.started"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.deleted"`

        - `"deployment.deleted"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunSucceededEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.succeeded"`

        - `"deployment_run.succeeded"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.created"`

        - `"environment.created"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentUpdatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.updated"`

        - `"environment.updated"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.archived"`

        - `"environment.archived"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.deleted"`

        - `"environment.deleted"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.created"`

        - `"memory_store.created"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.archived"`

        - `"memory_store.archived"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.deleted"`

        - `"memory_store.deleted"`

      - `workspace_id: string`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

    - `"event"`

### Beta Webhook Event Data

- `BetaWebhookEventData = BetaWebhookSessionCreatedEventData or BetaWebhookSessionPendingEventData or BetaWebhookSessionRunningEventData or 40 more`

  - `BetaWebhookSessionCreatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.created"`

      - `"session.created"`

    - `workspace_id: string`

  - `BetaWebhookSessionPendingEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.pending"`

      - `"session.pending"`

    - `workspace_id: string`

  - `BetaWebhookSessionRunningEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.running"`

      - `"session.running"`

    - `workspace_id: string`

  - `BetaWebhookSessionIdledEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.idled"`

      - `"session.idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionRequiresActionEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.requires_action"`

      - `"session.requires_action"`

    - `workspace_id: string`

  - `BetaWebhookSessionArchivedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.archived"`

      - `"session.archived"`

    - `workspace_id: string`

  - `BetaWebhookSessionDeletedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.deleted"`

      - `"session.deleted"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusRescheduledEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_rescheduled"`

      - `"session.status_rescheduled"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusRunStartedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_run_started"`

      - `"session.status_run_started"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusIdledEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_idled"`

      - `"session.status_idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusTerminatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_terminated"`

      - `"session.status_terminated"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadCreatedEventData object { id, organization_id, session_thread_id, 2 more }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_created"`

      - `"session.thread_created"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadIdledEventData object { id, organization_id, session_thread_id, 2 more }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_idled"`

      - `"session.thread_idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadTerminatedEventData object { id, organization_id, session_thread_id, 2 more }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_terminated"`

      - `"session.thread_terminated"`

    - `workspace_id: string`

  - `BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.outcome_evaluation_ended"`

      - `"session.outcome_evaluation_ended"`

    - `workspace_id: string`

  - `BetaWebhookVaultCreatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.created"`

      - `"vault.created"`

    - `workspace_id: string`

  - `BetaWebhookVaultArchivedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.archived"`

      - `"vault.archived"`

    - `workspace_id: string`

  - `BetaWebhookVaultDeletedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.deleted"`

      - `"vault.deleted"`

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialCreatedEventData object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.created"`

      - `"vault_credential.created"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialArchivedEventData object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.archived"`

      - `"vault_credential.archived"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialDeletedEventData object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.deleted"`

      - `"vault_credential.deleted"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.refresh_failed"`

      - `"vault_credential.refresh_failed"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookSessionUpdatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.updated"`

      - `"session.updated"`

    - `workspace_id: string`

  - `BetaWebhookAgentCreatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.created"`

      - `"agent.created"`

    - `workspace_id: string`

  - `BetaWebhookAgentArchivedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.archived"`

      - `"agent.archived"`

    - `workspace_id: string`

  - `BetaWebhookAgentDeletedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.deleted"`

      - `"agent.deleted"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentPausedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.paused"`

      - `"deployment.paused"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunFailedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.failed"`

      - `"deployment_run.failed"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentCreatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.created"`

      - `"deployment.created"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentUpdatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.updated"`

      - `"deployment.updated"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentUnpausedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.unpaused"`

      - `"deployment.unpaused"`

    - `workspace_id: string`

  - `BetaWebhookAgentUpdatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.updated"`

      - `"agent.updated"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentArchivedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.archived"`

      - `"deployment.archived"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunStartedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.started"`

      - `"deployment_run.started"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentDeletedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.deleted"`

      - `"deployment.deleted"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunSucceededEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.succeeded"`

      - `"deployment_run.succeeded"`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentCreatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.created"`

      - `"environment.created"`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentUpdatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.updated"`

      - `"environment.updated"`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentArchivedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.archived"`

      - `"environment.archived"`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentDeletedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.deleted"`

      - `"environment.deleted"`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreCreatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.created"`

      - `"memory_store.created"`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreArchivedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.archived"`

      - `"memory_store.archived"`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreDeletedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.deleted"`

      - `"memory_store.deleted"`

    - `workspace_id: string`

### Beta Webhook Memory Store Archived Event Data

- `BetaWebhookMemoryStoreArchivedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.archived"`

    - `"memory_store.archived"`

  - `workspace_id: string`

### Beta Webhook Memory Store Created Event Data

- `BetaWebhookMemoryStoreCreatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.created"`

    - `"memory_store.created"`

  - `workspace_id: string`

### Beta Webhook Memory Store Deleted Event Data

- `BetaWebhookMemoryStoreDeletedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.deleted"`

    - `"memory_store.deleted"`

  - `workspace_id: string`

### Beta Webhook Session Archived Event Data

- `BetaWebhookSessionArchivedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.archived"`

    - `"session.archived"`

  - `workspace_id: string`

### Beta Webhook Session Created Event Data

- `BetaWebhookSessionCreatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.created"`

    - `"session.created"`

  - `workspace_id: string`

### Beta Webhook Session Deleted Event Data

- `BetaWebhookSessionDeletedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.deleted"`

    - `"session.deleted"`

  - `workspace_id: string`

### Beta Webhook Session Idled Event Data

- `BetaWebhookSessionIdledEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.idled"`

    - `"session.idled"`

  - `workspace_id: string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.outcome_evaluation_ended"`

    - `"session.outcome_evaluation_ended"`

  - `workspace_id: string`

### Beta Webhook Session Pending Event Data

- `BetaWebhookSessionPendingEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.pending"`

    - `"session.pending"`

  - `workspace_id: string`

### Beta Webhook Session Requires Action Event Data

- `BetaWebhookSessionRequiresActionEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.requires_action"`

    - `"session.requires_action"`

  - `workspace_id: string`

### Beta Webhook Session Running Event Data

- `BetaWebhookSessionRunningEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.running"`

    - `"session.running"`

  - `workspace_id: string`

### Beta Webhook Session Status Idled Event Data

- `BetaWebhookSessionStatusIdledEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_idled"`

    - `"session.status_idled"`

  - `workspace_id: string`

### Beta Webhook Session Status Rescheduled Event Data

- `BetaWebhookSessionStatusRescheduledEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_rescheduled"`

    - `"session.status_rescheduled"`

  - `workspace_id: string`

### Beta Webhook Session Status Run Started Event Data

- `BetaWebhookSessionStatusRunStartedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_run_started"`

    - `"session.status_run_started"`

  - `workspace_id: string`

### Beta Webhook Session Status Terminated Event Data

- `BetaWebhookSessionStatusTerminatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_terminated"`

    - `"session.status_terminated"`

  - `workspace_id: string`

### Beta Webhook Session Thread Created Event Data

- `BetaWebhookSessionThreadCreatedEventData object { id, organization_id, session_thread_id, 2 more }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_created"`

    - `"session.thread_created"`

  - `workspace_id: string`

### Beta Webhook Session Thread Idled Event Data

- `BetaWebhookSessionThreadIdledEventData object { id, organization_id, session_thread_id, 2 more }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_idled"`

    - `"session.thread_idled"`

  - `workspace_id: string`

### Beta Webhook Session Thread Terminated Event Data

- `BetaWebhookSessionThreadTerminatedEventData object { id, organization_id, session_thread_id, 2 more }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_terminated"`

    - `"session.thread_terminated"`

  - `workspace_id: string`

### Beta Webhook Session Updated Event Data

- `BetaWebhookSessionUpdatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.updated"`

    - `"session.updated"`

  - `workspace_id: string`

### Beta Webhook Vault Archived Event Data

- `BetaWebhookVaultArchivedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.archived"`

    - `"vault.archived"`

  - `workspace_id: string`

### Beta Webhook Vault Created Event Data

- `BetaWebhookVaultCreatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.created"`

    - `"vault.created"`

  - `workspace_id: string`

### Beta Webhook Vault Credential Archived Event Data

- `BetaWebhookVaultCredentialArchivedEventData object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.archived"`

    - `"vault_credential.archived"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Created Event Data

- `BetaWebhookVaultCredentialCreatedEventData object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.created"`

    - `"vault_credential.created"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Deleted Event Data

- `BetaWebhookVaultCredentialDeletedEventData object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.deleted"`

    - `"vault_credential.deleted"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.refresh_failed"`

    - `"vault_credential.refresh_failed"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Deleted Event Data

- `BetaWebhookVaultDeletedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.deleted"`

    - `"vault.deleted"`

  - `workspace_id: string`

### Unwrap Webhook Event

- `UnwrapWebhookEvent object { id, created_at, data, type }`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `BetaWebhookSessionCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

        - `"session.created"`

      - `workspace_id: string`

    - `BetaWebhookSessionPendingEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

        - `"session.pending"`

      - `workspace_id: string`

    - `BetaWebhookSessionRunningEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

        - `"session.running"`

      - `workspace_id: string`

    - `BetaWebhookSessionIdledEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

        - `"session.idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionRequiresActionEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

        - `"session.requires_action"`

      - `workspace_id: string`

    - `BetaWebhookSessionArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

        - `"session.archived"`

      - `workspace_id: string`

    - `BetaWebhookSessionDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

        - `"session.deleted"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRescheduledEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_rescheduled"`

        - `"session.status_rescheduled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRunStartedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

        - `"session.status_run_started"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusIdledEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

        - `"session.status_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusTerminatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

        - `"session.status_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadCreatedEventData object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_created"`

        - `"session.thread_created"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadIdledEventData object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_idled"`

        - `"session.thread_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadTerminatedEventData object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_terminated"`

        - `"session.thread_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `BetaWebhookVaultCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

        - `"vault.created"`

      - `workspace_id: string`

    - `BetaWebhookVaultArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

        - `"vault.archived"`

      - `workspace_id: string`

    - `BetaWebhookVaultDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

        - `"vault.deleted"`

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialCreatedEventData object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

        - `"vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialArchivedEventData object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

        - `"vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialDeletedEventData object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

        - `"vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.refresh_failed"`

        - `"vault_credential.refresh_failed"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookSessionUpdatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.updated"`

        - `"session.updated"`

      - `workspace_id: string`

    - `BetaWebhookAgentCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.created"`

        - `"agent.created"`

      - `workspace_id: string`

    - `BetaWebhookAgentArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.archived"`

        - `"agent.archived"`

      - `workspace_id: string`

    - `BetaWebhookAgentDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.deleted"`

        - `"agent.deleted"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentPausedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.paused"`

        - `"deployment.paused"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunFailedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.failed"`

        - `"deployment_run.failed"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.created"`

        - `"deployment.created"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUpdatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.updated"`

        - `"deployment.updated"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUnpausedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.unpaused"`

        - `"deployment.unpaused"`

      - `workspace_id: string`

    - `BetaWebhookAgentUpdatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.updated"`

        - `"agent.updated"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.archived"`

        - `"deployment.archived"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunStartedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.started"`

        - `"deployment_run.started"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.deleted"`

        - `"deployment.deleted"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunSucceededEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.succeeded"`

        - `"deployment_run.succeeded"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.created"`

        - `"environment.created"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentUpdatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.updated"`

        - `"environment.updated"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.archived"`

        - `"environment.archived"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.deleted"`

        - `"environment.deleted"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.created"`

        - `"memory_store.created"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.archived"`

        - `"memory_store.archived"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.deleted"`

        - `"memory_store.deleted"`

      - `workspace_id: string`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

    - `"event"`
