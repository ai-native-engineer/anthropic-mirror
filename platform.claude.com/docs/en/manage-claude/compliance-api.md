<!-- source: https://platform.claude.com/docs/en/manage-claude/compliance-api -->

# Compliance API
Programmatic access to your organization's Claude activity, chats, files, projects, and users for compliance, audit, and governance.
The Compliance API gives Claude Enterprise customers programmatic access to their organization's Activity Feed, the directory of users, roles, and groups across every linked organization, the effective settings in force for each organization, and, for claude.ai organizations, the underlying chats, files, and projects. Security, legal, and compliance teams use it to audit activity, retrieve or delete content, and feed events into downstream tooling.
Two key types unlock the Compliance API. A **Compliance Access Key** (created in claude.ai) reaches every endpoint, and an **Admin API key** (created in Claude Console) reaches the Activity Feed only. See [Which key do you need?](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#which-key-do-you-need) for the full key-type comparison.
The following call returns the most recent activity event in your organization. Any key with the `read:compliance_activities` scope can make it. To create a key and grant it that scope, see [Get access to the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access).
cURL

curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/activities?limit=1" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY"

A successful response returns a JSON object containing `data` (an array of `Activity` records), `has_more`, `first_id`, and `last_id`:
Response

  "data": [
      "id": "activity_01XyDMpzjS89pFZXqSFUBDr6",
      "created_at": "2026-04-10T08:09:10Z",
      "organization_id": "org_01Wv6QeBcDfGhJkLmNpQrSt8",
      "organization_uuid": "abcdef01-2345-6789-abcd-ef0123456789",
      "actor": {
        "type": "user_actor",
        "email_address": "[email protected][](https://platform.claude.com/cdn-cgi/l/email-protection)",
        "user_id": "user_01TuVwXyZaBcDeFgH2JkLmN4",
        "ip_address": "192.0.2.34",
        "user_agent": "Mozilla/5.0..."
      "type": "claude_chat_created",
      "claude_chat_id": "claude_chat_01XyDMpzjS89pFZXqSFUBDr6",
      "claude_project_id": "claude_proj_01KGp4eZNug9ri4kE35RSppq"
  ],
  "has_more": true,
  "first_id": "activity_01XyDMpzjS89pFZXqSFUBDr6",
  "last_id": "activity_01XyDMpzjS89pFZXqSFUBDr6"

* * *
How the Compliance API works
Every endpoint lives under `/v1/compliance/*` on `https://api.anthropic.com` and authenticates through the `x-api-key` header. To provision a key, see [Get access to the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access).
The Activity Feed (`GET /v1/compliance/activities`) is available to any key that carries the `read:compliance_activities` scope; see [Query the Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed) for filters, pagination, and the full `Activity` object. The remaining endpoints require a Compliance Access Key carrying the relevant scope.
A Claude Enterprise tenant has one parent organization (the top-level container that centralizes identity) with linked organizations of two kinds: claude.ai organizations, where users chat and store content, and Claude Console organizations, where users manage Claude API workloads. The directory endpoints (organizations, users, roles, and groups) return data from every linked organization of either kind. The content endpoints (chats, files, projects, and project attachments) serve claude.ai data only.
All `/v1/compliance/*` endpoints share a single rate limit of 600 requests per minute per parent organization; see [429 Too Many Requests](https://platform.claude.com/docs/en/manage-claude/compliance-errors#429-too-many-requests) for the response headers and retry contract.
* * *
Compliance API versus related features
Two adjacent features overlap with the Compliance API; here is how to choose.
### 
Export audit logs
The audit log export is a separate feature in [claude.ai > Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls) that lets owners and primary owners download a CSV of organization events. It's significantly narrower than the Compliance API: a capped lookback window, CSV download only, and no access to chat, file, or project content. Standardize on the Compliance API for ongoing programmatic use.
### 
Analytics API
Anthropic provides two analytics APIs: the Claude Enterprise Analytics API and the [Claude Code Analytics API](https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api). Both return aggregated usage and cost figures for IT, FinOps, and platform teams, whereas the Compliance API returns per-event records for security, legal, and compliance teams. The two API families answer different questions, use different keys, and are provisioned separately.
* * *
In this section
[ Get access to the Compliance API Request Compliance API access for your organization, then create a Compliance Access Key (with scoped permissions) or an Admin API key, and learn which to use. ](https://platform.claude.com/docs/en/manage-claude/compliance-api-access)[ Query the Activity Feed Retrieve, filter, and paginate the shared Activity Feed. Supported by both key types. ](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed)[ Retrieve and delete chats, files, and projects Read chat content and attachments, then delete on demand. Compliance Access Key required. ](https://platform.claude.com/docs/en/manage-claude/compliance-content-data)[ List organizations, users, roles, groups, and settings Enumerate linked organizations, members, roles, and directory groups, and read each organization's effective settings. ](https://platform.claude.com/docs/en/manage-claude/compliance-org-data)[ Design your compliance integration Choose a feed-consumption pattern, plan SIEM correlation, and decide your retention approach. ](https://platform.claude.com/docs/en/manage-claude/compliance-integration-patterns)[ Handle Compliance API errors Every 400, 401, 403, 404, 409, 429, and 5xx response the Compliance API returns, with the fix for each. ](https://platform.claude.com/docs/en/manage-claude/compliance-errors)[ API reference Endpoint paths, parameters, and response schemas for every Compliance API call. ](https://platform.claude.com/docs/en/api/compliance)[ Compliance API FAQ Answers to common key, scope, availability, and integration questions. ](https://platform.claude.com/docs/en/manage-claude/compliance-faq)
  * [How the Compliance API works](https://platform.claude.com/docs/en/manage-claude/compliance-api#how-the-compliance-api-works)
  * [Compliance API versus related features](https://platform.claude.com/docs/en/manage-claude/compliance-api#compliance-api-versus-related-features)
  * [Export audit logs](https://platform.claude.com/docs/en/manage-claude/compliance-api#export-audit-logs)
  * [Analytics API](https://platform.claude.com/docs/en/manage-claude/compliance-api#analytics-api)
  * [In this section](https://platform.claude.com/docs/en/manage-claude/compliance-api#in-this-section)

Admin/Compliance API
# Compliance API
Programmatic access to your organization's Claude activity, chats, files, projects, and users for compliance, audit, and governance.
The Compliance API gives Claude Enterprise customers programmatic access to their organization's Activity Feed, the directory of users, roles, and groups across every linked organization, the effective settings in force for each organization, and, for claude.ai organizations, the underlying chats, files, and projects. Security, legal, and compliance teams use it to audit activity, retrieve or delete content, and feed events into downstream tooling.
Two key types unlock the Compliance API. A **Compliance Access Key** (created in claude.ai) reaches every endpoint, and an **Admin API key** (created in Claude Console) reaches the Activity Feed only. See [Which key do you need?](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#which-key-do-you-need) for the full key-type comparison.
The following call returns the most recent activity event in your organization. Any key with the `read:compliance_activities` scope can make it. To create a key and grant it that scope, see [Get access to the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access).
cURL

curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/activities?limit=1" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY"

A successful response returns a JSON object containing `data` (an array of `Activity` records), `has_more`, `first_id`, and `last_id`:
Response

  "data": [
      "id": "activity_01XyDMpzjS89pFZXqSFUBDr6",
      "created_at": "2026-04-10T08:09:10Z",
      "organization_id": "org_01Wv6QeBcDfGhJkLmNpQrSt8",
      "organization_uuid": "abcdef01-2345-6789-abcd-ef0123456789",
      "actor": {
        "type": "user_actor",
        "email_address": "[email protected][](https://platform.claude.com/cdn-cgi/l/email-protection)",
        "user_id": "user_01TuVwXyZaBcDeFgH2JkLmN4",
        "ip_address": "192.0.2.34",
        "user_agent": "Mozilla/5.0..."
      "type": "claude_chat_created",
      "claude_chat_id": "claude_chat_01XyDMpzjS89pFZXqSFUBDr6",
      "claude_project_id": "claude_proj_01KGp4eZNug9ri4kE35RSppq"
  ],
  "has_more": true,
  "first_id": "activity_01XyDMpzjS89pFZXqSFUBDr6",
  "last_id": "activity_01XyDMpzjS89pFZXqSFUBDr6"

* * *
How the Compliance API works
Every endpoint lives under `/v1/compliance/*` on `https://api.anthropic.com` and authenticates through the `x-api-key` header. To provision a key, see [Get access to the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access).
The Activity Feed (`GET /v1/compliance/activities`) is available to any key that carries the `read:compliance_activities` scope; see [Query the Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed) for filters, pagination, and the full `Activity` object. The remaining endpoints require a Compliance Access Key carrying the relevant scope.
A Claude Enterprise tenant has one parent organization (the top-level container that centralizes identity) with linked organizations of two kinds: claude.ai organizations, where users chat and store content, and Claude Console organizations, where users manage Claude API workloads. The directory endpoints (organizations, users, roles, and groups) return data from every linked organization of either kind. The content endpoints (chats, files, projects, and project attachments) serve claude.ai data only.
All `/v1/compliance/*` endpoints share a single rate limit of 600 requests per minute per parent organization; see [429 Too Many Requests](https://platform.claude.com/docs/en/manage-claude/compliance-errors#429-too-many-requests) for the response headers and retry contract.
* * *
Compliance API versus related features
Two adjacent features overlap with the Compliance API; here is how to choose.
### 
Export audit logs
The audit log export is a separate feature in [claude.ai > Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls) that lets owners and primary owners download a CSV of organization events. It's significantly narrower than the Compliance API: a capped lookback window, CSV download only, and no access to chat, file, or project content. Standardize on the Compliance API for ongoing programmatic use.
### 
Analytics API
Anthropic provides two analytics APIs: the Claude Enterprise Analytics API and the [Claude Code Analytics API](https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api). Both return aggregated usage and cost figures for IT, FinOps, and platform teams, whereas the Compliance API returns per-event records for security, legal, and compliance teams. The two API families answer different questions, use different keys, and are provisioned separately.
* * *
In this section
[ Get access to the Compliance API Request Compliance API access for your organization, then create a Compliance Access Key (with scoped permissions) or an Admin API key, and learn which to use. ](https://platform.claude.com/docs/en/manage-claude/compliance-api-access)[ Query the Activity Feed Retrieve, filter, and paginate the shared Activity Feed. Supported by both key types. ](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed)[ Retrieve and delete chats, files, and projects Read chat content and attachments, then delete on demand. Compliance Access Key required. ](https://platform.claude.com/docs/en/manage-claude/compliance-content-data)[ List organizations, users, roles, groups, and settings Enumerate linked organizations, members, roles, and directory groups, and read each organization's effective settings. ](https://platform.claude.com/docs/en/manage-claude/compliance-org-data)[ Design your compliance integration Choose a feed-consumption pattern, plan SIEM correlation, and decide your retention approach. ](https://platform.claude.com/docs/en/manage-claude/compliance-integration-patterns)[ Handle Compliance API errors Every 400, 401, 403, 404, 409, 429, and 5xx response the Compliance API returns, with the fix for each. ](https://platform.claude.com/docs/en/manage-claude/compliance-errors)[ API reference Endpoint paths, parameters, and response schemas for every Compliance API call. ](https://platform.claude.com/docs/en/api/compliance)[ Compliance API FAQ Answers to common key, scope, availability, and integration questions. ](https://platform.claude.com/docs/en/manage-claude/compliance-faq)
