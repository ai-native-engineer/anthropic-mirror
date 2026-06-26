<!-- source: https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user -->

# Get Per-User Cost
GET/v1/organizations/analytics/user_cost_report
Get per-user cost in USD across a date range.
Returns one row per user, ranked by spend. Use this to see which users account for the most cost. Available to organizations on a Claude Enterprise plan. Requires an API key with the `read:analytics` scope.
##### Query ParametersExpand Collapse 
starting_at: string
Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00
.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.starting_at)
bucket_width: optional "1m" or "1h" or "1d"
Time-bucket granularity. When set, each row's `starting_at` and `ending_at` are populated and one actor may span several rows (one per time bucket with usage). The time bucket counts toward `limit`, so one page can return multiple rows for the same actor. `ending_at` is required when `bucket_width` is set, and with `bucket_width="1m"` the range may span at most 24 hours. When omitted, each row aggregates the full `[starting_at, ending_at)` range.
"1m"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.bucket_width%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.bucket_width%5B1%5D)
"1d"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.bucket_width%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.bucket_width)
context_windows: optional array of "0-200k" or "200k-1M"
Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.
"0-200k"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.context_windows.items%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.context_windows.items%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.context_windows)
ending_at: optional string
End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.ending_at)
exclude_deleted_users: optional boolean
If true, omit rows for deleted accounts. Pages may return fewer than `limit` rows when deleted users were filtered.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.exclude_deleted_users)
group_by: optional array of "product" or "model" or "context_window" or 4 more
Break each actor's row out by the given dimensions. Accepts the same values as the bucketed `/cost_report` endpoint. The `product`, `model`, `context_window`, `inference_geo`, and `speed` dimensions — and the time bucket, when `bucket_width` is set — count toward `limit`. `cost_type` and `token_type` do not: `cost_type` returns one row per cost component (tokens, web search, code execution); `token_type` returns one row per token type, each with `cost_type: "tokens"`; combining both returns the per-token-type rows plus the web-search and code-execution rows. A page can therefore contain more rows than `limit` when `cost_type` or `token_type` is requested.
"product"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.group_by.items%5B0%5D)
"model"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.group_by.items%5B1%5D)
"context_window"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.group_by.items%5B2%5D)
"inference_geo"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.group_by.items%5B3%5D)
"speed"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.group_by.items%5B4%5D)
"cost_type"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.group_by.items%5B5%5D)
"token_type"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.group_by.items%5B6%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.group_by)
inference_geos: optional array of "global" or "us" or "not_available"
Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.
"global"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.inference_geos.items%5B0%5D)
"us"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.inference_geos.items%5B1%5D)
"not_available"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.inference_geos.items%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.inference_geos)
limit: optional number
Number of rows per page (1-1000, default 20). One row per actor unless `group_by[]` or `bucket_width` splits an actor across rows; `cost_type`/`token_type` fan-out rows (cost endpoint only) are the exception — they do not count toward this limit, so `data` can exceed it.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.limit)
models: optional array of string
Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.models)
order: optional "desc" or "asc"
Sort direction. Defaults to `desc`.
"desc"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.order%5B0%5D)
"asc"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.order%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.order)
order_by: optional "amount" or "list_amount"
Metric to rank actors by. Defaults to `amount`.
"amount"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.order_by%5B0%5D)
"list_amount"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.order_by%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.order_by)
page: optional string
Opaque cursor from a previous response's `next_page` field.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.page)
products: optional array of string
Product surfaces to include. Defaults to all products. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design".
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.products)
speeds: optional array of "fast" or "standard"
Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.
"fast"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.speeds.items%5B0%5D)
"standard"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.speeds.items%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.speeds)
user_ids: optional array of string
Filter to specific users by tagged user ID.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#list_by_user.user_ids)
UserCost object { data, data_refreshed_at, has_more, 2 more } 
data: array of object { actor, amount, context_window, 11 more } 
actor: [AnalyticsUserActor](https://platform.claude.com/docs/en/api/admin#analytics_user_actor) { user_id, deleted, email, 2 more } 
user_id: string
Tagged user ID.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.actor%20%2B%20\(resource\)%20admin.analytics.user_id)
deleted: optional boolean
True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.actor%20%2B%20\(resource\)%20admin.analytics.deleted)
email: optional string
The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.actor%20%2B%20\(resource\)%20admin.analytics.email)
name: optional string
The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.actor%20%2B%20\(resource\)%20admin.analytics.name)
type: optional "user_actor"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.actor%20%2B%20\(resource\)%20admin.analytics.type)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.actor)
amount: string
Amount (post-discount, pre-credit) in fractional cents (minor units).
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.amount)
context_window: "0-200k" or "200k-1M"
"0-200k"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.context_window%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.context_window%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.context_window)
cost_type: "tokens" or "web_search" or "code_execution"
Cost component breakdown; null when returning the combined total.
"tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.cost_type%5B0%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.cost_type%5B1%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.cost_type%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.cost_type)
currency: "USD"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.currency)
ending_at: string
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.ending_at)
inference_geo: "global" or "us"
"global"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.inference_geo%5B0%5D)
"us"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.inference_geo%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.inference_geo)
list_amount: string
List-price amount (pre-discount) in fractional cents.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.list_amount)
model: string
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.model)
product: string
Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.product)
requests: number
Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.requests)
speed: "fast" or "standard"
"fast"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.speed%5B0%5D)
"standard"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.speed)
starting_at: string
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.starting_at)
token_type: "uncached_input_tokens" or "output_tokens" or "cache_read_input_tokens" or 2 more
Token type when cost_type=tokens; null otherwise.
"uncached_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.token_type%5B0%5D)
"output_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.token_type%5B1%5D)
"cache_read_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.token_type%5B2%5D)
"cache_creation.ephemeral_1h_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.token_type%5B3%5D)
"cache_creation.ephemeral_5m_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.token_type%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data.items.token_type)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data)
data_refreshed_at: string
RFC 3339 timestamp of the export this response was served from. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.data_refreshed_at)
has_more: boolean
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.has_more)
next_page: string
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.next_page)
organization_id: string
ID of the Organization.
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost.organization_id)
[](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user#user_cost)
Get Per-User Cost

curl https://api.anthropic.com/v1/organizations/analytics/user_cost_report \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "actor": {
        "user_id": "user_01AbCdEfGhIjKlMnOpQrSt",
        "deleted": true,
        "email": "jane@example.com",
        "name": "Jane Smith",
        "type": "user_actor"
      "amount": "41280.000000",
      "context_window": "0-200k",
      "cost_type": "tokens",
      "currency": "USD",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "list_amount": "51600.000000",
      "model": "model",
      "product": "product",
      "requests": 128,
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "token_type": "uncached_input_tokens"
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"

  "data": [
      "actor": {
        "user_id": "user_01AbCdEfGhIjKlMnOpQrSt",
        "deleted": true,
        "email": "jane@example.com",
        "name": "Jane Smith",
        "type": "user_actor"
      "amount": "41280.000000",
      "context_window": "0-200k",
      "cost_type": "tokens",
      "currency": "USD",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "list_amount": "51600.000000",
      "model": "model",
      "product": "product",
      "requests": 128,
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "token_type": "uncached_input_tokens"
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
