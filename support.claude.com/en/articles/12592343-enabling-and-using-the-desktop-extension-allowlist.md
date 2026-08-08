<!-- source: https://support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist -->

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

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781755172/63c92550571842577ad435860ec5/6f5cc4e1-ff7d-48de-863a-c4e6184d4605?expires=1786167000&signature=e5d204f6fdd52f3d9a49d7b59a3d99477cdff816c23357d41548e1a09024d594&req=dScvF857mIBYW%2FMW1HO4zQ9pXUwL%2BXfb0ugSQm1MFW%2Bfn212qAM1xB8u0ZbO%0AGf6q%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781755172/63c92550571842577ad435860ec5/6f5cc4e1-ff7d-48de-863a-c4e6184d4605?expires=1786167000&signature=e5d204f6fdd52f3d9a49d7b59a3d99477cdff816c23357d41548e1a09024d594&req=dScvF857mIBYW%2FMW1HO4zQ9pXUwL%2BXfb0ugSQm1MFW%2Bfn212qAM1xB8u0ZbO%0AGf6q%0A)
5. Toggle **Allowlist** on:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781755578/a6bafff5f084dc86ae463703fd3d/6cf0ee18-4e71-4129-98e8-cc08174e3c3a?expires=1786167000&signature=14b53dd3c916e61cdcc1c8d4797cefa3c5ae53d3265b1accd9d21e3d1d275baa&req=dScvF857mIRYUfMW1HO4zaj0BHcqT6AETAorLxpdoc%2FIk%2B9B91g16lNvFh0A%0A901t%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781755578/a6bafff5f084dc86ae463703fd3d/6cf0ee18-4e71-4129-98e8-cc08174e3c3a?expires=1786167000&signature=14b53dd3c916e61cdcc1c8d4797cefa3c5ae53d3265b1accd9d21e3d1d275baa&req=dScvF857mIRYUfMW1HO4zaj0BHcqT6AETAorLxpdoc%2FIk%2B9B91g16lNvFh0A%0A901t%0A)

## What happens after enabling the allowlist?

Once the allowlist is enabled:

* Any existing desktop extension installations will be force-deleted from Claude Desktop clients.
* Users will no longer be able to install new desktop extensions that are not included within the allowlist.
* Users can only download extensions from the sanctioned in-app registry; they can no longer drag or click to install MCPBs.

Note that the allowlist does not guard against individuals tampering with local MCP file contents after installation.

Consider completing the allowlist setup during off-hours to minimize disruption to existing users. If a user's installed extension is deleted while the allowlist is being configured, they will need to manually re-install the extension.

**Important:** The allowlist requires Claude Desktop version 0.13.91 or higher, so users should update the desktop app by clicking “Claude”, then either “Check for updates” or “Restart to update to Claude 0.13.91”:

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781756960/ad18af50c83d35f2673656c23e00/a7ee450f-0c7d-42d6-a75f-fb1bc088cb52?expires=1786167000&signature=aaeb70bd30c2a0db889177d40fad42dece7cd3e69c3b1c3a2f65559458791f71&req=dScvF857m4hZWfMW1HO4zYUJqYWrDDXrCEDZ5AdBjIan7o6KYx06SrfNIXGQ%0AKLUI5YB7ypuCyjtz98Q%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781756960/ad18af50c83d35f2673656c23e00/a7ee450f-0c7d-42d6-a75f-fb1bc088cb52?expires=1786167000&signature=aaeb70bd30c2a0db889177d40fad42dece7cd3e69c3b1c3a2f65559458791f71&req=dScvF857m4hZWfMW1HO4zYUJqYWrDDXrCEDZ5AdBjIan7o6KYx06SrfNIXGQ%0AKLUI5YB7ypuCyjtz98Q%3D%0A)

## Managing allowed extensions

After enabling the allowlist, you can choose which extensions to allow:

1. Navigate to Organization settings > Connectors and select the “Desktop” tab.
2. Click “Browse extensions” to view the list of available extensions.
3. Select the extension you want to add.
4. Click the “Add to your team” button.
5. The extension will appear in your allowlist.

If you want to remove an extension from the allowlist, click the “...” button and “Remove from allowlist.”

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781751250/6558c0f59aea7976bd44b0213d76/e750f02b-cd0d-437e-a83f-9ac362cdf456?expires=1786167000&signature=584c12c67a985db250137bcb895ea4b5cae1ffad4134c25ea80f35ac57e152c4&req=dScvF857nINaWfMW1HO4zTrxBa4o%2BVCVqXridZhfx1JZN3GjpFMZ%2BkIA%2BNHF%0AoCZqNCu7DfxweXbLb%2Fo%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781751250/6558c0f59aea7976bd44b0213d76/e750f02b-cd0d-437e-a83f-9ac362cdf456?expires=1786167000&signature=584c12c67a985db250137bcb895ea4b5cae1ffad4134c25ea80f35ac57e152c4&req=dScvF857nINaWfMW1HO4zTrxBa4o%2BVCVqXridZhfx1JZN3GjpFMZ%2BkIA%2BNHF%0AoCZqNCu7DfxweXbLb%2Fo%3D%0A)

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
