<!-- source: https://platform.claude.com/docs/en/api/admin/service_accounts/workspaces/delete -->

# Remove Workspace From Service Account
DELETE/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}
Remove a service account from a workspace.
Mirror of `DELETE /workspaces/{workspace_id}/service_accounts/{service_account_id}`, addressed from the service-account side. Removal is idempotent (returns 200 even if the membership was already removed). A DELETE against the implicit default-workspace membership returns 200 but is a no-op and the membership persists; deleting an explicit default-workspace row reverts to the implicit `workspace_user` membership. Archived workspaces return 400. Requires an OAuth bearer or Console session; Admin API keys are not accepted.
##### Path ParametersExpand Collapse 
service_account_id: string
ID of the service account.
[](https://platform.claude.com/docs/en/api/admin/service_accounts/workspaces/delete#delete.service_account_id)
workspace_id: string
ID of the workspace.
[](https://platform.claude.com/docs/en/api/admin/service_accounts/workspaces/delete#delete.workspace_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of string
Optional header to specify the beta version(s) you want to use.
To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.
[](https://platform.claude.com/docs/en/api/admin/service_accounts/workspaces/delete#delete.anthropic-beta)
service_account_id: string
Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.
[](https://platform.claude.com/docs/en/api/admin/service_accounts/workspaces/delete#workspace_delete_response.service_account_id)
type: "service_account_workspace_member_deleted"
[](https://platform.claude.com/docs/en/api/admin/service_accounts/workspaces/delete#workspace_delete_response.type)
workspace_id: string
Tagged workspace ID (`wrkspc_...`) named in the delete request.
[](https://platform.claude.com/docs/en/api/admin/service_accounts/workspaces/delete#workspace_delete_response.workspace_id)
Remove Workspace From Service Account

curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/workspaces/$WORKSPACE_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member_deleted",
  "workspace_id": "workspace_id"

  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member_deleted",
  "workspace_id": "workspace_id"
