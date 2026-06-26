<!-- source: https://platform.claude.com/docs/en/api/admin/analytics/users/list -->

# List User Activity
GET/v1/organizations/analytics/users
Get per-user activity for a given day, with cursor-based pagination.
Returns activity metrics for each user in the organization, sorted by email address. Available to organizations on a Claude Enterprise plan. Requires an API key with the `read:analytics` scope.
##### Query ParametersExpand Collapse 
date: string
UTC date in YYYY-MM-DD format. The day to get user activity for. Must be at least 3 days in the past (data is finalized with a 3-day lag) and no earlier than 2026-01-01.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#list.date)
limit: optional number
Number of results per page (1-1000, default 100).
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#list.limit)
page: optional string
Opaque cursor from a previous response's next_page field.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#list.page)
UserActivity object { data, next_page } 
Response for GET /v1/organizations/analytics/users.
data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 4 more } 
chat_metrics: object { connectors_used_count, distinct_artifacts_created_count, distinct_conversation_count, 8 more } 
Claude.ai activity metrics for a single user on a given day.
connectors_used_count: number
Number of MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.chat_metrics.connectors_used_count)
distinct_artifacts_created_count: number
Number of distinct artifacts created
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.chat_metrics.distinct_artifacts_created_count)
distinct_conversation_count: number
Number of distinct conversations the user participated in. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.chat_metrics.distinct_conversation_count)
distinct_files_uploaded_count: number
Number of distinct files uploaded. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.chat_metrics.distinct_files_uploaded_count)
distinct_projects_created_count: number
Number of distinct projects created
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.chat_metrics.distinct_projects_created_count)
distinct_projects_used_count: number
Number of distinct projects used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.chat_metrics.distinct_projects_used_count)
distinct_shared_artifacts_viewed_count: number
Number of distinct shared artifacts the user viewed. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.chat_metrics.distinct_shared_artifacts_viewed_count)
distinct_skills_used_count: number
Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.chat_metrics.distinct_skills_used_count)
message_count: number
Number of messages sent
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.chat_metrics.message_count)
shared_conversations_viewed_count: number
Number of times the user opened a shared conversation in a project
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.chat_metrics.shared_conversations_viewed_count)
thinking_message_count: number
Number of messages that used extended thinking
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.chat_metrics.thinking_message_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.chat_metrics)
claude_code_metrics: object { core_metrics, tool_actions } 
Claude Code activity metrics for a single user on a given day.
core_metrics: object { commit_count, distinct_session_count, lines_of_code, pull_request_count } 
Core Claude Code activity metrics for a single user on a given day.
commit_count: number
Number of commits made via Claude Code
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.core_metrics.commit_count)
distinct_session_count: number
Number of distinct Claude Code sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.core_metrics.distinct_session_count)
lines_of_code: object { added_count, removed_count } 
Lines of code added and removed via Claude Code.
added_count: number
Lines of code added
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.core_metrics.lines_of_code.added_count)
removed_count: number
Lines of code removed
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.core_metrics.lines_of_code.removed_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.core_metrics.lines_of_code)
pull_request_count: number
Number of pull requests created via Claude Code
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.core_metrics.pull_request_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.core_metrics)
tool_actions: object { edit_tool, multi_edit_tool, notebook_edit_tool, write_tool } 
Per-tool accepted/rejected counts for Claude Code file modification tools.
edit_tool: [ToolActionCounts](https://platform.claude.com/docs/en/api/admin#tool_action_counts) { accepted_count, rejected_count } 
Accepted/rejected counts for a single Claude Code tool type.
accepted_count: number
Number of tool proposals accepted
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.tool_actions.edit_tool%20%2B%20\(resource\)%20admin.analytics.accepted_count)
rejected_count: number
Number of tool proposals rejected
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.tool_actions.edit_tool%20%2B%20\(resource\)%20admin.analytics.rejected_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.tool_actions.edit_tool)
multi_edit_tool: [ToolActionCounts](https://platform.claude.com/docs/en/api/admin#tool_action_counts) { accepted_count, rejected_count } 
Accepted/rejected counts for a single Claude Code tool type.
accepted_count: number
Number of tool proposals accepted
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.tool_actions.multi_edit_tool%20%2B%20\(resource\)%20admin.analytics.accepted_count)
rejected_count: number
Number of tool proposals rejected
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.tool_actions.multi_edit_tool%20%2B%20\(resource\)%20admin.analytics.rejected_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.tool_actions.multi_edit_tool)
notebook_edit_tool: [ToolActionCounts](https://platform.claude.com/docs/en/api/admin#tool_action_counts) { accepted_count, rejected_count } 
Accepted/rejected counts for a single Claude Code tool type.
accepted_count: number
Number of tool proposals accepted
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.tool_actions.notebook_edit_tool%20%2B%20\(resource\)%20admin.analytics.accepted_count)
rejected_count: number
Number of tool proposals rejected
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.tool_actions.notebook_edit_tool%20%2B%20\(resource\)%20admin.analytics.rejected_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.tool_actions.notebook_edit_tool)
write_tool: [ToolActionCounts](https://platform.claude.com/docs/en/api/admin#tool_action_counts) { accepted_count, rejected_count } 
Accepted/rejected counts for a single Claude Code tool type.
accepted_count: number
Number of tool proposals accepted
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.tool_actions.write_tool%20%2B%20\(resource\)%20admin.analytics.accepted_count)
rejected_count: number
Number of tool proposals rejected
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.tool_actions.write_tool%20%2B%20\(resource\)%20admin.analytics.rejected_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.tool_actions.write_tool)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics.tool_actions)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.claude_code_metrics)
cowork_metrics: object { action_count, connectors_used_count, dispatch_turn_count, 5 more } 
Cowork activity metrics for a single user on a given day.
action_count: number
Number of tool actions completed in Cowork sessions
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.cowork_metrics.action_count)
connectors_used_count: number
Total number of connector invocations in Cowork sessions
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.cowork_metrics.connectors_used_count)
dispatch_turn_count: number
Number of Dispatch (background agent) turns completed
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.cowork_metrics.dispatch_turn_count)
distinct_connectors_used_count: number
Number of distinct connectors used in Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.cowork_metrics.distinct_connectors_used_count)
distinct_session_count: number
Number of distinct Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.cowork_metrics.distinct_session_count)
distinct_skills_used_count: number
Number of distinct skills used in Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.cowork_metrics.distinct_skills_used_count)
message_count: number
Number of messages sent in Cowork sessions
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.cowork_metrics.message_count)
skills_used_count: number
Total number of skill invocations in Cowork sessions
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.cowork_metrics.skills_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.cowork_metrics)
design_metrics: object { distinct_projects_created_count, distinct_projects_used_count, distinct_session_count, message_count } 
Claude Design activity metrics for a single user on a given day.
distinct_projects_created_count: number
Number of distinct Claude Design projects created
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.design_metrics.distinct_projects_created_count)
distinct_projects_used_count: number
Number of distinct Claude Design projects the user worked in. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.design_metrics.distinct_projects_used_count)
distinct_session_count: number
Number of distinct Claude Design sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.design_metrics.distinct_session_count)
message_count: number
Number of messages sent in Claude Design sessions
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.design_metrics.message_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.design_metrics)
office_metrics: object { excel, outlook, powerpoint, word } 
Office Agent activity metrics for a single user on a given day, broken out by Office product.
excel: [OfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#office_product_metrics) { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more } 
Office Agent activity metrics for a single user on a given day within one Office product.
connectors_used_count: number
Number of MCP connector invocations
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.connectors_used_count)
distinct_connectors_used_count: number
Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.distinct_connectors_used_count)
distinct_session_count: number
Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.distinct_session_count)
distinct_skills_used_count: number
Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.distinct_skills_used_count)
message_count: number
Number of messages sent
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.message_count)
skills_used_count: number
Number of skill invocations
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.skills_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.excel)
outlook: [OfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#office_product_metrics) { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more } 
Office Agent activity metrics for a single user on a given day within one Office product.
connectors_used_count: number
Number of MCP connector invocations
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.connectors_used_count)
distinct_connectors_used_count: number
Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.distinct_connectors_used_count)
distinct_session_count: number
Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.distinct_session_count)
distinct_skills_used_count: number
Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.distinct_skills_used_count)
message_count: number
Number of messages sent
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.message_count)
skills_used_count: number
Number of skill invocations
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.skills_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.outlook)
powerpoint: [OfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#office_product_metrics) { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more } 
Office Agent activity metrics for a single user on a given day within one Office product.
connectors_used_count: number
Number of MCP connector invocations
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.connectors_used_count)
distinct_connectors_used_count: number
Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.distinct_connectors_used_count)
distinct_session_count: number
Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.distinct_session_count)
distinct_skills_used_count: number
Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.distinct_skills_used_count)
message_count: number
Number of messages sent
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.message_count)
skills_used_count: number
Number of skill invocations
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.skills_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.powerpoint)
word: [OfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#office_product_metrics) { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more } 
Office Agent activity metrics for a single user on a given day within one Office product.
connectors_used_count: number
Number of MCP connector invocations
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.connectors_used_count)
distinct_connectors_used_count: number
Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.distinct_connectors_used_count)
distinct_session_count: number
Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.distinct_session_count)
distinct_skills_used_count: number
Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.distinct_skills_used_count)
message_count: number
Number of messages sent
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.message_count)
skills_used_count: number
Number of skill invocations
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.skills_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics.word)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.office_metrics)
web_search_count: number
Number of web searches performed
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.web_search_count)
user: optional [AnalyticsUser](https://platform.claude.com/docs/en/api/admin#analytics_user) { id, email_address } 
User identifier.
Tagged user identifier (e.g. user_...)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.user%20%2B%20\(resource\)%20admin.analytics.id)
email_address: string
Email address of the user
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.user%20%2B%20\(resource\)%20admin.analytics.email_address)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data.items.user)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.data)
next_page: string
Opaque cursor for the next page, or null if no more results
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity.next_page)
[](https://platform.claude.com/docs/en/api/admin/analytics/users/list#user_activity)
List User Activity

curl https://api.anthropic.com/v1/organizations/analytics/users \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "chat_metrics": {
        "connectors_used_count": 0,
        "distinct_artifacts_created_count": 0,
        "distinct_conversation_count": 0,
        "distinct_files_uploaded_count": 0,
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_shared_artifacts_viewed_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "shared_conversations_viewed_count": 0,
        "thinking_message_count": 0
      "claude_code_metrics": {
        "core_metrics": {
          "commit_count": 0,
          "distinct_session_count": 0,
          "lines_of_code": {
            "added_count": 0,
            "removed_count": 0
          "pull_request_count": 0
        "tool_actions": {
          "edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          "multi_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          "notebook_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          "write_tool": {
            "accepted_count": 0,
            "rejected_count": 0
      "cowork_metrics": {
        "action_count": 0,
        "connectors_used_count": 0,
        "dispatch_turn_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_session_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "skills_used_count": 0
      "design_metrics": {
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_session_count": 0,
        "message_count": 0
      "office_metrics": {
        "excel": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        "outlook": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        "powerpoint": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        "word": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
      "web_search_count": 0,
      "user": {
        "id": "id",
        "email_address": "email_address"
  ],
  "next_page": "next_page"

  "data": [
      "chat_metrics": {
        "connectors_used_count": 0,
        "distinct_artifacts_created_count": 0,
        "distinct_conversation_count": 0,
        "distinct_files_uploaded_count": 0,
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_shared_artifacts_viewed_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "shared_conversations_viewed_count": 0,
        "thinking_message_count": 0
      "claude_code_metrics": {
        "core_metrics": {
          "commit_count": 0,
          "distinct_session_count": 0,
          "lines_of_code": {
            "added_count": 0,
            "removed_count": 0
          "pull_request_count": 0
        "tool_actions": {
          "edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          "multi_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          "notebook_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          "write_tool": {
            "accepted_count": 0,
            "rejected_count": 0
      "cowork_metrics": {
        "action_count": 0,
        "connectors_used_count": 0,
        "dispatch_turn_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_session_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "skills_used_count": 0
      "design_metrics": {
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_session_count": 0,
        "message_count": 0
      "office_metrics": {
        "excel": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        "outlook": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        "powerpoint": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        "word": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
      "web_search_count": 0,
      "user": {
        "id": "id",
        "email_address": "email_address"
  ],
  "next_page": "next_page"
