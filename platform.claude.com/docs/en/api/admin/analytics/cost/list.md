<!-- source: https://platform.claude.com/docs/en/api/admin/analytics/cost/list -->

# Get Cost Over Time
GET/v1/organizations/analytics/cost_report
Get cost in USD over time across a date range.
Returns cost bucketed by minute, hour, or day, optionally broken down by product, model, context window, inference region, speed, cost type, or token type. Available to organizations on a Claude Enterprise plan. Requires an API key with the `read:analytics` scope.
##### Query ParametersExpand Collapse 
starting_at: string
Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00
.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.starting_at)
bucket_width: optional "1m" or "1h" or "1d"
Time bucket granularity.
"1m"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.bucket_width%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.bucket_width%5B1%5D)
"1d"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.bucket_width%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.bucket_width)
context_windows: optional array of "0-200k" or "200k-1M"
Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.
"0-200k"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.context_windows.items%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.context_windows.items%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.context_windows)
ending_at: optional string
End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.ending_at)
group_by: optional array of "product" or "model" or "context_window" or 4 more
Dimensions to break each time bucket out by. Defaults to no grouping (one total per bucket).
"product"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.group_by.items%5B0%5D)
"model"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.group_by.items%5B1%5D)
"context_window"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.group_by.items%5B2%5D)
"inference_geo"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.group_by.items%5B3%5D)
"speed"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.group_by.items%5B4%5D)
"cost_type"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.group_by.items%5B5%5D)
"token_type"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.group_by.items%5B6%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.group_by)
inference_geos: optional array of "global" or "us" or "not_available"
Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.
"global"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.inference_geos.items%5B0%5D)
"us"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.inference_geos.items%5B1%5D)
"not_available"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.inference_geos.items%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.inference_geos)
limit: optional number
Maximum number of time buckets per page. Defaults and caps vary by bucket_width (1d: default 7, max 31; 1h: default 24, max 168; 1m: default 60, max 256).
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.limit)
models: optional array of string
Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.models)
page: optional string
Opaque cursor from a previous response's `next_page` field.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.page)
products: optional array of string
Product surfaces to include. Defaults to all products. Use `group_by[]=product` to break out per-product values. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design".
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.products)
speeds: optional array of "fast" or "standard"
Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.
"fast"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.speeds.items%5B0%5D)
"standard"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.speeds.items%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.speeds)
user_ids: optional array of string
Filter to specific users by tagged user ID.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#list.user_ids)
CostBucket object { data, data_refreshed_at, has_more, 2 more } 
data: array of object { ending_at, results, starting_at } 
ending_at: string
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.ending_at)
results: array of object { amount, context_window, cost_type, 8 more } 
amount: string
Amount (post-discount, pre-credit) in fractional cents.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.amount)
context_window: "0-200k" or "200k-1M"
"0-200k"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.context_window%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.context_window%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.context_window)
cost_type: "tokens" or "web_search" or "code_execution"
Cost component when `group_by[]=cost_type`; null otherwise (amount is the combined total).
"tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.cost_type%5B0%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.cost_type%5B1%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.cost_type%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.cost_type)
currency: "USD"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.currency)
inference_geo: "global" or "us"
"global"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.inference_geo%5B0%5D)
"us"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.inference_geo%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.inference_geo)
list_amount: string
List-price amount (pre-discount) in fractional cents.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.list_amount)
model: string
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.model)
product: string
Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.product)
requests: number
Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.requests)
speed: "fast" or "standard"
"fast"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.speed%5B0%5D)
"standard"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.speed)
token_type: "uncached_input_tokens" or "output_tokens" or "cache_read_input_tokens" or 2 more
Token type when `group_by[]=token_type` and `cost_type=tokens`; null otherwise.
"uncached_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.token_type%5B0%5D)
"output_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.token_type%5B1%5D)
"cache_read_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.token_type%5B2%5D)
"cache_creation.ephemeral_1h_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.token_type%5B3%5D)
"cache_creation.ephemeral_5m_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.token_type%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results.items.token_type)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.results)
starting_at: string
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data.items.starting_at)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data)
data_refreshed_at: string
RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.data_refreshed_at)
has_more: boolean
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.has_more)
next_page: string
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.next_page)
organization_id: string
ID of the Organization.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket.organization_id)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list#cost_bucket)
Get Cost Over Time

curl https://api.anthropic.com/v1/organizations/analytics/cost_report \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "ending_at": "2019-12-27T18:11:19.117Z",
      "results": [
          "amount": "amount",
          "context_window": "0-200k",
          "cost_type": "tokens",
          "currency": "USD",
          "inference_geo": "global",
          "list_amount": "list_amount",
          "model": "model",
          "product": "product",
          "requests": 0,
          "speed": "fast",
          "token_type": "uncached_input_tokens"
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
          "amount": "amount",
          "context_window": "0-200k",
          "cost_type": "tokens",
          "currency": "USD",
          "inference_geo": "global",
          "list_amount": "list_amount",
          "model": "model",
          "product": "product",
          "requests": 0,
          "speed": "fast",
          "token_type": "uncached_input_tokens"
      ],
      "starting_at": "2019-12-27T18:11:19.117Z"
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
