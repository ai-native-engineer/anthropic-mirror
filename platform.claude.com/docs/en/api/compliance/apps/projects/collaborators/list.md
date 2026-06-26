<!-- source: https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list -->

# List project collaborators
GET/v1/compliance/apps/projects/{project_id}/collaborators
List the users, groups, and organization-wide grants on a project.
Each entry represents one active role assignment on the project. Principals are returned as a discriminated union on `type` — an individual user, an RBAC group, the whole organization, or all holders of an organization-level role.
##### Path ParametersExpand Collapse 
project_id: string
The project ID (tagged ID, e.g., claude_proj_abc123)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#list.project_id)
##### Query ParametersExpand Collapse 
limit: optional number
Maximum results (default: 20, max: 100)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#list.limit)
page: optional string
Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#list.page)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#list.x-api-key)
data: array of object { granted_at, role, type, user_id }  or object { granted_at, group_id, role, type }  or object { granted_at, organization_uuid, role, type }  or object { granted_at, organization_role, role, type } 
List of collaborators sorted chronologically by granted_at, tie break by the underlying role-assignment UUID
ComplianceProjectUserCollaborator object { granted_at, role, type, user_id } 
An individual user granted a role on a project.
granted_at: string
When this collaborator was granted access (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B0%5D.granted_at)
role: "admin" or "editor" or "owner" or "viewer"
Role granted on the project
"admin"
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B0%5D.role%5B0%5D)
"editor"
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B0%5D.role%5B1%5D)
"owner"
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B0%5D.role%5B2%5D)
"viewer"
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B0%5D.role%5B3%5D)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B0%5D.role)
type: "user"
Discriminator marking this as an individual user collaborator
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B0%5D.type)
user_id: string
Identifier of the user granted access (tagged ID), or null if their account has since been deleted
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B0%5D.user_id)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B0%5D)
ComplianceProjectGroupCollaborator object { granted_at, group_id, role, type } 
An RBAC group granted a role on a project.
granted_at: string
When this collaborator was granted access (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B1%5D.granted_at)
group_id: string
Identifier of the group granted access (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B1%5D.group_id)
role: "admin" or "editor" or "owner" or "viewer"
Role granted on the project
"admin"
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B1%5D.role%5B0%5D)
"editor"
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B1%5D.role%5B1%5D)
"owner"
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B1%5D.role%5B2%5D)
"viewer"
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B1%5D.role%5B3%5D)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B1%5D.role)
type: "group"
Discriminator marking this as a group collaborator
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B1%5D)
ComplianceProjectOrganizationCollaborator object { granted_at, organization_uuid, role, type } 
An entire organization granted a role on a project.
granted_at: string
When this collaborator was granted access (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B2%5D.granted_at)
organization_uuid: string
UUID of the organization granted access
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B2%5D.organization_uuid)
role: "admin" or "editor" or "owner" or "viewer"
Role granted on the project
"admin"
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B2%5D.role%5B0%5D)
"editor"
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B2%5D.role%5B1%5D)
"owner"
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B2%5D.role%5B2%5D)
"viewer"
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B2%5D.role%5B3%5D)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B2%5D.role)
type: "organization"
Discriminator marking this as an organization-wide grant
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B2%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B2%5D)
ComplianceProjectOrganizationRoleCollaborator object { granted_at, organization_role, role, type } 
All holders of an organization-level role granted a role on a project.
granted_at: string
When this collaborator was granted access (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B3%5D.granted_at)
organization_role: string
The organization-level role whose holders are granted access
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B3%5D.organization_role)
role: "admin" or "editor" or "owner" or "viewer"
Role granted on the project
"admin"
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B3%5D.role%5B0%5D)
"editor"
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B3%5D.role%5B1%5D)
"owner"
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B3%5D.role%5B2%5D)
"viewer"
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B3%5D.role%5B3%5D)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B3%5D.role)
type: "organization_role"
Discriminator marking this as a grant to all organization members holding a specific org-level role
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B3%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#collaborator_list_response%5B3%5D)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#list)
has_more: boolean
Whether more records exist beyond the current result set
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#list)
next_page: string
To get the next page, use the 'next_page' from the current response as the 'page' in your next request
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list#list)
List project collaborators

curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/collaborators \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "data": [
      "granted_at": "2019-12-27T18:11:19.117Z",
      "role": "admin",
      "type": "user",
      "user_id": "user_id"
  ],
  "has_more": true,
  "next_page": "next_page"

  "data": [
      "granted_at": "2019-12-27T18:11:19.117Z",
      "role": "admin",
      "type": "user",
      "user_id": "user_id"
  ],
  "has_more": true,
  "next_page": "next_page"
