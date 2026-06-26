<!-- source: https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list -->

# List project attachments
GET/v1/compliance/apps/projects/{project_id}/attachments
List files and documents attached to a project.
List files and project documents attached to the project referenced by project_id. This includes the IDs of attached files, and attached project documents.
The raw binary content of attached files can be downloaded using the GET /v1/compliance/apps/chats/files/{claude_file_id}/content endpoint.
The text content of attached project documents can be fetched using the GET /v1/compliance/apps/projects/documents/{claude_proj_doc_id} endpoint.
##### Path ParametersExpand Collapse 
project_id: string
The project ID (tagged ID, e.g., claude_proj_abc123)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#list.project_id)
##### Query ParametersExpand Collapse 
limit: optional number
Maximum results (default: 20, max: 100)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#list.limit)
page: optional string
Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#list.page)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#list.x-api-key)
data: array of object { id, created_at, filename, 4 more }  or object { id, created_at, filename, 3 more } 
List of attachments sorted chronologically by created_at, tie break by id
ComplianceProjectFileReference object { id, created_at, filename, 4 more } 
File attachment reference for compliance responses.
File identifier (e.g., 'claude_file_abcd')
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#attachment_list_response%5B0%5D.id)
created_at: string
Creation timestamp (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#attachment_list_response%5B0%5D.created_at)
filename: string
Display name of the file (e.g., 'document.pdf')
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#attachment_list_response%5B0%5D.filename)
md5: string
Lowercase hex MD5 of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#attachment_list_response%5B0%5D.md5)
mime_type: string
MIME type of the file's preferred downloadable variant when one is recorded, else 'application/octet-stream'. Use the per-file `/metadata` endpoint for the authoritative value.
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#attachment_list_response%5B0%5D.mime_type)
size_bytes: number
Size in bytes of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#attachment_list_response%5B0%5D.size_bytes)
type: "project_file"
Discriminator marking this as a binary file
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#attachment_list_response%5B0%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#attachment_list_response%5B0%5D)
ComplianceProjectDocReference object { id, created_at, filename, 3 more } 
Project document attachment reference for compliance responses.
Project document identifier (e.g., 'claude_proj_doc_abcd')
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#attachment_list_response%5B1%5D.id)
created_at: string
Creation timestamp (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#attachment_list_response%5B1%5D.created_at)
filename: string
Display name of the document (e.g., 'document.txt')
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#attachment_list_response%5B1%5D.filename)
mime_type: "text/plain"
MIME type of the project document, always set to plain text
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#attachment_list_response%5B1%5D.mime_type)
type: "project_doc"
Discriminator marking this as a plain text document
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#attachment_list_response%5B1%5D.type)
updated_at: string
Last-modified timestamp of the document. Reserved for future use — currently always null.
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#attachment_list_response%5B1%5D.updated_at)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#attachment_list_response%5B1%5D)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#list)
has_more: boolean
Whether more records exist beyond the current result set
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#list)
next_page: string
To get the next page, use the 'next_page' from the current response as the 'page' in your next request
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list#list)
List project attachments

curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/attachments \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "data": [
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "filename": "filename",
      "md5": "md5",
      "mime_type": "mime_type",
      "size_bytes": 0,
      "type": "project_file"
  ],
  "has_more": true,
  "next_page": "next_page"

  "data": [
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "filename": "filename",
      "md5": "md5",
      "mime_type": "mime_type",
      "size_bytes": 0,
      "type": "project_file"
  ],
  "has_more": true,
  "next_page": "next_page"
