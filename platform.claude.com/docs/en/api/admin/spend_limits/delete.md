<!-- source: https://platform.claude.com/docs/en/api/admin/spend_limits/delete -->

# Delete Spend Limit
DELETE/v1/organizations/spend_limits/{spend_limit_id}
Delete a per-user spend limit override.
The member falls back to any inherited cap at that period. Seat-tier, group, and organization-level rows cannot be deleted via this endpoint.
##### Path ParametersExpand Collapse 
spend_limit_id: string
ID of the Spend Limit.
[](https://platform.claude.com/docs/en/api/admin/spend_limits/delete#delete.spend_limit_id)
[](https://platform.claude.com/docs/en/api/admin/spend_limits/delete#spend_limit_delete_response.id)
type: "spend_limit_deleted"
[](https://platform.claude.com/docs/en/api/admin/spend_limits/delete#spend_limit_delete_response.type)
Delete Spend Limit

curl https://api.anthropic.com/v1/organizations/spend_limits/$SPEND_LIMIT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "id": "id",
  "type": "spend_limit_deleted"

  "id": "id",
  "type": "spend_limit_deleted"
