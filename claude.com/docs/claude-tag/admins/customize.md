<!-- source: https://claude.com/docs/claude-tag/admins/customize -->

Claude Tag’s behavior is shaped by four layers, each set in a different place:

| Layer | What it is | Who sets it | Where |
| --- | --- | --- | --- |
| **Connections** | Credentials for the systems Claude can reach (GitHub, Drive, Datadog, your APIs) | Owner | [Access bundles](/docs/claude-tag/admins/add-connections) |
| **Plugins and skills** | Instructions that teach Claude how to use a tool or follow a process. A plugin bundles one or more [skills](https://code.claude.com/docs/en/skills). | Owner | [Bundle Plugins tab](/docs/claude-tag/admins/add-connections#attach-plugins) or a [skills repository](/docs/claude-tag/admins/skills-repo) |
| **Custom instructions** | Standing guidance read in every session at a scope (team conventions, output formats). Outranks channel memory. | Owner | [Per-scope instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions) |
| **Channel memory** | Facts Claude saves while working in a channel | Anyone in the channel | By [telling Claude](/docs/claude-tag/users/memory) |

Connections and plugins decide what Claude *can do*; instructions and memory shape *how it does it*.

##  Settings admins control

Access and organization-wide behavior are set at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), per scope (a scope is a channel, a workspace, or your whole organization), so the same agent can work differently in different channels. Most controls below are Owner-only.

| Setting | What it does | More |
| --- | --- | --- |
| Custom instructions | Standing guidance read in every session on a scope, like team conventions. Outranks channel memory. | [Add custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions) |
| Plugins | Bundles of skills that teach Claude how to use a specific tool | [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins) |
| Connections | Which systems it can reach from each channel | [Add connections](/docs/claude-tag/admins/add-connections) |
| Claude in Slack version | Which generation answers (New, Legacy, or Off) in a scope | [Migrate from the earlier Claude in Slack](/docs/claude-tag/admins/restrict-access#migrate-from-the-earlier-claude-in-slack) |

###  Channel connections are separate from personal connectors

An Owner configures Claude’s connections, plugins, and skills, and they apply per scope. They are separate from the connectors, skills, or MCP servers an individual user has set up in their own claude.ai or Claude Desktop account. A user’s personal connectors are not available to Claude in a channel, and the channel’s connections are not visible in that user’s claude.ai.
To give Claude access to a tool that is not in the built-in connection list, including a custom MCP server, see [add a custom connection](/docs/claude-tag/admins/connections/custom).

##  Change behavior from the channel

Everything below is open to channel members, with no admin involved. Members tell Claude in the channel and the instruction saves to channel memory.

| To change | Say something like | More |
| --- | --- | --- |
| How Claude formats output | ”remember for this channel: post reports as a table” | [Memory](/docs/claude-tag/users/memory) |
| How chatty Claude is | ”ask before posting anything longer than a screen” | [Memory](/docs/claude-tag/users/memory) |
| When Claude follows a thread | ”stay quiet in this thread unless someone tags you” | [Control when Claude Tag responds](/docs/claude-tag/users/when-claude-responds) |
| What Claude does on a schedule | ”every morning at 9, post a digest of open threads” | [Set up routines](/docs/claude-tag/users/proactivity) |
| What Claude remembers | ”what do you remember about this channel?” then correct it | [Memory](/docs/claude-tag/users/memory) |

Channel changes are saved to channel memory, so verify one stuck by asking what it remembers.

##  Settings no one can change

* The Claude app’s name, @-handle, and avatar in Slack are the same in every workspace; there is no rename or rebrand setting.
* Channel sessions run on Claude Opus, with no setting to switch to Sonnet or Haiku. See [current limits](/docs/claude-tag/admins/restrict-access#controls-that-arent-available).

* [What Claude Tag remembers](/docs/claude-tag/users/memory): how channel instructions are stored, shared, and corrected
* [Good habits for working with Claude Tag](/docs/claude-tag/users/good-habits): phrasings that make recurring output consistent
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): why access is set per channel

[Vercel](/docs/claude-tag/admins/connections/vercel)[Add custom skills](/docs/claude-tag/admins/skills-repo)
