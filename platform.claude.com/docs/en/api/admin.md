<!-- source: https://platform.claude.com/docs/en/api/admin -->

# Admin
####  AdminOrganizations
##### [Get Current Organization](https://platform.claude.com/docs/en/api/admin/organizations/me)
GET/v1/organizations/me
##### ModelsExpand Collapse 
Organization object { id, name, type } 
ID of the Organization.
[](https://platform.claude.com/docs/en/api/admin#organization.id)
name: string
Name of the Organization.
[](https://platform.claude.com/docs/en/api/admin#organization.name)
type: "organization"
Object type.
For Organizations, this is always `"organization"`.
[](https://platform.claude.com/docs/en/api/admin#organization.type)
[](https://platform.claude.com/docs/en/api/admin#organization)
####  AdminInvites
##### [Create Invite](https://platform.claude.com/docs/en/api/admin/invites/create)
POST/v1/organizations/invites
##### [Get Invite](https://platform.claude.com/docs/en/api/admin/invites/retrieve)
GET/v1/organizations/invites/{invite_id}
##### [List Invites](https://platform.claude.com/docs/en/api/admin/invites/list)
GET/v1/organizations/invites
##### [Delete Invite](https://platform.claude.com/docs/en/api/admin/invites/delete)
DELETE/v1/organizations/invites/{invite_id}
##### ModelsExpand Collapse 
Invite object { id, email, expires_at, 4 more } 
ID of the Invite.
[](https://platform.claude.com/docs/en/api/admin#invite.id)
email: string
Email of the User being invited.
[](https://platform.claude.com/docs/en/api/admin#invite.email)
expires_at: string
RFC 3339 datetime string indicating when the Invite expires.
[](https://platform.claude.com/docs/en/api/admin#invite.expires_at)
invited_at: string
RFC 3339 datetime string indicating when the Invite was created.
[](https://platform.claude.com/docs/en/api/admin#invite.invited_at)
role: "user" or "developer" or "billing" or 2 more
Organization role of the User.
"user"
[](https://platform.claude.com/docs/en/api/admin#invite.role%5B0%5D)
"developer"
[](https://platform.claude.com/docs/en/api/admin#invite.role%5B1%5D)
"billing"
[](https://platform.claude.com/docs/en/api/admin#invite.role%5B2%5D)
"admin"
[](https://platform.claude.com/docs/en/api/admin#invite.role%5B3%5D)
"claude_code_user"
[](https://platform.claude.com/docs/en/api/admin#invite.role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin#invite.role)
status: "accepted" or "expired" or "deleted" or "pending"
Status of the Invite.
"accepted"
[](https://platform.claude.com/docs/en/api/admin#invite.status%5B0%5D)
"expired"
[](https://platform.claude.com/docs/en/api/admin#invite.status%5B1%5D)
"deleted"
[](https://platform.claude.com/docs/en/api/admin#invite.status%5B2%5D)
"pending"
[](https://platform.claude.com/docs/en/api/admin#invite.status%5B3%5D)
[](https://platform.claude.com/docs/en/api/admin#invite.status)
type: "invite"
Object type.
For Invites, this is always `"invite"`.
[](https://platform.claude.com/docs/en/api/admin#invite.type)
[](https://platform.claude.com/docs/en/api/admin#invite)
InviteDeleteResponse object { id, type } 
ID of the Invite.
[](https://platform.claude.com/docs/en/api/admin#invite_delete_response.id)
type: "invite_deleted"
Deleted object type.
For Invites, this is always `"invite_deleted"`.
[](https://platform.claude.com/docs/en/api/admin#invite_delete_response.type)
[](https://platform.claude.com/docs/en/api/admin#invite_delete_response)
####  AdminUsers
##### [Get User](https://platform.claude.com/docs/en/api/admin/users/retrieve)
GET/v1/organizations/users/{user_id}
##### [List Users](https://platform.claude.com/docs/en/api/admin/users/list)
GET/v1/organizations/users
##### [Update User](https://platform.claude.com/docs/en/api/admin/users/update)
POST/v1/organizations/users/{user_id}
##### [Remove User](https://platform.claude.com/docs/en/api/admin/users/delete)
DELETE/v1/organizations/users/{user_id}
##### ModelsExpand Collapse 
User object { id, added_at, email, 3 more } 
ID of the User.
[](https://platform.claude.com/docs/en/api/admin#user.id)
added_at: string
RFC 3339 datetime string indicating when the User joined the Organization.
[](https://platform.claude.com/docs/en/api/admin#user.added_at)
email: string
Email of the User.
[](https://platform.claude.com/docs/en/api/admin#user.email)
name: string
Name of the User.
[](https://platform.claude.com/docs/en/api/admin#user.name)
role: "user" or "developer" or "billing" or 2 more
Organization role of the User.
"user"
[](https://platform.claude.com/docs/en/api/admin#user.role%5B0%5D)
"developer"
[](https://platform.claude.com/docs/en/api/admin#user.role%5B1%5D)
"billing"
[](https://platform.claude.com/docs/en/api/admin#user.role%5B2%5D)
"admin"
[](https://platform.claude.com/docs/en/api/admin#user.role%5B3%5D)
"claude_code_user"
[](https://platform.claude.com/docs/en/api/admin#user.role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin#user.role)
type: "user"
Object type.
For Users, this is always `"user"`.
[](https://platform.claude.com/docs/en/api/admin#user.type)
[](https://platform.claude.com/docs/en/api/admin#user)
UserDeleteResponse object { id, type } 
ID of the User.
[](https://platform.claude.com/docs/en/api/admin#user_delete_response.id)
type: "user_deleted"
Deleted object type.
For Users, this is always `"user_deleted"`.
[](https://platform.claude.com/docs/en/api/admin#user_delete_response.type)
[](https://platform.claude.com/docs/en/api/admin#user_delete_response)
####  AdminWorkspaces
##### [Create Workspace](https://platform.claude.com/docs/en/api/admin/workspaces/create)
POST/v1/organizations/workspaces
##### [Get Workspace](https://platform.claude.com/docs/en/api/admin/workspaces/retrieve)
GET/v1/organizations/workspaces/{workspace_id}
##### [List Workspaces](https://platform.claude.com/docs/en/api/admin/workspaces/list)
GET/v1/organizations/workspaces
##### [Update Workspace](https://platform.claude.com/docs/en/api/admin/workspaces/update)
POST/v1/organizations/workspaces/{workspace_id}
##### [Archive Workspace](https://platform.claude.com/docs/en/api/admin/workspaces/archive)
POST/v1/organizations/workspaces/{workspace_id}/archive
####  AdminWorkspacesMembers
##### [Create Workspace Member](https://platform.claude.com/docs/en/api/admin/workspaces/members/create)
POST/v1/organizations/workspaces/{workspace_id}/members
##### [Get Workspace Member](https://platform.claude.com/docs/en/api/admin/workspaces/members/retrieve)
GET/v1/organizations/workspaces/{workspace_id}/members/{user_id}
##### [List Workspace Members](https://platform.claude.com/docs/en/api/admin/workspaces/members/list)
GET/v1/organizations/workspaces/{workspace_id}/members
##### [Update Workspace Member](https://platform.claude.com/docs/en/api/admin/workspaces/members/update)
POST/v1/organizations/workspaces/{workspace_id}/members/{user_id}
##### [Delete Workspace Member](https://platform.claude.com/docs/en/api/admin/workspaces/members/delete)
DELETE/v1/organizations/workspaces/{workspace_id}/members/{user_id}
##### ModelsExpand Collapse 
WorkspaceMember object { type, user_id, workspace_id, workspace_role } 
type: "workspace_member"
Object type.
For Workspace Members, this is always `"workspace_member"`.
[](https://platform.claude.com/docs/en/api/admin#workspaceMember.type)
user_id: string
ID of the User.
[](https://platform.claude.com/docs/en/api/admin#workspaceMember.user_id)
workspace_id: string
ID of the Workspace.
[](https://platform.claude.com/docs/en/api/admin#workspaceMember.workspace_id)
workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more
Role of the Workspace Member.
"workspace_user"
[](https://platform.claude.com/docs/en/api/admin#workspaceMember.workspace_role%5B0%5D)
"workspace_developer"
[](https://platform.claude.com/docs/en/api/admin#workspaceMember.workspace_role%5B1%5D)
"workspace_restricted_developer"
[](https://platform.claude.com/docs/en/api/admin#workspaceMember.workspace_role%5B2%5D)
"workspace_admin"
[](https://platform.claude.com/docs/en/api/admin#workspaceMember.workspace_role%5B3%5D)
"workspace_billing"
[](https://platform.claude.com/docs/en/api/admin#workspaceMember.workspace_role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin#workspaceMember.workspace_role)
[](https://platform.claude.com/docs/en/api/admin#workspaceMember)
MemberDeleteResponse object { type, user_id, workspace_id } 
type: "workspace_member_deleted"
Deleted object type.
For Workspace Members, this is always `"workspace_member_deleted"`.
[](https://platform.claude.com/docs/en/api/admin#member_delete_response.type)
user_id: string
ID of the User.
[](https://platform.claude.com/docs/en/api/admin#member_delete_response.user_id)
workspace_id: string
ID of the Workspace.
[](https://platform.claude.com/docs/en/api/admin#member_delete_response.workspace_id)
[](https://platform.claude.com/docs/en/api/admin#member_delete_response)
####  AdminWorkspacesRate Limits
##### [List Workspace Rate Limits](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list)
GET/v1/organizations/workspaces/{workspace_id}/rate_limits
##### ModelsExpand Collapse 
RateLimitListResponse object { data, next_page } 
data: array of object { group_type, limits, models, type } 
Rate-limit entries for the workspace, one per group that has at least one override.
group_type: "model_group" or "batch" or "token_count" or 3 more
The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.
"model_group"
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.group_type%5B0%5D)
"batch"
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.group_type%5B1%5D)
"token_count"
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.group_type%5B2%5D)
"files"
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.group_type%5B3%5D)
"skills"
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.group_type%5B4%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.group_type%5B5%5D)
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.group_type)
limits: array of object { org_limit, type, value } 
The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.
org_limit: number
The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.limits.items.org_limit)
type: string
The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.limits.items.type)
value: number
The workspace-level override value for this limiter type.
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.limits.items.value)
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.limits)
models: array of string
Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.models)
type: "workspace_rate_limit"
Object type. Always `workspace_rate_limit` for workspace rate-limit entries.
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.type)
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data)
next_page: string
Token to provide in as `page` in the subsequent request to retrieve the next page of data.
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.next_page)
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response)
####  AdminWorkspacesService Accounts
##### [Create Service Account Workspace Member](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create)
POST/v1/organizations/workspaces/{workspace_id}/service_accounts
##### [Get Service Account Workspace Member](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/retrieve)
GET/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}
##### [List Service Account Workspace Members](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list)
GET/v1/organizations/workspaces/{workspace_id}/service_accounts
##### [Update Service Account Workspace Member](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/update)
POST/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}
##### [Delete Service Account Workspace Member](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/delete)
DELETE/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}
##### ModelsExpand Collapse 
ServiceAccountCreateResponse object { created_by_actor_id, implicit, service_account_id, 3 more } 
created_by_actor_id: string
Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.
[](https://platform.claude.com/docs/en/api/admin#service_account_create_response.created_by_actor_id)
implicit: boolean
True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.
[](https://platform.claude.com/docs/en/api/admin#service_account_create_response.implicit)
service_account_id: string
Tagged service account ID (`svac_...`).
[](https://platform.claude.com/docs/en/api/admin#service_account_create_response.service_account_id)
type: "service_account_workspace_member"
[](https://platform.claude.com/docs/en/api/admin#service_account_create_response.type)
workspace_id: string
Tagged workspace ID (`wrkspc_...`).
[](https://platform.claude.com/docs/en/api/admin#service_account_create_response.workspace_id)
workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more
Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.
"workspace_user"
[](https://platform.claude.com/docs/en/api/admin#service_account_create_response.workspace_role%5B0%5D)
"workspace_developer"
[](https://platform.claude.com/docs/en/api/admin#service_account_create_response.workspace_role%5B1%5D)
"workspace_restricted_developer"
[](https://platform.claude.com/docs/en/api/admin#service_account_create_response.workspace_role%5B2%5D)
"workspace_admin"
[](https://platform.claude.com/docs/en/api/admin#service_account_create_response.workspace_role%5B3%5D)
"workspace_billing"
[](https://platform.claude.com/docs/en/api/admin#service_account_create_response.workspace_role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin#service_account_create_response.workspace_role)
[](https://platform.claude.com/docs/en/api/admin#service_account_create_response)
ServiceAccountRetrieveResponse object { created_by_actor_id, implicit, service_account_id, 3 more } 
created_by_actor_id: string
Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.
[](https://platform.claude.com/docs/en/api/admin#service_account_retrieve_response.created_by_actor_id)
implicit: boolean
True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.
[](https://platform.claude.com/docs/en/api/admin#service_account_retrieve_response.implicit)
service_account_id: string
Tagged service account ID (`svac_...`).
[](https://platform.claude.com/docs/en/api/admin#service_account_retrieve_response.service_account_id)
type: "service_account_workspace_member"
[](https://platform.claude.com/docs/en/api/admin#service_account_retrieve_response.type)
workspace_id: string
Tagged workspace ID (`wrkspc_...`).
[](https://platform.claude.com/docs/en/api/admin#service_account_retrieve_response.workspace_id)
workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more
Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.
"workspace_user"
[](https://platform.claude.com/docs/en/api/admin#service_account_retrieve_response.workspace_role%5B0%5D)
"workspace_developer"
[](https://platform.claude.com/docs/en/api/admin#service_account_retrieve_response.workspace_role%5B1%5D)
"workspace_restricted_developer"
[](https://platform.claude.com/docs/en/api/admin#service_account_retrieve_response.workspace_role%5B2%5D)
"workspace_admin"
[](https://platform.claude.com/docs/en/api/admin#service_account_retrieve_response.workspace_role%5B3%5D)
"workspace_billing"
[](https://platform.claude.com/docs/en/api/admin#service_account_retrieve_response.workspace_role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin#service_account_retrieve_response.workspace_role)
[](https://platform.claude.com/docs/en/api/admin#service_account_retrieve_response)
ServiceAccountListResponse object { created_by_actor_id, implicit, service_account_id, 3 more } 
created_by_actor_id: string
Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.
[](https://platform.claude.com/docs/en/api/admin#service_account_list_response.created_by_actor_id)
implicit: boolean
True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.
[](https://platform.claude.com/docs/en/api/admin#service_account_list_response.implicit)
service_account_id: string
Tagged service account ID (`svac_...`).
[](https://platform.claude.com/docs/en/api/admin#service_account_list_response.service_account_id)
type: "service_account_workspace_member"
[](https://platform.claude.com/docs/en/api/admin#service_account_list_response.type)
workspace_id: string
Tagged workspace ID (`wrkspc_...`).
[](https://platform.claude.com/docs/en/api/admin#service_account_list_response.workspace_id)
workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more
Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.
"workspace_user"
[](https://platform.claude.com/docs/en/api/admin#service_account_list_response.workspace_role%5B0%5D)
"workspace_developer"
[](https://platform.claude.com/docs/en/api/admin#service_account_list_response.workspace_role%5B1%5D)
"workspace_restricted_developer"
[](https://platform.claude.com/docs/en/api/admin#service_account_list_response.workspace_role%5B2%5D)
"workspace_admin"
[](https://platform.claude.com/docs/en/api/admin#service_account_list_response.workspace_role%5B3%5D)
"workspace_billing"
[](https://platform.claude.com/docs/en/api/admin#service_account_list_response.workspace_role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin#service_account_list_response.workspace_role)
[](https://platform.claude.com/docs/en/api/admin#service_account_list_response)
ServiceAccountUpdateResponse object { created_by_actor_id, implicit, service_account_id, 3 more } 
created_by_actor_id: string
Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.
[](https://platform.claude.com/docs/en/api/admin#service_account_update_response.created_by_actor_id)
implicit: boolean
True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.
[](https://platform.claude.com/docs/en/api/admin#service_account_update_response.implicit)
service_account_id: string
Tagged service account ID (`svac_...`).
[](https://platform.claude.com/docs/en/api/admin#service_account_update_response.service_account_id)
type: "service_account_workspace_member"
[](https://platform.claude.com/docs/en/api/admin#service_account_update_response.type)
workspace_id: string
Tagged workspace ID (`wrkspc_...`).
[](https://platform.claude.com/docs/en/api/admin#service_account_update_response.workspace_id)
workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more
Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.
"workspace_user"
[](https://platform.claude.com/docs/en/api/admin#service_account_update_response.workspace_role%5B0%5D)
"workspace_developer"
[](https://platform.claude.com/docs/en/api/admin#service_account_update_response.workspace_role%5B1%5D)
"workspace_restricted_developer"
[](https://platform.claude.com/docs/en/api/admin#service_account_update_response.workspace_role%5B2%5D)
"workspace_admin"
[](https://platform.claude.com/docs/en/api/admin#service_account_update_response.workspace_role%5B3%5D)
"workspace_billing"
[](https://platform.claude.com/docs/en/api/admin#service_account_update_response.workspace_role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin#service_account_update_response.workspace_role)
[](https://platform.claude.com/docs/en/api/admin#service_account_update_response)
ServiceAccountDeleteResponse object { service_account_id, type, workspace_id } 
service_account_id: string
Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.
[](https://platform.claude.com/docs/en/api/admin#service_account_delete_response.service_account_id)
type: "service_account_workspace_member_deleted"
[](https://platform.claude.com/docs/en/api/admin#service_account_delete_response.type)
workspace_id: string
Tagged workspace ID (`wrkspc_...`) named in the delete request.
[](https://platform.claude.com/docs/en/api/admin#service_account_delete_response.workspace_id)
[](https://platform.claude.com/docs/en/api/admin#service_account_delete_response)
####  AdminAPI Keys
##### [Get API Key](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve)
GET/v1/organizations/api_keys/{api_key_id}
##### [List API Keys](https://platform.claude.com/docs/en/api/admin/api_keys/list)
GET/v1/organizations/api_keys
##### [Update API Key](https://platform.claude.com/docs/en/api/admin/api_keys/update)
POST/v1/organizations/api_keys/{api_key_id}
####  AdminExternal Keys
##### [Create External Key](https://platform.claude.com/docs/en/api/admin/external_keys/create)
POST/v1/organizations/external_keys
##### [List External Keys](https://platform.claude.com/docs/en/api/admin/external_keys/list)
GET/v1/organizations/external_keys
##### [Get External Key](https://platform.claude.com/docs/en/api/admin/external_keys/retrieve)
GET/v1/organizations/external_keys/{external_key_id}
##### [Update External Key](https://platform.claude.com/docs/en/api/admin/external_keys/update)
POST/v1/organizations/external_keys/{external_key_id}
##### [Delete External Key](https://platform.claude.com/docs/en/api/admin/external_keys/delete)
DELETE/v1/organizations/external_keys/{external_key_id}
##### [Validate External Key](https://platform.claude.com/docs/en/api/admin/external_keys/validate)
POST/v1/organizations/external_keys/{external_key_id}/validate
##### ModelsExpand Collapse 
ExternalKeyCreateResponse object { id, created_at, display_name, 4 more } 
CMEK external key config belonging to the caller's organization.
Configs are organization-scoped. Workspaces attach to a config; once any workspace references it, the provider fields become effectively immutable (existing encrypted data needs the config for decrypt).
Tagged ID of the external key config.
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.id)
created_at: string
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.created_at)
display_name: string
Human-friendly display name.
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.display_name)
geo: string
Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.geo)
provider_config: object { kms_arn, role_arn, type, region }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more } 
KMS provider identity and auth coordinates.
Aws object { kms_arn, role_arn, type, region } 
kms_arn: string
Full ARN of the AWS KMS key.
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.provider_config%5B0%5D.kms_arn)
role_arn: string
IAM role ARN that Anthropic assumes to access the KMS key.
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.provider_config%5B0%5D.role_arn)
type: "aws"
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.provider_config%5B0%5D.type)
region: optional string
AWS region. Derived from kms_arn if omitted.
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.provider_config%5B0%5D.region)
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.provider_config%5B0%5D)
Gcp object { key_name, type } 
key_name: string
Full resource name of the Cloud KMS key.
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.provider_config%5B1%5D.key_name)
type: "gcp"
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.provider_config%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.provider_config%5B1%5D)
Azure object { key_name, tenant_id, type, 2 more } 
key_name: string
Name of the key within the vault.
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.provider_config%5B2%5D.key_name)
tenant_id: string
Azure AD tenant ID.
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.provider_config%5B2%5D.tenant_id)
type: "azure"
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.provider_config%5B2%5D.type)
vault_uri: string
Key Vault URI.
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.provider_config%5B2%5D.vault_uri)
client_id: optional string
Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.provider_config%5B2%5D.client_id)
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.provider_config%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.provider_config)
type: "external_key"
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.type)
updated_at: string
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response.updated_at)
[](https://platform.claude.com/docs/en/api/admin#external_key_create_response)
ExternalKeyListResponse object { id, created_at, display_name, 4 more } 
CMEK external key config belonging to the caller's organization.
Configs are organization-scoped. Workspaces attach to a config; once any workspace references it, the provider fields become effectively immutable (existing encrypted data needs the config for decrypt).
Tagged ID of the external key config.
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.id)
created_at: string
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.created_at)
display_name: string
Human-friendly display name.
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.display_name)
geo: string
Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.geo)
provider_config: object { kms_arn, role_arn, type, region }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more } 
KMS provider identity and auth coordinates.
Aws object { kms_arn, role_arn, type, region } 
kms_arn: string
Full ARN of the AWS KMS key.
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.provider_config%5B0%5D.kms_arn)
role_arn: string
IAM role ARN that Anthropic assumes to access the KMS key.
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.provider_config%5B0%5D.role_arn)
type: "aws"
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.provider_config%5B0%5D.type)
region: optional string
AWS region. Derived from kms_arn if omitted.
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.provider_config%5B0%5D.region)
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.provider_config%5B0%5D)
Gcp object { key_name, type } 
key_name: string
Full resource name of the Cloud KMS key.
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.provider_config%5B1%5D.key_name)
type: "gcp"
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.provider_config%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.provider_config%5B1%5D)
Azure object { key_name, tenant_id, type, 2 more } 
key_name: string
Name of the key within the vault.
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.provider_config%5B2%5D.key_name)
tenant_id: string
Azure AD tenant ID.
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.provider_config%5B2%5D.tenant_id)
type: "azure"
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.provider_config%5B2%5D.type)
vault_uri: string
Key Vault URI.
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.provider_config%5B2%5D.vault_uri)
client_id: optional string
Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.provider_config%5B2%5D.client_id)
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.provider_config%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.provider_config)
type: "external_key"
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.type)
updated_at: string
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response.updated_at)
[](https://platform.claude.com/docs/en/api/admin#external_key_list_response)
ExternalKeyRetrieveResponse object { id, created_at, display_name, 4 more } 
CMEK external key config belonging to the caller's organization.
Configs are organization-scoped. Workspaces attach to a config; once any workspace references it, the provider fields become effectively immutable (existing encrypted data needs the config for decrypt).
Tagged ID of the external key config.
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.id)
created_at: string
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.created_at)
display_name: string
Human-friendly display name.
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.display_name)
geo: string
Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.geo)
provider_config: object { kms_arn, role_arn, type, region }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more } 
KMS provider identity and auth coordinates.
Aws object { kms_arn, role_arn, type, region } 
kms_arn: string
Full ARN of the AWS KMS key.
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.provider_config%5B0%5D.kms_arn)
role_arn: string
IAM role ARN that Anthropic assumes to access the KMS key.
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.provider_config%5B0%5D.role_arn)
type: "aws"
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.provider_config%5B0%5D.type)
region: optional string
AWS region. Derived from kms_arn if omitted.
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.provider_config%5B0%5D.region)
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.provider_config%5B0%5D)
Gcp object { key_name, type } 
key_name: string
Full resource name of the Cloud KMS key.
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.provider_config%5B1%5D.key_name)
type: "gcp"
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.provider_config%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.provider_config%5B1%5D)
Azure object { key_name, tenant_id, type, 2 more } 
key_name: string
Name of the key within the vault.
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.provider_config%5B2%5D.key_name)
tenant_id: string
Azure AD tenant ID.
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.provider_config%5B2%5D.tenant_id)
type: "azure"
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.provider_config%5B2%5D.type)
vault_uri: string
Key Vault URI.
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.provider_config%5B2%5D.vault_uri)
client_id: optional string
Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.provider_config%5B2%5D.client_id)
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.provider_config%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.provider_config)
type: "external_key"
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.type)
updated_at: string
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response.updated_at)
[](https://platform.claude.com/docs/en/api/admin#external_key_retrieve_response)
ExternalKeyUpdateResponse object { id, created_at, display_name, 4 more } 
CMEK external key config belonging to the caller's organization.
Configs are organization-scoped. Workspaces attach to a config; once any workspace references it, the provider fields become effectively immutable (existing encrypted data needs the config for decrypt).
Tagged ID of the external key config.
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.id)
created_at: string
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.created_at)
display_name: string
Human-friendly display name.
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.display_name)
geo: string
Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.geo)
provider_config: object { kms_arn, role_arn, type, region }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more } 
KMS provider identity and auth coordinates.
Aws object { kms_arn, role_arn, type, region } 
kms_arn: string
Full ARN of the AWS KMS key.
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.provider_config%5B0%5D.kms_arn)
role_arn: string
IAM role ARN that Anthropic assumes to access the KMS key.
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.provider_config%5B0%5D.role_arn)
type: "aws"
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.provider_config%5B0%5D.type)
region: optional string
AWS region. Derived from kms_arn if omitted.
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.provider_config%5B0%5D.region)
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.provider_config%5B0%5D)
Gcp object { key_name, type } 
key_name: string
Full resource name of the Cloud KMS key.
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.provider_config%5B1%5D.key_name)
type: "gcp"
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.provider_config%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.provider_config%5B1%5D)
Azure object { key_name, tenant_id, type, 2 more } 
key_name: string
Name of the key within the vault.
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.provider_config%5B2%5D.key_name)
tenant_id: string
Azure AD tenant ID.
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.provider_config%5B2%5D.tenant_id)
type: "azure"
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.provider_config%5B2%5D.type)
vault_uri: string
Key Vault URI.
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.provider_config%5B2%5D.vault_uri)
client_id: optional string
Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.provider_config%5B2%5D.client_id)
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.provider_config%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.provider_config)
type: "external_key"
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.type)
updated_at: string
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response.updated_at)
[](https://platform.claude.com/docs/en/api/admin#external_key_update_response)
ExternalKeyDeleteResponse object { id, type } 
ID of the deleted External Key.
[](https://platform.claude.com/docs/en/api/admin#external_key_delete_response.id)
type: "external_key_deleted"
[](https://platform.claude.com/docs/en/api/admin#external_key_delete_response.type)
[](https://platform.claude.com/docs/en/api/admin#external_key_delete_response)
ExternalKeyValidateResponse object { error, status, type } 
Result of a validation roundtrip against the customer's KMS.
HTTP 200 for both outcomes — the operation completed; `status` says whether the key works.
error: string
Error message when status is `failure`. Null otherwise.
[](https://platform.claude.com/docs/en/api/admin#external_key_validate_response.error)
status: "success" or "failure"
`success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.
"success"
[](https://platform.claude.com/docs/en/api/admin#external_key_validate_response.status%5B0%5D)
"failure"
[](https://platform.claude.com/docs/en/api/admin#external_key_validate_response.status%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#external_key_validate_response.status)
type: "external_key_validation"
[](https://platform.claude.com/docs/en/api/admin#external_key_validate_response.type)
[](https://platform.claude.com/docs/en/api/admin#external_key_validate_response)
####  AdminUsage Report
##### [Get Messages Usage Report](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages)
GET/v1/organizations/usage_report/messages
##### [Get Claude Code Usage Report](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code)
GET/v1/organizations/usage_report/claude_code
##### ModelsExpand Collapse 
ClaudeCodeUsageReport object { data, has_more, next_page } 
data: array of object { actor, core_metrics, customer_type, 6 more } 
List of Claude Code usage records for the requested date.
actor: object { email_address, type }  or object { api_key_name, type } 
The user or API key that performed the Claude Code actions.
UserActor object { email_address, type } 
email_address: string
Email address of the user who performed Claude Code actions.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.actor%5B0%5D.email_address)
type: "user_actor"
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.actor%5B0%5D.type)
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.actor%5B0%5D)
APIActor object { api_key_name, type } 
api_key_name: string
Name of the API key used to perform Claude Code actions.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.actor%5B1%5D.api_key_name)
type: "api_actor"
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.actor%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.actor%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.actor)
core_metrics: object { commits_by_claude_code, lines_of_code, num_sessions, pull_requests_by_claude_code } 
Core productivity metrics measuring Claude Code usage and impact.
commits_by_claude_code: number
Number of git commits created through Claude Code's commit functionality.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.core_metrics.commits_by_claude_code)
lines_of_code: object { added, removed } 
Statistics on code changes made through Claude Code.
added: number
Total number of lines of code added across all files by Claude Code.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.core_metrics.lines_of_code.added)
removed: number
Total number of lines of code removed across all files by Claude Code.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.core_metrics.lines_of_code.removed)
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.core_metrics.lines_of_code)
num_sessions: number
Number of distinct Claude Code sessions initiated by this actor.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.core_metrics.num_sessions)
pull_requests_by_claude_code: number
Number of pull requests created through Claude Code's PR functionality.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.core_metrics.pull_requests_by_claude_code)
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.core_metrics)
customer_type: "api" or "subscription"
Type of customer account (api for API customers, subscription for Pro/Team customers).
"api"
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.customer_type%5B0%5D)
"subscription"
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.customer_type%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.customer_type)
date: string
UTC date for the usage metrics in YYYY-MM-DD format.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.date)
model_breakdown: array of object { estimated_cost, model, tokens } 
Token usage and cost breakdown by AI model used.
estimated_cost: object { amount, currency } 
Estimated cost for using this model
amount: number
Estimated cost amount in minor currency units (e.g., cents for USD).
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.model_breakdown.items.estimated_cost.amount)
currency: string
Currency code for the estimated cost (e.g., 'USD').
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.model_breakdown.items.estimated_cost.currency)
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.model_breakdown.items.estimated_cost)
model: string
Name of the AI model used for Claude Code interactions.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.model_breakdown.items.model)
tokens: object { cache_creation, cache_read, input, output } 
Token usage breakdown for this model
cache_creation: number
Number of cache creation tokens consumed by this model.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.model_breakdown.items.tokens.cache_creation)
cache_read: number
Number of cache read tokens consumed by this model.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.model_breakdown.items.tokens.cache_read)
input: number
Number of input tokens consumed by this model.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.model_breakdown.items.tokens.input)
output: number
Number of output tokens generated by this model.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.model_breakdown.items.tokens.output)
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.model_breakdown.items.tokens)
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.model_breakdown)
organization_id: string
ID of the organization that owns the Claude Code usage.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.organization_id)
terminal_type: string
Type of terminal or environment where Claude Code was used.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.terminal_type)
tool_actions: map[object { accepted, rejected } ]
Breakdown of tool action acceptance and rejection rates by tool type.
accepted: number
Number of tool action proposals that the user accepted.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.tool_actions.items.accepted)
rejected: number
Number of tool action proposals that the user rejected.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.tool_actions.items.rejected)
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.tool_actions)
subscription_type: optional "enterprise" or "team"
Subscription tier for subscription customers. `null` for API customers.
"enterprise"
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.subscription_type%5B0%5D)
"team"
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.subscription_type%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data.items.subscription_type)
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.data)
has_more: boolean
True if there are more records available beyond the current page.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.has_more)
next_page: string
Opaque cursor token for fetching the next page of results, or null if no more pages are available.
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report.next_page)
[](https://platform.claude.com/docs/en/api/admin#claude_code_usage_report)
MessagesUsageReport object { data, has_more, next_page } 
data: array of object { ending_at, results, starting_at } 
ending_at: string
End of the time bucket (exclusive) in RFC 3339 format.
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.ending_at)
results: array of object { account_id, api_key_id, cache_creation, 10 more } 
List of usage items for this time bucket. There may be multiple items if one or more `group_by[]` parameters are specified.
account_id: string
ID of the user account that made the request. `null` if not grouping by account or for non-OAuth requests.
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.account_id)
api_key_id: string
ID of the API key used. `null` if not grouping by API key or for usage in the Anthropic Console.
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.api_key_id)
cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
The number of input tokens for cache creation.
ephemeral_1h_input_tokens: number
The number of input tokens used to create the 1 hour cache entry.
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.cache_creation.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: number
The number of input tokens used to create the 5 minute cache entry.
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.cache_creation.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.cache_creation)
cache_read_input_tokens: number
The number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.cache_read_input_tokens)
context_window: "0-200k" or "200k-1M"
Context window used. `null` if not grouping by context window.
"0-200k"
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.context_window%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.context_window%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.context_window)
inference_geo: string
Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`. For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.inference_geo)
model: string
Model used. `null` if not grouping by model.
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.model)
output_tokens: number
The number of output tokens generated.
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.output_tokens)
server_tool_use: object { web_search_requests } 
Server-side tool usage metrics.
web_search_requests: number
The number of web search requests made.
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.server_tool_use.web_search_requests)
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.server_tool_use)
service_account_id: string
ID of the service account that made the request. `null` if not grouping by service account or for non-OIDC-federation requests.
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.service_account_id)
service_tier: "standard" or "batch" or "priority" or 3 more
Service tier used. `null` if not grouping by service tier.
"standard"
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.service_tier%5B0%5D)
"batch"
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.service_tier%5B1%5D)
"priority"
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.service_tier%5B2%5D)
"priority_on_demand"
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.service_tier%5B3%5D)
"flex"
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.service_tier%5B4%5D)
"flex_discount"
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.service_tier%5B5%5D)
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.service_tier)
uncached_input_tokens: number
The number of uncached input tokens processed.
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.uncached_input_tokens)
workspace_id: string
ID of the Workspace used. `null` if not grouping by workspace or for the default workspace.
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results.items.workspace_id)
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.results)
starting_at: string
Start of the time bucket (inclusive) in RFC 3339 format.
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data.items.starting_at)
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.data)
has_more: boolean
Indicates if there are more results.
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.has_more)
next_page: string
Token to provide in as `page` in the subsequent request to retrieve the next page of data.
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report.next_page)
[](https://platform.claude.com/docs/en/api/admin#messages_usage_report)
####  AdminCost Report
##### [Get Cost Report](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve)
GET/v1/organizations/cost_report
##### ModelsExpand Collapse 
CostReport object { data, has_more, next_page } 
data: array of object { ending_at, results, starting_at } 
ending_at: string
End of the time bucket (exclusive) in RFC 3339 format.
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.ending_at)
results: array of object { amount, context_window, cost_type, 7 more } 
List of cost items for this time bucket. There may be multiple items if one or more `group_by[]` parameters are specified.
amount: string
Cost amount in lowest currency units (e.g. cents) as a decimal string. For example, `"123.45"` in `"USD"` represents `$1.23`.
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.amount)
context_window: "0-200k" or "200k-1M"
Input context window used. `null` if not grouping by description or for non-token costs.
"0-200k"
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.context_window%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.context_window%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.context_window)
cost_type: "tokens" or "web_search" or "code_execution" or "session_usage"
Type of cost. `null` if not grouping by description.
"tokens"
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.cost_type%5B0%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.cost_type%5B1%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.cost_type%5B2%5D)
"session_usage"
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.cost_type%5B3%5D)
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.cost_type)
currency: string
Currency code for the cost amount. Currently always `"USD"`.
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.currency)
description: string
Description of the cost item. `null` if not grouping by description.
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.description)
inference_geo: string
Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`. For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.inference_geo)
model: string
Model name used. `null` if not grouping by description or for non-token costs.
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.model)
service_tier: "standard" or "batch"
Service tier used. `null` if not grouping by description or for non-token costs.
"standard"
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.service_tier%5B0%5D)
"batch"
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.service_tier%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.service_tier)
token_type: "uncached_input_tokens" or "output_tokens" or "cache_read_input_tokens" or 2 more
Type of token. `null` if not grouping by description or for non-token costs.
"uncached_input_tokens"
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.token_type%5B0%5D)
"output_tokens"
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.token_type%5B1%5D)
"cache_read_input_tokens"
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.token_type%5B2%5D)
"cache_creation.ephemeral_1h_input_tokens"
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.token_type%5B3%5D)
"cache_creation.ephemeral_5m_input_tokens"
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.token_type%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.token_type)
workspace_id: string
ID of the Workspace this cost is associated with. `null` if not grouping by workspace or for the default workspace.
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results.items.workspace_id)
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.results)
starting_at: string
Start of the time bucket (inclusive) in RFC 3339 format.
[](https://platform.claude.com/docs/en/api/admin#cost_report.data.items.starting_at)
[](https://platform.claude.com/docs/en/api/admin#cost_report.data)
has_more: boolean
Indicates if there are more results.
[](https://platform.claude.com/docs/en/api/admin#cost_report.has_more)
next_page: string
Token to provide in as `page` in the subsequent request to retrieve the next page of data.
[](https://platform.claude.com/docs/en/api/admin#cost_report.next_page)
[](https://platform.claude.com/docs/en/api/admin#cost_report)
####  AdminAnalytics
##### [Get Activity Summaries](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries)
GET/v1/organizations/analytics/summaries
##### ModelsExpand Collapse 
ActivitySummary object { summaries } 
Response for GET /v1/organizations/analytics/summaries.
summaries: array of object { assigned_seat_count, cowork_daily_active_user_count, cowork_monthly_active_user_count, 10 more } 
assigned_seat_count: number
Number of seats currently assigned to members
[](https://platform.claude.com/docs/en/api/admin#activity_summary.summaries.items.assigned_seat_count)
cowork_daily_active_user_count: number
Number of users with Cowork activity on the requested day
[](https://platform.claude.com/docs/en/api/admin#activity_summary.summaries.items.cowork_daily_active_user_count)
cowork_monthly_active_user_count: number
Number of users with Cowork activity in the 30-day rolling window
[](https://platform.claude.com/docs/en/api/admin#activity_summary.summaries.items.cowork_monthly_active_user_count)
cowork_weekly_active_user_count: number
Number of users with Cowork activity in the 7-day rolling window
[](https://platform.claude.com/docs/en/api/admin#activity_summary.summaries.items.cowork_weekly_active_user_count)
daily_active_user_count: number
Number of users with token consumption on the requested day
[](https://platform.claude.com/docs/en/api/admin#activity_summary.summaries.items.daily_active_user_count)
daily_adoption_rate: number
Percentage of assigned seats with activity on the requested day (DAU / assigned_seat_count * 100)
[](https://platform.claude.com/docs/en/api/admin#activity_summary.summaries.items.daily_adoption_rate)
ending_at: string
End time in UTC of aggregation period (e.g. 2026-01-16T00:00
)
[](https://platform.claude.com/docs/en/api/admin#activity_summary.summaries.items.ending_at)
monthly_active_user_count: number
Number of users with token consumption in the 30-day rolling window
[](https://platform.claude.com/docs/en/api/admin#activity_summary.summaries.items.monthly_active_user_count)
monthly_adoption_rate: number
Percentage of assigned seats with activity in the 30-day rolling window (MAU / assigned_seat_count * 100)
[](https://platform.claude.com/docs/en/api/admin#activity_summary.summaries.items.monthly_adoption_rate)
pending_invite_count: number
Number of pending invitations to join the organization
[](https://platform.claude.com/docs/en/api/admin#activity_summary.summaries.items.pending_invite_count)
starting_at: string
Start time in UTC of aggregation period (e.g. 2026-01-15T00:00
)
[](https://platform.claude.com/docs/en/api/admin#activity_summary.summaries.items.starting_at)
weekly_active_user_count: number
Number of users with token consumption in the 7-day rolling window
[](https://platform.claude.com/docs/en/api/admin#activity_summary.summaries.items.weekly_active_user_count)
weekly_adoption_rate: number
Percentage of assigned seats with activity in the 7-day rolling window (WAU / assigned_seat_count * 100)
[](https://platform.claude.com/docs/en/api/admin#activity_summary.summaries.items.weekly_adoption_rate)
[](https://platform.claude.com/docs/en/api/admin#activity_summary.summaries)
[](https://platform.claude.com/docs/en/api/admin#activity_summary)
AnalyticsUser object { id, email_address } 
User identifier.
Tagged user identifier (e.g. user_...)
[](https://platform.claude.com/docs/en/api/admin#analytics_user.id)
email_address: string
Email address of the user
[](https://platform.claude.com/docs/en/api/admin#analytics_user.email_address)
[](https://platform.claude.com/docs/en/api/admin#analytics_user)
AnalyticsUserActor object { user_id, deleted, email, 2 more } 
user_id: string
Tagged user ID.
[](https://platform.claude.com/docs/en/api/admin#analytics_user_actor.user_id)
deleted: optional boolean
True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.
[](https://platform.claude.com/docs/en/api/admin#analytics_user_actor.deleted)
email: optional string
The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).
[](https://platform.claude.com/docs/en/api/admin#analytics_user_actor.email)
name: optional string
The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.
[](https://platform.claude.com/docs/en/api/admin#analytics_user_actor.name)
type: optional "user_actor"
[](https://platform.claude.com/docs/en/api/admin#analytics_user_actor.type)
[](https://platform.claude.com/docs/en/api/admin#analytics_user_actor)
ConnectorOfficeProductMetrics object { distinct_session_connector_used_count } 
Office Agent activity metrics for a single connector on a given day within one Office product.
distinct_session_connector_used_count: number
Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#connector_office_product_metrics.distinct_session_connector_used_count)
[](https://platform.claude.com/docs/en/api/admin#connector_office_product_metrics)
OfficeProductMetrics object { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more } 
Office Agent activity metrics for a single user on a given day within one Office product.
connectors_used_count: number
Number of MCP connector invocations
[](https://platform.claude.com/docs/en/api/admin#office_product_metrics.connectors_used_count)
distinct_connectors_used_count: number
Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#office_product_metrics.distinct_connectors_used_count)
distinct_session_count: number
Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#office_product_metrics.distinct_session_count)
distinct_skills_used_count: number
Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#office_product_metrics.distinct_skills_used_count)
message_count: number
Number of messages sent
[](https://platform.claude.com/docs/en/api/admin#office_product_metrics.message_count)
skills_used_count: number
Number of skill invocations
[](https://platform.claude.com/docs/en/api/admin#office_product_metrics.skills_used_count)
[](https://platform.claude.com/docs/en/api/admin#office_product_metrics)
SkillOfficeProductMetrics object { distinct_session_skill_used_count } 
Office Agent activity metrics for a single skill on a given day within one Office product.
distinct_session_skill_used_count: number
Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#skill_office_product_metrics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin#skill_office_product_metrics)
ToolActionCounts object { accepted_count, rejected_count } 
Accepted/rejected counts for a single Claude Code tool type.
accepted_count: number
Number of tool proposals accepted
[](https://platform.claude.com/docs/en/api/admin#tool_action_counts.accepted_count)
rejected_count: number
Number of tool proposals rejected
[](https://platform.claude.com/docs/en/api/admin#tool_action_counts.rejected_count)
[](https://platform.claude.com/docs/en/api/admin#tool_action_counts)
####  AdminAnalyticsUsage
##### [Get Token Usage Over Time](https://platform.claude.com/docs/en/api/admin/analytics/usage/list)
GET/v1/organizations/analytics/usage_report
##### [Get Per-User Token Usage](https://platform.claude.com/docs/en/api/admin/analytics/usage/list_by_user)
GET/v1/organizations/analytics/user_usage_report
##### ModelsExpand Collapse 
UsageBucket object { data, data_refreshed_at, has_more, 2 more } 
data: array of object { ending_at, results, starting_at } 
ending_at: string
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.ending_at)
results: array of object { cache_creation, cache_read_input_tokens, context_window, 8 more } 
cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
ephemeral_1h_input_tokens: number
The number of input tokens used to create the 1 hour cache entry.
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.cache_creation.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: number
The number of input tokens used to create the 5 minute cache entry.
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.cache_creation.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.cache_creation)
cache_read_input_tokens: number
The number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.cache_read_input_tokens)
context_window: "0-200k" or "200k-1M"
"0-200k"
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.context_window%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.context_window%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.context_window)
inference_geo: "global" or "us"
"global"
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.inference_geo%5B0%5D)
"us"
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.inference_geo%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.inference_geo)
model: string
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.model)
output_tokens: number
The number of output tokens generated.
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.output_tokens)
product: string
Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.product)
requests: number
Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.requests)
server_tool_use: object { web_search_requests } 
web_search_requests: number
The number of web search requests made.
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.server_tool_use.web_search_requests)
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.server_tool_use)
speed: "fast" or "standard"
"fast"
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.speed%5B0%5D)
"standard"
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.speed)
uncached_input_tokens: number
The number of uncached input tokens processed.
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results.items.uncached_input_tokens)
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.results)
starting_at: string
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data.items.starting_at)
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data)
data_refreshed_at: string
RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.data_refreshed_at)
has_more: boolean
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.has_more)
next_page: string
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.next_page)
organization_id: string
ID of the Organization.
[](https://platform.claude.com/docs/en/api/admin#usage_bucket.organization_id)
[](https://platform.claude.com/docs/en/api/admin#usage_bucket)
UserUsage object { data, data_refreshed_at, has_more, 2 more } 
data: array of object { actor, cache_creation, cache_read_input_tokens, 12 more } 
actor: [AnalyticsUserActor](https://platform.claude.com/docs/en/api/admin#analytics_user_actor) { user_id, deleted, email, 2 more } 
user_id: string
Tagged user ID.
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.actor%20%2B%20\(resource\)%20admin.analytics.user_id)
deleted: optional boolean
True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.actor%20%2B%20\(resource\)%20admin.analytics.deleted)
email: optional string
The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.actor%20%2B%20\(resource\)%20admin.analytics.email)
name: optional string
The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.actor%20%2B%20\(resource\)%20admin.analytics.name)
type: optional "user_actor"
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.actor%20%2B%20\(resource\)%20admin.analytics.type)
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.actor)
cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
ephemeral_1h_input_tokens: number
The number of input tokens used to create the 1 hour cache entry.
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.cache_creation.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: number
The number of input tokens used to create the 5 minute cache entry.
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.cache_creation.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.cache_creation)
cache_read_input_tokens: number
The number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.cache_read_input_tokens)
context_window: "0-200k" or "200k-1M"
"0-200k"
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.context_window%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.context_window%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.context_window)
ending_at: string
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.ending_at)
inference_geo: "global" or "us"
"global"
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.inference_geo%5B0%5D)
"us"
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.inference_geo%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.inference_geo)
model: string
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.model)
output_tokens: number
The number of output tokens generated.
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.output_tokens)
product: string
Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.product)
requests: number
Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.requests)
server_tool_use: object { web_search_requests } 
web_search_requests: number
The number of web search requests made.
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.server_tool_use.web_search_requests)
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.server_tool_use)
speed: "fast" or "standard"
"fast"
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.speed%5B0%5D)
"standard"
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.speed)
starting_at: string
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.starting_at)
total_tokens: number
Total token count across all token types. This is the value the default order_by='total_tokens' sorts on.
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.total_tokens)
uncached_input_tokens: number
The number of uncached input tokens processed.
[](https://platform.claude.com/docs/en/api/admin#user_usage.data.items.uncached_input_tokens)
[](https://platform.claude.com/docs/en/api/admin#user_usage.data)
data_refreshed_at: string
RFC 3339 timestamp of the export this response was served from. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).
[](https://platform.claude.com/docs/en/api/admin#user_usage.data_refreshed_at)
has_more: boolean
[](https://platform.claude.com/docs/en/api/admin#user_usage.has_more)
next_page: string
[](https://platform.claude.com/docs/en/api/admin#user_usage.next_page)
organization_id: string
ID of the Organization.
[](https://platform.claude.com/docs/en/api/admin#user_usage.organization_id)
[](https://platform.claude.com/docs/en/api/admin#user_usage)
####  AdminAnalyticsCost
##### [Get Cost Over Time](https://platform.claude.com/docs/en/api/admin/analytics/cost/list)
GET/v1/organizations/analytics/cost_report
##### [Get Per-User Cost](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user)
GET/v1/organizations/analytics/user_cost_report
##### ModelsExpand Collapse 
CostBucket object { data, data_refreshed_at, has_more, 2 more } 
data: array of object { ending_at, results, starting_at } 
ending_at: string
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.ending_at)
results: array of object { amount, context_window, cost_type, 8 more } 
amount: string
Amount (post-discount, pre-credit) in fractional cents.
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.amount)
context_window: "0-200k" or "200k-1M"
"0-200k"
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.context_window%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.context_window%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.context_window)
cost_type: "tokens" or "web_search" or "code_execution"
Cost component when `group_by[]=cost_type`; null otherwise (amount is the combined total).
"tokens"
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.cost_type%5B0%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.cost_type%5B1%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.cost_type%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.cost_type)
currency: "USD"
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.currency)
inference_geo: "global" or "us"
"global"
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.inference_geo%5B0%5D)
"us"
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.inference_geo%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.inference_geo)
list_amount: string
List-price amount (pre-discount) in fractional cents.
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.list_amount)
model: string
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.model)
product: string
Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.product)
requests: number
Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.requests)
speed: "fast" or "standard"
"fast"
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.speed%5B0%5D)
"standard"
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.speed)
token_type: "uncached_input_tokens" or "output_tokens" or "cache_read_input_tokens" or 2 more
Token type when `group_by[]=token_type` and `cost_type=tokens`; null otherwise.
"uncached_input_tokens"
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.token_type%5B0%5D)
"output_tokens"
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.token_type%5B1%5D)
"cache_read_input_tokens"
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.token_type%5B2%5D)
"cache_creation.ephemeral_1h_input_tokens"
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.token_type%5B3%5D)
"cache_creation.ephemeral_5m_input_tokens"
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.token_type%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results.items.token_type)
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.results)
starting_at: string
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data.items.starting_at)
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data)
data_refreshed_at: string
RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.data_refreshed_at)
has_more: boolean
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.has_more)
next_page: string
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.next_page)
organization_id: string
ID of the Organization.
[](https://platform.claude.com/docs/en/api/admin#cost_bucket.organization_id)
[](https://platform.claude.com/docs/en/api/admin#cost_bucket)
UserCost object { data, data_refreshed_at, has_more, 2 more } 
data: array of object { actor, amount, context_window, 11 more } 
actor: [AnalyticsUserActor](https://platform.claude.com/docs/en/api/admin#analytics_user_actor) { user_id, deleted, email, 2 more } 
user_id: string
Tagged user ID.
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.actor%20%2B%20\(resource\)%20admin.analytics.user_id)
deleted: optional boolean
True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.actor%20%2B%20\(resource\)%20admin.analytics.deleted)
email: optional string
The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.actor%20%2B%20\(resource\)%20admin.analytics.email)
name: optional string
The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.actor%20%2B%20\(resource\)%20admin.analytics.name)
type: optional "user_actor"
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.actor%20%2B%20\(resource\)%20admin.analytics.type)
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.actor)
amount: string
Amount (post-discount, pre-credit) in fractional cents (minor units).
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.amount)
context_window: "0-200k" or "200k-1M"
"0-200k"
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.context_window%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.context_window%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.context_window)
cost_type: "tokens" or "web_search" or "code_execution"
Cost component breakdown; null when returning the combined total.
"tokens"
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.cost_type%5B0%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.cost_type%5B1%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.cost_type%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.cost_type)
currency: "USD"
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.currency)
ending_at: string
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.ending_at)
inference_geo: "global" or "us"
"global"
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.inference_geo%5B0%5D)
"us"
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.inference_geo%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.inference_geo)
list_amount: string
List-price amount (pre-discount) in fractional cents.
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.list_amount)
model: string
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.model)
product: string
Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.product)
requests: number
Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.requests)
speed: "fast" or "standard"
"fast"
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.speed%5B0%5D)
"standard"
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.speed)
starting_at: string
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.starting_at)
token_type: "uncached_input_tokens" or "output_tokens" or "cache_read_input_tokens" or 2 more
Token type when cost_type=tokens; null otherwise.
"uncached_input_tokens"
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.token_type%5B0%5D)
"output_tokens"
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.token_type%5B1%5D)
"cache_read_input_tokens"
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.token_type%5B2%5D)
"cache_creation.ephemeral_1h_input_tokens"
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.token_type%5B3%5D)
"cache_creation.ephemeral_5m_input_tokens"
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.token_type%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin#user_cost.data.items.token_type)
[](https://platform.claude.com/docs/en/api/admin#user_cost.data)
data_refreshed_at: string
RFC 3339 timestamp of the export this response was served from. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).
[](https://platform.claude.com/docs/en/api/admin#user_cost.data_refreshed_at)
has_more: boolean
[](https://platform.claude.com/docs/en/api/admin#user_cost.has_more)
next_page: string
[](https://platform.claude.com/docs/en/api/admin#user_cost.next_page)
organization_id: string
ID of the Organization.
[](https://platform.claude.com/docs/en/api/admin#user_cost.organization_id)
[](https://platform.claude.com/docs/en/api/admin#user_cost)
####  AdminAnalyticsUsers
##### [List User Activity](https://platform.claude.com/docs/en/api/admin/analytics/users/list)
GET/v1/organizations/analytics/users
##### ModelsExpand Collapse 
UserActivity object { data, next_page } 
Response for GET /v1/organizations/analytics/users.
data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 4 more } 
chat_metrics: object { connectors_used_count, distinct_artifacts_created_count, distinct_conversation_count, 8 more } 
Claude.ai activity metrics for a single user on a given day.
connectors_used_count: number
Number of MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.chat_metrics.connectors_used_count)
distinct_artifacts_created_count: number
Number of distinct artifacts created
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.chat_metrics.distinct_artifacts_created_count)
distinct_conversation_count: number
Number of distinct conversations the user participated in. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.chat_metrics.distinct_conversation_count)
distinct_files_uploaded_count: number
Number of distinct files uploaded. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.chat_metrics.distinct_files_uploaded_count)
distinct_projects_created_count: number
Number of distinct projects created
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.chat_metrics.distinct_projects_created_count)
distinct_projects_used_count: number
Number of distinct projects used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.chat_metrics.distinct_projects_used_count)
distinct_shared_artifacts_viewed_count: number
Number of distinct shared artifacts the user viewed. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.chat_metrics.distinct_shared_artifacts_viewed_count)
distinct_skills_used_count: number
Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.chat_metrics.distinct_skills_used_count)
message_count: number
Number of messages sent
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.chat_metrics.message_count)
shared_conversations_viewed_count: number
Number of times the user opened a shared conversation in a project
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.chat_metrics.shared_conversations_viewed_count)
thinking_message_count: number
Number of messages that used extended thinking
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.chat_metrics.thinking_message_count)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.chat_metrics)
claude_code_metrics: object { core_metrics, tool_actions } 
Claude Code activity metrics for a single user on a given day.
core_metrics: object { commit_count, distinct_session_count, lines_of_code, pull_request_count } 
Core Claude Code activity metrics for a single user on a given day.
commit_count: number
Number of commits made via Claude Code
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.core_metrics.commit_count)
distinct_session_count: number
Number of distinct Claude Code sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.core_metrics.distinct_session_count)
lines_of_code: object { added_count, removed_count } 
Lines of code added and removed via Claude Code.
added_count: number
Lines of code added
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.core_metrics.lines_of_code.added_count)
removed_count: number
Lines of code removed
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.core_metrics.lines_of_code.removed_count)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.core_metrics.lines_of_code)
pull_request_count: number
Number of pull requests created via Claude Code
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.core_metrics.pull_request_count)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.core_metrics)
tool_actions: object { edit_tool, multi_edit_tool, notebook_edit_tool, write_tool } 
Per-tool accepted/rejected counts for Claude Code file modification tools.
edit_tool: [ToolActionCounts](https://platform.claude.com/docs/en/api/admin#tool_action_counts) { accepted_count, rejected_count } 
Accepted/rejected counts for a single Claude Code tool type.
accepted_count: number
Number of tool proposals accepted
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.tool_actions.edit_tool%20%2B%20\(resource\)%20admin.analytics.accepted_count)
rejected_count: number
Number of tool proposals rejected
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.tool_actions.edit_tool%20%2B%20\(resource\)%20admin.analytics.rejected_count)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.tool_actions.edit_tool)
multi_edit_tool: [ToolActionCounts](https://platform.claude.com/docs/en/api/admin#tool_action_counts) { accepted_count, rejected_count } 
Accepted/rejected counts for a single Claude Code tool type.
accepted_count: number
Number of tool proposals accepted
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.tool_actions.multi_edit_tool%20%2B%20\(resource\)%20admin.analytics.accepted_count)
rejected_count: number
Number of tool proposals rejected
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.tool_actions.multi_edit_tool%20%2B%20\(resource\)%20admin.analytics.rejected_count)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.tool_actions.multi_edit_tool)
notebook_edit_tool: [ToolActionCounts](https://platform.claude.com/docs/en/api/admin#tool_action_counts) { accepted_count, rejected_count } 
Accepted/rejected counts for a single Claude Code tool type.
accepted_count: number
Number of tool proposals accepted
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.tool_actions.notebook_edit_tool%20%2B%20\(resource\)%20admin.analytics.accepted_count)
rejected_count: number
Number of tool proposals rejected
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.tool_actions.notebook_edit_tool%20%2B%20\(resource\)%20admin.analytics.rejected_count)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.tool_actions.notebook_edit_tool)
write_tool: [ToolActionCounts](https://platform.claude.com/docs/en/api/admin#tool_action_counts) { accepted_count, rejected_count } 
Accepted/rejected counts for a single Claude Code tool type.
accepted_count: number
Number of tool proposals accepted
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.tool_actions.write_tool%20%2B%20\(resource\)%20admin.analytics.accepted_count)
rejected_count: number
Number of tool proposals rejected
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.tool_actions.write_tool%20%2B%20\(resource\)%20admin.analytics.rejected_count)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.tool_actions.write_tool)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics.tool_actions)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.claude_code_metrics)
cowork_metrics: object { action_count, connectors_used_count, dispatch_turn_count, 5 more } 
Cowork activity metrics for a single user on a given day.
action_count: number
Number of tool actions completed in Cowork sessions
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.cowork_metrics.action_count)
connectors_used_count: number
Total number of connector invocations in Cowork sessions
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.cowork_metrics.connectors_used_count)
dispatch_turn_count: number
Number of Dispatch (background agent) turns completed
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.cowork_metrics.dispatch_turn_count)
distinct_connectors_used_count: number
Number of distinct connectors used in Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.cowork_metrics.distinct_connectors_used_count)
distinct_session_count: number
Number of distinct Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.cowork_metrics.distinct_session_count)
distinct_skills_used_count: number
Number of distinct skills used in Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.cowork_metrics.distinct_skills_used_count)
message_count: number
Number of messages sent in Cowork sessions
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.cowork_metrics.message_count)
skills_used_count: number
Total number of skill invocations in Cowork sessions
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.cowork_metrics.skills_used_count)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.cowork_metrics)
design_metrics: object { distinct_projects_created_count, distinct_projects_used_count, distinct_session_count, message_count } 
Claude Design activity metrics for a single user on a given day.
distinct_projects_created_count: number
Number of distinct Claude Design projects created
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.design_metrics.distinct_projects_created_count)
distinct_projects_used_count: number
Number of distinct Claude Design projects the user worked in. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.design_metrics.distinct_projects_used_count)
distinct_session_count: number
Number of distinct Claude Design sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.design_metrics.distinct_session_count)
message_count: number
Number of messages sent in Claude Design sessions
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.design_metrics.message_count)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.design_metrics)
office_metrics: object { excel, outlook, powerpoint, word } 
Office Agent activity metrics for a single user on a given day, broken out by Office product.
excel: [OfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#office_product_metrics) { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more } 
Office Agent activity metrics for a single user on a given day within one Office product.
connectors_used_count: number
Number of MCP connector invocations
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.connectors_used_count)
distinct_connectors_used_count: number
Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.distinct_connectors_used_count)
distinct_session_count: number
Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.distinct_session_count)
distinct_skills_used_count: number
Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.distinct_skills_used_count)
message_count: number
Number of messages sent
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.message_count)
skills_used_count: number
Number of skill invocations
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.skills_used_count)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.excel)
outlook: [OfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#office_product_metrics) { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more } 
Office Agent activity metrics for a single user on a given day within one Office product.
connectors_used_count: number
Number of MCP connector invocations
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.connectors_used_count)
distinct_connectors_used_count: number
Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.distinct_connectors_used_count)
distinct_session_count: number
Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.distinct_session_count)
distinct_skills_used_count: number
Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.distinct_skills_used_count)
message_count: number
Number of messages sent
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.message_count)
skills_used_count: number
Number of skill invocations
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.skills_used_count)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.outlook)
powerpoint: [OfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#office_product_metrics) { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more } 
Office Agent activity metrics for a single user on a given day within one Office product.
connectors_used_count: number
Number of MCP connector invocations
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.connectors_used_count)
distinct_connectors_used_count: number
Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.distinct_connectors_used_count)
distinct_session_count: number
Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.distinct_session_count)
distinct_skills_used_count: number
Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.distinct_skills_used_count)
message_count: number
Number of messages sent
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.message_count)
skills_used_count: number
Number of skill invocations
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.skills_used_count)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.powerpoint)
word: [OfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#office_product_metrics) { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more } 
Office Agent activity metrics for a single user on a given day within one Office product.
connectors_used_count: number
Number of MCP connector invocations
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.connectors_used_count)
distinct_connectors_used_count: number
Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.distinct_connectors_used_count)
distinct_session_count: number
Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.distinct_session_count)
distinct_skills_used_count: number
Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.distinct_skills_used_count)
message_count: number
Number of messages sent
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.message_count)
skills_used_count: number
Number of skill invocations
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.skills_used_count)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics.word)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.office_metrics)
web_search_count: number
Number of web searches performed
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.web_search_count)
user: optional [AnalyticsUser](https://platform.claude.com/docs/en/api/admin#analytics_user) { id, email_address } 
User identifier.
Tagged user identifier (e.g. user_...)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.user%20%2B%20\(resource\)%20admin.analytics.id)
email_address: string
Email address of the user
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.user%20%2B%20\(resource\)%20admin.analytics.email_address)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data.items.user)
[](https://platform.claude.com/docs/en/api/admin#user_activity.data)
next_page: string
Opaque cursor for the next page, or null if no more results
[](https://platform.claude.com/docs/en/api/admin#user_activity.next_page)
[](https://platform.claude.com/docs/en/api/admin#user_activity)
####  AdminAnalyticsSkills
##### [Get Skill Usage](https://platform.claude.com/docs/en/api/admin/analytics/skills/list)
GET/v1/organizations/analytics/skills
##### ModelsExpand Collapse 
SkillUsage object { data, next_page } 
Response for GET /v1/organizations/analytics/skills.
data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 3 more } 
chat_metrics: object { distinct_conversation_skill_used_count } 
Claude.ai activity metrics for a single skill on a given day.
distinct_conversation_skill_used_count: number
Number of distinct conversations in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data.items.chat_metrics.distinct_conversation_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data.items.chat_metrics)
claude_code_metrics: object { distinct_session_skill_used_count } 
Claude Code activity metrics for a single skill on a given day.
distinct_session_skill_used_count: number
Number of distinct Claude Code sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data.items.claude_code_metrics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data.items.claude_code_metrics)
cowork_metrics: object { distinct_session_skill_used_count } 
Cowork activity metrics for a single skill on a given day.
distinct_session_skill_used_count: number
Number of distinct Cowork sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data.items.cowork_metrics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data.items.cowork_metrics)
distinct_user_count: number
Number of distinct users who used the skill on the requested day
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data.items.distinct_user_count)
office_metrics: object { excel, outlook, powerpoint, word } 
Office Agent activity metrics for a single skill on a given day, broken out by Office product.
excel: [SkillOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#skill_office_product_metrics) { distinct_session_skill_used_count } 
Office Agent activity metrics for a single skill on a given day within one Office product.
distinct_session_skill_used_count: number
Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data.items.office_metrics.excel)
outlook: [SkillOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#skill_office_product_metrics) { distinct_session_skill_used_count } 
Office Agent activity metrics for a single skill on a given day within one Office product.
distinct_session_skill_used_count: number
Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data.items.office_metrics.outlook)
powerpoint: [SkillOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#skill_office_product_metrics) { distinct_session_skill_used_count } 
Office Agent activity metrics for a single skill on a given day within one Office product.
distinct_session_skill_used_count: number
Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data.items.office_metrics.powerpoint)
word: [SkillOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#skill_office_product_metrics) { distinct_session_skill_used_count } 
Office Agent activity metrics for a single skill on a given day within one Office product.
distinct_session_skill_used_count: number
Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data.items.office_metrics.word)
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data.items.office_metrics)
skill_name: string
Name of the skill
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data.items.skill_name)
[](https://platform.claude.com/docs/en/api/admin#skill_usage.data)
next_page: string
Opaque cursor for the next page, or null if no more results
[](https://platform.claude.com/docs/en/api/admin#skill_usage.next_page)
[](https://platform.claude.com/docs/en/api/admin#skill_usage)
####  AdminAnalyticsConnectors
##### [Get Connector Usage](https://platform.claude.com/docs/en/api/admin/analytics/connectors/list)
GET/v1/organizations/analytics/connectors
##### ModelsExpand Collapse 
ConnectorUsage object { data, next_page } 
Response for GET /v1/organizations/analytics/connectors.
data: array of object { chat_metrics, claude_code_metrics, connector_name, 3 more } 
chat_metrics: object { distinct_conversation_connector_used_count } 
Claude.ai activity metrics for a single connector on a given day.
distinct_conversation_connector_used_count: number
Number of distinct conversations in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data.items.chat_metrics.distinct_conversation_connector_used_count)
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data.items.chat_metrics)
claude_code_metrics: object { distinct_session_connector_used_count } 
Claude Code activity metrics for a single connector on a given day.
distinct_session_connector_used_count: number
Number of distinct Claude Code sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data.items.claude_code_metrics.distinct_session_connector_used_count)
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data.items.claude_code_metrics)
connector_name: string
Name of the connector
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data.items.connector_name)
cowork_metrics: object { distinct_session_connector_used_count } 
Cowork activity metrics for a single connector on a given day.
distinct_session_connector_used_count: number
Number of distinct Cowork sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data.items.cowork_metrics.distinct_session_connector_used_count)
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data.items.cowork_metrics)
distinct_user_count: number
Number of distinct users who used the connector on the requested day
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data.items.distinct_user_count)
office_metrics: object { excel, outlook, powerpoint, word } 
Office Agent activity metrics for a single connector on a given day, broken out by Office product.
excel: [ConnectorOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#connector_office_product_metrics) { distinct_session_connector_used_count } 
Office Agent activity metrics for a single connector on a given day within one Office product.
distinct_session_connector_used_count: number
Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.distinct_session_connector_used_count)
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data.items.office_metrics.excel)
outlook: [ConnectorOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#connector_office_product_metrics) { distinct_session_connector_used_count } 
Office Agent activity metrics for a single connector on a given day within one Office product.
distinct_session_connector_used_count: number
Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.distinct_session_connector_used_count)
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data.items.office_metrics.outlook)
powerpoint: [ConnectorOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#connector_office_product_metrics) { distinct_session_connector_used_count } 
Office Agent activity metrics for a single connector on a given day within one Office product.
distinct_session_connector_used_count: number
Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.distinct_session_connector_used_count)
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data.items.office_metrics.powerpoint)
word: [ConnectorOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#connector_office_product_metrics) { distinct_session_connector_used_count } 
Office Agent activity metrics for a single connector on a given day within one Office product.
distinct_session_connector_used_count: number
Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.distinct_session_connector_used_count)
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data.items.office_metrics.word)
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data.items.office_metrics)
[](https://platform.claude.com/docs/en/api/admin#connector_usage.data)
next_page: string
Opaque cursor for the next page, or null if no more results
[](https://platform.claude.com/docs/en/api/admin#connector_usage.next_page)
[](https://platform.claude.com/docs/en/api/admin#connector_usage)
####  AdminAnalyticsChat Projects
##### [Get Chat Project Usage](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list)
GET/v1/organizations/analytics/apps/chat/projects
##### ModelsExpand Collapse 
ChatProjectUsage object { data, next_page } 
Response for GET /v1/organizations/analytics/apps/chat/projects.
data: array of object { distinct_conversation_count, distinct_user_count, message_count, 4 more } 
distinct_conversation_count: number
Number of distinct conversations in the project on the requested day
[](https://platform.claude.com/docs/en/api/admin#chat_project_usage.data.items.distinct_conversation_count)
distinct_user_count: number
Number of distinct users who used the project on the requested day
[](https://platform.claude.com/docs/en/api/admin#chat_project_usage.data.items.distinct_user_count)
message_count: number
Number of messages sent in the project on the requested day
[](https://platform.claude.com/docs/en/api/admin#chat_project_usage.data.items.message_count)
project_id: string
Tagged project identifier (e.g. claude_proj_...)
[](https://platform.claude.com/docs/en/api/admin#chat_project_usage.data.items.project_id)
project_name: string
Name of the project
[](https://platform.claude.com/docs/en/api/admin#chat_project_usage.data.items.project_name)
created_at: optional string
Project creation timestamp, RFC 3339. Null if the project was deleted before attribution was recorded.
[](https://platform.claude.com/docs/en/api/admin#chat_project_usage.data.items.created_at)
created_by: optional [AnalyticsUser](https://platform.claude.com/docs/en/api/admin#analytics_user) { id, email_address } 
User identifier.
Tagged user identifier (e.g. user_...)
[](https://platform.claude.com/docs/en/api/admin#chat_project_usage.data.items.created_by%20%2B%20\(resource\)%20admin.analytics.id)
email_address: string
Email address of the user
[](https://platform.claude.com/docs/en/api/admin#chat_project_usage.data.items.created_by%20%2B%20\(resource\)%20admin.analytics.email_address)
[](https://platform.claude.com/docs/en/api/admin#chat_project_usage.data.items.created_by)
[](https://platform.claude.com/docs/en/api/admin#chat_project_usage.data)
next_page: string
Opaque cursor for the next page, or null if no more results
[](https://platform.claude.com/docs/en/api/admin#chat_project_usage.next_page)
[](https://platform.claude.com/docs/en/api/admin#chat_project_usage)
####  AdminSpend Limits
##### [Set Spend Limit](https://platform.claude.com/docs/en/api/admin/spend_limits/create)
POST/v1/organizations/spend_limits
##### [Get Spend Limit](https://platform.claude.com/docs/en/api/admin/spend_limits/retrieve)
GET/v1/organizations/spend_limits/{spend_limit_id}
##### [Delete Spend Limit](https://platform.claude.com/docs/en/api/admin/spend_limits/delete)
DELETE/v1/organizations/spend_limits/{spend_limit_id}
##### [List Effective Spend Limits](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective)
GET/v1/organizations/spend_limits/effective
##### ModelsExpand Collapse 
SpendLimit object { id, amount, created_at, 5 more } 
[](https://platform.claude.com/docs/en/api/admin#spend_limit.id)
amount: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit.amount)
created_at: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit.created_at)
currency: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit.currency)
period: "monthly" or "daily" or "weekly"
"monthly"
[](https://platform.claude.com/docs/en/api/admin#spend_limit.period%5B0%5D)
"daily"
[](https://platform.claude.com/docs/en/api/admin#spend_limit.period%5B1%5D)
"weekly"
[](https://platform.claude.com/docs/en/api/admin#spend_limit.period%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin#spend_limit.period)
scope: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more
User object { type, user_id } 
type: "user"
[](https://platform.claude.com/docs/en/api/admin#spend_limit.scope%5B0%5D.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit.scope%5B0%5D.user_id)
[](https://platform.claude.com/docs/en/api/admin#spend_limit.scope%5B0%5D)
SeatTier object { seat_tier, type } 
seat_tier: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit.scope%5B1%5D.seat_tier)
type: "seat_tier"
[](https://platform.claude.com/docs/en/api/admin#spend_limit.scope%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin#spend_limit.scope%5B1%5D)
RbacGroup object { rbac_group_id, type } 
rbac_group_id: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit.scope%5B2%5D.rbac_group_id)
type: "rbac_group"
[](https://platform.claude.com/docs/en/api/admin#spend_limit.scope%5B2%5D.type)
[](https://platform.claude.com/docs/en/api/admin#spend_limit.scope%5B2%5D)
OrganizationService object { service, type } 
service: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit.scope%5B3%5D.service)
type: "organization_service"
[](https://platform.claude.com/docs/en/api/admin#spend_limit.scope%5B3%5D.type)
[](https://platform.claude.com/docs/en/api/admin#spend_limit.scope%5B3%5D)
Organization object { type } 
type: "organization"
[](https://platform.claude.com/docs/en/api/admin#spend_limit.scope%5B4%5D.type)
[](https://platform.claude.com/docs/en/api/admin#spend_limit.scope%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin#spend_limit.scope)
type: "spend_limit"
[](https://platform.claude.com/docs/en/api/admin#spend_limit.type)
updated_at: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit.updated_at)
[](https://platform.claude.com/docs/en/api/admin#spend_limit)
SpendSummary object { actor, amount, currency, 5 more } 
Per-member effective-limit report row (GET /spend_limits/effective).
actor: object { deleted, email_address, name, 2 more } 
A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.
deleted: boolean
[](https://platform.claude.com/docs/en/api/admin#spend_summary.actor.deleted)
email_address: string
[](https://platform.claude.com/docs/en/api/admin#spend_summary.actor.email_address)
name: string
[](https://platform.claude.com/docs/en/api/admin#spend_summary.actor.name)
type: "user_actor"
[](https://platform.claude.com/docs/en/api/admin#spend_summary.actor.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin#spend_summary.actor.user_id)
[](https://platform.claude.com/docs/en/api/admin#spend_summary.actor)
amount: string
[](https://platform.claude.com/docs/en/api/admin#spend_summary.amount)
currency: string
[](https://platform.claude.com/docs/en/api/admin#spend_summary.currency)
period: "monthly" or "daily" or "weekly"
"monthly"
[](https://platform.claude.com/docs/en/api/admin#spend_summary.period%5B0%5D)
"daily"
[](https://platform.claude.com/docs/en/api/admin#spend_summary.period%5B1%5D)
"weekly"
[](https://platform.claude.com/docs/en/api/admin#spend_summary.period%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin#spend_summary.period)
period_to_date_spend: string
[](https://platform.claude.com/docs/en/api/admin#spend_summary.period_to_date_spend)
scope: object { type, user_id } 
type: "user"
[](https://platform.claude.com/docs/en/api/admin#spend_summary.scope.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin#spend_summary.scope.user_id)
[](https://platform.claude.com/docs/en/api/admin#spend_summary.scope)
source: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more
User object { type, user_id } 
type: "user"
[](https://platform.claude.com/docs/en/api/admin#spend_summary.source%5B0%5D.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin#spend_summary.source%5B0%5D.user_id)
[](https://platform.claude.com/docs/en/api/admin#spend_summary.source%5B0%5D)
SeatTier object { seat_tier, type } 
seat_tier: string
[](https://platform.claude.com/docs/en/api/admin#spend_summary.source%5B1%5D.seat_tier)
type: "seat_tier"
[](https://platform.claude.com/docs/en/api/admin#spend_summary.source%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin#spend_summary.source%5B1%5D)
RbacGroup object { rbac_group_id, type } 
rbac_group_id: string
[](https://platform.claude.com/docs/en/api/admin#spend_summary.source%5B2%5D.rbac_group_id)
type: "rbac_group"
[](https://platform.claude.com/docs/en/api/admin#spend_summary.source%5B2%5D.type)
[](https://platform.claude.com/docs/en/api/admin#spend_summary.source%5B2%5D)
OrganizationService object { service, type } 
service: string
[](https://platform.claude.com/docs/en/api/admin#spend_summary.source%5B3%5D.service)
type: "organization_service"
[](https://platform.claude.com/docs/en/api/admin#spend_summary.source%5B3%5D.type)
[](https://platform.claude.com/docs/en/api/admin#spend_summary.source%5B3%5D)
Organization object { type } 
type: "organization"
[](https://platform.claude.com/docs/en/api/admin#spend_summary.source%5B4%5D.type)
[](https://platform.claude.com/docs/en/api/admin#spend_summary.source%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin#spend_summary.source)
spend_limit_id: string
[](https://platform.claude.com/docs/en/api/admin#spend_summary.spend_limit_id)
[](https://platform.claude.com/docs/en/api/admin#spend_summary)
SpendLimitDeleteResponse object { id, type } 
[](https://platform.claude.com/docs/en/api/admin#spend_limit_delete_response.id)
type: "spend_limit_deleted"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_delete_response.type)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_delete_response)
####  AdminSpend LimitsIncrease Requests
##### [List Spend Limit Increase Requests](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/list)
GET/v1/organizations/spend_limit_increase_requests
##### [Get Spend Limit Increase Request](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/retrieve)
GET/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}
##### [Approve Spend Limit Increase Request](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve)
POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve
##### [Deny Spend Limit Increase Request](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/deny)
POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny
##### ModelsExpand Collapse 
SpendLimitIncreaseRequest object { id, actor, created_at, 6 more } 
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.id)
actor: object { deleted, email_address, name, 2 more } 
A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.
deleted: boolean
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.actor.deleted)
email_address: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.actor.email_address)
name: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.actor.name)
type: "user_actor"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.actor.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.actor.user_id)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.actor)
created_at: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.created_at)
period: "monthly" or "daily" or "weekly"
"monthly"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.period%5B0%5D)
"daily"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.period%5B1%5D)
"weekly"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.period%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.period)
resolved_at: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.resolved_at)
resolved_by: object { deleted, email_address, name, 2 more }  or object { scoped_api_key_id, type } 
A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.
UserActor object { deleted, email_address, name, 2 more } 
A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.
deleted: boolean
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.resolved_by%5B0%5D.deleted)
email_address: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.resolved_by%5B0%5D.email_address)
name: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.resolved_by%5B0%5D.name)
type: "user_actor"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.resolved_by%5B0%5D.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.resolved_by%5B0%5D.user_id)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.resolved_by%5B0%5D)
ScopedAPIKeyActor object { scoped_api_key_id, type } 
A scoped Admin API key acting on behalf of the organization.
scoped_api_key_id: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.resolved_by%5B1%5D.scoped_api_key_id)
type: "scoped_api_key_actor"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.resolved_by%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.resolved_by%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.resolved_by)
spend_summary: [SpendSummary](https://platform.claude.com/docs/en/api/admin#spend_summary) { actor, amount, currency, 5 more } 
Per-member effective-limit report row (GET /spend_limits/effective).
actor: object { deleted, email_address, name, 2 more } 
A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.
deleted: boolean
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor.deleted)
email_address: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor.email_address)
name: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor.name)
type: "user_actor"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor.user_id)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor)
amount: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.amount)
currency: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.currency)
period: "monthly" or "daily" or "weekly"
"monthly"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.period%5B0%5D)
"daily"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.period%5B1%5D)
"weekly"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.period%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.period)
period_to_date_spend: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.period_to_date_spend)
scope: object { type, user_id } 
type: "user"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.scope.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.scope.user_id)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.scope)
source: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more
User object { type, user_id } 
type: "user"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B0%5D.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B0%5D.user_id)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B0%5D)
SeatTier object { seat_tier, type } 
seat_tier: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B1%5D.seat_tier)
type: "seat_tier"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B1%5D)
RbacGroup object { rbac_group_id, type } 
rbac_group_id: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B2%5D.rbac_group_id)
type: "rbac_group"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B2%5D.type)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B2%5D)
OrganizationService object { service, type } 
service: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B3%5D.service)
type: "organization_service"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B3%5D.type)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B3%5D)
Organization object { type } 
type: "organization"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B4%5D.type)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source)
spend_limit_id: string
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.spend_limit_id)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.spend_summary)
status: "pending" or "approved" or "denied"
"pending"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.status%5B0%5D)
"approved"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.status%5B1%5D)
"denied"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.status%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.status)
type: "spend_limit_increase_request"
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request.type)
[](https://platform.claude.com/docs/en/api/admin#spend_limit_increase_request)
IncreaseRequestApproveResponse object { id, actor, created_at, 7 more } 
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.id)
actor: object { deleted, email_address, name, 2 more } 
A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.
deleted: boolean
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.actor.deleted)
email_address: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.actor.email_address)
name: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.actor.name)
type: "user_actor"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.actor.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.actor.user_id)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.actor)
created_at: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.created_at)
period: "monthly" or "daily" or "weekly"
"monthly"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.period%5B0%5D)
"daily"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.period%5B1%5D)
"weekly"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.period%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.period)
resolved_at: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.resolved_at)
resolved_by: object { deleted, email_address, name, 2 more }  or object { scoped_api_key_id, type } 
A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.
UserActor object { deleted, email_address, name, 2 more } 
A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.
deleted: boolean
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.resolved_by%5B0%5D.deleted)
email_address: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.resolved_by%5B0%5D.email_address)
name: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.resolved_by%5B0%5D.name)
type: "user_actor"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.resolved_by%5B0%5D.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.resolved_by%5B0%5D.user_id)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.resolved_by%5B0%5D)
ScopedAPIKeyActor object { scoped_api_key_id, type } 
A scoped Admin API key acting on behalf of the organization.
scoped_api_key_id: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.resolved_by%5B1%5D.scoped_api_key_id)
type: "scoped_api_key_actor"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.resolved_by%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.resolved_by%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.resolved_by)
spend_limit: [SpendLimit](https://platform.claude.com/docs/en/api/admin#spend_limit) { id, amount, created_at, 5 more } 
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.id)
amount: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.amount)
created_at: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.created_at)
currency: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.currency)
period: "monthly" or "daily" or "weekly"
"monthly"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.period%5B0%5D)
"daily"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.period%5B1%5D)
"weekly"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.period%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.period)
scope: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more
User object { type, user_id } 
type: "user"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B0%5D.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B0%5D.user_id)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B0%5D)
SeatTier object { seat_tier, type } 
seat_tier: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B1%5D.seat_tier)
type: "seat_tier"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B1%5D)
RbacGroup object { rbac_group_id, type } 
rbac_group_id: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B2%5D.rbac_group_id)
type: "rbac_group"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B2%5D.type)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B2%5D)
OrganizationService object { service, type } 
service: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B3%5D.service)
type: "organization_service"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B3%5D.type)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B3%5D)
Organization object { type } 
type: "organization"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B4%5D.type)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope)
type: "spend_limit"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.type)
updated_at: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.updated_at)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_limit)
spend_summary: [SpendSummary](https://platform.claude.com/docs/en/api/admin#spend_summary) { actor, amount, currency, 5 more } 
Per-member effective-limit report row (GET /spend_limits/effective).
actor: object { deleted, email_address, name, 2 more } 
A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.
deleted: boolean
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor.deleted)
email_address: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor.email_address)
name: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor.name)
type: "user_actor"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor.user_id)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor)
amount: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.amount)
currency: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.currency)
period: "monthly" or "daily" or "weekly"
"monthly"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.period%5B0%5D)
"daily"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.period%5B1%5D)
"weekly"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.period%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.period)
period_to_date_spend: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.period_to_date_spend)
scope: object { type, user_id } 
type: "user"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.scope.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.scope.user_id)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.scope)
source: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more
User object { type, user_id } 
type: "user"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B0%5D.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B0%5D.user_id)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B0%5D)
SeatTier object { seat_tier, type } 
seat_tier: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B1%5D.seat_tier)
type: "seat_tier"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B1%5D)
RbacGroup object { rbac_group_id, type } 
rbac_group_id: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B2%5D.rbac_group_id)
type: "rbac_group"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B2%5D.type)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B2%5D)
OrganizationService object { service, type } 
service: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B3%5D.service)
type: "organization_service"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B3%5D.type)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B3%5D)
Organization object { type } 
type: "organization"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B4%5D.type)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source)
spend_limit_id: string
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.spend_limit_id)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.spend_summary)
status: "pending" or "approved" or "denied"
"pending"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.status%5B0%5D)
"approved"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.status%5B1%5D)
"denied"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.status%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.status)
type: "spend_limit_increase_request"
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response.type)
[](https://platform.claude.com/docs/en/api/admin#increase_request_approve_response)
####  AdminRate Limits
##### [List Organization Rate Limits](https://platform.claude.com/docs/en/api/admin/rate_limits/list)
GET/v1/organizations/rate_limits
##### ModelsExpand Collapse 
RateLimitListResponse object { data, next_page } 
data: array of object { group_type, limits, models, type } 
Rate-limit entries for the organization, one per group.
group_type: "model_group" or "batch" or "token_count" or 3 more
The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.
"model_group"
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.group_type%5B0%5D)
"batch"
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.group_type%5B1%5D)
"token_count"
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.group_type%5B2%5D)
"files"
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.group_type%5B3%5D)
"skills"
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.group_type%5B4%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.group_type%5B5%5D)
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.group_type)
limits: array of object { type, value } 
The limiter values that apply to this group.
type: string
The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.limits.items.type)
value: number
The configured limit value for this limiter type.
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.limits.items.value)
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.limits)
models: array of string
Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.models)
type: "rate_limit"
Object type. Always `rate_limit` for organization rate-limit entries.
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data.items.type)
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.data)
next_page: string
Token to provide in as `page` in the subsequent request to retrieve the next page of data.
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response.next_page)
[](https://platform.claude.com/docs/en/api/admin#rate_limit_list_response)
####  AdminService Accounts
##### [Create Service Account](https://platform.claude.com/docs/en/api/admin/service_accounts/create)
POST/v1/organizations/service_accounts
##### [Get Service Account](https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve)
GET/v1/organizations/service_accounts/{service_account_id}
##### [List Service Accounts](https://platform.claude.com/docs/en/api/admin/service_accounts/list)
GET/v1/organizations/service_accounts
##### [Update Service Account](https://platform.claude.com/docs/en/api/admin/service_accounts/update)
POST/v1/organizations/service_accounts/{service_account_id}
##### [Archive Service Account](https://platform.claude.com/docs/en/api/admin/service_accounts/archive)
POST/v1/organizations/service_accounts/{service_account_id}/archive
##### ModelsExpand Collapse 
ServiceAccount object { id, archived_at, archived_by_actor_id, 8 more } 
Named non-human identity within the caller's organization.
A service account is a pure identity: name + org. Authorization lives on whatever references it (federation rules).
Tagged ID of the service account.
[](https://platform.claude.com/docs/en/api/admin#service_account.id)
archived_at: string
If set, this service account is archived.
[](https://platform.claude.com/docs/en/api/admin#service_account.archived_at)
archived_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that archived this service account.
[](https://platform.claude.com/docs/en/api/admin#service_account.archived_by_actor_id)
created_at: string
When this service account was created.
[](https://platform.claude.com/docs/en/api/admin#service_account.created_at)
created_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that created this service account.
[](https://platform.claude.com/docs/en/api/admin#service_account.created_by_actor_id)
description: string
Optional free-text description.
[](https://platform.claude.com/docs/en/api/admin#service_account.description)
name: string
Admin-chosen slug identifier.
[](https://platform.claude.com/docs/en/api/admin#service_account.name)
organization_role: "developer" or "admin"
Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.
"developer"
[](https://platform.claude.com/docs/en/api/admin#service_account.organization_role%5B0%5D)
"admin"
[](https://platform.claude.com/docs/en/api/admin#service_account.organization_role%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin#service_account.organization_role)
type: "service_account"
[](https://platform.claude.com/docs/en/api/admin#service_account.type)
updated_at: string
When this service account was last updated.
[](https://platform.claude.com/docs/en/api/admin#service_account.updated_at)
updated_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.
[](https://platform.claude.com/docs/en/api/admin#service_account.updated_by_actor_id)
[](https://platform.claude.com/docs/en/api/admin#service_account)
####  AdminService AccountsWorkspaces
##### [Add Workspace To Service Account](https://platform.claude.com/docs/en/api/admin/service_accounts/workspaces/create)
POST/v1/organizations/service_accounts/{service_account_id}/workspaces
##### [List Workspaces For Service Account](https://platform.claude.com/docs/en/api/admin/service_accounts/workspaces/list)
GET/v1/organizations/service_accounts/{service_account_id}/workspaces
##### [Remove Workspace From Service Account](https://platform.claude.com/docs/en/api/admin/service_accounts/workspaces/delete)
DELETE/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}
##### ModelsExpand Collapse 
WorkspaceCreateResponse object { created_by_actor_id, implicit, service_account_id, 3 more } 
created_by_actor_id: string
Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response.created_by_actor_id)
implicit: boolean
True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response.implicit)
service_account_id: string
Tagged service account ID (`svac_...`).
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response.service_account_id)
type: "service_account_workspace_member"
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response.type)
workspace_id: string
Tagged workspace ID (`wrkspc_...`).
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response.workspace_id)
workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more
Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.
"workspace_user"
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response.workspace_role%5B0%5D)
"workspace_developer"
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response.workspace_role%5B1%5D)
"workspace_restricted_developer"
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response.workspace_role%5B2%5D)
"workspace_admin"
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response.workspace_role%5B3%5D)
"workspace_billing"
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response.workspace_role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response.workspace_role)
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response)
WorkspaceListResponse object { created_by_actor_id, implicit, service_account_id, 3 more } 
created_by_actor_id: string
Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response.created_by_actor_id)
implicit: boolean
True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response.implicit)
service_account_id: string
Tagged service account ID (`svac_...`).
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response.service_account_id)
type: "service_account_workspace_member"
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response.type)
workspace_id: string
Tagged workspace ID (`wrkspc_...`).
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response.workspace_id)
workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more
Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.
"workspace_user"
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response.workspace_role%5B0%5D)
"workspace_developer"
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response.workspace_role%5B1%5D)
"workspace_restricted_developer"
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response.workspace_role%5B2%5D)
"workspace_admin"
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response.workspace_role%5B3%5D)
"workspace_billing"
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response.workspace_role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response.workspace_role)
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response)
WorkspaceDeleteResponse object { service_account_id, type, workspace_id } 
service_account_id: string
Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.
[](https://platform.claude.com/docs/en/api/admin#workspace_delete_response.service_account_id)
type: "service_account_workspace_member_deleted"
[](https://platform.claude.com/docs/en/api/admin#workspace_delete_response.type)
workspace_id: string
Tagged workspace ID (`wrkspc_...`) named in the delete request.
[](https://platform.claude.com/docs/en/api/admin#workspace_delete_response.workspace_id)
[](https://platform.claude.com/docs/en/api/admin#workspace_delete_response)
####  AdminFederation Issuers
##### [Create Federation Issuer](https://platform.claude.com/docs/en/api/admin/federation_issuers/create)
POST/v1/organizations/federation_issuers
##### [Get Federation Issuer](https://platform.claude.com/docs/en/api/admin/federation_issuers/retrieve)
GET/v1/organizations/federation_issuers/{federation_issuer_id}
##### [List Federation Issuers](https://platform.claude.com/docs/en/api/admin/federation_issuers/list)
GET/v1/organizations/federation_issuers
##### [Update Federation Issuer](https://platform.claude.com/docs/en/api/admin/federation_issuers/update)
POST/v1/organizations/federation_issuers/{federation_issuer_id}
##### [Archive Federation Issuer](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive)
POST/v1/organizations/federation_issuers/{federation_issuer_id}/archive
##### ModelsExpand Collapse 
FederationIssuer object { id, archived_at, archived_by_actor_id, 12 more } 
Registered external OIDC identity provider.
Records an external IdP the organization trusts for the RFC 7523 jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.
Tagged ID of the federation issuer.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.id)
archived_at: string
If set, all rules referencing this issuer reject token exchange.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.archived_at)
archived_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.archived_by_actor_id)
check_jti: boolean
Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.check_jti)
created_at: string
When this issuer was created.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.created_at)
created_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that created this issuer.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.created_by_actor_id)
issuer_url: string
The `iss` claim value. Incoming JWTs must match exactly.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.issuer_url)
jwks: object { type, ca_cert_pem, discovery_base }  or object { type, url, ca_cert_pem }  or object { keys, type } 
How signing keys are obtained for signature verification.
Discovery object { type, ca_cert_pem, discovery_base } 
JWKS via the issuer's OIDC discovery document.
type: "discovery"
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.jwks%5B0%5D.type)
ca_cert_pem: optional string
Optional custom CA (PEM) for TLS verification of the JWKS fetch.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.jwks%5B0%5D.ca_cert_pem)
discovery_base: optional string
Set when the discovery URL differs from `issuer_url`.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.jwks%5B0%5D.discovery_base)
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.jwks%5B0%5D)
ExplicitURL object { type, url, ca_cert_pem } 
JWKS fetched from a fixed endpoint.
type: "explicit_url"
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.jwks%5B1%5D.type)
url: string
JWKS endpoint.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.jwks%5B1%5D.url)
ca_cert_pem: optional string
Optional custom CA (PEM) for TLS verification of the JWKS fetch.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.jwks%5B1%5D.ca_cert_pem)
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.jwks%5B1%5D)
Inline object { keys, type } 
JWKS supplied directly; no network fetch.
keys: array of map[unknown]
Inline JWK objects.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.jwks%5B2%5D.keys)
type: "inline"
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.jwks%5B2%5D.type)
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.jwks%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.jwks)
jwks_polling_disabled_at: string
If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.jwks_polling_disabled_at)
max_jwt_lifetime_seconds: number
Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.max_jwt_lifetime_seconds)
name: string
Admin-chosen slug identifier.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.name)
poll_status: object { consecutive_failures, last_fetched_at, next_poll_at } 
Status of automatic JWKS polling for a federation issuer.
Anthropic periodically fetches the issuer's signing keys in the background. These fields summarize the most recent fetches so the health of the JWKS endpoint can be monitored.
consecutive_failures: number
Consecutive fetch failures since the last success.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.poll_status.consecutive_failures)
last_fetched_at: string
When the last successful fetch completed.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.poll_status.last_fetched_at)
next_poll_at: string
When the next fetch is scheduled. Null if paused.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.poll_status.next_poll_at)
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.poll_status)
type: "federation_issuer"
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.type)
updated_at: string
When this issuer was last updated.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.updated_at)
updated_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.
[](https://platform.claude.com/docs/en/api/admin#federation_issuer.updated_by_actor_id)
[](https://platform.claude.com/docs/en/api/admin#federation_issuer)
####  AdminFederation Rules
##### [Create Federation Rule](https://platform.claude.com/docs/en/api/admin/federation_rules/create)
POST/v1/organizations/federation_rules
##### [Get Federation Rule](https://platform.claude.com/docs/en/api/admin/federation_rules/retrieve)
GET/v1/organizations/federation_rules/{federation_rule_id}
##### [List Federation Rules](https://platform.claude.com/docs/en/api/admin/federation_rules/list)
GET/v1/organizations/federation_rules
##### [Update Federation Rule](https://platform.claude.com/docs/en/api/admin/federation_rules/update)
POST/v1/organizations/federation_rules/{federation_rule_id}
##### [Archive Federation Rule](https://platform.claude.com/docs/en/api/admin/federation_rules/archive)
POST/v1/organizations/federation_rules/{federation_rule_id}/archive
##### ModelsExpand Collapse 
FederationRule object { id, applies_to_all_workspaces, archived_at, 17 more } 
Authorization rule binding an external OIDC identity to Anthropic.
Evaluates the match conditions and mints an OAuth access token for the resolved target, scoped to a single workspace where the rule is enabled (chosen by the caller at exchange time when the rule is enabled for more than one). For rules enabled via `workspace_ids` or `applies_to_all_workspaces`, the target service account must be a member of that workspace (it is implicitly a member of the default workspace); rules carrying only the legacy `workspace_id` binding do not enforce this.
Tagged ID of the federation rule.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.id)
applies_to_all_workspaces: boolean
When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.applies_to_all_workspaces)
archived_at: string
If set, this rule is archived and rejects token exchange.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.archived_at)
archived_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that archived this rule.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.archived_by_actor_id)
attributes: map[string]
CEL expressions extracting named values from claims. Not yet supported; always null.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.attributes)
created_at: string
When this rule was created.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.created_at)
created_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that created this rule.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.created_by_actor_id)
description: string
Optional free-text description.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.description)
issuer_id: string
Tagged ID of the issuer whose tokens this rule accepts.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.issuer_id)
issuer_name: string
Issuer's display name at read time.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.issuer_name)
match: object { audience, claims, condition, subject_prefix } 
Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.
audience: optional string
Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.match.audience)
claims: optional map[string]
Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.match.claims)
condition: optional string
CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.match.condition)
subject_prefix: optional string
Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.match.subject_prefix)
[](https://platform.claude.com/docs/en/api/admin#federation_rule.match)
name: string
Admin-chosen slug identifier.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.name)
oauth_scope: string
Space-separated OAuth scopes granted on the minted token.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.oauth_scope)
target: object { service_account_id, type, service_account_name } 
Identity that tokens minted via this rule act as. Currently always a `service_account` target.
service_account_id: string
Tagged ID of the service account to mint tokens for.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.target.service_account_id)
type: "service_account"
[](https://platform.claude.com/docs/en/api/admin#federation_rule.target.type)
service_account_name: optional string
Service account's display name at read time. Ignored on writes.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.target.service_account_name)
[](https://platform.claude.com/docs/en/api/admin#federation_rule.target)
token_lifetime_seconds: number
Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.token_lifetime_seconds)
type: "federation_rule"
[](https://platform.claude.com/docs/en/api/admin#federation_rule.type)
updated_at: string
When this rule was last updated.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.updated_at)
updated_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.updated_by_actor_id)
workspace_id: string
Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.
[](https://platform.claude.com/docs/en/api/admin#federation_rule.workspace_id)
workspace_ids: array of string
Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).
[](https://platform.claude.com/docs/en/api/admin#federation_rule.workspace_ids)
[](https://platform.claude.com/docs/en/api/admin#federation_rule)
####  AdminFederation RulesWorkspaces
##### [List Federation Rule Workspaces](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/list)
GET/v1/organizations/federation_rules/{federation_rule_id}/workspaces
##### [Add Federation Rule Workspace](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/create)
POST/v1/organizations/federation_rules/{federation_rule_id}/workspaces
##### [Remove Federation Rule Workspace](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/delete)
DELETE/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}
##### ModelsExpand Collapse 
WorkspaceListResponse object { created_at, created_by_actor_id, federation_rule_id, 3 more } 
created_at: string
When this workspace was enabled for the rule.
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response.created_at)
created_by_actor_id: string
Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response.created_by_actor_id)
federation_rule_id: string
Tagged ID of the federation rule.
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response.federation_rule_id)
type: "federation_rule_workspace"
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response.type)
workspace_id: string
Tagged ID of the workspace this rule is enabled for.
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response.workspace_id)
workspace_name: string
Workspace display name. Populated when listing; null in the enable response.
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response.workspace_name)
[](https://platform.claude.com/docs/en/api/admin#workspace_list_response)
WorkspaceCreateResponse object { created_at, created_by_actor_id, federation_rule_id, 3 more } 
created_at: string
When this workspace was enabled for the rule.
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response.created_at)
created_by_actor_id: string
Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response.created_by_actor_id)
federation_rule_id: string
Tagged ID of the federation rule.
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response.federation_rule_id)
type: "federation_rule_workspace"
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response.type)
workspace_id: string
Tagged ID of the workspace this rule is enabled for.
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response.workspace_id)
workspace_name: string
Workspace display name. Populated when listing; null in the enable response.
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response.workspace_name)
[](https://platform.claude.com/docs/en/api/admin#workspace_create_response)
WorkspaceDeleteResponse object { federation_rule_id, type, workspace_id } 
federation_rule_id: string
Tagged ID of the federation rule.
[](https://platform.claude.com/docs/en/api/admin#workspace_delete_response.federation_rule_id)
type: "federation_rule_workspace_deleted"
[](https://platform.claude.com/docs/en/api/admin#workspace_delete_response.type)
workspace_id: string
Tagged ID of the workspace named in the delete request. Removal is idempotent.
[](https://platform.claude.com/docs/en/api/admin#workspace_delete_response.workspace_id)
[](https://platform.claude.com/docs/en/api/admin#workspace_delete_response)
####  AdminMCP Tunnels
##### [Get Tunnel](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/retrieve)
GET/v1/organizations/tunnels/{tunnel_id}
##### [List Tunnels](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/list)
GET/v1/organizations/tunnels
##### [Reveal Tunnel Token](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/reveal_token)
POST/v1/organizations/tunnels/{tunnel_id}/reveal_token
##### [Rotate Tunnel Token](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/rotate_token)
POST/v1/organizations/tunnels/{tunnel_id}/rotate_token
##### [Archive Tunnel](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/archive)
POST/v1/organizations/tunnels/{tunnel_id}/archive
##### ModelsExpand Collapse 
MCPTunnelRetrieveResponse object { id, archived_at, created_at, 4 more } 
ID of the Tunnel.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_retrieve_response.id)
archived_at: string
RFC 3339 datetime string indicating when the Tunnel was archived, or `null` if it is not archived.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_retrieve_response.archived_at)
created_at: string
RFC 3339 datetime string indicating when the Tunnel was created.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_retrieve_response.created_at)
display_name: string
Human-readable name for the Tunnel (1–255 characters), or `null` if unset.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_retrieve_response.display_name)
domain: string
Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a subdomain of this value are routed through the Tunnel. Globally unique and never reused, even after the Tunnel is archived.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_retrieve_response.domain)
type: "tunnel"
Object type. Always `tunnel` for Tunnels.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_retrieve_response.type)
workspace_id: string
ID of the Workspace this Tunnel belongs to, or `null` for the default Workspace. Immutable after creation.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_retrieve_response.workspace_id)
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_retrieve_response)
MCPTunnelListResponse object { id, archived_at, created_at, 4 more } 
ID of the Tunnel.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_list_response.id)
archived_at: string
RFC 3339 datetime string indicating when the Tunnel was archived, or `null` if it is not archived.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_list_response.archived_at)
created_at: string
RFC 3339 datetime string indicating when the Tunnel was created.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_list_response.created_at)
display_name: string
Human-readable name for the Tunnel (1–255 characters), or `null` if unset.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_list_response.display_name)
domain: string
Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a subdomain of this value are routed through the Tunnel. Globally unique and never reused, even after the Tunnel is archived.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_list_response.domain)
type: "tunnel"
Object type. Always `tunnel` for Tunnels.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_list_response.type)
workspace_id: string
ID of the Workspace this Tunnel belongs to, or `null` for the default Workspace. Immutable after creation.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_list_response.workspace_id)
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_list_response)
MCPTunnelRevealTokenResponse object { id, tunnel_token, type } 
Stable identifier for the current token value. Changes when the token is rotated.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_reveal_token_response.id)
tunnel_token: string
The tunnel's connection token.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_reveal_token_response.tunnel_token)
type: "tunnel_token"
Object type. Always `tunnel_token` for Tunnel Tokens.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_reveal_token_response.type)
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_reveal_token_response)
MCPTunnelRotateTokenResponse object { id, tunnel_token, type } 
Stable identifier for the current token value. Changes when the token is rotated.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_rotate_token_response.id)
tunnel_token: string
The tunnel's connection token.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_rotate_token_response.tunnel_token)
type: "tunnel_token"
Object type. Always `tunnel_token` for Tunnel Tokens.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_rotate_token_response.type)
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_rotate_token_response)
MCPTunnelArchiveResponse object { id, archived_at, created_at, 4 more } 
ID of the Tunnel.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_archive_response.id)
archived_at: string
RFC 3339 datetime string indicating when the Tunnel was archived, or `null` if it is not archived.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_archive_response.archived_at)
created_at: string
RFC 3339 datetime string indicating when the Tunnel was created.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_archive_response.created_at)
display_name: string
Human-readable name for the Tunnel (1–255 characters), or `null` if unset.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_archive_response.display_name)
domain: string
Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a subdomain of this value are routed through the Tunnel. Globally unique and never reused, even after the Tunnel is archived.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_archive_response.domain)
type: "tunnel"
Object type. Always `tunnel` for Tunnels.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_archive_response.type)
workspace_id: string
ID of the Workspace this Tunnel belongs to, or `null` for the default Workspace. Immutable after creation.
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_archive_response.workspace_id)
[](https://platform.claude.com/docs/en/api/admin#mcp_tunnel_archive_response)
####  AdminMCP TunnelsTunnel Certificates
##### [Create Tunnel Certificate](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create)
POST/v1/organizations/tunnels/{tunnel_id}/certificates
##### [Get Tunnel Certificate](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/retrieve)
GET/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}
##### [List Tunnel Certificates](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list)
GET/v1/organizations/tunnels/{tunnel_id}/certificates
##### [Archive Tunnel Certificate](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/archive)
POST/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}/archive
##### ModelsExpand Collapse 
TunnelCertificateCreateResponse object { id, archived_at, created_at, 4 more } 
ID of the Tunnel Certificate.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_create_response.id)
archived_at: string
RFC 3339 datetime string indicating when the certificate was archived, or `null` if it is not archived.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_create_response.archived_at)
created_at: string
RFC 3339 datetime string indicating when the certificate was registered.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_create_response.created_at)
expires_at: string
RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_create_response.expires_at)
fingerprint: string
The certificate's SHA-256 fingerprint, as a lowercase hex string.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_create_response.fingerprint)
tunnel_id: string
ID of the Tunnel this certificate is registered against.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_create_response.tunnel_id)
type: "tunnel_certificate"
Object type. Always `tunnel_certificate` for Tunnel Certificates.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_create_response.type)
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_create_response)
TunnelCertificateRetrieveResponse object { id, archived_at, created_at, 4 more } 
ID of the Tunnel Certificate.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_retrieve_response.id)
archived_at: string
RFC 3339 datetime string indicating when the certificate was archived, or `null` if it is not archived.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_retrieve_response.archived_at)
created_at: string
RFC 3339 datetime string indicating when the certificate was registered.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_retrieve_response.created_at)
expires_at: string
RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_retrieve_response.expires_at)
fingerprint: string
The certificate's SHA-256 fingerprint, as a lowercase hex string.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_retrieve_response.fingerprint)
tunnel_id: string
ID of the Tunnel this certificate is registered against.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_retrieve_response.tunnel_id)
type: "tunnel_certificate"
Object type. Always `tunnel_certificate` for Tunnel Certificates.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_retrieve_response.type)
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_retrieve_response)
TunnelCertificateListResponse object { id, archived_at, created_at, 4 more } 
ID of the Tunnel Certificate.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_list_response.id)
archived_at: string
RFC 3339 datetime string indicating when the certificate was archived, or `null` if it is not archived.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_list_response.archived_at)
created_at: string
RFC 3339 datetime string indicating when the certificate was registered.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_list_response.created_at)
expires_at: string
RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_list_response.expires_at)
fingerprint: string
The certificate's SHA-256 fingerprint, as a lowercase hex string.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_list_response.fingerprint)
tunnel_id: string
ID of the Tunnel this certificate is registered against.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_list_response.tunnel_id)
type: "tunnel_certificate"
Object type. Always `tunnel_certificate` for Tunnel Certificates.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_list_response.type)
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_list_response)
TunnelCertificateArchiveResponse object { id, archived_at, created_at, 4 more } 
ID of the Tunnel Certificate.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_archive_response.id)
archived_at: string
RFC 3339 datetime string indicating when the certificate was archived, or `null` if it is not archived.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_archive_response.archived_at)
created_at: string
RFC 3339 datetime string indicating when the certificate was registered.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_archive_response.created_at)
expires_at: string
RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_archive_response.expires_at)
fingerprint: string
The certificate's SHA-256 fingerprint, as a lowercase hex string.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_archive_response.fingerprint)
tunnel_id: string
ID of the Tunnel this certificate is registered against.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_archive_response.tunnel_id)
type: "tunnel_certificate"
Object type. Always `tunnel_certificate` for Tunnel Certificates.
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_archive_response.type)
[](https://platform.claude.com/docs/en/api/admin#tunnel_certificate_archive_response)
