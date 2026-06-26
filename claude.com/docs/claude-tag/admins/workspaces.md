<!-- source: https://claude.com/docs/claude-tag/admins/workspaces -->

This page covers managing Slack workspace pairings after initial setup: adding more workspaces, choosing which version of Claude in Slack each one runs, and disconnecting one.
A workspace pairing links one Slack workspace (or Enterprise Grid) to your Claude organization so `@Claude` can run there. Your first pairing was created during [setup](/docs/claude-tag/admins/setup-overview). To add more, you must be an Owner in your Claude organization, and a Workspace Admin (or Grid Org Admin) in the Slack workspace you’re adding.

##  Pair another workspace

You can connect multiple Slack workspaces to one Claude organization. After the first pairing, the **Set up** button is gone and the Slack row appears under **Where Claude Tag works**.

1

Open the pairing dialog

At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), under **Where Claude Tag works**, either select **+ Connect** at the top right, or open the **⋮** menu on the Slack row and select **+ Add workspace**.

2

Get a pairing code from Slack

In any channel of the new workspace, send `@Claude connect`. Paste the code Claude sends you into the dialog.

If your organization used the earlier Claude in Slack app, the dialog header reads **Switch to Claude Tag** instead of **Set up Claude Tag for your workspace**. The steps are the same, and the new workspace is added alongside your existing one, not in place of it.

**You’ll see:** the new workspace in the Slack row’s connected list and as a scope in the **Claude Tag’s access** section.

##  Set the version for a scope

Every scope routes to one of four versions. In the **Claude Tag’s access** section of admin settings, select the scope and use the **Claude in Slack version** control.

| Label | Effect |
| **New** | Claude Tag. Access bundles, skills, and custom instructions apply |
| **Legacy** | The earlier per-user Claude in Slack. Bundles and skills do not apply. Being deprecated; see [Migrate from the earlier app](/docs/claude-tag/admins/migrate-from-earlier) |
| **Off** | Claude doesn’t respond to channel mentions in this scope. Direct messages are unaffected |
| **Inherit** | Use the parent scope’s value. Not shown at **Default Slack access** |

Per-scope version changes (workspace and channel) are reversible; see [Migrate from the earlier app](/docs/claude-tag/admins/migrate-from-earlier).

##  Revoke a pairing

In the **Connected workspaces** list, select **Disconnect** on the workspace’s row. Disconnecting revokes the pairing so `@Claude` no longer runs in that workspace, but the workspace’s scope and any bundles bound to it remain in the **Slack** tab; remove the scope separately if you want it gone. Claude stops responding in that workspace immediately. Its scopes remain in the Claude Tag’s access section, so credentials and instructions are preserved, until you remove them.

* [Migrate from the earlier app](/docs/claude-tag/admins/migrate-from-earlier): the upgrade path and what changes for existing users
* [Pair your Slack workspace](/docs/claude-tag/admins/pair-workspace): the first pairing, with the Slack-admin handoff

[Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access)[Audit and review](/docs/claude-tag/admins/audit)
