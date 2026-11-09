<!-- source: https://claude.dev/blog/building-effective-agent-automations/ -->

# Building effective agent automations

A reference implementation walkthrough with common failure modes

Lance Martin and CJ Avilla

Agents

Oct 08, 2026

9 min

Building effective agent automations

[└Get the code](#get-the-code)[└Overview](#overview)[└Sources](#sources)[└Destination](#destination)[└Agent](#agent)[└Schedule](#schedule)[└Memory](#memory)[└Guardrails](#guardrails)[└Getting started](#getting-started)

9 MIN READ

[X.com](https://twitter.com/intent/tweet?text=Building%20effective%20agent%20automations%20%2F%20claude.dev%20Blog&url=https%3A%2F%2Fclaude.dev%2Fblog%2Fbuilding-effective-agent-automations%2F)[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fclaude.dev%2Fblog%2Fbuilding-effective-agent-automations%2F)[Email](mailto:?subject=Building%20effective%20agent%20automations%20%2F%20claude.dev%20Blog&body=https%3A%2F%2Fclaude.dev%2Fblog%2Fbuilding-effective-agent-automations%2F)Copy URL[Copy markdown](https://claude.dev/blog/building-effective-agent-automations.md)

As AI accelerates our work, it's getting harder to keep up. At Anthropic, [simple agent automations](https://claude.com/resources/articles/how-an-anthropic-japan-business-development-representative-runs-his-day) are frequently used to help. They often [run on a schedule](https://claude.com/resources/articles/whats-new-in-claude-managed-agents), gather context in the background, and proactively tell us what we need to know. But it’s difficult to build effective agent automations: they can lose access to a source without anyone noticing or fail to follow our preferences.

Using [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) (beta), we built a reference implementation that reads custom sources (e.g., Slack and GitHub repos) on a schedule, tracks what changed since the last run, and posts what you need to know (e.g., to Slack). In this article, we walk through each step, share a reference implementation, and provide a command to run in [Claude Code](https://claude.com/product/claude-code) that configures the agent for you.

## GET THE CODE

The reference implementation is [here](https://github.com/anthropics/claude-quickstarts/tree/main/managed-agents/daily-brief). For an interactive walkthrough, run the command below in Claude Code. The `claude-api` skill can help set up the agent following the guidance in this article:

PROMPTCopy

```
/claude-api managed-agents-onboard https://claude.dev/blog/building-effective-agent-automations/
```

For this reference implementation, you need a Slack app ([create it from the manifest](https://api.slack.com/apps?new_app=1&manifest_yaml=display_information%3A%0A%20%20name%3A%20Daily%20brief%0A%20%20description%3A%20Posts%20one%20short%20brief%20each%20weekday%20morning.%0Afeatures%3A%0A%20%20bot_user%3A%0A%20%20%20%20display_name%3A%20Daily%20brief%0A%20%20%20%20always_online%3A%20false%0A%20%20app_home%3A%0A%20%20%20%20home_tab_enabled%3A%20false%0A%20%20%20%20messages_tab_enabled%3A%20true%0A%20%20%20%20messages_tab_read_only_enabled%3A%20true%0Aoauth_config%3A%0A%20%20scopes%3A%0A%20%20%20%20bot%3A%0A%20%20%20%20%20%20-%20channels%3Ahistory%0A%20%20%20%20%20%20-%20chat%3Awrite%0Asettings%3A%0A%20%20org_deploy_enabled%3A%20false%0A%20%20socket_mode_enabled%3A%20false%0A%20%20token_rotation_enabled%3A%20false%0A)) and a [GitHub token](https://github.com/settings/personal-access-tokens/new). The provided files (shown below) are configuration for Claude API resources, including the agent, its environment, memory stores, vault, and deployment.

CODETextCopy

```
daily-brief/
├── agent.md                        model, tools, instructions
├── deployment.md                   schedule, time zone, budget, input message
├── environment.yaml                network allowlist
├── memory_store_preferences.yaml   user preferences
├── memory_store_state.yaml         the agent's bookmarks, ledger, notes, and run records
├── vault.yaml                      the vault that holds the credentials
├── claude-lock.json                resource IDs, written by ant apply
└── slack/manifest.yaml             one bot app
```

[`ant apply`](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/apply), a command in the ant CLI, reads these files, creates the resources in your Claude API workspace (where the platform stores and runs them), and records the IDs in `claude-lock.json`.

We'll use this command in the sections below. Once configured, the automation runs on a schedule on Anthropic's infrastructure, so [nothing has to stay running on your machine](https://claude.dev/blog/claude-code-in-the-cloud/).

## OVERVIEW

The agent we’ll build has six components, covered in this order:

* Sources - A named list of places to read
* Destination - One place the agent may write
* Agent - The model, tools, and run steps in agent.md
* Schedule - A cron schedule
* Memory - Your preferences and the agent's own memory
* Guardrails - Read-only access wherever the agent only reads, and a spending cap per run

![Architecture of the agent: a schedule wakes the agent, which reads from its sources and posts a brief to one destination for the reader. Memory holds the agent's state and the reader's preferences, and guardrails surround the agent.](https://claude.dev/media/fdbe45db5e3ce9afbb00bf62f87e64078a683800bc492d4ac6cf716a2d313a00.png)

## SOURCES

The agent reads two default sources: Slack channels and GitHub pull requests. The channels and repos are listed in your `preferences` file. The template can be extended to use other sources.

![The architecture diagram with Sources highlighted. The sources are read-only, reached through MCP or HTTPS with credentials from a vault, and feed the agent.](https://claude.dev/media/d8508de61bb90f3bfccf6184dd3d7cbe9c65e2e76bd00477efd1620e3910dae7.png)

### Give the agent its own, scoped credentials

With [Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview), credentials live in [vaults](https://platform.claude.com/docs/en/managed-agents/vaults). The agent can reference these credentials but the real values stay in the vault, [outside the sandbox](https://claude.com/resources/articles/giving-companies-more-control-over-their-ai-agents-with-nvidia) where Claude's code runs (see [here](https://www.anthropic.com/engineering/managed-agents) and [here](https://x.com/katelyn_lesse/status/2099315903884415400)):

* **MCP servers (GitHub).** The agent calls MCP tools through a proxy that runs outside the sandbox. The proxy finds the vault credential whose URL matches the server’s.
* **The shell (Slack).** The agent calls the Slack API with curl using the bash tool inside the sandbox. The sandbox only holds an opaque placeholder, `$SLACK_BOT_TOKEN`. As the request leaves the sandbox, the platform swaps in the real token for hosts you allow.

Create the vault using the `ant` CLI and the template file in the repo:

CODEShellCopy

```
ant apply vault.yaml
```

This creates the vault in your Claude API workspace, where the platform stores it, and records its ID in `claude-lock.json`. Then add each credential to the vault with the [TypeScript SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/typescript). Here is an example showing addition of the Slack credential:

CODETypeScriptCopy

```
const vaultId = process.env.VAULT_ID!; // the vault's ID, from claude-lock.json

await client.beta.vaults.credentials.create(vaultId, {
  display_name: "SLACK_BOT_TOKEN",
  auth: {
    type: "environment_variable",
    secret_name: "SLACK_BOT_TOKEN",
    secret_value: process.env.SLACK_BOT_TOKEN!,
    networking: { type: "limited", allowed_hosts: ["slack.com"] },
    injection_location: { header: true },
  },
});
```

After creating the vault and adding each credential, attach the vault to the deployment. Copy the vault ID from `claude-lock.json` into `vault_ids` in the deployment file, `deployment.md`.

### Read from where you left off

A common mistake is asking the agent to read a fixed window like "*the last 24 hours*." A late run leaves a gap and an early run repeats items. Instead, give the agent a bookmark per source. At the end of each run, the agent writes the timestamp of the newest item it read from each source to one file, `bookmarks.json`, with an entry per source: `"slack": "2026-09-14T13:02:11Z"`.

The next run starts from those bookmarks, so its window stretches or shrinks to cover everything since the last run. The bookmarks live in the [memory store](https://platform.claude.com/docs/en/managed-agents/memory) called `state`: a folder of text files that the platform mounts into every run's sandbox under `/mnt/memory/` and keeps between runs. The agent reads and writes it with its ordinary file tools, and the instructions in `agent.md` tell it how.

### Don't mistake a failed read for a quiet day

If an MCP server is down or its token has expired, the run still starts, just without that server's tools. The [session logs an error](https://claude.com/resources/articles/agent-observability-on-the-claude-platform), but the agent sees nothing from that source and reports "nothing new."

Three rules in `agent.md` help fix this. When a source fails, the agent will: keep the source’s bookmark where it is, write the brief from the other sources, and end the brief with one line naming what it couldn't read ("pull requests unavailable this run"), so the reader is made aware.

## DESTINATION

Our template posts to one Slack channel, with a dated post each time it runs.

![The architecture diagram with Destination highlighted. After a check that today's brief isn't already posted, the agent posts to one destination, which delivers the brief to the reader.](https://claude.dev/media/15481dc4dff01b4a613e8ff36039bc14036ab97781eddeaf749746533b97bd16.png)

The agent posts to Slack using the bash tool in its sandbox, using the same bot token it reads with.

Nothing has to approve the post. The agent sends it with a bash command, and the built-in bash tool runs without asking for approval by default. `slack.com` is also on the allowlist of the agent's [environment](https://platform.claude.com/docs/en/managed-agents/environments), the sandbox it runs in. The post is one request:

CODEShellCopy

```
curl -s https://slack.com/api/chat.postMessage \
  -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{"channel": "C0123456789", "text": "Daily brief, Tue Sep 15 ..."}'
```

### Confirm the post landed before recording it

Once a post is confirmed, the agent updates its ledger of reported items and its bookmarks. If those records don't match what was actually posted, two things can go wrong. If the agent records a post that never landed, the bookmarks move on and those items are never reported. If it posts again because it isn't sure the first post landed, readers get the same brief twice.

Three rules in `agent.md` prevent this. First, the agent looks for today's title in the channel's recent messages and doesn't post if the edition is already there. Second, the post counts as sent only if Slack returns `"ok": true` and a message ts. Third, the agent updates the ledger and bookmarks only after that confirmation. If the result is unclear, it marks the run "maybe posted" and changes nothing else, so nothing is lost.

The agent keeps a run record in its memory store (`runs/<date>.md`). It marks the run "posting" before the post, then "posted" with the message ID, or "maybe posted."

## AGENT

In Claude Managed Agents, an [agent](https://platform.claude.com/docs/en/managed-agents/agent-setup) is a versioned configuration: a model, a system prompt, and tools. Each run follows its run steps and stops.

![The architecture diagram with the Agent highlighted: a model plus a prompt that holds the run loop and the judgement rules.](https://claude.dev/media/8b00d803c6eee8a1c6419c15961f688cba2f6fbff5031e1bd0539725cba1780b.png)

In our reference implementation, the agent configuration is `agent.md`:

CODEMarkdownCopy

```
---
name: Daily brief
model: claude-sonnet-5-5
mcp_servers:
  - type: url
    name: github
    url: https://api.githubcopilot.com/mcp/
tools:
  - type: agent_toolset_20260401
    configs:
      - name: web_search
        enabled: false
      - name: web_fetch
        enabled: false
  - type: mcp_toolset
    mcp_server_name: github
    default_config:
      permission_policy:
        type: always_allow
---

[Eight numbered run steps; the full text is in agent.md in the repo.]
```

The frontmatter supplies the agent name, model, tools, and MCP servers. The body provides the agent instructions. MCP tools ask for approval by default and nobody is there to give it, so the GitHub toolset is set to `always_allow` and the GitHub token is `read-only`.

### Keep the brief short

`agent.md` steers Claude toward brevity:

CODETextCopy

```
4. Decide. An item earns a line when the reader would act on it today, or it changes a decision they are about to make. When unsure, leave it out. Most days that is a few items, sometimes none. A count ("12 open reviews") is not an item; link the ones that are blocked. An item already in the ledger and still open is carried as one marked line ("still waiting, day 3"), not re-reported; a closed item is dropped without comment. Do not bring back a topic the preferences file has retired.
```

### Re-check anything still open right before posting

Items can change between when the agent reads sources and when it posts. Just before posting, `agent.md` instructs the agent to re-check the live status of each item:

CODETextCopy

```
5. Verify. The world moved while you read. For every item you will report, re-check its live source just before posting: resolved since you read it, drop it; still open but changed, fix the line; cannot confirm, drop it and list it in the run record's cuts. One stale "still waiting on you" costs more trust than ten missing items, so never hedge an item's status: assert it or drop it. Every link is copied from the source's own link field (a pull request's html_url, a Slack permalink), never assembled by hand.
```

## SCHEDULE

With [Claude Managed Agents](https://claude.com/platform/claude-managed-agents), the agent is only a configuration file; a [deployment](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments) runs it. The deployment names the agent, environment, and the first message of each run. It also holds the schedule, vault, memory stores, and budget. Each time the schedule fires, the platform starts a fresh agent [session](https://platform.claude.com/docs/en/managed-agents/sessions).

![The architecture diagram with Schedule highlighted: a scheduled deployment that wakes the agent for each run.](https://claude.dev/media/a206f78f34b18dcf7a51bc9bca1acaaf3b68df80ee4034ff521cfbf353af7bc5.png)

In our template, the deployment is captured in `deployment.md`, with the first message as its body:

CODEMarkdownCopy

```
---
name: Daily brief
agent: ./agent.md
environment_id: ./environment.yaml
schedule:
  type: cron
  expression: "32 7 * * 1-5"
  timezone: America/New_York
vault_ids: [vlt_...]   # the vault you create under Sources
resources:
  - path: ./memory_store_preferences.yaml
    access: read_only
    instructions: The reader's preferences. Re-read them every run. Never write here.
  - path: ./memory_store_state.yaml
    access: read_write
    instructions: Your state. Bookmarks, ledger, notes, proposals, and run records.

---

Write today's brief.
The reader's time zone is America/New_York. Work out every date in that zone.

Follow your run steps in order. Today's edition is titled "Daily brief, <weekday> <month> <day>".
```

This creates the deployment with the agent, environment and memory stores it names by path.

CODEShellCopy

```
ant apply deployment.md
```

To test it without waiting for the schedule, start a run by hand with `ant beta:deployments run --deployment-id <id>`, using the ID from `claude-lock.json`.

### Compute dates in your time zone

A common bug is the agent calling this morning "yesterday" because it computes dates in the server's time zone. In `deployment.md`, the `timezone` field sets when the run fires and the second line of the body tells the agent which zone to use for dates.

## MEMORY

Each run starts in a fresh sandbox with no memory of the last one. Without memory, feedback doesn't stick. However, stale memory can confuse the agent: it reports an item as still waiting after it was resolved, or drops one that's still open because it was "already reported."

![The architecture diagram with Memory highlighted. State is what the agent reads and writes, and Preferences is what the reader writes and the agent only reads.](https://claude.dev/media/30e51eab0381bb583fe355fe412162b4e8868643b8d58b2c76c4aa2d0eafea57.png)

Our template keeps two [memory stores](https://platform.claude.com/docs/en/managed-agents/memory), the folders mounted under /mnt/memory/ (see Sources):

* **preferences** (yours, read-only to the agent): which channels and repos to read, what to leave out, the length cap, the destination, and when to stop.
* **state** (the agent's, read-write): the bookmarks, a ledger of what it reported, one record per run, changes it proposes to your preferences, and notes on how each source behaves ("returns only the newest 50 items").

`ant apply deployment.md` creates the preferences store, but not the file in it. Before the first run, write your preferences.md there with the repo's `scripts/seed-preferences.sh`.

### Re-read your preferences at the start of every run

A common problem occurs when a copy of the preferences is baked into the prompt, which keeps applying rules you've already changed. Have the agent read the file fresh every run. If it can't read the file, it should stop and say so instead of running on defaults.

### Keep a ledger of what you've already reported, and report the change

The agent keeps a ledger, `ledger.md`, of every item it has reported, so the brief doesn't repeat itself. Each line records when the item was reported, where it came from, an ID that doesn't change (a Slack message timestamp or a pull request number), and its last known status:

CODETextCopy

```
2026-09-09 slack:C0123456789 1788963600.000100 refund thread: customer waiting on a decision
2026-09-11 github 481 review blocked, day 2 (still waiting)
2026-09-11 slack:C0234567891 1789117333.000300 enterprise escalation: owner named, in progress
```

## GUARDRAILS

Because our automation runs in the “background” on a schedule, we set limits on what the agent can do and what it can spend.

![The architecture diagram with Guardrails highlighted: a boundary around the agent with caps on turns, time and spend, and a heartbeat that someone watches.](https://claude.dev/media/746533f20f4e2bf093d08a04f368a8c5eca739de6579c384e9742b86d5385f50.png)

### Limits on what it can do

The agent reads messages and issues that other people wrote, and that text can be interpreted as instructions. Limit what the agent could do if it followed them. In our example, the GitHub token and the `preferences` store are read-only, and the environment only reaches the hosts on its allowlist. A planted instruction can still change what the brief says, including through the notes the agent keeps between runs. It can't write to GitHub or edit your rules.

Slack is the exception: the same token posts, so invite the bot only where it needs to read or post.

### Set the spending cap from real runs

A spending cap protects you from runaway costs. Start at three to five times the cost of a normal run, then tighten it as you see real numbers. A run that hits its cap pauses instead of failing, so a cap set too low looks like a brief that went quiet. The cap is the [`budget`](https://platform.claude.com/docs/en/managed-agents/budgets) in `deployment.md`. Every run gets the full amount, and a run that reaches it pauses with a `budget_reached` stop reason:

CODEYAMLCopy

```
budget:
  type: limit
  max_list_cost:
    amount: "500" # a string, in cents: "500" is $5.00
    currency: USD
```

## GETTING STARTED

Our reference implementation comes down to six rules:

* Read each source from a bookmark, not a fixed time window.
* Report a failed read as unreadable, never as a quiet day.
* Re-check every item right before posting.
* Count a post as sent only when Slack confirms it, then update bookmarks and ledger.
* Re-read your preferences every run, from a store the agent can't edit.
* Give the agent read-only access wherever it only reads, and cap what each run can spend.

Claude Code can walk you through the guidance provided in this article. First, update:

CODEShellCopy

```
claude update
```

Then, use the claude-api skill:

PROMPTCopy

```
/claude-api managed-agents-onboard https://claude.dev/blog/building-effective-agent-automations/
```

The claude-api skill reads this post, proposes a setup, writes the files to an agents/ folder in your project, and creates the resources with ant apply. Treat this as a starting point, and customize the agent for your sources, destination, or memory preferences.

[Oct 15, 2026How the Claude Code team does code review14 min](https://claude.dev/blog/solving-code-review-at-anthropic/)[Oct 06, 2026Claude Code in the cloud: a field guide to cloud sessions18 min](https://claude.dev/blog/claude-code-in-the-cloud/)[Oct 01, 2026Getting started with Claude Code mods11 min](https://claude.dev/blog/getting-started-with-claude-code-mods/)[Sep 28, 2026Automating eval design and hillclimbing with Claude12 min](https://claude.dev/blog/automating-eval-design-and-hillclimbing/)[Sep 28, 2026Building with Claude Sonnet 5.59 min](https://claude.dev/blog/building-with-claude-sonnet-5-5/)
