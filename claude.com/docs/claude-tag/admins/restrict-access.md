<!-- source: https://claude.com/docs/claude-tag/admins/restrict-access -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

In channels, Claude Tag responds only where it’s been added and addressed, and the controls on this page narrow that further. DMs are a separate surface that runs on the user’s own account; see [how DMs differ from channels](https://claude.com/docs/claude-tag/concepts/agent-identity#direct-message-channels).

Most controls on this page require the Owner role in your Claude organization; the [permissions table](#permissions-by-role) below lists which actions an Admin or a channel member can take.

##  Control who can invoke Claude Tag

In channels where the app has been added, an @-mention guarantees a response; Claude may also respond to a message that doesn’t mention it when it judges a reply is warranted, and once a thread is active it follows replies in that thread. By default, anyone in such a channel can address it. A single toggle narrows that to people in your Claude organization.

###  Restrict who can use Claude

Open **Manage** on the Slack entry under **Where Claude Tag works** at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag). The dialog shows a toggle that controls who in your Slack workspace can use Claude at all; its label depends on your plan. You must be an Owner of your Claude organization to change it.

| Plan | Toggle | Off (default) | On |
| --- | --- | --- | --- |
| Enterprise | **Restrict in your organization via RBAC** | Anyone in the connected Slack workspace can use Claude, even without a Claude account | Only members whose role grants the **Claude Tag in Slack** capability can use Claude |
| Team | **Restrict to your organization** | Anyone in the connected Slack workspace can use Claude, even without a Claude account | Only Slack users with a Claude account in your organization can use Claude |

The toggle applies to channels and DMs alike.

You may see the earlier three-option **Members** dropdown instead of the toggle. The dialog keeps the dropdown while your organization’s stored choice matches neither toggle state. That happens for an Enterprise organization that previously chose **Open to any organization member** (now marked deprecated), and for a Team organization still restricted by role from an earlier Enterprise plan. Switch to one of the toggle’s two states. The dropdown is then replaced by the toggle, and the deprecated option is no longer offered.

####  Restrict by role on Enterprise

Role restriction requires an Enterprise plan. Team plans don’t have role-level control; turning on **Restrict to your organization** is the only restriction available there.
Restricting by role spans three console pages.

1. On [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), turn on **Restrict in your organization via RBAC**.
2. On [`claude.ai/admin-settings/groups`](https://claude.ai/admin-settings/groups), create groups and add the relevant members.
3. On [`claude.ai/admin-settings/roles`](https://claude.ai/admin-settings/roles), create a custom role with the **Claude Tag in Slack** capability turned on or off, and choose which groups hold the role in the role editor.

Three rules govern how role restrictions resolve.

* **The toggle gates the capability.** The **Claude Tag in Slack** capability on a role has no effect until **Restrict in your organization via RBAC** is on. While the toggle is off, every member can use Claude regardless of what their role grants.
* **Built-in roles always grant access.** Every built-in role, including User, Owner, and Primary owner, grants **Claude Tag in Slack** automatically, so the restriction only blocks members on a custom role that doesn’t grant it.
* **Any grant wins.** A member in more than one group keeps access if any of their roles grants it.

A member whose roles don’t grant the capability is excluded everywhere Claude works, in three ways:

* **@-mentions and DMs get a private notice.** Claude doesn’t act on the request. The member sees a notice only they can see, saying their role doesn’t allow Claude Tag and to ask their admin for access.
* **Automatic replies skip them.** In channels where Claude responds without being tagged, a restricted member’s messages never trigger a response.
* **Their thread replies aren’t read.** In a thread an allowed member started, a restricted member’s replies don’t reach Claude as content. Claude sees that a message arrived, but the message body is withheld.

On a Slack Enterprise Grid whose workspaces are paired to different Claude organizations, one organization’s access settings govern the entire grid, so your restrictions may not be enforced in your own workspaces.

##  Control where Claude Tag operates

The restriction toggle decides who can use Claude. The controls in this section decide where it works at all, from one channel up to a workspace, and which generation answers in each scope (a scope is a channel, a workspace, or your whole organization).

###  Quiet or remove Claude Tag

Six ways to stop Claude Tag from responding, ordered from quietest to most complete:

1. **Ask it to stay quiet.** Saying “stay quiet in this thread unless tagged” stops Claude following an active thread.
2. **Remove it from the channel.** Run `/remove @Claude`. It can no longer read or post there.
3. **Set the scope’s Claude Tag version to Off.** Claude stops responding in that scope even if someone invites it back; an @-mention gets a disabled notice instead of a reply. The control is on the scope’s panel at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), and only an Owner can change it.
4. **Detach the scope.** The channel loses its elevated access and falls back to inherited baselines.
5. **Delete the bundle.** This revokes its credentials everywhere it was attached (the credentials are removed; memory, routines, and transcripts are not). Running sessions may keep a revoked credential for a short window before the change propagates.
6. **Uninstall the app.** This removes Claude from the workspace entirely.

Steps 1–4 and 6 do not delete any data. Step 5 (deleting a bundle) removes the credentials in that bundle; memory, routines, and session transcripts are unaffected by any of these steps. Removing Claude from a channel stops it responding there; the channel’s memory and routines remain on record, and re-adding it restores them. Credentials are stored in Access bundles on the claude.ai side and persist independently of the Slack app installation. To delete data, use the dedicated controls at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) rather than removal alone.

###  Limit Claude Tag to specific channels

To let Claude respond only in channels you choose, for example during a pilot confined to one channel, turn the [version setting](https://claude.com/docs/claude-tag/admins/workspaces#set-the-version-for-a-scope) **Off** everywhere and switch the chosen channels back to **New**. Both changes happen in the **Claude Tag’s access** section at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag). DMs, guest channels, and shared channels need more than the version setting; each gets its own treatment after the steps.

**Off** silences the earlier Claude in Slack too. If you’re in the middle of migrating from the earlier app, decide which scopes stay on **Legacy** before you start; the earlier app keeps answering in those channels.

1

Turn Claude Tag off everywhere

Set the **Claude Tag version** on [**Default Slack access**](https://claude.com/docs/claude-tag/admins/attach-to-scope) to **Off**. Then set any workspace or channel scope whose version is something other than **Inherit** to **Off** or **Inherit** too, leaving alone the scopes you’re keeping on **Legacy**.

2

Switch the chosen channels back on

Set each chosen channel’s version to **New**. A channel’s own setting wins over the **Off** above it, so Claude responds in the chosen channels and nowhere else. A channel that doesn’t appear in the **Claude Tag’s access** section yet needs a scope first; create one with **Add channel** as described in [Attach to a channel](https://claude.com/docs/claude-tag/admins/attach-to-scope#attach-to-a-channel), and the version control is on the new scope’s panel.

If someone invites the app into another channel afterward, Claude stays silent there. Mentioning `@Claude` in that channel gets a notice that Claude is disabled in the channel, not a reply.
DMs, guest channels, and shared channels sit outside the version setting:

* **DMs.** The version setting doesn’t cover them. To close those off too, turn off [Allow direct messages](#allow-or-disable-direct-messages).
* **Guest channels.** By default Claude is off in any channel that includes a Slack guest. If a chosen channel has guests, also set [Allow Claude to respond to guests](#restrict-guest-channels) to **Allow** on its scope.
* **Shared channels.** A [channel shared across workspaces in your Enterprise Grid](#channels-shared-across-workspaces-in-your-enterprise-grid) takes its settings from **Default Slack access** only, and Claude [doesn’t operate in Slack Connect channels](#externally-shared-channels) at all; neither can serve as a chosen channel.

To control who can use Claude in the allowed channels, turn on the [restriction toggle](#restrict-who-can-use-claude); to cap what a channel spends, [set a per-channel spend limit](#set-spend-limits).

###  Restrict guest channels

By default, Claude is disabled in any channel that includes a Slack guest. To allow it there, set **Allow Claude to respond to guests** to **Allow** for the scope covering the channel; **Restrict** (the default) keeps it off wherever a guest is present. The setting is at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), on the **Slack** tab under **Claude Tag’s access**, in the scope’s collapsed **Advanced** section.
**Allow** applies to every guest channel the scope covers, and guests in those channels can see Claude’s replies and interact with it. To open one channel rather than a whole workspace, set it on the channel’s own scope.
**Allow** controls whether Claude replies, not what it can search. Workspace search is unavailable in any channel that includes a guest, even when the setting is **Allow**. Search results could include content from channels the guests can’t see, the same reason Claude doesn’t search private channels. To run a search that covers the workspace, ask from a channel without guests.

###  Externally shared channels

Claude doesn’t operate in Slack Connect channels, the ones shared with another company. It’s off in those channels regardless of scope or bundle, and this isn’t configurable.

###  Channels shared across workspaces in your Enterprise Grid

What happens in a channel shared across more than one workspace inside your Enterprise Grid depends on whether every workspace in it is connected to the same Claude organization.
When the workspaces all belong to your one Claude organization, Claude replies in the channel, but only with the access and settings on your organization’s [Default Slack access](https://claude.com/docs/claude-tag/admins/attach-to-scope) scope. Bundles, instructions, and memory set on a workspace or on that channel don’t reach it. Claude posts a notice in the thread explaining this, about once a month per channel at most rather than on every reply. Where guest access is at its default **Restrict**, the [guest check](#restrict-guest-channels) still runs first and can refuse the reply.
When the workspaces belong to different Claude organizations, each with its own settings and plan, Claude won’t reply and posts a refusal message instead.
There is no per-channel override for either case.

###  Migrate from the earlier Claude in Slack

If your organization used the earlier Claude in Slack app, you choose which generation answers `@Claude` per scope. The control is the **Claude Tag version** setting on each workspace or channel scope at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), with the choices **Off**, **Legacy**, **New**, and **Inherit**, plus the **Claude Tag version** row on the **Default Slack access** scope above them.
Both generations answer through the same @Claude app, so **Off** turns off both. To opt out of Claude Tag but keep the earlier app answering in a scope, choose **Legacy**.
Access bundles only apply where the New version answers. The [glossary](https://claude.com/docs/claude-tag/concepts/glossary#the-earlier-claude-in-slack) covers how the two differ.

###  Allow or disable direct messages

The **Allow direct messages** toggle controls whether members can message Claude directly. When it’s off, Claude is reachable only in channels. The default is on, and you must be an Owner of your Claude organization to change it.
On [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), the toggle appears in one of two places: directly on the Claude Tag settings page, or in the **Manage** dialog on the Slack entry under **Where Claude Tag works**, where the toggle is labeled **Allow direct messages with Claude**. If your organization still uses the earlier Claude in Slack settings page at [`claude.ai/admin-settings/claude-in-slack`](https://claude.ai/admin-settings/claude-in-slack), the toggle appears there too. It’s the same setting in each place, so change it wherever it appears for your organization.

###  Set spend limits

Spend limits and usage analytics live at [`claude.ai/admin-settings/usage/claude-tag`](https://claude.ai/admin-settings/usage/claude-tag), a different page than the main Claude Tag settings.
A spend limit is a cap on how much of your organization’s usage balance Claude Tag can draw each billing period. Setting a limit doesn’t fund the balance; on a Team plan, [fund the usage balance first](https://claude.com/docs/claude-tag/admins/set-spend-limit) or Claude won’t respond in channels regardless of the limit.

* **Organization-wide limit.** Caps total Claude Tag spend across every channel.
* **Per-channel limits.** Set on any channel that has its own scope, in addition to the organization limit.
* **Usage analytics.** Per-channel spend breakdown on the same page.

Work that would exceed a limit is declined rather than silently truncated. A user blocked by a limit can request more usage from their admin in Slack, and the admin notification names whether the usage balance or the limit caused the block.

##  Permissions by role

Creating bundles, binding them to scopes, and pairing workspaces need an Owner; an Admin can edit a bundle’s Credentials and Domains tabs but not its other tabs. Everything else happens inside the channel and is open to its members. The table lists each action and who can take it.

| Action | Owner | Admin | Channel member |
| --- | --- | --- | --- |
| Pair a workspace | Yes | No | No |
| Create, rename, delete, or bind an Access bundle | Yes | No (view only) | No |
| Edit a bundle’s Repositories, Plugins, or Instructions tab | Yes | No (view only) | No |
| Edit a bundle’s Credentials or Domains tab | Yes | Yes | No |
| Write channel memory | Yes, in the channel | Yes, in the channel | Yes |
| Set channel instructions from the Configure link | Yes | Yes | Yes, unless the scope’s [Channel member edits](https://claude.com/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions) setting blocks it |
| Create, list, or disable a scheduled job in the channel | Yes, in the channel | Yes, in the channel | Yes |
| Remove Claude from a channel | Yes | Yes | Yes, with `/remove`, unless your Slack admin restricts it |

Scheduled jobs run with the channel’s credentials, so a member creating one can’t reach anything the channel itself can’t.

##  Controls that aren’t available

These are controls an admin might look for that Claude Tag doesn’t have.

* **Third-party deployment.** Sessions run on Anthropic’s first-party infrastructure; Claude Tag isn’t available through third-party deployments.
* **Renaming or rebranding the app.** The Claude app’s name, @-handle, and avatar in Slack are fixed; there is no per-workspace rename setting.
* **A pre-invite channel blocklist.** Once the app is installed in a workspace, anyone can `/invite @Claude` into a public channel; there’s no list that prevents the invite itself. To keep Claude out of a channel after the fact, [set that scope’s Claude Tag version to Off](#quiet-or-remove-claude-tag). To confine Claude to chosen channels instead, see [Limit Claude Tag to specific channels](#limit-claude-tag-to-specific-channels).
* **Per-user spend caps on channel work.** Spend limits apply at the organization and channel level. There’s no way to cap what one member can spend in channels; DM usage bills to that member’s own seat and follows the seat’s usual limits.
* **Per-channel responder allowlist.** The restriction toggle governs who can invoke Claude across the workspace; you can’t narrow it to a list of people for one channel only.
* **An open-internet switch in Claude Tag settings.** A channel sandbox reaches only allowed hosts. To let Claude reach a public site or API, an Owner or Admin adds that hostname on a [bundle’s Domains tab](https://claude.com/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential); for broad web access, they pin an [environment](https://claude.com/docs/claude-tag/concepts/glossary#environment) whose network access level is Full on the scope. [Allow-all egress](https://claude.com/docs/claude-tag/admins/add-connections#allow-all-hosts), a `*` entry on the Domains tab, is off by default and enabled per organization by Anthropic.
* **A web search toggle for channels.** No setting turns web search off for channel sessions; the web search capability setting in claude.ai admin settings governs claude.ai chat, not channels. Web search runs on Anthropic’s servers rather than from the channel sandbox, so Domains entries and egress settings don’t govern it, and a search opens no new path out of the sandbox; search requests travel to Anthropic the same way the session’s model traffic already does. See [Web search vs. network requests](https://claude.com/docs/claude-tag/concepts/agent-identity#web-search-vs-network-requests).
* **Read-scope confinement.** Claude can search public channels by keyword the same way any Slack user can; it can’t read a channel’s full history unless it’s been added there. There’s no setting to disable workspace search, and no setting to enable it in [channels that include guests](#restrict-guest-channels), where search is unavailable.
* **Session length enforcement.** Your organization’s Slack session-length policy is not enforced on this surface.

##  Related resources

* [Configure per-channel access](https://claude.com/docs/claude-tag/admins/attach-to-scope): change the scopes these controls apply to
* [How agent identity works](https://claude.com/docs/claude-tag/concepts/agent-identity): the model these controls operate on
* [Security and data handling](https://claude.com/docs/claude-tag/concepts/security-and-data): what these controls don’t cover (data flow, retention, where credentials are stored)
