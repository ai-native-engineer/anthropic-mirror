<!-- source: https://academy.claude.com/tutorials/claude-tag-admin-guide -->

2. /[Tutorials](https://academy.claude.com/tutorials)

[Tutorials](https://academy.claude.com/tutorials)

# Claude Tag admin guide

Pair your Slack workspace with Claude Tag and decide what systems it can access. This tutorial walks you through the setup flow, covers post-launch oversight, and links to the full documentation for each step.

25 minClaude Tag

![](https://academy.claude.com/assets/v1/thumbnail.dark-hq618sar.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-hq618sar.png)

Claude Tag (public beta) is Claude working in your team's Slack channels, with its own accounts in your tools. People tag Claude the way they'd tag a colleague, and Claude Tag picks up the work and follows through in the thread. Hand it standing work and it runs on its own: a Monday-morning routine posts its report before anyone opens Slack. Out of the box, anyone on your team can tag Claude, and Claude Tag answers using your team's connected tools, from Google Drive to BigQuery to GitHub. By the end of this guide you'll have paired the workspace, decided who can use Claude Tag, connected its tools, capped its spending, and planned the rollout.

## 1. Before you start[](#before-you-start)

You will need:

* **A Team or Enterprise plan:** individual plans and third-party deployments don't qualify ([the prerequisites(opens in new tab)](https://claude.com/docs/claude-tag/admins/setup-overview#before-you-start) cover what to do if you don't have one).
* **An Owner (or Primary Owner) in the Claude organization that will hold the pairing:** pairing and access bundles are Owner-only writes (on Enterprise, a channel manager an Owner has delegated can also create a bundle for their assigned channel; section 4), and Owner status in another Claude organization does not apply.
* **A Slack workspace admin:** installs the app and generates the pairing code. On Enterprise Grid, a Grid org admin also qualifies. The code is single-use and expires 15 minutes after generation, so coordinate to be online at the same time. This person can be the same as the Owner.
* **A funded usage balance:** on a Team plan, Claude Tag won't answer in channels until your organization's usage balance is funded, and a launch usage credit counts as funding. How channel work bills, and the card-billed vs. invoiced difference, is in [Set a spend limit(opens in new tab)](https://claude.com/docs/claude-tag/admins/set-spend-limit).
* **An IP allowlist entry, filed early:** if a connected service restricts by source IP, add Anthropic's published egress range now; enterprise allowlist changes can take days, and every connected service must be reachable from the internet ([network requirements(opens in new tab)](https://claude.com/docs/claude-tag/admins/network-requirements) has the range).
* **A Claude organization without Zero Data Retention (ZDR) or customer-managed encryption keys (CMEK):** neither policy permits Claude Tag. If other Claude products need them, ask your account team about a separate Claude organization to hold the Slack pairing.
* **Routines enabled for your Claude organization (Admin settings › Capabilities):** Claude Tag requires the feature. Until an admin enables it, every mention and direct message (DM) gets an "unavailable" reply and no work happens.
* **One Claude organization to hold the pairing:** a Slack workspace (or Enterprise Grid) pairs with one Claude organization at a time. If your company has multiple organizations, determine which one holds the pairing before you connect.

### The six decisions you own[](#six-decisions)

1. **Where Claude Tag lives:** the paired workspace and which channels it works in (sections 3–4).
2. **Who steers it:** Owners hold the admin controls; channel members shape their own channel from within it (sections 4–5).
3. **What it can touch:** repositories, credentials, connections, and plugins, organized into access bundles and scoped to different levels (section 4).
4. **How it behaves:** ambient or mention-only, controlled by a switch on each channel's `Configure` page, plus written instructions (section 5).
5. **What it remembers:** channel and workspace memory that you can open, edit, and delete (section 5).
6. **What it costs:** a monthly ceiling for the organization and a limit per channel (section 6).

When a question about Claude Tag comes up later, start by working out which of the six it touches.

## 2. The map: five surfaces, three scopes[](#the-map)

Claude Tag's settings are spread across several pages in claude.ai and Slack, each controlling a different type of configuration.

| Surface | Who changes it | What it controls |
| --- | --- | --- |
| The Claude Tag admin page, under Admin settings › Products | An Owner | Access, custom instructions, the default model, and where Claude Tag may operate, per scope, plus each channel's `Respond automatically` switch |
| The Usage page, under Admin settings › Usage | An Owner or Admin | The organization spend limit, per-channel limits, and the per-channel spend breakdown |
| The `Configure` link, in the footer of Claude's replies in Slack (Grid-shared channels have no `Configure` link) | Channel members in your Claude organization | That one channel's `Respond automatically` switch, its instructions, and its plugins (an Owner can block member edits to this page) |
| Personal connectors, under Customize › Connectors on claude.ai | Each user | Which of their own tools apply in their direct messages with Claude Tag and, in organizations where Anthropic has enabled it, for their own tasks in a channel |
| The Analytics page, under Analytics › Claude Tag | Anyone who can view the Analytics dashboard | Read-only: spend to date and projected, spend by channel, and spend by kind of work |

Channel memory and individual routines aren't created on a settings page: you shape both by talking to Claude Tag in the channel. An Owner can review both (memory files from the scope's menu, section 5; routines from the Activity page's Scheduled work tab, section 7), and the org-level Routines feature itself is switched on by an admin (see Before you start). The [settings map(opens in new tab)](https://claude.com/docs/claude-tag/concepts/settings-map) is the one-page reference.

### Access is granted in scopes, and scopes inherit downward[](#scopes)

Access is packaged into access bundles: named sets of connections, repository grants, domains, plugins, and instructions. Bundles attach to scopes. There are three scopes:

1. **Default Slack access:** the organization-wide root that every channel gets.
2. **A workspace:** everything Claude Tag does in that paired workspace.
3. **A single channel:** just that one room.

Scopes stack downward, so a channel sees the union of everything above it plus its own:

1. **Narrower scopes only ever add:** detaching a channel's bundle removes only that channel's additions; the workspace and default bundles still apply there.
2. **Same host, two credentials, the narrowest scope supplies the credential:** channel beats workspace beats default, with no fallback. If the winning credential returns a 401 or 403, Claude Tag does not quietly retry with the next one.
3. **Custom instructions concatenate top-down:** default first, then workspace, then channel. A channel's instructions add to what's set above it.
4. **A thread keeps what it started with:** a running thread keeps the skills, plugins, and custom instructions it began with, while connections and domain rules apply on every request, so a connection added mid-thread works if you name the service. After any configuration change, test from a new top-level thread.

**A bundle on a public channel is open to everyone who joins:** in most workspaces anyone can join a public channel, so the channel's join policy becomes the effective access control. Keep elevated credentials on private-channel scopes. See [per-channel access(opens in new tab)](https://claude.com/docs/claude-tag/admins/attach-to-scope).

## 3. Get live: the setup flow, screen by screen[](#get-live)

Aside from two moments in Slack itself (installing the app and sending the connect message) and the accounts you create in your own tools (steps 3–4), every setup step runs on one page: claude.ai's Admin settings › Products › Claude Tag (claude.ai/admin-settings). Every step saves as you go, so you can leave and come back later.

**Varies by org:** this guide walks the six-step path a card-billed organization billing in US dollars with no usage credits loaded sees, where Buy usage credits comes before Launch and the spend limit is set on the Usage page after launch. Invoiced organizations, organizations billing in another currency, and organizations with credits already loaded skip that step, so for them Launch is the fifth step and carries the spend-limit picker. See the [setup steps(opens in new tab)](https://claude.com/docs/claude-tag/admins/setup-overview).

### Step 1. Pair your Slack workspace[](#step-1-pair)

Pairing takes one code. It links your Claude organization to Slack, and Claude Tag joins the workspace like a new member with its own profile.

1. **Add the Claude app to Slack** from the Slack Marketplace. A Slack workspace admin does this.
2. **Invite Claude and send `@Claude connect`:** in a channel with no guests that belongs only to this workspace, run `/invite @Claude` (Claude posts a short welcome), then send `@Claude connect` as a new message with no other text. Claude Tag can decline to reply in guest channels, and Slack Connect channels don't work at all. Claude replies with a one-time pairing code that only you can see.
3. **Paste the pairing code** into the `Paste the pairing code` field on this screen; `Connected to` and your workspace name appear when it's accepted.
4. **Choose where Claude can reply when tagged**, between `Entire workspace` and `Specific channel`. `Entire workspace` is the recommended default. (If the screen doesn't ask, Claude Tag replies across the whole workspace once you launch.)
5. **Click `Pair workspace`.**

#### Entire workspace or Specific channel

| Choice | What it does |
| --- | --- |
| `Entire workspace` | The Launch step sets that workspace's own switch to On. |
| `Specific channel` | Confines the pilot to named channel IDs; you can expand later without pairing again. The Launch step sets each chosen channel's own switch to On. |

Both set a switch you can hand back to `Inherit` later (section 4; a Team plan has a single switch for all workspaces instead). Neither choice automatically adds Claude Tag to any channel: members bring it in one channel at a time, and it joins on its own only where an admin has set an auto-join channel-name rule (section 4). How members add it, and how those joins appear in Slack's audit log, is covered in [What the Claude Slack app can access(opens in new tab)](https://claude.com/docs/claude-tag/admins/for-slack-admins#where-claude-reads-and-posts).

*The console shown is an illustration of a fictional company; all names and numbers are invented.*

#### What access pairing grants

Pairing grants Claude Tag no one's existing access. It takes nothing from:

* The Slack admin who installs the app
* The Owner who redeems the code
* Any workspace member's connected tools

It creates a new participant in Slack, tied to your Claude organization, and that participant has no access to your external systems until an Owner (or, on Enterprise, a channel manager an Owner has delegated) adds connections.

#### Pairing on Enterprise Grid

On Slack Enterprise Grid, the `@Claude connect` reply carries two codes: `workspace_…` pairs one workspace, and `enterprise_…` pairs the whole grid. DMs work only for people whose home workspace is paired, so pair the grid if DMs should work for everyone. [The pairing steps in the setup docs(opens in new tab)](https://claude.com/docs/claude-tag/admins/setup-overview#pair-your-slack-workspace) cover both codes and have the complete walkthrough.

### Step 2. Choose Claude Tag's first tools[](#step-2-tools)

Claude Tag works in tools with its own account, so it acts as itself, not as you. Pick at least two tools your team actually works in to start (`Search all tools` finds ones not shown; GitHub has its own step next).

#### Connections and connectors

**A connection is Claude Tag's; a connector is yours.** The tools you connect in this setup flow become connections: Claude Tag's own sign-ins, shared by the workspace or a channel, recording every action under Claude Tag's name for audit and revocation. A connector is a tool on your own claude.ai account, under Customize › Connectors: private to you, and used in your direct messages with Claude Tag.

In organizations where Anthropic has enabled personal connectors in channels, Claude Tag can also offer to use your connectors for a task you asked for in a channel, after you allow it, and never for anyone else's request. The boundary otherwise runs both ways: your connectors don't do the channel's shared work, and a channel's connections don't follow anyone into their DMs.

### Step 3. Connect GitHub, then choose repositories[](#step-3-github)

If your GitHub organization doesn't yet have the [Claude GitHub App(opens in new tab)](https://claude.com/docs/claude-tag/admins/configure-github), the GitHub owner installs it here; [the setup docs(opens in new tab)](https://claude.com/docs/claude-tag/admins/setup-overview#connect-github) cover the three states this screen can show, including an app installed on a personal GitHub account (Claude Tag needs it on a GitHub organization).

#### Choose repositories

Once the app is installed, you land on the repository picker: one row per GitHub organization, with options to connect all or pick specific ones. These grants attach to the workspace you just paired and apply to every channel Claude Tag works in there; on an Enterprise Grid organization-wide pairing they apply across the whole organization instead.

Treat the picker's grants as a floor: a bundle bound to a workspace or channel adds repositories on top, and narrower scopes only ever add. The real ceiling is upstream of any bundle, in the Claude GitHub App installation's repository selection on github.com.

You can skip this step and grant repositories from the admin page later. See [granting repository access(opens in new tab)](https://claude.com/docs/claude-tag/admins/configure-github#grant-repository-access).

### Step 4. Create accounts for Claude Tag's other tools[](#step-4-accounts)

Claude Tag can't act in a tool until it has an account there, so a skipped tool stays out of Claude Tag's reach until you add it. The account is usually an email address Claude Tag can be invited with; some tools that do not support email accounts offer service accounts instead, which serve the same purpose.

#### Create the account and paste its keys

The screen shows three rows (create the email address, invite Claude Tag to each tool, connect each tool with its credentials); the work behind them is four sub-steps:

1. Create an email address for Claude Tag.
2. Invite it to each tool the way you'd invite a new hire (scoped to only what it needs).
3. Create an API key as Claude Tag in each tool.
4. Paste each key here.

[The setup docs(opens in new tab)](https://claude.com/docs/claude-tag/admins/setup-overview#create-accounts-for-claude%E2%80%99s-other-tools) detail each sub-step; work one tool end to end before starting the next.

*The console shown is an illustration of a fictional company; all names and numbers are invented.*

#### Limit what each account can reach

For the recommended account pattern per service type, and how to limit each account to only the folders, projects, or spaces Claude Tag should reach, see [creating a dedicated account per service(opens in new tab)](https://claude.com/docs/claude-tag/admins/add-connections#create-a-dedicated-account-per-service); the [per-service connection guides(opens in new tab)](https://claude.com/docs/claude-tag/admins/connections/overview) have the exact credential fields and allowed-website values per tool.

### Step 5. Buy usage credits[](#step-5-credits)

Claude Tag runs on usage credits: its channel messages and tool actions draw from your organization's usage balance.

**Load the credits on this setup screen:**

1. Type an amount ($5 or more).
2. Confirm the total.
3. `Buy now` charges your saved card.

If your organization has a launch usage credit, it counts as funding, so check what you already have before you buy.

You can skip and fund later from the Usage page, but Claude Tag stays silent in channels until the balance is funded. See [Set a spend limit(opens in new tab)](https://claude.com/docs/claude-tag/admins/set-spend-limit).

**Varies by org:** invoiced organizations, organizations billing in a currency other than US dollars, and organizations with credits already loaded do not see this step. Instead, the Launch screen shows a monthly spend-limit picker ([the setup docs(opens in new tab)](https://claude.com/docs/claude-tag/admins/setup-overview#launch-claude-tag) list the options); "Unlimited" is a choice you'd have to make on purpose.

### Step 6. Launch Claude Tag[](#step-6-launch)

One decision every organization sees at launch: the `Let members know they can now tag Claude` toggle, which has Claude Tag DM each member to say it's available. Those messages do not count toward billing. The toggle is on by default; turn it off until your pilot channel is running well and you want wider adoption.

**Then press `Launch Claude Tag`.**

## 4. Access and identity[](#access-and-identity)

After launch, come back to the Claude Tag page (claude.ai's Admin settings › Products › Claude Tag). It's your control room:

* The enable switch for the organization
* The `Allow direct messages` switch under it
* The included-usage meter if you started on a promotion
* Two sections below them: Where Claude Tag works, one row per surface, and Claude Tag's access

### One toggle decides who may use Claude Tag[](#restrict-toggle)

**Under Where Claude Tag works, click `Manage` next to Member access and set the restriction toggle: `Restrict to your organization` on a Team plan, `Restrict to roles with Claude Tag access` on Enterprise.** The toggle decides who in the paired workspace can use Claude Tag, and it applies to channels and direct messages alike:

* **Off (the default):** anyone in the workspace can use Claude Tag in channels, whether or not they have a Claude account. A direct message still needs the person's own Claude account, because a DM runs on it (the identity model below).
* **On:** only Slack users with a Claude account in your organization can.

On Enterprise, every built-in role already grants the `Claude Tag in Slack` capability, so in an organization with no custom roles, turning it on simply limits Claude Tag to your organization's members. To narrow further, create a custom role that grants or withholds the capability; see [restrict by role on Enterprise(opens in new tab)](https://claude.com/docs/claude-tag/admins/restrict-access#restrict-by-role-on-enterprise).

If your organization sits under a parent enterprise organization, the Member access dialog also offers `Restrict to your verified domains`. The dialog lists the connected workspaces as well, each with a `Disconnect`. Disconnecting deletes that workspace's Claude Tag data after a short grace period (your access bundles stay), so read [disconnect a workspace(opens in new tab)](https://claude.com/docs/claude-tag/admins/workspaces#revoke-a-pairing) before you use it. See [restricting who can use Claude Tag(opens in new tab)](https://claude.com/docs/claude-tag/admins/restrict-access#restrict-who-can-use-claude).

### Three settings that are easy to mix up[](#three-settings)

| # | Setting | What it controls | Where you set it |
| --- | --- | --- | --- |
| 1 | Who can invoke it | Which people can address Claude Tag at all | The member-access toggle (above): `Restrict to your organization` on Team, `Restrict to roles with Claude Tag access` on Enterprise |
| 2 | Where it answers | Which channels and workspaces respond | Each scope's enable switch (`Enable Claude Tag in Slack`, `Enable Claude Tag in this workspace`, or `Enable Claude Tag in this channel`); its `Claude Tag version` under `Advanced`: New, Legacy (the earlier per-user generation of Claude in Slack, where still offered; see below), or Inherit (use the parent scope's value) |
| 3 | What it can touch | Credentials and repositories | Access bundles bound to scopes, the only one of the three that controls credentials |

#### Scope switches and Inherit

Turning a scope's switch off stops Claude Tag there (on Default Slack access it turns off Legacy too); a workspace or channel with its own On setting stays on even when the scope above it is off. That includes a workspace you launched with `Entire workspace`, or each channel you chose in a `Specific channel` launch: the Launch step sets that scope's switch to On for you.

To make a scope follow the one above it again, set its `Claude Tag version` under `Advanced` back to `Inherit`, or use the inherited-setting link beside its switch (an "Inherited: On" or "Inherited: Off" byline there shows what the scope above passes down until you set the switch yourself).

On the Team plan you instead see a single `Enable Claude Tag` switch on Default Slack and no per-scope switches; it turns Claude Tag on or off in every connected workspace at once.

#### Guests and Slack Connect

Two checks run before a scope's enable switch is consulted. Claude Tag is off in any channel that includes a Slack guest unless the scope's `How should Claude work in channels with guests` is set to `Channel only` or `Full access`. Under `Channel only` and `Full access` alike, guests can read what Claude Tag posts there. Under `Channel only`, treat the channel's own instructions, and those in any bundle attached directly to it, as visible to them; under `Full access`, treat everything the scope inherits as visible too.

Claude Tag doesn't work in Slack Connect channels, the channels your workspace shares with another company, and no admin setting turns it on there; see [Slack Connect channels in the docs(opens in new tab)](https://claude.com/docs/claude-tag/admins/restrict-access#slack-connect-channels) for what a mention gets and what happens when a channel Claude Tag works in becomes one.

#### Grid-shared channels

Claude Tag answers in a channel shared across your Enterprise Grid's workspaces only when every one of them is paired to your Claude organization, and even then with just your Default Slack access scope (workspace and channel bundles, instructions, and memory don't reach it). See [grid-shared channels(opens in new tab)](https://claude.com/docs/claude-tag/admins/restrict-access#channels-shared-across-workspaces-in-your-enterprise-grid) for the guest check, the refusal cases, and why there is no per-channel override.

#### The Legacy version

Legacy is the earlier Claude in Slack; skip this if your organization never used it. Both versions answer through the same Claude app, so turning off `Enable Claude Tag in Slack` on Default Slack access turns off Legacy too; setting a scope's `Claude Tag version` to `Legacy` keeps the earlier generation answering there.

Legacy is being deprecated; your account team has the cutover date, after which scopes still on Legacy stop responding until set to `New`. You can tell a scope is still answering with Legacy when pull requests it opens appear under the asker's name instead of its own. See [migrating from the earlier Claude in Slack(opens in new tab)](https://claude.com/docs/claude-tag/admins/restrict-access#migrate-from-the-earlier-claude-in-slack).

### The access editor: pick a scope, read its access[](#access-editor)

Under Claude Tag's access, the Slack tab is a two-pane editor.

#### The left rail: your scopes

* **Default Slack:** at the top is Default Slack access, the organization-wide root. Each paired workspace sits under it with its channels underneath.
* **Channels appear automatically:** whenever Claude Tag is added to a channel in Slack, that channel shows up here as a scope under its workspace, with nothing to create on this page. The `Search channels` field finds one by channel name or ID.
* **Add the rest yourself:** a channel that isn't listed yet gets a scope with `Add channel`; [attach to a channel(opens in new tab)](https://claude.com/docs/claude-tag/admins/attach-to-scope#attach-to-a-channel) covers finding channel IDs and the private-channel caveat.

#### The right pane: the selected scope

* **Connectors:** every connector Claude can use in this scope, the scope's own and the inherited ones in one list, with a `+` for attaching a single connector without opening a bundle. Despite the name, this section deals in Claude Tag's own connections, not anyone's personal connectors (section 3's boundary).
* **Repositories:** every repository Claude can reach in this scope, own and inherited in one list, with the same `+` for granting a single repository.
* **Plugins:** the org plugins Claude loads in this scope, own and inherited in one list, with the same `+`; the section appears once your organization has installed plugins.
* **Custom instructions:** the scope's standing guidance, in plain text.
* **Access bundles:** the bundles attached to this scope, each with a remove, plus a `+` to attach another. What a bundle from a parent scope grants shows up in the lists above; to change it, edit the scope it comes from.

Each row carries an origin line naming the scope or bundle it came from; select the name in it to open that scope or bundle (both forms of the origin line are explained under [attach a single repository or connector(opens in new tab)](https://claude.com/docs/claude-tag/admins/attach-to-scope#attach-a-single-repository-or-connector)).

#### Reading a scope's lists

A scope's lists are the resolved answer: every connector and repository this channel ends up with after the channel's bundles, the workspace's, and the root's are unioned together, each row labeled with where it came from. When someone asks "Can Claude reach Datadog from this channel?", open the scope and read its Connectors and Repositories lists instead of reasoning about inheritance.

Which credential acts on a host is rule-governed: Claude Tag uses the narrowest scope's credential, with no fallback to a broader one. Keep the map just as legible within a scope by binding one credential per host per scope; then the Connectors list reads one-to-one, for you and for any security review.

*The console shown is an illustration of a fictional company; all names and numbers are invented.*

### The rest of a scope's settings live under Advanced[](#advanced-controls)

The scope's `Advanced` section holds `Claude Tag version`: New or Legacy (where still offered), plus Inherit on workspaces and channels. The other `Advanced` settings:

* **Default model:** the model new sessions start on, drawn from the models your organization allows for Claude Code. A scope without its own setting inherits its parent's.
* **Auto mode allow rules:** plain-sentence rules that pre-approve actions Claude Tag's permission checker would otherwise flag or stop. Rules inherit downward, so keep each one narrow ([auto mode allow rules(opens in new tab)](https://claude.com/docs/claude-tag/admins/customize#auto-mode-allow-rules) has the form and an example).
* **Environment:** the cloud environment the scope's sessions run in, which sets their network access level (see Credentials never reach the sandbox, below).
* **Channel name rules:** two pattern lists on the root and workspace scopes: blocked channel patterns keep Claude Tag out of channels whose names match, and auto-join channel patterns add it to new public ones.
* **How should Claude work in channels with guests:** three values. `Restrict`, the default, means Claude Tag doesn't reply wherever a guest is present; `Channel only` lets it answer with only what's set directly on the channel (its own instructions and connections, plus a bundle attached to it whose attachment includes channels with guests; members-only is the default), with nothing inherited from the workspace or the organization, no memory or skills, and the standard environment in place of the scope's own ([how Channel only works(opens in new tab)](https://claude.com/docs/claude-tag/admins/restrict-access#how-channel-only-works) has the full exclusion list); `Full access` lets Claude Tag use everything the scope gives it. Even on `Full access`, workspace search is unavailable while a guest is present, and `Channel only` takes effect only on scopes set to `New`.
* **Channel member edits:** whether channel members can edit this channel's settings from the `Configure` link in Slack. `Block` at the workspace or root makes the whole `Configure` page read-only for members across every channel beneath it (section 5 has the details). A channel manager (on Enterprise, someone an Owner has delegated that channel's setup to) can still edit the channel's instructions and default model regardless of this setting.
* **Respond automatically** (a per-channel setting; workspaces and the organization have no such switch): on by default; turn it off and Claude Tag replies in that channel only when mentioned. Channel members can also flip this by asking Claude Tag in Slack.

The rows carry an Inherit option that shows what a scope currently resolves to. That is the place to look when one channel behaves differently from its siblings. See [which settings admins control(opens in new tab)](https://claude.com/docs/claude-tag/admins/customize#settings-admins-control).

### Inside a bundle, and who can edit what[](#inside-a-bundle)

**Click a bundle to open it.** The bundle editor has five tabs:

1. **Credentials:** Claude Tag's own account in each app. Connect a preset, or use `Custom tool` for anything with an API; a credential's `Edit` can narrow what it may do by HTTP method and path ([add a connection(opens in new tab)](https://claude.com/docs/claude-tag/admins/add-connections#add-a-connection)).
2. **Repositories:** the GitHub grants for this bundle.
3. **Domains:** hosts allowed through with no credential attached, and, where your organization has it, a Blocked domains list: blocked entries are checked ahead of this bundle's allowed domains. A domain entry needs only the host, plus a port when the service isn't on 443.
4. **Plugins:** your organization's plugins toggled on for this bundle.
5. **Instructions:** text that rides along wherever the bundle is bound.

Each bundle shows how many scopes use it. **Check that count before you edit a shared bundle.**

#### Who can do what

The built-in Admin role in your Claude organization can't do any of these:

* Pair a workspace
* Manage access bundles
* Open the Activity page or memory files

Those need an Owner (the one delegation is the Enterprise channel manager below). Spend limits are the exception: an Owner or Admin can set those on the Usage page.

| Who | What they can do |
| --- | --- |
| A channel manager (Enterprise) | Create a bundle for an assigned channel and edit that bundle's Credentials and Plugins tabs (not its Repositories, Domains, or Instructions tabs), plus the channel's own instructions and default model, and, from the channel's `Configure` page, repositories their own GitHub account is an admin of; pairing a workspace and organization-wide settings stay with Owners |
| Channel members | Work from inside the channel: memory, routines, the `Configure` page |

The full table is in the docs; see [permissions by role(opens in new tab)](https://claude.com/docs/claude-tag/admins/restrict-access#permissions-by-role).

### The identity model: Claude Tag acts as itself by default[](#identity-model)

In a channel, Claude Tag acts with its own service accounts:

| Where | Claude Tag's account |
| --- | --- |
| In Slack | The Claude app |
| On code | The Claude GitHub App |
| In every other tool | The service account you provisioned |

Claude Tag doesn't use the requester's own access for a channel's shared work. Two things follow: every action taken through the channel's connections is attributable to Claude Tag, which makes audit clean; and least privilege becomes a decision you make when you connect each tool. Three points to carry into that decision:

* **Its own accounts:** the channel's own connections give everyone in it the same capability, so the shared work doesn't change based on who asked. (Where personal connectors in channels is enabled, a member's own connectors can additionally serve that member's own task, with their approval.)
* **Grant read broadly, write narrowly:** read-only connections across the tools your teams work in are a sound day-one default. Add write access per team's bundle, only where you want Claude Tag changing things, and revisit as it earns trust.
* **Keep a human as the approver:** pull requests Claude Tag opens are authored by the Claude GitHub App, so required-review branch protection still demands a human approval. But it no longer keeps the asker from approving their own request, because GitHub blocks only the PR's author (under Legacy, the asker was the author). To make sure a second person reviews Claude Tag's work, require two approving reviews in the branch protection rule, and dismiss stale approvals on new commits.

**Direct messages are the exception.** A DM has no channel to scope it to, so it runs on that person's own claude.ai account, with their personal connectors, billed to their seat, and attributed to them, except for pull requests: the Claude GitHub App authors those from DMs too, though it can only reach repositories connected on that user's own account.

Channels are the shared, service-identity surface; DMs are personal. See [how agent identity works(opens in new tab)](https://claude.com/docs/claude-tag/concepts/agent-identity).

### Credentials never reach the sandbox[](#credential-boundary)

Each channel task runs in an isolated sandbox, one per thread, and that sandbox holds no keys. In an Anthropic-hosted environment, when the work needs an outside system the request crosses Agent Proxy, the network boundary, which checks it against your rules and attaches the matching credential there. The model and the sandbox are not handed the key.

A request that matches no connection rule, no Domains entry, and no environment setting is blocked, and only HTTP and HTTPS cross at all. See [security and data handling(opens in new tab)](https://claude.com/docs/claude-tag/concepts/security-and-data).

**What Claude Tag can reach:** the environment layer starts at the `Trusted access` network level, a documented set of package registries and developer hosts. For broader access, create an organization-shared environment from the Cloud environments page in Admin settings with a more permissive level (`Full access` allows any domain) and pin it on the scope. **Do not create it at claude.ai/code**, where environments belong to your individual account and never appear in the picker.

Allow-all egress, a `*` entry on a bundle's Domains tab, is off by default and enabled per organization by Anthropic; see [allowing a host without a credential(opens in new tab)](https://claude.com/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential).

Web search runs on Anthropic's servers, outside all these layers; [web search vs. network requests(opens in new tab)](https://claude.com/docs/claude-tag/admins/add-connections#web-search-vs-network-requests) explains why Claude Tag can quote a page it can't open.

### For companies that handle PHI[](#for-companies-that-handle-phi)

If anyone in your Slack workspace handles protected health information (PHI), configure Claude Tag so that it cannot read, search, or connect to places that might include PHI. Claude Tag is in public beta and is not a HIPAA-eligible service under Anthropic's Business Associate Agreement (BAA). Do not submit PHI to Claude Tag.

In an organization on Anthropic's HIPAA-ready Enterprise offering, Claude Tag additionally starts switched off; an Owner can turn it on, and it remains outside BAA coverage. The Claude Tag documentation carries the fuller procedures: see [Use Claude Tag at a healthcare organization(opens in new tab)](https://claude.com/docs/claude-tag/admins/healthcare).

**What this setup covers:** Claude Tag is not BAA-covered, and this configuration doesn't change that: it limits where PHI can reach Claude Tag; whether your deployment meets HIPAA requirements is a determination for your compliance team. This guidance addresses PHI under HIPAA; other rules that may apply to health or clinical data in your workspace are not addressed here. Review it with your own privacy and compliance counsel. For questions, ask your Anthropic account team if you have one, or reach Anthropic Support through the Claude Help Center.

#### Retention and deletion

Claude Tag retains channel memory and session transcripts (the Zero Data Retention item in section 1), so treat "what Claude can reach" as the boundary to design. Deleting a memory file doesn't delete transcripts, and there is no control that deletes a single thread's transcript.

The deletion controls run from largest to smallest: disconnecting a workspace deletes the workspace's Claude Tag data (sessions and transcripts, memory, routines, published artifacts, scopes, and members' account links; the `Disconnect` control itself is in the Member access dialog, above), and removing a channel's entry under Claude Tag's access deletes that channel's transcripts, memory, routines, and published artifacts.

Removing a channel's entry doesn't reach what the channel's sessions left elsewhere: notes saved to shared workspace memory or transcripts in other channels (disconnecting the workspace does delete those). And neither control reaches the pages, tickets, and pull requests Claude Tag created in your connected tools; those live in those tools and are yours to clean up.

#### What to do if PHI reaches a channel

If PHI does reach a channel, Anthropic recommends the following, alongside your own incident-response and HIPAA obligations: report to your privacy officer, remove the Slack message in line with your retention and legal-hold policies, have an Owner remove that channel's entry immediately, check workspace memory for notes saved while the channel was public, then contact Anthropic at [privacy@anthropic.com(opens in new tab)](mailto:privacy@anthropic.com) for anything those controls don't reach, for example a transcript in another channel whose session found the message through search. Include the workspace, the channel ID, and the approximate time of the message. Do not include the PHI itself.

#### The recommended configuration

* **Run Claude Tag as an allowlist:** turn off `Enable Claude Tag in Slack` on Default Slack access, set any workspace or channel that has its own On setting back to `Inherit` (the inherited-setting link beside its enable switch, or `Claude Tag version` under `Advanced`; a workspace you launched with `Entire workspace` has one, and so does each channel chosen in a `Specific channel` launch), then turn on `Enable Claude Tag in this channel` on only the channels you approve. A mention anywhere else gets a disabled notice instead of a reply. Choosing `Specific channel` when pairing starts you in this posture. Per-scope switches are an Enterprise-plan capability. A Team plan has name-based blocked channel patterns and `Specific channel` pairing (see [limiting Claude Tag to specific channels(opens in new tab)](https://claude.com/docs/claude-tag/admins/restrict-access#limit-claude-tag-to-specific-channels)), and Team plans can't be HIPAA-enabled for any Anthropic service. If PHI may be present in your workspace and you're on a Team plan, don't deploy Claude Tag in that workspace. Whichever plan you're on, turn off `Allow direct messages` so every interaction happens in channels, where the controls and deletion ladder above apply; a DM runs on the member's personal account, with their personal connectors. See [allowing or disabling direct messages(opens in new tab)](https://claude.com/docs/claude-tag/admins/restrict-access#allow-or-disable-direct-messages).
* **Keep Claude Tag out of PHI's path entirely:** Claude Tag can read a channel's full history only where it has been added, so never invite it to a PHI-bearing channel. It can, however, keyword-search public channels across the workspace from the guest-free channels it works in; that search is the same keyword search any workspace member has, so the allowlist only keeps PHI out of Claude Tag's reach if your workspace policy already keeps PHI out of public channels. If you can't rely on that policy, pair Claude Tag with a separate Slack workspace that has no PHI rather than one in which PHI may appear. Approve PHI-free channels only. Slack Connect channels, the ones shared with other organizations, are already covered: Claude Tag doesn't work in them at all (see "Guests and Slack Connect," above). And Claude Tag is off by default wherever a Slack guest is present; see [restricting guest channels(opens in new tab)](https://claude.com/docs/claude-tag/admins/restrict-access#restrict-guest-channels).
* **Never connect PHI-bearing systems:** Claude Tag holds no credential for an external system until an Owner, or a channel manager an Owner has delegated, adds a connection, so the EHR and clinical tools simply never get one. Read each approved channel's Connectors and Repositories lists to confirm the resolved set. Also ask your account team whether personal connectors in channels is enabled for your organization; if it is, members' own claude.ai connectors count among the tools that must stay PHI-free. See [per-channel access(opens in new tab)](https://claude.com/docs/claude-tag/admins/attach-to-scope).
* **Review what accumulates:** an Owner can open, edit, or delete each scope's memory files. The Activity page lists scheduled work, and actions in connected tools land in those tools' own logs under Claude Tag's service accounts (work done with a member's personal connectors is recorded under that member's name instead; section 7). Published artifacts are pages hosted on claude.ai, so anything that reaches one is held by Anthropic until the channel's entry is removed. See [audit and review(opens in new tab)](https://claude.com/docs/claude-tag/admins/audit).

## 5. What your members will do, and what you control[](#when-it-responds)

Claude Tag is an ambient, multiplayer presence: one Claude per channel, shared by everyone in it. Wherever Claude Tag is on, a mention guarantees a reply; it isn't required for one.

What it can see follows the same shape: it reads the channels it has been added to, it can keyword-search public channels across the workspace (the same search any member has, though not from channels with guests; section 4), and it can't read private channels it isn't in.

### When it replies on its own[](#when-it-replies)

| Where the message is | Does Claude Tag reply without a mention? |
| --- | --- |
| A direct message | Yes, where DMs are enabled. |
| A thread it's already in | Yes, until someone quiets the thread. |
| A channel, top-level | Sometimes, when it judges it can answer the question or pick up the task. |

With Claude Tag enabled for your organization (section 4) and Routines enabled (section 1), four settings decide whether DMs work, and all four must allow it:

| DMs work only if | Where that lives |
| --- | --- |
| `Allow direct messages` is on | The Claude Tag page (section 4) |
| The person has their own Claude account | The identity model (section 4): a DM runs on their account |
| The member-access restriction includes them | The member-access toggle (section 4), which applies to DMs too |
| Their home workspace is paired (Enterprise Grid only) | Pairing, step 1 (section 3) |

### Quieting a channel[](#quieting)

The volume knob lives where the noise is heard. Anyone in the channel can turn it by telling Claude Tag there; a channel member in your Claude organization can also flip `Respond automatically` on the channel's `Configure` page (an Owner has the same switch under the channel scope's `Advanced` settings in Admin settings). Either way it applies to everyone's threads there.

Quiet one noisy thread by saying so in that thread, and remove Claude Tag entirely with `/remove @Claude`. The exact prompts to paste are in [Control when Claude Tag responds(opens in new tab)](https://claude.com/docs/claude-tag/users/when-claude-responds).

Claude Tag also understands a short list of commands, sent as `@Claude` followed by the exact command word: `!mute` and `!unmute` quiet a thread or undo it (muting is per thread by design), `!restart` resets a stuck or wrong-context session, `!configure` returns the link to this channel's `Configure` page, and `!status` asks whether Claude Tag is still working, with an answer only you can see. The full list (including `!fork`, `!help`, `!feedback`, and `!routines`), with each command's exact syntax, is in [Commands Claude Tag understands(opens in new tab)](https://claude.com/docs/claude-tag/users/commands).

Two behaviors surprise people before they read the docs: reacting 👎 to one of Claude Tag's replies mutes that thread (a mention that carries a request brings it back), and when a lot of messages pile up in a channel since Claude Tag last posted there, it stops reading that channel and unprompted replies stop with it; it doesn't announce this, and a mention starts it reading again.

### The hard boundaries[](#enforced-controls)

`Respond automatically` and the muting commands are guidance Claude Tag follows, and there is no organization-wide mention-only switch. If your security team wants an enforced boundary, use one of these:

| Enforced control | What it stops |
| --- | --- |
| The spend limit | New work in a channel once either limit is reached (section 6) |
| The member-access toggle | Who can use Claude Tag at all (section 4) |
| `Enable Claude Tag for your organization`, turned off | Everything, direct messages included |
| A scope's enable switch (`Enable Claude Tag in this workspace` or `Enable Claude Tag in this channel`), turned off | That workspace or channel; a scope beneath it with its own On setting stays on until set back to `Inherit` (section 4) |

### Channel members shape their own channel[](#configure-page)

Every Claude reply in Slack ends with a footer, and outside Grid-shared channels its `Configure` link opens a page for that channel. Anyone in the channel who is also in your Claude organization can adjust how Claude Tag behaves there.

The page's two levers are the `Respond automatically` switch and `Channel instructions`: standing guidance read in every session there, which outranks channel memory. Instructions cover tone, scope, what to route to a human, and what never to touch. A pilot channel's might read:

> Keep answers short and cite the dashboard you used. Only take on reporting questions for this team. Route anything about customer contracts to a human. Never touch production configs.

The rest of the page shows the channel's connections and allowed domains read-only, lets members add plugins, and lists the channel's routines; the tab-by-tab tour is in [Configure Claude for a channel(opens in new tab)](https://claude.com/docs/claude-tag/users/good-habits#configure-claude-for-a-channel).

If you set `Channel member edits` to `Block`, the whole page goes read-only for members, the `Respond automatically` switch included; a channel manager you've assigned can still edit the instructions and default model.

### Memory: who can see it, and how you review it[](#memory)

Claude Tag records memories as it works ([What Claude Tag remembers(opens in new tab)](https://claude.com/docs/claude-tag/users/memory) has the mechanics), and where a memory lands depends on the channel it was made in.

Memory files and transcripts are separate records: deleting a memory file doesn't delete transcripts, and changing a channel between public and private doesn't move what's already saved. Deleting stored data happens at the workspace or channel level (section 4).

Who can see a memory follows two rules:

1. **Public channels can add to the shared workspace memory:** a note Claude Tag saves there from one public channel is available when someone asks in another, by design. If that's not what a team wants, that work belongs in a private channel.
2. **A private channel reads the shared workspace memory but writes only to its own store:** nothing Claude Tag learns in a private channel leaks into the shared pool.

Direct messages and other workspaces stay separate in both cases.

From any scope's menu, an Owner can open `View memory files` to read, edit, or delete the store, and anyone in the channel can curate memory just by asking Claude Tag what it remembers (see [checking and correcting memory(opens in new tab)](https://claude.com/docs/claude-tag/users/memory#check-and-correct-what-claude-tag-remembers)).

## 6. Cost aligns with the work Claude Tag does[](#cost)

Channel work bills to your organization's usage balance, and a spend limit caps how much of that balance Claude Tag can draw each billing period. Direct messages are the one exception: a DM bills to that user's own seat, like the rest of their claude.ai usage.

### Where the limits live[](#usage-page)

The money lives on the Usage page, not on the Claude Tag settings page, and that is easy to miss. It holds:

* The organization-wide limit for the period
* The default limit for channels without their own
* One row per channel with its spend against its own limit or the default; a channel whose limit you've set to none shows `No spend limit` and no usage bar, because only the organization-wide limit applies there

Channel spend counts toward two limits at once, the organization-wide limit and each channel's own, and Claude Tag declines new work in a channel when either is reached.

Limits are enforced at list price and reset each billing period; for the fine print (negotiated discounts apply on your invoice, and promotional-credit usage shows here as $0.00, so read the List price column on the Analytics page instead), see [Set a spend limit(opens in new tab)](https://claude.com/docs/claude-tag/admins/set-spend-limit#set-the-spend-limit).

*The console shown is an illustration of a fictional company; all names and numbers are invented.*

**Varies by org:** if your organization bills through a reseller, funding and limits are handled through the reseller and the Usage page isn't available.

### What happens at a limit, and how spend is attributed[](#at-a-limit)

1. **Claude Tag declines work that would cross a limit:** it tells the requester in the thread. They can ask an admin for more, and the admin's notification says whether the balance or the limit caused the block. A separate throughput limit can also pause work; the reply names a short wait, and raising the spend limit doesn't clear it. See [rate limits versus the spend limit(opens in new tab)](https://claude.com/docs/claude-tag/admins/set-spend-limit#rate-limits-versus-the-spend-limit).
2. **Spend is shown per channel, not per user:** on an Enterprise plan you can also pull per-user rows from the Analytics API's cost report grouped by `claude_tag_user_id`; see [attributing costs to users(opens in new tab)](https://claude.com/docs/claude-tag/admins/attribute-costs) in the docs for how work maps to people. **Structure channels so each maps to a team**, and the per-channel breakdown reads as your per-team report, with per-channel limits acting as team budgets.

### Lowering spend in a high-volume channel[](#lower-spend)

A channel where Claude Tag follows every message uses more of the budget than a mention-only channel, because it starts more working sessions on its own (reading the channel itself isn't billed). Where volume is high and value is low, turning off `Respond automatically` is your first lever, before the limit.

## 7. Review what Claude Tag has done[](#audit)

The Activity page (under Claude Tag in Admin settings) is the organization-wide view of:

* Scheduled work
* Memory files
* An hourly export of the network calls Claude Tag made through Agent Proxy

The page opens for Owners, not the built-in Admin role. The docs' [Review what Claude Tag has done(opens in new tab)](https://claude.com/docs/claude-tag/admins/audit#what-the-audit-view-lists) page details each tab.

### Where each task is recorded[](#where-tasks-are-recorded)

The Activity page does not log every task and who asked for it. That record lives in four places:

1. **The Slack thread:** Claude Tag works in the open. The plan, progress, and the result are in the thread, visible to anyone in the channel. For a task that used a member's personal connectors, the thread has the result Claude posted, and the detailed work lives in a session only that member can open.
2. **The work itself:** posts come from the Claude app; commits and pull requests show the Claude GitHub App and link back to the Slack thread. Who can open a published artifact follows access to the source channel, with no share setting to change; see [artifact visibility(opens in new tab)](https://claude.com/docs/claude-tag/concepts/security-and-data#artifact-visibility) in the security and data handling docs.
3. **Each system's own log:** because you provisioned the service accounts, what Claude Tag does through a connection shows up in that tool's own audit log the same way any user's actions do, under the account your security team already watches. Work done with a member's personal connectors is recorded under that member's name instead.
4. **Your Claude organization's audit log** (admin changes, not tasks): read through the Compliance API, it records workspace disconnects, scope removals, and what channel managers change.

## 8. Rollout: widen in rings, each one earns the next[](#rollout-rings)

Nothing here is a big-bang install. The organization ceiling is set once; everything after is a channel at a time, at the pace teams pull it. Ring one is a single pilot channel your own admin team lives in; you'll notice every quirk because you're in the room. Ring two is one team with real work in their channel and their own instructions. Ring three is everyone who asks, and by then budgets and habits are boring, which is the goal.

**Day one:** complete this checklist in order.

1. **Pair the workspace and choose where Claude Tag may reply when tagged:** the `Entire workspace` or `Specific channel` choice from step 1 of setup.
2. **Connect GitHub and the other tools:** create Claude Tag's own account in each tool it will use.
3. **Fund usage and set limits:** buy usage credits during setup (organizations that don't see that step set the monthly limit at launch instead), launch, then set a limit on the pilot channel from the Usage page, plus the organization spend limit if you didn't set it at launch.
4. **Decide who may use Claude Tag at all:** the restriction toggle under Member access › `Manage`.
5. **Bind the pilot channel's access:** keep elevated credentials on private-channel scopes.
6. **Write the pilot channel's instructions on day one:** tone, scope, what routes to a human, what never to touch; and turn off `Respond automatically` if it should stay quiet unless tagged.
7. **Run one test task:** ask Claude Tag to file a ticket or create a draft document in a connected tool, and confirm the action appears in that tool's own audit log under Claude Tag's account.

**Watch the first week:** check the Usage page for spend by channel, the Activity page for what's scheduled, or just ask Claude Tag in the channel what it's been working on. Then stop watching. Widen to ring two only after all of the above is dull.

The Claude Tag docs' [after setup(opens in new tab)](https://claude.com/docs/claude-tag/admins/setup-overview#after-setup) guidance covers the same pattern in more depth, and [verifying your setup(opens in new tab)](https://claude.com/docs/claude-tag/admins/setup-overview#verify-your-setup) has the first-task checks.

## 9. FAQ[](#faq)

### Where do I see every channel Claude Tag is working in?[](#where-is-claude-live)

The access editor's left rail (section 4) is the roster: every channel Claude Tag has been added to appears there automatically, whether it has spent anything or not. Spend by channel and per-channel limits live on the Usage page, and the Analytics page shows spend by channel read-only, including promotional-credit usage that the Usage page reports as $0.00 (section 6 also has the reseller note).

### Can I make it mention-only across the whole organization?[](#mention-only)

Not organization-wide; the switch is per channel. **Turn off `Respond automatically`** on the channel scope's `Advanced` settings in Admin settings, on the channel's `Configure` page, or just by telling Claude Tag in the channel, and it holds for everyone there; see [controlling when Claude Tag responds(opens in new tab)](https://claude.com/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off). If you need a hard organization-wide boundary instead, use the enforced controls listed under "The hard boundaries" in section 5.

### Whose permissions does Claude Tag use?[](#whose-permissions)

Its own service accounts in channels; the asker's own claude.ai account in direct messages. Where Anthropic has enabled personal connectors in channels, the asker's own connectors can also serve their own request after they allow it, recorded under their name. Section 4 has the identity model.

### Can I block Claude Tag from a channel before someone invites it?[](#block-a-channel)

Yes: **a Blocked channel pattern** (the Advanced settings in section 4) keeps it out of matching channels even if someone invites it, and one channel's own `Enable Claude Tag in this channel` switch does the same for that channel. To confine it to chosen channels instead, see [limiting Claude Tag to specific channels(opens in new tab)](https://claude.com/docs/claude-tag/admins/restrict-access#limit-claude-tag-to-specific-channels) in the docs (on a Team plan, blocked channel patterns are the fence).

### Can I read or delete what it remembers?[](#read-or-delete-memory)

Yes. An Owner can open a scope's memory files from the scope's menu, and can edit or delete them. Anyone in a channel can also ask Claude Tag what it remembers and tell it to update or forget an entry.

### Can I cap spend per user, or bill back by user?[](#per-user-caps)

Caps, no: limits are per organization and per channel, and channel work bills to the organization balance. Bill-back, yes on Enterprise, through the Analytics API's cost report (section 6; the how is in [attributing costs to users(opens in new tab)](https://claude.com/docs/claude-tag/admins/attribute-costs)).

Not answered here? The full list of [controls that aren't available(opens in new tab)](https://claude.com/docs/claude-tag/admins/restrict-access#controls-that-aren%E2%80%99t-available) (third-party deployment, renaming the app, per-user caps, session-length enforcement, and more) is in the docs, alongside the [glossary(opens in new tab)](https://claude.com/docs/claude-tag/concepts/glossary).

For the authoritative reference on every step, see the [Claude Tag documentation(opens in new tab)](https://claude.com/docs/claude-tag/overview). For account and billing questions, the [Claude Help Center(opens in new tab)](https://support.claude.com) is the support channel.

* [1. Before you start](#before-you-start)
* [2. The map: five surfaces, three scopes](#the-map)
* [3. Get live: the setup flow, screen by screen](#get-live)
* [4. Access and identity](#access-and-identity)
* [5. What your members will do, and what you control](#when-it-responds)
* [6. Cost aligns with the work Claude Tag does](#cost)
* [7. Review what Claude Tag has done](#audit)
* [8. Rollout: widen in rings, each one earns the next](#rollout-rings)
* [9. FAQ](#faq)
