<!-- source: https://platform.claude.com/docs/en/api/compliance/organizations/roles/permissions/list -->

# List Compliance Role Permissions
GET/v1/compliance/organizations/{org_uuid}/roles/{role_id}/permissions
List Compliance Role Permissions
##### Path ParametersExpand Collapse 
org_uuid: string
The organization UUID
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/permissions/list#list.org_uuid)
role_id: string
The role ID (tagged ID, e.g., rbac_role_abc123)
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/permissions/list#list.role_id)
##### Query ParametersExpand Collapse 
limit: optional number
Maximum results (default: 500, max: 1000)
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/permissions/list#list.limit)
page: optional string
Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/permissions/list#list.page)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/permissions/list#list.x-api-key)
data: array of object { action, resource_id, resource_type } 
List of permissions
action: string
Action permitted on the resource
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/permissions/list#permission_list_response.action)
resource_id: string
Identifier of the resource the permission applies to
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/permissions/list#permission_list_response.resource_id)
resource_type: string
Type of resource the permission applies to
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/permissions/list#permission_list_response.resource_type)
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/permissions/list#list)
has_more: boolean
Whether more records exist beyond the current result set
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/permissions/list#list)
next_page: string
Token to retrieve the next page. Use this as the 'page' parameter in your next request
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/permissions/list#list)
List Compliance Role Permissions

curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID/permissions \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "data": [
      "action": "action",
      "resource_id": "resource_id",
      "resource_type": "resource_type"
  ],
  "has_more": true,
  "next_page": "next_page"

  "data": [
      "action": "action",
      "resource_id": "resource_id",
      "resource_type": "resource_type"
  ],
  "has_more": true,
  "next_page": "next_page"
