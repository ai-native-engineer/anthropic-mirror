<!-- source: https://platform.claude.com/docs/en/api/compliance/organizations/roles/list -->

# List Compliance Roles
GET/v1/compliance/organizations/{org_uuid}/roles
List Compliance Roles
##### Path ParametersExpand Collapse 
org_uuid: string
The organization UUID
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/list#list.org_uuid)
##### Query ParametersExpand Collapse 
limit: optional number
Maximum results (default: 500, max: 1000)
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/list#list.limit)
page: optional string
Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/list#list.page)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/list#list.x-api-key)
data: array of object { id, created_at, description, 2 more } 
List of roles
Role identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/list#role_list_response.id)
created_at: string
Role creation timestamp (ISO 8601)
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/list#role_list_response.created_at)
description: string
Role description
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/list#role_list_response.description)
name: string
Role name
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/list#role_list_response.name)
updated_at: string
Role last-updated timestamp (ISO 8601)
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/list#role_list_response.updated_at)
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/list#list)
has_more: boolean
Whether more records exist beyond the current result set
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/list#list)
next_page: string
Token to retrieve the next page. Use this as the 'page' parameter in your next request
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/list#list)
List Compliance Roles

curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "data": [
      "id": "id",
      "created_at": "created_at",
      "description": "description",
      "name": "name",
      "updated_at": "updated_at"
  ],
  "has_more": true,
  "next_page": "next_page"

  "data": [
      "id": "id",
      "created_at": "created_at",
      "description": "description",
      "name": "name",
      "updated_at": "updated_at"
  ],
  "has_more": true,
  "next_page": "next_page"
