<!-- source: https://platform.claude.com/docs/en/manage-claude/workspaces -->

# Workspaces
Organize API keys, manage team access, and control costs with workspaces.
Workspaces provide a way to organize your API usage within an organization. Use workspaces to separate different projects, environments, or teams while maintaining centralized billing and administration.
How workspaces work
Every organization has a **Default Workspace** that cannot be renamed, archived, or deleted. When you create additional workspaces, you can assign API keys, members, and resource limits to each one.
Key characteristics:
  * **Workspace identifiers** use the `wrkspc_` prefix (for example, `wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ`)
  * **Maximum 100 workspaces** per organization (archived workspaces don't count)
  * **Default Workspace** has no ID and doesn't appear in list endpoints
  * **API keys** are scoped to a single workspace and can only access resources within that workspace

### 
Claude Code workspace
When a member of your organization first signs in to [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) with their Claude Console account, Anthropic automatically creates a **Claude Code** workspace in the organization and adds that member to it. Every subsequent member who signs in to Claude Code is added the same way.
The Claude Code workspace keeps Claude Code traffic separate from your other API workloads:
  * Claude Code mints a per-user API key in this workspace at sign-in. You cannot create keys in it manually from the Console.
  * A Claude Code key stops working if its owner is removed from the workspace or organization, unlike standard workspace keys.
  * Claude Code usage is rate-limited separately, and admins can cap its share of the organization's limits under [Settings > Workspaces](https://platform.claude.com/settings/workspaces).
  * It is the only workspace that supports per-user monthly spend limits.


Archiving the Claude Code workspace disables Claude Code sign-in through Console billing for the whole organization.
Workspace roles and permissions
Members can have different roles in each workspace, allowing fine-grained access control.  
| Role  | Permissions  |  
| --- | --- |  
| Workspace User  | Use the Workbench only  |  
| Workspace Limited Developer  | Create and manage API keys, use the API. Cannot access session tracing views or download files.  |  
| Workspace Developer  | Create and manage API keys, use the API  |  
| Workspace Admin  | Full control over workspace settings and members  |  
| Workspace Billing  | View workspace billing information (inherited from organization billing role)  |  
### 
Role inheritance
  * **Organization admins** automatically receive Workspace Admin access to all workspaces
  * **Organization billing members** automatically receive Workspace Billing access to all workspaces
  * **Organization users and developers** must be explicitly added to each workspace

The Workspace Billing role cannot be manually assigned. It's inherited from having the organization billing role.
Managing workspaces
Only organization admins can create workspaces. Organization users and developers must be added to workspaces by an admin.
### 
Using the Console
Create and manage workspaces in the [Claude Console](https://platform.claude.com/settings/workspaces).
#### 
Create a workspace
  1. 1
Open workspace settings
In the Claude Console, go to **Settings > Workspaces**.
  2. 2
Create a workspace
Click **Create workspace**.
  3. 3
Configure the workspace
Enter a workspace name and select a color for visual identification.
  4. 4
Create the workspace
Click **Create** to finalize.


To switch between workspaces in the Console, use the **Workspaces** selector in the top-left corner.
#### 
Edit workspace details
To modify a workspace's name or color:
  1. Select the workspace from the list
  2. Click the ellipsis menu (**...**) and choose **Edit details**
  3. Update the name or color and save your changes

The Default Workspace cannot be renamed or deleted.
#### 
Add members to a workspace
  1. Navigate to the workspace's **Members** tab
  2. Click **Add to Workspace**
  3. Select an organization member and assign them a [workspace role](https://platform.claude.com/docs/en/manage-claude/workspaces#workspace-roles-and-permissions)
  4. Confirm the addition

To remove a member, click the trash icon next to their name.
Organization admins and billing members cannot be removed from workspaces while they hold those organization roles.
#### 
Set workspace limits
In the **Limits** tab, you can configure:
  * **Rate limits:** Set limits per model tier for requests per minute, input tokens, or output tokens
  * **Spend notifications:** Configure alerts when spending reaches certain thresholds

#### 
Archive a workspace
To archive a workspace, click the ellipsis menu (**...**) and select **Archive**. Archiving:
  * Preserves historical data for reporting
  * Deactivates the workspace and all associated API keys
  * Cannot be undone


Archiving a workspace immediately revokes all API keys in that workspace. This action cannot be undone. If you archive the [Claude Code workspace](https://platform.claude.com/docs/en/manage-claude/workspaces#claude-code-workspace), members of your organization can no longer sign in to Claude Code through Console billing.
### 
Using the Admin API
Programmatically manage workspaces using the [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api).
Admin API endpoints require an Admin API key (starting with `sk-ant-admin...`) that differs from standard API keys. See [Create an Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys) for how to provision one.
cURL

# Create a workspace
curl --request POST "https://api.anthropic.com/v1/organizations/workspaces" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{"name": "Production"}'

# List workspaces
curl "https://api.anthropic.com/v1/organizations/workspaces?limit=10&include_archived=false" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

# Archive a workspace
curl --request POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/archive" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

For complete parameter details and response schemas, see the [Workspaces API reference](https://platform.claude.com/docs/en/api/admin-api/workspaces/get-workspace).
### 
Managing workspace members
Add, update, or remove members from a workspace:
cURL

# Add a member to a workspace
curl --request POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{
    "user_id": "user_xxx",
    "workspace_role": "workspace_developer"
  }'

# Update a member's role
curl --request POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members/{user_id}" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{"workspace_role": "workspace_admin"}'

# Remove a member from a workspace
curl --request DELETE "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members/{user_id}" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

For complete parameter details, see the [Workspace Members API reference](https://platform.claude.com/docs/en/api/admin-api/workspace_members/get-workspace-member).
API keys and resource scoping
API keys are scoped to a specific workspace. When you create an API key in a workspace, it can only access resources within that workspace.
Resources scoped to workspaces include:
  * **Files** created through the [Files API](https://platform.claude.com/docs/en/build-with-claude/files)
  * **Message Batches** created through the [Batch API](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
  * **Skills** created through the [Skills API](https://platform.claude.com/docs/en/build-with-claude/skills-guide)

Some resources are managed at the organization level and cannot be managed with a workspace API key:
  * **[MCP tunnels](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview)** are managed with an org-scoped OAuth token (`org:manage_tunnels`) obtained through [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation), not a workspace API key, and the cap of 10 active tunnels applies organization-wide. Tunnel management requires a role with tunnel management permissions; organization developers can view but not change them. Tunnels are created in a workspace, and the Console **MCP tunnels** list and the Managed Agent server picker show tunnels in the current workspace only.
  * **Workspaces** themselves and **organization members** are managed through the [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api), which requires an Admin API key.

[Prompt caches](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) are also isolated per workspace on the Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), and [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry) (where Claude is in beta). On Amazon Bedrock and Google Cloud, prompt caches are isolated per organization.

To retrieve your organization's workspace IDs, use the [List Workspaces](https://platform.claude.com/docs/en/api/admin-api/workspaces/list-workspaces) endpoint, or find them in the [Claude Console](https://platform.claude.com/settings/workspaces).
Workspace limits
You can set custom spend and rate limits for each workspace to protect against overuse and ensure fair resource distribution.
### 
Setting workspace limits
Workspace limits can be set lower than (but not higher than) your organization's limits:
  * **Spend limits:** Cap monthly spending for a workspace
  * **Rate limits:** Limit requests per minute, input tokens per minute, or output tokens per minute

  * You cannot set limits on the Default Workspace
  * If not set, workspace limits match the organization's limits
  * Organization-wide limits always apply, even if workspace limits add up to more

For detailed information on rate limits and how they work, see [Rate limits](https://platform.claude.com/docs/en/api/rate-limits). You can also read your current organization and workspace rate limits programmatically with the [Rate Limits API](https://platform.claude.com/docs/en/manage-claude/rate-limits-api).
Usage and cost tracking
Track usage and costs by workspace using the [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api):
cURL

curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-01T00:00:00Z&\
ending_at=2025-01-08T00:00:00Z&\
workspace_ids[]=wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ&\
group_by[]=workspace_id&\
bucket_width=1d" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

Usage and costs attributed to the Default Workspace have a `null` value for `workspace_id`.
Common use cases
### 
Environment separation
Create separate workspaces for development, staging, and production:  
| Workspace  | Purpose  |  
| --- | --- |  
| Development  | Testing and experimentation with lower rate limits  |  
| Staging  | Pre-production testing with production-like limits  |  
| Production  | Live traffic with full rate limits and monitoring  |  
### 
Team or department isolation
Assign workspaces to different teams for cost allocation and access control:
  * **Engineering team** with developer access
  * **Data science team** with their own API keys
  * **Support team** with limited access for customer tools

### 
Project-based organization
Create workspaces for specific projects or products to track usage and costs separately.
Best practices
  1. 1
Plan your workspace structure
Consider how you'll organize workspaces before creating them. Think about billing, access control, and usage tracking needs.
  2. 2
Use meaningful names
Name workspaces clearly to indicate their purpose (for example, "Production - Customer Chatbot", "Dev - Internal Tools").
  3. 3
Set appropriate limits
Configure spend and rate limits to prevent unexpected costs and ensure fair resource distribution.
  4. 4
Audit access regularly
Review workspace membership periodically to ensure only appropriate users have access.
  5. 5
Monitor usage
Use the [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api) to track workspace-level consumption.

FAQ
### What's the Default Workspace?
### What's the Claude Code workspace?
### Are there limits on workspaces?
### How do organization roles affect workspace access?
### Which roles can be assigned in workspaces?
### Can organization admin or billing members' workspace roles be changed?
### What happens to workspace access when organization roles change?
### What happens to API keys when a user is removed from a workspace?
See also
  * [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api)
  * [Admin API reference](https://platform.claude.com/docs/en/api/admin)
  * [Rate limits](https://platform.claude.com/docs/en/api/rate-limits)
  * [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)

  * [How workspaces work](https://platform.claude.com/docs/en/manage-claude/workspaces#how-workspaces-work)
  * [Claude Code workspace](https://platform.claude.com/docs/en/manage-claude/workspaces#claude-code-workspace)
  * [Workspace roles and permissions](https://platform.claude.com/docs/en/manage-claude/workspaces#workspace-roles-and-permissions)
  * [Role inheritance](https://platform.claude.com/docs/en/manage-claude/workspaces#role-inheritance)
  * [Managing workspaces](https://platform.claude.com/docs/en/manage-claude/workspaces#managing-workspaces)
  * [Using the Console](https://platform.claude.com/docs/en/manage-claude/workspaces#using-the-console)
  * [Using the Admin API](https://platform.claude.com/docs/en/manage-claude/workspaces#using-the-admin-api)
  * [Managing workspace members](https://platform.claude.com/docs/en/manage-claude/workspaces#managing-workspace-members)
  * [API keys and resource scoping](https://platform.claude.com/docs/en/manage-claude/workspaces#api-keys-and-resource-scoping)
  * [Workspace limits](https://platform.claude.com/docs/en/manage-claude/workspaces#workspace-limits)
  * [Setting workspace limits](https://platform.claude.com/docs/en/manage-claude/workspaces#setting-workspace-limits)
  * [Usage and cost tracking](https://platform.claude.com/docs/en/manage-claude/workspaces#usage-and-cost-tracking)
  * [Common use cases](https://platform.claude.com/docs/en/manage-claude/workspaces#common-use-cases)
  * [Environment separation](https://platform.claude.com/docs/en/manage-claude/workspaces#environment-separation)
  * [Team or department isolation](https://platform.claude.com/docs/en/manage-claude/workspaces#team-or-department-isolation)
  * [Project-based organization](https://platform.claude.com/docs/en/manage-claude/workspaces#project-based-organization)
  * [Best practices](https://platform.claude.com/docs/en/manage-claude/workspaces#best-practices)
  * [FAQ](https://platform.claude.com/docs/en/manage-claude/workspaces#faq)
  * [See also](https://platform.claude.com/docs/en/manage-claude/workspaces#see-also)

Admin/Organization
# Workspaces
Organize API keys, manage team access, and control costs with workspaces.
Workspaces provide a way to organize your API usage within an organization. Use workspaces to separate different projects, environments, or teams while maintaining centralized billing and administration.
How workspaces work
Every organization has a **Default Workspace** that cannot be renamed, archived, or deleted. When you create additional workspaces, you can assign API keys, members, and resource limits to each one.
Key characteristics:
  * **Workspace identifiers** use the `wrkspc_` prefix (for example, `wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ`)
  * **Maximum 100 workspaces** per organization (archived workspaces don't count)
  * **Default Workspace** has no ID and doesn't appear in list endpoints
  * **API keys** are scoped to a single workspace and can only access resources within that workspace

### 
Claude Code workspace
When a member of your organization first signs in to [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) with their Claude Console account, Anthropic automatically creates a **Claude Code** workspace in the organization and adds that member to it. Every subsequent member who signs in to Claude Code is added the same way.
The Claude Code workspace keeps Claude Code traffic separate from your other API workloads:
  * Claude Code mints a per-user API key in this workspace at sign-in. You cannot create keys in it manually from the Console.
  * A Claude Code key stops working if its owner is removed from the workspace or organization, unlike standard workspace keys.
  * Claude Code usage is rate-limited separately, and admins can cap its share of the organization's limits under [Settings > Workspaces](https://platform.claude.com/settings/workspaces).
  * It is the only workspace that supports per-user monthly spend limits.


Archiving the Claude Code workspace disables Claude Code sign-in through Console billing for the whole organization.
Workspace roles and permissions
Members can have different roles in each workspace, allowing fine-grained access control.  
| Role  | Permissions  |  
| --- | --- |  
| Workspace User  | Use the Workbench only  |  
| Workspace Limited Developer  | Create and manage API keys, use the API. Cannot access session tracing views or download files.  |  
| Workspace Developer  | Create and manage API keys, use the API  |  
| Workspace Admin  | Full control over workspace settings and members  |  
| Workspace Billing  | View workspace billing information (inherited from organization billing role)  |  
### 
Role inheritance
  * **Organization admins** automatically receive Workspace Admin access to all workspaces
  * **Organization billing members** automatically receive Workspace Billing access to all workspaces
  * **Organization users and developers** must be explicitly added to each workspace

The Workspace Billing role cannot be manually assigned. It's inherited from having the organization billing role.
Managing workspaces
Only organization admins can create workspaces. Organization users and developers must be added to workspaces by an admin.
### 
Using the Console
Create and manage workspaces in the [Claude Console](https://platform.claude.com/settings/workspaces).
#### 
Create a workspace
  1. 1
Open workspace settings
In the Claude Console, go to **Settings > Workspaces**.
  2. 2
Create a workspace
Click **Create workspace**.
  3. 3
Configure the workspace
Enter a workspace name and select a color for visual identification.
  4. 4
Create the workspace
Click **Create** to finalize.


To switch between workspaces in the Console, use the **Workspaces** selector in the top-left corner.
#### 
Edit workspace details
To modify a workspace's name or color:
  1. Select the workspace from the list
  2. Click the ellipsis menu (**...**) and choose **Edit details**
  3. Update the name or color and save your changes

The Default Workspace cannot be renamed or deleted.
#### 
Add members to a workspace
  1. Navigate to the workspace's **Members** tab
  2. Click **Add to Workspace**
  3. Select an organization member and assign them a [workspace role](https://platform.claude.com/docs/en/manage-claude/workspaces#workspace-roles-and-permissions)
  4. Confirm the addition

To remove a member, click the trash icon next to their name.
Organization admins and billing members cannot be removed from workspaces while they hold those organization roles.
#### 
Set workspace limits
In the **Limits** tab, you can configure:
  * **Rate limits:** Set limits per model tier for requests per minute, input tokens, or output tokens
  * **Spend notifications:** Configure alerts when spending reaches certain thresholds

#### 
Archive a workspace
To archive a workspace, click the ellipsis menu (**...**) and select **Archive**. Archiving:
  * Preserves historical data for reporting
  * Deactivates the workspace and all associated API keys
  * Cannot be undone


Archiving a workspace immediately revokes all API keys in that workspace. This action cannot be undone. If you archive the [Claude Code workspace](https://platform.claude.com/docs/en/manage-claude/workspaces#claude-code-workspace), members of your organization can no longer sign in to Claude Code through Console billing.
### 
Using the Admin API
Programmatically manage workspaces using the [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api).
Admin API endpoints require an Admin API key (starting with `sk-ant-admin...`) that differs from standard API keys. See [Create an Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys) for how to provision one.
cURL

# Create a workspace
curl --request POST "https://api.anthropic.com/v1/organizations/workspaces" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{"name": "Production"}'

# List workspaces
curl "https://api.anthropic.com/v1/organizations/workspaces?limit=10&include_archived=false" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

# Archive a workspace
curl --request POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/archive" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

For complete parameter details and response schemas, see the [Workspaces API reference](https://platform.claude.com/docs/en/api/admin-api/workspaces/get-workspace).
### 
Managing workspace members
Add, update, or remove members from a workspace:
cURL

# Add a member to a workspace
curl --request POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{
    "user_id": "user_xxx",
    "workspace_role": "workspace_developer"
  }'

# Update a member's role
curl --request POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members/{user_id}" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{"workspace_role": "workspace_admin"}'

# Remove a member from a workspace
curl --request DELETE "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members/{user_id}" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

For complete parameter details, see the [Workspace Members API reference](https://platform.claude.com/docs/en/api/admin-api/workspace_members/get-workspace-member).
API keys and resource scoping
API keys are scoped to a specific workspace. When you create an API key in a workspace, it can only access resources within that workspace.
Resources scoped to workspaces include:
  * **Files** created through the [Files API](https://platform.claude.com/docs/en/build-with-claude/files)
  * **Message Batches** created through the [Batch API](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
  * **Skills** created through the [Skills API](https://platform.claude.com/docs/en/build-with-claude/skills-guide)

Some resources are managed at the organization level and cannot be managed with a workspace API key:
  * **[MCP tunnels](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview)** are managed with an org-scoped OAuth token (`org:manage_tunnels`) obtained through [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation), not a workspace API key, and the cap of 10 active tunnels applies organization-wide. Tunnel management requires a role with tunnel management permissions; organization developers can view but not change them. Tunnels are created in a workspace, and the Console **MCP tunnels** list and the Managed Agent server picker show tunnels in the current workspace only.
  * **Workspaces** themselves and **organization members** are managed through the [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api), which requires an Admin API key.

[Prompt caches](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) are also isolated per workspace on the Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), and [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry) (where Claude is in beta). On Amazon Bedrock and Google Cloud, prompt caches are isolated per organization.

To retrieve your organization's workspace IDs, use the [List Workspaces](https://platform.claude.com/docs/en/api/admin-api/workspaces/list-workspaces) endpoint, or find them in the [Claude Console](https://platform.claude.com/settings/workspaces).
Workspace limits
You can set custom spend and rate limits for each workspace to protect against overuse and ensure fair resource distribution.
### 
Setting workspace limits
Workspace limits can be set lower than (but not higher than) your organization's limits:
  * **Spend limits:** Cap monthly spending for a workspace
  * **Rate limits:** Limit requests per minute, input tokens per minute, or output tokens per minute

  * You cannot set limits on the Default Workspace
  * If not set, workspace limits match the organization's limits
  * Organization-wide limits always apply, even if workspace limits add up to more

For detailed information on rate limits and how they work, see [Rate limits](https://platform.claude.com/docs/en/api/rate-limits). You can also read your current organization and workspace rate limits programmatically with the [Rate Limits API](https://platform.claude.com/docs/en/manage-claude/rate-limits-api).
Usage and cost tracking
Track usage and costs by workspace using the [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api):
cURL

curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-01T00:00:00Z&\
ending_at=2025-01-08T00:00:00Z&\
workspace_ids[]=wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ&\
group_by[]=workspace_id&\
bucket_width=1d" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

Usage and costs attributed to the Default Workspace have a `null` value for `workspace_id`.
Common use cases
### 
Environment separation
Create separate workspaces for development, staging, and production:  
| Workspace  | Purpose  |  
| --- | --- |  
| Development  | Testing and experimentation with lower rate limits  |  
| Staging  | Pre-production testing with production-like limits  |  
| Production  | Live traffic with full rate limits and monitoring  |  
### 
Team or department isolation
Assign workspaces to different teams for cost allocation and access control:
  * **Engineering team** with developer access
  * **Data science team** with their own API keys
  * **Support team** with limited access for customer tools

### 
Project-based organization
Create workspaces for specific projects or products to track usage and costs separately.
Best practices
  1. 1
Plan your workspace structure
Consider how you'll organize workspaces before creating them. Think about billing, access control, and usage tracking needs.
  2. 2
Use meaningful names
Name workspaces clearly to indicate their purpose (for example, "Production - Customer Chatbot", "Dev - Internal Tools").
  3. 3
Set appropriate limits
Configure spend and rate limits to prevent unexpected costs and ensure fair resource distribution.
  4. 4
Audit access regularly
Review workspace membership periodically to ensure only appropriate users have access.
  5. 5
Monitor usage
Use the [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api) to track workspace-level consumption.

FAQ
### What's the Default Workspace?
### What's the Claude Code workspace?
### Are there limits on workspaces?
### How do organization roles affect workspace access?
### Which roles can be assigned in workspaces?
### Can organization admin or billing members' workspace roles be changed?
### What happens to workspace access when organization roles change?
### What happens to API keys when a user is removed from a workspace?
See also
  * [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api)
  * [Admin API reference](https://platform.claude.com/docs/en/api/admin)
  * [Rate limits](https://platform.claude.com/docs/en/api/rate-limits)
  * [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)
