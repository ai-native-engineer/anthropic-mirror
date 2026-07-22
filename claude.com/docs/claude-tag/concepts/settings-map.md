<!-- source: https://claude.com/docs/claude-tag/concepts/settings-map -->

Claude Tag’s settings live on claude.ai, split across a few pages that each own a different kind of setting. Which page you need depends on what you’re changing. The table maps each surface to what it controls.

| Surface | Who changes it | What it controls |
| --- | --- | --- |
| [Claude Tag admin page](https://claude.ai/admin-settings/claude-tag) | An Owner in your Claude organization | Access, behavior, and restrictions for channels, per [scope](/docs/claude-tag/concepts/glossary#scope) |
| [Usage page](https://claude.ai/admin-settings/usage/claude-tag) | An admin | Spend limits and per-channel usage analytics |
| The **Configure** link in any Claude reply footer | Channel members, unless an admin restricts editing | One channel’s instructions |
| [Connectors settings](https://claude.ai/settings/connectors) on your own claude.ai account | You | Which of your personal tools apply in [DMs](/docs/claude-tag/concepts/agent-identity#direct-message-channels) |

Channel memory and routines aren’t in the table because you change them by talking to Claude in the channel; see [what anyone can change from the channel](/docs/claude-tag/admins/customize#change-behavior-from-the-channel).

##  The Claude Tag admin page

Everything an Owner configures for channels lives at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag). Settings there apply per scope (a channel, a workspace, or the whole organization). A scope without its own setting inherits from its parent, and a channel’s setting overrides its workspace’s, so two channels can run with different connections, models, and instructions. Most controls are Owner-only; the [permissions table](/docs/claude-tag/admins/restrict-access#permissions-by-role) lists each action and who can take it.

* **Access bundles**: the connections, domain entries, repository grants, and plugins Claude uses in the channels a bundle covers. See [Give Claude access](/docs/claude-tag/admins/add-connections).
* **Custom instructions**: standing guidance Claude reads in every session on a scope. See [Add custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions).
* **Default model**: the model new sessions in a scope start on. The options come from the models your organization allows for Claude Code; see [Choose the model for a scope](/docs/claude-tag/admins/customize#choose-the-model-for-a-scope).
* **Workspace pairing and restrictions**: which Slack workspaces are paired, whether DMs are allowed, guest-channel behavior, who can invoke Claude, and which generation of the app answers in each scope. See [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access).

##  Spend limits and usage

Spend limits and usage analytics live at [`claude.ai/admin-settings/usage/claude-tag`](https://claude.ai/admin-settings/usage/claude-tag), a different page than the Claude Tag admin page. It holds the organization-wide spend limit, per-channel limits, and the per-channel spend breakdown. See [Set a spend limit](/docs/claude-tag/admins/set-spend-limit) for funding the usage balance and what users see when a limit is reached.

##  The Configure page

Every Claude reply in Slack ends with a footer, and its **Configure** link opens a claude.ai page for that channel. Anyone in the channel who is also a member of your Claude organization can edit the **Channel instructions** field there, unless an admin has [restricted editing to admins](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions). The page also shows the channel’s **Connections**, which admins set, so members can see the list but not change it.
The Configure page and the scope’s settings dialog in admin settings write the same instructions, so a change from either place is visible in the other. See [Configure Claude for a channel](/docs/claude-tag/users/good-habits#configure-claude-for-a-channel).

##  Personal connectors on claude.ai

Connectors you add to your own claude.ai account, under **Settings > Connectors**, apply only in DMs with Claude, because [a DM runs on your own account](/docs/claude-tag/concepts/agent-identity#direct-message-channels). A channel uses only the connections an admin attached to it, and personal connectors never apply there. Slack has no connector settings of its own.
See [connectors on claude.ai](/docs/connectors/overview) for setting one up, and [the troubleshooting entry](/docs/claude-tag/users/troubleshooting#a-connector-works-on-claude-ai-but-not-in-slack) if a connector you use on claude.ai is missing in Slack.

##  Claude Tag versus Claude Managed Agents

[Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) is a separate product for developers, a pre-built agent harness that runs in managed infrastructure. You configure it on the Claude Platform through the Managed Agents API, and access requires a Claude API key. An agent there is defined by its model, system prompt, tools, MCP servers, and skills. Environments choose where its sessions run (a cloud sandbox, or a self-hosted sandbox on your own infrastructure), and scheduled deployments run it on a cron schedule.
The two products don’t share settings. Nothing on the Claude Tag admin page configures a Managed Agent, and an agent defined on the Claude Platform doesn’t change how Claude behaves in Slack.

##  Related resources

* [Customize Claude Tag](/docs/claude-tag/admins/customize): the layers that shape Claude’s behavior in a channel and who sets each one
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): why channels and DMs use different access
* [Set up Claude Tag](/docs/claude-tag/admins/setup-overview): where each setting is first created during setup

[Security and data handling](/docs/claude-tag/concepts/security-and-data)[Glossary](/docs/claude-tag/concepts/glossary)
