<!-- source: https://platform.claude.com/docs/en/api/admin/analytics/usage/list -->

# Get Token Usage Over Time
GET/v1/organizations/analytics/usage_report
Get token usage over time across a date range.
Returns token usage bucketed by minute, hour, or day, optionally broken down by product, model, context window, inference region, or speed. Available to organizations on a Claude Enterprise plan. Requires an API key with the `read:analytics` scope.
##### Query ParametersExpand Collapse 
starting_at: string
Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00
.
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.starting_at)
bucket_width: optional "1m" or "1h" or "1d"
Time bucket granularity.
"1m"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.bucket_width%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.bucket_width%5B1%5D)
"1d"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.bucket_width%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.bucket_width)
context_windows: optional array of "0-200k" or "200k-1M"
Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.
"0-200k"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.context_windows.items%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.context_windows.items%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.context_windows)
ending_at: optional string
End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.ending_at)
group_by: optional array of "product" or "model" or "context_window" or 2 more
Dimensions to break each time bucket out by. Defaults to no grouping (one total per bucket).
"product"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.group_by.items%5B0%5D)
"model"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.group_by.items%5B1%5D)
"context_window"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.group_by.items%5B2%5D)
"inference_geo"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.group_by.items%5B3%5D)
"speed"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.group_by.items%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.group_by)
inference_geos: optional array of "global" or "us" or "not_available"
Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.
"global"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.inference_geos.items%5B0%5D)
"us"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.inference_geos.items%5B1%5D)
"not_available"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.inference_geos.items%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.inference_geos)
limit: optional number
Maximum number of time buckets per page. Defaults and caps vary by bucket_width (1d: default 7, max 31; 1h: default 24, max 168; 1m: default 60, max 256).
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.limit)
models: optional array of string
Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.models)
page: optional string
Opaque cursor from a previous response's `next_page` field.
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.page)
products: optional array of string
Product surfaces to include. Defaults to all products. Use `group_by[]=product` to break out per-product values. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design".
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.products)
speeds: optional array of "fast" or "standard"
Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.
"fast"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.speeds.items%5B0%5D)
"standard"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.speeds.items%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.speeds)
user_ids: optional array of string
Filter to specific users by tagged user ID.
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#list.user_ids)
UsageBucket object { data, data_refreshed_at, has_more, 2 more } 
data: array of object { ending_at, results, starting_at } 
ending_at: string
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.ending_at)
results: array of object { cache_creation, cache_read_input_tokens, context_window, 8 more } 
cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
ephemeral_1h_input_tokens: number
The number of input tokens used to create the 1 hour cache entry.
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.cache_creation.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: number
The number of input tokens used to create the 5 minute cache entry.
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.cache_creation.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.cache_creation)
cache_read_input_tokens: number
The number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.cache_read_input_tokens)
context_window: "0-200k" or "200k-1M"
"0-200k"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.context_window%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.context_window%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.context_window)
inference_geo: "global" or "us"
"global"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.inference_geo%5B0%5D)
"us"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.inference_geo%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.inference_geo)
model: string
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.model)
output_tokens: number
The number of output tokens generated.
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.output_tokens)
product: string
Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.product)
requests: number
Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.requests)
server_tool_use: object { web_search_requests } 
web_search_requests: number
The number of web search requests made.
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.server_tool_use.web_search_requests)
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.server_tool_use)
speed: "fast" or "standard"
"fast"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.speed%5B0%5D)
"standard"
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.speed)
uncached_input_tokens: number
The number of uncached input tokens processed.
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results.items.uncached_input_tokens)
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.results)
starting_at: string
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data.items.starting_at)
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data)
data_refreshed_at: string
RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.data_refreshed_at)
has_more: boolean
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.has_more)
next_page: string
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.next_page)
organization_id: string
ID of the Organization.
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket.organization_id)
[](https://platform.claude.com/docs/en/api/admin/analytics/usage/list#usage_bucket)
Get Token Usage Over Time

curl https://api.anthropic.com/v1/organizations/analytics/usage_report \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "ending_at": "2019-12-27T18:11:19.117Z",
      "results": [
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          "cache_read_input_tokens": 0,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "model",
          "output_tokens": 0,
          "product": "product",
          "requests": 0,
          "server_tool_use": {
            "web_search_requests": 10
          "speed": "fast",
          "uncached_input_tokens": 0
      ],
      "starting_at": "2019-12-27T18:11:19.117Z"
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"

  "data": [
      "ending_at": "2019-12-27T18:11:19.117Z",
      "results": [
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          "cache_read_input_tokens": 0,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "model",
          "output_tokens": 0,
          "product": "product",
          "requests": 0,
          "server_tool_use": {
            "web_search_requests": 10
          "speed": "fast",
          "uncached_input_tokens": 0
      ],
      "starting_at": "2019-12-27T18:11:19.117Z"
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
