<!-- source: https://platform.claude.com/docs/en/api/compliance/groups/list -->

# List Compliance Groups
GET/v1/compliance/groups
List Compliance Groups
##### Query ParametersExpand Collapse 
limit: optional number
Maximum results (default: 500, max: 1000)
[](https://platform.claude.com/docs/en/api/compliance/groups/list#list.limit)
name_prefix: optional string
Filter groups by name prefix
[](https://platform.claude.com/docs/en/api/compliance/groups/list#list.name_prefix)
page: optional string
Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.
[](https://platform.claude.com/docs/en/api/compliance/groups/list#list.page)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/groups/list#list.x-api-key)
data: array of object { id, created_at, description, 4 more } 
List of groups
Group identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/groups/list#group_list_response.id)
created_at: string
Group creation timestamp (ISO 8601)
[](https://platform.claude.com/docs/en/api/compliance/groups/list#group_list_response.created_at)
description: string
Group description
[](https://platform.claude.com/docs/en/api/compliance/groups/list#group_list_response.description)
name: string
Group name
[](https://platform.claude.com/docs/en/api/compliance/groups/list#group_list_response.name)
roles: array of string
Role IDs assigned to this group.
[](https://platform.claude.com/docs/en/api/compliance/groups/list#group_list_response.roles)
source_type: string
How the group was created ('direct' or 'scim')
[](https://platform.claude.com/docs/en/api/compliance/groups/list#group_list_response.source_type)
updated_at: string
Group last-updated timestamp (ISO 8601)
[](https://platform.claude.com/docs/en/api/compliance/groups/list#group_list_response.updated_at)
[](https://platform.claude.com/docs/en/api/compliance/groups/list#list)
has_more: boolean
Whether more records exist beyond the current result set
[](https://platform.claude.com/docs/en/api/compliance/groups/list#list)
next_page: string
Token to retrieve the next page. Use this as the 'page' parameter in your next request
[](https://platform.claude.com/docs/en/api/compliance/groups/list#list)
List Compliance Groups

curl https://api.anthropic.com/v1/compliance/groups \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "data": [
      "id": "id",
      "created_at": "created_at",
      "description": "description",
      "name": "name",
      "roles": [
        "string"
      ],
      "source_type": "source_type",
      "updated_at": "updated_at"
  ],
  "has_more": true,
  "next_page": "next_page"

  "data": [
      "id": "id",
      "created_at": "created_at",
      "description": "description",
      "name": "name",
      "roles": [
        "string"
      ],
      "source_type": "source_type",
      "updated_at": "updated_at"
  ],
  "has_more": true,
  "next_page": "next_page"
