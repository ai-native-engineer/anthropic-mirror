<!-- source: https://platform.claude.com/docs/en/api/compliance/organizations -->

# Organizations
##### [List organizations](https://platform.claude.com/docs/en/api/compliance/organizations/list)
GET/v1/compliance/organizations
##### ModelsExpand Collapse 
OrganizationListResponse object { data } 
List of organizations under a parent organization.
data: array of object { created_at, name, uuid } 
List of organizations sorted by creation date, ascending
created_at: string
Organization creation time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/organizations#organization_list_response.data.items.created_at)
name: string
Organization name
[](https://platform.claude.com/docs/en/api/compliance/organizations#organization_list_response.data.items.name)
uuid: string
Unique identifier for the organization (UUID format)
[](https://platform.claude.com/docs/en/api/compliance/organizations#organization_list_response.data.items.uuid)
[](https://platform.claude.com/docs/en/api/compliance/organizations#organization_list_response.data)
[](https://platform.claude.com/docs/en/api/compliance/organizations#organization_list_response)
####  OrganizationsUsers
##### [List organization users](https://platform.claude.com/docs/en/api/compliance/organizations/users/list)
GET/v1/compliance/organizations/{org_uuid}/users
##### ModelsExpand Collapse 
UserListResponse object { id, created_at, email, 2 more } 
User member information for compliance responses.
User identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/organizations#user_list_response.id)
created_at: string
User account creation timestamp
[](https://platform.claude.com/docs/en/api/compliance/organizations#user_list_response.created_at)
email: string
User's current email address
[](https://platform.claude.com/docs/en/api/compliance/organizations#user_list_response.email)
full_name: string
User's current full name
[](https://platform.claude.com/docs/en/api/compliance/organizations#user_list_response.full_name)
organization_role: "admin" or "billing" or "claude_code_user" or 6 more
User's built-in role within the organization. This is distinct from any custom RBAC roles that may also be assigned.
"admin"
[](https://platform.claude.com/docs/en/api/compliance/organizations#user_list_response.organization_role%5B0%5D)
"billing"
[](https://platform.claude.com/docs/en/api/compliance/organizations#user_list_response.organization_role%5B1%5D)
"claude_code_user"
[](https://platform.claude.com/docs/en/api/compliance/organizations#user_list_response.organization_role%5B2%5D)
"developer"
[](https://platform.claude.com/docs/en/api/compliance/organizations#user_list_response.organization_role%5B3%5D)
"managed"
[](https://platform.claude.com/docs/en/api/compliance/organizations#user_list_response.organization_role%5B4%5D)
"membership_admin"
[](https://platform.claude.com/docs/en/api/compliance/organizations#user_list_response.organization_role%5B5%5D)
"owner"
[](https://platform.claude.com/docs/en/api/compliance/organizations#user_list_response.organization_role%5B6%5D)
"primary_owner"
[](https://platform.claude.com/docs/en/api/compliance/organizations#user_list_response.organization_role%5B7%5D)
"user"
[](https://platform.claude.com/docs/en/api/compliance/organizations#user_list_response.organization_role%5B8%5D)
[](https://platform.claude.com/docs/en/api/compliance/organizations#user_list_response.organization_role)
[](https://platform.claude.com/docs/en/api/compliance/organizations#user_list_response)
####  OrganizationsRoles
##### [List Compliance Roles](https://platform.claude.com/docs/en/api/compliance/organizations/roles/list)
GET/v1/compliance/organizations/{org_uuid}/roles
##### [Get Compliance Role](https://platform.claude.com/docs/en/api/compliance/organizations/roles/retrieve)
GET/v1/compliance/organizations/{org_uuid}/roles/{role_id}
##### ModelsExpand Collapse 
RoleListResponse object { id, created_at, description, 2 more } 
Role information for compliance responses.
Role identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/organizations#role_list_response.id)
created_at: string
Role creation timestamp (ISO 8601)
[](https://platform.claude.com/docs/en/api/compliance/organizations#role_list_response.created_at)
description: string
Role description
[](https://platform.claude.com/docs/en/api/compliance/organizations#role_list_response.description)
name: string
Role name
[](https://platform.claude.com/docs/en/api/compliance/organizations#role_list_response.name)
updated_at: string
Role last-updated timestamp (ISO 8601)
[](https://platform.claude.com/docs/en/api/compliance/organizations#role_list_response.updated_at)
[](https://platform.claude.com/docs/en/api/compliance/organizations#role_list_response)
RoleRetrieveResponse object { id, created_at, description, 2 more } 
Role information for compliance responses.
Role identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/organizations#role_retrieve_response.id)
created_at: string
Role creation timestamp (ISO 8601)
[](https://platform.claude.com/docs/en/api/compliance/organizations#role_retrieve_response.created_at)
description: string
Role description
[](https://platform.claude.com/docs/en/api/compliance/organizations#role_retrieve_response.description)
name: string
Role name
[](https://platform.claude.com/docs/en/api/compliance/organizations#role_retrieve_response.name)
updated_at: string
Role last-updated timestamp (ISO 8601)
[](https://platform.claude.com/docs/en/api/compliance/organizations#role_retrieve_response.updated_at)
[](https://platform.claude.com/docs/en/api/compliance/organizations#role_retrieve_response)
####  OrganizationsRolesPermissions
##### [List Compliance Role Permissions](https://platform.claude.com/docs/en/api/compliance/organizations/roles/permissions/list)
GET/v1/compliance/organizations/{org_uuid}/roles/{role_id}/permissions
##### ModelsExpand Collapse 
PermissionListResponse object { action, resource_id, resource_type } 
Permission granted by a role.
action: string
Action permitted on the resource
[](https://platform.claude.com/docs/en/api/compliance/organizations#permission_list_response.action)
resource_id: string
Identifier of the resource the permission applies to
[](https://platform.claude.com/docs/en/api/compliance/organizations#permission_list_response.resource_id)
resource_type: string
Type of resource the permission applies to
[](https://platform.claude.com/docs/en/api/compliance/organizations#permission_list_response.resource_type)
[](https://platform.claude.com/docs/en/api/compliance/organizations#permission_list_response)
####  OrganizationsSettings
##### [Get effective organization settings](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve)
GET/v1/compliance/organizations/{organization_id}/settings
##### ModelsExpand Collapse 
SettingRetrieveResponse object { api_keys, organization_id, settings, type } 
The resolved settings in force for one organization at read time.
Settings appear at most once each, in a fixed relative order, and values reflect the enforced state. A setting the organization's administrators cannot change — for example, one controlled by Anthropic policy or not available to the organization — is omitted from the list.
api_keys: array of object { id, created_at, created_by_id, 4 more } 
Compliance API keys configured for the organization hierarchy, ordered by creation time ascending. Key secret values are never included.
Unique identifier for the API key.
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.api_keys.items.id)
created_at: string
When the key was created.
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.api_keys.items.created_at)
created_by_id: string
Identifier of the user who created the key, or null when the key was created by automation or its creator's account no longer exists.
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.api_keys.items.created_by_id)
is_active: boolean
Whether the key is currently active. A deactivated key is listed for audit visibility but cannot authenticate requests.
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.api_keys.items.is_active)
name: string
The name given to the API key when it was created.
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.api_keys.items.name)
scopes: array of string
The permission scopes granted to the key.
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.api_keys.items.scopes)
type: optional "compliance_api_key"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.api_keys.items.type)
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.api_keys)
organization_id: string
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.organization_id)
settings: array of object { name, value, type }  or object { name, value, type }  or object { name, value, type }  or 2 more
Boolean object { name, value, type } 
A setting whose enforced value is a single true/false flag.
name: "api_workbench_feedback_collection_enabled" or "claude_ai_feedback_collection_enabled" or "claude_code_trusted_devices_required" or 9 more
"api_workbench_feedback_collection_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B0%5D.name%5B0%5D)
"claude_ai_feedback_collection_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B0%5D.name%5B1%5D)
"claude_code_trusted_devices_required"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B0%5D.name%5B2%5D)
"code_execution_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B0%5D.name%5B3%5D)
"code_execution_network_egress_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B0%5D.name%5B4%5D)
"content_redaction_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B0%5D.name%5B5%5D)
"directory_sync_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B0%5D.name%5B6%5D)
"frontier_data_use_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B0%5D.name%5B7%5D)
"ip_allowlist_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B0%5D.name%5B8%5D)
"sso_claude_ai_enforced"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B0%5D.name%5B9%5D)
"sso_console_enforced"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B0%5D.name%5B10%5D)
"sso_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B0%5D.name%5B11%5D)
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B0%5D.name)
value: boolean
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B0%5D.value)
type: optional "boolean"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B0%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B0%5D)
Integer object { name, value, type } 
A setting whose enforced value is a whole number; null means no limit is in force.
name: "account_session_duration_seconds"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B1%5D.name)
value: number
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B1%5D.value)
type: optional "integer"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B1%5D)
StringList object { name, value, type } 
A setting whose enforced value is a list of strings.
name: "allowed_invite_domains" or "ip_allowlist_ip_ranges"
"allowed_invite_domains"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B2%5D.name%5B0%5D)
"ip_allowlist_ip_ranges"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B2%5D.name%5B1%5D)
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B2%5D.name)
value: array of string
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B2%5D.value)
type: optional "string_list"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B2%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B2%5D)
ProvisioningMode object { value, name, type } 
How organization members are provisioned, resolved to the enforced mode.
A configured mode is reported only while the mechanism that enforces it is active: just-in-time modes require single sign-on to be enabled, and SCIM modes require directory sync to be enabled. Otherwise `login_only` is reported, regardless of any stored configuration.
value: "jit_advanced" or "jit_permissive" or "login_only" or 2 more
How organization members are provisioned under SSO.
"jit_advanced"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B3%5D.value%5B0%5D)
"jit_permissive"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B3%5D.value%5B1%5D)
"login_only"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B3%5D.value%5B2%5D)
"scim_advanced"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B3%5D.value%5B3%5D)
"scim_permissive"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B3%5D.value%5B4%5D)
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B3%5D.value)
name: optional "sso_provisioning_mode"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B3%5D.name)
type: optional "provisioning_mode"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B3%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B3%5D)
DataRetention object { value, name, type } 
The data retention periods in force, keyed by the type of data they apply to.
A key of `all` covers every data type and is exclusive: when present it is the only key. A missing key means no organization-level administrator-configured retention period is in force for that data type; Anthropic's service defaults may still apply.
value: map[object { duration, timescale, type }  or object { type } ]
Fixed object { duration, timescale, type } 
A fixed retention window measured from each item's last activity.
duration: number
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B4%5D.value.items%5B0%5D.duration)
timescale: "day" or "month"
"day"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B4%5D.value.items%5B0%5D.timescale%5B0%5D)
"month"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B4%5D.value.items%5B0%5D.timescale%5B1%5D)
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B4%5D.value.items%5B0%5D.timescale)
type: optional "fixed"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B4%5D.value.items%5B0%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B4%5D.value.items%5B0%5D)
Indefinite object { type } 
An indefinite retention period: data is kept with no time limit.
type: optional "indefinite"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B4%5D.value.items%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B4%5D.value.items%5B1%5D)
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B4%5D.value)
name: optional "data_retention_periods"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B4%5D.name)
type: optional "data_retention"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B4%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings.items%5B4%5D)
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.settings)
type: optional "effective_organization_settings"
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response.type)
[](https://platform.claude.com/docs/en/api/compliance/organizations#setting_retrieve_response)
