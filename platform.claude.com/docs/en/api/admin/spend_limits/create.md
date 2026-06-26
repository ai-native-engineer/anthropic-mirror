<!-- source: https://platform.claude.com/docs/en/api/admin/spend_limits/create -->

# Set Spend Limit
POST/v1/organizations/spend_limits
Set a per-user spend limit override.
Upsert keyed on (scope, period): setting a limit that already exists overwrites it in place. Only `scope.type: "user"` is accepted; seat-tier, group, and organization-level defaults are configured in claude.ai.
#####  Body ParametersJSONExpand Collapse 
amount: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#create.amount)
scope: object { type, user_id } 
type: "user"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#create.scope.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#create.scope.user_id)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#create.scope)
period: optional "monthly" or "daily" or "weekly"
"monthly"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#create.period%5B0%5D)
"daily"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#create.period%5B1%5D)
"weekly"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#create.period%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#create.period)
SpendLimit object { id, amount, created_at, 5 more } 
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.id)
amount: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.amount)
created_at: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.created_at)
currency: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.currency)
period: "monthly" or "daily" or "weekly"
"monthly"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.period%5B0%5D)
"daily"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.period%5B1%5D)
"weekly"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.period%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.period)
scope: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more
User object { type, user_id } 
type: "user"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.scope%5B0%5D.type)
user_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.scope%5B0%5D.user_id)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.scope%5B0%5D)
SeatTier object { seat_tier, type } 
seat_tier: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.scope%5B1%5D.seat_tier)
type: "seat_tier"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.scope%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.scope%5B1%5D)
RbacGroup object { rbac_group_id, type } 
rbac_group_id: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.scope%5B2%5D.rbac_group_id)
type: "rbac_group"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.scope%5B2%5D.type)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.scope%5B2%5D)
OrganizationService object { service, type } 
service: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.scope%5B3%5D.service)
type: "organization_service"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.scope%5B3%5D.type)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.scope%5B3%5D)
Organization object { type } 
type: "organization"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.scope%5B4%5D.type)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.scope%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.scope)
type: "spend_limit"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.type)
updated_at: string
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit.updated_at)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/create#spend_limit)
Set Spend Limit

curl https://api.anthropic.com/v1/organizations/spend_limits \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "amount": "amount",
          "scope": {
            "type": "user",
            "user_id": "user_id"
        }'

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
