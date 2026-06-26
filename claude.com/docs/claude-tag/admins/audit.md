<!-- source: https://claude.com/docs/claude-tag/admins/audit -->

Use this page to review what Claude Tag is doing across your organization: which routines are scheduled, what memory it has saved, and where to find a record of each action it took.

You must be an Admin or Owner in your Claude organization to open the Audit page; the other trails on this page are visible to anyone with access to the underlying surface.

Claude Tag activity is auditable in four places:

* **[The Audit page](#what-the-audit-view-lists)** in admin settings, with tabs for scheduled work, memory, and (if enabled) network events
* **Memory files on each scope** (open the scope’s settings dialog in the **Claude Tag’s access** section), where you can review what Claude has saved
* **[Attribution on each action](#trace-an-action-to-its-source)** Claude takes in a connected tool
* **[The audit logs of each connected service](#trace-an-action-to-its-source)**, where its actions appear under the service account you provisioned

##  What the Audit view lists

The **Audit** page (left-nav label **Audit logs**) at [`claude.ai/admin-settings/claude-tag/audit`](https://claude.ai/admin-settings/claude-tag/audit) has these tabs:

| Tab | What it shows |
| **Scheduled work** | Every routine across your organization, with a **Scope** filter and a per-row **⋮** menu (View details, Pause/Resume, Delete) |
| **Memory** | A link to each scope’s memory files, where you can read what Claude has saved for that workspace or channel (an Owner can also edit or delete) |
| **Network events** | An hourly JSON export of outbound calls Claude made through Agent Proxy. Git and MCP traffic are not included in this export. Select a date and hour to download. This tab only appears if your organization has network-event export enabled; contact your account team to request it. |

Each routine on the **Scheduled work** tab shows **Created by** (the member who set it up) in its **View details** dialog. There is no per-action log of every task and who asked; for that, use the trails below.

##  Trace an action to its source

In channels, Claude acts as itself, so each action there carries the service-account identity:

* **In Slack**, it posts as the Claude app, and its work happens in threads anyone in the channel can read.
* **On code**, commits and pull requests show the Claude GitHub App as the author, and each one links back to the Slack thread it came from.
* **In every other connected service**, actions appear under the service account you created for the connection.

That last one is the general-purpose trail: because you provisioned the credential, the connected service’s audit log shows everything Claude did there, under an account your security team already monitors.
The [Test your setup](/docs/claude-tag/admins/test-it) uses this check to validate a new connection.

##  See what’s scheduled in a channel

Anyone in the channel can see its standing work. Ask in the channel:

@Claude what triggers do you have set up in this channel?

Claude lists the channel’s scheduled jobs and watches, and anyone there can ask it to disable one.
Routines run with the channel’s credentials, so the channel listing is also the permission picture. See [proactivity](/docs/claude-tag/users/proactivity#manage-standing-work).

* [How agent identity works](/docs/claude-tag/concepts/agent-identity): how attribution differs in channels and DMs
* [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access): the controls when an audit turns something up
* [Security and data handling](/docs/claude-tag/concepts/security-and-data): the model behind the trails

[Workspaces and versions](/docs/claude-tag/admins/workspaces)[Migrate from legacy Claude in Slack](/docs/claude-tag/admins/migrate-from-earlier)
