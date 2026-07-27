<!-- source: https://claude.com/docs/government/org-admin/configuration -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

> **Who this is for:** Organization owners who need to set product behavior, such as the session timeout, desktop banner, and enabled tabs, for everyone in their organization.

Use this page to view and change the product settings that apply to everyone in your organization, and to see where each effective value comes from.

##  How settings are applied

Each setting is resolved through a chain that runs from the application default, to your tenant, to your organization. If you don’t set a value here, your organization uses whatever your tenant has set, or the application default if the tenant hasn’t set one either. When you expand a setting you can see each step of this chain, which value is currently **In effect**, and where it came from.
Settings also have a **kind** that controls how values from different levels combine.

* Most settings simply take the most specific value: if your organization sets it, that wins; otherwise the tenant’s value wins; otherwise the default applies.
* Some settings are **restrictions**, where the tightest value across every level wins. For these, your organization can tighten the value but cannot loosen it past what your tenant allows. The session idle timeout works this way.
* A few settings are **collections** that accumulate entries from every level rather than picking one. Managed connectors works this way, so your organization’s entries are added to any the tenant has defined.

A higher level can **lock** a setting so that levels below it cannot change it. A setting that your tenant has locked shows as **Managed** and is read-only here. A setting that you lock at your own level shows as **Enforced** and prevents any group-level value within your organization from overriding it.
Settings that may contain secrets, such as telemetry headers, are never echoed back in the chain view. You will see that a value is set, but not what it is.

##  When changes take effect

Settings that govern the admin portal, such as whether organizations may manage seat tiers, apply immediately. Settings that govern the Claude applications themselves, such as the desktop banner, enabled tabs, and telemetry endpoint, are delivered to each member’s application the next time it refreshes its configuration, which happens when the application is launched or the member signs in. You do not need to push anything, but members who are currently running the application may need to restart it to pick up a change.

##  Working with the list

Settings are grouped by category in the sidebar on the left. Select a category to see its settings; the number beside each category shows how many settings it contains.
Each setting appears as an expandable card showing its name, a one-line description, which products it applies to, its current value, and where that value comes from (for example, **From Anthropic default** or **Set at tenant**). Click a card to expand the full chain and the editor.
The scope bar above the list shows which level you are editing and lets you switch between levels when you have access to more than one. Use **Compare config across levels** to see every setting side by side across the Anthropic default, your tenant, and your organization.
To change a setting, expand it, adjust the value, and save. To stop overriding a setting at your level and return to whatever the level above provides, reset it.

##  Available settings

