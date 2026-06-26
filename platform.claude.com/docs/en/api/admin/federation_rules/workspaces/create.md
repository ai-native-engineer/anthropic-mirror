<!-- source: https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/create -->

# Add Federation Rule Workspace
POST/v1/organizations/federation_rules/{federation_rule_id}/workspaces
Enable a federation rule for a workspace.
Idempotent; re-enabling returns the existing enablement. The rule and workspace must both belong to your organization. Membership of the rule's target service account in this workspace is not checked at enablement: token exchange into this workspace is rejected unless the target is a member (it is implicitly a member of the default workspace). Archived rules are rejected with 400. OAuth callers may only manage rules whose `oauth_scope` is `workspace:developer` or `workspace:inference`; other scopes require a Console session. Admin API keys are not accepted.
##### Path ParametersExpand Collapse 
federation_rule_id: string
ID of the federation rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/create#create.federation_rule_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of string
Optional header to specify the beta version(s) you want to use.
To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/create#create.anthropic-beta)
#####  Body ParametersJSONExpand Collapse 
workspace_id: string
Tagged ID of the workspace to enable this rule for.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/create#create.workspace_id)
created_at: string
When this workspace was enabled for the rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/create#workspace_create_response.created_at)
created_by_actor_id: string
Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/create#workspace_create_response.created_by_actor_id)
federation_rule_id: string
Tagged ID of the federation rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/create#workspace_create_response.federation_rule_id)
type: "federation_rule_workspace"
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/create#workspace_create_response.type)
workspace_id: string
Tagged ID of the workspace this rule is enabled for.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/create#workspace_create_response.workspace_id)
workspace_name: string
Workspace display name. Populated when listing; null in the enable response.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/create#workspace_create_response.workspace_name)
Add Federation Rule Workspace

curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "workspace_id": "workspace_id"
        }'

  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace",
  "workspace_id": "workspace_id",
  "workspace_name": "workspace_name"

  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace",
  "workspace_id": "workspace_id",
  "workspace_name": "workspace_name"
