<!-- source: https://platform.claude.com/docs/en/api/admin-api/users/get-user -->

# Get User
GET/v1/organizations/users/{user_id}
Get User
##### Path ParametersExpand Collapse 
user_id: string
ID of the User.
[](https://platform.claude.com/docs/en/api/admin/users/retrieve#retrieve.user_id)
User object { id, added_at, email, 3 more } 
ID of the User.
[](https://platform.claude.com/docs/en/api/admin/users/retrieve#user.id)
added_at: string
RFC 3339 datetime string indicating when the User joined the Organization.
[](https://platform.claude.com/docs/en/api/admin/users/retrieve#user.added_at)
email: string
Email of the User.
[](https://platform.claude.com/docs/en/api/admin/users/retrieve#user.email)
name: string
Name of the User.
[](https://platform.claude.com/docs/en/api/admin/users/retrieve#user.name)
role: "user" or "developer" or "billing" or 2 more
Organization role of the User.
"user"
[](https://platform.claude.com/docs/en/api/admin/users/retrieve#user.role%5B0%5D)
"developer"
[](https://platform.claude.com/docs/en/api/admin/users/retrieve#user.role%5B1%5D)
"billing"
[](https://platform.claude.com/docs/en/api/admin/users/retrieve#user.role%5B2%5D)
"admin"
[](https://platform.claude.com/docs/en/api/admin/users/retrieve#user.role%5B3%5D)
"claude_code_user"
[](https://platform.claude.com/docs/en/api/admin/users/retrieve#user.role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/users/retrieve#user.role)
type: "user"
Object type.
For Users, this is always `"user"`.
[](https://platform.claude.com/docs/en/api/admin/users/retrieve#user.type)
[](https://platform.claude.com/docs/en/api/admin/users/retrieve#user)
Get User

curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "user",
  "type": "user"

  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "user",
  "type": "user"
