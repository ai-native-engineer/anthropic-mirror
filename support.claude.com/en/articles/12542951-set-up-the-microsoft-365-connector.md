<!-- source: https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector -->

# Set up the Microsoft 365 connector

Updated over 2 weeks ago

This article walks admins through enabling the Microsoft 365 connector for their organization in Claude—including granting Microsoft Entra consent, restricting access, and managing permissions. Once setup is complete, people in your tenant can connect Microsoft 365 to their own Claude accounts and search across SharePoint, OneDrive, Outlook, and Teams from Claude.

The Microsoft 365 connector is available on all Claude plans: Free, Pro, Max, Team, and Enterprise.

For end-user instructions on connecting and using Microsoft 365 once setup is complete, see **[Connect Claude to Microsoft 365](https://support.claude.com/en/articles/15183774-)**.

**Important:** The Microsoft 365 connector requires a Microsoft Entra tenant tied to a Microsoft Business plan. Personal Microsoft accounts (such as @outlook.com or @hotmail.com addresses) can't be used to connect.

##

## Setup overview

Two things need to happen before anyone in your organization can connect Microsoft 365:

1. **On Team and Enterprise plans:** A Claude organization owner enables the Microsoft 365 connector for the organization.
2. **In every tenant:** A Microsoft Entra Global Administrator grants a one-time consent that authorizes the integration for your tenant.

Once both are done, members can connect Microsoft 365 to their own Claude accounts following the steps in **[Connect Claude to Microsoft 365](https://support.claude.com/en/articles/15183774-)**.

## Enable the connector for your organization

This step applies to Team and Enterprise plans only. On Free, Pro, and Max plans, skip to the next section.

1. Sign in to Claude.
2. Navigate to **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**.
3. Click “+ Add” at the top of the page, then “All available.”
4. Find **Microsoft 365** and click “Add to your team.”

## Grant Microsoft Entra admin consent

A Microsoft Entra Global Administrator in your tenant needs to authorize the integration before anyone can connect. There are two ways to do this.

### Option 1: Consent through Claude

If your Microsoft Entra Global Administrator has a Claude account, they can grant consent during the standard connection flow:

1. Navigate to **[Customize > Connectors](http://claude.ai/customize/connectors)**.
2. Find **Microsoft 365** and click “Connect.”
3. Authenticate with Microsoft 365 credentials.
4. Review and accept the requested permissions, checking the box to grant access on behalf of the whole organization.

After this, other people in the same Entra tenant can connect by following the standard end-user steps. They won't see the consent prompt—they'll just authenticate and start using the integration.

### Option 2: Manual setup in Microsoft Entra ID

Use this path if your Microsoft Entra Global Administrator doesn't have a Claude account, or if you need to troubleshoot the app install and permissions setup. You can add the connector apps and grant admin consent directly in Microsoft Entra ID.

This process adds two service principals to your tenant. Each principal establishes a service-level identity for one of the two M365 MCP for Claude app registrations, allowing them to access and interact with your organization's data and resources via the Microsoft Graph API.

**1. Add the service principals**

Using Microsoft Graph Explorer, add both required service principals:

M365 MCP Client for Claude:

```
POST https://graph.microsoft.com/v1.0/servicePrincipals  
{"appId":"08ad6f98-a4f8-4635-bb8d-f1a3044760f0"}
```

M365 MCP Server for Claude:

```
POST https://graph.microsoft.com/v1.0/servicePrincipals  
{"appId":"07c030f6-5743-41b7-ba00-0a6e85f37c17"}
```

**2. Grant admin consent**

Construct and visit the following URLs in your browser, replacing {your-tenant-id} with your organization's tenant ID.

M365 MCP Client for Claude:

```
https://login.microsoftonline.com/{your-tenant-id}/adminconsent?client_id=08ad6f98-a4f8-4635-bb8d-f1a3044760f0
```

M365 MCP Server for Claude:

```
https://login.microsoftonline.com/{your-tenant-id}/adminconsent?client_id=07c030f6-5743-41b7-ba00-0a6e85f37c17
```

When you visit each URL, you'll be prompted to consent to the delegated permissions required by the integration on behalf of your organization.

**3. Finish setup**

* **Team and Enterprise plans:** A Claude organization Owner needs to enable the connector in **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**. Then members can connect individually.
* **Free, Pro, and Max plans:** Members can connect by navigating to **[Customize > Connectors](http://claude.ai/customize/connectors)**, finding **Microsoft 365**, and clicking “Connect.”

### Restrict who can use the connector

To limit which people in your tenant can authenticate to Microsoft 365 through Claude:

1. Go to the Microsoft Entra admin center at entra.microsoft.com.
2. Navigate to the **M365 MCP Server for Claude** enterprise application.
3. Go to **Properties** and set **Assignment required?** to “Yes.”
4. Under **Users and groups**, add the specific users or groups who should have access.
5. Repeat the same steps for the **M365 MCP Client for Claude** enterprise application.

Both components need to be restricted to the same set of authorized people.

### Restrict which permissions the connector can use

To limit which types of resources the integration can access, selectively revoke permissions from the default set of authorized scopes. This requires Microsoft Entra admin access.

1. As a Microsoft Entra admin, go to entra.admin.com.
2. Select “Enterprise Applications.”
3. Next to the search box, remove the application type filter.
4. Search for and click “M365 MCP Server for Claude.”
5. Go to **Permissions**.
6. Under the **Admin consent** tab and in the Microsoft Graph list of permissions, select the permission you would like to revoke and click the “**…**” button.
7. Select “Revoke permission” and confirm with “Yes, revoke.”

Once revoked, attempts to access a resource with that permission will return a "Failed to call tool" error.

Members can also individually turn off specific tools in their own Microsoft 365 settings to prevent Claude from trying to access a tool for which the permission has been revoked.

To restore a revoked permission, follow the steps to grant admin consent described in **Option 2: Manual setup in Microsoft Entra ID**. This will revert the permissions to the default state.

##

## Permissions reference

The Microsoft 365 connector uses **delegated permissions**, meaning Claude acts on behalf of each individual user and can only access data that user already has permission to view in Microsoft 365. Permissions are read-only—Claude can't modify, delete, or create content in your tenant.

During authentication, the integration requests the following permissions:

**Basic access**

* `User.Read`: Sign in and read user profile
* `openid`: Sign in with organizational account
* `offline_access`: Maintain access to data
* `email`: View email address
* `profile`: View basic profile information

**Email (Outlook)**

* `Mail.Read`: Read email messages
* `Mail.ReadBasic`: Read email metadata (sender, subject, date)
* `Mail.Read.Shared`: Read emails in mailboxes the user has access to
* `MailboxFolder.Read`: Read mailbox folder structure
* `MailboxItem.Read`: Read items in mailbox

**Note:** Shared mailbox access is included through the `Mail.Read.Shared` permission. Members can search shared mailboxes they have delegate access to in Microsoft 365, including full access and folder-level delegation. No setup is needed beyond standard admin consent and the delegate permissions already configured in Microsoft 365.

**Calendar**

* `Calendars.Read`: Read calendar events
* `Calendars.Read.Shared`: Read calendars shared with the user

**Teams chat**

* `Chat.Read`: Read Teams chat messages
* `Chat.ReadBasic`: Read Teams chat metadata
* `ChatMember.Read`: Read information about chat participants
* `ChatMessage.Read`: Read Teams chat messages

**Teams channels**

* `Channel.ReadBasic.All`: Read channel names and descriptions
* `ChannelMessage.Read.All`: Read channel messages

**Meetings**

* `OnlineMeetings.Read`: Read online meetings
* `OnlineMeetingTranscript.Read.All`: Read meeting transcripts
* `OnlineMeetingAiInsight.Read`: Read AI-generated meeting insights
* `OnlineMeetingArtifact.Read.All`: Read meeting recordings and artifacts
* `OnlineMeetingRecording.Read.All`: Read meeting recordings

**Files (OneDrive and SharePoint)**

* `Files.Read`: Read user files
* `Files.Read.All`: Read all files the user can access
* `Sites.Read.All`: Read items in SharePoint sites

**User directory**

* `User.ReadBasic.All`: Read basic profile information for all users in the organization (used for finding meeting availability)

The Microsoft 365 connector searches SharePoint across the entire tenant using the permissions of the user. Site-specific search restriction isn't supported.

## Privacy and security

* **Permission inheritance:** Claude mirrors each user's existing Microsoft 365 permissions. Members can't access anything through Claude that they couldn't already see directly in Microsoft 365.
* **On-demand access:** Claude only accesses data when a user explicitly asks a question that requires it.
* **Revocable access:** Members can disconnect their own integration through **[Customize > Connectors](http://claude.ai/customize/connectors)**. Team and Enterprise plan Owners can also remove the connector for the entire organization in **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**.

For more detail, see the **[Microsoft 365 connector security guide](https://support.claude.com/en/articles/12684923-)**.

##

## Troubleshooting

### A member can't authenticate

1. Confirm their account is tied to a Microsoft Entra tenant, not a personal Microsoft account.
2. Confirm their Microsoft 365 license is active.
3. Confirm admin consent has been granted using Option 1 or Option 2 above.
4. Check whether organizational policies (such as conditional access) are blocking third-party app authentication.

### Members are seeing "Failed to call tool" errors

A permission may have been selectively revoked in Microsoft Entra. Members can turn off the corresponding tool in their Microsoft 365 settings to suppress the error, or you can restore the permission by repeating the admin consent steps in **Option 2: Manual setup in Microsoft Entra ID**.

##

## Frequently asked questions

### What happens if a member tries to connect before consent is granted?

They'll see an error message indicating that an administrator must grant app permissions before they can use the integration. The connection will fail until a Microsoft Entra Global Administrator approves the necessary permissions.

### Can the Microsoft 365 connector be used with enterprise search?

Yes. When enterprise search is enabled, it can query Microsoft 365 alongside other connected services for unified search across Slack, Google Workspace, Microsoft 365, and more.

### Can the integration modify Microsoft 365 data?

No. All permissions are read-only. Claude can search and analyze Microsoft 365 data but can't create, edit, or delete documents; send emails or calendar invites; modify SharePoint sites or OneDrive files; or change Teams settings or permissions.

[Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)[Microsoft 365 connector security guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide)[Use Claude for Microsoft 365 with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-microsoft-365-with-third-party-platforms)[MCP connectors](https://support.claude.com/en/articles/14503689-mcp-connectors)[Connect to Microsoft 365](https://support.claude.com/en/articles/15183774-connect-to-microsoft-365)
