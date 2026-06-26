<!-- source: https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code -->

# Get Claude Code Usage Report
GET/v1/organizations/usage_report/claude_code
Retrieve daily aggregated usage metrics for Claude Code users. Enables organizations to analyze developer productivity and build custom dashboards.
##### Query ParametersExpand Collapse 
starting_at: string
UTC date in YYYY-MM-DD format. Returns metrics for this single day only.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#retrieve_claude_code.starting_at)
limit: optional number
Number of records per page (default: 20, max: 1000).
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#retrieve_claude_code.limit)
page: optional string
Opaque cursor token from previous response's `next_page` field.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#retrieve_claude_code.page)
ClaudeCodeUsageReport object { data, has_more, next_page } 
data: array of object { actor, core_metrics, customer_type, 6 more } 
List of Claude Code usage records for the requested date.
actor: object { email_address, type }  or object { api_key_name, type } 
The user or API key that performed the Claude Code actions.
UserActor object { email_address, type } 
email_address: string
Email address of the user who performed Claude Code actions.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.actor%5B0%5D.email_address)
type: "user_actor"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.actor%5B0%5D.type)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.actor%5B0%5D)
APIActor object { api_key_name, type } 
api_key_name: string
Name of the API key used to perform Claude Code actions.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.actor%5B1%5D.api_key_name)
type: "api_actor"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.actor%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.actor%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.actor)
core_metrics: object { commits_by_claude_code, lines_of_code, num_sessions, pull_requests_by_claude_code } 
Core productivity metrics measuring Claude Code usage and impact.
commits_by_claude_code: number
Number of git commits created through Claude Code's commit functionality.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.core_metrics.commits_by_claude_code)
lines_of_code: object { added, removed } 
Statistics on code changes made through Claude Code.
added: number
Total number of lines of code added across all files by Claude Code.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.core_metrics.lines_of_code.added)
removed: number
Total number of lines of code removed across all files by Claude Code.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.core_metrics.lines_of_code.removed)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.core_metrics.lines_of_code)
num_sessions: number
Number of distinct Claude Code sessions initiated by this actor.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.core_metrics.num_sessions)
pull_requests_by_claude_code: number
Number of pull requests created through Claude Code's PR functionality.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.core_metrics.pull_requests_by_claude_code)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.core_metrics)
customer_type: "api" or "subscription"
Type of customer account (api for API customers, subscription for Pro/Team customers).
"api"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.customer_type%5B0%5D)
"subscription"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.customer_type%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.customer_type)
date: string
UTC date for the usage metrics in YYYY-MM-DD format.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.date)
model_breakdown: array of object { estimated_cost, model, tokens } 
Token usage and cost breakdown by AI model used.
estimated_cost: object { amount, currency } 
Estimated cost for using this model
amount: number
Estimated cost amount in minor currency units (e.g., cents for USD).
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.model_breakdown.items.estimated_cost.amount)
currency: string
Currency code for the estimated cost (e.g., 'USD').
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.model_breakdown.items.estimated_cost.currency)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.model_breakdown.items.estimated_cost)
model: string
Name of the AI model used for Claude Code interactions.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.model_breakdown.items.model)
tokens: object { cache_creation, cache_read, input, output } 
Token usage breakdown for this model
cache_creation: number
Number of cache creation tokens consumed by this model.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.model_breakdown.items.tokens.cache_creation)
cache_read: number
Number of cache read tokens consumed by this model.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.model_breakdown.items.tokens.cache_read)
input: number
Number of input tokens consumed by this model.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.model_breakdown.items.tokens.input)
output: number
Number of output tokens generated by this model.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.model_breakdown.items.tokens.output)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.model_breakdown.items.tokens)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.model_breakdown)
organization_id: string
ID of the organization that owns the Claude Code usage.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.organization_id)
terminal_type: string
Type of terminal or environment where Claude Code was used.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.terminal_type)
tool_actions: map[object { accepted, rejected } ]
Breakdown of tool action acceptance and rejection rates by tool type.
accepted: number
Number of tool action proposals that the user accepted.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.tool_actions.items.accepted)
rejected: number
Number of tool action proposals that the user rejected.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.tool_actions.items.rejected)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.tool_actions)
subscription_type: optional "enterprise" or "team"
Subscription tier for subscription customers. `null` for API customers.
"enterprise"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.subscription_type%5B0%5D)
"team"
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.subscription_type%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data.items.subscription_type)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.data)
has_more: boolean
True if there are more records available beyond the current page.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.has_more)
next_page: string
Opaque cursor token for fetching the next page of results, or null if no more pages are available.
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report.next_page)
[](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code#claude_code_usage_report)
Get Claude Code Usage Report

curl https://api.anthropic.com/v1/organizations/usage_report/claude_code \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "actor": {
        "email_address": "user@emaildomain.com",
        "type": "user_actor"
      "core_metrics": {
        "commits_by_claude_code": 8,
        "lines_of_code": {
          "added": 342,
          "removed": 128
        "num_sessions": 15,
        "pull_requests_by_claude_code": 2
      "customer_type": "api",
      "date": "2025-08-08T00:00:00Z",
      "model_breakdown": [
          "estimated_cost": {
            "amount": 186,
            "currency": "USD"
          "model": "claude-sonnet-4-20250514",
          "tokens": {
            "cache_creation": 2340,
            "cache_read": 8790,
            "input": 45230,
            "output": 12450
          "estimated_cost": {
            "amount": 42,
            "currency": "USD"
          "model": "claude-3-5-haiku-20241022",
          "tokens": {
            "cache_creation": 890,
            "cache_read": 3420,
            "input": 23100,
            "output": 5680
      ],
      "organization_id": "12345678-1234-5678-1234-567812345678",
      "terminal_type": "iTerm.app",
      "tool_actions": {
        "edit_tool": {
          "accepted": 25,
          "rejected": 3
        "multi_edit_tool": {
          "accepted": 12,
          "rejected": 1
        "notebook_edit_tool": {
          "accepted": 5,
          "rejected": 2
        "write_tool": {
          "accepted": 8,
          "rejected": 0
      "subscription_type": "enterprise"
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="

  "data": [
      "actor": {
        "email_address": "user@emaildomain.com",
        "type": "user_actor"
      "core_metrics": {
        "commits_by_claude_code": 8,
        "lines_of_code": {
          "added": 342,
          "removed": 128
        "num_sessions": 15,
        "pull_requests_by_claude_code": 2
      "customer_type": "api",
      "date": "2025-08-08T00:00:00Z",
      "model_breakdown": [
          "estimated_cost": {
            "amount": 186,
            "currency": "USD"
          "model": "claude-sonnet-4-20250514",
          "tokens": {
            "cache_creation": 2340,
            "cache_read": 8790,
            "input": 45230,
            "output": 12450
          "estimated_cost": {
            "amount": 42,
            "currency": "USD"
          "model": "claude-3-5-haiku-20241022",
          "tokens": {
            "cache_creation": 890,
            "cache_read": 3420,
            "input": 23100,
            "output": 5680
      ],
      "organization_id": "12345678-1234-5678-1234-567812345678",
      "terminal_type": "iTerm.app",
      "tool_actions": {
        "edit_tool": {
          "accepted": 25,
          "rejected": 3
        "multi_edit_tool": {
          "accepted": 12,
          "rejected": 1
        "notebook_edit_tool": {
          "accepted": 5,
          "rejected": 2
        "write_tool": {
          "accepted": 8,
          "rejected": 0
      "subscription_type": "enterprise"
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
