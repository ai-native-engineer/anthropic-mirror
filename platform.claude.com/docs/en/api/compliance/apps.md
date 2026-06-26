<!-- source: https://platform.claude.com/docs/en/api/compliance/apps -->

# Apps
####  AppsChats
##### [List chats](https://platform.claude.com/docs/en/api/compliance/apps/chats/list)
GET/v1/compliance/apps/chats
##### [Delete chat](https://platform.claude.com/docs/en/api/compliance/apps/chats/delete)
DELETE/v1/compliance/apps/chats/{claude_chat_id}
##### ModelsExpand Collapse 
ChatListResponse object { id, created_at, deleted_at, 8 more } 
Chat metadata for listing chats (without messages).
Chat ID
[](https://platform.claude.com/docs/en/api/compliance/apps#chat_list_response.id)
created_at: string
Creation timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps#chat_list_response.created_at)
deleted_at: string
Deletion timestamp if deleted
[](https://platform.claude.com/docs/en/api/compliance/apps#chat_list_response.deleted_at)
href: string
URL to view this chat in claude.ai
[](https://platform.claude.com/docs/en/api/compliance/apps#chat_list_response.href)
model: string
Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.
[](https://platform.claude.com/docs/en/api/compliance/apps#chat_list_response.model)
name: string
Chat name/title
[](https://platform.claude.com/docs/en/api/compliance/apps#chat_list_response.name)
Deprecatedorganization_id: string
Organization ID this chat belongs to
[](https://platform.claude.com/docs/en/api/compliance/apps#chat_list_response.organization_id)
organization_uuid: string
Organization UUID this chat belongs to
[](https://platform.claude.com/docs/en/api/compliance/apps#chat_list_response.organization_uuid)
project_id: string
Project ID this chat belongs to
[](https://platform.claude.com/docs/en/api/compliance/apps#chat_list_response.project_id)
updated_at: string
Last update timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps#chat_list_response.updated_at)
user: object { id, email_address } 
User information for the chat creator
User identifier
[](https://platform.claude.com/docs/en/api/compliance/apps#chat_list_response.user.id)
email_address: string
User's email address
[](https://platform.claude.com/docs/en/api/compliance/apps#chat_list_response.user.email_address)
[](https://platform.claude.com/docs/en/api/compliance/apps#chat_list_response.user)
[](https://platform.claude.com/docs/en/api/compliance/apps#chat_list_response)
ChatDeleteResponse object { id, type } 
Response for deleting a Claude chat.
The ID of the Claude chat that was deleted
[](https://platform.claude.com/docs/en/api/compliance/apps#chat_delete_response.id)
type: optional "claude_chat_deleted"
Constant string confirming deletion
[](https://platform.claude.com/docs/en/api/compliance/apps#chat_delete_response.type)
[](https://platform.claude.com/docs/en/api/compliance/apps#chat_delete_response)
####  AppsChatsMessages
##### [Get chat messages](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list)
GET/v1/compliance/apps/chats/{claude_chat_id}/messages
##### ModelsExpand Collapse 
MessageListResponse object { id, artifacts, content, 4 more } 
A single message in a chat conversation.
Unique identifier for the message e.g. 'claude_chat_msg_abcd1234'
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.id)
artifacts: array of object { id, artifact_type, title, version_id } 
Versioned documents generated or updated by the assistant in this message. Download via `GET /v1/compliance/apps/artifacts/{artifact_version_id}/content`.
Artifact ID e.g. 'claude_artifact_abc123'
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.artifacts.items.id)
artifact_type: string
MIME-like artifact type e.g. 'application/vnd.ant.code'
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.artifacts.items.artifact_type)
title: string
Artifact title
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.artifacts.items.title)
version_id: string
Artifact version ID e.g. 'claude_artifact_version_abc123'
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.artifacts.items.version_id)
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.artifacts)
content: array of object { text, type }  or object { id, input, integration_name, 4 more }  or object { content, integration_name, is_error, 5 more } 
Content blocks within the message
Text object { text, type } 
Text content block.
text: string
Text content from human or assistant
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B0%5D.text)
type: "text"
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B0%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B0%5D)
ToolUse object { id, input, integration_name, 4 more } 
Tool invocation requested by the assistant.
Tool-use ID, e.g. 'toolu_01AbC...'
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B1%5D.id)
input: string
Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B1%5D.input)
integration_name: string
Name of the integration that provides this tool, when applicable
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B1%5D.integration_name)
mcp_server_url: string
Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B1%5D.mcp_server_url)
name: string
Name of the tool invoked
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B1%5D.name)
truncated: boolean
True when `input` was shortened. Pass tool_use_input_max_chars=-1 to disable the limit
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B1%5D.truncated)
type: "tool_use"
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B1%5D)
ToolResult object { content, integration_name, is_error, 5 more } 
Result returned by a tool invocation.
content: array of object { text, type } 
Text content returned by the tool. Generated files are surfaced via the message's `generated_files` list; other non-text item types (including images and links) are omitted.
text: string
Text returned by the tool
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B2%5D.content.items.text)
type: "text"
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B2%5D.content.items.type)
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B2%5D.content)
integration_name: string
Name of the integration that provides this tool, when applicable
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B2%5D.integration_name)
is_error: boolean
True when the tool reported an error
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B2%5D.is_error)
mcp_server_url: string
Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B2%5D.mcp_server_url)
name: string
Name of the tool that produced this result
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B2%5D.name)
tool_use_id: string
ID of the tool_use block this result responds to
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B2%5D.tool_use_id)
truncated: boolean
True when one or more text items in `content` were shortened. Pass tool_result_max_chars=-1 to retrieve full content.
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B2%5D.truncated)
type: "tool_result"
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B2%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content.items%5B2%5D)
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.content)
created_at: string
Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.created_at)
files: array of object { id, created_at, filename, 3 more } 
Binary file attachments uploaded by the user. Download via `GET /v1/compliance/apps/chats/files/{claude_file_id}/content`.
File ID
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.files.items.id)
created_at: string
File creation timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.files.items.created_at)
filename: string
Display name of the file
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.files.items.filename)
md5: string
Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available.
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.files.items.md5)
mime_type: string
MIME type of the file's preferred downloadable variant (e.g. 'application/pdf')
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.files.items.mime_type)
size_bytes: number
Size in bytes of the file's preferred downloadable variant, if known. Null for older files uploaded before size was recorded.
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.files.items.size_bytes)
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.files)
generated_files: array of object { id, filename, md5, 2 more } 
Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message. Download via `GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`.
Opaque generated-file id, e.g. 'claude_gen_file_abc123'. Treat as an opaque string; the encoding may change without notice.
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.generated_files.items.id)
filename: string
Display name of the generated file
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.generated_files.items.filename)
md5: string
Lowercase hex MD5 of the generated file, when available. Null when no stored hash is available.
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.generated_files.items.md5)
mime_type: string
MIME type reported by the tool that produced the file
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.generated_files.items.mime_type)
size_bytes: number
Size in bytes of the generated file, when available. Null when the file has expired or size is not recorded.
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.generated_files.items.size_bytes)
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.generated_files)
role: "assistant" or "user"
Message sender (user or assistant)
"assistant"
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.role%5B0%5D)
"user"
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.role%5B1%5D)
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response.role)
[](https://platform.claude.com/docs/en/api/compliance/apps#message_list_response)
####  AppsChatsFiles
##### [Get file metadata](https://platform.claude.com/docs/en/api/compliance/apps/chats/files/retrieve)
GET/v1/compliance/apps/chats/files/{claude_file_id}
##### [Delete file](https://platform.claude.com/docs/en/api/compliance/apps/chats/files/delete)
DELETE/v1/compliance/apps/chats/files/{claude_file_id}
##### [Download file content](https://platform.claude.com/docs/en/api/compliance/apps/chats/files/download)
GET/v1/compliance/apps/chats/files/{claude_file_id}/content
##### ModelsExpand Collapse 
FileRetrieveResponse object { id, claude_chat_ids, created_at, 5 more } 
File metadata for GET /v1/compliance/apps/chats/files/{claude_file_id}.
Returns metadata only. Use the sibling `/content` endpoint to download the file bytes.
File ID
[](https://platform.claude.com/docs/en/api/compliance/apps#file_retrieve_response.id)
claude_chat_ids: array of string
Chats this file is attached to. A file can be referenced by messages across multiple chats.
[](https://platform.claude.com/docs/en/api/compliance/apps#file_retrieve_response.claude_chat_ids)
created_at: string
File creation timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps#file_retrieve_response.created_at)
filename: string
Display name of the file, if set
[](https://platform.claude.com/docs/en/api/compliance/apps#file_retrieve_response.filename)
md5: string
Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes; when the two disagree, the header is authoritative.
[](https://platform.claude.com/docs/en/api/compliance/apps#file_retrieve_response.md5)
message_ids: array of string
Chat message IDs this file is attached to. A file can be referenced by multiple messages.
[](https://platform.claude.com/docs/en/api/compliance/apps#file_retrieve_response.message_ids)
mime_type: string
MIME type of the file's preferred downloadable variant (e.g. 'application/pdf'). May be null for files with no downloadable content (e.g. code-interpreter outputs).
[](https://platform.claude.com/docs/en/api/compliance/apps#file_retrieve_response.mime_type)
size_bytes: number
Size in bytes of the file's preferred downloadable variant, if known
[](https://platform.claude.com/docs/en/api/compliance/apps#file_retrieve_response.size_bytes)
[](https://platform.claude.com/docs/en/api/compliance/apps#file_retrieve_response)
FileDeleteResponse object { id, type } 
Response for deleting a compliance file.
The ID of the file that was deleted
[](https://platform.claude.com/docs/en/api/compliance/apps#file_delete_response.id)
type: optional "claude_file_deleted"
Constant string confirming deletion
[](https://platform.claude.com/docs/en/api/compliance/apps#file_delete_response.type)
[](https://platform.claude.com/docs/en/api/compliance/apps#file_delete_response)
####  AppsChatsGenerated Files
##### [Get Claude-generated file metadata](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/retrieve)
GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}
##### [Download a Claude-generated file](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/download)
GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content
##### ModelsExpand Collapse 
GeneratedFileRetrieveResponse object { id, claude_chat_id, created_at, 4 more } 
Metadata for GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}.
Returns metadata only. Use the sibling `/content` endpoint to download the bytes. The owning chat is included since the id is opaque; to find the specific message that produced the file, fetch `/v1/compliance/apps/chats/{claude_chat_id}/messages` and match on `generated_files[].id`.
Opaque generated-file id, e.g. 'claude_gen_file_abc123'.
[](https://platform.claude.com/docs/en/api/compliance/apps#generated_file_retrieve_response.id)
claude_chat_id: string
The chat this generated file belongs to
[](https://platform.claude.com/docs/en/api/compliance/apps#generated_file_retrieve_response.claude_chat_id)
created_at: string
File creation timestamp, when available
[](https://platform.claude.com/docs/en/api/compliance/apps#generated_file_retrieve_response.created_at)
filename: string
Display name of the generated file
[](https://platform.claude.com/docs/en/api/compliance/apps#generated_file_retrieve_response.filename)
md5: string
Lowercase hex MD5 of the stored file. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes.
[](https://platform.claude.com/docs/en/api/compliance/apps#generated_file_retrieve_response.md5)
mime_type: string
MIME type of the stored file, when available
[](https://platform.claude.com/docs/en/api/compliance/apps#generated_file_retrieve_response.mime_type)
size_bytes: number
Size in bytes of the stored file, when available
[](https://platform.claude.com/docs/en/api/compliance/apps#generated_file_retrieve_response.size_bytes)
[](https://platform.claude.com/docs/en/api/compliance/apps#generated_file_retrieve_response)
####  AppsProjects
##### [List projects](https://platform.claude.com/docs/en/api/compliance/apps/projects/list)
GET/v1/compliance/apps/projects
##### [Get project details](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve)
GET/v1/compliance/apps/projects/{project_id}
##### [Delete project](https://platform.claude.com/docs/en/api/compliance/apps/projects/delete)
DELETE/v1/compliance/apps/projects/{project_id}
##### ModelsExpand Collapse 
ProjectListResponse object { id, created_at, deleted_at, 6 more } 
Project information for compliance responses.
Project identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps#project_list_response.id)
created_at: string
Project creation timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps#project_list_response.created_at)
deleted_at: string
Timestamp when the project was deleted by an end user, or null otherwise
[](https://platform.claude.com/docs/en/api/compliance/apps#project_list_response.deleted_at)
is_private: boolean
If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators
[](https://platform.claude.com/docs/en/api/compliance/apps#project_list_response.is_private)
name: string
Project name
[](https://platform.claude.com/docs/en/api/compliance/apps#project_list_response.name)
Deprecatedorganization_id: string
Organization identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps#project_list_response.organization_id)
organization_uuid: string
Organization UUID this project belongs to
[](https://platform.claude.com/docs/en/api/compliance/apps#project_list_response.organization_uuid)
updated_at: string
Project last update timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps#project_list_response.updated_at)
user: object { id, email_address } 
The user who created a project or project document.
Fields that reference this type are null when the creator's account has been deleted or the creator is no longer a member of any organization under the parent organization.
User identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps#project_list_response.user.id)
email_address: string
User's email address
[](https://platform.claude.com/docs/en/api/compliance/apps#project_list_response.user.email_address)
[](https://platform.claude.com/docs/en/api/compliance/apps#project_list_response.user)
[](https://platform.claude.com/docs/en/api/compliance/apps#project_list_response)
ProjectRetrieveResponse object { id, attachments_count, chats_count, 10 more } 
Detailed project information for compliance responses.
Project identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps#project_retrieve_response.id)
attachments_count: number
Number of attachments contained within this project
[](https://platform.claude.com/docs/en/api/compliance/apps#project_retrieve_response.attachments_count)
chats_count: number
Number of chats contained within this project
[](https://platform.claude.com/docs/en/api/compliance/apps#project_retrieve_response.chats_count)
created_at: string
Project creation timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps#project_retrieve_response.created_at)
deleted_at: string
Timestamp when the project was deleted by an end user, or null otherwise
[](https://platform.claude.com/docs/en/api/compliance/apps#project_retrieve_response.deleted_at)
description: string
Project description
[](https://platform.claude.com/docs/en/api/compliance/apps#project_retrieve_response.description)
instructions: string
Project's custom instructions / prompt
[](https://platform.claude.com/docs/en/api/compliance/apps#project_retrieve_response.instructions)
is_private: boolean
If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators
[](https://platform.claude.com/docs/en/api/compliance/apps#project_retrieve_response.is_private)
name: string
Project name
[](https://platform.claude.com/docs/en/api/compliance/apps#project_retrieve_response.name)
Deprecatedorganization_id: string
Organization identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps#project_retrieve_response.organization_id)
organization_uuid: string
Organization UUID this project belongs to
[](https://platform.claude.com/docs/en/api/compliance/apps#project_retrieve_response.organization_uuid)
updated_at: string
Project last update timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps#project_retrieve_response.updated_at)
user: object { id, email_address } 
The user who created a project or project document.
Fields that reference this type are null when the creator's account has been deleted or the creator is no longer a member of any organization under the parent organization.
User identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps#project_retrieve_response.user.id)
email_address: string
User's email address
[](https://platform.claude.com/docs/en/api/compliance/apps#project_retrieve_response.user.email_address)
[](https://platform.claude.com/docs/en/api/compliance/apps#project_retrieve_response.user)
[](https://platform.claude.com/docs/en/api/compliance/apps#project_retrieve_response)
ProjectDeleteResponse object { id, type } 
Response for deleting a Claude project.
The ID of the Claude project that was deleted
[](https://platform.claude.com/docs/en/api/compliance/apps#project_delete_response.id)
type: optional "claude_project_deleted"
Constant string confirming deletion.
[](https://platform.claude.com/docs/en/api/compliance/apps#project_delete_response.type)
[](https://platform.claude.com/docs/en/api/compliance/apps#project_delete_response)
####  AppsProjectsAttachments
##### [List project attachments](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list)
GET/v1/compliance/apps/projects/{project_id}/attachments
##### ModelsExpand Collapse 
AttachmentListResponse = object { id, created_at, filename, 4 more }  or object { id, created_at, filename, 3 more } 
File attachment reference for compliance responses.
ComplianceProjectFileReference object { id, created_at, filename, 4 more } 
File attachment reference for compliance responses.
File identifier (e.g., 'claude_file_abcd')
[](https://platform.claude.com/docs/en/api/compliance/apps#attachment_list_response%5B0%5D.id)
created_at: string
Creation timestamp (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps#attachment_list_response%5B0%5D.created_at)
filename: string
Display name of the file (e.g., 'document.pdf')
[](https://platform.claude.com/docs/en/api/compliance/apps#attachment_list_response%5B0%5D.filename)
md5: string
Lowercase hex MD5 of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.
[](https://platform.claude.com/docs/en/api/compliance/apps#attachment_list_response%5B0%5D.md5)
mime_type: string
MIME type of the file's preferred downloadable variant when one is recorded, else 'application/octet-stream'. Use the per-file `/metadata` endpoint for the authoritative value.
[](https://platform.claude.com/docs/en/api/compliance/apps#attachment_list_response%5B0%5D.mime_type)
size_bytes: number
Size in bytes of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.
[](https://platform.claude.com/docs/en/api/compliance/apps#attachment_list_response%5B0%5D.size_bytes)
type: "project_file"
Discriminator marking this as a binary file
[](https://platform.claude.com/docs/en/api/compliance/apps#attachment_list_response%5B0%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/apps#attachment_list_response%5B0%5D)
ComplianceProjectDocReference object { id, created_at, filename, 3 more } 
Project document attachment reference for compliance responses.
Project document identifier (e.g., 'claude_proj_doc_abcd')
[](https://platform.claude.com/docs/en/api/compliance/apps#attachment_list_response%5B1%5D.id)
created_at: string
Creation timestamp (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps#attachment_list_response%5B1%5D.created_at)
filename: string
Display name of the document (e.g., 'document.txt')
[](https://platform.claude.com/docs/en/api/compliance/apps#attachment_list_response%5B1%5D.filename)
mime_type: "text/plain"
MIME type of the project document, always set to plain text
[](https://platform.claude.com/docs/en/api/compliance/apps#attachment_list_response%5B1%5D.mime_type)
type: "project_doc"
Discriminator marking this as a plain text document
[](https://platform.claude.com/docs/en/api/compliance/apps#attachment_list_response%5B1%5D.type)
updated_at: string
Last-modified timestamp of the document. Reserved for future use — currently always null.
[](https://platform.claude.com/docs/en/api/compliance/apps#attachment_list_response%5B1%5D.updated_at)
[](https://platform.claude.com/docs/en/api/compliance/apps#attachment_list_response%5B1%5D)
[](https://platform.claude.com/docs/en/api/compliance/apps#attachment_list_response)
####  AppsProjectsCollaborators
##### [List project collaborators](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list)
GET/v1/compliance/apps/projects/{project_id}/collaborators
##### ModelsExpand Collapse 
CollaboratorListResponse = object { granted_at, role, type, user_id }  or object { granted_at, group_id, role, type }  or object { granted_at, organization_uuid, role, type }  or object { granted_at, organization_role, role, type } 
An individual user granted a role on a project.
ComplianceProjectUserCollaborator object { granted_at, role, type, user_id } 
An individual user granted a role on a project.
granted_at: string
When this collaborator was granted access (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B0%5D.granted_at)
role: "admin" or "editor" or "owner" or "viewer"
Role granted on the project
"admin"
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B0%5D.role%5B0%5D)
"editor"
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B0%5D.role%5B1%5D)
"owner"
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B0%5D.role%5B2%5D)
"viewer"
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B0%5D.role%5B3%5D)
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B0%5D.role)
type: "user"
Discriminator marking this as an individual user collaborator
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B0%5D.type)
user_id: string
Identifier of the user granted access (tagged ID), or null if their account has since been deleted
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B0%5D.user_id)
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B0%5D)
ComplianceProjectGroupCollaborator object { granted_at, group_id, role, type } 
An RBAC group granted a role on a project.
granted_at: string
When this collaborator was granted access (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B1%5D.granted_at)
group_id: string
Identifier of the group granted access (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B1%5D.group_id)
role: "admin" or "editor" or "owner" or "viewer"
Role granted on the project
"admin"
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B1%5D.role%5B0%5D)
"editor"
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B1%5D.role%5B1%5D)
"owner"
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B1%5D.role%5B2%5D)
"viewer"
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B1%5D.role%5B3%5D)
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B1%5D.role)
type: "group"
Discriminator marking this as a group collaborator
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B1%5D)
ComplianceProjectOrganizationCollaborator object { granted_at, organization_uuid, role, type } 
An entire organization granted a role on a project.
granted_at: string
When this collaborator was granted access (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B2%5D.granted_at)
organization_uuid: string
UUID of the organization granted access
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B2%5D.organization_uuid)
role: "admin" or "editor" or "owner" or "viewer"
Role granted on the project
"admin"
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B2%5D.role%5B0%5D)
"editor"
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B2%5D.role%5B1%5D)
"owner"
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B2%5D.role%5B2%5D)
"viewer"
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B2%5D.role%5B3%5D)
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B2%5D.role)
type: "organization"
Discriminator marking this as an organization-wide grant
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B2%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B2%5D)
ComplianceProjectOrganizationRoleCollaborator object { granted_at, organization_role, role, type } 
All holders of an organization-level role granted a role on a project.
granted_at: string
When this collaborator was granted access (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B3%5D.granted_at)
organization_role: string
The organization-level role whose holders are granted access
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B3%5D.organization_role)
role: "admin" or "editor" or "owner" or "viewer"
Role granted on the project
"admin"
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B3%5D.role%5B0%5D)
"editor"
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B3%5D.role%5B1%5D)
"owner"
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B3%5D.role%5B2%5D)
"viewer"
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B3%5D.role%5B3%5D)
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B3%5D.role)
type: "organization_role"
Discriminator marking this as a grant to all organization members holding a specific org-level role
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B3%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response%5B3%5D)
[](https://platform.claude.com/docs/en/api/compliance/apps#collaborator_list_response)
####  AppsProjectsDocuments
##### [Get project document content](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/retrieve)
GET/v1/compliance/apps/projects/documents/{document_id}
##### [Get project document metadata](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata)
GET/v1/compliance/apps/projects/documents/{document_id}/metadata
##### [Delete project document](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/delete)
DELETE/v1/compliance/apps/projects/documents/{document_id}
##### ModelsExpand Collapse 
DocumentRetrieveResponse object { id, content, created_at, 2 more } 
Project document information for compliance responses.
Project document identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps#document_retrieve_response.id)
content: string
Document text content
[](https://platform.claude.com/docs/en/api/compliance/apps#document_retrieve_response.content)
created_at: string
Document creation timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps#document_retrieve_response.created_at)
filename: string
Document filename
[](https://platform.claude.com/docs/en/api/compliance/apps#document_retrieve_response.filename)
user: object { id, email_address } 
The user who created a project or project document.
Fields that reference this type are null when the creator's account has been deleted or the creator is no longer a member of any organization under the parent organization.
User identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps#document_retrieve_response.user.id)
email_address: string
User's email address
[](https://platform.claude.com/docs/en/api/compliance/apps#document_retrieve_response.user.email_address)
[](https://platform.claude.com/docs/en/api/compliance/apps#document_retrieve_response.user)
[](https://platform.claude.com/docs/en/api/compliance/apps#document_retrieve_response)
DocumentMetadataResponse object { id, claude_project_id, created_at, 5 more } 
Project document metadata for GET /v1/compliance/apps/projects/documents/{document_id}/metadata.
Returns metadata only. Use the sibling endpoint (without `/metadata`) to fetch the document text content.
Project document identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps#document_metadata_response.id)
claude_project_id: string
The project this document belongs to
[](https://platform.claude.com/docs/en/api/compliance/apps#document_metadata_response.claude_project_id)
created_at: string
Document creation timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps#document_metadata_response.created_at)
filename: string
Document filename
[](https://platform.claude.com/docs/en/api/compliance/apps#document_metadata_response.filename)
md5: string
Lowercase hex MD5 of the document content (UTF-8 encoded). Matches the `content` field returned by the sibling content endpoint.
[](https://platform.claude.com/docs/en/api/compliance/apps#document_metadata_response.md5)
mime_type: "text/plain"
MIME type of the document content, always plain text
[](https://platform.claude.com/docs/en/api/compliance/apps#document_metadata_response.mime_type)
size_bytes: number
Size in bytes of the document content (UTF-8 encoded)
[](https://platform.claude.com/docs/en/api/compliance/apps#document_metadata_response.size_bytes)
user: object { id, email_address } 
The user who created a project or project document.
Fields that reference this type are null when the creator's account has been deleted or the creator is no longer a member of any organization under the parent organization.
User identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps#document_metadata_response.user.id)
email_address: string
User's email address
[](https://platform.claude.com/docs/en/api/compliance/apps#document_metadata_response.user.email_address)
[](https://platform.claude.com/docs/en/api/compliance/apps#document_metadata_response.user)
[](https://platform.claude.com/docs/en/api/compliance/apps#document_metadata_response)
DocumentDeleteResponse object { id, type } 
Response for deleting a project document.
The ID of the project document that was deleted
[](https://platform.claude.com/docs/en/api/compliance/apps#document_delete_response.id)
type: "claude_project_document_deleted"
Constant string confirming deletion.
[](https://platform.claude.com/docs/en/api/compliance/apps#document_delete_response.type)
[](https://platform.claude.com/docs/en/api/compliance/apps#document_delete_response)
####  AppsArtifacts
##### [Get artifact metadata](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/retrieve)
GET/v1/compliance/apps/artifacts/{artifact_version_id}
##### [Download artifact content](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/download)
GET/v1/compliance/apps/artifacts/{artifact_version_id}/content
##### ModelsExpand Collapse 
ArtifactRetrieveResponse object { id, artifact_type, claude_chat_id, 5 more } 
Artifact version metadata for GET /v1/compliance/apps/artifacts/{artifact_version_id}.
Returns metadata only. Use the sibling `/content` endpoint to fetch the artifact body.
Artifact ID e.g. 'claude_artifact_abc123'
[](https://platform.claude.com/docs/en/api/compliance/apps#artifact_retrieve_response.id)
artifact_type: string
MIME-like artifact type e.g. 'application/vnd.ant.code'
[](https://platform.claude.com/docs/en/api/compliance/apps#artifact_retrieve_response.artifact_type)
claude_chat_id: string
The chat this artifact belongs to
[](https://platform.claude.com/docs/en/api/compliance/apps#artifact_retrieve_response.claude_chat_id)
created_at: string
Artifact version creation timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps#artifact_retrieve_response.created_at)
md5: string
Lowercase hex MD5 of the artifact content (UTF-8 encoded). Matches the `content` field returned by the sibling `/content` endpoint.
[](https://platform.claude.com/docs/en/api/compliance/apps#artifact_retrieve_response.md5)
size_bytes: number
Size in bytes of the artifact content (UTF-8 encoded)
[](https://platform.claude.com/docs/en/api/compliance/apps#artifact_retrieve_response.size_bytes)
title: string
Artifact title
[](https://platform.claude.com/docs/en/api/compliance/apps#artifact_retrieve_response.title)
version_id: string
Artifact version ID e.g. 'claude_artifact_version_abc123'
[](https://platform.claude.com/docs/en/api/compliance/apps#artifact_retrieve_response.version_id)
[](https://platform.claude.com/docs/en/api/compliance/apps#artifact_retrieve_response)
