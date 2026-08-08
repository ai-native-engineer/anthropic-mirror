<!-- source: https://claude.com/docs/government/config/settings -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

> **Who this is for:** Tenant administrators and organization owners who set product behavior for the people they manage.

This page describes the settings on the **Config** page in the admin portal. Each setting is written once here and can be set at both the tenant and organization level unless noted otherwise. For how the levels combine, what locking does, and how to compare and preview, see [How Config works](https://claude.com/docs/government/config/overview).

##  Settings list

###  Session idle timeout

Controls how long a member can stay inactive before being signed out. The value must be a whole number of minutes, 15 or higher, and the Anthropic default is 1440 minutes (24 hours). A lower value applies at the next sign-in; a higher value applies on the next request. This is a restriction, so each level can shorten the timeout but not lengthen it past what the level above allows, and the value that takes effect is always the shortest one in the chain.

###  Permit organizations to manage their own seat tiers

Controls whether organization owners may create and edit self-managed seat tiers on the [Tiers](https://claude.com/docs/government/org-admin/seat-tiers) page, in addition to the tenant-managed ones. Only tenant administrators can change this setting; it is always read-only at the organization level, and organization owners cannot grant themselves the capability. When it is off, the **New seat tier** button and the edit and delete controls on the Tiers page are hidden, and the **Reset usage limits** action on the [Users](https://claude.com/docs/government/org-admin/users) page is also unavailable.

**Set at the tenant level only.** This setting is read-only for organization owners.

###  Compliance API

Controls whether the [Compliance API](https://claude.com/docs/government/org-admin/compliance-api) is available. When it is off, organization owners cannot create new keys and every request to the API returns an error, including requests made with keys that were valid before. Listing and revoking existing keys remains available even when this is off, so that a disabled organization can still revoke an exposed key.

**Set at the tenant level only.** This setting is read-only for organization owners.

###  Telemetry endpoint (Claude Desktop)

The address where Claude Desktop sends usage telemetry using the OpenTelemetry protocol. A matching **Telemetry endpoint (Claude for Microsoft 365)** setting covers that product. The value must be an absolute address beginning with `https://`, and its host must be a hostname or a private-network address. A public IP address is refused. Leaving the value empty disables telemetry.

###  Telemetry headers (Claude Desktop)

Additional headers, such as an authorization token, that are sent with every telemetry request. Because the value may contain a secret, it is never displayed after you save it; you see only that it is set.

###  Managed connectors (Claude Desktop)

Pre-configured connectors that are made available in Claude Desktop. A connector is an integration that extends Claude with external tools and data sources. Each entry requires a name and an address beginning with `https://`, and the address must not point at a private or internal network range. This is a collection, so entries added at each level appear alongside those from the levels above. Because entries may contain credentials, saved values are not echoed back.

###  Desktop banner

A persistent banner shown at the top of Claude Desktop. You can set the text, colors, and an optional link, and preview the result as you edit. Banner text may be up to 200 characters, leading and trailing spaces are rejected, colors must be valid hex codes, and the link (if set) must begin with `https://`. An empty banner is valid and simply hides it.
The system-use notification shown at sign-in is separate from this banner. It is fixed text and cannot be edited. Use the Desktop banner setting if you need a configurable message inside the application.

###  Product availability

A group of separate switches that control which Claude products and features are available to members. Each switch appears as its own row: **Claude Desktop**, **Chat in Claude Desktop**, **Advanced file analysis in Chat**, **Cowork in Claude Desktop**, **Code in Claude Desktop**, **Claude Code**, and **Claude for Microsoft 365**. All are on by default. Turning a switch off makes that product or feature unavailable.
The **Chat in Claude Desktop**, **Cowork in Claude Desktop**, and **Code in Claude Desktop** switches each make one part of the app available to members. Chat is for simple conversations, Cowork is for longer tasks that Claude works through on its own in a local workspace folder, and Code is for software development.
When Chat and Cowork are both available, Claude Desktop presents them together as **Home** in its sidebar, next to **Code**. From Home, a member chooses **Chat** or **Cowork** in the message box, and the sidebar lists their chats and tasks together.
Turning a switch off also changes this layout. For example, with **Chat in Claude Desktop** off, the sidebar shows **Cowork** in place of Home and the message box offers no choice, and with **Cowork in Claude Desktop** off, the message box offers Chat only. If Chat, Cowork, and Code are all turned off, Claude Desktop keeps Cowork on. There is no setting that chooses what Claude Desktop opens to, or whether the message box starts on Chat or Cowork.

This layout applies to Claude Desktop 1.26832.0 and later. Earlier versions show **Chat**, **Cowork**, and **Code** as three separate tabs, controlled by the same switches.

###  Allowed network hosts

A list of hostnames that tools in Claude Desktop may reach, for example to install packages or fetch web pages. This covers the tools Claude uses during Cowork tasks and Code sessions, and web fetch in Chat. The connection to Claude is always allowed and does not need to be listed. An empty list shows as **Claude connection only**. Use **Add package registries** to add npm, PyPI, GitHub, crates.io, and other common registries so that Claude can install libraries; hosts added this way appear together as a single **Package registries** pill with a count. This list does not cover addresses on your private network, direct IP addresses, or Web search, so do not rely on it alone to restrict network access.

###  Allowed workspace folders

Controls which folders members can pick as a project folder in Claude Desktop, and where Claude can read and write files. Leave it unset to allow any folder. Add folder paths to limit members to those locations, or check **Block all workspace folders** to allow none, in which case Claude can still work in folders it creates inside its own sandbox. You can list Windows and Mac paths together, and each device uses only the paths for its platform. An unset value shows as **Any folder** and an empty list shows as **No folders**.

##  Tool and connector cards

Alongside the settings list, the Config page shows cards for the built-in tools (Web search, Web fetch, and Shell commands), the built-in connector (Microsoft 365), a **Connectors** card for the ones you add yourself, and a **Plugins** card for plugin packages you upload. A connector is an integration that lets Claude reach an external service on a user’s behalf.
The **Web search** card controls whether Claude can search the web from Claude Desktop. It is off by default. When you turn it on you are shown a short description of how search works and asked to acknowledge it before the setting is saved. A **Require approval for each search** sub-setting sits below the toggle and becomes available once web search is on; it is on by default, and turning it off lets each user choose whether to approve every search or allow searches to run automatically.
The **Web fetch** card controls whether Claude can fetch web pages during tasks in Claude Desktop. It is on by default, and fetches are subject to the Allowed network hosts list above. A **Require approval for each fetch** sub-setting sits below the toggle; it is off by default, and turning it on asks the user to approve every page fetch before it runs.
The **Shell commands** card controls whether Claude can run shell commands in the sandbox during tasks in Claude Desktop. It is on by default, and turning it off also turns off Advanced file analysis in Chat. A **Require approval for each command** sub-setting sits below the toggle; it is off by default, and turning it on asks the user to approve every shell command before it runs.
The **Microsoft 365** card lets members reach your agency’s Microsoft 365 content, including SharePoint, OneDrive, Outlook, and Teams, from Claude Desktop. Each member signs in with their own Microsoft account. Enter the **Tenant ID** and **Client ID** from an application you register in Microsoft Entra, choose the **Azure cloud** your Microsoft tenant is in, and select which Microsoft Graph permissions to allow under **Access**. The connector is off while Tenant ID and Client ID are both blank. See [Set up the Microsoft 365 connector](https://claude.com/docs/government/connectors/microsoft-365) for the full walkthrough.
The **Connectors** card lists the Model Context Protocol servers you have added for your own systems. Each connector is defined once and applied to the products you choose. See the [Connectors](https://claude.com/docs/government/connectors/overview) page for how to add and manage them.
The **Plugins** card lets you upload plugin packages and provision them to members on Claude Desktop. A plugin bundles connectors, skills, slash commands, and sub-agents for Claude Desktop. See the [Plugins overview](https://claude.com/docs/plugins/overview) for what a plugin can contain. Plugins are delivered only to Claude Desktop.
Click **Add plugins** and drop a `.zip` file. The file can be a single plugin package or a whole marketplace archive, for example the **Download ZIP** of a GitHub repository that holds several plugins. A preview shows each plugin’s name, version, and description, and marks any plugin that declares hooks or an MCP server. In Claude for Government, a plugin’s hooks run on the member’s machine at defined points during a session; a plugin’s declared local MCP server is disabled and does not run. For those plugins, you confirm that you trust the package before it is added.
Each plugin you add appears as a row with an **Auto-install** or **Members choose** control. **Auto-install** installs the plugin for every member automatically, and **Members choose** makes it available for members to install themselves. Click the remove icon to queue a plugin for removal. Changes here are staged: nothing is applied until you click **Save changes**, and **Discard** clears the pending changes. Removing a plugin stops provisioning it, and members who already installed it keep their copy until they remove it themselves.
At the organization level, plugins the tenant has added appear under a **From levels above** heading with an **Inherited from your tenant** badge. You can see them there but cannot change or remove them. Upload a plugin with the same name at your organization level to take priority over one.

The Claude for Government deployment may include additional settings that are not listed above. Any extra setting follows the same chain, status badges, and edit and reset behavior.
