<!-- source: https://support.claude.com/en/articles/10186004-claude-console-roles-and-permissions -->

# Claude Console roles and permissions

May 20, 2026

The Claude Console uses a role-based access system with six distinct roles: User, Claude Code User, Limited Developer, Developer, Billing, and Admin. Each role has specific permissions and capabilities designed to help teams manage their API access securely.

## Role types and permissions

### User

* Can only use Workbench
* Can view MCP tunnels
* Cannot view API keys, usage logs, or billing details

### Claude Code User

* Can use Workbench and **[Claude Code](https://code.claude.com/docs/en/overview)**
* Can access Claude Code workspace in your org
* Can view MCP tunnels

### Limited Developer

* Can use Workbench and Claude Code
* Can manage API keys and webhook endpoints
* Can view usage and cost data
* Can manage vaults and credentials
* Can view MCP tunnels  
  ​

### Developer

* Can use Workbench and Claude Code
* Can manage API keys and webhook endpoints
* Can view usage and cost data
* Can manage vaults and credentials
* Can view sessions traces
* Can download files
* Can view MCP tunnels

### Billing

* Can use Workbench
* Can manage billing details
* Can view usage and cost data
* Can view MCP tunnels
* Cannot access Claude Code workspace in your org

### Admin

* Can perform all actions available to User, Developer, and Billing roles
* Can manage users and their role assignments
* Can send events to active (non-archived) sessions
* Can create MCP tunnels

## Workspace-Level Permissions

* Organization Admins automatically receive Workspace Admin permissions in all Workspaces.
* Organization Billing role holders can view cost, usage, and limit values across all Workspaces.
* Organization-level roles serve as a baseline, while Workspace roles can grant additional permissions.

  + For example, a User at the organization level can be granted Admin permissions within specific Workspaces

## Important Notes

* Removing an Admin or Billing role does not automatically update the billing email in our payment processor.
* To modify the primary billing email address or add additional billing contact emails, please **[contact our Support Team](https://support.claude.com/en/articles/9015913-how-to-get-support)**.

[How do I pay for my Claude API usage?](https://support.claude.com/en/articles/8977456-how-do-i-pay-for-my-claude-api-usage)[Cost and Usage Reporting in the Claude Console](https://support.claude.com/en/articles/9534590-cost-and-usage-reporting-in-the-claude-console)[Creating and managing Workspaces in the Claude Console](https://support.claude.com/en/articles/9796807-creating-and-managing-workspaces-in-the-claude-console)[Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)[What is Claude Tag?](https://support.claude.com/en/articles/15594475-what-is-claude-tag)
