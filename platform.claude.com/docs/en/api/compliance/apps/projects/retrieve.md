<!-- source: https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve -->

# Get project details
GET/v1/compliance/apps/projects/{project_id}
Get detailed information for a specific project.
##### Path ParametersExpand Collapse 
project_id: string
The project ID (tagged ID, e.g., claude_proj_abc123)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve#retrieve.project_id)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve#retrieve.x-api-key)
Project identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve#project_retrieve_response.id)
attachments_count: number
Number of attachments contained within this project
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve#project_retrieve_response.attachments_count)
chats_count: number
Number of chats contained within this project
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve#project_retrieve_response.chats_count)
created_at: string
Project creation timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve#project_retrieve_response.created_at)
deleted_at: string
Timestamp when the project was deleted by an end user, or null otherwise
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve#project_retrieve_response.deleted_at)
description: string
Project description
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve#project_retrieve_response.description)
instructions: string
Project's custom instructions / prompt
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve#project_retrieve_response.instructions)
is_private: boolean
If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve#project_retrieve_response.is_private)
name: string
Project name
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve#project_retrieve_response.name)
Deprecatedorganization_id: string
Organization identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve#project_retrieve_response.organization_id)
organization_uuid: string
Organization UUID this project belongs to
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve#project_retrieve_response.organization_uuid)
updated_at: string
Project last update timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve#project_retrieve_response.updated_at)
user: object { id, email_address } 
The user who created a project or project document.
Fields that reference this type are null when the creator's account has been deleted or the creator is no longer a member of any organization under the parent organization.
User identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve#project_retrieve_response.user.id)
email_address: string
User's email address
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve#project_retrieve_response.user.email_address)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve#project_retrieve_response.user)
Get project details

curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "id": "id",
  "attachments_count": 0,
  "chats_count": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "instructions": "instructions",
  "is_private": true,
  "name": "name",
  "organization_id": "organization_id",
  "organization_uuid": "organization_uuid",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "user": {
    "id": "id",
    "email_address": "email_address"

  "id": "id",
  "attachments_count": 0,
  "chats_count": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "instructions": "instructions",
  "is_private": true,
  "name": "name",
  "organization_id": "organization_id",
  "organization_uuid": "organization_uuid",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "user": {
    "id": "id",
    "email_address": "email_address"
