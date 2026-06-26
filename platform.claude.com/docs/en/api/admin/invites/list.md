<!-- source: https://platform.claude.com/docs/en/api/admin/invites/list -->

# List Invites
GET/v1/organizations/invites
List Invites
##### Query ParametersExpand Collapse 
after_id: optional string
ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.
[](https://platform.claude.com/docs/en/api/admin/invites/list#list.after_id)
before_id: optional string
ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.
[](https://platform.claude.com/docs/en/api/admin/invites/list#list.before_id)
limit: optional number
Number of items to return per page.
Defaults to `20`. Ranges from `1` to `1000`.
maximum1000
minimum1
[](https://platform.claude.com/docs/en/api/admin/invites/list#list.limit)
data: array of [Invite](https://platform.claude.com/docs/en/api/admin#invite) { id, email, expires_at, 4 more } 
ID of the Invite.
[](https://platform.claude.com/docs/en/api/admin/invites/list#invite.id)
email: string
Email of the User being invited.
[](https://platform.claude.com/docs/en/api/admin/invites/list#invite.email)
expires_at: string
RFC 3339 datetime string indicating when the Invite expires.
[](https://platform.claude.com/docs/en/api/admin/invites/list#invite.expires_at)
invited_at: string
RFC 3339 datetime string indicating when the Invite was created.
[](https://platform.claude.com/docs/en/api/admin/invites/list#invite.invited_at)
role: "user" or "developer" or "billing" or 2 more
Organization role of the User.
"user"
[](https://platform.claude.com/docs/en/api/admin/invites/list#invite.role%5B0%5D)
"developer"
[](https://platform.claude.com/docs/en/api/admin/invites/list#invite.role%5B1%5D)
"billing"
[](https://platform.claude.com/docs/en/api/admin/invites/list#invite.role%5B2%5D)
"admin"
[](https://platform.claude.com/docs/en/api/admin/invites/list#invite.role%5B3%5D)
"claude_code_user"
[](https://platform.claude.com/docs/en/api/admin/invites/list#invite.role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/invites/list#invite.role)
status: "accepted" or "expired" or "deleted" or "pending"
Status of the Invite.
"accepted"
[](https://platform.claude.com/docs/en/api/admin/invites/list#invite.status%5B0%5D)
"expired"
[](https://platform.claude.com/docs/en/api/admin/invites/list#invite.status%5B1%5D)
"deleted"
[](https://platform.claude.com/docs/en/api/admin/invites/list#invite.status%5B2%5D)
"pending"
[](https://platform.claude.com/docs/en/api/admin/invites/list#invite.status%5B3%5D)
[](https://platform.claude.com/docs/en/api/admin/invites/list#invite.status)
type: "invite"
Object type.
For Invites, this is always `"invite"`.
[](https://platform.claude.com/docs/en/api/admin/invites/list#invite.type)
[](https://platform.claude.com/docs/en/api/admin/invites/list#list)
first_id: string
First ID in the `data` list. Can be used as the `before_id` for the previous page.
[](https://platform.claude.com/docs/en/api/admin/invites/list#list)
has_more: boolean
Indicates if there are more results in the requested page direction.
[](https://platform.claude.com/docs/en/api/admin/invites/list#list)
last_id: string
Last ID in the `data` list. Can be used as the `after_id` for the next page.
[](https://platform.claude.com/docs/en/api/admin/invites/list#list)
List Invites

curl https://api.anthropic.com/v1/organizations/invites \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
      "email": "user@emaildomain.com",
      "expires_at": "2024-11-20T23:58:27.427722Z",
      "invited_at": "2024-10-30T23:58:27.427722Z",
      "role": "user",
      "status": "pending",
      "type": "invite"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"

  "data": [
      "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
      "email": "user@emaildomain.com",
      "expires_at": "2024-11-20T23:58:27.427722Z",
      "invited_at": "2024-10-30T23:58:27.427722Z",
      "role": "user",
      "status": "pending",
      "type": "invite"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
