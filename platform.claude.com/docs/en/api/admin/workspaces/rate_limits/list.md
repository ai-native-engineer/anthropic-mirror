<!-- source: https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list -->

# List Workspace Rate Limits
GET/v1/organizations/workspaces/{workspace_id}/rate_limits
List rate-limit overrides configured for a workspace.
Returns only the groups and limiter types that have a workspace-level override. Groups without overrides inherit the organization limits and are not listed; use `GET /v1/organizations/rate_limits` to see those.
##### Path ParametersExpand Collapse 
workspace_id: string
The ID of the workspace.
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#list.workspace_id)
##### Query ParametersExpand Collapse 
group_type: optional "model_group" or "batch" or "token_count" or 3 more
Filter by group type.
"model_group"
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#list.group_type%5B0%5D)
"batch"
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#list.group_type%5B1%5D)
"token_count"
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#list.group_type%5B2%5D)
"files"
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#list.group_type%5B3%5D)
"skills"
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#list.group_type%5B4%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#list.group_type%5B5%5D)
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#list.group_type)
page: optional string
Opaque cursor from a previous response's `next_page`.
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#list.page)
data: array of object { group_type, limits, models, type } 
Rate-limit entries for the workspace, one per group that has at least one override.
group_type: "model_group" or "batch" or "token_count" or 3 more
The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.
"model_group"
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#rate_limit_list_response.data.items.group_type%5B0%5D)
"batch"
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#rate_limit_list_response.data.items.group_type%5B1%5D)
"token_count"
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#rate_limit_list_response.data.items.group_type%5B2%5D)
"files"
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#rate_limit_list_response.data.items.group_type%5B3%5D)
"skills"
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#rate_limit_list_response.data.items.group_type%5B4%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#rate_limit_list_response.data.items.group_type%5B5%5D)
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#rate_limit_list_response.data.items.group_type)
limits: array of object { org_limit, type, value } 
The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.
org_limit: number
The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#rate_limit_list_response.data.items.limits.items.org_limit)
type: string
The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#rate_limit_list_response.data.items.limits.items.type)
value: number
The workspace-level override value for this limiter type.
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#rate_limit_list_response.data.items.limits.items.value)
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#rate_limit_list_response.data.items.limits)
models: array of string
Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#rate_limit_list_response.data.items.models)
type: "workspace_rate_limit"
Object type. Always `workspace_rate_limit` for workspace rate-limit entries.
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#rate_limit_list_response.data.items.type)
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#rate_limit_list_response.data)
next_page: string
Token to provide in as `page` in the subsequent request to retrieve the next page of data.
[](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list#rate_limit_list_response.next_page)
List Workspace Rate Limits

curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/rate_limits \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "group_type": "model_group",
      "limits": [
          "org_limit": 0,
          "type": "type",
          "value": 0
      ],
      "models": [
        "string"
      ],
      "type": "workspace_rate_limit"
  ],
  "next_page": "next_page"

  "data": [
      "group_type": "model_group",
      "limits": [
          "org_limit": 0,
          "type": "type",
          "value": 0
      ],
      "models": [
        "string"
      ],
      "type": "workspace_rate_limit"
  ],
  "next_page": "next_page"