**Session idle timeout** controls how long a member can stay inactive before being signed out. It must be a whole number of minutes, 15 or higher. The application default is 1440 minutes (24 hours). A lower value applies at the next sign-in; a higher value applies on the next request. This is a restriction, so you may set a shorter timeout than your tenant but not a longer one, and the value that takes effect is always the shortest one in the chain.
**Permit organizations to manage their own seat tiers** controls whether organization admins may create and edit self-managed seat tiers on the [Tiers](https://claude.com/docs/government/org-admin/seat-tiers) page. This setting can only be changed by a tenant administrator; it is always read-only here. When it is off, the **New seat tier** button and the edit and delete controls on that page are hidden, and the **Reset usage limits** action on the [Users](https://claude.com/docs/government/org-admin/users) page is also unavailable.
**Telemetry endpoint (Claude Desktop)** sets where Claude Desktop sends usage telemetry using the OpenTelemetry protocol. A matching **Telemetry endpoint (Claude for Microsoft 365)** setting covers that product. The value must be an absolute address beginning with `https://`, and leaving it empty disables telemetry.
**Telemetry headers (Claude Desktop)** sets additional headers, such as an authorization token, that are sent with telemetry. Because the value may contain a secret, it is never displayed after you save it; you will see only that it is set.
**Managed connectors (Claude Desktop)** defines the connectors that are made available in Claude Desktop. Connectors are integrations that extend Claude with external tools and data sources. Each entry requires a name and an address beginning with `https://`, and the address must not point at a private or internal network range. This setting accumulates across levels, so entries you add here appear alongside any your tenant has defined. Because entries may contain credentials, saved values are not echoed back.
**Desktop banner** configures a persistent banner shown at the top of Claude Desktop. You can set the text, the colors, and an optional link, and you can preview the result as you edit. Banner text may be up to 200 characters, leading and trailing spaces are rejected, colors must be valid hex codes, and the link (if set) must begin with `https://`. An empty banner is valid and simply hides it.
**Product availability** is a group of separate switches that control which Claude products and features are available to members. Each switch appears as its own row: **Claude Desktop**, **Claude Code**, **Claude for Microsoft 365**, **Chat tab**, **Cowork tab**, **Code tab**, and **Advanced file analysis in Chat**. All are on by default. Turning a switch off makes that product or tab unavailable.
**Allowed network hosts** is a list of hostnames that tools in the Cowork and Code tabs may reach, for example to install packages or fetch web pages. The connection to Claude is always allowed and does not need to be listed. An empty list shows as **Claude connection only**. Use **Add package registries** to add npm, PyPI, GitHub, crates.io, and other common registries so that Claude can install libraries; hosts added this way appear together as a single **Package registries** pill with a count. This list does not cover addresses on your private network, direct IP addresses, or Web search, so do not rely on it alone to restrict network access.
**Allowed workspace folders** controls which folders members can pick as a project folder in Claude Desktop, and where Claude can read and write files. Leave it unset to allow any folder. Add folder paths to limit members to those locations, or check **Block all workspace folders** to allow none, in which case Claude can still work in folders it creates inside its own sandbox. You can list Windows and Mac paths together, and each device uses only the paths for its platform. An unset value shows as **Any folder** and an empty list shows as **No folders**.

##  Tool and connector cards

Alongside the settings list, the Config page shows cards for the built-in tools (Web search, Web fetch, and Shell commands), the built-in connector (Microsoft 365), and a **Connectors** card for the ones you add yourself. A connector is an integration that lets Claude reach an external service on a user’s behalf.
The **Web search** card controls whether Claude can search the web from Claude Desktop. It is off by default. When you turn it on you are shown a short description of how search works and asked to acknowledge it before the setting is saved. A **Require approval for each search** sub-setting sits below the toggle and becomes available once web search is on; it is on by default, and turning it off lets each user choose whether to approve every search or allow searches to run automatically.
The **Web fetch** card controls whether Claude can fetch web pages during tasks in Claude Desktop. It is on by default, and fetches are subject to the Allowed network hosts list above. A **Require approval for each fetch** sub-setting sits below the toggle; it is off by default, and turning it on asks the user to approve every page fetch before it runs.
The **Shell commands** card controls whether Claude can run shell commands in the sandbox during tasks in Claude Desktop. It is on by default, and turning it off also turns off Advanced file analysis in Chat. A **Require approval for each command** sub-setting sits below the toggle; it is off by default, and turning it on asks the user to approve every shell command before it runs.
The **Microsoft 365** card controls whether Claude can reach your agency’s Microsoft 365 content, including SharePoint, OneDrive, Outlook, and Teams. It is off by default.
The **Connectors** card lists the Model Context Protocol servers you have added for your own systems. Each connector is defined once and applied to the products you choose. See the [Connectors](https://claude.com/docs/government/connectors/overview) page for how to add and manage them.

##  Comparing settings across levels

Select **Compare config across levels** at the top of the Config page to open a read-only table that lays every setting out side by side across the full chain. This view is for understanding how a value got to be what it is, especially when a setting has been set at more than one level. You can’t change anything from here; each row has an **Edit** link that takes you back to that setting on the main Config page.
The table has one row per setting and one column per level in the chain: the **Anthropic default**, your **Tenant**, **Groups** (tenant-wide group settings), your **Organization**, **Org groups** (group settings scoped to this organization), and the **Final value** that actually takes effect. A dash means that level has not set a value for that setting. A lock icon next to a value means that level has locked it, and anything below it in the chain is ignored. Use the **All levels** / **Final only** toggle to hide the middle columns and show just the setting, where it was set, and the final value.

###  Looking up one person’s settings

Type a name into the search box above the table to see exactly what settings apply to one of your organization’s members. The table re-resolves every setting from that person’s point of view, including the directory groups they belong to, and the **Final value** column shows what they actually get. A summary card above the table lists the tenant, group, and organization being used for the lookup.
Click any row to expand a plain-English explanation of how the final value was reached, walking through each level in the chain and whether it set or locked the value. This is the quickest way to answer a question like “why can’t this person see the Code tab?”

##  Group-specific settings

In addition to setting values for your whole organization, you can set values for the members of a directory group within your organization. Directory groups are pushed from your agency’s identity provider over SCIM and are managed at the tenant level; you see the same list of groups here that the tenant does. A value you set at this level applies only to people who are both a member of the group and a member of your organization, and it is the most specific level in the chain.
To edit settings for a group, open the scope bar above the settings list and choose the group’s name from the dropdown. The page switches to show the same settings editor, now scoped to that group within your organization. Editing, saving, resetting, and locking all work the same way as at the organization level. Anything the tenant or the tenant-wide group has locked still shows as **Managed** here and cannot be changed.
When someone belongs to more than one group, only their highest-priority group that has any configuration is used, and the others are ignored for that person. Group priority is set by your tenant administrator and is shown here for reference; you cannot reorder it from the organization portal.
If the group list is empty, no groups have been synced from the tenant’s identity provider yet. Groups appear here automatically once the tenant has connected SCIM and your directory has pushed them.

Your deployment may include additional settings that are not listed above. Any extra setting follows the same chain, status badges, and edit and reset behavior.
