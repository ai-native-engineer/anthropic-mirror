<!-- source: https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list -->

# List Service Account Workspace Members
GET/v1/organizations/workspaces/{workspace_id}/service_accounts
List the service accounts that are members of a workspace.
Each entry includes the service account's `workspace_role`. Use `limit` and the `next_page` cursor to paginate. Archived workspaces return 400; use `GET /service_accounts/{id}/workspaces` to audit memberships of an archived workspace. The implicit default-workspace membership is not included in this list. Memberships of archived service accounts are omitted from the results.
##### Path ParametersExpand Collapse 
workspace_id: string
ID of the workspace.
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list#list.workspace_id)
##### Query ParametersExpand Collapse 
limit: optional number
Number of results per page.
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list#list.limit)
page: optional string
Opaque cursor from a previous response's `next_page`.
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list#list.page)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of string
Optional header to specify the beta version(s) you want to use.
To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list#list.anthropic-beta)
data: array of object { created_by_actor_id, implicit, service_account_id, 3 more } 
created_by_actor_id: string
Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list#service_account_list_response.created_by_actor_id)
implicit: boolean
True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list#service_account_list_response.implicit)
service_account_id: string
Tagged service account ID (`svac_...`).
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list#service_account_list_response.service_account_id)
type: "service_account_workspace_member"
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list#service_account_list_response.type)
workspace_id: string
Tagged workspace ID (`wrkspc_...`).
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list#service_account_list_response.workspace_id)
workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more
Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.
"workspace_user"
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list#service_account_list_response.workspace_role%5B0%5D)
"workspace_developer"
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list#service_account_list_response.workspace_role%5B1%5D)
"workspace_restricted_developer"
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list#service_account_list_response.workspace_role%5B2%5D)
"workspace_admin"
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list#service_account_list_response.workspace_role%5B3%5D)
"workspace_billing"
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list#service_account_list_response.workspace_role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list#service_account_list_response.workspace_role)
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list#list)
next_page: string
Opaque cursor for the next page, or null if no more results.
[](https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list#list)
List Service Account Workspace Members

curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "created_by_actor_id": "created_by_actor_id",
      "implicit": true,
      "service_account_id": "service_account_id",
      "type": "service_account_workspace_member",
      "workspace_id": "workspace_id",
      "workspace_role": "workspace_user"
  ],
  "next_page": "next_page"

  "data": [
      "created_by_actor_id": "created_by_actor_id",
      "implicit": true,
      "service_account_id": "service_account_id",
      "type": "service_account_workspace_member",
      "workspace_id": "workspace_id",
      "workspace_role": "workspace_user"
  ],
  "next_page": "next_page"
