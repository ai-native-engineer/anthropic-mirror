<!-- source: https://platform.claude.com/docs/en/api/admin/invites/delete -->

# Delete Invite
DELETE/v1/organizations/invites/{invite_id}
Delete Invite
##### Path ParametersExpand Collapse 
invite_id: string
ID of the Invite.
[](https://platform.claude.com/docs/en/api/admin/invites/delete#delete.invite_id)
ID of the Invite.
[](https://platform.claude.com/docs/en/api/admin/invites/delete#invite_delete_response.id)
type: "invite_deleted"
Deleted object type.
For Invites, this is always `"invite_deleted"`.
[](https://platform.claude.com/docs/en/api/admin/invites/delete#invite_delete_response.type)
Delete Invite

curl https://api.anthropic.com/v1/organizations/invites/$INVITE_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "type": "invite_deleted"

  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "type": "invite_deleted"
