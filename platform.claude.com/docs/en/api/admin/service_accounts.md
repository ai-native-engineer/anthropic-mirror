<!-- source: https://platform.claude.com/docs/en/api/admin/service_accounts -->

# Service Accounts
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
[](https://platform.claude.com/docs/en/api/admin/service_accounts#service_account.id)
archived_at: string
If set, this service account is archived.
[](https://platform.claude.com/docs/en/api/admin/service_accounts#service_account.archived_at)
archived_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that archived this service account.
[](https://platform.claude.com/docs/en/api/admin/service_accounts#service_account.archived_by_actor_id)
created_at: string
When this service account was created.
[](https://platform.claude.com/docs/en/api/admin/service_accounts#service_account.created_at)
created_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that created this service account.
[](https://platform.claude.com/docs/en/api/admin/service_accounts#service_account.created_by_actor_id)
description: string
Optional free-text description.
[](https://platform.claude.com/docs/en/api/admin/service_accounts#service_account.description)
name: string
Admin-chosen slug identifier.
[](https://platform.claude.com/docs/en/api/admin/service_accounts#service_account.name)
organization_role: "developer" or "admin"
Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.
"developer"
[](https://platform.claude.com/docs/en/api/admin/service_accounts#service_account.organization_role%5B0%5D)
"admin"
[](https://platform.claude.com/docs/en/api/admin/service_accounts#service_account.organization_role%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/service_accounts#service_account.organization_role)
type: "service_account"
[](https://platform.claude.com/docs/en/api/admin/service_accounts#service_account.type)
updated_at: string
When this service account was last updated.
[](https://platform.claude.com/docs/en/api/admin/service_accounts#service_account.updated_at)
updated_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.
[](https://platform.claude.com/docs/en/api/admin/service_accounts#service_account.updated_by_actor_id)
[](https://platform.claude.com/docs/en/api/admin/service_accounts#service_account)
####  Service AccountsWorkspaces
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
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_create_response.created_by_actor_id)
implicit: boolean
True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_create_response.implicit)
service_account_id: string
Tagged service account ID (`svac_...`).
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_create_response.service_account_id)
type: "service_account_workspace_member"
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_create_response.type)
workspace_id: string
Tagged workspace ID (`wrkspc_...`).
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_create_response.workspace_id)
workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more
Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.
"workspace_user"
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_create_response.workspace_role%5B0%5D)
"workspace_developer"
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_create_response.workspace_role%5B1%5D)
"workspace_restricted_developer"
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_create_response.workspace_role%5B2%5D)
"workspace_admin"
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_create_response.workspace_role%5B3%5D)
"workspace_billing"
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_create_response.workspace_role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_create_response.workspace_role)
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_create_response)
WorkspaceListResponse object { created_by_actor_id, implicit, service_account_id, 3 more } 
created_by_actor_id: string
Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_list_response.created_by_actor_id)
implicit: boolean
True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_list_response.implicit)
service_account_id: string
Tagged service account ID (`svac_...`).
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_list_response.service_account_id)
type: "service_account_workspace_member"
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_list_response.type)
workspace_id: string
Tagged workspace ID (`wrkspc_...`).
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_list_response.workspace_id)
workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more
Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.
"workspace_user"
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_list_response.workspace_role%5B0%5D)
"workspace_developer"
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_list_response.workspace_role%5B1%5D)
"workspace_restricted_developer"
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_list_response.workspace_role%5B2%5D)
"workspace_admin"
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_list_response.workspace_role%5B3%5D)
"workspace_billing"
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_list_response.workspace_role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_list_response.workspace_role)
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_list_response)
WorkspaceDeleteResponse object { service_account_id, type, workspace_id } 
service_account_id: string
Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_delete_response.service_account_id)
type: "service_account_workspace_member_deleted"
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_delete_response.type)
workspace_id: string
Tagged workspace ID (`wrkspc_...`) named in the delete request.
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_delete_response.workspace_id)
[](https://platform.claude.com/docs/en/api/admin/service_accounts#workspace_delete_response)
