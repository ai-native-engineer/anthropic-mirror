<!-- source: https://claude.com/docs/government/tenant-admin/configuration -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

> **Who this is for:** Tenant administrators who set and enforce product settings across every organization in their deployment.

Use this page to set tenant-wide defaults for product behavior, lock settings so organizations can’t override them, and preview how a change would affect each organization.

##  How settings are applied

Each setting is resolved through a chain: **Application default → Your tenant → Each organization**. A value you set here becomes the default for every organization, and an organization can still change the setting on its own Config page unless you lock it. When you expand a setting you can see each step of this chain, which value is **In effect**, and (in the tenant view) which organizations have set their own value.
A **lock** prevents levels below from changing the setting. When you lock a setting here it shows as **Enforced**, and organizations see it as **Managed**, which means it is read-only for them. Any value an organization had previously set is ignored while your lock is in place, and it comes back into effect if you later remove the lock.
> **For organization owners:** When a setting shows as **Managed** on your organization’s Config page, it has been locked at the tenant level and you can’t change it. Any value you had previously set is ignored while the lock is in place.

###  Setting kinds

Settings combine across the chain in one of three ways, and the kind is fixed per setting (you don’t choose it):

* A **simple value** is replaced at each level, and the most specific level that set it wins. Most settings work this way.
* A **restriction** is a limit where the tightest value across all levels wins. Any level can tighten the limit but none can loosen it. For example, if you set a session timeout of 30 minutes, an organization can set 15 but cannot set 60.
* A **collection** accumulates entries from each level. A level can add entries to what the level above provided, or replace the list entirely.

##  Working with the list

Settings are grouped by category in the sidebar on the left. Select a category to see its settings; the number beside each category shows how many settings it contains.
Each setting appears as an expandable card showing its name, a one-line description, which products it applies to, its current value, and where that value comes from (for example, **From Anthropic default** or **Set at tenant**). Click a card to expand the full chain and the editor.
The scope bar above the list shows which level you are editing and lets you switch between levels when you have access to more than one. Use **Compare config across levels** to see every setting side by side across the Anthropic default, your tenant, and each organization.
To change a setting, expand it, adjust the value, and save. To stop overriding a setting at your level and return to whatever the level above provides, reset it.

##  Previewing impact

After you change a setting, a **Preview impact** button appears next to **Save changes**. Select it to see a table listing every organization with its current effective value and what it would become after your change. Organizations where nothing would change are marked **unchanged**. This is especially useful when locking a setting, so you can see which organizations currently have a different value that your lock will override.
Preview isn’t available for settings whose values are hidden for security reasons (for example, settings that can contain authorization tokens). For those settings the preview shows whether a value is set rather than what it is.

##  Available settings

