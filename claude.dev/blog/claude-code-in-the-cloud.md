<!-- source: https://claude.dev/blog/claude-code-in-the-cloud/ -->

# Claude Code in the cloud: a field guide to cloud sessions

What changes when Claude Code runs on its own machine, the workflows where that pays off, and how to connect GitHub on the first try.

Addy Osmani

Oct 06, 2026

18 min

Claude Code in the cloud: a field guide to cloud sessions

[└Three tasks, one repository, three machines](#three-tasks-one-repository-three-machines)[└Under the hood of a Claude Code cloud session](#under-the-hood-of-a-claude-code-cloud-session)[└Local or cloud?](#local-or-cloud)[└Seven workflows that suit cloud sessions](#seven-workflows-that-suit-cloud-sessions)[└Connecting GitHub without getting stuck](#connecting-github-without-getting-stuck)[└Give sessions what they need to check their own work](#give-sessions-what-they-need-to-check-their-own-work)[└Habits that pay off](#habits-that-pay-off)[└Common questions](#common-questions)[└Start in five minutes](#start-in-five-minutes)

[X.com](https://twitter.com/intent/tweet?text=Claude%20Code%20in%20the%20cloud%3A%20a%20field%20guide%20to%20cloud%20sessions%20%2F%20claude.dev%20Blog&url=https%3A%2F%2Fclaude.dev%2Fblog%2Fclaude-code-in-the-cloud%2F)[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fclaude.dev%2Fblog%2Fclaude-code-in-the-cloud%2F)[Email](mailto:?subject=Claude%20Code%20in%20the%20cloud%3A%20a%20field%20guide%20to%20cloud%20sessions%20%2F%20claude.dev%20Blog&body=https%3A%2F%2Fclaude.dev%2Fblog%2Fclaude-code-in-the-cloud%2F)Copy URL[Copy markdown](https://claude.dev/blog/claude-code-in-the-cloud.md)

You probably run Claude Code in a terminal on your own laptop. That session depends on the laptop in three ways:

* It shares your working tree, so two sessions on one repository can edit the same files and fight over the same port.
* It runs with your credentials.
* It stops when your computer sleeps or the Wi-Fi drops.

[A cloud session](https://code.claude.com/docs/en/claude-code-on-the-web) runs Claude Code on a machine of its own. Each task gets a fresh virtual machine with your repository cloned onto a new branch and your environment's setup already done.

You can start one from [claude.ai/code](https://code.claude.com/docs/en/web-quickstart), the [Claude mobile app](https://code.claude.com/docs/en/mobile), the [Desktop app](https://code.claude.com/docs/en/desktop#run-long-running-tasks-in-the-cloud), your [terminal](https://code.claude.com/docs/en/claude-code-on-the-web#from-terminal-to-cloud), and [Slack](https://code.claude.com/docs/en/slack). You can then follow it from the browser, the mobile app, and Desktop. When the work is done, it sits on a branch you can turn into a pull request.

Cloud sessions come with your Pro, Max, Team, or Enterprise plan at no additional cost: there's no separate charge for the cloud machine, and sessions draw on the same usage limits as the rest of Claude Code. Depending on your plan, an organization owner may need to [turn on cloud sessions](https://claude.ai/admin-settings/claude-code) first.

**Bonus credit for cloud sessions.** Existing individual Pro and Max subscribers can claim a one-time bonus credit for cloud sessions, on top of their plan limits: $100 on Pro and $250 on Max. Claim it by October 7 at claude.ai/code/claim-credit or with `/claim-credit` in Claude Code. The credit expires on November 4. After it's used or expires, your plan's regular usage applies. It isn't eligible for Projects or Routines. See the [Promotional Credit Offer Terms](https://www.anthropic.com/legal/promotion-credit-terms).

For this guide I ran four real cloud sessions against a small sample repository. Their transcripts, diffs, and timings appear throughout. The repository and the user in the screenshots are made up. The work, the output, and the numbers come from those sessions.

One of the main advantages of cloud sessions is that you can run several tasks at once without them getting in each other's way. Here are three I started within 16 seconds of each other, each on its own machine. On my laptop, I'd have run these one after another, or spent my time keeping them out of each other's way.

[![](https://claude.dev/media/58bd02532f8c5914f4dc430c84caddcb4158c4dc7b2905bcf602c9cb439ab5e2.png)](/media/84f43e2c4f4d1dce037e0807473d5bc41652ecd6a8dbffa5a835407a9bcc180f.mp4)![Timeline of three cloud sessions in three VMs, started within 16 seconds of each other. After a hatched setup bar, the flaky-test fix finishes at 65 seconds with the suite run 40 times and 0 failures, the docs rewrite at 62 seconds with 5 doc errors fixed, and the structured-logging change at 87 seconds with JSON logs and 5 new tests.](https://claude.dev/media/58bd02532f8c5914f4dc430c84caddcb4158c4dc7b2905bcf602c9cb439ab5e2.png)Play video

**FIG A**PauseThe real timeline of three cloud sessions on one repository, in seconds from the first start. Hatched bars are the setup step that recreated the sample repository (a GitHub clone replaces it in normal use), and each dot is one tool call.

## THREE TASKS, ONE REPOSITORY, THREE MACHINES

The sample repository is **tidepool**, a small Node API that predicts tides for three fictional harbors. It had three ordinary problems: one test failed about one run in four, the API docs described parameters the code no longer read, and the logger built its lines by concatenating strings.

I started three cloud sessions within 16 seconds of each other, one per problem. I started them programmatically, and because tidepool isn't on GitHub, each session first recreated the repository from files in its prompt. With a real repository you'd skip that step, and from a terminal each session is one `claude --cloud` command. Shortened, the three prompts were:

CODEShellCopy

```
claude --cloud "npm test fails maybe one run in four. Find the flaky test, fix the root cause in the code (not the test), and prove it by running the suite at least 30 times in a row."
claude --cloud "docs/API.md is out of date with src/server.js. Rewrite it so every endpoint, parameter, default and response shape matches the code. Start the server and run each curl example to check it."
claude --cloud "Make src/logger.js emit one JSON object per line, keep LOG_LEVEL, and log method, path, status and duration_ms as fields. Add a test for the logger."
```

The sessions ran for 61, 65 and 72 seconds, and all three were done 87 seconds after the first one started. Recreating the repository took roughly a third to just over half of each run. Here are the results.

* **The flaky test.** Claude found a race in `TtlCache.get`. The cache stored a value only after the loader finished, so a second `get` for the same key during a load called the loader again. Claude changed the cache to store the in-flight promise, dropped the entry when a load fails, and ran `npm test` 40 times in a row with zero failures.
* **The docs.** Claude started the server, ran a curl against every endpoint, and found five ways the old doc was wrong. It listed fields the API never returns, documented a `days` parameter the code ignores, gave heights in feet when they are metres, skipped the `/next-high` endpoint, and left out the error responses. It also found that a malformed `from=` value returns an empty list with a 200, and documented that as a caveat instead of changing server code it wasn't asked to touch.
* **The logger.** Claude wrote the JSON logger, moved the request log to structured fields, and added five tests. Its commit went in with one failing test, so Claude reran the cache test eight times, saw it fail in five of them, and traced the failure to the same race the first session was fixing. It proposed the same fix, left the cache alone because that was outside its task, and said in its summary that the suite wasn't clean.

![claude.ai/code showing the Structured logging session: an expanded diff of src/server.js replacing a string-built request log with logger.info('request', { method, path, status, duration_ms }), and a branch bar for claude/structured-logging with a Create PR button.](https://claude.dev/media/6dfaea2721b24b4bcaeb1ecd1888d0b592776c363e69f8563a1db7ea97413659.png)

**FIG B**The three sessions in the claude.ai/code interface, running locally and replaying their real transcripts. Setup steps are trimmed, paths show under /home/user, the bottom three sidebar titles are filler, and the mode chip shows the default.

![The Fix the flaky test session: the command that patched cache.js and ran the test suite 40 times, its output runs=40 fails=0, and Claude's explanation of the race in TtlCache.get.](https://claude.dev/media/caa714fdd2f78736773e380b98b2491123ef497120b00760b9bef931c21a29c0.png)

**FIG C**The Fix the flaky test session

![The Update the tidepool API docs session: Claude's summary of the five ways the old docs/API.md was wrong.](https://claude.dev/media/a195ee38cd704981526163e2824c10fc9ba813b2dce9045ce2d6ab8651159a70.png)

**FIG D**The Update the tidepool API docs session

[![](https://claude.dev/media/6bb12b4794b3722a932f313ae46a5da915be2159a9d250d4dc3837957b158e52.png)](/media/f821b611fd96e1d6e5ef41e731d1c13a0b9d2fd5fa09d2e0c593f9d38a1a5095.mp4)

**FIG E**A 20-second recording of the same local build: clicking between the three sessions, then scrolling the logger session's transcript

The logger result shows why cloud sessions suit parallel work. Each session had its own copy of the repository, its own processes and its own branch. The docs session and the logger session each started the API server to test against it, and neither affected the other. On a single laptop, two agents working in one checkout would edit the same files, and would collide on a port unless each picked its own.

Because of that isolation, the logger session had no access to the cache fix the first session was making. Split parallel tasks along file boundaries, merge the branches in a sensible order, and expect a session to report problems that another session is already fixing.

## UNDER THE HOOD OF A CLAUDE CODE CLOUD SESSION

A cloud session is a Claude Code session running on Anthropic-managed infrastructure, or on your organization's own machines with a [self-hosted environment](https://code.claude.com/docs/en/self-hosted-environments). The figure shows the parts. The four takeaways after it are the ones that change how you work.

![You start a session from a browser, phone, Desktop, terminal, Slack or a routine. It runs in a fresh VM with a clone of your repository on a claude branch, Claude Code in auto mode, and your environment's setup. GitHub traffic passes through a proxy that holds your token outside the VM; other traffic passes through a security proxy that applies the network allowlist. The result is a branch and a pull request.](https://claude.dev/media/7c0f2a65796202281cbc6ededff3f0dbfe216aca98e3831640eec064e2b85165.png)

**FIG F**Anatomy of a cloud session. Everything the agent can touch sits inside the VM. Your GitHub token and the network policy sit outside it.

* **Every task gets its own machine.** A fresh VM with your repository cloned onto a new branch, so sessions can't touch each other's files or ports. See [what's installed](https://code.claude.com/docs/en/cloud-environments#installed-tools).
* **Your GitHub token never enters the VM.** A proxy holds it, and the session gets a short-lived credential that can push only to its own working branch. See the [GitHub proxy](https://code.claude.com/docs/en/cloud-environments#github-proxy).
* **The repository's Claude config comes along. Your personal one doesn't.** `CLAUDE.md`, rules, skills, agents, and commands travel with the repo, and your `~/.claude` stays on your laptop. See [settings in cloud sessions](https://code.claude.com/docs/en/settings#settings-in-cloud-sessions).
* **Idle VMs get reclaimed.** Reopen the session and you get a fresh VM with the conversation restored, so commit work you care about. See [environment expiry](https://code.claude.com/docs/en/claude-code-on-the-web#environment-expired).

For specs, [permission modes](https://code.claude.com/docs/en/permission-modes), and network levels, see the [cloud environments docs](https://code.claude.com/docs/en/cloud-environments).

## LOCAL OR CLOUD?

Cloud sessions don't replace local ones, and most people use both. The table shows where they differ, and the paragraphs after it say when each one fits.

|  | Local session | Cloud session |
| --- | --- | --- |
| Runs on | Your machine | A fresh VM for each task |
| Laptop asleep or offline | The session stops | The session keeps going |
| Several tasks on one repo | Separate worktrees, ports and care | One VM and one branch per task |
| What the agent can reach | Anything your user account can, including SSH keys, cloud CLIs and `~/.claude` | The repository, the network level you set, the connectors you enable, and a session-scoped GitHub credential |
| Start or follow from | That machine, or your phone through remote control | Browser, phone, Desktop, terminal, Slack, an API call or a schedule |
| Approvals | Any mode, including per-command | Auto, Accept edits or Plan |
| Ends with | Changes in your working tree | A branch, and a pull request when you want one |
| Compute | Your machine | No separate compute charge; uses your plan's limits |

Stay local when the task needs something only your machine has. That covers a database with real local data, a service you reach over VPN, a GPU, a phone simulator, or hardware on your desk. Stay local too for tight visual loops where you want to see each change in your own browser within seconds, and when your organization runs with [Zero Data Retention](https://code.claude.com/docs/en/zero-data-retention), which turns cloud sessions off.

Two features sit between the options. **Remote control** keeps the session on your machine and lets you steer it from your phone or browser. **[Self-hosted environments](https://code.claude.com/docs/en/self-hosted-environments)**, in beta for Team and Enterprise, run cloud sessions on your organization's own infrastructure, so they can reach private networks.

If none of that applies, the task is a good candidate for the cloud. The next section covers the workflows where that pays off most.

## SEVEN WORKFLOWS THAT SUIT CLOUD SESSIONS

These workflows put the differences in the table to work: a separate machine for each task, sessions that keep running while you're away, and a branch at the end for you to review.

### 1. Clear a backlog in parallel

Let's say you have five small, unrelated fixes. Locally, you'd do them one after another, or set up five worktrees and keep their ports and installs apart. In the cloud, you'd start five sessions and review five branches.

CODEShellCopy

```
claude --cloud "Fix the flaky test in auth.spec.ts"
claude --cloud "Update the API documentation"
claude --cloud "Refactor the logger to use structured output"
```

`claude --cloud` clones your GitHub remote at your current branch, so push your local commits first. While the VM starts, the CLI shows a live checklist of setup steps and queues anything you type.

Write each task as a self-contained ticket that states what's wrong, what done looks like, and how to prove it. The flaky-test prompt named its proof: running the suite at least 30 times in a row. The session ran it 40 times.

When the tasks belong to one larger effort, a **[project](https://claude.com/blog/projects-redesigned)** (public beta for Pro and Max) runs a coordinator conversation that starts and tracks the cloud sessions for you. It then groups them by state: working, waiting on you, and ready for review.

### 2. Let it prove the fix

A flaky test is the clearest case of work that needs repeated proof: you have to run the suite again and again, and you don't want that loop tying up the machine you're working on. In the cloud, Claude patched the cache and ran the whole suite 40 times in one command.

![The flaky-test session's Bash step: a patch to src/cache.js that caches the in-flight promise, then a loop running the test suite 40 times, with output runs=40 fails=0.](https://claude.dev/media/6ce551ccd1a1cd64a0f9c0fb8b8116e1ca1e260a9f5de861de798e0fe578afe6.png)

**FIG G**Forty runs, zero failures: the flaky-test session's real command and output, replayed in the claude.ai/code interface running locally. Claude patched src/cache.js and looped the full suite 40 times in one step. Paths show under /home/user.

The VM has no compute charge and its CPU isn't yours, so ask for thorough proof. Run the suite 200 times, bisect a regression across 50 commits, run the slow integration tier, or start the app and hit it with curl the way the docs session did.

Each of Claude's turns still counts toward your plan, but a long test run inside one command costs little. [Foreground commands](https://code.claude.com/docs/en/cloud-environments) time out after 2 minutes by default (10 at most) and then keep running in the background for up to 30 more. You can raise the defaults with `BASH_DEFAULT_TIMEOUT_MS` and `BASH_MAX_TIMEOUT_MS` in the environment's variables.

### 3. Plan at your desk, build in the cloud, finish in your terminal

For a larger change, agree on the approach first where back-and-forth is cheap. Start Claude in plan mode, work out the plan together, commit the plan, and push it.

CODEShellCopy

```
claude --permission-mode plan
# ...agree on the plan, save it to docs/migration-plan.md, commit and push...
claude --cloud "Execute the migration plan in docs/migration-plan.md"
```

While the cloud session builds, your terminal is free for other work. When it's done, pull the session down to finish it by hand.

CODEShellCopy

```
claude --teleport            # pick a cloud session
claude --teleport <session-id>
```

Teleport checks that you're in the same repository, fetches the session's branch, checks it out, and loads the whole conversation into your terminal. You need a clean working tree (it offers to stash), and the branch has to be pushed. From inside Claude Code, `/teleport` (or `/tp`) opens the same picker, and `/tasks` then `t` works too. The Desktop app goes the other way, and its **Open in** menu sends a local session to the cloud.

### 4. Check in from your phone

The Code tab in the Claude app connects to the same sessions. From your phone you can start a task, follow it, steer it, answer a question Claude asked, or tell Claude to watch a pull request.

A phone suits questions you'd otherwise forget by the time you reach a keyboard. I gave a fourth session the kind of question you'd type on one: how does tidepool predict tides, and how could it go wrong at the edges of a time window? It ran code to check its answer and found a real bug. The loop never examines the first or last sample, so the API misses a high tide that falls exactly at the start of the window.

![Phone-width claude.ai/code showing the start of Claude's answer: predictTides has two edge problems, confirmed by running it, with a How it works section.](https://claude.dev/media/b07f3e2a23b519b872849b868c7ff83d07521d5e36a4fd7e9d4c0b0fb4f0701f.png)

**FIG H**A question asked from a phone: claude.ai/code at phone width in a browser (not the native app), running locally and replaying the fourth session's real answer

![The end of the answer: a table of how often reported highs and lows had an equal-height neighbour per station, and the proposed fix.](https://claude.dev/media/350260c5c66006b458f3f1512cf039933643e404080ac8aaa8c0451b23374d51.png)

**FIG I**Claude checked each claim by running code against the sample data and changed no files

### 5. Hand CI failures and review comments to Claude

With the Claude GitHub App installed on a repository, a cloud session can watch a pull request and act on what happens to it. From the CI bar in a session at claude.ai/code, turn on **Auto-fix**. You can also run `/autofix-pr` on the PR branch in your terminal, ask the mobile app to watch the PR, or paste the PR URL into a session.

Claude pushes clear fixes for failing checks and review comments, and explains what it changed. It asks you about anything ambiguous or architectural. Replies on review threads post under your GitHub username, labeled as Claude Code. Claude doesn't get notified about merge conflicts with the base branch, so ask it to rebase. Its comments can also trigger comment-driven automation such as Atlantis.

### 6. Start work without starting it yourself

A **routine** (research preview) is several saved resources designed to accomplish a task, such as a prompt, repositories, connectors, and an environment. Each run is a cloud session, started by a trigger. Triggers can be a schedule (hourly at most often), an HTTP call to the routine's own endpoint, or a GitHub event such as a pull request opening or a release. Create one at claude.ai/code/routines, in the Desktop app, or with `/schedule` in the CLI. Routines run without approval prompts, and by default they push to `claude/`-prefixed branches.

Two smaller tools help here. You can queue a follow-up into a running session from any machine where you're logged in, including a CI job.

CODEShellCopy

```
claude -p "The integration tier is green now; rebase on main and push" --cloud <session-id>
```

You can also bookmark a prefilled session. A URL such as `claude.ai/code?prompt=Triage+the+newest+issues&repositories=acme-labs/tidepool` opens claude.ai/code with the prompt and repository already filled in.

### 7. Run code you don't fully trust

A contributor's pull request, a new dependency's install script, or a repository you cloned five minutes ago can all run code you haven't read. On your laptop, that code runs next to your SSH keys, your cloud CLI sessions and your browser profile. In a cloud session it runs in a disposable VM with none of those, a session-scoped GitHub credential, and a network you can narrow.

Set the environment's network access to **None** for the strictest run, or keep **Trusted**, which allows package registries, GitHub and the major cloud SDK hosts. Even at None, Claude Code still sends requests to the Anthropic API, so data can leave the VM that way, and the session can still push to its own branch. All outbound traffic passes through a proxy that logs hostnames.

## CONNECTING GITHUB WITHOUT GETTING STUCK

If your first cloud session goes wrong, GitHub is the most likely reason. Most problems come from cloud sessions needing two separate GitHub permissions.

* **Signing in with GitHub** tells Claude who you are.
* **Installing the Claude GitHub App** on an account or organization sets which private repositories Claude can see there.

Public repositories work with the first alone. Private repositories need the second, on whichever account or organization owns them. If you connected GitHub and a private repository is missing, the App usually isn't installed on the account or organization that owns it.

| What you've connected | Public repos | Your private repos | An org's private repos | Auto-fix, GitHub triggers, projects |
| --- | --- | --- | --- | --- |
| Signed in with GitHub only | Yes | No | No | No |
| + App on your personal account | Yes | Yes | No | Your repos |
| + App on the organization (owner approves) | Yes | Only if also on your account | Yes | Org repos |
| `/web-setup` (your `gh` token) | Yes | Yes | Whatever your token can reach | No, needs the App |

### Path A: connect in the browser (recommended)

Connect your GitHub account at [claude.ai/connect-github](https://claude.ai/connect-github), then install the Claude GitHub App on the account or organization that owns your repository. For an organization, an owner usually has to approve the install. The [quickstart](https://code.claude.com/docs/en/web-quickstart) walks through each step.

![The Code with Claude anywhere screen with a Connect to GitHub button.](https://claude.dev/media/ff85ccc8f6a5ae3f2212014490ad5850c9bdb622908e85b8e33a8177cfc18942.png)

**FIG J**Step 1, sign in with GitHub. The claude.ai/code onboarding screens, running locally with sample data; the repository names in the illustrations and the Research preview chip are part of the product's own artwork.

![The Connect your repositories screen asking you to install the Claude GitHub App on your repositories, with Skip and Connect repositories buttons.](https://claude.dev/media/84004dce66bdcb7f9b4529e584e715f5d6e3d3930409689ca48df28aac45e685.png)

**FIG K**Step 2, install the Claude GitHub App

If GitHub doesn't send you back to claude.ai/code, the connect page at [claude.ai/connect-github](https://claude.ai/connect-github) can show a short checklist for the usual causes. One of them is the single sign-on step, which hides an organization's repositories if you skip it.

![The Didn't finish connecting screen with five tips: sign in to the right GitHub account, authorize each organization on the single sign-on step, start again if you saw GitHub connection not completed, connect your own account first and let an owner approve organization access later, or run /web-setup from the terminal.](https://claude.dev/media/0855b55ac62191f9b92cd9f5f1d5ab2d8181b03eb155678dd859cc7c8f8722ed.png)

**FIG L**If GitHub doesn't send you back: the product's own checklist for an interrupted GitHub connection, from the quick-setup onboarding flow in the claude.ai/code interface running locally

Auto-fix, GitHub-triggered routines and projects also depend on the App, so install it even if you connect another way.

### Path B: connect from your terminal with /web-setup

If you already use the `gh` CLI, run `/web-setup` inside Claude Code to send your `gh` token to your Claude account. Sessions can then reach any repository that token can, with or without the App. See [Connect from your terminal](https://code.claude.com/docs/en/web-quickstart#connect-from-your-terminal) for the walkthrough. On Team and Enterprise plans, an owner has to turn on [Quick setup](https://code.claude.com/docs/en/claude-code-on-the-web#quick-setup-for-team-and-enterprise) first.

### Path C: skip GitHub for a one-off

Run `claude --cloud` in a repository that has no GitHub remote, or one where the App isn't installed, and Claude Code uploads a bundle of your repository instead of cloning it. The session can push back only if your GitHub connection has push access to that repository. The docs list [what the bundle includes and leaves out](https://code.claude.com/docs/en/claude-code-on-the-web#send-local-repositories-without-github).

### If you run Team or Enterprise

An owner has a short checklist: turn on the GitHub connector at [claude.ai/admin-settings/connectors](https://claude.ai/admin-settings/connectors), allow cloud sessions in the [Claude Code admin settings](https://claude.ai/admin-settings/claude-code), install the Claude GitHub App on the organization's repositories (or approve members' requests), and decide whether to turn on [Quick setup](https://code.claude.com/docs/en/claude-code-on-the-web#quick-setup-for-team-and-enterprise). Organizations with IP allowlists or GitHub Enterprise Server have an extra step. See the docs on [IP allowlists](https://code.claude.com/docs/en/claude-code-on-the-web#limitations) and [GitHub Enterprise Server](https://code.claude.com/docs/en/github-enterprise-server).

### When it still doesn't work

| What you see | Why | Fix |
| --- | --- | --- |
| A private repository is missing from the picker | The App isn't installed on the account or organization that owns it, or its repository access excludes it | Install the App there, or add the repository to the App's Repository access in your GitHub settings |
| An error saying you must be an owner of the organization to link it | The organization blocked a membership check, usually because of a pending App permission request, an IP allow list, or SAML single sign-on | An owner accepts the pending permission request in the organization's GitHub App settings, turns on IP allow list inheritance for installed GitHub Apps, or (under SAML) grants Claude access to the organization |
| An organization's repositories are missing right after you connect | The organization uses SAML single sign-on, and its authorization step was skipped | On GitHub's "Single sign-on to your organizations" step, click **Authorize** next to each organization before you continue. If you already skipped it, authorize Claude for that organization in your GitHub settings, then reconnect |
| Every cloud session fails with an authentication error | Your Claude organization uses IP allowlisting | Ask support to exempt Anthropic-hosted services |

For anything else, see [troubleshooting](https://code.claude.com/docs/en/claude-code-on-the-web#troubleshooting) in the docs, including [no repositories appearing after you connect GitHub](https://code.claude.com/docs/en/web-quickstart#no-repositories-appear-after-connecting-github). To disconnect GitHub entirely, use claude.ai/customize/connectors.

## GIVE SESSIONS WHAT THEY NEED TO CHECK THEIR OWN WORK

A session that can run your tests checks its own work before it hands the work back. Without that, you review changes nobody has run. Most of the value in this guide's demos came from Claude running things: the suite 40 times, the server and its curls, the tide calculation at the window's edge. Ten minutes of environment setup gives Claude a way to run those checks.

![The Add cloud environment dialog with the name tidepool, Trusted network access, LOG_LEVEL=debug, and a setup script that installs shellcheck with apt-get.](https://claude.dev/media/aba93ba97b08d40ee9705338d22e861ed592cc8a7e32b8ddd715b6545b3c4fcd.png)

**FIG M**Adding a cloud environment in the claude.ai/code interface, running locally with sample values: a name, a network access level, variables in .env format, and a setup script

* **Start with the Default environment.** It uses Trusted network access, no variables and no setup script, which is enough for most JavaScript, Python, Go and Rust repositories.
* **Use a setup script for the machine.** It runs as root before Claude Code starts, so `apt install` works. It must exit 0 or the session won't start, and it should finish within about five minutes so the environment gets cached. After that, new sessions start from a snapshot with your tools on disk. The cache rebuilds when you change the script or the allowed hosts, and about every seven days.
* **Use a SessionStart hook for the project.** Put `npm install` and similar steps in a hook in the repository's `.claude/settings.json`, so they run the same way locally and in the cloud. Check `CLAUDE_CODE_REMOTE` if a step should run only in the cloud. Repository hooks load in single-repository sessions.
* **Start services per session.** The cache stores files. Processes that were running don't survive it. Ask Claude to run `service postgresql start`, or do it in a SessionStart hook.
* **Pick the narrowest network level that works.** Trusted covers the common registries. Use Custom to add a private registry, and Full only when the task needs the open internet. Changes reach running sessions within about a minute.
* **Keep secrets out of shared variables.** Environment variables are visible to anyone who uses the environment. On Pro and Max, an environment's API credentials attach a key to requests for the hosts you name, outside the VM, so the key never sits in a variable.
* **Put the commands in CLAUDE.md.** Your personal `~/.claude` doesn't reach the cloud VM. If Claude needs to know how to run the integration tests, the repository has to say so.

## HABITS THAT PAY OFF

* **One task, one session.** Small, separate sessions are easier to review and cheaper to throw away.
* **Ask for evidence.** Name the command that proves the task is done, and read Claude's summary before the diff.
* **Push before `claude --cloud`.** The VM clones from GitHub, so unpushed commits don't reach it.
* **Commit as you go on long tasks.** Idle VMs can be reclaimed.
* **Review in the diff view.** Inline comments are batched into your next message, and **Create PR** can open a full PR, a draft, or GitHub's compose page.
* **Steer while Claude works.** Messages you send while Claude works queue up, and you can take a queued one back.
* **Share the session.** On Team and Enterprise, set a session's visibility to Team so a reviewer can read how the change was made. Commits from cloud sessions carry a `Claude-Session` trailer that links back to the transcript.
* **Watch your limits.** Parallel sessions draw on your plan limits in parallel, so five sessions use them about five times as fast as one. Routines have their own hourly caps, and [projects](https://code.claude.com/docs/en/claude-projects) can start up to 200 new threads a day.

## COMMON QUESTIONS

**Who can use cloud sessions?** Pro, Max, and Team plans, and Enterprise users with a premium seat or a Chat + Claude Code seat, signed in with a claude.ai account. They aren't available with a Console API key or a third-party provider. See the [cloud sessions docs](https://code.claude.com/docs/en/claude-code-on-the-web).

**Where does my data go?** Anthropic stores the session transcript, and how long it's kept depends on your plan and model-improvement setting. VMs are reclaimed after inactivity, and deleting a session removes its data. See [data usage](https://code.claude.com/docs/en/data-usage) and [security](https://code.claude.com/docs/en/security).

**Will Claude train on my cloud sessions data?** Cloud sessions follow the same policy as the rest of Claude Code. On Team, Enterprise, and the API, Anthropic doesn't train models on your code or prompts unless your organization opts in. On Free, Pro, and Max, it depends on your [model-improvement setting](https://claude.ai/settings/data-privacy-controls). See [data usage](https://code.claude.com/docs/en/data-usage).

**Will it handle my large repository?** The VM has about 4 vCPUs, 16 GB of RAM, and 30 GB of disk. Put heavy installs in a [setup script](https://code.claude.com/docs/en/cloud-environments#setup-scripts) so they run once and land in the cached snapshot.

**What about GitLab or Bitbucket?** `claude --cloud` can upload a bundle from any git repository, but the session can't push back to those hosts. [GitHub Enterprise Server](https://code.claude.com/docs/en/github-enterprise-server) is supported on Team and Enterprise. See the [platform restrictions](https://code.claude.com/docs/en/claude-code-on-the-web#limitations).

**What happens when parallel branches conflict?** The sessions don't know about each other. Merge one branch, then [send the next session a follow-up](https://code.claude.com/docs/en/claude-code-on-the-web#send-follow-ups-from-the-cli) such as `claude -p "rebase on main and fix any conflicts" --cloud <session-id>`.

**Will I lose my local tools?** User-level config doesn't travel, so move what the team needs into the repository: commit skills and commands under `.claude/`, add project-scoped MCP servers to `.mcp.json`, and document test commands in `CLAUDE.md`. [Settings in cloud sessions](https://code.claude.com/docs/en/settings#settings-in-cloud-sessions) lists what each session reads.

## START IN FIVE MINUTES

Setup takes about five minutes. After that, you can hand off a task, close your laptop, and come back to a branch that's ready for review.

1. Open claude.ai/code, or run `/login` in Claude Code with your claude.ai account.
2. Connect GitHub and install the Claude GitHub App where your repository lives.
3. Pick the repository and the Default environment.
4. Give Claude one task from your backlog, with a command that proves it's done.
5. Close the tab. Check in from your phone later, then review the diff and create the pull request at claude.ai/code.

[Oct 01, 2026Getting started with Claude Code mods11 min](https://claude.dev/blog/getting-started-with-claude-code-mods/)[Sep 28, 2026Automating eval design and hillclimbing with Claude12 min](https://claude.dev/blog/automating-eval-design-and-hillclimbing/)[Sep 28, 2026Building with Claude Sonnet 5.59 min](https://claude.dev/blog/building-with-claude-sonnet-5-5/)[Sep 25, 2026Using Claude Code: Spending your effort8 min](https://claude.dev/blog/spending-your-effort/)[Sep 25, 2026What a task costs on Opus 5.521 min](https://claude.dev/blog/what-a-task-costs-on-opus-5-5/)
