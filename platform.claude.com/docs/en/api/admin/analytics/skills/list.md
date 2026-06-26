<!-- source: https://platform.claude.com/docs/en/api/admin/analytics/skills/list -->

# Get Skill Usage
GET/v1/organizations/analytics/skills
Get per-skill usage for a given day, with cursor-based pagination.
Returns skill usage metrics for the organization, sorted by skill name. Available to organizations on a Claude Enterprise plan. Requires an API key with the `read:analytics` scope.
##### Query ParametersExpand Collapse 
date: string
UTC date in YYYY-MM-DD format. The day to get skill usage for. Must be at least 3 days in the past (data is finalized with a 3-day lag) and no earlier than 2026-01-01.
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#list.date)
limit: optional number
Number of results per page (1-1000, default 100).
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#list.limit)
page: optional string
Opaque cursor from a previous response's next_page field.
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#list.page)
SkillUsage object { data, next_page } 
Response for GET /v1/organizations/analytics/skills.
data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 3 more } 
chat_metrics: object { distinct_conversation_skill_used_count } 
Claude.ai activity metrics for a single skill on a given day.
distinct_conversation_skill_used_count: number
Number of distinct conversations in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data.items.chat_metrics.distinct_conversation_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data.items.chat_metrics)
claude_code_metrics: object { distinct_session_skill_used_count } 
Claude Code activity metrics for a single skill on a given day.
distinct_session_skill_used_count: number
Number of distinct Claude Code sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data.items.claude_code_metrics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data.items.claude_code_metrics)
cowork_metrics: object { distinct_session_skill_used_count } 
Cowork activity metrics for a single skill on a given day.
distinct_session_skill_used_count: number
Number of distinct Cowork sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data.items.cowork_metrics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data.items.cowork_metrics)
distinct_user_count: number
Number of distinct users who used the skill on the requested day
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data.items.distinct_user_count)
office_metrics: object { excel, outlook, powerpoint, word } 
Office Agent activity metrics for a single skill on a given day, broken out by Office product.
excel: [SkillOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#skill_office_product_metrics) { distinct_session_skill_used_count } 
Office Agent activity metrics for a single skill on a given day within one Office product.
distinct_session_skill_used_count: number
Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data.items.office_metrics.excel%20%2B%20\(resource\)%20admin.analytics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data.items.office_metrics.excel)
outlook: [SkillOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#skill_office_product_metrics) { distinct_session_skill_used_count } 
Office Agent activity metrics for a single skill on a given day within one Office product.
distinct_session_skill_used_count: number
Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data.items.office_metrics.outlook%20%2B%20\(resource\)%20admin.analytics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data.items.office_metrics.outlook)
powerpoint: [SkillOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#skill_office_product_metrics) { distinct_session_skill_used_count } 
Office Agent activity metrics for a single skill on a given day within one Office product.
distinct_session_skill_used_count: number
Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data.items.office_metrics.powerpoint%20%2B%20\(resource\)%20admin.analytics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data.items.office_metrics.powerpoint)
word: [SkillOfficeProductMetrics](https://platform.claude.com/docs/en/api/admin#skill_office_product_metrics) { distinct_session_skill_used_count } 
Office Agent activity metrics for a single skill on a given day within one Office product.
distinct_session_skill_used_count: number
Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data.items.office_metrics.word%20%2B%20\(resource\)%20admin.analytics.distinct_session_skill_used_count)
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data.items.office_metrics.word)
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data.items.office_metrics)
skill_name: string
Name of the skill
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data.items.skill_name)
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.data)
next_page: string
Opaque cursor for the next page, or null if no more results
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage.next_page)
[](https://platform.claude.com/docs/en/api/admin/analytics/skills/list#skill_usage)
Get Skill Usage

curl https://api.anthropic.com/v1/organizations/analytics/skills \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "chat_metrics": {
        "distinct_conversation_skill_used_count": 0
      "claude_code_metrics": {
        "distinct_session_skill_used_count": 0
      "cowork_metrics": {
        "distinct_session_skill_used_count": 0
      "distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_skill_used_count": 0
        "outlook": {
          "distinct_session_skill_used_count": 0
        "powerpoint": {
          "distinct_session_skill_used_count": 0
        "word": {
          "distinct_session_skill_used_count": 0
      "skill_name": "skill_name"
  ],
  "next_page": "next_page"

  "data": [
      "chat_metrics": {
        "distinct_conversation_skill_used_count": 0
      "claude_code_metrics": {
        "distinct_session_skill_used_count": 0
      "cowork_metrics": {
        "distinct_session_skill_used_count": 0
      "distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_skill_used_count": 0
        "outlook": {
          "distinct_session_skill_used_count": 0
        "powerpoint": {
          "distinct_session_skill_used_count": 0
        "word": {
          "distinct_session_skill_used_count": 0
      "skill_name": "skill_name"
  ],
  "next_page": "next_page"
