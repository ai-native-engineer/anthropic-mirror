<!-- source: https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata -->

# Get project document metadata
GET/v1/compliance/apps/projects/documents/{document_id}/metadata
Returns metadata for a project document, without the content body.
Use the sibling `GET /v1/compliance/apps/projects/documents/{document_id}` endpoint to fetch the document text. The `md5` and `size_bytes` fields here are computed over the UTF-8 encoding of that text, so a DLP consumer can dedupe or match hashes without downloading every document.
##### Path ParametersExpand Collapse 
document_id: string
The document ID (tagged ID, e.g., claude_proj_doc_abc123)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata#metadata.document_id)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata#metadata.x-api-key)
Project document identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata#document_metadata_response.id)
claude_project_id: string
The project this document belongs to
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata#document_metadata_response.claude_project_id)
created_at: string
Document creation timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata#document_metadata_response.created_at)
filename: string
Document filename
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata#document_metadata_response.filename)
md5: string
Lowercase hex MD5 of the document content (UTF-8 encoded). Matches the `content` field returned by the sibling content endpoint.
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata#document_metadata_response.md5)
mime_type: "text/plain"
MIME type of the document content, always plain text
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata#document_metadata_response.mime_type)
size_bytes: number
Size in bytes of the document content (UTF-8 encoded)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata#document_metadata_response.size_bytes)
user: object { id, email_address } 
The user who created a project or project document.
Fields that reference this type are null when the creator's account has been deleted or the creator is no longer a member of any organization under the parent organization.
User identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata#document_metadata_response.user.id)
email_address: string
User's email address
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata#document_metadata_response.user.email_address)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata#document_metadata_response.user)
Get project document metadata

curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID/metadata \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "id": "id",
  "claude_project_id": "claude_project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "text/plain",
  "size_bytes": 0,
  "user": {
    "id": "id",
    "email_address": "email_address"

  "id": "id",
  "claude_project_id": "claude_project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "text/plain",
  "size_bytes": 0,
  "user": {
    "id": "id",
    "email_address": "email_address"
