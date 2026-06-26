<!-- source: https://platform.claude.com/docs/en/api/compliance/apps/projects/list -->

# List projects
GET/v1/compliance/apps/projects
Lists project metadata with filtering capabilities. Results are sorted chronologically (time ascending) by created_at.
##### Query ParametersExpand Collapse 
created_at: optional object { gt, gte, lt, lte } 
gt: optional string
Filter projects created after this time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list.created_at.gt)
gte: optional string
Filter projects created at or after this time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list.created_at.gte)
lt: optional string
Filter projects created before this time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list.created_at.lt)
lte: optional string
Filter projects created at or before this time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list.created_at.lte)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list.created_at)
limit: optional number
Maximum results (default: 20, max: 100)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list.limit)
organization_ids: optional array of string
Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list.organization_ids)
page: optional string
Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list.page)
updated_at: optional object { gt, gte, lt, lte } 
gt: optional string
Filter projects updated after this time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list.updated_at.gt)
gte: optional string
Filter projects updated at or after this time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list.updated_at.gte)
lt: optional string
Filter projects updated before this time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list.updated_at.lt)
lte: optional string
Filter projects updated at or before this time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list.updated_at.lte)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list.updated_at)
user_ids: optional array of string
Filter by user IDs. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list.user_ids)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list.x-api-key)
data: array of object { id, created_at, deleted_at, 6 more } 
List of projects sorted by creation date ascending
Project identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#project_list_response.id)
created_at: string
Project creation timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#project_list_response.created_at)
deleted_at: string
Timestamp when the project was deleted by an end user, or null otherwise
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#project_list_response.deleted_at)
is_private: boolean
If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#project_list_response.is_private)
name: string
Project name
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#project_list_response.name)
Deprecatedorganization_id: string
Organization identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#project_list_response.organization_id)
organization_uuid: string
Organization UUID this project belongs to
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#project_list_response.organization_uuid)
updated_at: string
Project last update timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#project_list_response.updated_at)
user: object { id, email_address } 
The user who created a project or project document.
Fields that reference this type are null when the creator's account has been deleted or the creator is no longer a member of any organization under the parent organization.
User identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#project_list_response.user.id)
email_address: string
User's email address
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#project_list_response.user.email_address)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#project_list_response.user)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list)
has_more: boolean
Whether more records exist beyond the current result set
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list)
next_page: string
Token to retrieve the next page. Use this as the 'page' parameter in your next request
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/list#list)
List projects

curl https://api.anthropic.com/v1/compliance/apps/projects \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "data": [
      "id": "claude_proj_abc123",
      "name": "Q4 Product Planning",
      "created_at": "2025-06-01T10:00:00Z",
      "updated_at": "2025-06-15T14:30:00Z",
      "is_private": true,
      "organization_id": "org_abc123",
      "organization_uuid": "abc12345-6789-0abc-def0-123456789abc",
      "user": {
        "id": "user_xyz456",
        "email_address": "user@example.com"
  ],
  "has_more": true,
  "next_page": "page_eyJjcmVhdGVkX2F0IjoiMjAyNS0wNi0wMVQxMDowMDowMFoiLCJ1dWlkIjoiYWJjMTIzIn0="

  "data": [
      "id": "claude_proj_abc123",
      "name": "Q4 Product Planning",
      "created_at": "2025-06-01T10:00:00Z",
      "updated_at": "2025-06-15T14:30:00Z",
      "is_private": true,
      "organization_id": "org_abc123",
      "organization_uuid": "abc12345-6789-0abc-def0-123456789abc",
      "user": {
        "id": "user_xyz456",
        "email_address": "user@example.com"
  ],
  "has_more": true,
  "next_page": "page_eyJjcmVhdGVkX2F0IjoiMjAyNS0wNi0wMVQxMDowMDowMFoiLCJ1dWlkIjoiYWJjMTIzIn0="
