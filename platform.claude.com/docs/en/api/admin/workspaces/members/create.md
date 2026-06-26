<!-- source: https://platform.claude.com/docs/en/api/admin/workspaces/members/create -->

# Create Workspace Member
POST/v1/organizations/workspaces/{workspace_id}/members
Create Workspace Member
##### Path ParametersExpand Collapse 
workspace_id: string
ID of the Workspace.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/create#create.workspace_id)
#####  Body ParametersJSONExpand Collapse 
user_id: string
ID of the User.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/create#create.user_id)
workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or "workspace_admin"
Role of the new Workspace Member. Cannot be "workspace_billing".
"workspace_user"
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/create#create.workspace_role%5B0%5D)
"workspace_developer"
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/create#create.workspace_role%5B1%5D)
"workspace_restricted_developer"
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/create#create.workspace_role%5B2%5D)
"workspace_admin"
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/create#create.workspace_role%5B3%5D)
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/create#create.workspace_role)
WorkspaceMember object { type, user_id, workspace_id, workspace_role } 
type: "workspace_member"
Object type.
For Workspace Members, this is always `"workspace_member"`.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/create#workspaceMember.type)
user_id: string
ID of the User.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/create#workspaceMember.user_id)
workspace_id: string
ID of the Workspace.
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/create#workspaceMember.workspace_id)
workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more
Role of the Workspace Member.
"workspace_user"
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/create#workspaceMember.workspace_role%5B0%5D)
"workspace_developer"
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/create#workspaceMember.workspace_role%5B1%5D)
"workspace_restricted_developer"
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/create#workspaceMember.workspace_role%5B2%5D)
"workspace_admin"
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/create#workspaceMember.workspace_role%5B3%5D)
"workspace_billing"
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/create#workspaceMember.workspace_role%5B4%5D)
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/create#workspaceMember.workspace_role)
[](https://platform.claude.com/docs/en/api/admin/workspaces/members/create#workspaceMember)
Create Workspace Member

curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "workspace_role": "workspace_user"
        }'

  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_user"

  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_user"
