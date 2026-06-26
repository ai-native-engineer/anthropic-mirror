<!-- source: https://platform.claude.com/docs/en/api/admin/analytics -->

# Analytics
##### [Get Activity Summaries](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries)
GET/v1/organizations/analytics/summaries
##### ModelsExpand Collapse 
ActivitySummary object { summaries } 
Response for GET /v1/organizations/analytics/summaries.
summaries: array of object { assigned_seat_count, cowork_daily_active_user_count, cowork_monthly_active_user_count, 10 more } 
assigned_seat_count: number
Number of seats currently assigned to members
[](https://platform.claude.com/docs/en/api/admin/analytics#activity_summary.summaries.items.assigned_seat_count)
cowork_daily_active_user_count: number
Number of users with Cowork activity on the requested day
[](https://platform.claude.com/docs/en/api/admin/analytics#activity_summary.summaries.items.cowork_daily_active_user_count)
cowork_monthly_active_user_count: number
Number of users with Cowork activity in the 30-day rolling window
[](https://platform.claude.com/docs/en/api/admin/analytics#activity_summary.summaries.items.cowork_monthly_active_user_count)
cowork_weekly_active_user_count: number
Number of users with Cowork activity in the 7-day rolling window
[](https://platform.claude.com/docs/en/api/admin/analytics#activity_summary.summaries.items.cowork_weekly_active_user_count)
daily_active_user_count: number
Number of users with token consumption on the requested day
[](https://platform.claude.com/docs/en/api/admin/analytics#activity_summary.summaries.items.daily_active_user_count)
daily_adoption_rate: number
Percentage of assigned seats with activity on the requested day (DAU / assigned_seat_count * 100)
[](https://platform.claude.com/docs/en/api/admin/analytics#activity_summary.summaries.items.daily_adoption_rate)
ending_at: string
End time in UTC of aggregation period (e.g. 2026-01-16T00:00
)
[](https://platform.claude.com/docs/en/api/admin/analytics#activity_summary.summaries.items.ending_at)
monthly_active_user_count: number
Number of users with token consumption in the 30-day rolling window
[](https://platform.claude.com/docs/en/api/admin/analytics#activity_summary.summaries.items.monthly_active_user_count)
monthly_adoption_rate: number
Percentage of assigned seats with activity in the 30-day rolling window (MAU / assigned_seat_count * 100)
[](https://platform.claude.com/docs/en/api/admin/analytics#activity_summary.summaries.items.monthly_adoption_rate)
pending_invite_count: number
Number of pending invitations to join the organization
[](https://platform.claude.com/docs/en/api/admin/analytics#activity_summary.summaries.items.pending_invite_count)
starting_at: string
Start time in UTC of aggregation period (e.g. 2026-01-15T00:00
)
[](https://platform.claude.com/docs/en/api/admin/analytics#activity_summary.summaries.items.starting_at)
weekly_active_user_count: number
Number of users with token consumption in the 7-day rolling window
[](https://platform.claude.com/docs/en/api/admin/analytics#activity_summary.summaries.items.weekly_active_user_count)
weekly_adoption_rate: number
Percentage of assigned seats with activity in the 7-day rolling window (WAU / assigned_seat_count * 100)
[](https://platform.claude.com/docs/en/api/admin/analytics#activity_summary.summaries.items.weekly_adoption_rate)
[](https://platform.claude.com/docs/en/api/admin/analytics#activity_summary.summaries)
[](https://platform.claude.com/docs/en/api/admin/analytics#activity_summary)
AnalyticsUser object { id, email_address } 
User identifier.
Tagged user identifier (e.g. user_...)
[](https://platform.claude.com/docs/en/api/admin/analytics#analytics_user.id)
email_address: string
Email address of the user
[](https://platform.claude.com/docs/en/api/admin/analytics#analytics_user.email_address)
[](https://platform.claude.com/docs/en/api/admin/analytics#analytics_user)
AnalyticsUserActor object { user_id, deleted, email, 2 more } 
user_id: string
Tagged user ID.
[](https://platform.claude.com/docs/en/api/admin/analytics#analytics_user_actor.user_id)
deleted: optional boolean
True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.
[](https://platform.claude.com/docs/en/api/admin/analytics#analytics_user_actor.deleted)
email: optional string
The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).
[](https://platform.claude.com/docs/en/api/admin/analytics#analytics_user_actor.email)
name: optional string
The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.
[](https://platform.claude.com/docs/en/api/admin/analytics#analytics_user_actor.name)
type: optional "user_actor"
[](https://platform.claude.com/docs/en/api/admin/analytics#analytics_user_actor.type)
[](https://platform.claude.com/docs/en/api/admin/analytics#analytics_user_actor)
ConnectorOfficeProductMetrics object { distinct_session_connector_used_count } 
Office Agent activity metrics for a single connector on a given day within one Office product.
distinct_session_connector_used_count: number
Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_office_product_metrics.distinct_session_connector_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_office_product_metrics)
OfficeProductMetrics object { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more } 
Office Agent activity metrics for a single user on a given day within one Office product.
connectors_used_count: number
Number of MCP connector invocations
[](https://platform.claude.com/docs/en/api/admin/analytics#office_product_metrics.connectors_used_count)
distinct_connectors_used_count: number
Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#office_product_metrics.distinct_connectors_used_count)
distinct_session_count: number
Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#office_product_metrics.distinct_session_count)
distinct_skills_used_count: number
Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#office_product_metrics.distinct_skills_used_count)
message_count: number
Number of messages sent
[](https://platform.claude.com/docs/en/api/admin/analytics#office_product_metrics.message_count)
skills_used_count: number
Number of skill invocations
[](https://platform.claude.com/docs/en/api/admin/analytics#office_product_metrics.skills_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#office_product_metrics)
SkillOfficeProductMetrics object { distinct_session_skill_used_count } 
Office Agent activity metrics for a single skill on a given day within one Office product.
distinct_session_skill_used_count: number
Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_office_product_metrics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_office_product_metrics)
ToolActionCounts object { accepted_count, rejected_count } 
Accepted/rejected counts for a single Claude Code tool type.
accepted_count: number
Number of tool proposals accepted
[](https://platform.claude.com/docs/en/api/admin/analytics#tool_action_counts.accepted_count)
rejected_count: number
Number of tool proposals rejected
[](https://platform.claude.com/docs/en/api/admin/analytics#tool_action_counts.rejected_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#tool_action_counts)
####  AnalyticsUsage
##### [Get Token Usage Over Time](https://platform.claude.com/docs/en/api/admin/analytics/usage/list)
GET/v1/organizations/analytics/usage_report
##### [Get Per-User Token Usage](https://platform.claude.com/docs/en/api/admin/analytics/usage/list_by_user)
GET/v1/organizations/analytics/user_usage_report
##### ModelsExpand Collapse 
UsageBucket object { data, data_refreshed_at, has_more, 2 more } 
data: array of object { ending_at, results, starting_at } 
ending_at: string
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.ending_at)
results: array of object { cache_creation, cache_read_input_tokens, context_window, 8 more } 
cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
ephemeral_1h_input_tokens: number
The number of input tokens used to create the 1 hour cache entry.
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.cache_creation.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: number
The number of input tokens used to create the 5 minute cache entry.
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.cache_creation.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.cache_creation)
cache_read_input_tokens: number
The number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.cache_read_input_tokens)
context_window: "0-200k" or "200k-1M"
"0-200k"
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.context_window%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.context_window%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.context_window)
inference_geo: "global" or "us"
"global"
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.inference_geo%5B0%5D)
"us"
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.inference_geo%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.inference_geo)
model: string
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.model)
output_tokens: number
The number of output tokens generated.
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.output_tokens)
product: string
Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.product)
requests: number
Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.requests)
server_tool_use: object { web_search_requests } 
web_search_requests: number
The number of web search requests made.
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.server_tool_use.web_search_requests)
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.server_tool_use)
speed: "fast" or "standard"
"fast"
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.speed%5B0%5D)
"standard"
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.speed)
uncached_input_tokens: number
The number of uncached input tokens processed.
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results.items.uncached_input_tokens)
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.results)
starting_at: string
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data.items.starting_at)
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data)
data_refreshed_at: string
RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.data_refreshed_at)
has_more: boolean
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.has_more)
next_page: string
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.next_page)
organization_id: string
ID of the Organization.
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket.organization_id)
[](https://platform.claude.com/docs/en/api/admin/analytics#usage_bucket)
UserUsage object { data, data_refreshed_at, has_more, 2 more } 
data: array of object { actor, cache_creation, cache_read_input_tokens, 12 more } 
actor: [AnalyticsUserActor](https://platform.claude.com/docs/en/api/admin#analytics_user_actor) { user_id, deleted, email, 2 more } 
user_id: string
Tagged user ID.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.actor%20%2B%20\(resource\)%20admin.analytics.user_id)
deleted: optional boolean
True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.actor%20%2B%20\(resource\)%20admin.analytics.deleted)
email: optional string
The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.actor%20%2B%20\(resource\)%20admin.analytics.email)
name: optional string
The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.actor%20%2B%20\(resource\)%20admin.analytics.name)
type: optional "user_actor"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.actor%20%2B%20\(resource\)%20admin.analytics.type)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.actor)
cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
ephemeral_1h_input_tokens: number
The number of input tokens used to create the 1 hour cache entry.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.cache_creation.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: number
The number of input tokens used to create the 5 minute cache entry.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.cache_creation.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.cache_creation)
cache_read_input_tokens: number
The number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.cache_read_input_tokens)
context_window: "0-200k" or "200k-1M"
"0-200k"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.context_window%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.context_window%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.context_window)
ending_at: string
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.ending_at)
inference_geo: "global" or "us"
"global"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.inference_geo%5B0%5D)
"us"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.inference_geo%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.inference_geo)
model: string
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.model)
output_tokens: number
The number of output tokens generated.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.output_tokens)
product: string
Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.product)
requests: number
Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.requests)
server_tool_use: object { web_search_requests } 
web_search_requests: number
The number of web search requests made.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.server_tool_use.web_search_requests)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.server_tool_use)
speed: "fast" or "standard"
"fast"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.speed%5B0%5D)
"standard"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.speed)
starting_at: string
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.starting_at)
total_tokens: number
Total token count across all token types. This is the value the default order_by='total_tokens' sorts on.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.total_tokens)
uncached_input_tokens: number
The number of uncached input tokens processed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data.items.uncached_input_tokens)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data)
data_refreshed_at: string
RFC 3339 timestamp of the export this response was served from. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.data_refreshed_at)
has_more: boolean
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.has_more)
next_page: string
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.next_page)
organization_id: string
ID of the Organization.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage.organization_id)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_usage)
####  AnalyticsCost
##### [Get Cost Over Time](https://platform.claude.com/docs/en/api/admin/analytics/cost/list)
GET/v1/organizations/analytics/cost_report
##### [Get Per-User Cost](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user)
GET/v1/organizations/analytics/user_cost_report
##### ModelsExpand Collapse 
CostBucket object { data, data_refreshed_at, has_more, 2 more } 
data: array of object { ending_at, results, starting_at } 
ending_at: string
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.ending_at)
results: array of object { amount, context_window, cost_type, 8 more } 
amount: string
Amount (post-discount, pre-credit) in fractional cents.
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.amount)
context_window: "0-200k" or "200k-1M"
"0-200k"
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.context_window%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.context_window%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.context_window)
cost_type: "tokens" or "web_search" or "code_execution"
Cost component when `group_by[]=cost_type`; null otherwise (amount is the combined total).
"tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.cost_type%5B0%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.cost_type%5B1%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.cost_type%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.cost_type)
currency: "USD"
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.currency)
inference_geo: "global" or "us"
"global"
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.inference_geo%5B0%5D)
"us"
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.inference_geo%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.inference_geo)
list_amount: string
List-price amount (pre-discount) in fractional cents.
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.list_amount)
model: string
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.model)
product: string
Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.product)
requests: number
Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.requests)
speed: "fast" or "standard"
"fast"
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.speed%5B0%5D)
"standard"
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.speed)
token_type: "uncached_input_tokens" or "output_tokens" or "cache_read_input_tokens" or 2 more
Token type when `group_by[]=token_type` and `cost_type=tokens`; null otherwise.
"uncached_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.token_type%5B0%5D)
"output_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.token_type%5B1%5D)
"cache_read_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.token_type%5B2%5D)
"cache_creation.ephemeral_1h_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.token_type%5B3%5D)
"cache_creation.ephemeral_5m_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.token_type%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results.items.token_type)
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.results)
starting_at: string
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data.items.starting_at)
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data)
data_refreshed_at: string
RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.data_refreshed_at)
has_more: boolean
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.has_more)
next_page: string
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.next_page)
organization_id: string
ID of the Organization.
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket.organization_id)
[](https://platform.claude.com/docs/en/api/admin/analytics#cost_bucket)
UserCost object { data, data_refreshed_at, has_more, 2 more } 
data: array of object { actor, amount, context_window, 11 more } 
actor: [AnalyticsUserActor](https://platform.claude.com/docs/en/api/admin#analytics_user_actor) { user_id, deleted, email, 2 more } 
user_id: string
Tagged user ID.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.actor%20%2B%20\(resource\)%20admin.analytics.user_id)
deleted: optional boolean
True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.actor%20%2B%20\(resource\)%20admin.analytics.deleted)
email: optional string
The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.actor%20%2B%20\(resource\)%20admin.analytics.email)
name: optional string
The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.actor%20%2B%20\(resource\)%20admin.analytics.name)
type: optional "user_actor"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.actor%20%2B%20\(resource\)%20admin.analytics.type)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.actor)
amount: string
Amount (post-discount, pre-credit) in fractional cents (minor units).
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.amount)
context_window: "0-200k" or "200k-1M"
"0-200k"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.context_window%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.context_window%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.context_window)
cost_type: "tokens" or "web_search" or "code_execution"
Cost component breakdown; null when returning the combined total.
"tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.cost_type%5B0%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.cost_type%5B1%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.cost_type%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.cost_type)
currency: "USD"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.currency)
ending_at: string
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.ending_at)
inference_geo: "global" or "us"
"global"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.inference_geo%5B0%5D)
"us"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.inference_geo%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.inference_geo)
list_amount: string
List-price amount (pre-discount) in fractional cents.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.list_amount)
model: string
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.model)
product: string
Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.product)
requests: number
Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.requests)
speed: "fast" or "standard"
"fast"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.speed%5B0%5D)
"standard"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.speed)
starting_at: string
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.starting_at)
token_type: "uncached_input_tokens" or "output_tokens" or "cache_read_input_tokens" or 2 more
Token type when cost_type=tokens; null otherwise.
"uncached_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.token_type%5B0%5D)
"output_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.token_type%5B1%5D)
"cache_read_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.token_type%5B2%5D)
"cache_creation.ephemeral_1h_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.token_type%5B3%5D)
"cache_creation.ephemeral_5m_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.token_type%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data.items.token_type)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data)
data_refreshed_at: string
RFC 3339 timestamp of the export this response was served from. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.data_refreshed_at)
has_more: boolean
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.has_more)
next_page: string
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.next_page)
organization_id: string
ID of the Organization.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost.organization_id)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_cost)
####  AnalyticsUsers
##### [List User Activity](https://platform.claude.com/docs/en/api/admin/analytics/users/list)
GET/v1/organizations/analytics/users
##### ModelsExpand Collapse 
UserActivity object { data, next_page } 
Response for GET /v1/organizations/analytics/users.
data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 4 more } 
chat_metrics: object { connectors_used_count, distinct_artifacts_created_count, distinct_conversation_count, 8 more } 
Claude.ai activity metrics for a single user on a given day.
connectors_used_count: number
Number of MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.chat_metrics.connectors_used_count)
distinct_artifacts_created_count: number
Number of distinct artifacts created
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.chat_metrics.distinct_artifacts_created_count)
distinct_conversation_count: number
Number of distinct conversations the user participated in. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.chat_metrics.distinct_conversation_count)
distinct_files_uploaded_count: number
Number of distinct files uploaded. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.chat_metrics.distinct_files_uploaded_count)
distinct_projects_created_count: number
Number of distinct projects created
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.chat_metrics.distinct_projects_created_count)
distinct_projects_used_count: number
Number of distinct projects used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.chat_metrics.distinct_projects_used_count)
distinct_shared_artifacts_viewed_count: number
Number of distinct shared artifacts the user viewed. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.chat_metrics.distinct_shared_artifacts_viewed_count)
distinct_skills_used_count: number
Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.chat_metrics.distinct_skills_used_count)
message_count: number
Number of messages sent
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.chat_metrics.message_count)
shared_conversations_viewed_count: number
Number of times the user opened a shared conversation in a project
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.chat_metrics.shared_conversations_viewed_count)
thinking_message_count: number
Number of messages that used extended thinking
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.chat_metrics.thinking_message_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.chat_metrics)
claude_code_metrics: object { core_metrics, tool_actions } 
Claude Code activity metrics for a single user on a given day.
core_metrics: object { commit_count, distinct_session_count, lines_of_code, pull_request_count } 
Core Claude Code activity metrics for a single user on a given day.
commit_count: number
Number of commits made via Claude Code
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.core_metrics.commit_count)
distinct_session_count: number
Number of distinct Claude Code sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.core_metrics.distinct_session_count)
lines_of_code: object { added_count, removed_count } 
Lines of code added and removed via Claude Code.
added_count: number
Lines of code added
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.core_metrics.lines_of_code.added_count)
removed_count: number
Lines of code removed
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.core_metrics.lines_of_code.removed_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.core_metrics.lines_of_code)
pull_request_count: number
Number of pull requests created via Claude Code
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.core_metrics.pull_request_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.core_metrics)
tool_actions: object { edit_tool, multi_edit_tool, notebook_edit_tool, write_tool } 
Per-tool accepted/rejected counts for Claude Code file modification tools.
edit_tool: [ToolActionCounts](https://platform.claude.com/docs/en/api/admin#tool_action_counts) { accepted_count, rejected_count } 
Accepted/rejected counts for a single Claude Code tool type.
accepted_count: number
Number of tool proposals accepted
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.tool_actions.edit_tool%20%2B%20\(resource\)%20admin.analytics.accepted_count)
rejected_count: number
Number of tool proposals rejected
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.tool_actions.edit_tool%20%2B%20\(resource\)%20admin.analytics.rejected_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.tool_actions.edit_tool)
multi_edit_tool: [ToolActionCounts](https://platform.claude.com/docs/en/api/admin#tool_action_counts) { accepted_count, rejected_count } 
Accepted/rejected counts for a single Claude Code tool type.
accepted_count: number
Number of tool proposals accepted
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.tool_actions.multi_edit_tool%20%2B%20\(resource\)%20admin.analytics.accepted_count)
rejected_count: number
Number of tool proposals rejected
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.tool_actions.multi_edit_tool%20%2B%20\(resource\)%20admin.analytics.rejected_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.tool_actions.multi_edit_tool)
notebook_edit_tool: [ToolActionCounts](https://platform.claude.com/docs/en/api/admin#tool_action_counts) { accepted_count, rejected_count } 
Accepted/rejected counts for a single Claude Code tool type.
accepted_count: number
Number of tool proposals accepted
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.tool_actions.notebook_edit_tool%20%2B%20\(resource\)%20admin.analytics.accepted_count)
rejected_count: number
Number of tool proposals rejected
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.tool_actions.notebook_edit_tool%20%2B%20\(resource\)%20admin.analytics.rejected_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.tool_actions.notebook_edit_tool)
write_tool: [ToolActionCounts](https://platform.claude.com/docs/en/api/admin#tool_action_counts) { accepted_count, rejected_count } 
Accepted/rejected counts for a single Claude Code tool type.
accepted_count: number
Number of tool proposals accepted
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.tool_actions.write_tool%20%2B%20\(resource\)%20admin.analytics.accepted_count)
rejected_count: number
Number of tool proposals rejected
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.tool_actions.write_tool%20%2B%20\(resource\)%20admin.analytics.rejected_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.tool_actions.write_tool)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics.tool_actions)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.claude_code_metrics)
cowork_metrics: object { action_count, connectors_used_count, dispatch_turn_count, 5 more } 
Cowork activity metrics for a single user on a given day.
action_count: number
Number of tool actions completed in Cowork sessions
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.cowork_metrics.action_count)
connectors_used_count: number
Total number of connector invocations in Cowork sessions
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.cowork_metrics.connectors_used_count)
dispatch_turn_count: number
Number of Dispatch (background agent) turns completed
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.cowork_metrics.dispatch_turn_count)
distinct_connectors_used_count: number
Number of distinct connectors used in Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.cowork_metrics.distinct_connectors_used_count)
distinct_session_count: number
Number of distinct Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.cowork_metrics.distinct_session_count)
distinct_skills_used_count: number
Number of distinct skills used in Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.cowork_metrics.distinct_skills_used_count)
message_count: number
Number of messages sent in Cowork sessions
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.cowork_metrics.message_count)
skills_used_count: number
Total number of skill invocations in Cowork sessions
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.cowork_metrics.skills_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.cowork_metrics)
design_metrics: object { distinct_projects_created_count, distinct_projects_used_count, distinct_session_count, message_count } 
Claude Design activity metrics for a single user on a given day.
distinct_projects_created_count: number
Number of distinct Claude Design projects created
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.design_metrics.distinct_projects_created_count)
distinct_projects_used_count: number
Number of distinct Claude Design projects the user worked in. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.design_metrics.distinct_projects_used_count)
distinct_session_count: number
Number of distinct Claude Design sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.design_metrics.distinct_session_count)
message_count: number
Number of messages sent in Claude Design sessions
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.design_metrics.message_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.design_metrics)
office_metrics: object { excel, outlook, powerpoint, word } 
Office Agent activity metrics for a single user on a given day, broken out by Office product.
excel: [OfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#office_product_metrics) { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more } 
Office Agent activity metrics for a single user on a given day within one Office product.
connectors_used_count: number
Number of MCP connector invocations
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.connectors_used_count)
distinct_connectors_used_count: number
Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.distinct_connectors_used_count)
distinct_session_count: number
Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.distinct_session_count)
distinct_skills_used_count: number
Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.distinct_skills_used_count)
message_count: number
Number of messages sent
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.message_count)
skills_used_count: number
Number of skill invocations
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.skills_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.excel)
outlook: [OfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#office_product_metrics) { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more } 
Office Agent activity metrics for a single user on a given day within one Office product.
connectors_used_count: number
Number of MCP connector invocations
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.connectors_used_count)
distinct_connectors_used_count: number
Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.distinct_connectors_used_count)
distinct_session_count: number
Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.distinct_session_count)
distinct_skills_used_count: number
Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.distinct_skills_used_count)
message_count: number
Number of messages sent
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.message_count)
skills_used_count: number
Number of skill invocations
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.skills_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.outlook)
powerpoint: [OfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#office_product_metrics) { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more } 
Office Agent activity metrics for a single user on a given day within one Office product.
connectors_used_count: number
Number of MCP connector invocations
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.connectors_used_count)
distinct_connectors_used_count: number
Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.distinct_connectors_used_count)
distinct_session_count: number
Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.distinct_session_count)
distinct_skills_used_count: number
Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.distinct_skills_used_count)
message_count: number
Number of messages sent
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.message_count)
skills_used_count: number
Number of skill invocations
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.skills_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.powerpoint)
word: [OfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#office_product_metrics) { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more } 
Office Agent activity metrics for a single user on a given day within one Office product.
connectors_used_count: number
Number of MCP connector invocations
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.connectors_used_count)
distinct_connectors_used_count: number
Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.distinct_connectors_used_count)
distinct_session_count: number
Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.distinct_session_count)
distinct_skills_used_count: number
Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.distinct_skills_used_count)
message_count: number
Number of messages sent
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.message_count)
skills_used_count: number
Number of skill invocations
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.skills_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics.word)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.office_metrics)
web_search_count: number
Number of web searches performed
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.web_search_count)
user: optional [AnalyticsUser](https://platform.claude.com/docs/en/api/admin#analytics_user) { id, email_address } 
User identifier.
Tagged user identifier (e.g. user_...)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.user%20%2B%20\(resource\)%20admin.analytics.id)
email_address: string
Email address of the user
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.user%20%2B%20\(resource\)%20admin.analytics.email_address)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data.items.user)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.data)
next_page: string
Opaque cursor for the next page, or null if no more results
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity.next_page)
[](https://platform.claude.com/docs/en/api/admin/analytics#user_activity)
####  AnalyticsSkills
##### [Get Skill Usage](https://platform.claude.com/docs/en/api/admin/analytics/skills/list)
GET/v1/organizations/analytics/skills
##### ModelsExpand Collapse 
SkillUsage object { data, next_page } 
Response for GET /v1/organizations/analytics/skills.
data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 3 more } 
chat_metrics: object { distinct_conversation_skill_used_count } 
Claude.ai activity metrics for a single skill on a given day.
distinct_conversation_skill_used_count: number
Number of distinct conversations in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data.items.chat_metrics.distinct_conversation_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data.items.chat_metrics)
claude_code_metrics: object { distinct_session_skill_used_count } 
Claude Code activity metrics for a single skill on a given day.
distinct_session_skill_used_count: number
Number of distinct Claude Code sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data.items.claude_code_metrics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data.items.claude_code_metrics)
cowork_metrics: object { distinct_session_skill_used_count } 
Cowork activity metrics for a single skill on a given day.
distinct_session_skill_used_count: number
Number of distinct Cowork sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data.items.cowork_metrics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data.items.cowork_metrics)
distinct_user_count: number
Number of distinct users who used the skill on the requested day
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data.items.distinct_user_count)
office_metrics: object { excel, outlook, powerpoint, word } 
Office Agent activity metrics for a single skill on a given day, broken out by Office product.
excel: [SkillOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#skill_office_product_metrics) { distinct_session_skill_used_count } 
Office Agent activity metrics for a single skill on a given day within one Office product.
distinct_session_skill_used_count: number
Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data.items.office_metrics.excel)
outlook: [SkillOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#skill_office_product_metrics) { distinct_session_skill_used_count } 
Office Agent activity metrics for a single skill on a given day within one Office product.
distinct_session_skill_used_count: number
Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data.items.office_metrics.outlook)
powerpoint: [SkillOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#skill_office_product_metrics) { distinct_session_skill_used_count } 
Office Agent activity metrics for a single skill on a given day within one Office product.
distinct_session_skill_used_count: number
Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data.items.office_metrics.powerpoint)
word: [SkillOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#skill_office_product_metrics) { distinct_session_skill_used_count } 
Office Agent activity metrics for a single skill on a given day within one Office product.
distinct_session_skill_used_count: number
Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data.items.office_metrics.word)
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data.items.office_metrics)
skill_name: string
Name of the skill
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data.items.skill_name)
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.data)
next_page: string
Opaque cursor for the next page, or null if no more results
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage.next_page)
[](https://platform.claude.com/docs/en/api/admin/analytics#skill_usage)
####  AnalyticsConnectors
##### [Get Connector Usage](https://platform.claude.com/docs/en/api/admin/analytics/connectors/list)
GET/v1/organizations/analytics/connectors
##### ModelsExpand Collapse 
ConnectorUsage object { data, next_page } 
Response for GET /v1/organizations/analytics/connectors.
data: array of object { chat_metrics, claude_code_metrics, connector_name, 3 more } 
chat_metrics: object { distinct_conversation_connector_used_count } 
Claude.ai activity metrics for a single connector on a given day.
distinct_conversation_connector_used_count: number
Number of distinct conversations in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data.items.chat_metrics.distinct_conversation_connector_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data.items.chat_metrics)
claude_code_metrics: object { distinct_session_connector_used_count } 
Claude Code activity metrics for a single connector on a given day.
distinct_session_connector_used_count: number
Number of distinct Claude Code sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data.items.claude_code_metrics.distinct_session_connector_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data.items.claude_code_metrics)
connector_name: string
Name of the connector
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data.items.connector_name)
cowork_metrics: object { distinct_session_connector_used_count } 
Cowork activity metrics for a single connector on a given day.
distinct_session_connector_used_count: number
Number of distinct Cowork sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data.items.cowork_metrics.distinct_session_connector_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data.items.cowork_metrics)
distinct_user_count: number
Number of distinct users who used the connector on the requested day
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data.items.distinct_user_count)
office_metrics: object { excel, outlook, powerpoint, word } 
Office Agent activity metrics for a single connector on a given day, broken out by Office product.
excel: [ConnectorOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#connector_office_product_metrics) { distinct_session_connector_used_count } 
Office Agent activity metrics for a single connector on a given day within one Office product.
distinct_session_connector_used_count: number
Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.distinct_session_connector_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data.items.office_metrics.excel)
outlook: [ConnectorOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#connector_office_product_metrics) { distinct_session_connector_used_count } 
Office Agent activity metrics for a single connector on a given day within one Office product.
distinct_session_connector_used_count: number
Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.distinct_session_connector_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data.items.office_metrics.outlook)
powerpoint: [ConnectorOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#connector_office_product_metrics) { distinct_session_connector_used_count } 
Office Agent activity metrics for a single connector on a given day within one Office product.
distinct_session_connector_used_count: number
Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.distinct_session_connector_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data.items.office_metrics.powerpoint)
word: [ConnectorOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#connector_office_product_metrics) { distinct_session_connector_used_count } 
Office Agent activity metrics for a single connector on a given day within one Office product.
distinct_session_connector_used_count: number
Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.distinct_session_connector_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data.items.office_metrics.word)
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data.items.office_metrics)
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.data)
next_page: string
Opaque cursor for the next page, or null if no more results
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage.next_page)
[](https://platform.claude.com/docs/en/api/admin/analytics#connector_usage)
####  AnalyticsChat Projects
##### [Get Chat Project Usage](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list)
GET/v1/organizations/analytics/apps/chat/projects
##### ModelsExpand Collapse 
ChatProjectUsage object { data, next_page } 
Response for GET /v1/organizations/analytics/apps/chat/projects.
data: array of object { distinct_conversation_count, distinct_user_count, message_count, 4 more } 
distinct_conversation_count: number
Number of distinct conversations in the project on the requested day
[](https://platform.claude.com/docs/en/api/admin/analytics#chat_project_usage.data.items.distinct_conversation_count)
distinct_user_count: number
Number of distinct users who used the project on the requested day
[](https://platform.claude.com/docs/en/api/admin/analytics#chat_project_usage.data.items.distinct_user_count)
message_count: number
Number of messages sent in the project on the requested day
[](https://platform.claude.com/docs/en/api/admin/analytics#chat_project_usage.data.items.message_count)
project_id: string
Tagged project identifier (e.g. claude_proj_...)
[](https://platform.claude.com/docs/en/api/admin/analytics#chat_project_usage.data.items.project_id)
project_name: string
Name of the project
[](https://platform.claude.com/docs/en/api/admin/analytics#chat_project_usage.data.items.project_name)
created_at: optional string
Project creation timestamp, RFC 3339. Null if the project was deleted before attribution was recorded.
[](https://platform.claude.com/docs/en/api/admin/analytics#chat_project_usage.data.items.created_at)
created_by: optional [AnalyticsUser](https://platform.claude.com/docs/en/api/admin#analytics_user) { id, email_address } 
User identifier.
Tagged user identifier (e.g. user_...)
[](https://platform.claude.com/docs/en/api/admin/analytics#chat_project_usage.data.items.created_by%20%2B%20\(resource\)%20admin.analytics.id)
email_address: string
Email address of the user
[](https://platform.claude.com/docs/en/api/admin/analytics#chat_project_usage.data.items.created_by%20%2B%20\(resource\)%20admin.analytics.email_address)
[](https://platform.claude.com/docs/en/api/admin/analytics#chat_project_usage.data.items.created_by)
[](https://platform.claude.com/docs/en/api/admin/analytics#chat_project_usage.data)
next_page: string
Opaque cursor for the next page, or null if no more results
[](https://platform.claude.com/docs/en/api/admin/analytics#chat_project_usage.next_page)
[](https://platform.claude.com/docs/en/api/admin/analytics#chat_project_usage)
