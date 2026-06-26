<!-- source: https://platform.claude.com/docs/en/api/compliance/groups/members/list -->

# List Compliance Group Members
GET/v1/compliance/groups/{group_id}/members
List Compliance Group Members
##### Path ParametersExpand Collapse 
group_id: string
The group ID (tagged ID, e.g., rbac_group_abc123)
[](https://platform.claude.com/docs/en/api/compliance/groups/members/list#list.group_id)
##### Query ParametersExpand Collapse 
limit: optional number
Maximum results (default: 500, max: 1000)
[](https://platform.claude.com/docs/en/api/compliance/groups/members/list#list.limit)
page: optional string
Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.
[](https://platform.claude.com/docs/en/api/compliance/groups/members/list#list.page)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/groups/members/list#list.x-api-key)
data: array of object { created_at, email, updated_at, user_id } 
List of group members
created_at: string
Membership creation timestamp (ISO 8601)
[](https://platform.claude.com/docs/en/api/compliance/groups/members/list#member_list_response.created_at)
email: string
Member email address
[](https://platform.claude.com/docs/en/api/compliance/groups/members/list#member_list_response.email)
updated_at: string
Membership last-updated timestamp (ISO 8601)
[](https://platform.claude.com/docs/en/api/compliance/groups/members/list#member_list_response.updated_at)
user_id: string
Member user identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/groups/members/list#member_list_response.user_id)
[](https://platform.claude.com/docs/en/api/compliance/groups/members/list#list)
has_more: boolean
Whether more records exist beyond the current result set
[](https://platform.claude.com/docs/en/api/compliance/groups/members/list#list)
next_page: string
Token to retrieve the next page. Use this as the 'page' parameter in your next request
[](https://platform.claude.com/docs/en/api/compliance/groups/members/list#list)
List Compliance Group Members

curl https://api.anthropic.com/v1/compliance/groups/$GROUP_ID/members \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "data": [
      "created_at": "created_at",
      "email": "email",
      "updated_at": "updated_at",
      "user_id": "user_id"
  ],
  "has_more": true,
  "next_page": "next_page"

  "data": [
      "created_at": "created_at",
      "email": "email",
      "updated_at": "updated_at",
      "user_id": "user_id"
  ],
  "has_more": true,
  "next_page": "next_page"
