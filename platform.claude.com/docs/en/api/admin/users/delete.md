<!-- source: https://platform.claude.com/docs/en/api/admin/users/delete -->

# Remove User
DELETE/v1/organizations/users/{user_id}
Remove User
##### Path ParametersExpand Collapse 
user_id: string
ID of the User.
[](https://platform.claude.com/docs/en/api/admin/users/delete#delete.user_id)
ID of the User.
[](https://platform.claude.com/docs/en/api/admin/users/delete#user_delete_response.id)
type: "user_deleted"
Deleted object type.
For Users, this is always `"user_deleted"`.
[](https://platform.claude.com/docs/en/api/admin/users/delete#user_delete_response.type)
Remove User

curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "type": "user_deleted"

  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "type": "user_deleted"
