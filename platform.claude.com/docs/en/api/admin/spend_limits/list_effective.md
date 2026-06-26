<!-- source: https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective -->

# List Effective Spend Limits
GET/v1/organizations/spend_limits/effective
List each member's effective spend limit and period-to-date spend.
Returns one row per (member, period) the member resolves a cap for, with the `source` scope the cap was inherited from. Paginates by member, so a member's periods never split across pages.
##### Query ParametersExpand Collapse 
limit: optional number
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#list_effective.limit)
page: optional string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#list_effective.page)
period: optional array of string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#list_effective.period)
user_ids: optional array of string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#list_effective.user_ids)
data: array of [SpendSummary](https://platform.claude.com/docs/en/api/admin#spend_summary) { actor, amount, currency, 5 more } 
actor: object { deleted, email_address, name, 2 more } 
A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.
deleted: boolean
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.actor.deleted)
email_address: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.actor.email_address)
name: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.actor.name)
type: "user_actor"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.actor.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.actor.user_id)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.actor)
amount: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.amount)
currency: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.currency)
period: "monthly" or "daily" or "weekly"
"monthly"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.period%5B0%5D)
"daily"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.period%5B1%5D)
"weekly"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.period%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.period)
period_to_date_spend: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.period_to_date_spend)
scope: object { type, user_id } 
type: "user"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.scope.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.scope.user_id)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.scope)
source: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more
User object { type, user_id } 
type: "user"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.source%5B0%5D.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.source%5B0%5D.user_id)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.source%5B0%5D)
SeatTier object { seat_tier, type } 
seat_tier: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.source%5B1%5D.seat_tier)
type: "seat_tier"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.source%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.source%5B1%5D)
RbacGroup object { rbac_group_id, type } 
rbac_group_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.source%5B2%5D.rbac_group_id)
type: "rbac_group"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.source%5B2%5D.type)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.source%5B2%5D)
OrganizationService object { service, type } 
service: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.source%5B3%5D.service)
type: "organization_service"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.source%5B3%5D.type)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.source%5B3%5D)
Organization object { type } 
type: "organization"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.source%5B4%5D.type)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.source%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.source)
spend_limit_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#spend_summary.spend_limit_id)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#list_effective)
next_page: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective#list_effective)
List Effective Spend Limits

curl https://api.anthropic.com/v1/organizations/spend_limits/effective \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
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
  ],
  "next_page": "next_page"

  "data": [
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
  ],
  "next_page": "next_page"
