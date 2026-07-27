<!-- source: https://claude.com/docs/claude-tag/admins/migrate-from-earlier -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

If your organization already used the earlier Claude in Slack, including [Claude Code in Slack](https://code.claude.com/docs/en/slack), Claude Tag replaces it. Your existing Slack app and `@Claude` handle stay, and no data migrates. What changes is who Claude acts as and who sets it up.

##  Switch your workspace to Claude Tag

1

Connect the workspace in the Claude console

Open [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag). If your workspace isn’t paired, run [setup](https://claude.com/docs/claude-tag/admins/setup-overview); otherwise you’re already on Claude Tag. Once paired, channels and linked-user DMs answer with the New version by default; no per-channel action is needed.

2

Check for channels still on Legacy

In the **Claude Tag’s access** section, look at the **Claude Tag version** on each scope. Pairing defaults every scope to New, so this is usually empty; set any showing **Legacy** to **New**.

3

Give Claude its connections

The New version starts with no access of its own. GitHub repositories and other connections do not carry over from individual users’ linked accounts, so code requests in a switched channel have nothing to clone until you configure them. Follow the [setup overview](https://claude.com/docs/claude-tag/admins/setup-overview) to add connections, and [GitHub access](https://claude.com/docs/claude-tag/admins/configure-github) for code work specifically.If your teams keep custom skills in a repository’s `.claude/skills/` folder, those skills apply only in threads that have the repository. Grant the repository in an [Access bundle](https://claude.com/docs/claude-tag/admins/add-connections#your-first-access-bundle) and have users name it in the first message. To give skills to every channel under a scope, add them through a [skills repository](https://claude.com/docs/claude-tag/admins/skills-repo).

4

Tell your users

Send them [Get started](https://claude.com/docs/claude-tag/users/getting-started). The visible change is that work now belongs to the channel; see [What existing users notice after the switch](#what-existing-users-notice-after-the-switch) below.

**You’ll see:** the workspace appears under **Where Claude Tag works**, and the **Claude Tag version** on each scope shows **New**.

###  If `@Claude` doesn’t respond at all

On Enterprise Grid, an earlier install can lose its connection and stop responding in every workspace. Don’t uninstall the app. Have a Slack Org Owner or Org Admin, while signed in to one of the workspaces (not the org-level admin page), open [claude.com/claude-for-slack](https://claude.com/claude-for-slack), select **Add to Slack**, and choose **Install to entire organization**. This refreshes the connection in place. Then send `@Claude connect` as a new top-level channel message with no other text (as a reply inside a thread, the command is treated as a normal request) and continue with step 1 above.

The earlier Claude in Slack app, shown as **Legacy** in admin settings, is being deprecated; check with your account team for the cutover date. After that date, channels still set to Legacy stop responding until the scope’s Claude Tag version is set to New.

##  What stays the same

* The Slack app and the `@Claude` handle. Your existing Claude in Slack settings (allowed users, verified-domain restriction) carry over. If your earlier install predates a permission Claude now uses, `@Claude connect` says so when you pair; a Slack admin clicks the install link in that reply and approves the consent screen, which installs over the existing app. Otherwise no app-side action is needed.
* Direct messages still run on the user’s own claude.ai account, the same way they did before. The shift to a shared identity applies to channels.
* Users who already linked their claude.ai account keep that connection. It is what powers their DMs.

##  How Claude Tag differs from the earlier app

The earlier app linked each user’s own claude.ai account, so it answered as that person and used their connectors. Claude Tag has one identity for the team, provisioned by an admin who also sets what it can reach in each channel.

|  | Legacy (the earlier Claude in Slack) | New (Claude Tag) |
| --- | --- | --- |
| Identity | Each user links their own claude.ai account | One agent identity with org-level service credentials |
| Sessions | Spawned per request | One persistent session per thread, shared with the channel |
| Memory | None | Shared workspace memory plus private-channel memory |
| Standing work | None | Routines and channel watching |
| Who sets it up | Each user, individually | An Owner, once |

The **Claude Tag version** setting on each scope lets you pin a channel or workspace to **Off**, **Legacy**, or **New**, or **Inherit** the organization default. Use it to hold specific channels on the Legacy behavior while you finish provisioning, then switch them when ready. Access bundles only apply where the New version answers. See [the version setting](https://claude.com/docs/claude-tag/admins/restrict-access#migrate-from-the-earlier-claude-in-slack) for the control.
Both versions answer through the same @Claude app, so setting a scope to **Off** turns off the earlier version there too. To opt out of Claude Tag while keeping the earlier behavior, set the scope to **Legacy**, not **Off**.

##  What existing users notice after the switch

In channels, the visible difference is that work belongs to the channel, not to whoever asked. Anyone can reply in a thread to steer it, and the result stays where the team can see and pick it up. Code work is authored by the Claude GitHub App rather than as the requesting user.
A user who never linked a claude.ai account can now hand Claude work in channels, by default. Whether that stays open or narrows to organization members is the admin’s [access restriction](https://claude.com/docs/claude-tag/admins/restrict-access#members) setting.
If `@Claude` in a channel still opens pull requests under the asker’s name, that channel is answering with the Legacy version; check the scope’s Claude Tag version setting.

##  Related resources

* [Glossary: the earlier Claude in Slack](https://claude.com/docs/claude-tag/concepts/glossary#the-earlier-claude-in-slack): what each term meant in the old app versus now
* [Set up Claude Tag](https://claude.com/docs/claude-tag/admins/setup-overview): the new admin-side setup, since per-user setup no longer applies
* [Restrict where Claude Tag operates](https://claude.com/docs/claude-tag/admins/restrict-access): keep specific channels on the old version during a phased switch
