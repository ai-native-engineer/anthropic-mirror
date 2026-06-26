<!-- source: https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list -->

# Get Chat Project Usage
GET/v1/organizations/analytics/apps/chat/projects
Get per-project activity for a given day, with cursor-based pagination.
Returns activity metrics for each project in the organization, sorted by project ID. Available to organizations on a Claude Enterprise plan. Requires an API key with the `read:analytics` scope.
##### Query ParametersExpand Collapse 
date: string
UTC date in YYYY-MM-DD format. The day to get project activity for. Must be at least 3 days in the past (data is finalized with a 3-day lag) and no earlier than 2026-01-01.
[](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list#list.date)
limit: optional number
Number of results per page (1-1000, default 100).
[](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list#list.limit)
page: optional string
Opaque cursor from a previous response's next_page field.
[](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list#list.page)
ChatProjectUsage object { data, next_page } 
Response for GET /v1/organizations/analytics/apps/chat/projects.
data: array of object { distinct_conversation_count, distinct_user_count, message_count, 4 more } 
distinct_conversation_count: number
Number of distinct conversations in the project on the requested day
[](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list#chat_project_usage.data.items.distinct_conversation_count)
distinct_user_count: number
Number of distinct users who used the project on the requested day
[](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list#chat_project_usage.data.items.distinct_user_count)
message_count: number
Number of messages sent in the project on the requested day
[](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list#chat_project_usage.data.items.message_count)
project_id: string
Tagged project identifier (e.g. claude_proj_...)
[](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list#chat_project_usage.data.items.project_id)
project_name: string
Name of the project
[](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list#chat_project_usage.data.items.project_name)
created_at: optional string
Project creation timestamp, RFC 3339. Null if the project was deleted before attribution was recorded.
[](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list#chat_project_usage.data.items.created_at)
created_by: optional [AnalyticsUser](https://platform.claude.com/docs/en/api/admin#analytics_user) { id, email_address } 
User identifier.
Tagged user identifier (e.g. user_...)
[](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list#chat_project_usage.data.items.created_by%20%2B%20\(resource\)%20admin.analytics.id)
email_address: string
Email address of the user
[](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list#chat_project_usage.data.items.created_by%20%2B%20\(resource\)%20admin.analytics.email_address)
[](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list#chat_project_usage.data.items.created_by)
[](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list#chat_project_usage.data)
next_page: string
Opaque cursor for the next page, or null if no more results
[](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list#chat_project_usage.next_page)
[](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list#chat_project_usage)
Get Chat Project Usage

curl https://api.anthropic.com/v1/organizations/analytics/apps/chat/projects \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "distinct_conversation_count": 0,
      "distinct_user_count": 0,
      "message_count": 0,
      "project_id": "project_id",
      "project_name": "project_name",
      "created_at": "created_at",
      "created_by": {
        "id": "id",
        "email_address": "email_address"
  ],
  "next_page": "next_page"

  "data": [
      "distinct_conversation_count": 0,
      "distinct_user_count": 0,
      "message_count": 0,
      "project_id": "project_id",
      "project_name": "project_name",
      "created_at": "created_at",
      "created_by": {
        "id": "id",
        "email_address": "email_address"
  ],
  "next_page": "next_page"
