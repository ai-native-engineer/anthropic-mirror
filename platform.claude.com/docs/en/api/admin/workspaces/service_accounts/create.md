<!-- source: https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create -->

# Create Service Account Workspace Member
POST/v1/organizations/workspaces/{workspace_id}/service_accounts
Add a service account to a workspace with the given `workspace_role`.
The role determines what the service account can do in the workspace and which workspace-scoped permissions it can be granted when authenticating through federation. Every service account is already an implicit `workspace_user` member of the default workspace; adding it explicitly assigns a chosen role. If the service account is already an explicit member of the workspace, its `workspace_role` is replaced with the value supplied here. Archived workspaces return 400. Archived service accounts cannot be added and are rejected. Requires an OAuth bearer or Console session; Admin API keys are not accepted.
##### Path ParametersExpand Collapse 
workspace_id: string
ID of the workspace.
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#create.workspace_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of string
Optional header to specify the beta version(s) you want to use.
To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#create.anthropic-beta)
#####  Body ParametersJSONExpand Collapse 
service_account_id: string
Tagged service account ID to add.
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#create.service_account_id)
workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or "workspace_admin"
Role to assign to the service account in this workspace.
"workspace_user"
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#create.workspace_role%5B0%5D)
"workspace_developer"
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#create.workspace_role%5B1%5D)
"workspace_restricted_developer"
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#create.workspace_role%5B2%5D)
"workspace_admin"
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#create.workspace_role%5B3%5D)
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#create.workspace_role)
created_by_actor_id: string
Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#service_account_create_response.created_by_actor_id)
implicit: boolean
True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#service_account_create_response.implicit)
service_account_id: string
Tagged service account ID (`svac_...`).
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#service_account_create_response.service_account_id)
type: "service_account_workspace_member"
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#service_account_create_response.type)
workspace_id: string
Tagged workspace ID (`wrkspc_...`).
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#service_account_create_response.workspace_id)
workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more
Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.
"workspace_user"
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#service_account_create_response.workspace_role%5B0%5D)
"workspace_developer"
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#service_account_create_response.workspace_role%5B1%5D)
"workspace_restricted_developer"
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#service_account_create_response.workspace_role%5B2%5D)
"workspace_admin"
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#service_account_create_response.workspace_role%5B3%5D)
"workspace_billing"
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#service_account_create_response.workspace_role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/create#service_account_create_response.workspace_role)
Create Service Account Workspace Member

curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "service_account_id": "service_account_id",
          "workspace_role": "workspace_user"
        }'

  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_user"

  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_user"
