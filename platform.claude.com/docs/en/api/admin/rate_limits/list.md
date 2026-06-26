<!-- source: https://platform.claude.com/docs/en/api/admin/rate_limits/list -->

# List Organization Rate Limits
GET/v1/organizations/rate_limits
List Messages API rate limits for your organization.
Each entry corresponds to one rate-limit group (either a model family or an API-surface category such as the Files API or Message Batches) and contains the set of limiter values that apply to it.
##### Query ParametersExpand Collapse 
group_type: optional "model_group" or "batch" or "token_count" or 3 more
Filter by group type.
"model_group"
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#list.group_type%5B0%5D)
"batch"
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#list.group_type%5B1%5D)
"token_count"
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#list.group_type%5B2%5D)
"files"
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#list.group_type%5B3%5D)
"skills"
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#list.group_type%5B4%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#list.group_type%5B5%5D)
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#list.group_type)
model: optional string
Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#list.model)
page: optional string
Opaque cursor from a previous response's `next_page`.
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#list.page)
data: array of object { group_type, limits, models, type } 
Rate-limit entries for the organization, one per group.
group_type: "model_group" or "batch" or "token_count" or 3 more
The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.
"model_group"
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#rate_limit_list_response.data.items.group_type%5B0%5D)
"batch"
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#rate_limit_list_response.data.items.group_type%5B1%5D)
"token_count"
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#rate_limit_list_response.data.items.group_type%5B2%5D)
"files"
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#rate_limit_list_response.data.items.group_type%5B3%5D)
"skills"
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#rate_limit_list_response.data.items.group_type%5B4%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#rate_limit_list_response.data.items.group_type%5B5%5D)
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#rate_limit_list_response.data.items.group_type)
limits: array of object { type, value } 
The limiter values that apply to this group.
type: string
The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#rate_limit_list_response.data.items.limits.items.type)
value: number
The configured limit value for this limiter type.
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#rate_limit_list_response.data.items.limits.items.value)
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#rate_limit_list_response.data.items.limits)
models: array of string
Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#rate_limit_list_response.data.items.models)
type: "rate_limit"
Object type. Always `rate_limit` for organization rate-limit entries.
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#rate_limit_list_response.data.items.type)
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#rate_limit_list_response.data)
next_page: string
Token to provide in as `page` in the subsequent request to retrieve the next page of data.
[](https://platform.claude.com/docs/en/api/admin/rate_limits/list#rate_limit_list_response.next_page)
List Organization Rate Limits

curl https://api.anthropic.com/v1/organizations/rate_limits \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "group_type": "model_group",
      "limits": [
          "type": "type",
          "value": 0
      ],
      "models": [
        "string"
      ],
      "type": "rate_limit"
  ],
  "next_page": "next_page"

  "data": [
      "group_type": "model_group",
      "limits": [
          "type": "type",
          "value": 0
      ],
      "models": [
        "string"
      ],
      "type": "rate_limit"
  ],
  "next_page": "next_page"
