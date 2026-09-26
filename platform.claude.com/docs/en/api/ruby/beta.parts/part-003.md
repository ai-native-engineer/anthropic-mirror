<!-- source: https://platform.claude.com/docs/en/api/ruby/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/ruby/beta -->

<!-- chunk-start -->

  minimum: 3600, maximum: 7776000

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a federation issuer by its ID (`fdis_...`).

#### Parameters

- `federation_issuer_id: String`

  ID of the federation issuer.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a federation rule by its ID (`fdrl_...`).

#### Parameters

- `federation_rule_id: String`

  ID of the federation rule.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

- `federation_rule_id: String`

  ID of the federation rule to archive.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

- `federation_rule_id: String`

  ID of the federation rule.

- `workspace_id: String`

  Tagged ID of the workspace to enable this rule for.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a service account by its ID (`svac_...`).

#### Parameters

- `service_account_id: String`

  ID of the service account.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

- `service_account_id: String`

  ID of the service account.

- `workspace_id: String`

  ID of the workspace.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

      - `AllowedInferenceGeos = :unrestricted`

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

    - `AllowedInferenceGeos = :unrestricted`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

      - `AllowedInferenceGeos = :unrestricted`

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

      - `AllowedInferenceGeos = :unrestricted`

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

    - `AllowedInferenceGeos = :unrestricted`

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

      - `AllowedInferenceGeos = :unrestricted`

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

      - `AllowedInferenceGeos = :unrestricted`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 45 more`

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
or an API-surface category such as the Files API or Message Batches)
and contains the set of limiter values that apply to it.

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
