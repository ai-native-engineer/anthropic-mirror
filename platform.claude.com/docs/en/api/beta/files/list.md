<!-- source: https://platform.claude.com/docs/en/api/beta/files/list -->

# List Files
GET/v1/files
List Files
##### Query ParametersExpand Collapse 
after_id: optional string
ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.
[](https://platform.claude.com/docs/en/api/beta/files/list#list.after_id)
before_id: optional string
ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.
[](https://platform.claude.com/docs/en/api/beta/files/list#list.before_id)
limit: optional number
Number of items to return per page.
Defaults to `20`. Ranges from `1` to `1000`.
maximum1000
minimum1
[](https://platform.claude.com/docs/en/api/beta/files/list#list.limit)
scope_id: optional string
Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).
[](https://platform.claude.com/docs/en/api/beta/files/list#list.scope_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/files/list#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/files/list#list.betas)
data: array of [FileMetadata](https://platform.claude.com/docs/en/api/beta#file_metadata) { id, created_at, filename, 5 more } 
List of file metadata objects.
Unique object identifier.
The format and length of IDs may change over time.
[](https://platform.claude.com/docs/en/api/beta/files/list#file_metadata.id)
created_at: string
RFC 3339 datetime string representing when the file was created.
[](https://platform.claude.com/docs/en/api/beta/files/list#file_metadata.created_at)
filename: string
Original filename of the uploaded file.
[](https://platform.claude.com/docs/en/api/beta/files/list#file_metadata.filename)
mime_type: string
MIME type of the file.
[](https://platform.claude.com/docs/en/api/beta/files/list#file_metadata.mime_type)
size_bytes: number
Size of the file in bytes.
[](https://platform.claude.com/docs/en/api/beta/files/list#file_metadata.size_bytes)
type: "file"
Object type.
For files, this is always `"file"`.
[](https://platform.claude.com/docs/en/api/beta/files/list#file_metadata.type)
downloadable: optional boolean
Whether the file can be downloaded.
[](https://platform.claude.com/docs/en/api/beta/files/list#file_metadata.downloadable)
scope: optional [BetaFileScope](https://platform.claude.com/docs/en/api/beta#beta_file_scope) { id, type } 
The scope of this file, indicating the context in which it was created (e.g., a session).
The ID of the scoping resource (e.g., the session ID).
[](https://platform.claude.com/docs/en/api/beta/files/list#file_metadata.scope%20%2B%20\(resource\)%20beta.files.id)
type: "session"
The type of scope (e.g., `"session"`).
[](https://platform.claude.com/docs/en/api/beta/files/list#file_metadata.scope%20%2B%20\(resource\)%20beta.files.type)
[](https://platform.claude.com/docs/en/api/beta/files/list#file_metadata.scope)
[](https://platform.claude.com/docs/en/api/beta/files/list#list)
first_id: optional string
ID of the first file in this page of results.
[](https://platform.claude.com/docs/en/api/beta/files/list#list)
has_more: optional boolean
Whether there are more results available.
[](https://platform.claude.com/docs/en/api/beta/files/list#list)
last_id: optional string
ID of the last file in this page of results.
[](https://platform.claude.com/docs/en/api/beta/files/list#list)
List Files
cURL

curl https://api.anthropic.com/v1/files \
    -H 'anthropic-beta: files-api-2025-04-14' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "data": [
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
  ],
  "first_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "has_more": true,
  "last_id": "file_013Zva2CMHLNnXjNJJKqJ2EF"

  "data": [
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
  ],
  "first_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "has_more": true,
  "last_id": "file_013Zva2CMHLNnXjNJJKqJ2EF"
