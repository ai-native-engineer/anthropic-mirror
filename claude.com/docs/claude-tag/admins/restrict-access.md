<!-- source: https://claude.com/docs/claude-tag/admins/restrict-access -->

In channels, Claude Tag responds only where it’s been added and addressed, and the controls on this page narrow that further. DMs are a separate surface that runs on the user’s own account; see [how DMs differ from channels](/docs/claude-tag/concepts/agent-identity#direct-message-channels).

Most controls on this page require the Owner role in your Claude organization; the [permissions table](#permissions-by-role) below lists which actions an Admin or a channel member can take.

##  Control who can invoke Claude Tag

In channels where the app has been added, an @-mention guarantees a response; Claude may also respond to a message that doesn’t mention it when it judges a reply is warranted, and once a thread is active it follows replies in that thread. By default, anyone in such a channel can address it. The **Members** setting narrows that to specific people.

###  Members

The **Members** setting (open **Manage** on the Slack entry under **Where Claude Tag works** at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag)) controls who in your Slack workspace can use Claude at all. You must be an Owner of your Claude organization to change it.

| Setting | Who can invoke Claude |
| **Open to anyone in your Slack workspace** (default) | Anyone in the connected workspace, with or without a Claude account |
| **Open to any organization member** | Anyone signed into a Claude account in the same organization that connected the workspace |
| **Only members whose role allows it** | Only members whose custom role grants the **Claude in Slack** capability |

Restricting by role spans three console pages.

1. On [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), set Members to **Only members whose role allows it**.
2. Switch to [`claude.ai/admin-settings/roles`](https://claude.ai/admin-settings/roles), a different page, and create a custom role with the **Claude in Slack** capability turned on or off.
3. On [`claude.ai/admin-settings/groups`](https://claude.ai/admin-settings/groups), assign that role to a group and add the relevant members.

Three rules govern how role restrictions resolve.

* **Custom roles only.** Members on a preset role like User or Owner are granted access regardless of role configuration; restrictions apply only to members on custom roles. This is because a custom role is the only place a deny can live; preset roles have no capability toggles.
* **Any grant wins.** A member in more than one group keeps access if any of their roles grants it.
* **Team plans can restrict by membership only.** Restricting by role requires an Enterprise plan; on a Team plan, the first two Members options are available.

The Members setting applies to channels and DMs alike.

Role-based restrictions do not apply if your Slack Enterprise Grid contains workspaces owned by different Claude organizations.

##  Control where Claude Tag operates

Members decides who can use Claude. The controls in this section decide where it works at all, from one channel up to a workspace, and which generation answers in each scope (a scope is a channel, a workspace, or your whole organization).

###  Quiet or remove Claude Tag

Six ways to stop Claude Tag from responding, ordered from quietest to most complete:

1. **Ask it to stay quiet.** Saying “stay quiet in this thread unless tagged” stops Claude following an active thread.
2. **Remove it from the channel.** Run `/remove @Claude`. It can no longer read or post there.
3. **Set the scope’s Claude in Slack version to Off.** Claude stops responding in that scope even if someone invites it back; an @-mention gets a disabled notice instead of a reply. The control is on the scope’s panel at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), and only an Owner can change it.
4. **Detach the scope.** The channel loses its elevated access and falls back to inherited baselines.
5. **Delete the bundle.** This revokes its credentials everywhere it was attached (the credentials are removed; memory, routines, and transcripts are not). Running sessions may keep a revoked credential for a short window before the change propagates.
6. **Uninstall the app.** This removes Claude from the workspace entirely.

Steps 1–4 and 6 do not delete any data. Step 5 (deleting a bundle) removes the credentials in that bundle; memory, routines, and session transcripts are unaffected by any of these steps. Removing Claude from a channel stops it responding there; the channel’s memory and routines remain on record, and re-adding it restores them. Credentials are stored in Access bundles on the claude.ai side and persist independently of the Slack app installation. To delete data, use the dedicated controls at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) rather than removal alone.

###  Restrict guest channels

By default, Claude is disabled in any channel that includes a Slack guest. To allow it there, set **Allow Claude to respond to guests** to **Allow** on the scope; Restrict (the default) keeps it off wherever a guest is present.

###  Externally shared channels

Claude doesn’t operate in Slack Connect channels, the ones shared with another company. It’s off in those channels regardless of scope or bundle, and this isn’t configurable.
The same applies to a channel shared across more than one workspace inside your Enterprise Grid, or across more than one workspace that has its own Claude connection. Claude won’t reply in those channels and posts a refusal message instead. There is no per-channel override.

###  Migrate from the earlier Claude in Slack

If your organization used the earlier Claude in Slack app, you choose which generation answers `@Claude` per scope. The control is the **Claude in Slack version** setting on each workspace or channel scope at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), with the choices **Off**, **Legacy**, **New**, and **Inherit**, plus the **Claude in Slack version** row on the **Default Slack access** scope above them.
Access bundles only apply where the New version answers. The [glossary](/docs/claude-tag/concepts/glossary#the-earlier-claude-in-slack) covers how the two differ.

###  Allow or disable direct messages

The **Allow direct messages** toggle (in the Slack entry’s **Manage** dialog under **Where Claude Tag works** at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag)) controls whether members can message Claude directly. When off, Claude is reachable only in channels. The default is on.

