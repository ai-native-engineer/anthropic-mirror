<!-- source: https://platform.claude.com/docs/en/api/admin/invites/create -->

# Create Invite
POST/v1/organizations/invites
Create Invite
#####  Body ParametersJSONExpand Collapse 
email: string
Email of the User.
[](https://platform.claude.com/docs/en/api/admin/invites/create#create.email)
role: "user" or "developer" or "billing" or "claude_code_user"
Role for the invited User. Cannot be "admin".
"user"
[](https://platform.claude.com/docs/en/api/admin/invites/create#create.role%5B0%5D)
"developer"
[](https://platform.claude.com/docs/en/api/admin/invites/create#create.role%5B1%5D)
"billing"
[](https://platform.claude.com/docs/en/api/admin/invites/create#create.role%5B2%5D)
"claude_code_user"
[](https://platform.claude.com/docs/en/api/admin/invites/create#create.role%5B3%5D)
[](https://platform.claude.com/docs/en/api/admin/invites/create#create.role)
Invite object { id, email, expires_at, 4 more } 
ID of the Invite.
[](https://platform.claude.com/docs/en/api/admin/invites/create#invite.id)
email: string
Email of the User being invited.
[](https://platform.claude.com/docs/en/api/admin/invites/create#invite.email)
expires_at: string
RFC 3339 datetime string indicating when the Invite expires.
[](https://platform.claude.com/docs/en/api/admin/invites/create#invite.expires_at)
invited_at: string
RFC 3339 datetime string indicating when the Invite was created.
[](https://platform.claude.com/docs/en/api/admin/invites/create#invite.invited_at)
role: "user" or "developer" or "billing" or 2 more
Organization role of the User.
"user"
[](https://platform.claude.com/docs/en/api/admin/invites/create#invite.role%5B0%5D)
"developer"
[](https://platform.claude.com/docs/en/api/admin/invites/create#invite.role%5B1%5D)
"billing"
[](https://platform.claude.com/docs/en/api/admin/invites/create#invite.role%5B2%5D)
"admin"
[](https://platform.claude.com/docs/en/api/admin/invites/create#invite.role%5B3%5D)
"claude_code_user"
[](https://platform.claude.com/docs/en/api/admin/invites/create#invite.role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/invites/create#invite.role)
status: "accepted" or "expired" or "deleted" or "pending"
Status of the Invite.
"accepted"
[](https://platform.claude.com/docs/en/api/admin/invites/create#invite.status%5B0%5D)
"expired"
[](https://platform.claude.com/docs/en/api/admin/invites/create#invite.status%5B1%5D)
"deleted"
[](https://platform.claude.com/docs/en/api/admin/invites/create#invite.status%5B2%5D)
"pending"
[](https://platform.claude.com/docs/en/api/admin/invites/create#invite.status%5B3%5D)
[](https://platform.claude.com/docs/en/api/admin/invites/create#invite.status)
type: "invite"
Object type.
For Invites, this is always `"invite"`.
[](https://platform.claude.com/docs/en/api/admin/invites/create#invite.type)
[](https://platform.claude.com/docs/en/api/admin/invites/create#invite)
Create Invite

curl https://api.anthropic.com/v1/organizations/invites \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "email": "user@emaildomain.com",
          "role": "user"
        }'

  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "email": "user@emaildomain.com",
  "expires_at": "2024-11-20T23:58:27.427722Z",
  "invited_at": "2024-10-30T23:58:27.427722Z",
  "role": "user",
  "status": "pending",
  "type": "invite"

  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "email": "user@emaildomain.com",
  "expires_at": "2024-11-20T23:58:27.427722Z",
  "invited_at": "2024-10-30T23:58:27.427722Z",
  "role": "user",
  "status": "pending",
  "type": "invite"
