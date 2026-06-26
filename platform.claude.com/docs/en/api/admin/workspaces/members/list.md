<!-- source: https://platform.claude.com/docs/en/api/admin/workspaces/members/list -->

# List Workspace Members
GET/v1/organizations/workspaces/{workspace_id}/members
List Workspace Members
##### Path ParametersExpand Collapse 
workspace_id: string
ID of the Workspace.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/list#list.workspace_id)
##### Query ParametersExpand Collapse 
after_id: optional string
ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/list#list.after_id)
before_id: optional string
ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/list#list.before_id)
limit: optional number
Number of items to return per page.
Defaults to `20`. Ranges from `1` to `1000`.
maximum1000
minimum1
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/list#list.limit)
data: array of [WorkspaceMember](https://platform.claude.com/docs/en/api/admin#workspaceMember) { type, user_id, workspace_id, workspace_role } 
type: "workspace_member"
Object type.
For Workspace Members, this is always `"workspace_member"`.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/list#workspaceMember.type)
user_id: string
ID of the User.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/list#workspaceMember.user_id)
workspace_id: string
ID of the Workspace.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/list#workspaceMember.workspace_id)
workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more
Role of the Workspace Member.
"workspace_user"
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/list#workspaceMember.workspace_role%5B0%5D)
"workspace_developer"
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/list#workspaceMember.workspace_role%5B1%5D)
"workspace_restricted_developer"
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/list#workspaceMember.workspace_role%5B2%5D)
"workspace_admin"
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/list#workspaceMember.workspace_role%5B3%5D)
"workspace_billing"
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/list#workspaceMember.workspace_role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/list#workspaceMember.workspace_role)
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/list#list)
first_id: string
First ID in the `data` list. Can be used as the `before_id` for the previous page.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/list#list)
has_more: boolean
Indicates if there are more results in the requested page direction.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/list#list)
last_id: string
Last ID in the `data` list. Can be used as the `after_id` for the next page.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/list#list)
List Workspace Members

curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "type": "workspace_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "workspace_role": "workspace_user"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"

  "data": [
      "type": "workspace_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "workspace_role": "workspace_user"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