###  Set spend limits

Spend limits and usage analytics live at [`claude.ai/admin-settings/usage/claude-in-slack`](https://claude.ai/admin-settings/usage/claude-in-slack), a different page than the main Claude Tag settings.

* **Organization-wide limit.** Caps total Claude Tag spend across every channel.
* **Per-channel limits.** Set on any channel that has its own scope, in addition to the organization limit.
* **Usage analytics.** Per-channel spend breakdown on the same page.

Work that would exceed a limit is declined rather than silently truncated. A user blocked by a limit can request more usage from their admin in Slack, and the admin notification names whether the wallet or the limit caused the block.

##  Permissions by role

Creating bundles, binding them to scopes, and pairing workspaces need an Owner; an Admin can edit a bundle’s Credentials and Domains tabs but not its other tabs. Everything else happens inside the channel and is open to its members. The table lists each action and who can take it.

| Action | Owner | Admin | Channel member |
| --- | --- | --- | --- |
| Pair a workspace | Yes | No | No |
| Create, rename, delete, or bind an Access bundle | Yes | No (view only) | No |
| Edit a bundle’s Repositories, Plugins, or Instructions tab | Yes | No (view only) | No |
| Edit a bundle’s Credentials or Domains tab | Yes | Yes | No |
| Write channel memory | Yes, in the channel | Yes, in the channel | Yes |
| Create, list, or disable a scheduled job in the channel | Yes, in the channel | Yes, in the channel | Yes |
| Remove Claude from a channel | Yes | Yes | Yes, with `/remove`, unless your Slack admin restricts it |

Scheduled jobs run with the channel’s credentials, so a member creating one can’t reach anything the channel itself can’t.

##  Controls that aren’t available

These are controls an admin might look for that Claude Tag doesn’t have.

* **Model selection.** Channel sessions run on Claude Opus
* **Third-party deployment.** Sessions run on Anthropic’s first-party infrastructure; Claude Tag isn’t available through third-party deployments.
* **Renaming or rebranding the app.** The Claude app’s name, @-handle, and avatar in Slack are fixed; there is no per-workspace rename setting.
* **A pre-invite channel blocklist.** Once the app is installed in a workspace, anyone can `/invite @Claude` into a public channel; there’s no list that prevents the invite itself. To keep Claude out of a channel after the fact, [set that scope’s Claude in Slack version to Off](#quiet-or-remove-claude-tag).
* **Per-user spend caps on channel work.** Spend limits apply at the organization and channel level. There’s no way to cap what one member can spend in channels; DM usage bills to that member’s own seat and follows the seat’s usual limits.
* **Per-channel responder allowlist.** Members governs who can invoke Claude across the workspace; you can’t narrow it to a list of people for one channel only.
* **Read-scope confinement.** Claude can search public channels by keyword the same way any Slack user can; it can’t read a channel’s full history unless it’s been added there. There’s no setting to disable workspace search.
* **Session length enforcement.** Your organization’s Slack session-length policy is not enforced on this surface.

* [Configure per-channel access](/docs/claude-tag/admins/attach-to-scope): change the scopes these controls apply to
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): the model these controls operate on
* [Security and data handling](/docs/claude-tag/concepts/security-and-data): what these controls don’t cover (data flow, retention, where credentials are stored)

[Add custom skills](/docs/claude-tag/admins/skills-repo)[Workspaces and versions](/docs/claude-tag/admins/workspaces)
