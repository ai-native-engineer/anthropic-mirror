<!-- source: https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve -->

# Approve Spend Limit Increase Request
POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve
Approve a pending spend limit increase request.
Writes a per-user spend limit at `amount` for the requester and transitions the request to `approved`. `period` defaults to the period the member was blocked on. Anthropic emails the requester unless `suppress_notification` is set.
##### Path ParametersExpand Collapse 
spend_limit_increase_request_id: string
ID of the spend limit increase request.
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#approve.spend_limit_increase_request_id)
#####  Body ParametersJSONExpand Collapse 
amount: string
New per-user cap as a non-negative integer decimal string (minor units).
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#approve.amount)
period: optional "monthly" or "daily" or "weekly"
"monthly"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#approve.period%5B0%5D)
"daily"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#approve.period%5B1%5D)
"weekly"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#approve.period%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#approve.period)
suppress_notification: optional boolean
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#approve.suppress_notification)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.id)
actor: object { deleted, email_address, name, 2 more } 
A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.
deleted: boolean
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.actor.deleted)
email_address: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.actor.email_address)
name: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.actor.name)
type: "user_actor"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.actor.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.actor.user_id)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.actor)
created_at: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.created_at)
period: "monthly" or "daily" or "weekly"
"monthly"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.period%5B0%5D)
"daily"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.period%5B1%5D)
"weekly"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.period%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.period)
resolved_at: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.resolved_at)
resolved_by: object { deleted, email_address, name, 2 more }  or object { scoped_api_key_id, type } 
A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.
UserActor object { deleted, email_address, name, 2 more } 
A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.
deleted: boolean
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.resolved_by%5B0%5D.deleted)
email_address: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.resolved_by%5B0%5D.email_address)
name: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.resolved_by%5B0%5D.name)
type: "user_actor"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.resolved_by%5B0%5D.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.resolved_by%5B0%5D.user_id)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.resolved_by%5B0%5D)
ScopedAPIKeyActor object { scoped_api_key_id, type } 
A scoped Admin API key acting on behalf of the organization.
scoped_api_key_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.resolved_by%5B1%5D.scoped_api_key_id)
type: "scoped_api_key_actor"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.resolved_by%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.resolved_by%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.resolved_by)
spend_limit: [SpendLimit](https://platform.claude.com/docs/en/api/admin#spend_limit) { id, amount, created_at, 5 more } 
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.id)
amount: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.amount)
created_at: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.created_at)
currency: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.currency)
period: "monthly" or "daily" or "weekly"
"monthly"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.period%5B0%5D)
"daily"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.period%5B1%5D)
"weekly"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.period%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.period)
scope: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more
User object { type, user_id } 
type: "user"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B0%5D.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B0%5D.user_id)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B0%5D)
SeatTier object { seat_tier, type } 
seat_tier: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B1%5D.seat_tier)
type: "seat_tier"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B1%5D)
RbacGroup object { rbac_group_id, type } 
rbac_group_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B2%5D.rbac_group_id)
type: "rbac_group"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B2%5D.type)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B2%5D)
OrganizationService object { service, type } 
service: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B3%5D.service)
type: "organization_service"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B3%5D.type)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B3%5D)
Organization object { type } 
type: "organization"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B4%5D.type)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.scope)
type: "spend_limit"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.type)
updated_at: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit%20%2B%20\(resource\)%20admin.spend_limits.updated_at)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_limit)
spend_summary: [SpendSummary](https://platform.claude.com/docs/en/api/admin#spend_summary) { actor, amount, currency, 5 more } 
Per-member effective-limit report row (GET /spend_limits/effective).
actor: object { deleted, email_address, name, 2 more } 
A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.
deleted: boolean
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor.deleted)
email_address: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor.email_address)
name: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor.name)
type: "user_actor"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor.user_id)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.actor)
amount: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.amount)
currency: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.currency)
period: "monthly" or "daily" or "weekly"
"monthly"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.period%5B0%5D)
"daily"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.period%5B1%5D)
"weekly"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.period%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.period)
period_to_date_spend: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.period_to_date_spend)
scope: object { type, user_id } 
type: "user"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.scope.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.scope.user_id)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.scope)
source: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more
User object { type, user_id } 
type: "user"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B0%5D.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B0%5D.user_id)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B0%5D)
SeatTier object { seat_tier, type } 
seat_tier: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B1%5D.seat_tier)
type: "seat_tier"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B1%5D)
RbacGroup object { rbac_group_id, type } 
rbac_group_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B2%5D.rbac_group_id)
type: "rbac_group"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B2%5D.type)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B2%5D)
OrganizationService object { service, type } 
service: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B3%5D.service)
type: "organization_service"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B3%5D.type)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B3%5D)
Organization object { type } 
type: "organization"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B4%5D.type)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.source)
spend_limit_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary%20%2B%20\(resource\)%20admin.spend_limits.spend_limit_id)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.spend_summary)
status: "pending" or "approved" or "denied"
"pending"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.status%5B0%5D)
"approved"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.status%5B1%5D)
"denied"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.status%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.status)
type: "spend_limit_increase_request"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/increase_requests/approve#increase_request_approve_response.type)
Approve Spend Limit Increase Request

curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID/approve \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "amount": "amount"
        }'

  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_id"
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "monthly",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_id"
  "spend_limit": {
    "id": "id",
    "amount": "amount",
    "created_at": "2019-12-27T18:11:19.117Z",
    "currency": "currency",
    "period": "monthly",
    "scope": {
      "type": "user",
      "user_id": "user_id"
    "type": "spend_limit",
    "updated_at": "2019-12-27T18:11:19.117Z"
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_id"
    "amount": "amount",
    "currency": "currency",
    "period": "monthly",
    "period_to_date_spend": "period_to_date_spend",
    "scope": {
      "type": "user",
      "user_id": "user_id"
    "source": {
      "type": "user",
      "user_id": "user_id"
    "spend_limit_id": "spend_limit_id"
  "status": "pending",
  "type": "spend_limit_increase_request"

  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_id"
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "monthly",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_id"
  "spend_limit": {
    "id": "id",
    "amount": "amount",
    "created_at": "2019-12-27T18:11:19.117Z",
    "currency": "currency",
    "period": "monthly",
    "scope": {
      "type": "user",
      "user_id": "user_id"
    "type": "spend_limit",
    "updated_at": "2019-12-27T18:11:19.117Z"
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_id"
    "amount": "amount",
    "currency": "currency",
    "period": "monthly",
    "period_to_date_spend": "period_to_date_spend",
    "scope": {
      "type": "user",
      "user_id": "user_id"
    "source": {
      "type": "user",
      "user_id": "user_id"
    "spend_limit_id": "spend_limit_id"
  "status": "pending",
  "type": "spend_limit_increase_request"
