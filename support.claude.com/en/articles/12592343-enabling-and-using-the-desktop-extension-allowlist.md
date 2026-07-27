<!-- source: https://support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist -->

# Enabling and using the desktop extension allowlist

March 16, 2026

The desktop extension allowlist is available for Owners and Primary Owners of Team and Enterprise plans.

This article introduces a desktop extension allowlist that Team and Enterprise plan Owners can use to manage their organization’s access to extensions.

## How to enable the allowlist

**Important:** If you’ve previously configured Enterprise policy controls at the user-machine level, these will override the in-app allowlist. Ensure both `isDesktopExtensionDirectoryEnabled` and `isDesktopExtensionEnabled` are not set to "false" so the allowlist can populate the available registry. Refer to our **[desktop enterprise configuration documentation](https://support.claude.com/en/articles/12622667-enterprise-configuration)** for more information.

The desktop extension allowlist is disabled by default, so an organization Owner will need to switch it on manually. Note that **users will be able to access all desktop extensions in the registry until you enable the allowlist.** To prevent this, ensure you activate the allowlist to block all desktop extensions by default, then add only the extensions your team needs access to.

**To turn on the allowlist:**

1. Open Claude Desktop
2. Click your initials or name in the lower left corner
3. Navigate to Organization settings > Connectors
4. Switch to the "Desktop" tab:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781755172/63c92550571842577ad435860ec5/6f5cc4e1-ff7d-48de-863a-c4e6184d4605?expires=1784923200&signature=53e91bc92372dcf0af5f121ae658ec3d29514735f382b370c8dea98704b28508&req=dScvF857mIBYW%2FMW1HO4zQ9pXU4D%2FXPZ0ugSQm1MFW8%2BFSCrk32%2BjhfxZRhg%0A8UCK%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781755172/63c92550571842577ad435860ec5/6f5cc4e1-ff7d-48de-863a-c4e6184d4605?expires=1784923200&signature=53e91bc92372dcf0af5f121ae658ec3d29514735f382b370c8dea98704b28508&req=dScvF857mIBYW%2FMW1HO4zQ9pXU4D%2FXPZ0ugSQm1MFW8%2BFSCrk32%2BjhfxZRhg%0A8UCK%0A)
5. Toggle **Allowlist** on:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781755578/a6bafff5f084dc86ae463703fd3d/6cf0ee18-4e71-4129-98e8-cc08174e3c3a?expires=1784923200&signature=d26189db65e0ab2d93425bd90b66a27252e7756b5a7138f751500b8bd1a0c343&req=dScvF857mIRYUfMW1HO4zaj0BHUiS6QGTAorLxpdoc%2BM%2Bgob5TO%2F482jffin%0Awn8h%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781755578/a6bafff5f084dc86ae463703fd3d/6cf0ee18-4e71-4129-98e8-cc08174e3c3a?expires=1784923200&signature=d26189db65e0ab2d93425bd90b66a27252e7756b5a7138f751500b8bd1a0c343&req=dScvF857mIRYUfMW1HO4zaj0BHUiS6QGTAorLxpdoc%2BM%2Bgob5TO%2F482jffin%0Awn8h%0A)

## What happens after enabling the allowlist?

Once the allowlist is enabled:

* Any existing desktop extension installations will be force-deleted from Claude Desktop clients.
* Users will no longer be able to install new desktop extensions that are not included within the allowlist.
* Users can only download extensions from the sanctioned in-app registry; they can no longer drag or click to install MCPBs.

Note that the allowlist does not guard against individuals tampering with local MCP file contents after installation.

Consider completing the allowlist setup during off-hours to minimize disruption to existing users. If a user's installed extension is deleted while the allowlist is being configured, they will need to manually re-install the extension.

