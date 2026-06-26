<!-- source: https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/retrieve -->

# Get project document content
GET/v1/compliance/apps/projects/documents/{document_id}
Get detailed information for a specific project document.
##### Path ParametersExpand Collapse 
document_id: string
The document ID (tagged ID, e.g., claude_proj_doc_abc123)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/retrieve#retrieve.document_id)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/retrieve#retrieve.x-api-key)
Project document identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/retrieve#document_retrieve_response.id)
content: string
Document text content
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/retrieve#document_retrieve_response.content)
created_at: string
Document creation timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/retrieve#document_retrieve_response.created_at)
filename: string
Document filename
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/retrieve#document_retrieve_response.filename)
user: object { id, email_address } 
The user who created a project or project document.
Fields that reference this type are null when the creator's account has been deleted or the creator is no longer a member of any organization under the parent organization.
User identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/retrieve#document_retrieve_response.user.id)
email_address: string
User's email address
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/retrieve#document_retrieve_response.user.email_address)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/retrieve#document_retrieve_response.user)
Get project document content

curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "id": "id",
  "content": "content",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "user": {
    "id": "id",
    "email_address": "email_address"

  "id": "id",
  "content": "content",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "user": {
    "id": "id",
    "email_address": "email_address"
