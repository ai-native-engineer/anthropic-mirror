<!-- source: https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages -->

# Get Messages Usage Report
GET/v1/organizations/usage_report/messages
Get Messages Usage Report
##### Query ParametersExpand Collapse 
starting_at: string
Time buckets that start on or after this RFC 3339 timestamp will be returned. Each time bucket will be snapped to the start of the minute/hour/day in UTC.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.starting_at)
account_ids: optional array of string
Restrict usage returned to the specified user account ID(s).
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.account_ids)
api_key_ids: optional array of string
Restrict usage returned to the specified API key ID(s).
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.api_key_ids)
bucket_width: optional "1d" or "1m" or "1h"
Time granularity of the response data.
"1d"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.bucket_width%5B0%5D)
"1m"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.bucket_width%5B1%5D)
"1h"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.bucket_width%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.bucket_width)
context_window: optional array of "0-200k" or "200k-1M"
Restrict usage returned to the specified context window(s).
"0-200k"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.context_window.items%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.context_window.items%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.context_window)
ending_at: optional string
Time buckets that end before this RFC 3339 timestamp will be returned.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.ending_at)
group_by: optional array of "api_key_id" or "workspace_id" or "model" or 6 more
Group by any subset of the available options. Grouping by `speed` requires the `fast-mode-2026-02-01` beta header.
"api_key_id"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.group_by.items%5B0%5D)
"workspace_id"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.group_by.items%5B1%5D)
"model"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.group_by.items%5B2%5D)
"service_tier"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.group_by.items%5B3%5D)
"context_window"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.group_by.items%5B4%5D)
"inference_geo"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.group_by.items%5B5%5D)
"speed"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.group_by.items%5B6%5D)
"account_id"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.group_by.items%5B7%5D)
"service_account_id"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.group_by.items%5B8%5D)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.group_by)
inference_geos: optional array of "global" or "us" or "not_available"
Restrict usage returned to the specified inference geo(s). Use `not_available` for models that do not support specifying `inference_geo`.
"global"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.inference_geos.items%5B0%5D)
"us"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.inference_geos.items%5B1%5D)
"not_available"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.inference_geos.items%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.inference_geos)
limit: optional number
Maximum number of time buckets to return in the response.
The default and max limits depend on `bucket_width`: • `"1d"`: Default of 7 days, maximum of 31 days • `"1h"`: Default of 24 hours, maximum of 168 hours • `"1m"`: Default of 60 minutes, maximum of 1440 minutes
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.limit)
models: optional array of string
Restrict usage returned to the specified model(s).
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.models)
page: optional string
Optionally set to the `next_page` token from the previous response.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.page)
service_account_ids: optional array of string
Restrict usage returned to the specified service account ID(s).
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.service_account_ids)
service_tiers: optional array of "standard" or "batch" or "priority" or 3 more
Restrict usage returned to the specified service tier(s).
"standard"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.service_tiers.items%5B0%5D)
"batch"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.service_tiers.items%5B1%5D)
"priority"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.service_tiers.items%5B2%5D)
"priority_on_demand"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.service_tiers.items%5B3%5D)
"flex"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.service_tiers.items%5B4%5D)
"flex_discount"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.service_tiers.items%5B5%5D)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.service_tiers)
speeds: optional array of "standard" or "fast"
Restrict usage returned to the specified speed(s) (Claude Code research preview). Requires the `fast-mode-2026-02-01` beta header.
"standard"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.speeds.items%5B0%5D)
"fast"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.speeds.items%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.speeds)
workspace_ids: optional array of string
Restrict usage returned to the specified workspace ID(s).
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.workspace_ids)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of string
Optional header to specify the beta version(s) you want to use.
To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#retrieve_messages.anthropic-beta)
MessagesUsageReport object { data, has_more, next_page } 
data: array of object { ending_at, results, starting_at } 
ending_at: string
End of the time bucket (exclusive) in RFC 3339 format.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.ending_at)
results: array of object { account_id, api_key_id, cache_creation, 10 more } 
List of usage items for this time bucket. There may be multiple items if one or more `group_by[]` parameters are specified.
account_id: string
ID of the user account that made the request. `null` if not grouping by account or for non-OAuth requests.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.account_id)
api_key_id: string
ID of the API key used. `null` if not grouping by API key or for usage in the Anthropic Console.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.api_key_id)
cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
The number of input tokens for cache creation.
ephemeral_1h_input_tokens: number
The number of input tokens used to create the 1 hour cache entry.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.cache_creation.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: number
The number of input tokens used to create the 5 minute cache entry.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.cache_creation.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.cache_creation)
cache_read_input_tokens: number
The number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.cache_read_input_tokens)
context_window: "0-200k" or "200k-1M"
Context window used. `null` if not grouping by context window.
"0-200k"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.context_window%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.context_window%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.context_window)
inference_geo: string
Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`. For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.inference_geo)
model: string
Model used. `null` if not grouping by model.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.model)
output_tokens: number
The number of output tokens generated.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.output_tokens)
server_tool_use: object { web_search_requests } 
Server-side tool usage metrics.
web_search_requests: number
The number of web search requests made.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.server_tool_use.web_search_requests)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.server_tool_use)
service_account_id: string
ID of the service account that made the request. `null` if not grouping by service account or for non-OIDC-federation requests.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.service_account_id)
service_tier: "standard" or "batch" or "priority" or 3 more
Service tier used. `null` if not grouping by service tier.
"standard"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.service_tier%5B0%5D)
"batch"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.service_tier%5B1%5D)
"priority"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.service_tier%5B2%5D)
"priority_on_demand"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.service_tier%5B3%5D)
"flex"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.service_tier%5B4%5D)
"flex_discount"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.service_tier%5B5%5D)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.service_tier)
uncached_input_tokens: number
The number of uncached input tokens processed.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.uncached_input_tokens)
workspace_id: string
ID of the Workspace used. `null` if not grouping by workspace or for the default workspace.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results.items.workspace_id)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.results)
starting_at: string
Start of the time bucket (inclusive) in RFC 3339 format.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data.items.starting_at)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.data)
has_more: boolean
Indicates if there are more results.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.has_more)
next_page: string
Token to provide in as `page` in the subsequent request to retrieve the next page of data.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report.next_page)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages#messages_usage_report)
Get Messages Usage Report

curl https://api.anthropic.com/v1/organizations/usage_report/messages \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "ending_at": "2025-08-02T00:00:00Z",
      "results": [
          "account_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "api_key_id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          "cache_read_input_tokens": 200,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "claude-opus-4-6",
          "output_tokens": 500,
          "server_tool_use": {
            "web_search_requests": 10
          "service_account_id": "svac_01Hk3R9TWxq7CfQak00OiVw4",
          "service_tier": "standard",
          "uncached_input_tokens": 1500,
          "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
      ],
      "starting_at": "2025-08-01T00:00:00Z"
  ],
  "has_more": true,
  "next_page": "2019-12-27T18:11:19.117Z"

  "data": [
      "ending_at": "2025-08-02T00:00:00Z",
      "results": [
          "account_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "api_key_id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          "cache_read_input_tokens": 200,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "claude-opus-4-6",
          "output_tokens": 500,
          "server_tool_use": {
            "web_search_requests": 10
          "service_account_id": "svac_01Hk3R9TWxq7CfQak00OiVw4",
          "service_tier": "standard",
          "uncached_input_tokens": 1500,
          "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
      ],
      "starting_at": "2025-08-01T00:00:00Z"
  ],
  "has_more": true,
  "next_page": "2019-12-27T18:11:19.117Z"