**Important:** The allowlist requires Claude Desktop version 0.13.91 or higher, so users should update the desktop app by clicking “Claude”, then either “Check for updates” or “Restart to update to Claude 0.13.91”:

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781756960/ad18af50c83d35f2673656c23e00/a7ee450f-0c7d-42d6-a75f-fb1bc088cb52?expires=1784923200&signature=ac048331728cadded83c276407741f3e2aedbebecd1f4b58499e8b1f9fe73a95&req=dScvF857m4hZWfMW1HO4zYUJqYejCDHpCEDZ5AdBjIbjIQ7O7X8O4Nj%2FmXTV%0AeE3T5gB%2FtKW737i4wpw%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781756960/ad18af50c83d35f2673656c23e00/a7ee450f-0c7d-42d6-a75f-fb1bc088cb52?expires=1784923200&signature=ac048331728cadded83c276407741f3e2aedbebecd1f4b58499e8b1f9fe73a95&req=dScvF857m4hZWfMW1HO4zYUJqYejCDHpCEDZ5AdBjIbjIQ7O7X8O4Nj%2FmXTV%0AeE3T5gB%2FtKW737i4wpw%3D%0A)

## Managing allowed extensions

After enabling the allowlist, you can choose which extensions to allow:

1. Navigate to Organization settings > Connectors and select the “Desktop” tab.
2. Click “Browse extensions” to view the list of available extensions.
3. Select the extension you want to add.
4. Click the “Add to your team” button.
5. The extension will appear in your allowlist.

If you want to remove an extension from the allowlist, click the “...” button and “Remove from allowlist.”

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781751250/6558c0f59aea7976bd44b0213d76/e750f02b-cd0d-437e-a83f-9ac362cdf456?expires=1784923200&signature=1d9e2028174e69e21cce9a43849da65fa3261ae3370ea2e158cf633ab9dd5af8&req=dScvF857nINaWfMW1HO4zTrxBawg%2FVSXqXridZhfx1JV2pe4LTaFU5lYMwHX%0AzzlxZ2D%2FMfcQCOvPiL0%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781751250/6558c0f59aea7976bd44b0213d76/e750f02b-cd0d-437e-a83f-9ac362cdf456?expires=1784923200&signature=1d9e2028174e69e21cce9a43849da65fa3261ae3370ea2e158cf633ab9dd5af8&req=dScvF857nINaWfMW1HO4zTrxBawg%2FVSXqXridZhfx1JV2pe4LTaFU5lYMwHX%0AzzlxZ2D%2FMfcQCOvPiL0%3D%0A)

## Uploading custom extensions

You can also upload custom extensions to deploy across your organization via Organization settings > Connectors > Desktop.

**Note:** Ensure the name field in the manifest.json does not overlap with any existing MCPBs. All names for unique MCPBs / desktop extensions must be unique.

1. Click “Add custom extension”
2. This will open a filepicker; select the .mcpb file.
3. The extension will appear under **Custom team extensions**.
4. Click "...” then “Add to team” to add it to your allowlist and enable it for your team.

When you allowlist a custom extension, it's scoped to your specific organization and can't be used across other organizations. For more in-depth information about creating custom extensions with MCP Bundles (.mcpb), please refer to our **[desktop extension developer documentation](https://github.com/anthropics/mcpb)**.

## Updating custom extensions

We’ve also introduced the ability to update previously-installed custom extensions to new versions without having to remove and reinstall them.

You can update a new MCPB version by making changes to manifest.json, ensuring the version field for the update candidate is incremented from the current uploaded version, and that you leave the name value unchanged. Changing the name will create a new custom desktop extension rather than uploading a new version. Then navigate to the custom upload pane, select "Upload new version" via the kebab menu, and upload the new file.

* [Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)
* [Deploy Claude Desktop for macOS](https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos)
* [Enterprise configuration for Claude Desktop](https://support.claude.com/en/articles/12622667-enterprise-configuration-for-claude-desktop)
* [Deploying enterprise-grade MCP servers with desktop extensions](https://support.claude.com/en/articles/12702546-deploying-enterprise-grade-mcp-servers-with-desktop-extensions)
* [Claude in Chrome admin controls](https://support.claude.com/en/articles/13065128-claude-in-chrome-admin-controls)
