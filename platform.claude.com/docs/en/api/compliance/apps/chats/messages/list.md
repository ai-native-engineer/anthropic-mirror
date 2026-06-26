<!-- source: https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list -->

# Get chat messages
GET/v1/compliance/apps/chats/{claude_chat_id}/messages
Retrieves message history and file metadata for a specific chat.
##### Path ParametersExpand Collapse 
claude_chat_id: string
The chat ID (tagged ID, e.g., claude_chat_abc123)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.claude_chat_id)
##### Query ParametersExpand Collapse 
after_id: optional string
Pagination cursor for retrieving the next page of results. To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.after_id)
before_id: optional string
Pagination cursor for retrieving the previous page of results. To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.before_id)
created_at: optional object { gt, gte, lt, lte } 
gt: optional string
Filter messages created after this time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.created_at.gt)
gte: optional string
Filter messages created at or after this time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.created_at.gte)
lt: optional string
Filter messages created before this time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.created_at.lt)
lte: optional string
Filter messages created at or before this time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.created_at.lte)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.created_at)
limit: optional number
Maximum results (max: 1000). When omitted, the full result set is returned in one response.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.limit)
order: optional "asc" or "desc"
Sort direction for messages within the response. `asc` (the default) returns oldest-first; `desc` returns newest-first.
"asc"
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.order%5B0%5D)
"desc"
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.order%5B1%5D)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.order)
tool_result_max_chars: optional number
Maximum characters returned per tool-result text item. Items longer than this are shortened and the block's `truncated` field is set. Pass -1 to disable the limit.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.tool_result_max_chars)
tool_use_input_max_chars: optional number
Maximum characters of JSON-encoded tool input returned per tool_use block. Inputs longer than this are shortened and the block's `truncated` field is set. Pass -1 to disable the limit.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.tool_use_input_max_chars)
updated_at: optional object { gt, gte, lt, lte } 
gt: optional string
Filter messages updated after this time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.updated_at.gt)
gte: optional string
Filter messages updated at or after this time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.updated_at.gte)
lt: optional string
Filter messages updated before this time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.updated_at.lt)
lte: optional string
Filter messages updated at or before this time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.updated_at.lte)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.updated_at)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list.x-api-key)
Chat ID
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list)
chat_messages: array of object { id, artifacts, content, 4 more } 
Array of chat messages in order of created_at
Unique identifier for the message e.g. 'claude_chat_msg_abcd1234'
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.id)
artifacts: array of object { id, artifact_type, title, version_id } 
Versioned documents generated or updated by the assistant in this message. Download via `GET /v1/compliance/apps/artifacts/{artifact_version_id}/content`.
Artifact ID e.g. 'claude_artifact_abc123'
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.artifacts.items.id)
artifact_type: string
MIME-like artifact type e.g. 'application/vnd.ant.code'
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.artifacts.items.artifact_type)
title: string
Artifact title
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.artifacts.items.title)
version_id: string
Artifact version ID e.g. 'claude_artifact_version_abc123'
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.artifacts.items.version_id)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.artifacts)
content: array of object { text, type }  or object { id, input, integration_name, 4 more }  or object { content, integration_name, is_error, 5 more } 
Content blocks within the message
Text object { text, type } 
Text content block.
text: string
Text content from human or assistant
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B0%5D.text)
type: "text"
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B0%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B0%5D)
ToolUse object { id, input, integration_name, 4 more } 
Tool invocation requested by the assistant.
Tool-use ID, e.g. 'toolu_01AbC...'
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B1%5D.id)
input: string
Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B1%5D.input)
integration_name: string
Name of the integration that provides this tool, when applicable
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B1%5D.integration_name)
mcp_server_url: string
Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B1%5D.mcp_server_url)
name: string
Name of the tool invoked
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B1%5D.name)
truncated: boolean
True when `input` was shortened. Pass tool_use_input_max_chars=-1 to disable the limit
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B1%5D.truncated)
type: "tool_use"
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B1%5D)
ToolResult object { content, integration_name, is_error, 5 more } 
Result returned by a tool invocation.
content: array of object { text, type } 
Text content returned by the tool. Generated files are surfaced via the message's `generated_files` list; other non-text item types (including images and links) are omitted.
text: string
Text returned by the tool
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B2%5D.content.items.text)
type: "text"
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B2%5D.content.items.type)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B2%5D.content)
integration_name: string
Name of the integration that provides this tool, when applicable
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B2%5D.integration_name)
is_error: boolean
True when the tool reported an error
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B2%5D.is_error)
mcp_server_url: string
Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B2%5D.mcp_server_url)
name: string
Name of the tool that produced this result
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B2%5D.name)
tool_use_id: string
ID of the tool_use block this result responds to
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B2%5D.tool_use_id)
truncated: boolean
True when one or more text items in `content` were shortened. Pass tool_result_max_chars=-1 to retrieve full content.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B2%5D.truncated)
type: "tool_result"
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B2%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content.items%5B2%5D)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.content)
created_at: string
Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.created_at)
files: array of object { id, created_at, filename, 3 more } 
Binary file attachments uploaded by the user. Download via `GET /v1/compliance/apps/chats/files/{claude_file_id}/content`.
File ID
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.files.items.id)
created_at: string
File creation timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.files.items.created_at)
filename: string
Display name of the file
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.files.items.filename)
md5: string
Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.files.items.md5)
mime_type: string
MIME type of the file's preferred downloadable variant (e.g. 'application/pdf')
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.files.items.mime_type)
size_bytes: number
Size in bytes of the file's preferred downloadable variant, if known. Null for older files uploaded before size was recorded.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.files.items.size_bytes)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.files)
generated_files: array of object { id, filename, md5, 2 more } 
Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message. Download via `GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`.
Opaque generated-file id, e.g. 'claude_gen_file_abc123'. Treat as an opaque string; the encoding may change without notice.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.generated_files.items.id)
filename: string
Display name of the generated file
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.generated_files.items.filename)
md5: string
Lowercase hex MD5 of the generated file, when available. Null when no stored hash is available.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.generated_files.items.md5)
mime_type: string
MIME type reported by the tool that produced the file
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.generated_files.items.mime_type)
size_bytes: number
Size in bytes of the generated file, when available. Null when the file has expired or size is not recorded.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.generated_files.items.size_bytes)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.generated_files)
role: "assistant" or "user"
Message sender (user or assistant)
"assistant"
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.role%5B0%5D)
"user"
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.role%5B1%5D)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#message_list_response.role)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list)
created_at: string
Creation timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list)
deleted_at: string
Deletion timestamp if deleted
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list)
first_id: string
Opaque pagination cursor for the first message in the current result set. Pass as `before_id` on the next request to page backwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list)
has_more: boolean
Whether more chat messages exist beyond the current result set. Use `last_id` as `after_id` in a follow-up request to page forward.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list)
href: string
URL to view this chat in claude.ai
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list)
last_id: string
Opaque pagination cursor for the last message in the current result set. Pass as `after_id` on the next request to page forwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list)
model: string
Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list)
name: string
Chat name
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list)
Deprecatedorganization_id: string
Organization ID this chat belongs to
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list)
organization_uuid: string
Organization UUID this chat belongs to
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list)
project_id: string
Project ID this chat belongs to
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list)
updated_at: string
Last update timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list)
user: object { id, email_address } 
User information
User identifier
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list)
email_address: string
User's email address
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list#list)
Get chat messages

curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID/messages \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "id": "claude_chat_abc123",
  "name": "Product Requirements Discussion",
  "created_at": "2025-06-07T08:09:10Z",
  "updated_at": "2025-06-07T08:09:11Z",
  "organization_id": "org_abc123",
  "organization_uuid": "abcdef0123-4567-89ab-cdef-0123456789ab",
  "project_id": "claude_proj_xyz789",
  "model": "claude-opus-4-7",
  "user": {
    "id": "user_xyz456",
    "email_address": "user@example.com"
  "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789",
  "chat_messages": [
      "id": "claude_chat_msg_abc123",
      "role": "user",
      "created_at": "2025-06-07T08:09:10Z",
      "content": [
          "type": "text",
          "text": "Can you help me draft requirements for our new dashboard feature?"
      ],
      "files": [
          "id": "claude_file_xyz789",
          "filename": "dashboard_mockup_v1.pdf",
          "mime_type": "application/pdf",
          "size_bytes": 12345,
          "md5": "5d41402abc4b2a76b9719d911017c592",
          "created_at": "2025-06-07T08:09:10Z"
      ]
      "id": "claude_chat_msg_def456",
      "role": "assistant",
      "created_at": "2025-06-07T08:09:11Z",
      "content": [
          "type": "text",
          "text": "I'd be happy to help you draft requirements for your dashboard feature..."
      ],
      "artifacts": [
          "id": "claude_artifact_abc123",
          "version_id": "claude_artifact_version_xyz789",
          "title": "Dashboard Requirements Draft",
          "artifact_type": "text/markdown"
      ]
  ],
  "has_more": false,
  "first_id": "eyJtc2dfdXVpZCI6ICIwZjcwYjA2Ni0uLi4ifQ==",
  "last_id": "eyJtc2dfdXVpZCI6ICJhNGUwYjE3Mi0uLi4ifQ=="

  "id": "claude_chat_abc123",
  "name": "Product Requirements Discussion",
  "created_at": "2025-06-07T08:09:10Z",
  "updated_at": "2025-06-07T08:09:11Z",
  "organization_id": "org_abc123",
  "organization_uuid": "abcdef0123-4567-89ab-cdef-0123456789ab",
  "project_id": "claude_proj_xyz789",
  "model": "claude-opus-4-7",
  "user": {
    "id": "user_xyz456",
    "email_address": "user@example.com"
  "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789",
  "chat_messages": [
      "id": "claude_chat_msg_abc123",
      "role": "user",
      "created_at": "2025-06-07T08:09:10Z",
      "content": [
          "type": "text",
          "text": "Can you help me draft requirements for our new dashboard feature?"
      ],
      "files": [
          "id": "claude_file_xyz789",
          "filename": "dashboard_mockup_v1.pdf",
          "mime_type": "application/pdf",
          "size_bytes": 12345,
          "md5": "5d41402abc4b2a76b9719d911017c592",
          "created_at": "2025-06-07T08:09:10Z"
      ]
      "id": "claude_chat_msg_def456",
      "role": "assistant",
      "created_at": "2025-06-07T08:09:11Z",
      "content": [
          "type": "text",
          "text": "I'd be happy to help you draft requirements for your dashboard feature..."
      ],
      "artifacts": [
          "id": "claude_artifact_abc123",
          "version_id": "claude_artifact_version_xyz789",
          "title": "Dashboard Requirements Draft",
          "artifact_type": "text/markdown"
      ]
  ],
  "has_more": false,
  "first_id": "eyJtc2dfdXVpZCI6ICIwZjcwYjA2Ni0uLi4ifQ==",
  "last_id": "eyJtc2dfdXVpZCI6ICJhNGUwYjE3Mi0uLi4ifQ=="
