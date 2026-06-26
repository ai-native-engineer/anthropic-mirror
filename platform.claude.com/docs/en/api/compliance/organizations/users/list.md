<!-- source: https://platform.claude.com/docs/en/api/compliance/organizations/users/list -->

# List organization users
GET/v1/compliance/organizations/{org_uuid}/users
List current user members of an organization.
##### Path ParametersExpand Collapse 
org_uuid: string
The organization UUID
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#list.org_uuid)
##### Query ParametersExpand Collapse 
limit: optional number
Maximum results (default: 500, max: 1000)
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#list.limit)
page: optional string
Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#list.page)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#list.x-api-key)
data: array of object { id, created_at, email, 2 more } 
List of current organization members sorted by organization join date ascending
User identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#user_list_response.id)
created_at: string
User account creation timestamp
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#user_list_response.created_at)
email: string
User's current email address
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#user_list_response.email)
full_name: string
User's current full name
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#user_list_response.full_name)
organization_role: "admin" or "billing" or "claude_code_user" or 6 more
User's built-in role within the organization. This is distinct from any custom RBAC roles that may also be assigned.
"admin"
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#user_list_response.organization_role%5B0%5D)
"billing"
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#user_list_response.organization_role%5B1%5D)
"claude_code_user"
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#user_list_response.organization_role%5B2%5D)
"developer"
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#user_list_response.organization_role%5B3%5D)
"managed"
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#user_list_response.organization_role%5B4%5D)
"membership_admin"
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#user_list_response.organization_role%5B5%5D)
"owner"
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#user_list_response.organization_role%5B6%5D)
"primary_owner"
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#user_list_response.organization_role%5B7%5D)
"user"
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#user_list_response.organization_role%5B8%5D)
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#user_list_response.organization_role)
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#list)
has_more: boolean
Whether more records exist beyond the current result set
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#list)
next_page: string
Token to retrieve the next page. Use this as the 'page' parameter in your next request
[](https://platform.claude.com/docs/en/api/compliance/organizations/users/list#list)
List organization users

curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/users \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "data": [
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "email": "email",
      "full_name": "full_name",
      "organization_role": "admin"
  ],
  "has_more": true,
  "next_page": "next_page"

  "data": [
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "email": "email",
      "full_name": "full_name",
      "organization_role": "admin"
  ],
  "has_more": true,
  "next_page": "next_page"
