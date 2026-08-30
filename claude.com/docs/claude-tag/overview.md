<!-- source: https://claude.com/docs/claude-tag/overview -->

Public Beta

Tag @Claude in. Get results back in the thread.

Anyone in a channel can tag Claude into a problem and hand it work: reproduce a bug and open a pull request, turn a decision thread into a doc, assemble the state of a project. It posts a checklist in the thread as it goes, and the whole exchange stays visible to the channel.

[I’m setting it up →](https://claude.com/docs/docs/claude-tag/admins/setup-overview)[Use it in your channel ↓](#put-claude-tag-to-work)

# platform-eng38 members

D

Dana2:14 PM

checkout has felt slow all morning — anyone else seeing it?

L

Leo2:15 PM

same. @Claude can you investigate? Compare latency against this morning’s deploy and find what’s causing it.

![](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/logo/clay-spark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=032101c39ca3b1af9f72fc4af8e60d12)

ClaudeAPP2:15 PM

On it. I’ll compare latency before and after the deploy, track down the cause, and report back here.

Done: Pulled p99 latency from DatadogDone: Diffed deploy 4f2c1 against mainDone: Reproduced the slow query locallyIn progress: Opening a pull request with the fix…

##  Plans that include Claude Tag

Claude Tag is available on Team and Enterprise plans, on Anthropic’s first-party service. It isn’t available on individual plans (Free, Pro, or Max), or for third-party deployments. To use it, your organization pairs its Slack workspace with its Claude organization; see [the setup overview](https://claude.com/docs/claude-tag/admins/setup-overview) for the full prerequisites.
If you’re choosing between Claude products for Slack-shaped work, [how Claude Tag differs from Cowork and Claude Code](https://claude.com/docs/claude-tag/concepts/how-it-works#how-claude-tag-differs-from-cowork-and-claude-code) compares them directly: team work in shared channels is Claude Tag; personal work on your own files is Cowork or Claude Code.

##  Where Claude Tag runs

Claude Tag works in Slack. You interact with it by writing in a Slack channel, thread, or direct message, and it replies there. Mention `@Claude` in a channel to guarantee it picks the message up.
When Claude works on a task, it runs in an ephemeral sandbox, not on your computer. The sandbox is created when a conversation starts, holds any code or files Claude is working with, and is discarded when the conversation goes idle. See [how Claude Tag works](https://claude.com/docs/claude-tag/concepts/how-it-works) for the full lifecycle.
You extend what Claude can reach, like your repositories, ticketing systems, data warehouses, and custom tools, through [connections](https://claude.com/docs/claude-tag/admins/add-connections), [plugins, and skills](https://claude.com/docs/claude-tag/admins/customize). An Owner configures these per scope (a channel, a workspace, or the whole organization), separately from any connectors an individual user has set up in their own claude.ai account.

[For administratorsSet up Claude Tag![](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/illustrations/Hand-Key.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=1b7a9675728f971bc7a4663c7f1ea599)](https://claude.com/docs/docs/claude-tag/admins/setup-overview)

[Where do I start?Pair your Slack workspace, connect the services Claude will work in, launch, and test that it works](https://claude.com/docs/docs/claude-tag/admins/setup-overview)[What can Claude Tag access?How admins set access per channel, and where credentials are stored](https://claude.com/docs/docs/claude-tag/concepts/agent-identity)[How do I connect each service?Credential types, allowed hosts, and what each connection lets Claude reach](https://claude.com/docs/docs/claude-tag/admins/add-connections)

[For end usersPut Claude Tag to work![](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/illustrations/Hand-NodePair.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=c64df4c6d27a6da752aa32c9e0622781)](#put-claude-tag-to-work)

[How do I hand Claude Tag a task?Mention Claude in any channel it’s in, with nothing to install](https://claude.com/docs/docs/claude-tag/users/getting-started)[What is Claude Tag good at?Use cases for coding, data, incidents, and go-to-market](https://claude.com/docs/docs/claude-tag/users/use-cases)[How do I get good results?Good habits for scoping and reviewing work](https://claude.com/docs/docs/claude-tag/users/good-habits)[What does Claude Tag remember?Channel memory, what’s shared across the workspace, and who can see what](https://claude.com/docs/docs/claude-tag/users/memory)[Can Claude Tag run tasks on a schedule?Scheduled jobs, channel watching, and triggers](https://claude.com/docs/docs/claude-tag/users/proactivity)

##  Billing and spend limits

Adding Claude to Slack doesn’t add a per-seat charge. Channel and thread work is billed by usage instead: it draws from a **usage balance**, an amount in your organization’s billing currency that an Owner funds. A [spend limit](https://claude.com/docs/claude-tag/admins/set-spend-limit) caps how much of that balance Claude Tag can use each billing period.
Direct messages don’t draw from this balance. A DM runs on the sender’s own claude.ai account and follows that seat’s usual usage limits, so the organization spend limit doesn’t apply to it.
To learn what your team’s usage costs, run a pilot with a spend limit set and watch the per-channel breakdown on the [usage page in your admin settings](https://claude.ai/admin-settings/usage/claude-tag). Your organization may already have a [launch usage credit](https://support.claude.com/en/articles/15575654-claude-tag-launch-promo-for-claude-team-and-enterprise) to run that pilot against before it funds the balance itself.
[Set a spend limit](https://claude.com/docs/claude-tag/admins/set-spend-limit) covers how to fund the balance on each plan, set the limit, and what happens when usage reaches it.

For end users

##  Put Claude Tag to work

If Claude Tag is in your channel, you can use it now. (If it isn’t there yet, an Owner in your Claude organization runs setup: see [Set up Claude Tag](https://claude.com/docs/claude-tag/admins/setup-overview).) Anyone in the channel can hand it work, and channel work bills to the organization, not to you.
What it can reach depends on the channel you’re in, not on who you are. The fastest way to find out is to ask it: `@Claude what can you access from this channel?` Or, if you’re signed in to your Claude organization, click **Configure** in the footer of a Claude reply in the channel to see its [connections](https://claude.com/docs/claude-tag/concepts/glossary#connection), the external services an admin has connected for that channel. Replies in org-shared channels have no Configure link.
The one exception is a DM, where it runs on your own claude.ai account instead of the channel’s setup. Owners can disable DMs organization-wide; see [Allow or disable direct messages](https://claude.com/docs/claude-tag/admins/restrict-access#allow-or-disable-direct-messages).

###  Common uses

The list below covers common ways teams use Claude Tag. Each link opens a guide with the prompts to paste and the connections the task needs.

* [Watch monitors and alerts](https://claude.com/docs/claude-tag/users/use-cases/watch-monitors): scheduled dashboard checks, and alerts investigated as they arrive. Needs a monitoring connection like Datadog, Sentry, or PagerDuty.
* [Triage requests](https://claude.com/docs/claude-tag/users/use-cases/triage-requests): an intake channel where Claude answers what it can, flags duplicates, and routes the rest. Works on Slack content alone.
* [Find answers in your docs](https://claude.com/docs/claude-tag/users/use-cases/find-answers): policy and runbook questions answered with the source. Needs a docs connection like Google Drive, Notion, or Confluence.
* [Answer data questions](https://claude.com/docs/claude-tag/users/use-cases/answer-data-questions): a plain-language question becomes a warehouse query and a chart. Needs a data warehouse connection.
* [Track projects and chase approvals](https://claude.com/docs/claude-tag/users/use-cases/track-projects): standing status digests and follow-ups that run until an approval lands
* [Turn threads into docs and tickets](https://claude.com/docs/claude-tag/users/use-cases/create-artifacts): a settled discussion becomes the decision doc, the customer reply, or the filed tickets
* [Fix bugs](https://claude.com/docs/claude-tag/users/use-cases/fix-bugs): a bug reported in the channel comes back as a draft pull request. Needs GitHub.
* [Work from your own channel](https://claude.com/docs/claude-tag/users/use-cases/your-own-channel): scratch questions, digests of channels you don’t follow, and follow-ups on what you said you’d do

[Get started](https://claude.com/docs/claude-tag/users/getting-started) covers your first message, what you see while Claude works, and how to shape Claude’s behavior in your channel.

For administrators

##  Set Claude Tag up once for everyone

You set up Claude Tag once, at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), and you must be an Owner in your Claude organization to do it. The setup page at that URL walks you through it:

* **Pair your Slack workspace**: send `@Claude connect` in Slack to get a pairing code, then enter it on the setup page.
* **Connect the services Claude will work in**: for each one, such as your issue tracker or data warehouse, create an account for Claude and enter its credential.
* **Grant repositories**: choose which repositories the Claude GitHub App can reach.
* **Set a monthly spend limit and launch**.

Claude Tag starts with no access to your external systems. The services you connect during setup form an [Access bundle](https://claude.com/docs/claude-tag/concepts/glossary#access-bundle), the set of tools Claude can reach, attached to the workspace or channels you paired. Once you launch, everyone in a channel Claude is in can use Claude Tag immediately, with no per-user setup.
[Set up Claude Tag](https://claude.com/docs/claude-tag/admins/setup-overview) walks through those steps with what to have ready, what each choice means, and how to verify Claude Tag works once you launch.

Security review

[Security and data handling](https://claude.com/docs/docs/claude-tag/concepts/security-and-data)

The security model, what admins can and can’t restrict, audit trails, and network requirements.

##  Where to start with Claude Tag

## Set up Claude Tag

Admins: pair your Slack workspace, connect the services Claude will work in, and launch

## Hand Claude Tag your first task

It’s already in your channel: send your first message

## How Claude Tag works

The session model, what it can read, and how memory follows places

## Use case library

Prompts to paste, by team and connection
