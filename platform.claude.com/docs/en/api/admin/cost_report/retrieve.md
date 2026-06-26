<!-- source: https://platform.claude.com/docs/en/api/admin/cost_report/retrieve -->

# Get Cost Report
GET/v1/organizations/cost_report
Get Cost Report
##### Query ParametersExpand Collapse 
starting_at: string
Time buckets that start on or after this RFC 3339 timestamp will be returned. Each time bucket will be snapped to the start of the minute/hour/day in UTC.
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#retrieve.starting_at)
bucket_width: optional "1d"
Time granularity of the response data.
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#retrieve.bucket_width)
ending_at: optional string
Time buckets that end before this RFC 3339 timestamp will be returned.
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#retrieve.ending_at)
group_by: optional array of "workspace_id" or "description"
Group by any subset of the available options.
"workspace_id"
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#retrieve.group_by.items%5B0%5D)
"description"
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#retrieve.group_by.items%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#retrieve.group_by)
limit: optional number
Maximum number of time buckets to return in the response.
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#retrieve.limit)
page: optional string
Optionally set to the `next_page` token from the previous response.
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#retrieve.page)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of string
Optional header to specify the beta version(s) you want to use.
To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#retrieve.anthropic-beta)
CostReport object { data, has_more, next_page } 
data: array of object { ending_at, results, starting_at } 
ending_at: string
End of the time bucket (exclusive) in RFC 3339 format.
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.ending_at)
results: array of object { amount, context_window, cost_type, 7 more } 
List of cost items for this time bucket. There may be multiple items if one or more `group_by[]` parameters are specified.
amount: string
Cost amount in lowest currency units (e.g. cents) as a decimal string. For example, `"123.45"` in `"USD"` represents `$1.23`.
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.amount)
context_window: "0-200k" or "200k-1M"
Input context window used. `null` if not grouping by description or for non-token costs.
"0-200k"
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.context_window%5B0%5D)
"200k-1M"
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.context_window%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.context_window)
cost_type: "tokens" or "web_search" or "code_execution" or "session_usage"
Type of cost. `null` if not grouping by description.
"tokens"
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.cost_type%5B0%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.cost_type%5B1%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.cost_type%5B2%5D)
"session_usage"
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.cost_type%5B3%5D)
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.cost_type)
currency: string
Currency code for the cost amount. Currently always `"USD"`.
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.currency)
description: string
Description of the cost item. `null` if not grouping by description.
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.description)
inference_geo: string
Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`. For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.inference_geo)
model: string
Model name used. `null` if not grouping by description or for non-token costs.
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.model)
service_tier: "standard" or "batch"
Service tier used. `null` if not grouping by description or for non-token costs.
"standard"
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.service_tier%5B0%5D)
"batch"
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.service_tier%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.service_tier)
token_type: "uncached_input_tokens" or "output_tokens" or "cache_read_input_tokens" or 2 more
Type of token. `null` if not grouping by description or for non-token costs.
"uncached_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.token_type%5B0%5D)
"output_tokens"
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.token_type%5B1%5D)
"cache_read_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.token_type%5B2%5D)
"cache_creation.ephemeral_1h_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.token_type%5B3%5D)
"cache_creation.ephemeral_5m_input_tokens"
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.token_type%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.token_type)
workspace_id: string
ID of the Workspace this cost is associated with. `null` if not grouping by workspace or for the default workspace.
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results.items.workspace_id)
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.results)
starting_at: string
Start of the time bucket (inclusive) in RFC 3339 format.
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data.items.starting_at)
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.data)
has_more: boolean
Indicates if there are more results.
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.has_more)
next_page: string
Token to provide in as `page` in the subsequent request to retrieve the next page of data.
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report.next_page)
[](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve#cost_report)
Get Cost Report

curl https://api.anthropic.com/v1/organizations/cost_report \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "ending_at": "2025-08-02T00:00:00Z",
      "results": [
          "amount": "123.78912",
          "context_window": "0-200k",
          "cost_type": "tokens",
          "currency": "USD",
          "description": "Claude Sonnet 4 Usage - Input Tokens",
          "inference_geo": "global",
          "model": "claude-opus-4-6",
          "service_tier": "standard",
          "token_type": "uncached_input_tokens",
          "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
      ],
      "starting_at": "2025-08-01T00:00:00Z"
  ],
  "has_more": true,
  "next_page": "2019-12-27T18:11:19.117Z"

  "data": [
      "ending_at": "2025-08-02T00:00:00Z",
      "results": [
          "amount": "123.78912",
          "context_window": "0-200k",
          "cost_type": "tokens",
          "currency": "USD",
          "description": "Claude Sonnet 4 Usage - Input Tokens",
          "inference_geo": "global",
          "model": "claude-opus-4-6",
          "service_tier": "standard",
          "token_type": "uncached_input_tokens",
          "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
      ],
      "starting_at": "2025-08-01T00:00:00Z"
  ],
  "has_more": true,
  "next_page": "2019-12-27T18:11:19.117Z"
