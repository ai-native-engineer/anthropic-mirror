<!-- source: https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/list -->

# List Federation Rule Workspaces
GET/v1/organizations/federation_rules/{federation_rule_id}/workspaces
List workspaces where this federation rule is enabled.
Returns all workspace enablements in a single response; the `limit` and `page` parameters are accepted but have no effect, and `next_page` is always `null`. Returns explicit per-workspace enablements only; for rules with `applies_to_all_workspaces` or a legacy single `workspace_id`, check those fields on the rule itself.
##### Path ParametersExpand Collapse 
federation_rule_id: string
ID of the federation rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/list#list.federation_rule_id)
##### Query ParametersExpand Collapse 
limit: optional number
Number of results per page.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/list#list.limit)
page: optional string
Opaque cursor from a previous response's `next_page`.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/list#list.page)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of string
Optional header to specify the beta version(s) you want to use.
To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/list#list.anthropic-beta)
data: array of object { created_at, created_by_actor_id, federation_rule_id, 3 more } 
created_at: string
When this workspace was enabled for the rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/list#workspace_list_response.created_at)
created_by_actor_id: string
Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/list#workspace_list_response.created_by_actor_id)
federation_rule_id: string
Tagged ID of the federation rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/list#workspace_list_response.federation_rule_id)
type: "federation_rule_workspace"
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/list#workspace_list_response.type)
workspace_id: string
Tagged ID of the workspace this rule is enabled for.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/list#workspace_list_response.workspace_id)
workspace_name: string
Workspace display name. Populated when listing; null in the enable response.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/list#workspace_list_response.workspace_name)
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/list#list)
next_page: string
Opaque cursor for the next page; null when there are no more results.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/list#list)
List Federation Rule Workspaces

curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "federation_rule_id": "federation_rule_id",
      "type": "federation_rule_workspace",
      "workspace_id": "workspace_id",
      "workspace_name": "workspace_name"
  ],
  "next_page": "next_page"

  "data": [
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "federation_rule_id": "federation_rule_id",
      "type": "federation_rule_workspace",
      "workspace_id": "workspace_id",
      "workspace_name": "workspace_name"
  ],
  "next_page": "next_page"
