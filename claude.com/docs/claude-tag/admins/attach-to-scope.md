<!-- source: https://claude.com/docs/claude-tag/admins/attach-to-scope -->

This page covers adding access to more workspaces and channels, and how access stacks when several bundles apply to the same place. It assumes you have already [paired a workspace](/docs/claude-tag/admins/pair-workspace) and [created an Access bundle](/docs/claude-tag/admins/add-connections). You must be an Owner in your Claude organization to attach bundles.
A scope is where a bundle applies: **Default Slack access** (the organization-wide root), a workspace, or a single channel. Bundles inherit downward through those scopes, and when credentials overlap, the narrowest scope wins.

##  How scopes inherit

Bundles stack downward. A channel gets whatever is attached at Default Slack access, plus its workspace, plus anything attached to the channel itself.
![Nested boxes. The outermost box is the Default Slack access scope: a bundle attached here is the baseline every channel gets. Inside it, two examples. Outside the workspace box, a channel called another-team in a different workspace gets only the default bundle. Inside the workspace box, which adds an optional bundle for channels inside it, two channel boxes: a public channel called general, with no channel bundle, gets the default plus the workspace bundle; a private channel, marked with a lock, with its own channel bundle, gets all three, the default, workspace, and channel bundles.](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/scope-inheritance.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=673f78c6c43aceb03ed9c81a2de7b0b2)
![Nested boxes. The outermost box is the Default Slack access scope: a bundle attached here is the baseline every channel gets. Inside it, two examples. Outside the workspace box, a channel called another-team in a different workspace gets only the default bundle. Inside the workspace box, which adds an optional bundle for channels inside it, two channel boxes: a public channel called general, with no channel bundle, gets the default plus the workspace bundle; a private channel, marked with a lock, with its own channel bundle, gets all three, the default, workspace, and channel bundles.](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/scope-inheritance-dark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=b53a534b076e6c22f0d86a81841b00a8)

| Scope | What it covers | Access |
| --- | --- | --- |
| Default Slack access | Every Slack workspace and channel | The baseline set every channel gets |
| Workspace | All channels in one Slack workspace | Inherits Default Slack access, plus workspace-level bundles |
| Channel | A single Slack channel, public or private | Inherits Default Slack access and workspace, plus channel-level bundles |

The same stacking applies in reverse. Detaching a bundle from a channel removes only that channel’s additions, and bundles attached at the workspace or Default Slack access still apply there.
Memory is also scoped, but differently: there is no organization-wide memory, public-channel entries are shared across the workspace, and a private channel reads workspace memory but writes only to its own store. See [What Claude Tag remembers](/docs/claude-tag/users/memory).
DMs run under the user’s own claude.ai account, so bundles attached here apply only in channels. See [how DMs work in this model](/docs/claude-tag/concepts/agent-identity#direct-message-channels).

##  Attach the bundle

Attaching binds the bundle to a workspace scope or to a single channel under it, and the binding takes effect in new threads only.

###  Attach to a workspace

Each paired workspace already has a scope; bind a bundle in the scope’s **Access bundles** section. On the **Access bundles** page in the left navigation, each bundle’s card shows where it’s used. To add another workspace, [pair it](/docs/claude-tag/admins/pair-workspace) first.

###  Attach to a channel

Add channel scopes under a workspace for channels that need access beyond the workspace baseline:

1. On [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), find the workspace on the **Slack** tab under **Claude Tag’s access** and select **Add channel**.
2. Paste the channel’s ID into the **Channel ID** field. Channel IDs start with `C`. Copy the ID from the channel’s details in Slack.
3. Save, then bind bundles in the new scope’s **Access bundles** section, the same as for a workspace.

A bundle attached to a public channel grants its access to anyone who joins that channel. In most Slack workspaces, anyone can join a public channel, so the channel’s join policy becomes the effective access control for whatever the bundle grants. Keep elevated credentials in private-channel scopes.

##  Precedence when bundles overlap

A channel sees the **union** of every bundle bound at the channel itself, its workspace, and Default Slack access. Narrower scopes don’t replace wider ones; they add to them. When two bundles in the resolved set carry rules for the same host, the rule from the narrower scope wins. Within that union, fixed rules decide which credential and which instructions apply.

###  Which credential wins

When two bundles each carry a credential for the same host:

* The credential from the **narrowest scope** is used: channel beats workspace, which beats Default Slack access.
* Within the same scope, the order isn’t admin-configurable. Avoid binding overlapping credentials at the same scope; if you can’t predict which key acts, neither can a security review.
* There is no fallback. If the winning credential gets a `401` or `403`, Claude does not retry with the next one.

###  Repositories and plugins

Repository grants and plugins from every bound bundle are combined as a union; a channel gets every repo and plugin from any bundle in its chain. The **Access summary** section, shown when you select a scope on the Slack tab, lists the resolved set.

###  Custom instructions

Per-scope custom instructions are **concatenated**, Default Slack access first, then workspace, then channel. A channel’s instructions add to, rather than replace, what’s set above it.

###  Instruction layers

Three kinds of standing instruction can apply in a channel, written by different people:

| Layer | Who writes it | Where |
| --- | --- | --- |
| Custom instructions | Owner | The scope, in admin settings |
| Channel memory | Anyone in the channel | By telling Claude to remember |
| Task prompt | The requester | The message itself |

Channel members can shape how Claude responds in their channel through memory, but they can’t change which credentials or repositories it has; that’s bundle configuration. See [who controls what](/docs/claude-tag/admins/customize) for the full split.
Custom instructions are placed in the system prompt and take priority in practice, but they’re guidance, not an enforced guardrail. Don’t rely on them to block actions; use access controls for that.

###  Add custom instructions

Each scope can carry custom instructions, which are standing guidance Claude reads in every session there, like team conventions or where to file tickets. The field is in the scope’s settings dialog, opened from the **•••** button on the scope’s panel.
The field is plain text, inserted as written; there is no include or template syntax, and `{{include:...}}` is passed through literally. To give Claude a repository’s `CLAUDE.md`, [grant the repository](/docs/claude-tag/admins/configure-github#grant-repository-access) and name it in the request; its `CLAUDE.md` loads after the clone completes.

##  Verify the bundle is live

* The bundle card lists the workspace or channel you attached under the places it’s used.
* A test task in the pilot channel uses the bundle’s connections, and the action appears in the connected service’s audit log under your service account.

Repeat the attach step for any additional scopes that need elevated access, then widen per the [rollout patterns](/docs/claude-tag/admins/setup-overview#after-setup).

* [Getting started for users](/docs/claude-tag/users/getting-started): what your team does once the bundle is live
* [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access): narrow where it responds

[For Slack admins](/docs/claude-tag/admins/for-slack-admins)[GitHub access](/docs/claude-tag/admins/configure-github)