| Setting | What it does |
| --- | --- |
| **Session idle timeout** | This controls how long a member can stay inactive before being signed out. The default is 1440 minutes (24 hours), and the value must be a whole number of minutes, 15 or higher. A lower value applies at the next sign-in; a higher value applies on the next request. This is a restriction, so organizations can shorten it but not lengthen it past what you set here. |
| **Permit organizations to manage their own seat tiers** | This controls whether organization owners may create and edit their own custom seat tiers in addition to the tenant-managed ones. Only tenant administrators can change this setting; organization owners cannot grant themselves the capability. |
| **Compliance API** | This controls whether the [Compliance API](https://claude.com/docs/government/org-admin/compliance-api) is available. When it is off, organization owners cannot create new keys and every request to the API returns an error, including requests made with keys that were valid before. Listing and revoking existing keys remains available even when this is off, so that a disabled organization can still revoke an exposed key. |
| **Telemetry endpoint (Claude Desktop)** | This is the address where Claude Desktop sends usage telemetry using the OpenTelemetry protocol. A matching **Telemetry endpoint (Claude for Microsoft 365)** setting covers that product. Leave it empty to disable telemetry. |
| **Telemetry headers (Claude Desktop)** | These are additional headers (such as an authorization token) sent with every telemetry request. Values here are hidden in the preview for security. |
| **Managed connectors (Claude Desktop)** | These are pre-configured connectors made available in Claude Desktop. A connector is an integration that extends Claude with external tools and data sources. This is a collection, so organizations can add to the list you provide here. Connector addresses must use HTTPS. |
| **Desktop banner** | This is a persistent banner shown at the top of Claude Desktop. You can set the text, colors, and an optional link, and preview the result live. |
| **Product availability** | A group of separate switches (**Claude Desktop**, **Claude Code**, **Claude for Microsoft 365**, **Chat tab**, **Cowork tab**, **Code tab**, **Advanced file analysis in Chat**) that control which Claude products and tabs are available to members. All are on by default. |
| **Allowed network hosts** | This is a list of hostnames that tools in the Cowork and Code tabs may reach, for example to install packages or fetch web pages. The connection to Claude is always allowed and does not need to be listed. An empty list shows as **Claude connection only**. Use **Add package registries** to add npm, PyPI, GitHub, crates.io, and other common registries so that Claude can install libraries; hosts added this way appear together as a single **Package registries** pill with a count. This list does not cover addresses on your private network, direct IP addresses, or Web search, so do not rely on it alone to restrict network access. |
| **Allowed workspace folders** | This controls which folders members can pick as a project folder in Claude Desktop, and where Claude can read and write files. Leave it unset to allow any folder. Add folder paths to limit members to those locations, or check **Block all workspace folders** to allow none, in which case Claude can still work in folders it creates inside its own sandbox. You can list Windows and Mac paths together, and each device uses only the paths for its platform. An unset value shows as **Any folder** and an empty list shows as **No folders**. |

> Your deployment may include additional settings not listed above. Any extra setting still follows the same chain, status badges, and edit/reset behavior.

##  Tool and connector cards

Alongside the settings list, the Config page shows cards for the built-in tools (Web search, Web fetch, and Shell commands), the built-in connector (Microsoft 365), and a **Connectors** card for the ones you add yourself. A connector is an integration that lets Claude reach an external service on a user’s behalf.
The **Web search** card controls whether Claude can search the web from Claude Desktop. It is off by default. When you turn it on you are shown a short description of how search works and asked to acknowledge it before the setting is saved. A **Require approval for each search** sub-setting sits below the toggle; it is on by default, and turning it off lets each user choose whether to approve every search or allow searches to run automatically.
The **Web fetch** card controls whether Claude can fetch web pages during tasks in Claude Desktop. It is on by default, and fetches are subject to the Allowed network hosts list above. A **Require approval for each fetch** sub-setting sits below the toggle; it is off by default, and turning it on asks the user to approve every page fetch before it runs.
The **Shell commands** card controls whether Claude can run shell commands in the sandbox during tasks in Claude Desktop. It is on by default, and turning it off also turns off Advanced file analysis in Chat. A **Require approval for each command** sub-setting sits below the toggle; it is off by default, and turning it on asks the user to approve every shell command before it runs.
The **Microsoft 365** card controls whether Claude can reach your agency’s Microsoft 365 content, including SharePoint, OneDrive, Outlook, and Teams. It is off by default.
The **Connectors** card lists the Model Context Protocol servers you have added for your own systems. Each connector is defined once and applied to the products you choose. See the [Connectors](https://claude.com/docs/government/connectors/overview) page for how to add and manage them.

##  Comparing settings across levels

Select **Compare config across levels** at the top of the Config page to open a read-only table that lays every setting out side by side across the full chain. This view is for understanding how a value got to be what it is, and for spotting which levels have overridden which settings. You can’t change anything from here; each row has an **Edit** link that takes you back to that setting on the main Config page.
The table has one row per setting and one column per level in the chain: the **Anthropic default**, your **Tenant**, **Groups** (tenant-wide group settings), each **Organization**, **Org groups** (group settings scoped to one organization), and the **Final value** that actually takes effect. A dash means that level has not set a value for that setting. A lock icon next to a value means that level has locked it. Use the **All levels** / **Final only** toggle to hide the middle columns and show just the setting, where it was set, and the final value.
Before you pick a person, the **Groups** and **Organization** columns list every group and organization that has set its own value for that setting, so you can see at a glance where overrides exist across your tenant.

###  Looking up one person’s settings

Type a name into the search box above the table to see exactly what settings apply to that person. The table re-resolves every setting from that person’s point of view: the **Groups** column shows the value from the one group that applies to them (with any lower-priority groups they belong to shown faded, since those do not count), the **Organization** column shows their organization’s value, and the **Final value** column shows what they actually get. A summary card above the table lists the tenant, group, and organization being used for the lookup.
Click any row to expand a plain-English explanation of how the final value was reached, for example “Anthropic’s default is On. Your tenant hasn’t changed it. The Program-Reviewers group sets this to Off.” This is the quickest way to answer a question like “why is this turned off for this person?”

##  Group-specific settings

In addition to setting values for your whole tenant, you can set values for the members of a directory group. A directory group is a group that your identity provider has pushed to Claude for Government over SCIM, as described on the [Identity and access](https://claude.com/docs/government/tenant-admin/identity-and-access) page. Group-level settings sit between the tenant and the organization in the chain, so a value you set for a group overrides your tenant default for that group’s members, in every organization they belong to.
To edit settings for a group, open the scope bar above the settings list and choose the group’s name from the dropdown. The page switches to show the same settings editor, now scoped to that group, and the scope bar reads “Applies to members of [group], across all orgs.” Editing, saving, resetting, and locking all work the same way as at the tenant level. A lock you set at the tenant level still applies here and shows the setting as **Managed** for the group.

###  When someone belongs to more than one group

Only one group’s settings apply to any given person. When someone is a member of more than one group, the settings from their highest-priority group that has any configuration are used, and the other groups are ignored for that person. You set the priority order on the [Identity and access](https://claude.com/docs/government/tenant-admin/identity-and-access) page by dragging the groups into the order you want. The same priority order is used wherever configuration is resolved for a person; seat-tier group mappings on the [Provisioning](https://claude.com/docs/government/org-admin/provisioning) page use a separate fixed order.
If no groups appear in the scope bar dropdown, none have been synced from your identity provider yet. Connect SCIM on the Identity and access page and push groups from your directory, and they will appear automatically.

##  Things to know

* Changes saved here take effect across all organizations immediately, without requiring users to sign out. Client applications pick up the new values the next time they refresh their configuration, which is typically within moments. Lowering the session idle timeout is the one case that applies to new sign-ins only, as described above.
* Some settings can only be changed by tenant administrators (and not by organization owners at all), regardless of whether they are locked. These are noted in the descriptions above.
* Resetting a setting removes only the tenant’s value. Organization values are unaffected and remain in effect once your value is gone.
