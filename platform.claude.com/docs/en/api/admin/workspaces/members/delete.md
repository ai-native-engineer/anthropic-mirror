<!-- source: https://platform.claude.com/docs/en/api/admin/workspaces/members/delete -->

# Delete Workspace Member
DELETE/v1/organizations/workspaces/{workspace_id}/members/{user_id}
Delete Workspace Member
##### Path ParametersExpand Collapse 
workspace_id: string
ID of the Workspace.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/delete#delete.workspace_id)
user_id: string
ID of the User.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/delete#delete.user_id)
type: "workspace_member_deleted"
Deleted object type.
For Workspace Members, this is always `"workspace_member_deleted"`.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/delete#member_delete_response.type)
user_id: string
ID of the User.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/delete#member_delete_response.user_id)
workspace_id: string
ID of the Workspace.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/delete#member_delete_response.workspace_id)
Delete Workspace Member

curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "type": "workspace_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"

  "type": "workspace_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
