<!-- source: https://platform.claude.com/docs/en/api/admin/users/list -->

# List Users
GET/v1/organizations/users
List Users
##### Query ParametersExpand Collapse 
after_id: optional string
ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.
[](https://platform.claude.com/docs/en/api/admin/users/list#list.after_id)
before_id: optional string
ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.
[](https://platform.claude.com/docs/en/api/admin/users/list#list.before_id)
email: optional string
Filter by user email.
[](https://platform.claude.com/docs/en/api/admin/users/list#list.email)
limit: optional number
Number of items to return per page.
Defaults to `20`. Ranges from `1` to `1000`.
maximum1000
minimum1
[](https://platform.claude.com/docs/en/api/admin/users/list#list.limit)
data: array of [User](https://platform.claude.com/docs/en/api/admin#user) { id, added_at, email, 3 more } 
ID of the User.
[](https://platform.claude.com/docs/en/api/admin/users/list#user.id)
added_at: string
RFC 3339 datetime string indicating when the User joined the Organization.
[](https://platform.claude.com/docs/en/api/admin/users/list#user.added_at)
email: string
Email of the User.
[](https://platform.claude.com/docs/en/api/admin/users/list#user.email)
name: string
Name of the User.
[](https://platform.claude.com/docs/en/api/admin/users/list#user.name)
role: "user" or "developer" or "billing" or 2 more
Organization role of the User.
"user"
[](https://platform.claude.com/docs/en/api/admin/users/list#user.role%5B0%5D)
"developer"
[](https://platform.claude.com/docs/en/api/admin/users/list#user.role%5B1%5D)
"billing"
[](https://platform.claude.com/docs/en/api/admin/users/list#user.role%5B2%5D)
"admin"
[](https://platform.claude.com/docs/en/api/admin/users/list#user.role%5B3%5D)
"claude_code_user"
[](https://platform.claude.com/docs/en/api/admin/users/list#user.role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/users/list#user.role)
type: "user"
Object type.
For Users, this is always `"user"`.
[](https://platform.claude.com/docs/en/api/admin/users/list#user.type)
[](https://platform.claude.com/docs/en/api/admin/users/list#list)
first_id: string
First ID in the `data` list. Can be used as the `before_id` for the previous page.
[](https://platform.claude.com/docs/en/api/admin/users/list#list)
has_more: boolean
Indicates if there are more results in the requested page direction.
[](https://platform.claude.com/docs/en/api/admin/users/list#list)
last_id: string
Last ID in the `data` list. Can be used as the `after_id` for the next page.
[](https://platform.claude.com/docs/en/api/admin/users/list#list)
List Users

curl https://api.anthropic.com/v1/organizations/users \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "added_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "name": "Jane Doe",
      "role": "user",
      "type": "user"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"

  "data": [
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "added_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "name": "Jane Doe",
      "role": "user",
      "type": "user"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
