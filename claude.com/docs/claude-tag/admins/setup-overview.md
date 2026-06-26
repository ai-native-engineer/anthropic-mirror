<!-- source: https://claude.com/docs/claude-tag/admins/setup-overview -->

Claude Tag is Claude working in your team’s Slack channels, with its own accounts in your tools.
Open [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) and click **Set up** (or **+ Connect** if a workspace is already paired). If you started setup earlier without finishing, you’ll be asked to **Resume** or **Set up a new workspace**. A four-step setup dialog opens:

1. **[Set up Claude Tag for your workspace](#step-1-set-up-claude-tag-for-your-workspace)**: install the Slack app and link it with a pairing code
2. **[Give Claude Tag access](#step-2-give-claude-tag-access)**: name an [Access bundle](/docs/claude-tag/concepts/glossary#access-bundle) and connect your most-used apps
3. **[Set a spending limit](#step-3-set-a-spending-limit)**: cap monthly spend
4. **[Review and launch](#step-4-review-and-launch)**: turn on Claude Tag

The rest of this page covers [what to have ready before you start](#before-you-start), [each step in detail](#setup-steps), and [common setup issues](#common-setup-issues).

If your team already uses the earlier Claude in Slack, the same steps apply and your existing app stays; see [Migrate from the earlier app](/docs/claude-tag/admins/migrate-from-earlier) for what changes.

##  Before you start

| Prerequisite | Why you need it | If you don’t have it |
| --- | --- | --- |
| A **Team or Enterprise plan** on claude.ai | Claude Tag is available on Team and Enterprise plans, on Anthropic’s first-party service. It isn’t available on Pro or Free plans, or for third-party deployments. | Compare plans at [claude.com/pricing](https://claude.com/pricing) |
| A Claude organization **without Zero Data Retention (ZDR)** | Claude Tag stores channel memory and session transcripts, which ZDR doesn’t permit. | Claude Tag isn’t available to ZDR organizations |
| **Owner** role in your Claude organization | Pairing a workspace and creating Access bundles are Owner-only writes; an Admin can view settings but not complete setup. | Ask an Owner to run setup, or have one promote you at [`claude.ai/admin-settings/members`](https://claude.ai/admin-settings/members) |
| A **Slack workspace admin** | Running `@Claude connect` requires a Slack workspace admin; installing the app usually does too (most workspaces require admin approval for new apps) | If that’s someone else, [send them the install request](/docs/claude-tag/admins/pair-workspace#send-the-install-request-to-your-slack-admin) now so the pairing code is ready before you [pair your Slack workspace](#step-1-set-up-claude-tag-for-your-workspace) |
| **Usage credits** (Team plans) | Channel work draws from your organization’s usage balance; on a Team plan nothing runs until credits are loaded | Check whether your organization has a [launch usage credit](https://support.claude.com/en/articles/15575654-claude-tag-launch-promo-for-claude-team-and-enterprise) before buying; otherwise, buy credits at [`claude.ai/admin-settings/usage`](https://claude.ai/admin-settings/usage) |
| *(Optional)* A **channel to test in** | You’ll invite Claude to a channel to [test](#test-that-setup-worked) that setup worked | Create a private Slack channel for the pilot, or pick any existing one |

If any of your services restrict traffic by IP, file the [network requirements](/docs/claude-tag/admins/network-requirements) request with your network team early; in many organizations, IP allowlist changes take days to approve.

##  Setup steps

All four steps run in one dialog. Each section below shows what you’ll see and what to do.

###  Step 1: Set up Claude Tag for your workspace

A Slack workspace is your team’s space in Slack, at an address like `your-team.slack.com`; it contains all your channels. Pairing links one workspace to your Claude organization so `@Claude` can run in its channels and usage bills to your organization.
Step 1 shows three numbered substeps:

1

Install Claude for Slack

The **Install Claude for Slack** link opens the Slack Marketplace listing. Click **Add to Slack** there and approve the permissions.

2

Send `@Claude connect` in any channel

This message is shown with a copy button. In any channel of the workspace you just installed in, paste and send it. Claude replies with a pairing code valid for 15 minutes.Only a Slack workspace admin can run `@Claude connect`; anyone else gets a message naming who to ask. If that’s not you, [send them the install request](/docs/claude-tag/admins/pair-workspace#send-the-install-request-to-your-slack-admin) and have them return the code.

3

Paste the code Claude sends you

Paste the code into the input field (the placeholder reads `workspace_…`).

Under **Set up Claude Tag in**, choose **Whole workspace (Recommended)** or **Specific channel** (which asks for channel IDs). Click **Next**.
See [Pair your Slack workspace](/docs/claude-tag/admins/pair-workspace) for the Slack-admin handoff template, what to do if `@Claude connect` fails, and pairing on Enterprise Grid.

###  Step 2: Give Claude Tag access

An [Access bundle](/docs/claude-tag/concepts/glossary#access-bundle) is a named set of credentials, repository grants, plugins, and instructions that Claude uses on behalf of anyone in the channels it covers.

1

Name the bundle

**Access bundle name** is prefilled as **Slack default**; rename it if you want.

2

Connect your most-used apps

For each listed app you want Claude to reach, click **Connect** and enter a service-account credential (not a personal login). Use **Connect another app** at the bottom for a service that isn’t listed.

GitHub isn’t in this app list. It’s connected through the Claude GitHub App on a separate page after setup; see [Configure GitHub access](/docs/claude-tag/admins/configure-github).

You can skip connections here and add them afterward; without any, Claude can be invited to channels but can’t reach systems outside Slack. Click **Next**.
See [Give Claude access](/docs/claude-tag/admins/add-connections) for which services to connect first and how to create the service accounts, and the [per-service connection guides](/docs/claude-tag/admins/connections/overview) for credential fields per tool.

###  Step 3: Set a spending limit

Channel work draws from your organization’s usage balance, not from individual seats; the spend limit caps how much of that balance Claude in Slack can use each billing period. (DMs run on the user’s own claude.ai account and aren’t capped by this limit.)

1

Pick a preset or enter a custom amount

Choose from `$100`, `$250`, `$500`, `$1,000` (the default), **Unlimited**, or **Custom** (a US-dollar amount up to `$1,000,000`).

If your organization has no usage credits, this step shows **Buy usage credits** instead with a **Buy now** button; load credits, then continue. Click **Next**.
See [Set a spend limit](/docs/claude-tag/admins/set-spend-limit) for what counts toward the cap, per-channel limits, and what users see when it’s reached.

###  Step 4: Review and launch

1

Confirm and enable

Leave **Turn on Claude Tag** on.

2

Click Launch Claude

The dialog closes; Claude is now reachable in the workspace you paired.

##  Change a setting after setup

Everything you set during setup can be changed afterward on the [Claude Tag admin page](https://claude.ai/admin-settings/claude-tag).

| To change | Go to |
| Pair another workspace, or disconnect one | The Slack row’s **⋮** menu under **Where Claude Tag works**; see [Manage workspaces](/docs/claude-tag/admins/workspaces) |
| The Access bundle’s name, connections, repos, plugins, or instructions | **Access bundles** in the left navigation, or any scope’s panel on the **Slack** tab; see [Give Claude access](/docs/claude-tag/admins/add-connections) |
| The spending limit | [`claude.ai/admin-settings/usage/claude-in-slack`](https://claude.ai/admin-settings/usage/claude-in-slack); see [Set a spend limit](/docs/claude-tag/admins/set-spend-limit) |
| Whether Claude Tag is enabled at all | The **Enable Claude Tag for your organization** toggle at the top of the admin page |

##  Test that setup worked

In Slack, in your pilot channel, run `/invite @Claude` and then `@Claude summarize this channel`.
An *is thinking…* status under your message means the app is installed and listening. A reply means the workspace is paired and the channel is on the new version. This task doesn’t touch any connection, so it isolates pairing from credential issues.
See [Test your setup](/docs/claude-tag/admins/test-it) for a per-connection test that proves each credential works.

##  After setup

After your test passes, these guides cover what’s not part of initial setup:

| Guide | Do this when |
| [Give Claude access](/docs/claude-tag/admins/add-connections) | You skipped connections during setup, or a team needs another tool connected |
| [Configure per-channel access](/docs/claude-tag/admins/attach-to-scope) | One channel needs more (or different) access than the default. Keep elevated credentials in private-channel scopes; the org baseline stays minimal. |
| [Configure GitHub access](/docs/claude-tag/admins/configure-github) | A team will hand Claude code work: branches, pull requests, CI |
| [Restrict where Claude operates](/docs/claude-tag/admins/restrict-access) | Governance review: guest channels, member access, DM policy |
| [Customize](/docs/claude-tag/admins/customize) | Standing instructions, plugins, and what channel members can change |

There are two common ways to roll out from here:

| Pattern | What you do | What channel members experience |
| --- | --- | --- |
| Pilot first | One bundle on one workspace or channel; widen after validating | Claude appears in a few channels first, with capability growing as scopes are attached |
| Single bundle everywhere | One broad bundle at organization defaults | Every channel gets the same capability on day one. Fits orgs that already grant tools broadly. |

##  Common setup issues

| You expected | But got | Do this |
| --- | --- | --- |
| A pairing code from `@Claude connect` | “Only Slack workspace admins can link…” | The person who sent `@Claude connect` isn’t a Slack workspace admin. [Send the request](/docs/claude-tag/admins/pair-workspace#send-the-install-request-to-your-slack-admin) to someone who is. |
| A pairing code | “…installation is out of date” | Click the **reinstalls the Claude app** link in the reply, approve the Slack consent screen, then send `@Claude connect` again. See [why Manage apps doesn’t clear this](/docs/claude-tag/admins/pair-workspace#if-claude-connect-says-the-installation-is-out-of-date). |
| The Slack row under **Where Claude Tag works** to show your workspace as connected | It still shows **Not connected** | The code may have expired (codes last 15 minutes) or come from a different workspace. Send `@Claude connect` again for a fresh code. |
| A connected tool to work in your test | “I can’t reach…” | Connections only apply to **new** threads. Start a fresh thread before anything else. |
| The **Where Claude Tag works** section with a **+ Connect** button | Only the legacy Claude in Slack toggles | Your organization isn’t enabled for Claude Tag. Contact your account team. |

* [Network requirements](/docs/claude-tag/admins/network-requirements): what to allowlist before you start

[Glossary](/docs/claude-tag/concepts/glossary)[1. Pair your Slack workspace](/docs/claude-tag/admins/pair-workspace)
